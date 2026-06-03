# Reviewer FAQ

## Is this a migration service?

No.

Fediverse Portability Test Kit does not move real users between servers.

It checks whether export, import, restore, media, privacy, deleted-content, and relationship portability work as expected.

## Does this certify Fediverse servers?

No.

The project does not provide certification, legal compliance, or security-audit approval.

It produces QA evidence.

## Does it test real Mastodon servers today?

Not yet.

The current implementation uses a local synthetic Mastodon-like fixture.

Real-service adapters are planned as future work and must use dedicated test accounts.

## What exists now?

The repository currently includes:

- runnable local fixture CLI;
- JSON report generation;
- schema validation test;
- GitHub Actions workflow;
- strict CI mode with `--fail-on-partial`;
- check catalog;
- public report example;
- compatibility matrix template;
- grant submission pack.

## Who runs the tool?

The direct users are:

- server administrators;
- Fediverse service developers;
- public-interest organizations;
- reviewers and researchers.

Ordinary users are not expected to run the CLI themselves.

## How do ordinary users benefit?

They benefit from public reports or badges published by server operators.

Example:

```text
Portability checked: PASS / PARTIAL / FAIL
```

This helps users understand whether they can safely leave a server later.

## Why use PASS, PARTIAL, FAIL, and SKIP?

Portability is rarely binary.

`PARTIAL` is important because some migration behavior may be incomplete, manual, or service-dependent.

Unsupported behavior should be visible, not hidden as success.

## What is the main grant goal?

To turn the current runnable skeleton into a stronger open-source QA toolkit with:

- structured fixture dataset;
- expected-vs-actual comparison engine;
- media digest checks;
- privacy regression scenarios;
- adapter interface;
- public report workflow;
- community-reviewed documentation.
