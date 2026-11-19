"""Acceptance tests for the documented CLI and its synthetic datasets."""

from pathlib import Path
import subprocess
import sys
import unittest

from examples import gtm_lab as lab


ROOT = Path(__file__).resolve().parents[1]


class LabTests(unittest.TestCase):
    def setUp(self):
        self.policy = lab.read_json(lab.EXAMPLES / "config" / "policy.json")

    def fixture(self, name):
        return lab.read_json(lab.EXAMPLES / "fixtures" / f"{name}.json")

    def test_routing_outcomes_and_replay(self):
        data = self.fixture("routing")
        result = lab.routing(data, self.policy)
        self.assertEqual((result["deliveries"], result["duplicates"]), (7, 1))
        self.assertEqual(result["payload_conflicts"], [])
        self.assertEqual(len(result["decisions"]), 6)
        self.assertEqual(
            [task["action"] for task in result["tasks"]],
            ["review_demo_request", "review_onboarding_milestone"],
        )
        reasons = {row["event_id"]: row["reason"] for row in result["decisions"]}
        self.assertEqual(reasons["demo-202"], "account_suppressed")
        self.assertEqual(reasons["demo-old"], "stale_event")
        self.assertEqual(reasons["demo-303"], "missing_owner_or_crm_id")
        self.assertEqual(reasons["demo-999"], "unknown_account")
        data["deliveries"].append(dict(data["deliveries"][0]))
        replay = lab.routing(data, self.policy)
        self.assertEqual(replay["duplicates"], 2)
        self.assertEqual(replay["tasks"], result["tasks"])

    def test_same_event_id_from_a_second_source_is_distinct(self):
        data = self.fixture("routing")
        event = {**data["deliveries"][0], "source": "urn:synthetic:another-form"}
        data["deliveries"].append(event)
        result = lab.routing(data, self.policy)
        self.assertEqual(result["duplicates"], 1)
        self.assertEqual(len(result["tasks"]), 3)

    def test_changed_payload_for_the_same_identity_is_reported_and_held(self):
        data = self.fixture("routing")
        baseline = lab.routing(data, self.policy)
        first = data["deliveries"][0]
        data["deliveries"].append(dict(reversed(list(first.items()))))
        data["deliveries"].append({**first, "subject": "account-404"})

        result = lab.routing(data, self.policy)

        self.assertEqual(result["duplicates"], baseline["duplicates"] + 1)
        self.assertEqual(result["tasks"], baseline["tasks"])
        self.assertEqual(result["decisions"], baseline["decisions"])
        self.assertEqual(result["payload_conflicts"], [{
            "source": first["source"],
            "event_id": first["id"],
            "reason": "event_identity_reused",
        }])

    def test_missing_suppression_or_crm_identity_holds_tasks(self):
        data = self.fixture("routing")
        del data["accounts"][0]["crm_company_id"]
        del data["accounts"][3]["suppressed"]
        result = lab.routing(data, self.policy)
        self.assertEqual(result["tasks"], [])
        reasons = {row["event_id"]: row["reason"] for row in result["decisions"]}
        self.assertEqual(reasons["demo-101"], "missing_owner_or_crm_id")
        self.assertEqual(reasons["milestone-404"], "suppression_unknown")

    def test_evidence_freshness_conflict_and_missing_source(self):
        results = lab.intelligence(self.fixture("intelligence"), self.policy)
        self.assertEqual(
            [result["reason"] for result in results],
            ["fresh_support", "stale_evidence", "conflicting_evidence", "missing_evidence"],
        )
        self.assertEqual(
            [result["id"] for result in results if result["status"] == "eligible_for_review"],
            ["partner-review"],
        )

    def test_evidence_cannot_be_reassigned_to_another_subject(self):
        data = self.fixture("intelligence")
        data["proposals"][0]["subject"] = "different-subject"
        result = lab.intelligence(data, self.policy)[0]
        self.assertEqual((result["status"], result["reason"]), ("held", "invalid_provenance"))

    def test_offer_lint_detects_expiry_and_missing_terms(self):
        results = lab.offers(self.fixture("offers"), self.policy)
        self.assertTrue(results[0]["publishable"])
        self.assertFalse(results[1]["publishable"])
        self.assertEqual(results[1]["issues"], ["expired", "invalid_terms_url"])

    def test_measurement_value_and_duplicate_assignment(self):
        data = self.fixture("measurement")
        result = lab.measurement(data, self.policy)
        self.assertEqual(result["absolute_lift_percentage_points"], 25)
        self.assertEqual(result["illustrative_incremental_contribution_minor"], 20000)
        self.assertEqual(result["illustrative_roi_percent"], 100)
        data.append({**data[0], "group": "control"})
        with self.assertRaisesRegex(ValueError, "repeated assignment"):
            lab.measurement(data, self.policy)

    def test_default_cli_runs_the_four_modes(self):
        output = subprocess.check_output(
            [sys.executable, "examples/gtm_lab.py"], cwd=ROOT, text=True
        )
        for mode in lab.MODES:
            self.assertIn(f'"{mode}":', output)


if __name__ == "__main__":
    unittest.main()
