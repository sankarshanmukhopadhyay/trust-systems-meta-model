---
owner: maintainers
last_reviewed: 2026-09-03
applicable_version: 0.24.0
tier: 2
title: Contributing
---

# Contributing

## Validation environment

Install the repository-pinned validation dependencies before running the conformance checks:

```bash
python -m pip install -r requirements-dev.txt
make validate
```

## Scope

TSMM is the canonical semantic layer of TSMS. Contributions should improve clarity, portability, machine-readability, or cross-ecosystem usefulness without acquiring authority that belongs to TIS, TGA, an external specification, or an implementation repository.

## Preferred contribution types

- refine abstractions without overfitting to one implementation;
- add well-scoped crosswalks to relevant trust-system repositories;
- improve glossary precision and terminology consistency;
- strengthen examples, schemas, negative vectors, and validation coverage; and
- improve documentation freshness, navigation, and GitHub Pages readability.

## Contribution rules

- keep the model minimal and operational;
- distinguish identity, authority, assurance, conformance, and effect;
- avoid introducing repo-specific jargon as universal truth;
- update examples, schemas, projections, and test vectors when abstractions change;
- update `last_reviewed` metadata on touched documents; and
- preserve compatibility or record a deliberate versioned break with migration guidance.

## Issue → PR → evidence → merge

Substantive semantic, authority, compatibility, or release changes should start from an issue that states the proposition, scope, acceptance criteria, and uncertainty. The PR should then record:

- the canonical concept or authority boundary being changed;
- alternatives genuinely considered where consequential;
- downstream projection/schema/implementation impact;
- positive and negative evidence that tests the claim;
- validation commands and machine-readable evidence produced; and
- residual uncertainty, falsification conditions, and any reassessment/revocation consequence.

Do not weaken a failing test merely to restore CI unless the test is demonstrably wrong and that judgment is recorded.

## Versioning

TSMM uses semantic versioning for releases of the reference model and documentation package. A version bump must correspond to an actual semantic or consumability change; synchronized downstream releases do not by themselves create TSMM release authority.
