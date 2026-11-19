# GTM Commercial Engineering

**An open field guide from Useful in Practice for building reliable commercial systems.**

Follow a commercial signal from intake to a measured outcome. Learn to model records, make routing decisions auditable, evaluate research, and test workflows before connecting a production CRM or AI agent.

For GTM engineers, solutions engineers, RevOps professionals, technical founders, product managers, and automation builders.

## Start here

1. Pick a track in the [learning roadmap](docs/roadmap.md).
2. Run the [offline lab](docs/labs.md) from the repository root with Python 3.11 or later. It uses synthetic fixtures and requires no API keys.
3. Use the [first architecture guide](docs/fundamentals.md) to define the contract for a workflow you own.

```sh
python examples/gtm_lab.py
```

## Field guide

| Area | Chapters |
| --- | --- |
| Commercial systems | [GTM engineering fundamentals](docs/fundamentals.md) · [Revenue operations architecture](docs/revops.md) · [CRM data models and enrichment](docs/crm.md) |
| Workflow engineering | [Buying signals and event-driven workflows](docs/signals.md) · [n8n, Clay, Apollo, and HubSpot](docs/workflows.md) · [Customer lifecycle engineering](docs/lifecycle.md) |
| Intelligence | [Partnership intelligence](docs/partnerships.md) · [Product-market intelligence](docs/product-market.md) · [Vertical opportunity intelligence](docs/verticals.md) |
| AI and commerce | [AI agents for business operations](docs/agents.md) · [Agentic commerce and AI buyer readiness](docs/commerce.md) |
| Operating controls | [Security, compliance, and data governance](docs/governance.md) · [Measurement, experimentation, and ROI](docs/measurement.md) |

## Build and contribute

- [Labs and expected results](docs/labs.md) · [Sample contracts and workflow](examples/README.md) · [Operational checklists](docs/checklists.md)
- [Curated primary sources](docs/resources.md) · [Quarterly review process](docs/resource-review.md)
- [Contributing](CONTRIBUTING.md) · [Editorial standards](AGENTS.md) · [Licensing and attribution](LICENSING.md)

Build the searchable documentation locally in a Python 3.11+ virtual environment:

```sh
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

Open the local address printed by MkDocs. The [contributor guide](CONTRIBUTING.md) covers checks and optional GitHub Pages publishing.

Original code and machine configuration are MIT-licensed. Original prose, diagrams, and educational fixtures are CC BY 4.0.
