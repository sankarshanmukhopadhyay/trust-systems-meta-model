---
owner: maintainers
last_reviewed: 2026-03-23
applicable_version: v0.14.0
tier: 0
---

# TSMM Binding: A2A Protocol

The Agent2Agent (A2A) protocol enables communication and interoperability between
opaque agentic applications. Its foundational invariants — structured discovery,
capability negotiation, stateful task execution, and agent opacity — map cleanly onto
TSMM's agent interaction extension, introduced in v0.13.0 and completed in v0.14.0.

## Primary mappings

- **Agent Card (public)** → `ServiceDescriptor` (`disclosurePolicy: public`)
- **Agent Card (authenticated extended)** → `ServiceDescriptor` (`disclosurePolicy: authenticated`)
- **Skill** → `SkillContract` — `inputModes`, `outputModes`, `tags` map directly; `authorizationScope` is the governance layer TSMM adds
- **contextId** → `InteractionContext.id` — TSMM adds inherited authority, evidence, and re-authorization policy to the governance envelope A2A's contextId implies
- **Task** → `InteractionTask` — status transitions carry explicit governance significance in TSMM
- **input-required / auth-required task states** → `InteractionTask` + `AuthorizationCheckpoint` — TSMM treats these as governance checkpoints, not delivery states
- **Extensions** → `ExtensionContract` — negotiation record with requiredness, negotiated status, and failure handling
- **Agent opacity invariant** → `OpacityBoundary` — TSMM makes the governance consequence of A2A's foundational opacity principle explicit
- **Peer interaction model** → `PeerTrustRelation` — TSMM formalizes trust basis and scope for lateral agent relationships
- **Message/Artifact/Part** → `ContentProvenancePolicy` — governance obligations by modality, not wire payload structure
- **SSE streaming / push notifications** → `ObservabilityMode` — governance consequences of delivery model

## Why the mapping is not 1:1

TSMM operates one layer below protocol mechanics. It models the trust-semantic invariants
that A2A's protocol elements instantiate. Three patterns characterise the non-1:1 mapping:

**TSMM adds governance structure A2A implies but does not formalize.** A2A's contextId
exists; TSMM's InteractionContext adds the governance record of what authority and evidence
carry within that context. A2A's security schemes are declared; TSMM models how they resolve
to AuthorizationCheckpoints at runtime.

**TSMM does not replicate wire mechanics.** JSON-RPC method names, SSE framing details, and
retry semantics belong to A2A. ObservabilityMode captures the governance consequence of
those mechanics — not the mechanics themselves.

**TSMM makes A2A design principles machine-readable.** Agent opacity and peer interaction
are A2A's foundational design principles. They have no explicit schema counterpart in A2A.
OpacityBoundary and PeerTrustRelation give them machine-readable governance representation.

## Related artifacts

- Machine-readable binding: `bindings/a2a/tsmm-a2a-binding.json`
- Crosswalk: `docs/crosswalks/a2a-crosswalk.md`
- A2A protocol repository: `https://github.com/a2aproject/A2A`
