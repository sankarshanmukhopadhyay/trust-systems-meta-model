---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 2
title: TSMM ↔ ODRL Crosswalk
permalink: /crosswalks/odrl-crosswalk.html
parent: Crosswalks
grand_parent: Documentation
---

# TSMM ↔ ODRL Crosswalk

## Why this crosswalk exists

TSMM already needs a structured way to talk about policy, requirements, constraints, and downstream effect. ODRL contributes a recognized policy-expression model for those concerns.

The architectural move here is deliberately bounded. The goal is not to flatten TSMM into ODRL. The goal is to make **ODRL a portable policy layer inside a wider trust-system model**.

## Crosswalk table

| ODRL object / surface | Closest TSMM abstraction | Assurance significance |
| --- | --- | --- |
| `Policy` | `Policy` | Portable machine-readable policy contract. |
| `permission` | `Policy` rule | Allowed action statement that may support a later trust decision. |
| `prohibition` | `Policy` rule | Disallowed action statement that can limit acceptable system behavior. |
| `duty` / `obligation` | `Policy` rule | Required action or pre-condition that matters for policy satisfaction. |
| `party`, `assigner`, `assignee` | trust participant / subject / role bearer | Preserves accountable participants without collapsing TSMM role semantics. |
| `target` asset | trust-bearing object under policy | The governed target may be a service, credential, registry object, publication, or record. |
| `constraint` | policy condition | Determines when the rule should be interpreted as applicable. |
| `profile` | bounded ecosystem interpretation | Lets a sector or community publish extensions without forking the whole stack. |
| `conflict` strategy | policy interpretation aid | Helpful for deterministic policy handling, but not a substitute for evaluator governance. |

## Practical use across this repo set

### TSMM
TSMM uses the crosswalk to identify the exact part of the meta-model where ODRL belongs: the machine-readable policy layer.

### trust-infrastructure-schemas
The schema repo uses the crosswalk to define canonical policy artifacts or policy references that can point to ODRL content while preserving clear boundaries around enforcement.

### ANAB
ANAB uses the crosswalk only for optional policy-reference publication, such as disclosure duties, usage restrictions, notice obligations, or operator-defined conditions.

## Strategic point

The important move is not “adopt ODRL everywhere.” The important move is to avoid reinventing a policy object model where a stable one already exists, while also refusing to mistake policy syntax for trustworthy governance or assured execution.
