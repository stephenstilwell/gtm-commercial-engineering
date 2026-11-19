# Evidence freshness and human oversight

**Established practice.** Source provenance, timestamps, and repeatable review decisions make research auditable. Freshness captures time since observation or retrieval. It does not measure truth or independence.

**Emerging capability.** An agent can propose a claim with structured references. A verifier can reject IDs absent from the retrieval log, and a human can check the actual passage.

**Hypothesis.** A freshness threshold and a contradiction gate reduce unsupported recommendations at comparable reviewer effort. The right threshold may differ for company facts, partnership intent, and market observations.

## Reproduce a policy sensitivity check

1. Run `python examples/gtm_lab.py intelligence` with the default policy. One proposal is eligible and three are held. Record the reason for each outcome.
2. Copy `examples/config/policy.json` twice. Set `max_evidence_age_days` to 7 in one copy and 14 in the other. Run `python examples/gtm_lab.py intelligence --policy PATH` for both. In the fixture, the 7-day threshold holds all four proposals. The 14-day threshold allows the same partner proposal as the default 30-day threshold. The fresh contradiction remains held in all runs.
3. Hold the threshold constant and add an independently sourced synthetic contradiction with the partner subject. Attach its ID and verify that the proposal is held. The [evidence lab](../build/evidence.md) documents the record shape.

## Evaluate with approved data

Create a labeled benchmark at the claim level. Sample by source and job, then label support, contradiction, time sensitivity, and duplicate underlying observations. Use a second reviewer for an independently chosen subset and preserve disagreements. Compare against a manual rubric and record unsupported claims among eligible proposals, eligible coverage, and reviewer time. Decide acceptable error and coverage before running the study.

Revise the hypothesis if unsupported claims persist at the same rate, coverage falls below the agreed floor, or work shifts to a more expensive manual queue. The bundled records demonstrate a policy decision and cannot estimate performance on real data.

- Operational risk and review methods. [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- Controls for untrusted input and tool permissions. [OWASP Top 10 for LLM applications](https://owasp.org/projects/top-10-for-large-language-model-applications)
