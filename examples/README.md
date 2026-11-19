# Reproducible examples

From the repository root, run `python examples/gtm_lab.py` with Python 3.11+. The [lab guide](../docs/labs.md) lists commands, expected results, and variations.

Start with the [Build walkthroughs](../docs/build/index.md) to map the fixture and CLI output to a commercial problem. To modify a fixture without affecting the baseline, copy the fixture directory and pass it with `--fixtures PATH`.

| File | Purpose |
| --- | --- |
| [gtm_lab.py](gtm_lab.py) | Offline routing, intelligence review, offer validation, and measurement |
| [Sample policy](config/policy.json) | Fixed clock, freshness windows, routing rules, and measurement assumptions |
| [Event contract](config/signal.schema.json) | CloudEvents-inspired JSON Schema for the inputs |
| [Fixture directory](fixtures/) | Synthetic datasets |
| [n8n workflow](n8n/signal-triage.json) | Manual dry run with embedded fixtures |

The SQLite transaction couples event claims to decisions and task proposals. The n8n workflow demonstrates decision logic within a single execution. See [buying signals](../docs/signals.md) for durable delivery and replay handling.
