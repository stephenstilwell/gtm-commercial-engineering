# Research agenda

Stephen Stilwell uses **Commercial Systems Engineering** as a proposed framework for designing the software, data, controls, and human decisions that support commercial operations. The framework draws on RevOps, integration engineering, experimentation, and applied AI evaluation. Evaluate it by whether it makes ownership, failure recovery, and evidence easier to reason about.

| Status | How to read it |
| --- | --- |
| **Established practice** | A technique with primary documentation and a defined operational use, such as stable identities, event deduplication, or randomized assignment. |
| **Emerging capability** | A technical interface or operating model that exists. Deployment fit and reliability still need evidence. |
| **Hypothesis** | A claim with an unproven benefit in the proposed setting. State how to test it and what would change your decision. |

## Open protocols

| Question | Protocol |
| --- | --- |
| When does fresher evidence improve qualification and when does it add review work? | [Evidence freshness and oversight](evidence.md) |
| Which customer lifecycle actions remain reliable when events arrive twice or out of order? | [Lifecycle autonomy and replays](lifecycle.md) |
| Which published information helps software produce a correct purchase recommendation? | [Buyer readiness and agent-to-agent commerce](commerce.md) |

Partnership, product-market, and vertical opportunities share one unresolved measurement problem. A plausible signal may reflect the same underlying evidence, an unrepresentative sample, or a real market condition. Begin with the [evidence lab](../build/evidence.md) and its examples of corroboration and contradiction.

## Submit a study

Define the decision, unit of analysis, data source, baseline, outcome, and a disconfirming result. Publish a protocol, versioned synthetic fixtures or an approved data-access description, commands for reproduction, selection limitations, and the result including negative findings. Keep live side effects out of the initial experiment. Escalate proposals that affect people, money, or production systems to the designated owner.

Use the **Tutorial proposal** or **Technical example request** form to discuss the method before committing to an implementation. The [primary-source ledger](../resources.md) is a starting point for citations.
