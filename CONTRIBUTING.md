# Contributing

## Submit a resource

Select **Resource submission** in GitHub’s **New issue** menu. Include the canonical URL, publisher, topic, concrete learner task, date checked, and access or licensing constraints. Eligible primary sources include official specifications, vendor documentation, original research, and government datasets.

## Improve a guide or lab

1. Read the [editorial standards](AGENTS.md) and find the relevant chapter.
2. Show the learner’s starting state and expected result. Use synthetic fixtures and include failure cases.
3. Open new sources and log the check in the [resource index](docs/resources.md). Update related tutorials and navigation.
4. Run the checks below in a Python 3.11+ virtual environment from the repository root.
5. In the pull request, summarize the learner outcome, verification performed, and any vendor-specific step still pending. Submitted material is intended for distribution under the applicable [repository licenses](LICENSING.md). Include attribution for material you have permission to reuse.

```sh
python -m unittest discover -s tests -v
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
```

The site build validates internal links and anchors. CI also checks Markdown URLs with Lychee. Review changed diagrams visually and check that the cited material supports the text.

## Publish the documentation

A maintainer can enable **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Publish documentation** from the default branch in the Actions tab. The workflow builds the same searchable site as the local command.

## Maintain references

Run the [quarterly review](docs/resource-review.md) and update the source record in the same pull request as any affected tutorials.
