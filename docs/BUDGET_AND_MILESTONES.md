# Budget and Milestones

## Proposed grant request

Project: Fediverse Portability Test Kit

Fund: NGI Fediversity

Requested amount: EUR 40,000

Repository: https://github.com/safal207/fediverse-portability-test-kit

## Budget summary

- CLI runner and fixture engine: EUR 12,000
- Report schema and validation: EUR 5,000
- Adapter interface and local fixtures: EUR 8,000
- Test scenarios and expected outputs: EUR 7,000
- Documentation and reviewer reports: EUR 5,000
- Community feedback and compatibility matrix: EUR 3,000
- Total: EUR 40,000

## Milestone 1 — Test model and report schema

Duration: 1 month

Budget: EUR 7,000

Deliverables:

- portability test model;
- JSON report schema v0.1;
- sample report;
- initial check catalog;
- reviewer path.

Acceptance checks:

- schema is public;
- sample report validates against schema;
- check IDs are documented;
- reviewer can understand PASS, FAIL, PARTIAL, and SKIP.

## Milestone 2 — Local fixture engine

Duration: 2 months

Budget: EUR 10,000

Deliverables:

- local mastodon-like fixture;
- controlled test account dataset;
- export simulation;
- import and restore simulation;
- comparison engine.

Acceptance checks:

- fixture can create controlled data;
- export/import roundtrip can be simulated;
- comparison produces a report;
- deleted/private/media cases are represented.

## Milestone 3 — CLI runner

Duration: 1 month

Budget: EUR 8,000

Deliverables:

- CLI command for running fixture tests;
- output to JSON report;
- human-readable summary;
- stable exit codes for CI.

Acceptance checks:

- reviewer can run one command;
- report is generated;
- failures produce non-zero exit code when configured;
- summary is understandable without reading code.

## Milestone 4 — Adapter interface and first real-service path

Duration: 2 months

Budget: EUR 9,000

Deliverables:

- adapter interface;
- service metadata model;
- first experimental adapter notes;
- compatibility matrix template;
- privacy/safety guidelines for test accounts.

Acceptance checks:

- adapter boundary is documented;
- real service integration path is clear;
- tests default to safe fixtures;
- limitations are explicit.

## Milestone 5 — Documentation and community feedback

Duration: 1 month

Budget: EUR 6,000

Deliverables:

- implementation guide;
- server-operator guide;
- developer CI guide;
- public reviewer report;
- feedback round with Fediverse/FOSS maintainers.

Acceptance checks:

- server operator can understand how to run the tool;
- developer can understand how to integrate it into CI;
- reviewer can understand what is validated and what remains future work;
- feedback is captured in public issues or docs.

## Timeline

Month 1: test model and schema

Months 2-3: local fixture engine

Month 4: CLI runner

Months 5-6: adapter interface and first real-service path

Month 7: documentation and community feedback

## Public outputs

The grant will produce source code, CLI runner, local fixture engine, report schema, sample reports, test scenarios, adapter interface, documentation, compatibility matrix template, and reviewer report.

## Success definition

The project is successful if an independent reviewer can clone the repository, run a local portability fixture, generate a report, inspect PASS/FAIL/PARTIAL results, and understand how the approach can be adapted to real federated services.
