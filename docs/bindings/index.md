---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 0
---

# TSMM Ecosystem Bindings

TSMM bindings map external ecosystem concepts into TSMM abstractions. This is the practical move that keeps the model from becoming a beautiful conceptual terrarium: glass walls, lovely structure, zero operational gravity.

Bindings let implementers ask a much harder and more useful question than “what does TSMM mean?”

They ask:

- how does a real ecosystem map into TSMM terms
- where is the mapping exact versus approximate
- which ecosystem concepts bundle several TSMM abstractions together
- how can one topology be compared with another without flattening their differences

## Binding catalog

- [TRQP binding](trqp-binding.md)
- [OpenID Federation binding](openid-federation-binding.md)

## Machine-readable artifacts

- `bindings/trqp/tsmm-trqp-binding.json`
- `bindings/openid-federation/tsmm-openid-federation-binding.json`
- `schemas/tsmm-binding.schema.json`

## Design intent

Bindings are semantic translation layers. They do not replace upstream specifications, and they do not claim that every concept lands in TSMM with perfect symmetry. In some ecosystems, one external object combines registry, governance, and evidence semantics in a single artifact. TSMM pulls those apart so the governance logic can be seen clearly.
