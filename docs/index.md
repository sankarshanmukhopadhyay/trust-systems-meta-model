---
owner: maintainers
last_reviewed: 2026-04-27
applicable_version: v0.18.0
tier: 0
---

# Trust Systems Meta Model

Welcome to the documentation site for **Trust Systems Meta Model (TSMM)**.

TSMM is a portable reference model for designing, comparing, and implementing trust systems. It gives architects, standards authors, assurance teams, and protocol designers a common grammar for reasoning about roles, authority, policies, profiles, controls, evidence, assessment, verification, trust decisions, and operational effects. On the current main branch it also provides machine-readable authority, lifecycle, assurance, interoperability, and system-example artifacts so the model can be exercised directly.

## What you get here

- a canonical **primitive catalog** for the meta-model itself
- a compact **core model** for trust systems
- an **effect-centered evaluation model** for runtime legitimacy
- **conformance profiles** that help structure implementation maturity
- reusable **reference patterns** for recurring trust-system designs
- modular **extensions** for application domains such as Agentic AI, Agent Interaction (A2A-class ecosystems), Verifiable Trust Communities, and assurance-oriented architectures
- practical **crosswalks** to related repositories and implementations
- a machine-readable **graph model** for executable trust topology design
- an explicit **binding contract and validation layer** so ecosystem mappings can be tested rather than merely described

## Read this first

1. [Repository overview](../README.md)
2. [Model, Bind, Validate, Compare](getting-started/model-bind-validate-compare.md)
3. [TSMM Graph Model](model/tsmm-graph-model.md)
4. [Core model](core-model.md)
5. [Canonical meta-model schema](model/tsmm-meta-model-schema.md)
6. [Entity model](model/tsmm-entities.md)
7. [Relationship model](model/tsmm-relationships.md)
8. [Lifecycle model](model/tsmm-lifecycle.md)
9. [Effect evaluation model](evaluation/effect-evaluation-model.md)
10. [Threat model](security/trust-system-threat-model.md)


## Start by task

- **Model a system:** [Model, Bind, Validate, Compare](getting-started/model-bind-validate-compare.md), [TSMM Graph Model](model/tsmm-graph-model.md), [Authority graph](model/authority-graph.md), [System examples](examples/system-examples.md)
- **Bind a system:** [Bindings overview](bindings/index.md), [Binding contract model](bindings/binding-contract.md)
- **Validate a system:** [Validation and testability guide](conformance/validation-and-testability.md), `scripts/validate_examples.py`, `scripts/validate_tsmm_graph.py`, `scripts/validate_yaml_models.py`
- **Compare systems:** [Interoperability layer](interop/interoperability.md), [Crosswalks](crosswalks/trqp-tspp-crosswalk.md), [System examples](examples/system-examples.md)

## Conformance profiles

- [TSMM Minimal Profile](conformance/tsmm-profile-minimal.md)
- [TSMM Operational Profile](conformance/tsmm-profile-operational.md)
- [TSMM Assured Profile](conformance/tsmm-profile-assured.md)
- [TSMM Agentic Conformance Profile](conformance/tsmm-profile-agentic.md)

## Reference patterns

- [Trust Registry Pattern](patterns/trust-registry-pattern.md)
- [Delegated Agent Pattern](patterns/delegated-agent-pattern.md)
- [Credential Verification Pattern](patterns/credential-verification-pattern.md)
- [Assurance Evidence Pattern](patterns/assurance-evidence-pattern.md)
- [Multi-Agent Coordination Pattern](patterns/multi-agent-coordination-pattern.md)
- [Agent Governance Toolkit Crosswalk](crosswalks/agent-governance-toolkit-crosswalk.md) *(experimental)*

## Extensions

- [Extensions overview](extensions/index.md)
- [Agentic AI Extension](extensions/agentic-ai-extension.md)
- [Verifiable Trust Communities Extension](extensions/verifiable-trust-communities-extension.md)
- [Assurance Extension](extensions/assurance-extension.md)

## Agent Interaction Extension *(v0.13.0)*

- [Service Descriptor](model/service-descriptor.md)
- [Skill Contract](model/skill-contract.md)
- [Interaction Context](model/interaction-context.md)
- [Authorization Checkpoint](model/authorization-checkpoint.md)
- [Extension Contract](model/extension-contract.md)
- [Opacity Boundary](model/opacity-boundary.md)
- [Peer Trust Relation](model/peer-trust-relation.md)
- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- Example (A2A binding): `examples/agent-interaction-a2a-binding-instance.json`
- Interaction task: [InteractionTask](model/interaction-task.md)
- Content provenance policy: [ContentProvenancePolicy](model/content-provenance-policy.md)
- Observability mode: [ObservabilityMode](model/observability-mode.md)
- A2A crosswalk: [A2A Crosswalk](crosswalks/a2a-crosswalk.md)
- A2A binding: [A2A Binding](bindings/a2a-binding.md)

## Crosswalks

- [TRQP-TSPP Crosswalk](crosswalks/trqp-tspp-crosswalk.md)
- [ERC-8004-CSP Crosswalk](crosswalks/erc-8004-csp-crosswalk.md)
- [DCAS Crosswalk](crosswalks/dcas-crosswalk.md)
- [TRAA Crosswalk](crosswalks/trust-reference-assurance-architecture-crosswalk.md)
- [OpenID Federation Crosswalk](crosswalks/openid-federation-crosswalk.md)
- [Agent Taxonomy and SSA Crosswalk](crosswalks/agent-taxonomy-ssa-crosswalk.md)

## Ecosystem bindings

- [Binding contract model](bindings/binding-contract.md)

- [Bindings overview](bindings/index.md)
- [TRQP binding](bindings/trqp-binding.md)
- [OpenID Federation binding](bindings/openid-federation-binding.md)
- [DCAS binding](bindings/dcas-binding.md)
- [Verifiable Trust Communities binding](bindings/vtc-binding.md)
- [AIS-1 binding](bindings/ais1-binding.md) *(experimental)*
- [HAVID binding](bindings/havid-binding.md)
- `bindings/trqp/tsmm-trqp-binding.json`
- `bindings/openid-federation/tsmm-openid-federation-binding.json`
- `bindings/dcas/tsmm-dcas-binding.json`
- `bindings/vtc/tsmm-vtc-binding.json`
- `bindings/havid/tsmm-havid-binding.json`

## Executable graph layer

- [TSMM Graph Model](model/tsmm-graph-model.md)
- [Model, Bind, Validate, Compare](getting-started/model-bind-validate-compare.md)
- `schemas/tsmm-graph.schema.json`
- `model/graph/tsmm.graph.json`
- `examples/tsmm-ecosystem-example.json`
- `examples/profiles/ssi-ecosystem.json`
- `examples/profiles/agent-trust-network.json`
- `examples/profiles/agent-governance-network.json`
- `examples/profiles/trust-registry-federation.json`
- `examples/profiles/dpi-trust-layer.json`


## Authority, delegation, lifecycle, and interoperability

- [Authority graph](model/authority-graph.md)
- [Delegation patterns](model/delegation-patterns.md)
- [Lifecycle model](model/tsmm-lifecycle.md)
- [Interoperability layer](interop/interoperability.md)
- `model/authority-graph.yaml`
- `model/delegation-patterns.yaml`
- `model/lifecycle/trust-object-lifecycle.yaml`
- `extensions/assurance/assurance-properties.yaml`
- `interop/interoperability-matrix.yaml`

## System examples

- [System examples overview](examples/system-examples.md)
- `examples/systems/trqp-registry-system.json`
- `examples/systems/openid-federation-system.json`
- `examples/systems/decentralized-directory-system.json`
- `examples/systems/content-authenticity-workflow.json`
- `examples/systems/verifiable-trust-community-system.json`
- `examples/systems/ais1-bonded-agent-system.json`

## Registry publication

- [TSMM Registry Format](registry/tsmm-registry-format.md)
- `schemas/tsmm-registry.schema.json`
- `examples/registries/tsmm-registry-example.json`

## Validation and testability

- [Validation and testability guide](conformance/validation-and-testability.md)
- `validation/conformance/tsmm-validation-profile.json`
- `validation/test_vectors/valid/tsmm-binding-valid.json`
- `validation/test_vectors/invalid/tsmm-binding-invalid-missing-guarantees.json`
- `validation/test_vectors/valid/tsmm-binding-constraints-valid.json`
- `validation/test_vectors/invalid/tsmm-binding-constraints-invalid-empty-prohibited-inferences.json`

## Operational docs

- [Documentation governance](documentation-governance.md)
- [Freshness audit](freshness-audit.md)
- [Glossary](glossary.md)
- [Getting Started: Implementer Guide](getting-started-implementer-guide.md)
- [Roadmap](roadmap.md)

## Model thesis

TSMM is effect-centered. The core governance question is not merely whether an identity exists. The question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a specific effect.

## Current documentation snapshot

This documentation set remains aligned to **v0.18.0** and is intended to remain usable both on GitHub and through GitHub Pages. The current main branch now places the graph layer at the center of the repo, expands concrete system coverage, and tightens the contributor path around model, bind, validate, and compare.

- ODRL binding *(experimental)*: `bindings/odrl-binding.md`

## Runtime assurance layer *(v0.18.0)*

- [Runtime Governance Envelope](model/runtime-governance-envelope.md)
- [Decision Receipt](model/decision-receipt.md)
- [Runtime Governance Test Profile](conformance/runtime-governance-test-profile.md)
- [Implementation Paths](getting-started/implementation-paths.md)
- [Runtime Governance Walkthrough](examples/runtime-governance-walkthrough.md)
- Schema: `schemas/tsmm-runtime-governance.schema.json`
- Schema: `schemas/tsmm-decision-receipt.schema.json`
- Example: `examples/runtime-governance-boundary-instance.json`
- Example: `examples/decision-receipt-runtime-example.json`
- System example: `examples/systems/revocation-propagation-system.json`
