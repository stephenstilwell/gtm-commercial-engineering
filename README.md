# GTM Commercial Engineering

**An open engineering handbook from Useful in Practice.**

Learn how go-to-market and revenue systems turn signals into accountable decisions. Build a workflow, inspect what happens when it fails, and measure whether it improves the outcome.

For GTM engineers, RevOps practitioners, solutions engineers, technical founders, product managers, and automation builders.

## Find your starting point

| Path | Start here |
| --- | --- |
| **Learn** | [Learning roadmap](docs/roadmap.md) · [Courses, communities, and primary references](docs/learn/resources.md) |
| **Explore** | [Resource categories](docs/explore/index.md) · [Tool catalog with access and license evidence](docs/explore/catalog.md) |
| **Build** | [Workflow walkthroughs](docs/build/index.md) · [Offline labs and expected outputs](docs/labs.md) |
| **Research** | [Research agenda and experiments](docs/research/index.md) · [Primary-source ledger](docs/resources.md) |

## Run your first example

Use Python 3.11 or later from the repository root. The lab uses synthetic fixtures and needs no API keys.

```sh
python examples/gtm_lab.py routing
```

Follow one [signal-to-opportunity walkthrough](docs/build/routing.md) from event to task proposal. Inspect the [sample contracts and fixtures](examples/README.md) or run all four modes with `python examples/gtm_lab.py`.

## Browse the searchable handbook

In a Python virtual environment:

```sh
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

Open the local address printed by MkDocs.

## Contribute

Suggest a resource, report outdated information, propose a tutorial, submit an open-source project, or request a technical example. The [contribution guide](CONTRIBUTING.md) explains what reviewers need. See the [editorial standards](AGENTS.md) and [quarterly review process](docs/resource-review.md).

## Inspiration and related projects

Thanks to Elias Stråvik for [Learn GTM Engineering](https://github.com/eliasstravik/learn-gtm-engineering), [Open Source GTM](https://github.com/eliasstravik/open-source-gtm), and [Awesome GTM Engineering](https://github.com/eliasstravik/awesome-gtm-engineering). The [handbook audit](docs/maintainer/handbook-audit.md) describes how those three projects informed this structure.

Maintained by Stephen Stilwell at [Useful in Practice](https://stephenstilwell.com/). Original code and machine configuration use MIT. Original prose, diagrams, and educational fixtures use CC BY 4.0. See [licensing and attribution](LICENSING.md).
