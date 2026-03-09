---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# Trust Reference Assurance Architecture Crosswalk

This crosswalk maps the **Trust Reference Assurance Architecture (TRAA)** approach to TSMM and the TSMM Assurance Extension.

## Crosswalk summary

| TRAA concept | TSMM concept | TSMM Assurance Extension concept |
|---|---|---|
| Applications / ecosystem layer | Governance context, profiles, effects | — |
| Infrastructure architecture layer | Governance context, entities, policies | — |
| Credential / identity layer | Entities, artifacts, verification | Trust task |
| Secure transport layer | Controls, requirements | Control family |
| Trust assurance layer | Assessment, verification, trust decision | Assurance activity, assurance method, assurance decision |
| Artifact / data layer | Artifacts, evidence | Evidence artifact, evidence bundle, validation record |
| Threat modeling layer | Threats, controls | Control objective |
| Control catalog | Controls, requirements | Control family, control objective |
| Trust task taxonomy | Verification, evidence generation | Trust task |
| Validation methodology | Assessment, verification | Assurance method |
| Assurance result | Trust decision | Assurance decision |

## Interpretation

TRAA overlaps strongly with TSMM but sits at a different layer.

- **TSMM** provides the abstract trust-system grammar.
- **TRAA** provides an assurance-oriented architecture and workflow shape.
- The **TSMM Assurance Extension** is the modular bridge between them.

## Recommendation

TRAA should be treated as a **TSMM-aligned assurance architecture specialization**, not as a replacement for TSMM core and not as an unrelated side model.
