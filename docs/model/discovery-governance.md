---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 0
---


# Discovery Governance Model

Discovery is a governance event. Before a trust system can evaluate a service, agent, registry, issuer, verifier, or delegated actor, it must first decide whether the descriptor it discovered is authoritative enough to rely on.

TSMM v0.19.0 treats discovery as a control-plane surface rather than a convenience lookup. This generalizes the A2A pattern of public Agent Cards, authenticated extended Agent Cards, curated registries, and private configuration into a reusable trust-system abstraction.

## Governance objective

A conformant discovery model answers five questions:

1. **Where did the descriptor come from?**
2. **Who is authorized to publish or mediate it?**
3. **What disclosure class applies to the descriptor?**
4. **How fresh and integrity-bound is the descriptor?**
5. **What must the relying party do when discovery fails, is stale, or lacks integrity?**

## Discovery modes

| Mode | TSMM meaning | Typical use |
| --- | --- | --- |
| `well-known-uri` | Domain-bound public descriptor discovery | Public agent or service endpoint |
| `curated-registry` | Governance-mediated discovery through a registry or catalog | Enterprise agent marketplace, trust registry, assurance catalog |
| `direct-configuration` | Descriptor known through configuration or contract | Private integration, static B2B connection |
| `authenticated-extended` | Descriptor details disclosed after authentication or authorization | Sensitive skills, internal endpoints, elevated capabilities |
| `restricted-catalog` | Scoped catalog visibility under institutional policy | Regulated ecosystem, internal platform, consortium |

## Normative requirements

- A discovery model **MUST** identify the discovered subject and descriptor.
- A discovery model **MUST** declare a discovery mode and trust basis.
- A descriptor used for operational authorization **SHOULD** be integrity-bound.
- Authenticated or restricted descriptors **MUST** be governed by an access policy.
- Authenticated extended descriptors **MUST** require signature verification or an equivalent integrity control.
- A freshness policy **MUST** define cache behavior, revalidation expectations, and stale-descriptor handling.
- A relying party **MUST NOT** silently elevate capability or authority based only on a public descriptor.

## Evidence produced

Discovery governance produces evidence such as descriptor fetch records, registry query receipts, signature verification results, cache validation outcomes, and access-control decisions for authenticated descriptors.

## Schema and example

- Schema: `schemas/tsmm-discovery-governance.schema.json`
- Example: `examples/agent-discovery-governance-instance.json`
- Valid vector: `validation/test_vectors/valid/discovery-governance-valid.json`
- Invalid vector: `validation/test_vectors/invalid/discovery-governance-missing-integrity.json`
