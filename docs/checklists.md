# Operational checklists

## Design review

- [ ] Name the workflow owner, business outcome, system of record, and supported population.
- [ ] Map identity keys and relationships. Assign field authority and define how ambiguous matches are resolved.
- [ ] Specify input schema, freshness, retry bounds, deduplication, dead-letter handling, and replay behavior.
- [ ] Define suppression, data classification, retention, reviewer access, and action approval.
- [ ] Set a baseline, target, guardrail, and stop condition.

## Pre-production trial

- [ ] Replay a success, duplicate, stale event, missing owner, ambiguous match, and suppressed record.
- [ ] Reconcile a timeout after a downstream side effect succeeds.
- [ ] Run a shadow evaluation against an approved test population.
- [ ] Verify that reviewers can inspect evidence, override a proposal, and leave an audit record.
- [ ] Confirm the kill switch blocks queued side effects and assign an owner for in-flight work.

## Research and vendor changes

- [ ] Record the source owner, URL, date retrieved, coverage, and supporting claim.
- [ ] Check endpoint generation, scopes, export redaction, and test-account permissions.
- [ ] Flag dated and contradictory evidence in the output.
- [ ] Schedule follow-up through the [resource review process](resource-review.md).
