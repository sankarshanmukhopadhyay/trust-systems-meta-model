---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# TSMM ↔ Agent Governance Toolkit Crosswalk *(experimental)*

This crosswalk records how selected concepts from the Microsoft Agent Governance Toolkit can be interpreted through TSMM without changing the stable core model.

## Why this crosswalk exists

The Microsoft Agent Governance Toolkit focuses on **runtime security governance for autonomous AI agents** and describes deterministic interception of agent actions before execution, zero-trust identity, policy enforcement, execution sandboxing, and reliability controls. Its architecture documentation also states that the toolkit provides deterministic application-layer interception and recommends composing with container or VM isolation for defense in depth. TSMM does not import that implementation directly. Instead, it uses the toolkit as an upstream reference for a narrower question:

**Which runtime governance ideas are conceptually portable into a trust-system meta-model?**

## Crosswalk summary

| Agent Governance Toolkit concept | TSMM interpretation | Status |
|---|---|---|
| Deterministic pre-execution interception | [Pre-effect Governance Pattern](../patterns/pre-effect-governance-pattern.md) | Experimental |
| Security boundaries | [TrustBoundary](../model/trust-boundary.md) as a supporting abstraction | Experimental |
| Policy evaluation before execution | `Policy` + `Verification` + `TrustDecision` before `Effect` | Existing model, clarified |
| Audit trail / tamper-evident decision trace | `Evidence`, `Verification`, `LifecycleEvent`, downstream receipt pattern in assurance layers | Existing model, stronger emphasis |
| Kill switch / circuit breaker / suspend | `LifecycleEvent` + effect-modulating controls | Existing model, clarified |
| Agent-to-agent / agent-to-tool boundary governance | `Authority`, `Delegation`, `InteractionContext`, `TrustBoundary` | Existing + experimental |
| Trust score | No direct normative adoption | Out of scope for core TSMM |
| Execution rings / privilege tiers | Treated as implementation-specific privilege segmentation, not a TSMM primitive | Out of scope for core TSMM |

## Adoption boundary

This repo uses the toolkit as an **upstream reference**, not as an authority over TSMM semantics. The aim is to improve modeling clarity for runtime trust decisions while preserving TSMM as a protocol-agnostic, implementation-portable meta-model.

## Recommended reading path

1. [Core model](../core-model.md)
2. [Effect evaluation model](../evaluation/effect-evaluation-model.md)
3. [TrustBoundary](../model/trust-boundary.md)
4. [Pre-effect Governance Pattern](../patterns/pre-effect-governance-pattern.md)
