---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 0
---

# Trust Systems Meta Model (TSMM)

> **Flagship repository**  
> **Role:** `canonical-semantic-model`  
> **Current version:** `v0.22.0`  
> **Canonical validation:** `make validate`  
> **Authority:** [`governance/repository-authority.yaml`](governance/repository-authority.yaml)  
> **Start here:** [`docs/adoption.md`](docs/adoption.md)


[![Release](https://img.shields.io/badge/release-v0.22.0-blue)](releases/v0.22.0.md)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/license-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-brightgreen)](index.md)
[![Validate Schemas and Examples](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/validate.yml)
[![Deploy GitHub Pages](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model/actions/workflows/pages.yml)

**Version:** v0.22.0  
**Status:** Draft reference model with machine-readable modeling, validation, comparison, runtime-governance, and executable binding assurance artifacts  
**License:** CC BY-SA 4.0

## What TSMM is

Trust Systems Meta Model (TSMM) is a portable abstract reference model for designing, comparing, implementing, and assuring trust systems. It gives architects, standards authors, governance engineers, assurance teams, and protocol designers a common grammar for modeling entities, authority, delegation, policy, evidence, lifecycle state, verification, trust decisions, operational effects, and runtime governance.

TSMM is intentionally **effect-centered**. The core question is not only whether an identity exists or a credential verifies. The core question is whether a bounded authority, evaluated under policy and evidence, should be allowed to produce a defined effect.

## What v0.22.0 consolidates

TSMM v0.22.0 consolidates **Executable Binding Assurance and Catalog Completeness**. It makes the published binding catalog enforceable: every binding now carries an explicit governance contract, declared maturity, constraint set, and catalog validation path. It also validates all published graph artifacts and provides a reproducible local validation environment.

New release surfaces:

- **Complete binding contracts** for A2A and OASF, including bounded guarantees, limitations, behavioral expectations, and prohibited inferences.
- **Binding schema expansion** for TSMM extension-layer types and governance mapping semantics.
- **Catalog-wide validation** that discovers every published binding and graph artifact rather than relying on incomplete hand-maintained lists.
- **Negative conformance vectors** for binding contract completeness and mapping vocabulary.
- **Reproducible validation** through a repository-owned dependency manifest used by CI and local implementers.


## TSMM and Trust Infrastructure Schemas

TSMM now includes a dedicated binding to `trust-infrastructure-schemas` (TIS). The intended architecture is:

```text
TSMM = semantic model and cross-ecosystem grammar
TIS  = canonical executable artifact contracts
```

Use TSMM to model trust-system meaning, authority topology, delegation structure, evidence semantics, and runtime effects. Use TIS to package those claims as machine-validatable authority boundaries, evidence bundle manifests, evaluation envelopes, decision receipts, and registry entries.

Key artifacts:

- TIS binding: `docs/bindings/tis-binding.md`
- Cross-repo alignment: `docs/cross-repo/trust-infrastructure-schemas-alignment.md`
- Crosswalk index: `docs/crosswalks/trust-infrastructure-schemas-crosswalk.md`
- Decision receipt crosswalk: `docs/crosswalks/tis-decision-receipt-crosswalk.md`
- Assurance level crosswalk: `docs/crosswalks/tis-assurance-level-crosswalk.md`
- Executable artifact walkthrough: `docs/examples/tis-executable-artifact-walkthrough.md`
- Machine-readable binding: `bindings/tis/tsmm-tis-binding.json`

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


## GTR / GRID / DIA modeling

This archive includes an experimental TSMM binding for the Global Trust Registry, Global Registrar Information Directory, and Digital Identity Anchor architecture. The binding treats GTR as a discovery, verification, lifecycle, and reliance system rather than as a static directory.

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
python -m pip install -r requirements-dev.txt
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
- Release notes: `releases/v0.21.0.md`

## Current release posture

TSMM v0.21.0 is additive. It does not introduce breaking changes to the stable core model. It strengthens the enforceability of published bindings and examples, so implementers can rely on a clearer assurance boundary when they compare or adopt TSMM-aligned systems.

## Contributing

Contributions should preserve TSMM's core discipline: keep concepts abstract enough to travel across ecosystems, but concrete enough to validate. New model surfaces should include documentation, schema, example, test vectors, and validation coverage.

## Delegation lineage in v0.22.0

TSMM now models chained and fan-out delegation, including monotonic scope attenuation, originating-principal continuity, trust-domain transitions, convergence checks, and revocation propagation. See the [implementer guide](docs/getting-started-implementer-guide.md#implement-chained-delegation) and [v0.22.0 release notes](releases/v0.22.0.md).
