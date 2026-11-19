# Offline labs

Run from the repository root with Python 3.11+. The lab uses the standard library, synthetic files, and an in-memory SQLite database for routing. It prints JSON and makes no network requests.

Use the [Build walkthroughs](build/index.md) for business context, contracts, and recovery scenarios.

```sh
python examples/gtm_lab.py
python -m unittest discover -s tests -p test_lab.py -v
```

Pass a mode below to see one result. Use `--fixtures PATH` for a copy of the fixture directory or `--policy PATH` for a copy of the policy.

| Mode | Expected result | Try this variation |
| --- | --- | --- |
| `routing` | Seven deliveries, one duplicate, no payload conflicts, six decisions, and two proposed tasks | Change the suppressed event's ID. It still produces no task. Reuse a source and ID with a different subject to observe a conflict. |
| `intelligence` | Four proposals. One is eligible for human review, and three are held for stale, conflicting, or missing evidence | Set the stale source's retrieval timestamp to the policy date and compare the result. |
| `offers` | The USD monthly offer passes. The EUR annual offer is expired and lacks a terms URL | Move the expired offer's date forward and add a reserved HTTPS terms URL. |
| `measurement` | Two of four treatment accounts convert and one of four controls converts. The difference is 25 percentage points, illustrative incremental contribution is $200, and illustrative ROI is 100% | Change a control conversion to true. The observed difference becomes zero while workflow cost remains. |

The policy uses a fixed clock for reproducibility. The measurement fixture illustrates arithmetic with eight accounts. A rollout decision needs a separately designed experiment.

## Optional n8n workflow

Import `examples/n8n/signal-triage.json` and run it manually. It returns four decisions in order: `route_review_task`, `duplicate`, `blocked`, and `manual_review`. The workflow uses embedded synthetic records and makes no outbound calls. See the [workflow tutorial](workflows.md) for a controlled integration exercise.
