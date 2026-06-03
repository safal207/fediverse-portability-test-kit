import unittest

from fediverse_portability_test.report import build_fixture_report


class ReportShapeTest(unittest.TestCase):
    def test_fixture_report_has_required_schema_fields(self):
        report = build_fixture_report()

        for field in ["schema_version", "tool", "service", "scenario", "overall_result", "checks"]:
            self.assertIn(field, report)

        self.assertEqual(report["schema_version"], "0.1")
        self.assertEqual(report["tool"]["name"], "fediverse-portability-test-kit")
        self.assertEqual(report["service"]["type"], "local-fixture")
        self.assertEqual(report["overall_result"], "PARTIAL")
        self.assertEqual(
            report["summary"],
            {
                "passed": 5,
                "failed": 0,
                "partial": 1,
                "skipped": 0,
            },
        )

    def test_fixture_report_checks_have_required_fields(self):
        report = build_fixture_report()

        for check in report["checks"]:
            self.assertIn("id", check)
            self.assertIn("result", check)
            self.assertIn("description", check)
            self.assertIn(check["result"], {"PASS", "FAIL", "PARTIAL", "SKIP"})


if __name__ == "__main__":
    unittest.main()
