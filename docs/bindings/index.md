---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 1
title: Bindings
permalink: /bindings/
parent: Documentation
has_children: true
---

# TSMM Ecosystem Bindings

Bindings package semantic alignments between TSMM and adjacent ecosystems into machine-readable JSON artifacts paired with brief human-readable explanation documents. Each binding now includes a contract section and a per-ecosystem constraint set so the mapping can be reviewed as a bounded translation surface rather than as free-floating prose. Binding status values follow the repo-wide [maturity model](../maturity-model.md).

## Available bindings

| Binding | Scope | Status | Notes |
| --- | --- | --- | --- |
| [TRQP binding](trqp-binding.md) | Trust registry query and publication surface | Supported | Stable comparison surface for registry and directory workflows |
| [OpenID Federation binding](openid-federation-binding.md) | Federation metadata and policy distribution surface | Supported | Stable federation comparison surface |
| [DCAS binding](dcas-binding.md) | Conformance and assurance evaluation surface | Supported | Suitable for assured-system comparison and evidence portability |
| [VTC binding](vtc-binding.md) | Verifiable trust community profile surface | Supported | Available for normal comparison use |
| [A2A binding](a2a-binding.md) | Agent interaction protocol surface | Candidate | Suitable for governed discovery, negotiation, and task-evidence comparison; not an A2A conformance claim |
| [OASF binding](oasf-binding.md) | Open assurance signal publication surface | Candidate | Suitable for bounded publication and evaluation comparison; runtime governance must be composed separately |
| [AIS-1 binding](ais1-binding.md) | Bonded agent identity and accountability substrate | Experimental | Included for comparative modelling, not as a mature or complete trust-stack profile |
| [HAVID binding](havid-binding.md) | Composite identifier assurance pattern | Experimental | Useful for comparison while upstream semantics continue to mature |
| [ODRL binding](odrl-binding.md) | Policy expression and rule-carrier surface | Experimental | Useful for bounded policy modeling without replacing the wider trust meta model |
| [GTR GRID/DIA binding](gtr-binding.md) | Global registrar discovery and Digital Identity Anchor verification surface | Experimental | Models GRID discovery, registrar authority, DIA verification, lifecycle, revocation, and relying-party effects |


## Executable artifact bindings

- [Trust Infrastructure Schemas binding](tis-binding.md) — maps TSMM semantics into executable authority, evidence, decision, and registry artifacts.
