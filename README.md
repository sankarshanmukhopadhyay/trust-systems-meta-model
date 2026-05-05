---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

[![Release](https://img.shields.io/badge/release-v0.19.0-blue)](releases/v0.19.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.19.0  
**Status:** Draft reference model with machine-readable modeling, validation, comparison, and runtime-governance artifacts  
**License:** CC BY-SA 4.0

## What TSMM is

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, implementing, and assuring trust systems. It gives architects, standards authors, governance engineers, assurance teams, and protocol designers a common grammar for modeling entities, authority, delegation, policy, evidence, lifecycle state, verification, trust decisions, operational effects, and runtime governance.

TSMM is intentionally **effect-centered**. The core question is not only whether an identity exists or a credential verifies. The core question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a defined effect.

## What v0.19.0 adds

TSMM v0.19.0 delivers **Agent Discovery, Capability Negotiation, and Task Evidence Readiness**. It generalizes reusable A2A-class patterns into TSMM without copying protocol mechanics into the core model.

New release surfaces:

- **Discovery Governance Model** for public descriptors, authenticated extended descriptors, curated registries, direct configuration, restricted catalogs, freshness policy, integrity requirements, and failure behavior.
- **Capability Negotiation Model** for advertised, discoverable, negotiated, authorized, executed, and evidenced capabilities.
- **Task Evidence Lifecycle Model** for treating task state transitions as governance-relevant evidence events.
- **A2A binding refresh** covering discovery modes, descriptor integrity, extension requiredness, task lifecycle evidence, streaming/async observability, and opacity boundaries.
- **Documentation refresh** across README, docs index, roadmap, freshness audit, documentation governance, conformance guidance, and GitHub Pages entry points.
- **Validation hardening** with schemas, examples, and valid/invalid test vectors for the new governance surfaces.

## Use TSMM in five workflows

| Workflow | Start here | Evidence produced |
| --- | --- | --- |
| Model a trust system | `docs/getting-started/model-bind-validate-compare.md` | Graph model, authority graph, lifecycle model |
| Bind a protocol or ecosystem | `docs/bindings/index.md` | Binding JSON, crosswalk, interoperability notes |
| Validate artifacts | `scripts/validate_examples.py` and `scripts/validate_test_vectors.py` | Pass/fail validation evidence |
| Govern agent interaction | `docs/examples/a2a-governed-discovery-walkthrough.md` | Discovery, negotiation, task lifecycle records |
| Publish assurance-ready docs | `docs/documentation-governance.md` | Freshness metadata, release notes, link checks |

## Agentic systems and runtime governance

TSMM now provides a practical path for agentic systems where agents are discovered, evaluated, authorized, invoked, observed, and audited across organizational boundaries.

Key artifacts:

- Discovery governance: `docs/model/discovery-governance.md`
- Capability negotiation: `docs/model/capability-negotiation.md`
- Task evidence lifecycle: `docs/model/task-evidence-lifecycle.md`
- Governed A2A-class walkthrough: `docs/examples/a2a-governed-discovery-walkthrough.md`
- A2A binding: `docs/bindings/a2a-binding.md`
- A2A crosswalk: `docs/crosswalks/a2a-crosswalk.md`

## Repository map

| Path | Purpose |
| --- | --- |
| `schemas/` | JSON Schemas for TSMM core, extensions, bindings, governance surfaces, and validation artifacts |
| `examples/` | Valid example instances and ecosystem/system examples |
| `validation/test_vectors/` | Valid and invalid conformance vectors |
| `docs/model/` | Conceptual model surfaces |
| `docs/patterns/` | Reusable implementation and assurance patterns |
| `docs/bindings/` | Ecosystem/protocol binding documentation |
| `docs/crosswalks/` | Semantic comparison documents |
| `bindings/` | Machine-readable binding declarations |
| `interop/` | Machine-readable interoperability comparison matrix |
| `scripts/` | Validation, coverage, graph, registry, and docs checks |
| `releases/` | Release notes and migration guidance |

## Validation

Run the full validation set from the repository root:

```bash
python scripts/validate_examples.py
python scripts/validate_bindings.py
python scripts/validate_test_vectors.py
python scripts/validate_yaml_models.py
python scripts/validate_tsmm_graph.py
python scripts/validate_tsmm_registry.py
python scripts/check_docs.py
python scripts/check_schema_coverage.py
```

## Documentation

- GitHub Pages landing page: `index.md`
- Documentation home: `docs/index.md`
- Roadmap: `docs/roadmap.md`
- Freshness audit: `docs/freshness-audit.md`
- Documentation governance: `docs/documentation-governance.md`
- Release notes: `releases/v0.19.0.md`

## Current release posture

TSMM v0.19.0 is additive. It does not introduce breaking changes to the stable core model. New schemas and examples are introduced as candidate governance surfaces that can be adopted independently by implementers and promoted based on conformance evidence.

## Contributing

Contributions should preserve TSMM's core discipline: keep concepts abstract enough to travel across ecosystems, but concrete enough to validate. New model surfaces should include documentation, schema, example, test vectors, and validation coverage.
