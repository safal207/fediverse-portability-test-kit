# Security Policy

Fediverse Portability Test Kit is currently a pre-alpha QA toolkit.

## Current scope

The current version uses a local synthetic fixture.

It does not test real user accounts.

It does not claim production compatibility with Mastodon, PeerTube, Lemmy, or all ActivityPub services yet.

## Safety rules

- Do not run experimental adapters against real user accounts.
- Use dedicated test accounts only.
- Do not publish private user data in reports.
- Treat privacy widening as a critical failure.
- Report unsupported checks as `SKIP` or `PARTIAL`, not as success.
- Document cleanup behavior for any future real-service adapter.
- Make destructive operations explicit and opt-in.

## Privacy-sensitive failures

The following issues should be treated as high severity:

- private or followers-only posts becoming public;
- deleted content reappearing as live content;
- private media becoming publicly accessible;
- block or mute lists being lost silently;
- reports containing real private user data.

## Reporting security issues

Please avoid public disclosure of issues that could expose private data, weaken visibility settings, or damage live accounts.

Open a private security advisory where available, or contact the maintainer directly before publishing details.
