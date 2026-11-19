# Lifecycle autonomy and replays

**Established practice.** A replayable event log, an owned exception queue, and a downstream reconciliation record help operators recover from partial failure.

**Emerging capability.** A commercial agent can classify an exception or draft a next action under a deterministic authorization policy. It can work within an approval flow while operators collect evidence about its errors.

**Hypothesis.** Automating low-risk task proposals can reduce time to review without raising incorrect actions or manual queue age. Sending communications or updating commercial records needs its own error budget and approval policy.

## Reproduce a shadow-routing exercise

1. Run `python examples/gtm_lab.py routing` and record task count, deduplication count, and review reasons. This output is a proposed action stream.
2. In a copy of the routing fixture, add an exact duplicate, change a second copy’s subject while retaining the first copy’s identity, and remove the onboarding owner. Expect one additional duplicate, one payload conflict, and no onboarding task. Route the ownership exception and identity conflict to different operators in your design.
3. Draft a reconciliation record for a downstream action with an unknown outcome. Include the semantic action key, attempt count, observed state, and a decision to retry or hold. Practice reading remote state before deciding how to recover.
4. For a controlled trial, compare isolated shadow output against the current process on the same approved events. Measure time to owned review, false assignments, repeat side effects, and unresolved queue age before expanding scope.

A repeat side effect or higher error rate at the same review load can disconfirm the hypothesis. The fixture covers decisions in memory. To study execution reliability, add a mock task adapter that commits and then returns a timeout.

- Delivery identity. [CloudEvents 1.0.2](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md)
- Retry and reconciliation context. [Stripe webhooks](https://docs.stripe.com/webhooks)
- Cohort and causal measurement boundaries. [Pipeline measurement and attribution](../learn/pipeline-attribution.md)
