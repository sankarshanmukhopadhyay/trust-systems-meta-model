---
owner: maintainers
last_reviewed: 2026-03-29
applicable_version: v0.14.0
tier: 1
---

# TSMM Roadmap

This file records plausible next steps for TSMM after v0.14.0. It is directional. It is not a schedule.

## Current main-branch status

- **Completed on main branch (no release):** canonical primitive catalog formalization for the meta-model core
- **Completed on main branch (no release):** explicit ecosystem binding contracts and validation/test-vector scaffolding
- **Current main-branch direction:** deepen authority, delegation, lifecycle, assurance portability, and interoperability semantics with more concrete system coverage

## Newly completed modeling surfaces on main branch

- canonical authority graph and delegation pattern catalog
- machine-readable lifecycle state model
- compact assurance property model for evidence, verification, auditability, and revocation traceability
- interoperability matrix covering structural, semantic, and behavioral comparison modes
- concrete system examples for TRQP-style registry, OpenID Federation, and decentralized directory patterns

## 1. Agent role and control semantics

- determine whether agent class should remain an extension concept or be promoted into a more reusable cross-domain actor taxonomy
- deepen control-mode semantics so side-car, staged, and review-bound execution patterns can be compared more precisely
- add stronger examples for identity-proxy, execution, predictive, and coordination agents

## 2. Attention governance and signal routing

- expand attention-policy examples beyond single-agent screening into digital twin and unified-feed patterns
- connect interruption and routing logic more directly to trust decisions, evidence, and remediation
- explore how sender reputation, urgency scoring, and delivery pricing can be represented without overfitting TSMM to one product model

## 3. Registry and publication tooling

- expand registry validation and discovery behaviors
- add stronger artifact integrity and packaging guidance
- improve rendered graph outputs for assurance and review workflows

## 4. Agent governance operations

- deepen agent trace verification patterns
- improve delegated-action governance examples
- connect multi-agent coordination more tightly to review and remediation processes

## 5. Agent Interaction Extension *(completed in v0.14.0)*

All ten abstractions of the Agent Interaction Extension are now delivered. The A2A binding and crosswalk are published. The extension is available for implementer use and protocol-specific profiling.

## 6. Binding and crosswalk coverage

- add further machine-readable bindings for adjacent governance and assurance ecosystems
- improve comparison guidance across bindings so the catalog becomes easier to operationalize
- continue crosswalk work where external models expose missing but reusable TSMM structure

## OASF integration follow-through

A completed next increment is to move from semantic OASF binding to profile-level publication guidance so TSMM profiles, ANAB control publication, and DCAS evaluation outputs can travel through a shared OASF-facing surface without losing traceability.
