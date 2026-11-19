# Buyer readiness and agent-to-agent commerce

**Established practice.** Product and offer data can carry identifiers, prices, currency, and availability. A binding quote needs authoritative terms and an approval path.

**Emerging capability.** The Universal Commerce Protocol defines ways to publish capabilities and negotiate supported interfaces. Implementation and transaction compatibility depend on the specific sellers, platforms, protocol versions, and authorized actions.

**Hypothesis.** Buyers or their assistants produce fewer incorrect comparisons when price versions, billing units, and expiry are explicit in both the human page and machine-readable offer.

## Prototype a reproducible comparison

1. Run `python examples/gtm_lab.py offers`. Keep one valid and one expired offer. Copy the fixtures and repair the expired offer’s terms URL and expiry for a second treatment. Record the validation outcome in both sets.
2. Create two synthetic comparison inputs with equivalent commercial terms. Put the amount, currency, renewal period, and expiry in prose in one set and explicit structured fields in the other. Keep the offer IDs and reviewer questions fixed.
3. Have a reviewer label the correct amount, billing period, renewal commitment, eligibility, and whether the quote has expired. For any assistant under test, capture its answer, evidence reference, whether it abstains when terms conflict, and the protocol version assumed.
4. Compare error rates and inappropriate certainty by outcome type. Revise the hypothesis if structure fails to reduce meaningful errors or encourages confident use of outdated data. Do not enable checkout in this experiment.

The [commerce exercise](../build/commerce.md) links to a companion project with two offline public-site audit samples. Audit results describe observable publisher data. A purchase success rate or AI recommendation frequency requires a separate study.

- Product and offer vocabulary. [Schema.org Offer](https://schema.org/Offer)
- Capability and protocol contracts. [Universal Commerce Protocol specification](https://ucp.dev/2026-08-25/specification/overview/)
