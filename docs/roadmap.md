# Learning roadmap

Start at the level whose prerequisite skills you already use. Each path produces an artifact another practitioner can review. The [learning directory](learn/resources.md) lists the cost, difficulty, and purpose of recommended material.

| Path | Starting skills | Exit artifact |
| --- | --- | --- |
| [Beginner](#beginner) | Spreadsheets and basic record relationships | A handoff diagram and authority table |
| [Intermediate](#intermediate) | JSON, HTTP, and either basic SQL or workflow automation | A replayable dry run with audit reasons and an experiment plan |
| [Advanced](#advanced) | Event processing, data governance, and experiment design | An evaluated proposal workflow with an authorization boundary and a rollout decision |

## Beginner

**Objectives.** Identify actor, authority, grain, and exception ownership. A new demo request is an observation. Turning it into an owned task is a policy decision that depends on account identity and current ownership.

1. Read [GTM fundamentals](fundamentals.md), then redraw the [commercial systems diagram](learn/systems.md) around a handoff you know.
2. Use [RevOps architecture](revops.md) and [CRM design](crm.md) to identify which system can author each field. Give the account a stable ID and define which values enrichment may suggest.
3. Trace the demo and onboarding records in the [routing lab](build/routing.md) and compare them with the [lifecycle diagram](lifecycle.md). Expect two owned task proposals from the original fixture. Delete an owner in a scratch copy and check where the held proposal goes.

**Exit check.** A reviewer can point to the authoritative account field, the business outcome, and the manual review owner. If your join uses company display name, add two similar names and explain what evidence would resolve the collision.

**Recommended resource.** Start with the [free HubSpot Academy RevOps course](learn/resources.md#hubspot-revenue-operations-certification) to compare process and systems vocabulary.

## Intermediate

**Objectives.** Validate a signal, settle retries, check suppression, and distinguish attributed pipeline from incremental improvement. A retry and a new buying observation may arrive through the same integration. Stable identity and payload checks explain which path to take.

1. Inspect the [event architecture](signals.md), then use the [signal-to-opportunity lab](build/routing.md) to test exact replay, conflicting payload, and suppression. Expect one extra duplicate for a repeat, a recorded conflict for a changed payload using the original key, and no extra side effects.
2. Map [enrichment and workflow integration](workflows.md) to staging and authoritative fields. Run the [governance checklist](governance.md) against an example timeout and pick a safe reconciliation step before retry.
3. Work through the [pipeline attribution ledger](learn/pipeline-attribution.md) and [measurement exercise](measurement.md). Reconcile credit to the source amount, then record assignment unit, outcome window, and false-routing guardrail for a trial.

**Exit check.** The dry run exposes expected outputs and reason codes. The experiment design keeps assigned accounts in scope when processing fails. If you count every touch as a deal, compare first and last touch with the one-row-per-opportunity total.

**Recommended resources.** Use the [CloudEvents specification](learn/resources.md#cloudevents-specification) for event identity and [OpenTelemetry signals](learn/resources.md#opentelemetry-signals) to decide how to diagnose failed handoffs.

## Advanced

**Objectives.** Separate retrieval from authority, define abstention and expiry, and decide whether a new system is ready for wider use. A plausible claim can still refer to an unrelated entity, contradictory evidence, or a stale observation.

1. Follow the [agent review architecture](agents.md) and [evidence lab](build/evidence.md). Reproduce missing evidence, subject mismatch, and contradiction. Take one proposal from eligible to held by adding an independently sourced synthetic contradiction.
2. Compare [partnership](partnerships.md), [product-market](product-market.md), and [vertical](verticals.md) research. Write a sampling and labeling plan that preserves each source’s coverage and the counterevidence.
3. Use the [agentic commerce architecture](commerce.md) and [offer validation lab](build/commerce.md). Verify that invalid terms and expired quotes stay withheld. Pick a [research protocol](research/index.md) and specify a result that would disconfirm your hypothesis.

**Exit check.** The review packet includes a baseline, authorization boundary, expiry rule, and a written expand, revise, or stop decision. If the model can both propose and approve an action, put approval under a deterministic policy and name the accountable human.

**Recommended resources.** Use the [NIST AI RMF Playbook](learn/resources.md#nist-ai-rmf-playbook) to define review controls and the [Microsoft Experimentation Platform bibliography](learn/resources.md#microsoft-experimentation-platform) to study assignment and metric interpretation.
