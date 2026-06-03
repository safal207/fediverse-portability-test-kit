# Roadmap to a Real-Service Adapter

## Current scope

The current repository contains a first runnable local synthetic fixture.

It does not claim real Mastodon, PeerTube, Lemmy, or generic ActivityPub compatibility yet.

The fixture exists to prove the report model, CLI shape, result states, and reviewer workflow.

## Phase 1 — Synthetic local fixture

Goal: make the project runnable and reviewable without touching any real server.

Deliverables:

- `fediverse-portability-test run --fixture mastodon-like`;
- deterministic check results;
- generated `portability-report.json`;
- schema validation;
- human-readable CLI summary.

Status: first minimal version exists.

## Phase 2 — Fixture dataset and comparison engine

Goal: move from hardcoded check outputs to a real controlled dataset and comparison layer.

Deliverables:

- fixture account model;
- public/private/followers-only posts;
- media attachment fixtures;
- deleted-content markers;
- follower/following graph fixture;
- digest comparison;
- expected-vs-actual comparison output.

## Phase 3 — Adapter boundary

Goal: define the interface that real services can implement.

Possible adapter methods:

```python
class PortabilityAdapter:
    def create_test_account(self): ...
    def seed_fixture_data(self, fixture): ...
    def export_account(self): ...
    def import_or_restore_account(self, archive): ...
    def fetch_restored_state(self): ...
    def cleanup(self): ...
```

Design principles:

- adapters must use dedicated test accounts;
- tests must not touch real user accounts;
- destructive behavior must be explicit and isolated;
- private-content checks must be safe by default;
- skipped and unsupported checks must be visible in the report.

## Phase 4 — Mastodon-style experimental path

Goal: document and prototype a first real-service path around Mastodon-style export/import behavior.

Deliverables:

- adapter notes;
- required permissions;
- safe test-account procedure;
- export archive assumptions;
- import/restore limitations;
- unsupported checks reported as `SKIP` or `PARTIAL`.

This phase should be experimental until maintainers or operators confirm the safe adapter boundary.

## Phase 5 — CI and operator workflows

Goal: make the test kit useful for developers and server administrators.

Deliverables:

- CI examples;
- stable exit code policy;
- machine-readable reports;
- public badge summary;
- compatibility matrix template;
- operator guide.

## Phase 6 — Public evidence layer

Goal: help ordinary users evaluate portability risk before joining or leaving a server.

Deliverables:

- report-to-badge summary;
- static public report example;
- historical report format;
- independent report publication guidance;
- limitations and non-certification language.

## Safety constraints

The project should avoid:

- testing on real user accounts;
- silently deleting or changing live data;
- claiming full compliance or certification;
- hiding partial or skipped checks;
- widening private visibility during tests;
- treating unsupported behavior as success.
