"""Report construction and rendering helpers."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

from . import __version__
from .fixtures.mastodon_like import build_checks

RESULTS = ("PASS", "FAIL", "PARTIAL", "SKIP")


def utc_now() -> str:
    """Return an ISO-8601 UTC timestamp with second precision."""

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def summarize(checks: Iterable[dict[str, object]]) -> dict[str, int]:
    """Count check results for the JSON summary block."""

    summary = {"passed": 0, "failed": 0, "partial": 0, "skipped": 0}
    mapping = {
        "PASS": "passed",
        "FAIL": "failed",
        "PARTIAL": "partial",
        "SKIP": "skipped",
    }
    for check in checks:
        result = str(check.get("result", "SKIP"))
        summary[mapping.get(result, "skipped")] += 1
    return summary


def overall_result(summary: dict[str, int]) -> str:
    """Derive the report-level result from check counts."""

    if summary["failed"] > 0:
        return "FAIL"
    if summary["partial"] > 0:
        return "PARTIAL"
    if summary["passed"] == 0 and summary["skipped"] > 0:
        return "SKIP"
    return "PASS"


def build_fixture_report(fixture: str = "mastodon-like", target: str | None = None) -> dict[str, object]:
    """Build the first deterministic local fixture report."""

    if fixture != "mastodon-like":
        raise ValueError(f"Unsupported fixture: {fixture}")

    started_at = utc_now()
    checks = build_checks()
    summary = summarize(checks)
    service: dict[str, object] = {
        "name": "mastodon-like-fixture",
        "type": "local-fixture",
        "version": "0.1",
    }
    if target:
        service["url"] = target

    return {
        "schema_version": "0.1",
        "tool": {
            "name": "fediverse-portability-test-kit",
            "version": __version__,
        },
        "service": service,
        "scenario": "export_import_roundtrip",
        "overall_result": overall_result(summary),
        "started_at": started_at,
        "finished_at": utc_now(),
        "summary": summary,
        "checks": checks,
        "notes": [
            "This is a synthetic fixture report for reviewer orientation.",
            "It does not claim real Mastodon compatibility yet.",
        ],
    }


def write_report(report: dict[str, object], output_path: Path) -> Path:
    """Write a report to disk as pretty-printed JSON."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output_path


def render_summary(report: dict[str, object], output_path: Path) -> str:
    """Render a compact human-readable CLI summary."""

    labels = {
        "export_available": "Export/import roundtrip",
        "media_integrity": "Media integrity",
        "private_visibility_preserved": "Private visibility",
        "deleted_content_not_restored": "Deleted content safety",
        "follower_graph_preserved": "Follower graph",
    }
    lines: list[str] = []
    for check in report["checks"]:  # type: ignore[index]
        check_id = str(check["id"])
        if check_id in labels:
            lines.append(f"{labels[check_id]}: {check['result']}")
    lines.append("")
    lines.append(f"Overall: {report['overall_result']}")
    lines.append(f"Report: {output_path}")
    return "\n".join(lines)
