# User Benefit Model

## Core distinction

Ordinary users are not expected to run this test kit themselves.

The first direct users are server administrators, Fediverse software developers, public-interest organizations, and reviewers. They run the checks and publish evidence.

The end beneficiary is the ordinary user who needs a trustworthy signal before joining a server or migrating away from one.

## User scenario: choosing a server

A person compares several federated services:

- `social.example`
- `video.example`
- `forum.example`

On a server page, directory, or public status page, they see:

```text
Portability checked: PASS / PARTIAL / FAIL
```

They can then open a public report:

```text
Export: PASS
Import: PASS
Media restore: PARTIAL
Private posts safety: PASS
Followers migration: FAIL
Deleted content restored: PASS
```

This answers a practical trust question:

> If I later need to leave this server, can I take my data with me safely?

## User scenario: migration risk before damage

Without a portability report, many problems are discovered only after a move:

- photos are missing;
- private posts become public;
- deleted content reappears;
- follower/following relationships are incomplete;
- archives are not importable;
- old links break without warning.

With a portability report, the user sees the risk before the migration:

```text
old.social export: PASS
new.social import: PARTIAL
risk: media attachments may be lost
```

The user can then delay the move, choose another server, or make an informed backup plan.

## Operator scenario: proving trustworthiness

A server administrator runs the tool and publishes the report:

```bash
fediverse-portability-test run \
  --fixture mastodon-like \
  --target https://social.example \
  --output portability-report.json
```

The server can then say:

```text
We passed portability checks.
Here is the public report.
```

That is stronger than a policy promise because it gives users and reviewers concrete evidence.

## Developer scenario: preventing regressions

A Fediverse software developer can run portability checks in CI so pull requests do not silently break export, import, privacy, or restore behavior.

The test kit becomes QA infrastructure, not marketing decoration.

## Public-interest scenario

A reviewer, NGO, research group, or grant program can compare reports across services and ask:

- Which services support real portability?
- Which services only claim it?
- Where do private posts, media, deleted content, or relationships fail?
- Which failures are fixable by implementation work?

## Positioning

This project is not a migration service.

It does not move users itself.

It checks whether the road for migration is safe.
