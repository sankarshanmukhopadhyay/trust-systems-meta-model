---
title: Trust Graph Artifacts alignment
applicable_version: 0.24.0
---

# Trust Graph Artifacts alignment

Trust Graph Artifacts (TGA) is a downstream interpretation and assurance corpus that applies TSMM canonical semantics to governance patterns derived from The Trust Graph.

## Authority direction

The relationship is intentionally asymmetric:

```text
Trust Graph essays -> design pressure
TSMM             -> canonical trust-system semantics
TGA              -> interpretation, implementation, and assurance artifacts
TIS              -> portable executable contracts when required
```

TSMM does **not** depend on TGA for semantic authority. TGA may profile, implement, or illustrate TSMM concepts, but it cannot redefine their canonical meaning.

## Current reviewed baseline

- TSMM: **v0.24.0**
- TGA: **v0.12.1**
- TIS used by TGA for portable contracts: **v0.14.1**

The machine-readable downstream projection is:

```text
bindings/tga/tsmm-tga-semantic-projection.json
```

The projection maps TGA authority, delegation, scope, policy, evidence, assessment, trust-decision, effect, assurance, revocation, supersession, and redress surfaces to stable `urn:tsmm:concept:*` identifiers.

## What TSMM guarantees

TSMM guarantees the stability and authority semantics of the referenced concept identifiers within the release contract. It does not guarantee that a downstream TGA artifact is complete, conformant, or correctly implemented.

## What TGA must prove

TGA is responsible for proving that:

1. its active TSMM binding cites the current reviewed TSMM release;
2. its mappings use stable TSMM identifiers where available;
3. its local implementation vocabulary does not silently supersede TSMM semantics;
4. its TIS projection preserves TSMM as semantic authority;
5. its own repository validation detects binding, version, and documentation drift.

## Validation

TSMM validates the semantic projection contract as part of:

```bash
make validate
```

TGA independently validates its local binding through:

```bash
python3 scripts/validate_tsmm_alignment.py
make validate
```

These are complementary evidence surfaces. Neither repository's validation constitutes external certification.
