# Fediversity Reviewer Path

## Project

**Fediverse Portability Test Kit: Open QA Suite for Service Portability and Data Migration**

Repository: https://github.com/safal207/fediverse-portability-test-kit

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

1. Read this file.
2. Read `docs/FEDIVERSITY_ALIGNMENT.md`.
3. Read `docs/PORTABILITY_TEST_MODEL.md`.
4. Inspect `schemas/portability-report.schema.json`.
5. Inspect `examples/export-import-fixture/sample-report.json`.
6. Read `docs/BUDGET_AND_MILESTONES.md`.

## Current repository status

This repository is an early skeleton for a grant proposal.

It currently defines:

- the project problem;
- reviewer path;
- Fediversity alignment;
- portability test model;
- report schema;
- sample report;
- budget and milestones.

It does not yet claim a production runner, real-service adapters, or compliance certification.

## Target grant outcome

The grant will produce:

- CLI runner;
- local fixture tests;
- report schema v0.1;
- adapter interface;
- Mastodon-like fixture;
- export/import roundtrip tests;
- media and privacy checks;
- public documentation;
- compatibility matrix template;
- final reviewer report.

## Success criteria

A reviewer or developer should be able to:

- clone the repository;
- run a fixture-based test;
- generate a portability report;
- inspect PASS, FAIL, and PARTIAL results;
- understand how a real service adapter would connect;
- see how the test kit helps server operators improve portability.

## Non-goals

This project will not initially:

- migrate real users automatically;
- certify all Fediverse software;
- provide legal GDPR advice;
- replace existing service migration tools;
- perform production security audits;
- claim universal compatibility across all federated protocols.

## Project phrase

```text
We help federated services prove users can leave safely.
```
