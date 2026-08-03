# Fediversity Reviewer Path

## Project

**Fediverse Portability Test Kit: Open QA Suite for Service Portability and Data Migration**

Repository: https://github.com/safal207/fediverse-portability-test-kit

Application: `2026-08-012`

Requested amount: EUR 40,000

## One-sentence summary

Fediverse Portability Test Kit is an open-source QA suite that tests whether users can safely export, migrate, restore, and validate their data across federated and self-hosted services.

## Core reviewer question

```text
Can a user safely leave one server and move to another?
```

This project turns that question into reproducible tests, machine-readable reports, and reviewer-friendly evidence.

## Why this matters

Federated services promise autonomy, portability, and user control.

But portability can fail in practice:

- exported archives may be incomplete;
- media files may be lost;
- followers and following may not restore;
- private posts may become public;
- deleted content may reappear;
- blocked accounts may be forgotten;
- old links may break;
- backups may not restore cleanly.

This test kit focuses on the QA layer that detects those failures.

## Fit with NGI Fediversity

Fediversity is about practical, user-controlled, self-hosted and federated services.

A reusable portability test kit supports that mission by giving developers and server operators a way to verify whether service portability actually works.

The project contributes:

- reproducible export/import tests;
- report schema for portability evidence;
- privacy-preservation checks;
- fixture-based local validation;
- adapter model for real services;
- compatibility matrix roadmap;
- clear non-claims and limitations.

## Reviewer quick path

Start here:

1. Read [`GRANT_EVIDENCE_INDEX.md`](GRANT_EVIDENCE_INDEX.md).
2. Read this file.
3. Read [`FEDIVERSITY_ALIGNMENT.md`](FEDIVERSITY_ALIGNMENT.md).
4. Read [`PORTABILITY_TEST_MODEL.md`](PORTABILITY_TEST_MODEL.md).
5. Inspect [`../schemas/portability-report.schema.json`](../schemas/portability-report.schema.json).
6. Run the local fixture and inspect the generated report.
7. Read [`BUDGET_AND_MILESTONES.md`](BUDGET_AND_MILESTONES.md).

## Current repository status

The repository contains a runnable **synthetic local baseline**:

- installable Python package and CLI;
- `mastodon-like` local fixture;
- JSON report generation;
- report schema v0.1 and schema validation;
- human-readable summary;
- documented `PASS`, `PARTIAL`, `FAIL`, and `SKIP` semantics;
- strict `--fail-on-partial` mode;
- media, privacy, deleted-content, and relationship checks;
- CI workflow and unit tests;
- reviewer, operator, badge, and compatibility-matrix documentation.

The current baseline does **not** claim production Mastodon compatibility. Real-service adapters and broader comparison logic are grant-funded transitions.

## Reviewer command path

```bash
git clone https://github.com/safal207/fediverse-portability-test-kit.git
cd fediverse-portability-test-kit
python -m pip install -e .
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

Strict mode:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
```

Expected high-level story:

```text
controlled fixture
  -> export/import simulation
  -> check-level evidence
  -> schema-valid JSON report
  -> explicit PASS / PARTIAL / FAIL / SKIP
```

## Target grant outcome

The grant will turn the baseline into a broader QA toolkit with:

- stronger fixture datasets and comparison logic;
- an explicit service adapter interface;
- a safe experimental Mastodon-style path;
- expanded privacy, media, deletion, and relationship checks;
- CI integration examples;
- public evidence reports and compatibility matrix;
- community review and external feedback.

## Success criteria

A reviewer or developer should be able to:

- clone and run the repository from a clean environment;
- generate a schema-valid portability report;
- inspect positive, negative, partial, and unsupported outcomes;
- understand what is synthetic and what is real-service evidence;
- see how an adapter connects without unsafe production claims;
- understand how public evidence helps users evaluate migration risk.

## Non-goals

This project will not initially:

- migrate real users automatically;
- certify all Fediverse software;
- provide legal GDPR advice;
- replace existing service migration tools;
- perform production security audits;
- claim universal compatibility across all federated protocols.

## Temporal claim boundary

```text
implemented now:
  synthetic fixture + CLI + report schema + documented checks

grant-funded next:
  stronger comparison engine + safe adapter path + external validation

not claimed:
  universal production compatibility or certification
```

## Project phrase

```text
We help federated services prove users can leave safely.
```
