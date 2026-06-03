"""Command line interface for the first runnable MVP."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .report import build_fixture_report, render_summary, write_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fediverse-portability-test",
        description="Run local Fediverse portability QA checks and generate a JSON report.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    run = subcommands.add_parser("run", help="Run portability checks")
    run.add_argument(
        "--fixture",
        default="mastodon-like",
        choices=["mastodon-like"],
        help="Synthetic local fixture to run. Real service adapters are planned, not claimed yet.",
    )
    run.add_argument(
        "--target",
        default=None,
        help="Optional service URL to include in the report metadata.",
    )
    run.add_argument(
        "--output",
        default="portability-report.json",
        help="Path to write the machine-readable JSON report.",
    )
    return parser


def run_command(args: argparse.Namespace) -> int:
    output_path = Path(args.output)
    report = build_fixture_report(fixture=args.fixture, target=args.target)
    write_report(report, output_path)
    print(render_summary(report, output_path))

    summary = report["summary"]
    # PARTIAL is still a successful command execution. FAIL returns non-zero.
    return 1 if summary["failed"] else 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        return run_command(args)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
