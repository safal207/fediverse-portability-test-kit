# Compatibility Matrix Template

This template shows how portability results can be summarized across services, versions, and scenarios.

The matrix is not a certification table. It is a public evidence index linked to machine-readable reports.

## Matrix fields

| Field | Meaning |
|---|---|
| Service | Service or fixture name |
| Version | Service or fixture version |
| Scenario | Tested portability scenario |
| Report date | Date of the generated report |
| Export | Export availability and readability |
| Import/restore | Import or restore behavior |
| Media | Media attachment integrity |
| Privacy | Private/followers-only visibility preservation |
| Deleted content | Deleted content remains deleted |
| Followers | Follower/following graph preservation |
| Overall | Report-level PASS/PARTIAL/FAIL/SKIP |
| Report | Link to JSON report |

## Example

| Service | Version | Scenario | Export | Import/restore | Media | Privacy | Deleted content | Followers | Overall | Report |
|---|---:|---|---|---|---|---|---|---|---|---|
| mastodon-like-fixture | 0.1 | export_import_roundtrip | PASS | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL | `examples/export-import-fixture/sample-report.json` |

## Result interpretation

- `PASS`: evidence supports expected portability behavior.
- `PARTIAL`: behavior is incomplete, degraded, or requires manual confirmation.
- `FAIL`: expected portability behavior failed.
- `SKIP`: check was not applicable or could not run in the declared scope.

## Publication guidance

Public matrix pages should:

- link to the original JSON report;
- include tool version and schema version;
- state the scenario and fixture or adapter used;
- avoid implying legal compliance or universal certification;
- show limitations and skipped checks clearly.
