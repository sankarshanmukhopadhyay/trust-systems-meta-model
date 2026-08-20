---
owner: maintainers
last_reviewed: 2026-08-20
applicable_version: 0.24.0
tier: 1
title: Semantic Projection
permalink: /model/semantic-projection.html
---
# Semantic Projection

A semantic projection maps a stable TSMM concept into an artifact or representation owned by another repository. Projection is not equivalence and does not transfer semantic authority.

The canonical TIS projection is `bindings/tis/tsmm-tis-semantic-projection.json`. Every mapping uses a stable `urn:tsmm:concept:*` identifier and declares whether target coverage is complete, partial, or informative.

A target repository may choose its own identifiers, serialization, constraints, and release policy. It must not silently redefine the TSMM concept it claims to implement.
