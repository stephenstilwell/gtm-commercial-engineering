# Handbook expansion audit

Audit by the project editor, November 19, 2026. The starting point is the first published handbook revision, `98a153b`.

## Existing repository

| Area | What works | Expansion |
| --- | --- | --- |
| Education | The 13 chapters share a stable structure with diagrams, exercises, failure cases, and primary citations. The three-level roadmap has useful exit artifacts. | Keep chapter URLs and turn the roadmap into three teachable paths. Add a commercial systems boundary exercise and a pipeline attribution exercise. |
| Discovery | The source ledger gives claims contemporary references but uses one flat table. | Keep the citation ledger. Add structured educational and tool entries with license boundaries, maintenance evidence, and links into a practical guide. |
| Implementation | One standard-library CLI covers routing, evidence, offers, and measurement. The fixtures, test suite, and n8n export support safe exercises. | Organize these examples by business problem. Add scenario variations and recovery exercises around the existing commands. Link to companion implementations for public signal collection and website audits. |
| Research | The chapters contain a few labeled hypotheses and experimental practices. | Publish testable protocols with outcomes, disconfirming criteria, and decision boundaries. Identify the proposed status of Commercial Systems Engineering. |
| Maintenance | GitHub Actions runs tests, a strict MkDocs build, and Lychee. Existing issue forms cover resource submissions and review. | Add catalog validation and generated-page drift checks. Add contributor intake for tutorials, projects, and technical examples. Apply the Useful in Practice palette to the existing search and navigation. |

## Inspiration and related projects

Elias Stråvik maintains the three projects reviewed below. The review covered their readmes, navigation, contribution instructions, and repository licenses. All three lists use CC0 1.0 for their repository content. Linked projects have their own licenses.

| Project | What the review found | Applied here |
| --- | --- | --- |
| [Learn GTM Engineering](https://github.com/eliasstravik/learn-gtm-engineering) | A contents menu and a short reader orientation lead into courses, vendor academies, templates, communities, newsletters, and people. A concise contribution section accepts issues and pull requests. | Give readers a short route from each level into free or paid learning material, with prerequisites and an exercise to apply it. |
| [Open Source GTM](https://github.com/eliasstravik/open-source-gtm) | Product, skills, CLI, and playbook groupings sit alongside a separate source-available area. Its contribution guide requires primary license evidence, a canonical public repository, and active maintenance, with a removal process. | Record edition-level license evidence, classify mixed and source-available products explicitly, and validate duplicates before review. |
| [Awesome GTM Engineering](https://github.com/eliasstravik/awesome-gtm-engineering) | Short descriptions and contributions organized by workflow topics make it easy to browse. Broad topical coverage supports quick discovery. | Organize the catalog by the job a practitioner needs to accomplish and link each entry to a guide or lab that explains the trade-off. |

## Information architecture

- **Learn** owns the roadmap, learning resources, and foundational chapters.
- **Explore** owns the generated tool directory, taxonomy, and license views.
- **Build** owns scenario walkthroughs, offline execution, operating checklists, and vendor integration boundaries.
- **Research** owns hypotheses, experimental protocols, and advanced interpretation guides.
- **Project** owns the primary citation ledger, review process, and this audit.

The existing chapter paths and lab interface support links and bookmarks. The catalog data is separate from the technical citation ledger because listing a tool and substantiating a technical claim require different evidence.

## Remaining work

Catalog reviews are point-in-time. Edition boundaries, release activity, and pricing need quarterly re-checks. The core examples use synthetic data and local decision proposals. A useful next contribution is a provider-independent adapter test that demonstrates timeout recovery after a successful remote write. Another is an anonymized, permissioned evidence evaluation set with a written labeling rubric and disagreement procedure. Use the [research protocols](../research/index.md) as a starting point.
