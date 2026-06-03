# Fediversity Alignment

## Summary

Fediverse Portability Test Kit is an open-source QA tool for service portability.

It helps developers, server operators, and reviewers test whether users can safely move their data between federated and self-hosted services.

## Alignment thesis

Fediversity needs not only deployable federated services, but also evidence that those services preserve user autonomy.

A key autonomy question is:

```text
Can the user leave safely?
```

If export/import, migration, backup, restore, privacy preservation, and media integrity fail, portability remains only a promise.

This project makes portability testable.

## How it supports the ecosystem

The project supports:

- service portability;
- user autonomy;
- data decoupling;
- self-hosted service quality;
- migration safety;
- reproducible QA checks;
- transparency for server operators;
- compatibility reporting for developers.

## Practical use cases

### Server operator

A server operator can run the test kit before advertising portability.

Expected output:

```text
Export/import roundtrip: PASS
Media integrity: PASS
Private visibility: PASS
Follower graph: PARTIAL
Overall: PARTIAL
```

### Developer

A Fediverse software maintainer can add the checks to CI to prevent migration regressions.

### User community

A community can publish reports that help users understand portability risks before joining or migrating.

### Public-sector / NGO deployment

Organizations deploying federated services can use the report as evidence that exit, backup, restore, and privacy behavior were tested.

## Why QA is the right layer

Portability is a system property.

It cannot be verified by reading an API document alone.

It requires test data, export, import, restore, comparison, and failure reporting.

This is why a reusable QA test kit is valuable infrastructure.

## Non-claim discipline

The project should avoid claiming:

- legal compliance;
- universal Fediverse certification;
- production security audit coverage;
- guaranteed perfect migration;
- full compatibility with every service in v0.1.

Instead, the project should claim:

> This service or fixture was tested against a specific open portability test suite version, and here is the report.

## Long-term outcome

The long-term outcome is a shared testing language for portability:

- common scenarios;
- common report format;
- common failure categories;
- reproducible fixtures;
- adapter ecosystem;
- public compatibility matrix.

This helps turn portability from marketing language into testable infrastructure.
