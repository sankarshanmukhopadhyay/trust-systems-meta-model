---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
---

# Getting Started: TSMM Implementer Guide

## Purpose

This guide gives three opinionated entry points into TSMM for practitioners who are building or assessing a real system. Rather than reading the full model before starting, pick the entry point that best matches your situation, follow the suggested reading path, and use the conformance checklist to validate your implementation.

---

## Entry point 1: Trust registry operator

**You are building or assessing a system that publishes trust-relevant metadata or assertions that relying parties consume.**

Typical examples: governance authority registry, known-issuer list, accredited service directory, verifiable data registry.

### Suggested reading path

1. `docs/core-model.md` — understand Entity, Authority, Artifact, Policy, and Effect
2. `docs/model/tsmm-entities.md` — map your registry objects to TSMM entity types
3. `docs/patterns/trust-registry-pattern.md` — see the canonical registry flow
4. `docs/conformance/tsmm-profile-operational.md` — most registry operators should target Operational
5. `examples/minimal-trust-registry-instance.json` — a concrete starting point for your instance

### Key modeling decisions

- Define the **governance context** for your registry before writing policy. Policy without a declared governing environment is ambiguous.
- Identify the **effects** your registry produces for relying parties. At minimum: allow reliance, suppress reliance, and route for manual review.
- Map your **lifecycle events** explicitly. Expiry and revocation should trigger re-evaluation at relying party policy, not silent continuation.

### Conformance target

Start with Operational Profile. Advance to Assured if you operate under regulatory obligation, support high-stakes authorization decisions, or publish assurance-level metadata to downstream systems.

---

## Entry point 2: Verifiable credential issuer or verifier

**You are building or assessing a system that issues credentials, verifies presented credentials, or makes trust decisions based on credential content.**

Typical examples: issuer service, wallet-adjacent verifier, credential status service, schema registry, selective-disclosure verifier.

### Suggested reading path

1. `docs/core-model.md` — understand Artifact, Claim, Verification, Trust Decision, and Effect
2. `docs/effect-centered-trust-decision-model.md` — understand how verification feeds into a bounded decision
3. `docs/patterns/credential-verification-pattern.md` — the canonical credential flow
4. `docs/crosswalks/trqp-tspp-crosswalk.md` or `docs/crosswalks/erc-8004-csp-crosswalk.md` — if your system aligns to one of those ecosystems
5. `examples/consumer-policy-instance.json` — consumer-side policy modeling reference
6. `docs/conformance/tsmm-conformance-checklist.md` — complete the Tier 1 and Tier 2 checklists

### Key modeling decisions

- Model **Claims** as distinct from **Evidence**. A credential makes claims. The verification process produces evidence. Do not collapse them.
- Define your **verification method** explicitly. A verification object without a method is a placeholder, not a process.
- Specify **effect differentiation**. A verifier that can only allow or deny is less expressive than the real system. Model downgrade and warning effects if your policy uses them.

### Conformance target

Operational Profile for most production deployments. Assured Profile if you are operating as a trust anchor, hub, or assurance scheme participant.

---

## Entry point 3: Agentic system builder

**You are building or assessing a system where software agents take bounded actions on behalf of principals, potentially delegating sub-tasks to other agents.**

Typical examples: procurement automation, document processing pipeline, multi-step approval workflow, AI assistant with tool access, robotic process automation with trust-relevant side effects.

### Suggested reading path

1. `docs/core-model.md` — understand Entity, Authority, Policy, Trust Decision, and Effect
2. `docs/extensions/agentic-ai-extension.md` — the full agentic extension model
3. `docs/patterns/delegated-agent-pattern.md` — single-agent delegation baseline
4. `docs/patterns/multi-agent-coordination-pattern.md` — chained delegation and coordination
5. `examples/agentic-ai-extension-instance.json` — a worked single-agent instance
6. `examples/delegated-agent-instance.json` — a core-layer delegation reference
7. `docs/conformance/tsmm-conformance-checklist.md` — complete base profile checklist plus Agentic Extension checklist

### Key modeling decisions

- **Write down the delegation before the code.** An agent that operates without a modeled delegation artifact is an agent whose authority cannot be reviewed, revoked, or audited. Model the delegation first.
- **Set oversight mode per action, not per agent.** An agent may have different oversight modes for different action types depending on risk tier and context.
- **Plan for chain governance.** If an agent may sub-delegate, model the sub-delegation permission explicitly in the parent delegation. See `docs/patterns/multi-agent-coordination-pattern.md` for the escalation rules.
- **Trace records are evidence.** Every executed action that produces a real-world effect should produce a trace record. That record is the audit foundation for the Assured Profile and for any post-incident review.

### Conformance target

Operational Profile as the baseline. For agents that touch rights-affecting data, financial transactions, or regulated processes, target Assured Profile with the Agentic Extension checklist completed.

---

## Cross-cutting guidance

### Start with effects, work backward

Before modeling entities and policies, write down the effects your system is allowed to produce. Then ask what policy, evidence, and verification conditions must hold before each effect is permitted. That backward walk defines the minimum modeling scope.

### Use the conformance checklist early

The `docs/conformance/tsmm-conformance-checklist.md` is not only a final gate. It is a useful design tool. Running through it at the start of a project surfaces gaps in policy definition, lifecycle handling, and evidence requirements before they become code debt.

### Schemas are not the model

The JSON schemas in `schemas/` express a subset of the model in machine-readable form for validation. The authoritative model is the documentation in `docs/`. When they differ, the documentation governs and the schema should be updated.

### Extensions are additive

If your system needs the Agentic AI extension, the Verifiable Trust Communities extension, or the Assurance extension, those schemas layer on top of the core. You do not need to extend the core schema. Each extension is independently versionable and independently evaluable.

---

## Where to go next

| Goal | Document |
|---|---|
| Understand all core abstractions | `docs/core-model.md` |
| Review entity definitions and mandatory fields | `docs/model/tsmm-entities.md` |
| Understand lifecycle state management | `docs/model/tsmm-lifecycle.md` |
| Model threat and control relationships | `docs/security/trust-system-threat-model.md` |
| Assess conformance | `docs/conformance/tsmm-conformance-checklist.md` |
| Map to an adjacent specification | `docs/crosswalks/` |
| Validate a JSON instance | Run `scripts/validate_examples.py` |
