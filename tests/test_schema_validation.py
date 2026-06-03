import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from fediverse_portability_test.report import build_fixture_report


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "portability-report.schema.json"


class SchemaValidationTest(unittest.TestCase):
    def test_generated_fixture_report_validates_against_schema(self):
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        report = build_fixture_report()

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(report), key=lambda error: list(error.path))

        self.assertEqual(errors, [], [error.message for error in errors])


if __name__ == "__main__":
    unittest.main()
