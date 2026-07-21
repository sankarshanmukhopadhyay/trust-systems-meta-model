---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
title: TIS Authority Boundary Crosswalk
permalink: /crosswalks/tis-authority-boundary-crosswalk.html
parent: Crosswalks
grand_parent: Documentation
---

# TIS Authority Boundary Crosswalk

TSMM represents authority as graph structure. TIS represents bounded reliance as a specific artifact contract.

```text
TSMM AuthorityGraph = system-level authority topology
TIS AuthorityBoundary = artifact-level authority constraint
```

## Projection rule

A TIS authority boundary SHOULD be derived from one or more TSMM authority nodes, edges, or delegation chains. The boundary MUST preserve:

- authoritative party;
- authority type or basis;
- scope;
- delegation requirement;
- revocation actor and status-check requirement;
- relying-party constraints;
- evidence references.

## Revocation

If a TSMM authority edge is revocable, the TIS authority boundary SHOULD include revocation metadata and a relying-party constraint requiring status checks before reuse.

See `examples/cross-repo/authority-graph-to-boundary.example.json`.
