"""Run the synthetic commercial systems lab using only the Python standard library."""

import argparse
from collections import Counter
from contextlib import closing
from datetime import datetime, timedelta
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
from urllib.parse import urlsplit


EXAMPLES = Path(__file__).resolve().parent
TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})"
)
SOURCE_PREFIX = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def timestamp(value):
    if not isinstance(value, str) or not TIMESTAMP.fullmatch(value):
        raise ValueError(f"Expected an RFC 3339 timestamp with an offset, got {value!r}")
    return datetime.fromisoformat(value)


def is_text(value):
    return isinstance(value, str) and bool(value.strip())


def index_by_id(records):
    index = {}
    for record in records:
        record_id = record["id"]
        if not is_text(record_id) or record_id in index:
            raise ValueError(f"Invalid or repeated record ID: {record_id!r}")
        index[record_id] = record
    return index


def event_time(event):
    required = ("source", "id", "subject", "type")
    if event.get("specversion") != "1.0" or not all(
        is_text(event.get(field)) for field in required
    ):
        raise ValueError("Events require specversion 1.0, source, id, subject, and type")
    if not SOURCE_PREFIX.match(event["source"]) or any(
        char.isspace() for char in event["source"]
    ):
        raise ValueError(f"Expected an absolute event source URI, got {event['source']!r}")
    return timestamp(event.get("time"))


def routing_decision(event, account, actions, age, max_age):
    if age < timedelta(0):
        return "manual_review", "future_event"
    if age > max_age:
        return "skipped", "stale_event"
    if account is None:
        return "manual_review", "unknown_account"
    if account.get("suppressed") is True:
        return "blocked", "account_suppressed"
    if account.get("suppressed") is not False:
        return "manual_review", "suppression_unknown"
    if event["type"] not in actions:
        return "manual_review", "unsupported_event_type"
    if not is_text(account.get("owner")) or not is_text(account.get("crm_company_id")):
        return "manual_review", "missing_owner_or_crm_id"
    return "proposed", "eligible"


def routing(data, policy):
    accounts = index_by_id(data["accounts"])
    as_of = timestamp(policy["as_of"])
    max_age = timedelta(hours=policy["max_signal_age_hours"])
    actions = policy["routing_actions"]
    deliveries = data["deliveries"]
    duplicates = 0
    payload_conflicts = []

    with closing(sqlite3.connect(":memory:")) as db:
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        db.executescript("""
            CREATE TABLE decisions (
                source TEXT NOT NULL, event_id TEXT NOT NULL,
                account_id TEXT NOT NULL, decision TEXT NOT NULL, reason TEXT NOT NULL,
                fingerprint TEXT NOT NULL,
                PRIMARY KEY (source, event_id)
            );
            CREATE TABLE tasks (
                source TEXT NOT NULL, event_id TEXT NOT NULL, action TEXT NOT NULL,
                crm_company_id TEXT NOT NULL, owner TEXT NOT NULL,
                PRIMARY KEY (source, event_id, action),
                FOREIGN KEY (source, event_id) REFERENCES decisions (source, event_id)
            );
        """)
        for event in deliveries:
            age = as_of - event_time(event)
            account = accounts.get(event["subject"])
            decision, reason = routing_decision(event, account, actions, age, max_age)
            key = (event["source"], event["id"])
            payload = json.dumps(event, sort_keys=True, separators=(",", ":"), allow_nan=False)
            fingerprint = sha256(payload.encode("utf-8")).hexdigest()
            with db:
                cursor = db.execute("""
                    INSERT INTO decisions VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT (source, event_id) DO NOTHING
                """, (*key, event["subject"], decision, reason, fingerprint))
                if cursor.rowcount == 0:
                    original = db.execute("""
                        SELECT fingerprint FROM decisions WHERE source = ? AND event_id = ?
                    """, key).fetchone()["fingerprint"]
                    if original == fingerprint:
                        duplicates += 1
                    else:
                        payload_conflicts.append({
                            "source": event["source"],
                            "event_id": event["id"],
                            "reason": "event_identity_reused",
                        })
                elif decision == "proposed":
                    db.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?)", (
                        *key, actions[event["type"]], account["crm_company_id"], account["owner"]
                    ))

        return {
            "deliveries": len(deliveries),
            "duplicates": duplicates,
            "payload_conflicts": payload_conflicts,
            "decisions": [dict(row) for row in db.execute("""
                SELECT source, event_id, account_id, decision, reason
                FROM decisions ORDER BY rowid
            """)],
            "tasks": [dict(row) for row in db.execute("SELECT * FROM tasks ORDER BY rowid")],
        }


def https_url(value):
    if not is_text(value) or any(char.isspace() for char in value):
        return False
    try:
        url = urlsplit(value)
        return url.scheme == "https" and bool(url.hostname) and url.username is None
    except ValueError:
        return False


def evidence_gate(proposal, evidence, as_of, max_age):
    evidence_ids = proposal["evidence_ids"]
    cited = [evidence.get(evidence_id) for evidence_id in evidence_ids]
    if not cited or any(item is None for item in cited):
        return "held", "missing_evidence"
    if any(
        item.get("subject") != proposal["subject"] or not https_url(item.get("source_url"))
        for item in cited
    ):
        return "held", "invalid_provenance"

    ages = [as_of - timestamp(item["retrieved_at"]) for item in cited]
    if any(age < timedelta(0) for age in ages):
        return "held", "future_evidence"
    fresh = [item["verdict"] for item, age in zip(cited, ages) if age <= max_age]
    if "contradicts" in fresh:
        return "held", "conflicting_evidence"
    if not fresh:
        return "held", "stale_evidence"
    if "supports" not in fresh:
        return "held", "no_supporting_evidence"
    return "eligible_for_review", "fresh_support"


def intelligence(data, policy):
    evidence = index_by_id(data["evidence"])
    as_of = timestamp(policy["as_of"])
    max_age = timedelta(days=policy["max_evidence_age_days"])
    results = []
    for proposal in index_by_id(data["proposals"]).values():
        status, reason = evidence_gate(proposal, evidence, as_of, max_age)
        results.append({**proposal, "status": status, "reason": reason})
    return results


def offer_issues(offer, policy, as_of):
    issues = []
    for field in ("product_id", "price_version"):
        if not is_text(offer.get(field)):
            issues.append(f"missing_{field}")
    amount = offer.get("amount_minor")
    if type(amount) is not int or amount < 0:
        issues.append("invalid_amount_minor")
    if offer.get("currency") not in policy["supported_currencies"]:
        issues.append("unsupported_currency")
    if offer.get("billing_period") not in policy["supported_billing_periods"]:
        issues.append("unsupported_billing_period")
    try:
        expires_at = timestamp(offer.get("expires_at"))
    except ValueError:
        issues.append("invalid_expiry")
    else:
        if expires_at <= as_of:
            issues.append("expired")
    if not https_url(offer.get("terms_url")):
        issues.append("invalid_terms_url")
    return issues


def offers(data, policy):
    as_of = timestamp(policy["as_of"])
    results = []
    for offer in index_by_id(data).values():
        issues = offer_issues(offer, policy, as_of)
        results.append({"id": offer["id"], "publishable": not issues, "issues": issues})
    return results


def measurement(data, policy):
    assigned = Counter()
    converted = Counter()
    seen = set()
    for record in data:
        group = record["group"]
        account = record["account_id"]
        if group not in ("control", "treatment") or not is_text(account) or account in seen:
            raise ValueError(f"Invalid or repeated assignment: {record!r}")
        if type(record["converted"]) is not bool:
            raise ValueError(f"Expected a known boolean outcome for {account}")
        seen.add(account)
        assigned[group] += 1
        converted[group] += record["converted"]

    if not assigned["control"] or not assigned["treatment"]:
        raise ValueError("Measurement requires accounts in both groups")
    rates = {group: Fraction(converted[group], count) for group, count in assigned.items()}
    lift = rates["treatment"] - rates["control"]
    incremental = lift * assigned["treatment"]
    assumptions = policy["measurement"]
    contribution = incremental * assumptions["contribution_per_conversion_minor"]
    cost = assumptions["workflow_cost_minor"]
    if cost <= 0:
        raise ValueError("ROI calculation requires a positive workflow cost")
    return {
        "groups": {
            group: {
                "assigned": assigned[group],
                "converted": converted[group],
                "conversion_rate": float(rates[group]),
            }
            for group in ("control", "treatment")
        },
        "absolute_lift_percentage_points": float(lift * 100),
        "illustrative_incremental_conversions": float(incremental),
        "currency": assumptions["currency"],
        "illustrative_incremental_contribution_minor": round(contribution),
        "workflow_cost_minor": cost,
        "illustrative_roi_percent": float((contribution - cost) / cost * 100),
    }


MODES = {
    "routing": routing,
    "intelligence": intelligence,
    "offers": offers,
    "measurement": measurement,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", nargs="?", choices=["all", *MODES], default="all")
    parser.add_argument("--fixtures", type=Path, default=EXAMPLES / "fixtures")
    parser.add_argument("--policy", type=Path, default=EXAMPLES / "config" / "policy.json")
    args = parser.parse_args()
    try:
        policy = read_json(args.policy)
        modes = MODES if args.mode == "all" else [args.mode]
        results = {
            mode: MODES[mode](read_json(args.fixtures / f"{mode}.json"), policy)
            for mode in modes
        }
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Lab input error: {exc}\n")
    print(json.dumps(results if args.mode == "all" else results[args.mode], indent=2))


if __name__ == "__main__":
    main()
