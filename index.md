---
layout: default
title: Trust Systems Meta Model
---

# Trust Systems Meta Model

Welcome to the GitHub Pages site for **Trust Systems Meta Model (TSMM)**.

TSMM is a portable reference model for designing, comparing, and implementing trust systems. It gives architects, standards authors, and assurance teams a common grammar for reasoning about roles, authority, policy, evidence, trust decisions, and operational effects. The current main branch also includes machine-readable authority, lifecycle, assurance, interoperability, and example-system artifacts so the model can be used more directly.

## Start here

- [Documentation home](docs/index.md)
- [Model, Bind, Validate, Compare](docs/getting-started/model-bind-validate-compare.md)
- [TSMM Graph Model](docs/model/tsmm-graph-model.md)
- [Core model](docs/core-model.md)
- [Canonical meta-model schema](docs/model/tsmm-meta-model-schema.md)
- [Authority graph](docs/model/authority-graph.md)
- [Delegation patterns](docs/model/delegation-patterns.md)
- [Lifecycle model](docs/model/tsmm-lifecycle.md)
- [Interoperability layer](docs/interop/interoperability.md)
- [System examples](docs/examples/system-examples.md)
- [Validation and testability](docs/conformance/validation-and-testability.md)
- [Latest tagged release notes](releases/v0.14.0.md)

## At a glance

- **Canonical primitive catalog:** machine-readable Actor, Authority, Credential, Policy, TrustRelationship, Delegation, and VerificationProcess definitions
- **Core abstractions:** entities, roles, authority, artifacts, claims, policy, controls, evidence, assessment, verification, trust decisions, and effects
- **Profiles and patterns:** reusable guidance for shaping implementations without collapsing into one domain-specific standard
- **Extensions:** modular specialization for Agentic AI, Verifiable Trust Communities, and assurance architectures
- **Operational hygiene:** documentation governance, freshness audit, graph validation, registry validation, schema/example validation, representative valid/invalid test-vector checks, and metadata reference checks across graph examples
- **Bindings and publication:** ecosystem bindings, registry publication format, agentic instance indexing, graph rendering utility, and a clear handoff to the canonical trust artifact schema layer

## Explore by path

- [Conformance profiles](docs/conformance/tsmm-profile-minimal.md)
- [Reference patterns](docs/patterns/trust-registry-pattern.md)
- [Extensions](docs/extensions/index.md)
- [Crosswalks](docs/crosswalks/trqp-tspp-crosswalk.md)
- [Bindings](docs/bindings/index.md)
- [AIS-1 binding](docs/bindings/ais1-binding.md)
- [HAVID binding](docs/bindings/havid-binding.md)
- [Validation and testability](docs/conformance/validation-and-testability.md)
- [Registry format](docs/registry/tsmm-registry-format.md)
- [Assurance extension](docs/extensions/assurance-extension.md)
- [Glossary](docs/glossary.md)

## Why this matters

TSMM is designed as a bridge. It extracts recurring trust-system invariants from real implementation work so that other projects can apply the theory without waiting for one specific protocol, repository, or assurance package to do the translation for them. On the current main branch, the clearest way to use the repo is to start from the graph layer, adapt one of the concrete system examples, bind it to an ecosystem surface, and then validate the result.
