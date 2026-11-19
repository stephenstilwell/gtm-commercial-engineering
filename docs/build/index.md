# Build practical workflows

Choose a commercial problem and work it through with synthetic data before connecting a vendor or a CRM. The examples reuse the same small command-line lab so you can compare decision policies and trace their output.

| Problem | Walkthrough | What you can verify |
| --- | --- | --- |
| Turn a signal into an owned follow-up | [Signal-to-opportunity routing](routing.md) | Replay, CRM identity, and an exception queue |
| Make qualification and research auditable | [Evidence and review pipelines](evidence.md) | Provenance, contradictory evidence, partnership and vertical review |
| Catch missed customer milestones | [Lifecycle and measurement](lifecycle.md) | Onboarding follow-up, suppression, and a synthetic trial |
| Prepare offers for AI-assisted buying | [Commerce readiness](commerce.md) | Expiry, billing units, and a machine-readable terms boundary |

## Run the offline lab

Use Python 3.11 or newer in the repository root. The example uses the standard library and synthetic fixtures. Read the [lab interface](../labs.md) for all commands and expected outputs.

```sh
python examples/gtm_lab.py
python -m unittest discover -s tests -p test_lab.py -v
```

The lab proposes internal work and produces local reports. Production operation adds authorization at action time, durable storage, monitoring, and reconciliation. Practice those boundaries with the [operational checklists](../checklists.md).

## Integration status

| Example | Reviewed surface |
| --- | --- |
| Python CLI, SQLite routing, and synthetic fixture mutations | Reproduced through local commands and automated regression tests |
| [n8n, Clay, Apollo, and HubSpot](../workflows.md) | The n8n Code node decision logic was executed locally. Editor import and live vendor account steps need environment-specific verification |
| Companion repositories | Public readmes and licenses reviewed. Run their own quickstarts for their broader demos |
