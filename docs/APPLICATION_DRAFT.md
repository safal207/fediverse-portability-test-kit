# Proposal Draft: Fediverse Portability Test Kit

## Project title

Fediverse Portability Test Kit: Open QA Suite for Service Portability and Data Migration

## Abstract

Fediverse Portability Test Kit is an open-source QA test suite that helps server operators, developers, reviewers, and public-interest organizations verify whether users can safely export, import, restore, and validate their data across federated and self-hosted services.

The project does not aim to be a hosted migration service. Instead, it checks whether the road for migration is safe: whether content, media, privacy settings, deleted-content state, and relationship data survive an export/import or restore scenario without silent loss or privacy regression.

The first implementation provides a runnable local synthetic fixture, JSON report schema, CLI output, check catalog, and documentation. The grant work would turn this into a stronger fixture engine, comparison layer, adapter interface, public report model, and community-reviewed portability QA infrastructure.

## Expected outcomes

The project will produce:

- a CLI runner for portability checks;
- a controlled local fixture dataset;
- a comparison engine for expected vs actual restored state;
- a JSON report schema;
- human-readable summaries;
- check catalog and documentation;
- CI integration examples;
- adapter boundary for future real-service integrations;
- public report and badge model;
- compatibility matrix template;
- reviewer-facing documentation.

## Problem statement

Federated and self-hosted services often promise user autonomy and portability. In practice, portability can fail in ways users discover only after a move:

- export archives may be incomplete;
- media files may be lost;
- private or followers-only posts may become public;
- deleted content may reappear;
- follower/following relationships may not restore;
- old links may break;
- backups may not restore cleanly.

This project turns those risks into reproducible checks and public evidence.

## Who runs it and who benefits

Ordinary users are not expected to run the test kit themselves.

The first direct users are:

- server administrators;
- Fediverse service developers;
- public-interest organizations;
- reviewers and researchers.

The end beneficiary is the ordinary user who can inspect a public portability report or badge before joining a server or migrating away from one.

## Relevance to Fediversity

The project supports the goal of practical service portability and user autonomy in federated and self-hosted services.

It contributes an evidence layer: operators and developers can show whether portability works in practice, not only in documentation.

## Requested amount

EUR 40,000.

## Budget use

- Runnable report skeleton, schema validation, and CLI hardening: EUR 6,000
- Fixture dataset and comparison engine: EUR 10,000
- Check catalog expansion and CI-grade validation: EUR 8,000
- Adapter interface and Mastodon-style experimental path: EUR 8,000
- Documentation, public report/badge model, compatibility matrix, and community feedback: EUR 8,000

Total: EUR 40,000.

## Existing and historical efforts

The project does not replace built-in migration features, ActivityPub tests, or service-specific documentation.

Its role is narrower: reusable QA infrastructure that produces machine-readable and human-readable evidence about whether portability behavior works.

See `docs/EXISTING_EFFORTS.md` for a comparison table.

## Technical challenges

Key technical challenges include:

- designing fixtures that model realistic user data without using real accounts;
- comparing exported and restored state across different service models;
- representing partial support honestly;
- preserving privacy checks safely;
- avoiding destructive behavior on live systems;
- defining a real-service adapter boundary that maintainers can trust;
- producing reports that are understandable to non-technical users without overclaiming certification.

## Risk mitigation

- Start with local synthetic fixtures before real-service adapters.
- Use dedicated test accounts for any future live adapter path.
- Treat unsupported behavior as `SKIP` or `PARTIAL`, not success.
- Avoid legal or compliance claims.
- Keep report schema public and versioned.
- Document limitations clearly.

## Ecosystem and community engagement

Planned engagement:

- publish issues for check catalog and adapter boundary discussion;
- request feedback from Fediverse administrators and developers;
- document known limitations openly;
- create a compatibility matrix template;
- collect public feedback in GitHub issues or project documentation.

## Sustainability

The project is designed as a small open-source QA toolkit that can remain useful even without a hosted service.

Long-term sustainability paths include:

- integration into service CI pipelines;
- public-interest report publication;
- community-maintained adapters;
- compatibility matrix contributions;
- small hosted report viewer as a later optional layer.

## Current repository status

The repository currently includes:

- README and reviewer path;
- Fediversity alignment docs;
- user benefit model;
- JSON report schema;
- sample report;
- first runnable local fixture CLI;
- report generation helpers;
- unit tests;
- schema validation test;
- GitHub Actions workflow;
- check catalog;
- existing efforts comparison;
- badge and public report model;
- server operator guide;
- CI integration guide;
- roadmap to real-service adapter.

## GenAI disclosure

Generative AI assistance was used for documentation drafting, grant-readiness review, and initial boilerplate code/tests. The human applicant remains responsible for final review, correctness, licensing, and submission.

See `docs/GENAI_DISCLOSURE.md`.
