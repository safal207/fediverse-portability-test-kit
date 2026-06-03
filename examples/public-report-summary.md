# Public Portability Report Summary

Service: `mastodon-like-fixture`

Scenario: `export_import_roundtrip`

Overall: `PARTIAL`

```text
Portability checked: PARTIAL
```

## Summary

| Area | Result | Meaning |
|---|---|---|
| Export/import roundtrip | PASS | Fixture export can be produced, parsed, and restored in the local scenario |
| Media integrity | PASS | Media attachments are restored with matching digests in the fixture |
| Private visibility | PASS | Private and followers-only visibility labels are preserved |
| Deleted content safety | PASS | Deleted content does not reappear after restore |
| Follower graph | PARTIAL | Followers are restored, but following relationships require manual confirmation |

## User-facing interpretation

This fixture report suggests that the tested local scenario preserves posts, media, privacy labels, and deleted-content state. Relationship restoration is incomplete and should be treated as a migration risk.

## Limitations

This is a synthetic local fixture report.

It does not claim real Mastodon, PeerTube, Lemmy, or generic ActivityPub compatibility yet.

The full machine-readable report is available at:

```text
examples/export-import-fixture/sample-report.json
```
