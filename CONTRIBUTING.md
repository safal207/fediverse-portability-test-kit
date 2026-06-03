# Contributing

Thank you for considering a contribution to Fediverse Portability Test Kit.

This project is early. The current goal is to build a small, trustworthy QA toolkit for checking whether export, import, restore, media, privacy, deleted-content, and relationship portability work in practice.

## Contribution principles

- Keep claims narrow and testable.
- Prefer reproducible checks over broad promises.
- Do not use real user accounts for tests.
- Report unsupported behavior as `SKIP` or `PARTIAL`, not as success.
- Make expected vs actual behavior explicit.
- Keep public reports understandable to non-technical users.

## How to run locally

```bash
python -m pip install -e .
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p 'test_*.py'
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

## Strict CI mode

For CI gates that should fail on incomplete portability evidence:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
```

## Adding a new check

A check should include:

- stable `id`;
- `result`: `PASS`, `FAIL`, `PARTIAL`, or `SKIP`;
- clear `description`;
- expected behavior;
- actual behavior;
- optional reproduction guidance;
- optional evidence object.

Document the check in `docs/CHECK_CATALOG.md`.

## Adding a fixture

A fixture should:

- use synthetic data only;
- include public and restricted visibility examples when relevant;
- include deleted-content state when relevant;
- include media digest expectations when media is involved;
- remain deterministic across test runs.

## Adding a future real-service adapter

Real-service adapters should be treated cautiously.

They must:

- use dedicated test accounts only;
- avoid real user accounts;
- document required permissions;
- document cleanup behavior;
- make destructive actions explicit;
- report unsupported checks honestly.

See `docs/ROADMAP_TO_REAL_ADAPTER.md`.

## Documentation contributions

Useful documentation contributions include:

- server operator guides;
- CI integration examples;
- compatibility matrix examples;
- public report examples;
- feedback from Fediverse administrators or maintainers;
- limitations and risk notes.
