# NLnet Form Answers Draft

This document converts the project materials into concise answers suitable for an NLnet-style proposal form.

These answers are drafts. They should be reviewed and adapted before final submission.

## Project name

Fediverse Portability Test Kit

## Project subtitle

Open QA suite for Fediverse service portability and data migration evidence.

## Short abstract

Fediverse Portability Test Kit is an open-source QA toolkit that helps server operators, developers, reviewers, and public-interest organizations verify whether users can safely export, import, restore, and validate their data across federated and self-hosted services.

The project is not a hosted migration service. It checks whether the road for migration is safe: whether posts, media, privacy settings, deleted-content state, and relationship data survive portability scenarios without silent loss or privacy regression.

The current repository already contains a runnable local fixture CLI, JSON report schema, schema validation test, check catalog, public report model, and reviewer documentation. The requested grant would develop this into a stronger fixture engine, comparison layer, adapter boundary, CI integration path, and community-reviewed portability evidence model.

## Relevant background

The applicant has long-term practical experience in software quality assurance, manual testing, product analysis, and financial technology systems. This background is directly relevant because the project is fundamentally a QA infrastructure project: it defines expected behavior, creates reproducible scenarios, compares expected vs actual outcomes, reports failures, and communicates risks clearly.

The applicant's contribution to this project is the initial concept, repository structure, test model, runnable CLI skeleton, report schema direction, documentation, and grant-preparation materials. The project intentionally starts from the applicant's QA strengths rather than claiming to be a full production Fediverse migration platform from day one.

## Requested amount

EUR 40,000.

## Budget use and effort breakdown

Requested budget: EUR 40,000.

Approximate effort model: 80 person-days at an average rate of EUR 500/day, including design, implementation, testing, documentation, community feedback, and grant reporting.

Breakdown:

1. Runnable report skeleton and schema validation — EUR 6,000, about 12 days
2. Fixture dataset and comparison engine — EUR 10,000, about 20 days
3. Check expansion and CI-grade validation — EUR 8,000, about 16 days
4. Adapter interface and Mastodon-style experimental path — EUR 8,000, about 16 days
5. Public report model, documentation, compatibility matrix, and community feedback — EUR 8,000, about 16 days

Total: EUR 40,000.

## Other funding sources

No other funding sources are currently committed for this project.

## What problem are you solving?

Federated and self-hosted services promise user autonomy and portability. In practice, users may only discover portability failures after a move has already happened.

Typical failures include:

- incomplete export archives;
- missing images or videos;
- private or followers-only posts becoming public;
- deleted content reappearing;
- follower/following relationships not restoring;
- old links breaking;
- backups not restoring cleanly.

This project turns those risks into reproducible QA checks and public, machine-readable reports.

## Who benefits?

The direct tool users are:

- Fediverse server administrators;
- Fediverse software developers;
- public-interest organizations;
- reviewers and researchers.

The end beneficiary is the ordinary user.

Ordinary users are not expected to run the CLI themselves. Instead, server operators or developers run the checks and publish a report or badge such as:

```text
Portability checked: PASS / PARTIAL / FAIL
```

A user can then evaluate migration risk before joining or leaving a server.

## What will you make?

The project will produce:

- CLI runner for portability checks;
- controlled local fixture dataset;
- expected-vs-actual comparison engine;
- JSON report schema;
- human-readable report summaries;
- check catalog;
- CI integration examples;
- strict CI mode for partial/failure handling;
- adapter interface for future real-service validation;
- public report and badge model;
- compatibility matrix template;
- server-operator, developer, and reviewer documentation.

## What is already done?

The repository already includes:

- first runnable CLI command: `fediverse-portability-test run --fixture mastodon-like`;
- generated JSON report;
- human-readable CLI summary;
- `--fail-on-partial` strict mode;
- report schema v0.1;
- schema validation test;
- unit tests;
- GitHub Actions workflow;
- check catalog;
- user benefit model;
- badge/public report model;
- compatibility matrix template;
- application draft;
- GenAI disclosure draft;
- roadmap issues.

## What is new compared to existing efforts?

Existing Fediverse services may provide export/import features or migration documentation. Protocol tests may validate ActivityPub behavior. Project-specific test suites may prevent regressions inside one codebase.

This project focuses on a different layer: reusable QA infrastructure for portability evidence.

It provides:

- controlled portability scenarios;
- explicit expected vs actual behavior;
- PASS/FAIL/PARTIAL/SKIP result states;
- machine-readable reports;
- public summaries and badge model;
- CI-friendly execution;
- future adapter boundary for real-service validation.

It does not replace service migration features. It tests whether they work from the perspective of user data portability.

## Technical approach

The project starts with safe local synthetic fixtures before touching real services.

The planned architecture has these layers:

1. fixture data model;
2. export/import or restore simulation;
3. expected-vs-actual comparison engine;
4. check catalog;
5. JSON report schema;
6. CLI runner;
7. CI integration;
8. adapter boundary for future real-service validation;
9. public report and compatibility matrix layer.

Future adapters should use dedicated test accounts only and must not touch real user accounts.

## Key risks and mitigations

| Risk | Mitigation |
|---|---|
| Overclaiming certification | Use narrow wording: QA evidence, not certification |
| Unsafe live testing | Start with local fixtures and require dedicated test accounts for adapters |
| Unsupported service behavior hidden as success | Report unsupported behavior as `SKIP` or `PARTIAL` |
| Privacy regression during testing | Keep restricted-content checks synthetic and safe by default |
| Reports too technical for users | Provide public summaries and badge model |
| Too broad Fediverse scope | Start with Mastodon-like fixture and adapter boundary, then expand carefully |

## Work plan and milestones

Requested budget: EUR 40,000.

Planned milestones:

1. Runnable report skeleton and schema validation — EUR 6,000
2. Fixture dataset and comparison engine — EUR 10,000
3. Check expansion and CI-grade validation — EUR 8,000
4. Adapter interface and Mastodon-style experimental path — EUR 8,000
5. Public report model, documentation, and community feedback — EUR 8,000

## Community and ecosystem engagement

The project will seek feedback from Fediverse server operators, service developers, and public-interest reviewers.

Planned community work:

- publish roadmap issues;
- request feedback on portability failure modes;
- discuss adapter safety boundaries;
- collect examples of real migration pain points;
- document limitations openly;
- maintain a compatibility matrix template.

## Sustainability

The project is designed as an open-source QA toolkit that remains useful without a hosted service.

Possible long-term paths:

- integration into service CI pipelines;
- community-maintained adapters;
- public-interest portability reports;
- compatibility matrix contributions;
- optional hosted report viewer later.

## License

Apache-2.0.

## GenAI disclosure

Generative AI assistance was used for documentation drafting, grant-readiness review, and initial boilerplate code/tests. The human applicant remains responsible for final review, correctness, licensing, and submission.

See `docs/GENAI_DISCLOSURE.md`.

## Repository

https://github.com/safal207/fediverse-portability-test-kit
