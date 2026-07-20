---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# Model, Bind, Validate, Compare, Publish

This page is the shortest path through the repository if you want to use TSMM as infrastructure rather than read it as theory.

## 1. Model

Start with a graph.

- canonical graph: `model/graph/tsmm.graph.json`
- graph schema: `schemas/tsmm-graph.schema.json`
- graph model: [TSMM Graph Model](../model/tsmm-graph-model.md)
- authority and delegation: [Authority graph](../model/authority-graph.md), [Delegation patterns](../model/delegation-patterns.md)
- lifecycle: [Lifecycle model](../model/tsmm-lifecycle.md)

If you are designing a new system, the graph gives you the quickest way to represent actors, authorities, policies, evidence, decisions, and effects in one place.

## 2. Bind

Once the system is modeled, connect it to a real ecosystem surface.

- bindings overview: [Bindings](../bindings/index.md)
- contract model: [Binding contract](../bindings/binding-contract.md)
- machine-readable bindings:
  - `bindings/trqp/tsmm-trqp-binding.json`
  - `bindings/openid-federation/tsmm-openid-federation-binding.json`
  - `bindings/dcas/tsmm-dcas-binding.json`
  - `bindings/vtc/tsmm-vtc-binding.json`
  - `bindings/havid/tsmm-havid-binding.json`
  - `bindings/oasf/tsmm-oasf-binding.json`

Use the binding layer when you want to state what TSMM can preserve, what gets lost, and what behavior a translation is expected to uphold.

## 3. Validate

The repo now supports validation at four practical layers.

- schema and example validation: `python scripts/validate_examples.py`
- graph validation: `python scripts/validate_tsmm_graph.py`
- binding validation: `python scripts/validate_bindings.py`
- YAML model validation: `python scripts/validate_yaml_models.py`
- test vectors: `python scripts/validate_test_vectors.py`
- schema coverage: `python scripts/check_schema_coverage.py`
- documentation and link checks: `python scripts/check_docs.py`

The validation surface is deliberately lightweight. The aim is to make representative artifacts testable without requiring a large external harness.

## 4. Compare

Comparison becomes easier once systems share a graph vocabulary and binding contract.

- interoperability layer: [Interoperability](../interop/interoperability.md)
- interoperability matrix: `interop/interoperability-matrix.yaml`
- crosswalks: [Crosswalks](../crosswalks/trqp-tspp-crosswalk.md)
- concrete system examples: [System examples](../examples/system-examples.md)

Use this layer when you need to explain whether two systems align structurally, semantically, or behaviorally.

## 5. Publish

Once the model and binding are stable, publish the system in a way that preserves operator accountability, control references, evidence pointers, and evaluation traceability.

- publication guidance: [OASF publication guidance](../profiles/oasf-publication-guidance.md)
- publication binding: [TSMM to OASF Binding](../bindings/oasf-binding.md)
- publication crosswalk: [TSMM ↔ OASF Crosswalk](../crosswalks/oasf-crosswalk.md)
- worked example: `examples/profiles/oasf-publication-profile.json`

Use this layer when you need TSMM-described systems to become assurance-addressable without flattening trust semantics into a transport-specific schema.

## A practical sequence

1. Start from `model/graph/tsmm.graph.json`.
2. Copy the nearest example system from `examples/systems/`.
3. Adjust nodes, edges, policy, and evidence paths for your ecosystem.
4. Add the most relevant binding from `bindings/`.
5. Run the validators.
6. Use the interoperability matrix and crosswalks to compare your model with adjacent systems.
7. Publish the resulting profile through the OASF-oriented publication guidance if the system needs downstream discovery, assessment, or assurance reuse.
