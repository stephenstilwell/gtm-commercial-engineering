# Learning roadmap

Start at the level whose prerequisite skills you already use. Practice with the supplied fixtures, then apply the deliverable to one low-risk workflow you can observe.

| Level | Starting skills | Read and practice | Deliverable and exit check |
| --- | --- | --- | --- |
| Beginner | Spreadsheets and basic record relationships | [Fundamentals](fundamentals.md) → [RevOps architecture](revops.md) → [CRM and enrichment](crm.md) → [Lifecycle](lifecycle.md) | A flow diagram and field ownership table for one handoff. Point out the authoritative fields, deduplication key, and path for a missing owner. |
| Intermediate | JSON, HTTP, and basic SQL or automation tools | [Signals](signals.md) → [Tool workflows](workflows.md) → [Governance](governance.md) → [Measurement](measurement.md) | A dry run with an audit trail, suppression rule, replay test, and baseline. Show that two deliveries produce one action and a suppressed account produces none. |
| Advanced | Event processing, data governance, and experimental design | [Agents](agents.md) → [Partnerships](partnerships.md) → [Product-market intelligence](product-market.md) → [Vertical intelligence](verticals.md) → [Agentic commerce](commerce.md) | An evidence-backed decision system with an evaluation set, permission boundary, expiry rules, and a written decision to expand, revise, or stop. |

## Practice milestones

- **Beginner.** Trace the synthetic demo request from incoming event to proposed owner. Explain why a mutable company name is a poor join key.
- **Intermediate.** Replay a signal, introduce a suppressed account, and compare recorded decisions with the task list. Document the live equivalent's rollback strategy.
- **Advanced.** Add a contradictory source and an expired offer. Write a measurement plan before increasing exposure. Use the [offline lab](labs.md) for all three exercises.
