---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 0
---

# TSMM Binding: AIS-1

> **Experimental binding:** included for comparative modelling, not as a mature or complete trust-stack profile. See the [TSMM maturity model](../maturity-model.md).

AIS-1 is best understood as a **bonded agent identity and accountability substrate**. It gives a software agent a durable identifier, links that agent to a sponsor through a persistent bond, and surfaces a tiered trust signal that a verifier can check.

That makes AIS-1 relevant to TSMM, but the fit is specific. AIS-1 does not replace delegation protocols, runtime authorization, or full provenance-bearing transport. It contributes the lower layer that answers a narrower question: **who stands behind the agent, under what published bond state, and with what coarse assurance tier?**

## Primary mappings

- **AIS-1 Agent Card** → `Agent`
- **AIS-1 Sponsor Card** → `GovernanceAuthority`
- **AIS-1 bond** → composite trust state spanning `TrustDecision`, `Assessment`, and lifecycle-aware `Effect`
- **`did:ais1` identifier** → durable `Agent` identifier surface
- **AIS-1 tier (Basic / Verified / Sovereign)** → `AssuranceProfile`
- **Verifier result** → `Assessment`
- **Suspension / revocation** → trust-relevant `Effect`

## Why the mapping is not 1:1

TSMM models trust-semantic structure one layer below protocol and application mechanics. AIS-1 exposes an identity substrate with accountability semantics, but three gaps remain visible when it is normalized into TSMM.

**Bond is not delegation.** The bond states that an agent is backed by a sponsor. It does not, by itself, prove that the agent may spend funds, sign regulated filings, invoke a privileged workflow, or act within a bounded runtime scope.

**Tier is not complete assurance.** The Basic, Verified, and Sovereign labels are useful trust inputs, but TSMM treats them as profile-governed signals that still require verifier interpretation, policy context, and sometimes supplemental evidence.

**Verification is not provenance.** AIS-1 bond lookup and status checks improve accountability. They do not automatically produce message-level authenticity, content provenance, or transport security guarantees for every downstream interaction.

## How to use this binding

Use this binding when you need to compare AIS-1 with other trust systems, or when you need to normalize AIS-1 into cross-repo artifacts without semantic drift.

Typical downstream uses include:

- turning AIS-1 constructs into graph-comparable TSMM nodes and edges
- feeding AIS-1 identity state into schema profiles in `trust-infrastructure-schemas`
- clarifying verifier interpretation rules in `agent-name-assurance-baseline`
- keeping delegation and authority claims separate from bonded identity claims

## Related artifacts

- Machine-readable binding: `bindings/ais1/tsmm-ais1-binding.json`
- Constraint set: `bindings/ais1/constraints.json`
- Crosswalk: `docs/crosswalks/ais1-crosswalk.md`
- Example system graph: `examples/systems/ais1-bonded-agent-system.json`
