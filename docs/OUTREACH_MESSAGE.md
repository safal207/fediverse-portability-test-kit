# Outreach Message Draft

This message can be adapted for Mastodon, Fediverse admin forums, GitHub discussions, or direct maintainer feedback requests.

## Short version

```text
Hi! I am building Fediverse Portability Test Kit: an open-source QA test suite for checking whether export/import/restore portability actually works.

It is not a migration service and not a certification authority. The goal is to help server operators and developers produce public evidence like:

Portability checked: PASS / PARTIAL / FAIL

The first repo version has a runnable local synthetic fixture, JSON report schema, CLI, strict CI mode, public report example, and roadmap to real-service adapters.

I would appreciate feedback from Fediverse admins/developers:

- Which migration/export failures are most painful in practice?
- Which checks would be most useful first?
- What would make a portability report credible and safe?
- What adapter safety constraints should be mandatory?

Repo: https://github.com/safal207/fediverse-portability-test-kit
```

## Longer version

```text
Hi Fediverse admins and developers,

I am working on Fediverse Portability Test Kit: an open-source QA test suite for checking whether user data portability works in practice.

The project asks a narrow QA question:

Can a user safely leave one server and move to another?

The tool is not intended to migrate real users itself. Instead, the goal is to help server operators, service developers, reviewers, and public-interest organizations generate evidence about portability behavior:

- Can data be exported?
- Can it be imported or restored?
- Do media attachments survive?
- Do private/followers-only posts stay private?
- Does deleted content remain deleted?
- Are follower/following relationships preserved or honestly reported as partial?

The end beneficiary is the ordinary user, who should be able to inspect a public report or badge before trusting a server or planning a migration.

The current repository includes a runnable local synthetic fixture, JSON report schema, CLI output, strict CI mode, public report summary, compatibility matrix template, and roadmap to future real-service adapters.

I would be grateful for feedback on:

1. Real migration/export/import failures you have seen.
2. The most important checks to prioritize.
3. What would make a public portability report credible.
4. Safety constraints for any future adapter that touches real test servers.
5. Cases where this project should avoid overclaiming.

Repository:
https://github.com/safal207/fediverse-portability-test-kit

Thank you!
```

## Feedback issue link

Use this issue for structured feedback:

```text
https://github.com/safal207/fediverse-portability-test-kit/issues/7
```
