# Editorial standards

Apply these standards to every change in this repository.

- Define terms on first use and explain the operational decision each component supports. Each major guide needs an introduction, original Mermaid architecture, implementable tutorial with expected results, failure modes and remedies, and relevant primary sources.
- Use synthetic records and reserved domains in examples. Label hypothetical scenarios, experimental practices, and author hypotheses at the point of use. Avoid fictional case studies and unsupported benchmarks.
- Open each external reference, verify that it supports the adjacent claim, and record the verification date in the resource index. Preserve canonical or versioned URLs. Keep unverified candidates in their submission issues pending review.
- Write original prose, code, and diagrams. Attribute reused third-party material and preserve applicable license notices. Check compatibility before adding material.
- For vendor specifics, identify the product surface and version where available, and call out plan, scope, or configuration dependencies. Keep credentials and customer data out of examples and workflow exports.
- Explain identity, replays, field authority, and escalation when workflows mutate records or affect customers. Keep consent and suppression decisions outside model output.
- Run the lab tests and strict docs build before requesting review. Document tutorial commands from the repository root and include expected results. Add a targeted regression test when changing lab behavior.
- Use relative links inside the repository. Keep MkDocs navigation, README, and roadmap synchronized. Verify Mermaid rendering in GitHub and MkDocs.
- Follow the [resource review procedure](docs/resource-review.md) for changed external references.
- Use [catalog.json](catalog/catalog.json) as the source of truth for tool and learning entries. Regenerate both Markdown views with `python scripts/catalog.py` and run `python scripts/catalog.py --check` during verification.
- For catalog claims, manually review license scope, edition boundaries, price basis, status evidence, and fit with the linked exercise. An HTTP success or GitHub license label cannot establish those claims by itself.
- Label established practice, emerging capability, and hypotheses in research. Give experimental protocols a baseline, observable outcome, disconfirming criterion, and reproduction instructions.
