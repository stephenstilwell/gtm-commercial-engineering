"""Regression tests for review metadata, deduplication, and catalog generation."""

from copy import deepcopy
from datetime import date, timedelta
import unittest

from scripts import catalog


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.schema = catalog.read_json(catalog.SCHEMA)
        self.data = catalog.read_json(catalog.CATALOG)
        self.review_date = date.today()

    def validate(self):
        return catalog.validate(self.data, self.schema, as_of=self.review_date)

    def test_catalog_validates_and_generated_pages_are_current(self):
        self.assertEqual(self.validate(), [])
        entries = self.data["entries"]
        variants = (
            (catalog.SOFTWARE_PAGE, "software", catalog.render_software),
            (catalog.LEARNING_PAGE, "learning", catalog.render_learning),
        )
        for path, kind, render in variants:
            with self.subTest(page=path):
                generated = render([entry for entry in entries if entry["kind"] == kind])
                self.assertEqual((catalog.DOCS / path).read_text(encoding="utf-8"), generated)

    def test_reused_id_name_and_canonical_url_are_rejected(self):
        duplicate = deepcopy(self.data["entries"][0])
        duplicate["official_url"] += "/"
        self.data["entries"].append(duplicate)
        checks = "\n".join(self.validate())
        for message in ("duplicate id", "duplicate name", "duplicate URL"):
            self.assertIn(message, checks)

    def test_same_repository_cannot_be_relisted_under_an_alias(self):
        original = next(item for item in self.data["entries"] if item["id"] == "node-red")
        duplicate = deepcopy(original)
        duplicate.update(
            id="duplicate-runtime",
            name="Duplicate Runtime",
            official_url="https://example.org/runtime",
            repository_url=original["repository_url"].upper().replace("HTTPS://", "https://www.") + ".git",
        )
        self.data["entries"].append(duplicate)
        self.assertIn("duplicate URL", "\n".join(self.validate()))

    def test_open_source_requires_license_and_osi_evidence(self):
        entry = next(item for item in self.data["entries"] if item["classification"] == "open-source")
        del entry["license"]["osi_source"]
        self.assertIn("'osi_source' is a required property", "\n".join(self.validate()))
        del entry["license"]
        self.assertIn("'license' is a required property", "\n".join(self.validate()))

    def test_missing_metadata_and_invalid_dates_fail_validation(self):
        entry = self.data["entries"][0]
        del entry["cost"]["model"]
        entry["reviewed_on"] = "2026-02-30"
        checks = "\n".join(self.validate())
        self.assertIn("'model' is a required property", checks)
        self.assertIn("is not a 'date'", checks)

    def test_invalid_guide_and_future_review_fail_validation(self):
        entry = self.data["entries"][0]
        entry["guide"] = "missing-guide.md"
        entry["reviewed_on"] = (self.review_date + timedelta(days=1)).isoformat()
        checks = "\n".join(self.validate())
        self.assertIn("expected an existing handbook guide", checks)
        self.assertIn("reviewed_on is in the future", checks)

    def test_duplicate_json_object_key_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Repeated JSON key"):
            catalog.unique_keys([("name", "current"), ("name", "duplicate")])


if __name__ == "__main__":
    unittest.main()
