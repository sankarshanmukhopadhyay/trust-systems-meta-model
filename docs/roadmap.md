---
owner: maintainers
last_reviewed: 2026-03-23
applicable_version: v0.13.0
tier: 1
---

# TSMM Roadmap

This file records plausible next steps for TSMM after v0.13.0. It is directional. It is not a schedule.

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

## 5. Agent Interaction Extension completion *(v0.14.0 target)*

- A2A binding: machine-readable `bindings/a2a/tsmm-a2a-binding.json` and `docs/bindings/a2a-binding.md` mapping all seven v0.13.0 abstractions to A2A protocol concepts
- A2A crosswalk: `docs/crosswalks/a2a-crosswalk.md` with concept-level alignment table
- `InteractionTask` resolution: determine whether `ExecutionContext` + lifecycle event composition is sufficient or whether a new schema object is warranted
- `ContentProvenancePolicy`: trust-policy envelope for interaction payload content, scoped to governance semantics not wire structure
- `ObservabilityMode`: governance coverage constraints derivable from delivery model (synchronous, streaming, polling, push-callback)
- Extended worked example exercising the full v0.14.0 surface alongside v0.13.0 abstractions

## 6. Binding and crosswalk coverage

- add further machine-readable bindings for adjacent governance and assurance ecosystems
- improve comparison guidance across bindings so the catalog becomes easier to operationalize
- continue crosswalk work where external models expose missing but reusable TSMM structure
