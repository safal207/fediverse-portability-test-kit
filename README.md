# Fediverse Portability Test Kit

**Can a user safely leave one server and move to another?**

Fediverse Portability Test Kit is an open-source QA test suite for export, import, migration, restore, and privacy checks across federated and self-hosted services.

It is designed to test whether service portability is real in practice, not only promised in documentation.

## Core idea

```text
Portability is not a promise.
It should be tested.
```

The project checks whether user data can move between servers without losing content, media, relationships, privacy settings, blocked accounts, deleted-content state, or restore integrity.

## What this project does

The first version will provide:

- reproducible local portability fixtures;
- an adapter interface for Fediverse-style services;
- export/import roundtrip checks;
- media integrity checks;
- private/followers-only visibility checks;
- deleted-content safety checks;
- follower/following graph checks;
- JSON report schema;
- human-readable report format;
- CLI runner roadmap;
- Fediversity reviewer documentation.

## What this project is not

This project is not:

- a hosted migration service;
- a replacement for Mastodon, PeerTube, Lemmy, or other Fediverse software;
- a universal compliance certification;
- GDPR legal advice;
- a production security audit;
- a tool that moves real users automatically without operator review.

The narrow claim is stronger:

> This project provides open QA infrastructure for testing whether portability, export, import, and restore behavior work as expected.

## Reviewer quick path

Start here:

1. Read [`docs/FEDIVERSITY_REVIEWER_PATH.md`](docs/FEDIVERSITY_REVIEWER_PATH.md).
2. Read [`docs/FEDIVERSITY_ALIGNMENT.md`](docs/FEDIVERSITY_ALIGNMENT.md).
3. Read [`docs/PORTABILITY_TEST_MODEL.md`](docs/PORTABILITY_TEST_MODEL.md).
4. Inspect [`schemas/portability-report.schema.json`](schemas/portability-report.schema.json).
5. Inspect [`examples/export-import-fixture/sample-report.json`](examples/export-import-fixture/sample-report.json).
6. Read [`docs/BUDGET_AND_MILESTONES.md`](docs/BUDGET_AND_MILESTONES.md).

## Proposed CLI shape

The first implementation target is a local CLI command:

```bash
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

Example result:

```text
Export/import roundtrip: PASS
Media integrity: PASS
Private visibility: PASS
Deleted content safety: PASS
Follower graph: PARTIAL

Overall: PARTIAL
Report: ./portability-report.json
```

## Example report shape

```json
{
  "service": "mastodon-like-fixture",
  "scenario": "export_import_roundtrip",
  "overall_result": "PARTIAL",
  "checks": [
    {"id": "export_available", "result": "PASS"},
    {"id": "media_integrity", "result": "PASS"},
    {"id": "private_visibility_preserved", "result": "PASS"},
    {"id": "follower_graph_preserved", "result": "PARTIAL"}
  ]
}
```

## Why this matters

A federated internet should let users leave safely.

If a server closes, becomes hostile, changes rules, breaks trust, or simply stops being the right home, the user should be able to export, migrate, restore, and validate their data.

This test kit asks the uncomfortable QA question:

> Does the move actually work?

## Project status

Early grant-preparation skeleton.

No production test runner is claimed yet.

The current repository defines the problem, reviewer path, test model, schema direction, and grant milestones.

## License

Apache-2.0
