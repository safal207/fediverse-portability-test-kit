# Portability Test Model

## Core question

```text
Can a user safely leave one server and move to another?
```

The test model checks whether a controlled user dataset survives export, import, migration, restore, and validation.

## Test phases

### 1. Fixture creation

Create a controlled account dataset with:

- public posts;
- followers-only posts;
- private/direct content markers;
- media attachments;
- profile metadata;
- followers and following relationships;
- blocked and muted accounts;
- deleted content markers;
- old links and references.

### 2. Export

Request or simulate export from the source service.

Checks:

- export is available;
- archive is readable;
- expected object counts are present;
- media files are included;
- metadata is included;
- private visibility labels are preserved.

### 3. Import / restore

Import into a target service or fixture.

Checks:

- import completes;
- content count matches expected state;
- media files restore;
- follower/following relationships restore or produce documented partial results;
- blocked/muted accounts restore;
- deleted content does not reappear;
- private content does not become public.

### 4. Compare

Compare source fixture expectations with restored state.

Result categories:

```text
PASS      expected behavior preserved
FAIL      expected behavior broken
PARTIAL   behavior partially preserved or manually reviewable
SKIP      check was not applicable or not supported
```

### 5. Report

Generate:

- machine-readable JSON report;
- human-readable summary;
- failed checks;
- reproduction notes;
- adapter metadata;
- version metadata.

## Initial check catalog

| Check ID | Purpose |
|---|---|
| export_available | Export can be requested or simulated. |
| archive_readable | Export archive can be parsed. |
| public_posts_preserved | Public posts survive roundtrip. |
| media_integrity | Media count and digests match expectations. |
| private_visibility_preserved | Private/followers-only content does not become public. |
| deleted_content_not_restored | Deleted content does not reappear. |
| follower_graph_preserved | Follower/following graph is preserved or reported as partial. |
| blocks_preserved | Blocked accounts remain blocked. |
| links_resolvable | Internal links remain resolvable or mapped. |
| report_complete | Report contains required metadata and results. |

## Adapter model

A future adapter should expose a small interface:

```text
create_fixture_account()
seed_fixture_data()
export_account()
import_account()
read_restored_state()
cleanup_fixture_data()
```

The first implementation can use local fake services before real Fediverse integrations.

## Safety model

The test kit should default to controlled fixtures and test accounts.

It should avoid touching real user data unless an operator explicitly configures a safe test environment.

## Output model

The report should make failures actionable:

```text
what failed
why it matters
how to reproduce
what evidence was observed
what was expected
what was actually restored
```

## First MVP scenario

```text
Scenario: export_import_roundtrip
Fixture: mastodon-like local fixture
Result types: PASS / FAIL / PARTIAL / SKIP
Output: portability-report.json + summary text
```

## Future scenarios

- server-to-server migration;
- backup and restore;
- account alias and redirect migration;
- media-heavy export;
- followers-only visibility regression;
- deleted content resurrection;
- blocked-user preservation;
- cross-version migration;
- large archive stress test.
