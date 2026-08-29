---
owner: maintainers
last_reviewed: 2026-08-22
applicable_version: 0.24.0
tier: 0
title: Trust Systems Meta Model (TSMM)
nav_exclude: true
---

# Trust Systems Meta Model (TSMM)

> **Flagship repository**  
> **Role:** `canonical-semantic-model`  
> **Current version:** `v0.24.0`  
> **Canonical validation:** `make validate`  
> **Authority:** [`governance/repository-authority.yaml`](governance/repository-authority.yaml)  
> **Start here:** [`docs/adoption.md`](docs/adoption.md)

[![Release](https://img.shields.io/badge/release-v0.24.0-blue)](releases/v0.24.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.24.0  
**Status:** Candidate specification with machine-readable modeling, semantic projection, validation, comparison, runtime-governance, and executable binding assurance artifacts  
**License:** CC BY-SA 4.0

## What TSMM is

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, implementing, and assuring trust systems. It gives architects, standards authors, governance engineers, assurance teams, and protocol designers a common grammar for modeling entities, authority, delegation, policy, evidence, lifecycle state, verification, trust decisions, operational effects, and runtime governance.

TSMM is intentionally **effect-centered**. The core question is not only whether an identity exists or a credential verifies. The core question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a defined effect.

## What v0.24.0 adds

TSMM v0.24.0 adds **Executable Cross-Repository Semantic Governance**. Stable semantic identifiers, versioned projection contracts, compatibility declarations, and drift validation make authority boundaries independently inspectable and testable.

New release surfaces include:

- **Stable semantic identifiers** for canonical TSMM concepts using `urn:tsmm:concept:*`.
- **Machine-readable semantic projections** with explicit coverage and authority boundaries.
- **Portfolio relationship contracts** that can be compared with canonical portfolio topology without duplicating its authority.
- **Semantic drift and version consistency checks** integrated into repository validation.
- **Auditable validation evidence** that records cross-repository alignment checks.

## Authority model

TSMM owns **canonical trust-system semantics**. It does not own portable schema serialization, external protocol specifications, implementation releases, portfolio classification, or certification.

Downstream repositories may profile, implement, serialize, or illustrate TSMM concepts, but they do not acquire authority to redefine those concepts. The machine-readable semantic registry is:

```text
model/semantic-concepts.json
```


## Trust Systems Modelling Stack (TSMS)

TSMM is the semantic foundation of the **Trust Systems Modelling Stack (TSMS)**:

```text
TSMM semantics
    ↓
TIS portable contracts
    ↓
TGA executable governance artifacts
    ↓
validation / evidence / assurance consumers
```

TSMS is a coordination architecture, not a transfer of authority. TSMM remains authoritative only for canonical trust-system semantics; TIS remains authoritative for portable machine-readable contracts; TGA remains authoritative for its executable compositions and project-local assurance patterns.

The initial candidate baseline is **TSMM v0.24.0 / TIS v0.14.1 / TGA v0.12.1**. It is deliberately marked candidate until cross-repository conformance checks establish compatibility.

- [TSMS architecture and adoption guide](docs/tsms.md)
- Machine-readable stack manifest: `model/tsms-stack.json`
- Coordinating programme: [TSMM #5](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/issues/5)

## TSMM and Trust Infrastructure Schemas

TSMM includes a dedicated binding to `trust-infrastructure-schemas` (TIS):

```text
TSMM = semantic model and cross-ecosystem grammar
TIS  = canonical executable artifact contracts
```

Use TSMM to model trust-system meaning, authority topology, delegation structure, evidence semantics, and runtime effects. Use TIS to package those claims as machine-validatable authority boundaries, evidence bundle manifests, evaluation envelopes, decision receipts, registry entries, and assurance objects.

Key artifacts:

- TIS binding: `docs/bindings/tis-binding.md`
- Cross-repo alignment: `docs/cross-repo/trust-infrastructure-schemas-alignment.md`
- Crosswalk index: `docs/crosswalks/trust-infrastructure-schemas-crosswalk.md`
- Decision receipt crosswalk: `docs/crosswalks/tis-decision-receipt-crosswalk.md`
- Assurance level crosswalk: `docs/crosswalks/tis-assurance-level-crosswalk.md`
- Executable artifact walkthrough: `docs/examples/tis-executable-artifact-walkthrough.md`
- Machine-readable semantic projection: `bindings/tis/tsmm-tis-semantic-projection.json`

## TSMM and Trust Graph Artifacts

Trust Graph Artifacts (TGA) is a downstream interpretation and assurance corpus. It applies TSMM semantics to essay-derived governance patterns while preserving the authority boundary between source motivation, canonical semantics, implementation artifacts, and portable contracts.

The reviewed baseline is **TSMM v0.24.0 ↔ TGA v0.12.1**. TSMM does not depend on TGA for semantic authority.

Key artifacts:

- Alignment guide: `docs/cross-repo/trust-graph-artifacts-alignment.md`
- Machine-readable semantic projection: `bindings/tga/tsmm-tga-semantic-projection.json`
- Canonical semantic registry: `model/semantic-concepts.json`

## Use TSMM in five workflows

| Workflow | Start here | Evidence produced |
| --- | --- | --- |
| Model a trust system | `docs/getting-started/model-bind-validate-compare.md` | Graph model, authority graph, lifecycle model |
| Bind a protocol or ecosystem | `docs/bindings/index.md` | Binding JSON, crosswalk, interoperability notes |
| Validate artifacts | `scripts/validate_examples.py` and `scripts/validate_test_vectors.py` | Pass/fail validation evidence |
| Govern agent interaction | `docs/examples/a2a-governed-discovery-walkthrough.md` | Discovery, negotiation, task lifecycle records |
| Publish assurance-ready docs | `docs/documentation-governance.md` | Freshness metadata, release notes, link checks |

## Agentic systems and runtime governance

TSMM provides a practical path for agentic systems where agents are discovered, evaluated, authorized, invoked, observed, and audited across organizational boundaries.

Key artifacts:

- Discovery governance: `docs/model/discovery-governance.md`
- Capability negotiation: `docs/model/capability-negotiation.md`
- Task evidence lifecycle: `docs/model/task-evidence-lifecycle.md`
- Governed A2A-class walkthrough: `docs/examples/a2a-governed-discovery-walkthrough.md`
- A2A binding: `docs/bindings/a2a-binding.md`
- A2A crosswalk: `docs/crosswalks/a2a-crosswalk.md`

## GTR / GRID / DIA modeling

This repository includes an experimental TSMM binding for the Global Trust Registry, Global Registrar Information Directory, and Digital Identity Anchor architecture. The binding treats GTR as a discovery, verification, lifecycle, and reliance system rather than as a static directory.

Key artifacts:

- GTR binding: `docs/bindings/gtr-binding.md`
- GTR crosswalk: `docs/crosswalks/gtr-grid-dia-crosswalk.md`
- Machine-readable binding: `bindings/gtr/tsmm-gtr-binding.json`
- Authority graph: `examples/gtr/gtr-authority-graph-example.json`
- DIA decision receipt: `examples/gtr/gtr-dia-verification-decision-receipt.json`
- Registrar lifecycle model: `examples/gtr/gtr-registrar-lifecycle-event.json`
- System graph: `examples/systems/gtr-grid-dia-system.json`

The binding is suitable for architectural analysis, assurance design, documentation alignment, and future conformance-profile development. It does not claim GTR certification or production conformance.

## Repository map

| Path | Purpose |
| --- | --- |
| `model/` | Canonical semantic registry and core model surfaces |
| `schemas/` | JSON Schemas for TSMM core, extensions, bindings, governance surfaces, and validation artifacts |
| `examples/` | Valid example instances and ecosystem/system examples |
| `validation/test_vectors/` | Valid and invalid conformance vectors |
| `docs/model/` | Conceptual model surfaces |
| `docs/patterns/` | Reusable implementation and assurance patterns |
| `docs/bindings/` | Ecosystem/protocol binding documentation |
| `docs/crosswalks/` | Semantic comparison documents |
| `docs/cross-repo/` | Cross-repository authority and alignment guidance |
| `bindings/` | Machine-readable binding and semantic projection declarations |
| `interop/` | Machine-readable interoperability comparison matrix |
| `scripts/` | Validation, coverage, graph, registry, and documentation checks |
| `releases/` | Release notes and migration guidance |

## Validation

Run the canonical repository gate:

```bash
make validate
```

The gate covers schemas, examples, bindings, test vectors, YAML models, TSMM graph and registry integrity, semantic projection contracts, documentation integrity, coverage, version consistency, repository governance, and portfolio relationships. Validation produces machine-readable evidence under `artifacts/`.

## Documentation

- GitHub Pages landing page: `index.md`
- Documentation home: `docs/index.md`
- Roadmap: `docs/roadmap.md`
- Freshness audit: `docs/freshness-audit.md`
- Documentation governance: `docs/documentation-governance.md`
- Release notes: `releases/v0.24.0.md`

## Current release posture

TSMM v0.24.0 is additive. It does not introduce breaking changes to the stable core model. It strengthens the enforceability of published semantic projections, bindings, and examples so implementers can rely on clearer authority boundaries when comparing or adopting TSMM-aligned systems.

## Contributing

Contributions should preserve TSMM's core discipline: keep concepts abstract enough to travel across ecosystems, but concrete enough to validate. New model surfaces should include documentation, schema, example, test vectors, and validation coverage where applicable.

For delegation lineage, including chained and fan-out delegation, scope attenuation, originating-principal continuity, trust-domain transitions, convergence checks, and revocation propagation, see the [implementer guide](docs/getting-started-implementer-guide.md#implement-chained-delegation) and [v0.24.0 release notes](releases/v0.24.0.md).
