# CI Integration

## Purpose

Fediverse software developers can use portability checks as regression tests.

The goal is to detect changes that break export, import, restore, media integrity, privacy preservation, follower graph behavior, or deleted-content handling.

## Minimal GitHub Actions example

```yaml
name: Portability checks

on: [pull_request]

jobs:
  portability:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: python -m pip install -e .
      - run: fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

## Exit code policy

Current MVP policy:

- `0`: command completed without failed checks, including `PARTIAL` results;
- `1`: at least one check failed;
- `2`: command usage error.

This allows CI to fail on true failures while still preserving partial evidence during early adapter development.

## Future policy options

Future versions may add stricter modes:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
fediverse-portability-test run --adapter mastodon --target https://social.example --required-checks privacy,media,deleted-content
```
