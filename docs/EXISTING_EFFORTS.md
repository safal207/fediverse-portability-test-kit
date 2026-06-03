# Existing and Historical Efforts

This project does not start from the assumption that no portability work exists.

Many Fediverse and Fediverse-adjacent projects already provide export, import, account migration, or protocol-level testing. The gap addressed here is different: reusable QA infrastructure that produces public, machine-readable evidence about whether portability behavior works in practice.

## Comparison table

| Existing effort | What it does | Gap this project addresses |
|---|---|---|
| Built-in Mastodon export/import and account move features | Allows users to export account data and move parts of their social graph | Does not provide a reusable cross-service QA test suite or public PASS/PARTIAL/FAIL report schema |
| Fediverse service-specific migration docs | Explain how a user or operator can migrate data | Usually manual, service-specific, and not machine-verifiable |
| ActivityPub protocol tests | Check protocol-level behavior and interoperability | Do not validate full end-user export/import/restore data portability roundtrips |
| Project-internal test suites | Prevent regressions inside a specific Fediverse service | Usually not reusable as public portability evidence across services |
| Backup/restore scripts | Help operators preserve server state | Focus on server administration rather than user-level portability and privacy-preserving migration |
| Manual community reports | Describe migration success or failure cases | Valuable but not standardized, repeatable, or machine-readable |

## What this project adds

Fediverse Portability Test Kit focuses on the QA evidence layer:

- controlled fixtures;
- explicit expected vs actual behavior;
- PASS/FAIL/PARTIAL/SKIP result states;
- JSON report schema;
- human-readable summaries;
- CI-friendly command-line execution;
- public report and badge model;
- adapter boundary for future real-service validation.

## Non-competitive positioning

The goal is not to replace built-in migration features or service-specific tests.

The goal is to help maintainers, operators, reviewers, and public-interest organizations verify whether those features work from a user-portability perspective.

## Why this matters

A service can claim portability while still losing media, widening private visibility, restoring deleted content, or failing to preserve relationship data.

This project turns those claims into reproducible checks.
