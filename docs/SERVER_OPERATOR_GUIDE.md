# Server Operator Guide

## Who this is for

This guide is for administrators of Fediverse or Fediverse-like services who want to produce public evidence that portability works.

The first MVP uses a local synthetic fixture. Real service adapters are planned but not claimed yet.

## Run the local fixture

```bash
git clone https://github.com/safal207/fediverse-portability-test-kit.git
cd fediverse-portability-test-kit
python -m pip install -e .
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

Expected output:

```text
Export/import roundtrip: PASS
Media integrity: PASS
Private visibility: PASS
Deleted content safety: PASS
Follower graph: PARTIAL

Overall: PARTIAL
Report: portability-report.json
```

## Include server metadata

Operators can include a target URL in the report metadata:

```bash
fediverse-portability-test run \
  --fixture mastodon-like \
  --target https://social.example \
  --output portability-report.json
```

This does not yet test the live server. It records the declared target while using the local fixture.

## Publish the report

An operator can publish:

- `portability-report.json`;
- a short human-readable summary;
- a badge linking to the report;
- known limitations and skipped checks.

## Recommended honesty rule

Operators should not claim more than the report proves.

Good wording:

```text
We ran the Fediverse Portability Test Kit local fixture and published the report.
Real-service adapter validation is not claimed yet.
```

Bad wording:

```text
This server is fully certified for all Fediverse migrations.
```

## Future real-service adapter flow

A later adapter-based version may support a command shape like:

```bash
fediverse-portability-test run \
  --adapter mastodon \
  --target https://social.example \
  --output portability-report.json
```

That future flow should create test data, export it, import or restore it, compare results, validate privacy, and generate a report.
