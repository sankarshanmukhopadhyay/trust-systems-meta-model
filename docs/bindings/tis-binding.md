---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# Trust Infrastructure Schemas Binding

The TIS binding connects TSMM semantic concepts to executable Trust Infrastructure Schemas artifacts. It is a candidate binding introduced in v0.20.0.

## Binding purpose

The binding allows an implementer to model a trust system in TSMM and then publish concrete artifacts using TIS schemas. The intended pipeline is:

```text
TSMM model -> authority graph -> TIS authority boundary -> TIS evidence bundle -> TIS evaluation envelope -> TIS decision receipt -> TIS registry entry
```

## Machine-readable artifacts

- Binding: `bindings/tis/tsmm-tis-binding.json`
- Constraints: `bindings/tis/constraints.json`

## Governance boundaries

The binding does not certify conformance. It provides a structured interoperability pattern. Implementers still need validation evidence from both repositories and, where relevant, independent assurance.
