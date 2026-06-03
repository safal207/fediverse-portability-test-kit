"""Synthetic Mastodon-like fixture checks.

This fixture does not claim compatibility with real Mastodon servers yet.
It gives reviewers and developers a runnable local proof of the report model.
"""

from __future__ import annotations


def build_checks() -> list[dict[str, object]]:
    """Return deterministic checks for the first local MVP fixture."""

    return [
        {
            "id": "export_available",
            "result": "PASS",
            "description": "The fixture account export can be produced and parsed.",
            "expected": "Export archive exists and is readable.",
            "actual": "Fixture export archive parsed successfully.",
        },
        {
            "id": "public_posts_preserved",
            "result": "PASS",
            "description": "Public posts survive export/import roundtrip.",
            "expected": "10 public posts restored.",
            "actual": "10 public posts restored.",
        },
        {
            "id": "media_integrity",
            "result": "PASS",
            "description": "Media files survive export/import roundtrip with matching digests.",
            "expected": "5 media attachments restored with matching hashes.",
            "actual": "5 media attachments restored with matching hashes.",
        },
        {
            "id": "private_visibility_preserved",
            "result": "PASS",
            "description": "Private and followers-only posts do not become public after restore.",
            "expected": "Private visibility labels preserved.",
            "actual": "Private visibility labels preserved.",
        },
        {
            "id": "deleted_content_not_restored",
            "result": "PASS",
            "description": "Deleted content does not reappear after import.",
            "expected": "Deleted post marker remains deleted.",
            "actual": "Deleted post marker remains deleted.",
        },
        {
            "id": "follower_graph_preserved",
            "result": "PARTIAL",
            "description": "Follower/following relationships are preserved or reported as partial.",
            "expected": "5 followers and 4 following relationships restored.",
            "actual": "5 followers restored; following relationships require manual confirmation.",
            "reproduction": "Run export_import_roundtrip with the mastodon-like fixture and inspect relationship comparison output.",
        },
    ]
