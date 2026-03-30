---
owner: maintainers
last_reviewed: 2026-03-25
applicable_version: v0.14.0
tier: 1
---

# TSMM Ecosystem Bindings

Bindings package semantic alignments between TSMM and adjacent ecosystems into machine-readable JSON artifacts paired with brief human-readable explanation documents. Each binding now includes a contract section and a per-ecosystem constraint set so the mapping can be reviewed as a bounded translation surface rather than as free-floating prose.

## Available bindings

- [TRQP binding](trqp-binding.md)
- [OpenID Federation binding](openid-federation-binding.md)
- [DCAS binding](dcas-binding.md)
- [Verifiable Trust Communities binding](vtc-binding.md)
- [A2A Protocol binding](a2a-binding.md) *(v0.14.0)*
- [OASF binding](oasf-binding.md) *(integration increment)*
- [AIS-1 binding](ais1-binding.md) *(bonded identity substrate profile)*

## Contract model

- [Binding contract model](binding-contract.md)

## Machine-readable artifacts

- `bindings/trqp/tsmm-trqp-binding.json`
- `bindings/openid-federation/tsmm-openid-federation-binding.json`
- `bindings/dcas/tsmm-dcas-binding.json`
- `bindings/vtc/tsmm-vtc-binding.json`
- `bindings/trqp/constraints.json`
- `bindings/openid-federation/constraints.json`
- `bindings/dcas/constraints.json`
- `bindings/vtc/constraints.json`
- `bindings/a2a/tsmm-a2a-binding.json`
- `bindings/oasf/tsmm-oasf-binding.json`
- `bindings/ais1/tsmm-ais1-binding.json`
- `bindings/ais1/constraints.json`

## Publication note

As of v0.11.0, bindings are intended to be indexable through the TSMM registry format so graphs, profiles, bindings, and extension instances can travel together as publishable infrastructure.
