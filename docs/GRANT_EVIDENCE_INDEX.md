# Grant Evidence Index

Application: `2026-08-012`

Fund: NGI Fediversity

Requested amount: EUR 40,000

Canonical repository: https://github.com/safal207/fediverse-portability-test-kit

Review state: application acknowledged; first-round eligibility review pending.

## Reviewer thesis

Fediverse Portability Test Kit turns a user-autonomy claim into a reproducible QA question:

```text
Can a user export, move, restore, and verify their data without silent loss or privacy regression?
```

## Causal and temporal transition graph

```text
service dependency
  -> migration or shutdown risk
  -> export/import must preserve user state
  -> deterministic fixture and comparison checks
  -> machine-readable evidence report
  -> real-service adapter validation
  -> public compatibility evidence
  -> safer user choice and lower lock-in
```

Current verified transition:

```text
problem definition
  -> runnable synthetic fixture
  -> schema-valid report
  -> documented PASS / PARTIAL / FAIL / SKIP semantics
  -> compatibility matrix template and badge evidence model
```

Grant-funded transition:

```text
synthetic fixture
  -> stronger comparison engine
  -> safe adapter boundary
  -> experimental Mastodon-style path
  -> community-reviewed public evidence model
```

## Claim-to-evidence matrix

| Claim | Current evidence | Status | Grant-funded delta | Acceptance test |
| --- | --- | --- | --- | --- |
| A reviewer can run a local portability test | `fediverse-portability-test run --fixture mastodon-like` | Implemented baseline | Harden packaging and fixtures | Clean checkout produces a report |
| Reports are machine-readable | `schemas/portability-report.schema.json` | Implemented | Stabilise schema and evidence fields | Generated report validates against schema |
| Privacy regressions are visible | Private/followers-only and deleted-content checks in the local fixture | Implemented for synthetic data | Expand fixtures and comparison rules | Privacy state changes produce explicit failed checks |
| Media integrity is checked | Digest-oriented local fixture path | Implemented baseline | Expand media dataset and comparison engine | Changed media produces a deterministic failure |
| Relationship portability is represented | Follower/following graph check reports `PARTIAL` where evidence is incomplete | Implemented baseline | Improve graph fixtures and adapter support | Unsupported migration remains visible, never silently passes |
| Real Fediverse services can be tested safely | Adapter boundary and operator guidance are documented | Planned / partial | Build experimental adapter path and cleanup rules | Unsupported checks return `SKIP` or `PARTIAL`; test accounts are cleaned safely |
| Results can help users compare servers | `docs/COMPATIBILITY_MATRIX_TEMPLATE.md` and `docs/BADGE_MODEL.md` | Implemented documentary baseline | Validate wording with external operators | Public output links source evidence and avoids certification overclaim |
| External ecosystem feedback exists | Public issues and contribution path | Pending | Engage maintainers and operators | At least one external review is captured publicly |

## Reviewer commands

```bash
python -m pip install -e .
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

Strict CI-oriented mode:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
```

Expected evidence:

- a JSON report is created;
- the report validates against the published schema;
- incomplete portability remains visible as `PARTIAL` or `SKIP`;
- failed privacy or integrity checks cause a non-zero result under the documented policy.

## Current boundaries

The repository does not currently claim:

- production Mastodon compatibility;
- automatic migration of real users;
- universal Fediverse certification;
- a legal GDPR determination;
- a production security audit.

The current executable evidence is a synthetic local baseline. Real-service integration is a grant-funded transition, not a completed claim.

## Decision rule

A grant milestone is complete only when all four conditions hold:

1. the deliverable exists;
2. a reviewer command or inspection path is documented;
3. a negative or incomplete case is represented;
4. the result does not overclaim beyond the evidence.
