# Budget and Milestones

## Proposed grant request

Project: Fediverse Portability Test Kit

Fund: NGI Fediversity

Requested amount: EUR 40,000

Repository: https://github.com/safal207/fediverse-portability-test-kit

## Budget summary

- Runnable report skeleton, schema validation, and CLI hardening: EUR 6,000
- Fixture dataset and comparison engine: EUR 10,000
- Check catalog expansion and CI-grade validation: EUR 8,000
- Adapter interface and Mastodon-style experimental path: EUR 8,000
- Documentation, public report/badge model, compatibility matrix, and community feedback: EUR 8,000
- Total: EUR 40,000

## Current pre-grant baseline

The repository already contains a first runnable local fixture CLI and reviewer-facing skeleton:

- CLI command: `fediverse-portability-test run --fixture mastodon-like`;
- JSON report generation;
- human-readable CLI summary;
- report schema v0.1;
- sample report;
- unit tests;
- schema validation test;
- GitHub Actions workflow;
- initial documentation for reviewers, operators, CI usage, badge model, and user benefit.

The grant work will turn this baseline into a more complete QA toolkit with real fixture data, comparison logic, adapter boundary, and community-reviewed documentation.

## Milestone 1 — Runnable report skeleton and schema validation

Duration: 1 month

Budget: EUR 6,000

Deliverables:

- hardened CLI command for local fixture runs;
- JSON report schema v0.1;
- generated report validation against schema;
- human-readable summary;
- stable exit code policy;
- check catalog v0.1;
- reviewer quick path.

Acceptance checks:

- reviewer can install the package locally;
- reviewer can run one command;
- report is generated;
- generated report validates against schema;
- PASS, FAIL, PARTIAL, and SKIP are documented;
- limitations of the synthetic fixture are explicit.

## Milestone 2 — Fixture dataset and comparison engine

Duration: 2 months

Budget: EUR 10,000

Deliverables:

- local Mastodon-like fixture dataset;
- controlled public/private/followers-only post data;
- media attachment fixtures;
- deleted-content markers;
- follower/following graph fixtures;
- expected-vs-actual comparison engine;
- digest comparison for media files.

Acceptance checks:

- fixture can create controlled test data;
- export/import roundtrip can be simulated through structured data;
- comparison engine produces check results;
- private, deleted, media, and relationship cases are represented;
- evidence fields are included in report output.

## Milestone 3 — Check expansion and CI-grade validation

Duration: 1 month

Budget: EUR 8,000

Deliverables:

- expanded check catalog;
- stricter CLI modes, such as fail-on-partial;
- CI integration examples;
- compatibility matrix template;
- report examples for PASS, PARTIAL, FAIL, and SKIP cases;
- developer documentation for adding new checks.

Acceptance checks:

- tests pass in GitHub Actions;
- CI can fail on real failed checks;
- partial results remain visible and are not hidden as success;
- adding a new check is documented;
- reports remain schema-valid.

## Milestone 4 — Adapter interface and Mastodon-style experimental path

Duration: 2 months

Budget: EUR 8,000

Deliverables:

- documented adapter interface;
- service metadata model;
- safe test-account procedure;
- Mastodon-style experimental adapter notes;
- privacy and cleanup guidelines;
- explicit unsupported-check behavior.

Acceptance checks:

- adapter boundary is clear;
- tests default to safe fixtures;
- real-service integration path is documented;
- unsupported checks are reported as SKIP or PARTIAL;
- project does not claim production certification.

## Milestone 5 — Public report model, documentation, and community feedback

Duration: 1 month

Budget: EUR 8,000

Deliverables:

- server-operator guide;
- developer CI guide;
- user benefit model;
- public badge/report model;
- compatibility matrix template;
- final reviewer report;
- public feedback collection through issues or documentation.

Acceptance checks:

- server operator can understand how to run the tool;
- developer can understand how to integrate it into CI;
- ordinary user benefit is explained without requiring users to run the CLI;
- reviewer can understand what is validated and what remains future work;
- feedback is captured publicly.

## Timeline

Month 1: runnable report skeleton, schema validation, and check catalog

Months 2-3: fixture dataset and comparison engine

Month 4: check expansion and CI-grade validation

Months 5-6: adapter interface and Mastodon-style experimental path

Month 7: public report model, documentation, and community feedback

## Public outputs

The grant will produce source code, CLI runner, fixture dataset, comparison engine, report schema, sample reports, check catalog, adapter interface, documentation, compatibility matrix template, public report model, and reviewer report.

## Success definition

The project is successful if an independent reviewer can clone the repository, run a local portability fixture, generate a schema-valid report, inspect PASS/FAIL/PARTIAL/SKIP results, understand how the approach can be adapted to real federated services, and see how the output can help ordinary users evaluate migration risk.
