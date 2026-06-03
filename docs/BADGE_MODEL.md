# Badge and Public Report Model

## Purpose

The badge is a public trust signal derived from a machine-readable portability report.

It is meant for ordinary users who will not run the CLI themselves.

## Badge states

Recommended first badge states:

```text
Portability checked: PASS
Portability checked: PARTIAL
Portability checked: FAIL
Portability checked: SKIP
```

Meaning:

- `PASS`: all required checks passed for the declared scenario.
- `PARTIAL`: at least one check is incomplete, degraded, or requires manual confirmation.
- `FAIL`: at least one required check failed.
- `SKIP`: the check could not run or was outside the declared scope.

## Minimal public summary

A public report page can expose a short summary:

```text
Portability report for social.example

Overall: PARTIAL

Data export: PASS
Data import: PASS
Media restore: PASS
Privacy preservation: PASS
Follower graph: PARTIAL
Deleted content handling: PASS

Download report.json
```

## What the badge must not imply

The badge should stay narrow. It should not imply:

- legal compliance;
- full security audit coverage;
- universal compatibility with every Fediverse service;
- permanent certification;
- successful migration of real users.

## Evidence chain

A credible badge should link to:

1. the generated JSON report;
2. tool version;
3. scenario name;
4. fixture or adapter name;
5. timestamp;
6. known limitations;
7. reproduction command when possible.

## First implementation target

For the MVP, the badge can be static Markdown generated from `portability-report.json`.

Later versions can add:

- hosted report pages;
- signed reports;
- historical trend pages;
- compatibility matrix;
- independent third-party report mirrors.
