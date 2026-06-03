import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class CliTest(unittest.TestCase):
    def test_cli_writes_report(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "report.json"

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "fediverse_portability_test.cli",
                    "run",
                    "--fixture",
                    "mastodon-like",
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("Overall: PARTIAL", completed.stdout)
            self.assertTrue(output.exists())

            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(report["overall_result"], "PARTIAL")
            self.assertEqual(report["summary"]["passed"], 5)
            self.assertEqual(report["summary"]["partial"], 1)

    def test_fail_on_partial_returns_non_zero_for_partial_report(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "report.json"

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "fediverse_portability_test.cli",
                    "run",
                    "--fixture",
                    "mastodon-like",
                    "--output",
                    str(output),
                    "--fail-on-partial",
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 1)
            self.assertIn("Overall: PARTIAL", completed.stdout)
            self.assertTrue(output.exists())


if __name__ == "__main__":
    unittest.main()
