"""Validate the curated catalog and render its two MkDocs views."""

import argparse
from collections import defaultdict
from datetime import date
import html
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "catalog.json"
SCHEMA = ROOT / "catalog" / "catalog.schema.json"
DOCS = ROOT / "docs"
SOFTWARE_PAGE = PurePosixPath("explore/catalog.md")
LEARNING_PAGE = PurePosixPath("learn/resources.md")
CLASSIFICATIONS = {
    "open-source": "Open-source software",
    "source-available": "Source-available software",
    "mixed-license": "Mixed-license software",
    "proprietary": "Proprietary software",
}


def title_id(value):
    plain = re.sub(r"[^a-z0-9\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", plain).strip("-")


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Repeated JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def canonical_url(value):
    parsed = urlsplit(value)
    hostname = parsed.hostname
    if parsed.scheme != "https" or not hostname or parsed.username or parsed.password:
        raise ValueError(f"Expected a public HTTPS reference without credentials: {value}")
    if "@" in parsed.netloc or parsed.port not in (None, 443):
        raise ValueError(f"Expected a canonical HTTPS reference: {value}")
    hostname = hostname.lower().removeprefix("www.")
    path = unquote(parsed.path).rstrip("/")
    if hostname == "github.com":
        path = path.lower().removesuffix(".git")
    return (hostname, path, parsed.query, parsed.fragment)


def entry_urls(entry):
    yield entry["official_url"]
    if "repository_url" in entry:
        yield entry["repository_url"]
    yield entry["cost"]["source"]
    yield entry["maintenance"]["source"]
    if "license" in entry:
        yield entry["license"]["source"]
        if "osi_source" in entry["license"]:
            yield entry["license"]["osi_source"]


def validate(data, schema, docs=DOCS, as_of=None):
    as_of = as_of or date.today()
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda error: error.json_path)
    ]
    if errors:
        return errors

    owners = {}
    for entry in data["entries"]:
        identifier = entry["id"]
        if identifier != title_id(entry["name"]):
            errors.append(f"{identifier}: expected the heading ID {title_id(entry['name'])!r}")
        identity = [
            ("id", identifier),
            ("name", " ".join(entry["name"].casefold().split())),
        ]
        try:
            for url in entry_urls(entry):
                canonical_url(url)
            identity.append(("URL", canonical_url(entry["official_url"])))
            if "repository_url" in entry:
                identity.append(("URL", canonical_url(entry["repository_url"])))
        except ValueError as error:
            errors.append(f"{identifier}: {error}")

        for key in dict.fromkeys(identity):
            if key in owners:
                errors.append(f"{identifier}: duplicate {key[0]} also used by {owners[key]}")
            owners[key] = identifier

        reviewed = date.fromisoformat(entry["reviewed_on"])
        if reviewed > as_of:
            errors.append(f"{identifier}: reviewed_on is in the future")
        maintenance = entry["maintenance"]
        if "observed_on" in maintenance:
            observed = date.fromisoformat(maintenance["observed_on"])
            if observed > reviewed:
                errors.append(f"{identifier}: activity is dated after the review")
            if maintenance["status"] == "Recent repository activity" and (reviewed - observed).days > 180:
                errors.append(f"{identifier}: activity was over 180 days old at review")

        guide = docs / entry["guide"]
        if not guide.is_file() or PurePosixPath(entry["guide"]) in (SOFTWARE_PAGE, LEARNING_PAGE):
            errors.append(f"{identifier}: expected an existing handbook guide: {entry['guide']}")
    return errors


def escape(value):
    value = html.escape(value, quote=False)
    return re.sub(r"([\\\x60*_\[\]\|])", r"\\\1", value).replace("\n", " ")


def link(label, url):
    return f"[{escape(label)}](<{url}>)"


def guide_link(entry, page):
    target = posixpath.relpath(entry["guide"], start=page.parent.as_posix())
    return link("Handbook exercise", target)


def entry_markdown(entry, page, heading):
    official_url = entry["official_url"]
    links = [link("Official resource", official_url)]
    if "repository_url" in entry and entry["repository_url"] != official_url:
        links.append(link("Public repository", entry["repository_url"]))
    links.append(guide_link(entry, page))
    cost = entry["cost"]
    activity = entry["maintenance"]
    status = escape(activity["status"])
    if "observed_on" in activity:
        status += f" ({activity['observed_on']})"
    lines = [
        f"{heading} {escape(entry['name'])}",
        "",
        escape(entry["problem"]),
        "",
        f"- **Publisher** {escape(entry['organization'])}",
        f"- **Category** {escape(entry['category'])}",
        f"- **Difficulty** {escape(entry['difficulty'])}",
        f"- **Access** {escape(cost['model'])}. {escape(cost['note'])} {link('Access evidence', cost['source'])}",
        f"- **Status** {status}. {link('Status evidence', activity['source'])}",
        f"- **Reviewed** {entry['reviewed_on']}",
    ]
    if "license" in entry:
        license_info = entry["license"]
        references = [link("License terms", license_info["source"])]
        if "osi_source" in license_info:
            references.append(link("OSI listing", license_info["osi_source"]))
        lines.append(
            f"- **License** {escape(license_info['name'])}. {escape(license_info['scope'])} "
            + " · ".join(references)
        )
    lines.extend(["", " · ".join(links), ""])
    return lines


def render_software(entries):
    grouped = defaultdict(list)
    for entry in entries:
        grouped[entry["classification"]].append(entry)
    lines = [
        "# Tool catalog",
        "",
        "<!-- Generated by scripts/catalog.py from catalog/catalog.json. -->",
        "",
        "Browse the [category index](index.md) or these four license views. "
        "Access and activity reflect the recorded review. A repository push indicates recent "
        "activity. Support commitments require separate confirmation.",
        "",
        " · ".join(f"[{label}](#{title_id(label)})" for label in CLASSIFICATIONS.values()),
        "",
        "## Browse by category",
        "",
        "| Category | Entries |",
        "| --- | --- |",
    ]
    by_category = defaultdict(list)
    for entry in sorted(entries, key=lambda value: value["name"].casefold()):
        by_category[entry["category"]].append(entry)
    for category, items in sorted(by_category.items()):
        anchors = " · ".join(f"[{escape(item['name'])}](#{item['id']})" for item in items)
        lines.append(f"| {escape(category)} | {anchors} |")
    for classification, label in CLASSIFICATIONS.items():
        lines.extend(["", f"## {label}", ""])
        if classification == "proprietary":
            lines.extend(["These entries describe hosted commercial products. Their software source license is outside the reviewed offering.", ""])
        for entry in sorted(grouped[classification], key=lambda value: value["name"].casefold()):
            lines.extend(entry_markdown(entry, SOFTWARE_PAGE, "###"))
    return "\n".join(lines)


def render_learning(entries):
    groups = defaultdict(list)
    for entry in sorted(entries, key=lambda value: value["name"].casefold()):
        groups[entry["category"]].append(entry)
    lines = [
        "# Learning resources",
        "",
        "<!-- Generated by scripts/catalog.py from catalog/catalog.json. -->",
        "",
        "Use these courses, communities, newsletters, and reference materials alongside the "
        "[learning roadmap](../roadmap.md). Difficulty describes what you need to apply the resource.",
        "",
    ]
    for category, items in sorted(groups.items()):
        lines.extend([f"## {escape(category)}", ""])
        for entry in items:
            lines.extend(entry_markdown(entry, LEARNING_PAGE, "###"))
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate and check generated Markdown")
    args = parser.parse_args()
    try:
        data = read_json(CATALOG)
        errors = validate(data, read_json(SCHEMA))
        if errors:
            raise ValueError("\n".join(errors))
        entries = data["entries"]
        pages = {
            SOFTWARE_PAGE: render_software([item for item in entries if item["kind"] == "software"]),
            LEARNING_PAGE: render_learning([item for item in entries if item["kind"] == "learning"]),
        }
        for relative_path, rendered in pages.items():
            target = DOCS / relative_path
            if args.check:
                if not target.exists() or target.read_text(encoding="utf-8") != rendered:
                    raise ValueError(f"Generated page is stale: {target.relative_to(ROOT)}. Run python scripts/catalog.py.")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(rendered, encoding="utf-8", newline="\n")
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    print(f"Validated {len(entries)} catalog entries and {len(pages)} generated pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
