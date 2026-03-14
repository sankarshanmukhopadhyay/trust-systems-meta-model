---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 0
---

# TSMM Graph Model

The TSMM Graph Model introduces a machine-readable representation of the Trust Systems Meta Model. Its job is simple: take the prose abstractions in TSMM and express them as nodes, edges, profiles, and governance constraints that tooling can inspect.

This is the point where the repo stops being only an architectural reference and starts acting like executable infrastructure design. A trust model that cannot be represented in a machine-readable way is still useful, but it remains trapped in the land of elegant PDFs and committee eyebrows.

## Why the graph layer exists

The conceptual TSMM documents define entities, relationships, governance context, evidence, assessment, and trust effects. Implementers still need a practical way to:

- represent a trust ecosystem as a graph
- validate whether a relationship is structurally valid
- package reference ecosystem topologies for reuse
- build tooling such as visualizers, validators, registries, and conformance harnesses

The graph layer addresses that gap.

## Core components

The executable layer now includes six practical elements:

1. `schemas/tsmm-graph.schema.json` — canonical graph schema for TSMM nodes and edges
2. `examples/tsmm-ecosystem-example.json` — reference ecosystem graph instance
3. `scripts/validate_tsmm_graph.py` — graph validator with schema and semantic checks
4. `examples/profiles/` — reusable graph profiles for recurring ecosystem patterns
5. `scripts/render_tsmm_graph.py` — renderer for Mermaid and DOT outputs
6. `examples/registries/tsmm-registry-example.json` — registry publication example that indexes graph artifacts for discovery

## Node classes

The schema currently supports the following node classes:

- `TrustDomain`
- `GovernanceAuthority`
- `TrustRegistry`
- `RegistryService`
- `Issuer`
- `Verifier`
- `Subject`
- `Agent`
- `Credential`
- `Policy`
- `AssuranceProfile`
- `EvidenceBundle`
- `Assessment`
- `TrustDecision`
- `Effect`
- `RelyingParty`

These are not arbitrary labels. They are constrained abstractions aligned with the existing TSMM entity and evaluation model.

## Relationship classes

The schema and validator support a controlled relationship vocabulary:

- `governs`
- `defines`
- `operates`
- `registers`
- `authorizes`
- `issues`
- `verifies`
- `asserts`
- `delegates`
- `constrains`
- `substantiates`
- `assesses`
- `informs`
- `produces`
- `reliesOn`
- `anchors`

The validator checks not only whether the JSON is syntactically valid, but also whether a given relationship is used between permitted node types.

## What gets validated

The validator currently checks for:

- schema conformance
- duplicate node identifiers
- duplicate edge identifiers
- missing node references
- illegal relation pairings
- invalid `evidenceRefs`

That means the graph layer is not just decorative JSON. It can reject structurally incoherent trust topologies before they leak into downstream tooling.

## Reference ecosystem profiles

The initial profile set is intentionally practical:

- `examples/profiles/ssi-ecosystem.json`
- `examples/profiles/agent-trust-network.json`
- `examples/profiles/agent-governance-network.json`
- `examples/profiles/trust-registry-federation.json`
- `examples/profiles/dpi-trust-layer.json`

These profiles help implementers start from known patterns rather than inventing a topology from scratch every time. Reinventing the governance wheel is a beloved industry pastime, but it is not a serious interoperability strategy.

## Example use cases

The graph layer is designed to support:

- trust registry topology description
- credential ecosystem mapping
- delegated agent governance modeling
- assurance and evidence traceability
- profile-driven conformance tooling
- graph visualization and inspection

## Position within TSMM

The graph model does not replace the conceptual documentation. It operationalizes it.

- The conceptual documents explain what the abstractions mean.
- The graph schema expresses those abstractions as machine-readable structures.
- The validator enforces structural discipline.
- The profile examples provide starting points for adoption.

Together, they make TSMM more portable across standards work, open-source tooling, and trust-system implementation programs.

## Related artifacts

- [Entity model](tsmm-entities.md)
- [Relationship model](tsmm-relationships.md)
- [Lifecycle model](tsmm-lifecycle.md)
- [Effect evaluation model](../evaluation/effect-evaluation-model.md)
- [Getting Started: Implementer Guide](../getting-started-implementer-guide.md)
