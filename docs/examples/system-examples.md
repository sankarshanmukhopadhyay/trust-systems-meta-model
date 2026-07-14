---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 1
---

# TSMM System Examples

This page gathers concrete system examples that exercise TSMM as a modeling surface rather than as description alone.

## Why the examples matter

A meta-model becomes easier to adopt once it can express real systems. These examples are intentionally compact, but they are concrete enough to show how registry, federation, directory, content authenticity, and community trust systems can be described using the same graph vocabulary.

They are also meant to be copied. In practice, most contributors should start from the nearest example, adjust the nodes and edges, and then validate the result rather than beginning from an empty file.

## Recommended starting point

If you want the smallest graph that still expresses the full TSMM path, start with:

- `model/graph/tsmm.graph.json`

That file is the canonical graph-first reference for the repo.

## Concrete system examples

### Registry and federation
- `examples/systems/trqp-registry-system.json`
- `examples/systems/openid-federation-system.json`
- `examples/systems/decentralized-directory-system.json`

### Workflow and community examples
- `examples/systems/content-authenticity-workflow.json`
- `examples/systems/verifiable-trust-community-system.json`

## What each example includes

Each example provides:

- a concrete TSMM graph instance
- a profile or ecosystem context
- a reference to a binding, registry, validation profile, or comparison artifact where relevant
- a path that can be validated with the repo validation scripts

## Example selection guide

Use the examples based on the kind of question you are trying to answer.

- **How does authority publish or register trust state?** Start with `trqp-registry-system.json`.
- **How does federation anchoring work?** Start with `openid-federation-system.json`.
- **How does governed discovery work in a decentralized setting?** Start with `decentralized-directory-system.json`.
- **How does provenance, evidence, and verifier reliance fit together?** Start with `content-authenticity-workflow.json`.
- **How does community membership and reliance fit together?** Start with `verifiable-trust-community-system.json`.

## Validation

The system examples are covered by:

```bash
python scripts/validate_examples.py
python scripts/validate_tsmm_graph.py
```

## Related paths

- [TSMM Graph Model](../model/tsmm-graph-model.md)
- [Bindings](../bindings/index.md)
- [Interoperability layer](../interop/interoperability.md)
- [Model, Bind, Validate, Compare](../getting-started/model-bind-validate-compare.md)
