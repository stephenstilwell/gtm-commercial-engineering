# Contributing

## Start with an issue

| What you want to share | Choose |
| --- | --- |
| A course, reference, community, or other useful resource | **Resource submission** |
| A changed plan or license, an outdated guide, or a quarterly review | **Resource review** |
| An instructional walkthrough | **Tutorial proposal** |
| A project with public software license evidence | **Open-source project submission** |
| A workflow with a business problem and expected output | **Technical example request** |

Include a canonical URL, publisher, concrete learner task, date checked, and any access or licensing constraints. Cite primary references when the submission supports a substantive claim.

## Update the catalog

Edit [catalog.json](catalog/catalog.json), then run `python scripts/catalog.py` to regenerate the two Markdown views. Keep both output pages in the pull request. Use the [catalog schema](catalog/catalog.schema.json) to check required fields and controlled values. Reuse an existing entry if a product solves several problems.

For software, record the reviewed component or edition, the maintainer, official cost and activity evidence, and an existing guide. If classifying it as open-source, check the exact upstream license and the applicable OSI listing. Record enterprise boundaries for mixed-license or source-available repositories. Record the public activity date when available. Treat repository activity as a point-in-time observation.

The reviewer opens sources, checks the license and edition scope, reconciles the problem statement with current documentation, and confirms that the linked exercise fits. Automated schema and link checks give reviewers a consistent baseline.

## Improve a guide or lab

1. Read the [editorial standards](AGENTS.md) and find the relevant chapter.
2. Show the learner’s starting state and expected result. Use synthetic fixtures and include failure cases.
3. Open new sources and log the check in the [resource index](docs/resources.md). Update related tutorials and navigation.
4. Run the checks below in a Python 3.11+ virtual environment from the repository root.
5. In the pull request, summarize the learner outcome, verification performed, and any vendor-specific step still pending. Submitted material is intended for distribution under the applicable [repository licenses](LICENSING.md). Include attribution for material you have permission to reuse.

```sh
python -m pip install -r requirements-docs.txt
python scripts/catalog.py --check
python -m unittest discover -s tests -v
python -m mkdocs build --strict
```

The site build validates internal links and anchors. CI also checks Markdown URLs with Lychee. Review responsive navigation, keyboard focus, search, and changed diagrams in the rendered site. Verify that cited material supports the text.

## Publish the documentation

A maintainer can enable **Settings → Pages → Build and deployment → Source → GitHub Actions**, then run **Publish documentation** from the default branch in the Actions tab. The workflow builds the same searchable site as the local command.

## Maintain references

Run the [quarterly review](docs/resource-review.md) and update the source record in the same pull request as any affected tutorials.
