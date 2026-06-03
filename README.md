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

## Who runs this, and who benefits?

Ordinary users are not expected to run this test kit themselves.

The first users of the tool are:

- Fediverse server administrators;
- Fediverse software developers;
- public-interest organizations;
- reviewers and researchers evaluating real portability.

The end beneficiary is the ordinary user.

A server operator runs the test kit and publishes a report or badge:

```text
Portability checked: PASS / PARTIAL / FAIL
```

A user can then inspect the report before joining a server or migrating away from one:

- Can I export my data?
- Can I import it elsewhere?
- Will media survive?
- Will private posts stay private?
- Will deleted content remain deleted?
- Will follower/following relationships be preserved?

This project is not a migration service.

It is an open-source QA test suite that checks whether the road for migration is safe.

## What this project does

The first version provides or targets:

- reproducible local portability fixtures;
- an adapter interface for Fediverse-style services;
- export/import roundtrip checks;
- media integrity checks;
- private/followers-only visibility checks;
- deleted-content safety checks;
- follower/following graph checks;
- JSON report schema;
- human-readable report format;
- runnable CLI runner for a local synthetic fixture;
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
2. Read [`docs/USER_BENEFIT_MODEL.md`](docs/USER_BENEFIT_MODEL.md).
3. Read [`docs/FEDIVERSITY_ALIGNMENT.md`](docs/FEDIVERSITY_ALIGNMENT.md).
4. Read [`docs/PORTABILITY_TEST_MODEL.md`](docs/PORTABILITY_TEST_MODEL.md).
5. Inspect [`schemas/portability-report.schema.json`](schemas/portability-report.schema.json).
6. Run the local fixture and inspect the generated report.
7. Read [`docs/BUDGET_AND_MILESTONES.md`](docs/BUDGET_AND_MILESTONES.md).

## Install and run the local fixture

The current runnable scope is a synthetic local fixture. It does not claim real Mastodon compatibility yet.

```bash
python -m pip install -e .
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
Report: portability-report.json
```

The command exits with:

- `0` when the run completes without failed checks, including `PARTIAL` evidence;
- `1` when at least one check fails;
- `2` for command usage errors.

## Example report shape

```json
{
  "schema_version": "0.1",
  "tool": {
    "name": "fediverse-portability-test-kit",
    "version": "0.1.0-dev"
  },
  "service": {
    "name": "mastodon-like-fixture",
    "type": "local-fixture"
  },
  "scenario": "export_import_roundtrip",
  "overall_result": "PARTIAL",
  "checks": [
    {"id": "export_available", "result": "PASS", "description": "The fixture account export can be produced and parsed."},
    {"id": "media_integrity", "result": "PASS", "description": "Media files survive export/import roundtrip with matching digests."},
    {"id": "private_visibility_preserved", "result": "PASS", "description": "Private and followers-only posts do not become public after restore."},
    {"id": "follower_graph_preserved", "result": "PARTIAL", "description": "Follower/following relationships are preserved or reported as partial."}
  ]
}
```

## Service and badge model

A server can publish a public report summary such as:

```text
Portability checked: PARTIAL
Export: PASS
Import: PASS
Media restore: PASS
Private posts safety: PASS
Followers migration: PARTIAL
Deleted content handling: PASS
```

For details, see [`docs/BADGE_MODEL.md`](docs/BADGE_MODEL.md) and [`docs/SERVER_OPERATOR_GUIDE.md`](docs/SERVER_OPERATOR_GUIDE.md).

## Why this matters

A federated internet should let users leave safely.

If a server closes, becomes hostile, changes rules, breaks trust, or simply stops being the right home, the user should be able to export, migrate, restore, and validate their data.

This test kit asks the uncomfortable QA question:

> Does the move actually work?

## Project status

Early grant-preparation skeleton with a first runnable local fixture CLI.

No production real-service adapter is claimed yet.

The current repository defines the problem, reviewer path, test model, schema direction, grant milestones, and a minimal synthetic report generator.

## License

Apache-2.0
