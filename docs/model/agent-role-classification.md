---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 1
---

# TSMM Agent Role Classification

## Purpose

TSMM already models entities, roles, bounded authority, policy, evidence, and trust decisions. What v0.12.0 adds is a clearer way to describe **what kind of agentic actor is in scope** when delegated action is being evaluated.

This matters because not all agents are doing the same job. A digital twin that speaks on behalf of a principal, a virtual assistant that executes bounded tasks, and a predictive side-car that prepares likely next steps should not be treated as governance-equivalent simply because each is called an “agent”.

## Classification dimensions

### 1. Agent class

TSMM uses `agentClass` to distinguish broad operating posture:

- **identity-proxy** — an agent that represents or speaks for a principal in external contexts
- **execution** — an agent that performs bounded tasks or action paths under delegation
- **predictive** — an agent that stages, prioritizes, or recommends likely next steps without directly committing effects
- **coordination** — an agent that routes, sequences, or supervises other agents or workflows
- **attention-gateway** — an agent that filters, prioritizes, or modulates inbound signals before they reach a principal or another decision layer

### 2. Control mode

TSMM uses `controlMode` to capture the governance shape of behavior:

- **human-in-loop**
- **human-on-loop**
- **sidecar**
- **fully-bounded-autonomous**

The point is not to rank these as universally better or worse. The point is to make the operating posture explicit so policy, evidence, and oversight can be aligned with it.

### 3. Authority posture

TSMM already models delegation. v0.12.0 strengthens guidance so that delegated authority can be interpreted together with agent class. An identity-proxy agent usually needs stronger representation controls than a predictive side-car. An execution agent usually needs tighter capability and trace controls than an attention-gateway.

## Why TSMM needs this

Without typed agent roles, governance logic drifts toward vague statements such as “the agent was authorized”. That hides the practical question. Authorized to do **what kind of thing**, in **what posture**, and with **what review expectations**?

These distinctions make the agentic extension more useful for:

- delegated digital twin systems
- personal AI assistants
- multi-agent orchestration
- trust registries and agent discovery catalogs
- assurance and conformance profiling

## Relationship to other TSMM artifacts

- `docs/extensions/agentic-ai-extension.md` explains the extension scope
- `docs/model/attention-governance.md` explains how signal routing and interruption control fit effect-centered trust logic
- `docs/crosswalks/agent-taxonomy-ssa-crosswalk.md` maps external source concepts into TSMM terms

## Design note

This release deliberately keeps these concepts in the agentic extension and supporting model docs. They are useful and increasingly reusable, but they are not yet forced into TSMM core as universal primitives.
