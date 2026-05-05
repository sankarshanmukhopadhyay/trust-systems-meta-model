---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# OpacityBoundary

## Concept definition

An **OpacityBoundary** is a structural governance constraint that declares what is
deliberately not observable about an agent's operation and what the trust and evidence
implications of that non-observability are.

A2A's foundational design principle is that agents collaborate without exposing
internal state, memory, or tools. This is not a defect or an oversight — it is a
design invariant that enables agent opacity as a feature: protection of intellectual
property, separation of concerns, and security of internal implementation. TSMM
respects this. But it has direct governance consequences that must be modeled explicitly.

TSMM's existing model describes what is observable: entities, roles, artifacts, claims,
evidence, and trust decisions. OpacityBoundary models the complement: what is
structurally unknowable about an agent, and how trust decisions must be scoped given
what cannot be verified.

## Trust significance

Without an explicit opacity model, trust frameworks implicitly assume observability. A
policy that requires "evidence of correct behavior" cannot be evaluated against an agent
whose behavior is opaque by design. An assessment that checks "all reasoning steps are
auditable" will return indeterminate results for any agent that does not expose its
reasoning trace.

OpacityBoundary makes this explicit. It records:

1. **What components are opaque.** Internal state, tool set, memory, reasoning trace, or
   other components that counterparties structurally cannot inspect.

2. **What the evidence gap is.** A specific description of what cannot be verified given
   this opacity boundary. This is not a generic disclaimer — it is a governance-specific
   statement of what evidence is structurally unavailable.

3. **How trust decisions must be scoped.** Given the evidence gap, how must a trust
   decision about or involving this agent be bounded? What claims about the agent can
   and cannot be substantiated?

4. **What mitigations apply.** Controls that partially compensate for the evidence gap:
   attestation, external audit access, behavioral monitoring, or contractual commitment.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Evidence` | OpacityBoundary defines the boundary of what evidence is obtainable. Evidence claims that exceed this boundary are structurally unsupportable. |
| `Assessment` | An assessment of an opaque agent must scope its conclusions to what is observable. The `evidenceGap` in an OpacityBoundary should inform the assessment's scope limitations. |
| `TrustDecision` | `trustScopeConstraint` directly constrains what claims can be supported in a trust decision about an opaque agent |
| `Control` | `mitigations` reference compensating controls for the evidence gap. These are controls in the TSMM sense: safeguards that reduce a defined risk. |
| `Artifact` | An OpacityBoundary is attached to an agent entity but is itself a governance artifact: a structured record of an observable constraint |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `agentRef` | Yes | The agent entity whose opacity this boundary describes |
| `opaqueComponents` | Yes | Components that are not observable: `internalState`, `toolSet`, `memory`, `reasoningTrace`, `other` |
| `evidenceGap` | Yes | What cannot be verified about this agent given its opacity |
| `trustScopeConstraint` | Yes | How trust decisions must be bounded given this opacity |
| `mitigations` | No | Compensating controls: `attestation`, `audit`, `behavioral-monitoring`, `contractual-commitment` |

## Opaque component vocabulary

| Value | Meaning |
|---|---|
| `internalState` | The agent's current operational state is not externally visible |
| `toolSet` | Which tools the agent has access to or invokes is not disclosed |
| `memory` | The agent's persistent or session memory is not accessible to counterparties |
| `reasoningTrace` | The steps by which the agent reached a decision or output are not exposed |
| `other` | Other agent components not covered by the above; should be described in `evidenceGap` |

## Design notes

**Opacity is a design invariant, not a deficiency.** OpacityBoundary does not imply
that an opaque agent is untrustworthy. It means that trust decisions about that agent
must be calibrated to what can actually be verified. A well-governed opaque agent with
strong attestation and contractual commitments may be more trustworthy than a partially
transparent agent with weak evidence.

**Evidence gap is specific, not generic.** The `evidenceGap` field should describe the
specific governance consequence of the opacity — what particular claims, assessments,
or verifications cannot be completed — not a generic disclaimer about opacity.

**Mutual opacity.** In peer-to-peer agent interactions both parties may carry
OpacityBoundaries. Governance must account for bilateral opacity, not only opacity of
one party.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Agentic AI extension: `docs/extensions/agentic-ai-extension.md`
- Extension index: `docs/extensions/index.md`
