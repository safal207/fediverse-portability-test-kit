# Final Submission Checklist

Use this checklist before submitting the Fediverse Portability Test Kit proposal.

## Repository readiness

- [ ] README explains the project in the first 30 seconds.
- [ ] README includes install and run commands.
- [ ] CLI runs locally:

```bash
python -m pip install -e .
fediverse-portability-test run --fixture mastodon-like --output portability-report.json
```

- [ ] Strict CI mode works:

```bash
fediverse-portability-test run --fixture mastodon-like --fail-on-partial
```

- [ ] Generated report validates against `schemas/portability-report.schema.json`.
- [ ] Unit tests pass locally:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p 'test_*.py'
```

- [ ] GitHub Actions is green on `main`.
- [ ] `examples/public-report-summary.md` is readable by non-technical reviewers.
- [ ] `docs/COMPATIBILITY_MATRIX_TEMPLATE.md` exists.
- [ ] `CONTRIBUTING.md` exists.

## Proposal documents

- [ ] `docs/APPLICATION_DRAFT.md` reviewed.
- [ ] `docs/NLNET_FORM_ANSWERS.md` reviewed.
- [ ] `docs/BUDGET_AND_MILESTONES.md` matches the requested amount.
- [ ] `docs/EXISTING_EFFORTS.md` explains how this differs from existing work.
- [ ] `docs/ROADMAP_TO_REAL_ADAPTER.md` avoids overclaiming real-service support.
- [ ] `docs/GENAI_DISCLOSURE.md` is accurate.

## Scope and claims

- [ ] The proposal does not claim certification.
- [ ] The proposal does not claim legal compliance.
- [ ] The proposal does not claim production Mastodon compatibility yet.
- [ ] The proposal clearly says the current adapter is a synthetic local fixture.
- [ ] The proposal explains that ordinary users benefit from reports but do not need to run the tool.
- [ ] The proposal explains direct users: admins, developers, reviewers, public-interest orgs.

## Budget and milestones

- [ ] Requested amount is EUR 40,000.
- [ ] Milestones add up to EUR 40,000.
- [ ] Milestones have acceptance checks.
- [ ] Milestones are realistic for a small open-source QA toolkit.
- [ ] Pre-grant baseline is separated from grant deliverables.

## Community and ecosystem

- [ ] GitHub issues exist for core work items.
- [ ] There is an issue for collecting Fediverse operator/maintainer feedback.
- [ ] Outreach message is prepared.
- [ ] Any external feedback is captured in issues or docs.

## Submission form

- [ ] Project name finalized.
- [ ] Short abstract fits the form field.
- [ ] Relevant background is accurate.
- [ ] Existing efforts comparison is concise.
- [ ] Technical challenges are stated clearly.
- [ ] GenAI disclosure is included if required.
- [ ] Repository link is included.
- [ ] Contact details are correct.

## Final manual review

- [ ] No private information accidentally included.
- [ ] No impossible promise included.
- [ ] No unsupported technical claim included.
- [ ] README and application text tell the same story.
- [ ] The project sounds like QA infrastructure, not a migration service.
