# Submission Pack

This page is the reviewer-facing index for the Fediverse Portability Test Kit grant submission.

## Repository

https://github.com/safal207/fediverse-portability-test-kit

## One-sentence summary

Fediverse Portability Test Kit is an open-source QA toolkit for checking whether users can safely export, import, restore, and validate their data across federated and self-hosted services.

## Core claim

Portability should be tested, not only promised.

This project is not a hosted migration service and not a certification authority. It provides reproducible QA checks, machine-readable reports, and public summaries that help operators, developers, reviewers, and users understand migration risk.

## Current runnable proof

```bash
python -m pip install -e .
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p 'test_*.py'
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

Strict CI mode:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
```

## CI status

GitHub Actions workflow `Tests` was manually checked from the GitHub UI and reported green before submission preparation continued.

## What already exists

- Runnable local synthetic fixture CLI
- JSON report generation
- Human-readable summary
- `--fail-on-partial` strict CI mode
- JSON report schema v0.1
- Schema validation test
- Unit tests
- GitHub Actions workflow
- Public report summary example
- Compatibility matrix template
- Check catalog
- Server-operator guide
- Developer CI guide
- User benefit model
- Badge/public report model
- Roadmap to real-service adapters
- Existing efforts comparison
- GenAI disclosure draft
- NLnet form answers draft
- Final submission checklist
- Outreach message draft
- Public roadmap issues

## Reviewer quick path

1. Read `README.md`.
2. Run the local fixture.
3. Inspect `portability-report.json`.
4. Read `examples/public-report-summary.md`.
5. Read `docs/CHECK_CATALOG.md`.
6. Read `docs/EXISTING_EFFORTS.md`.
7. Read `docs/BUDGET_AND_MILESTONES.md`.
8. Read `docs/NLNET_FORM_ANSWERS.md`.
9. Review `docs/FINAL_SUBMISSION_CHECKLIST.md` before submission.

## Key documents

| Document | Purpose |
|---|---|
| `README.md` | Main project entry point |
| `docs/NLNET_FORM_ANSWERS.md` | Draft answers for the grant form |
| `docs/APPLICATION_DRAFT.md` | Longer proposal draft |
| `docs/BUDGET_AND_MILESTONES.md` | Budget and work plan |
| `docs/FEDIVERSITY_ALIGNMENT.md` | Alignment with Fediversity goals |
| `docs/EXISTING_EFFORTS.md` | Comparison with existing work |
| `docs/CHECK_CATALOG.md` | Current and planned checks |
| `docs/ROADMAP_TO_REAL_ADAPTER.md` | Safe path from fixture to real-service adapters |
| `docs/USER_BENEFIT_MODEL.md` | Who runs the tool and who benefits |
| `docs/BADGE_MODEL.md` | Public report and badge model |
| `docs/COMPATIBILITY_MATRIX_TEMPLATE.md` | Public matrix format |
| `docs/OUTREACH_MESSAGE.md` | Community feedback request draft |
| `docs/GENAI_DISCLOSURE.md` | Generative AI disclosure draft |
| `docs/FINAL_SUBMISSION_CHECKLIST.md` | Final pre-submit checklist |

## Current limitations

- The current implementation uses a synthetic local Mastodon-like fixture.
- It does not claim production compatibility with Mastodon, PeerTube, Lemmy, or all ActivityPub services yet.
- It does not migrate real users.
- It does not certify services.
- It does not provide legal or GDPR advice.

## Grant work focus

The requested grant would turn the current runnable skeleton into a stronger open-source QA toolkit by building:

- structured fixture dataset;
- expected-vs-actual comparison engine;
- expanded check catalog;
- media digest checks;
- privacy regression scenarios;
- adapter interface;
- Mastodon-style experimental path;
- public report and compatibility matrix workflow;
- community-reviewed documentation.

## Submission readiness status

Current status: close to submission-ready, pending final applicant review.

Confirmed pre-submit evidence:

- GitHub Actions workflow `Tests` reported green in the GitHub UI.
- Local runnable proof is documented.
- Schema validation is part of the test suite.
- Strict CI mode is implemented.

Remaining pre-submit tasks:

- review `docs/NLNET_FORM_ANSWERS.md` field by field;
- publish or prepare outreach message;
- capture any external feedback if available before submission;
- remove or soften unsupported claims;
- submit only after final applicant review.
