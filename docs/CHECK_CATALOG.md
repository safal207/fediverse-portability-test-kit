# Check Catalog

This catalog documents the first portability checks used by the local synthetic fixture.

The initial scope is intentionally narrow: export/import roundtrip behavior, media integrity, visibility preservation, deleted-content handling, and relationship restoration.

## Result states

- `PASS`: the observed behavior matches the expected behavior.
- `FAIL`: the observed behavior violates the expected behavior.
- `PARTIAL`: the behavior is incomplete, degraded, or requires manual confirmation.
- `SKIP`: the check was not applicable or could not be executed in the declared scope.

## export_available

Verifies that an export archive can be produced and parsed.

Expected behavior:

- export archive exists;
- archive metadata is readable;
- expected top-level data files are present.

Failure examples:

- no export can be produced;
- archive is unreadable;
- required data files are missing.

## public_posts_preserved

Verifies that public posts survive export/import roundtrip.

Expected behavior:

- public post count is preserved;
- post body/content is preserved;
- timestamps or stable identifiers are preserved where applicable.

Failure examples:

- public posts disappear;
- content is truncated;
- order or identity cannot be reconstructed.

## media_integrity

Verifies that media attachments survive export/import roundtrip with matching digests.

Expected behavior:

- media files are exported;
- media files are restored;
- restored file digest matches the original digest;
- media references still point to restored media.

Failure examples:

- image or video attachments are missing;
- restored file differs from the exported file;
- post references point to broken media.

## private_visibility_preserved

Verifies that private or followers-only posts do not become public after export/import or restore.

Expected behavior:

- private visibility remains private;
- followers-only visibility remains followers-only;
- restricted content is not widened to public visibility.

Failure examples:

- private post becomes public;
- followers-only post becomes public;
- visibility metadata is dropped.

## deleted_content_not_restored

Verifies that deleted content does not reappear after import or restore.

Expected behavior:

- deleted post state is preserved;
- deleted post body is not restored as live content;
- deletion marker or tombstone behavior is respected when applicable.

Failure examples:

- deleted post reappears as active content;
- deleted media attachment is restored unexpectedly;
- deletion state is lost.

## follower_graph_preserved

Verifies that follower/following relationships are preserved or explicitly reported as partial.

Expected behavior:

- followers are preserved where the platform supports restoration;
- following relationships are preserved where the platform supports restoration;
- unsupported or manual relationship restoration is reported as `PARTIAL`, not silently treated as success.

Failure examples:

- relationships are lost without reporting;
- follower counts are misleading;
- manual confirmation requirements are hidden.

## Future check candidates

- block list preservation;
- mute list preservation;
- profile fields preservation;
- pinned posts preservation;
- old link behavior;
- comments/replies/thread integrity;
- direct message exclusion or safety behavior;
- archive completeness scoring;
- cross-service compatibility matrix entries.
