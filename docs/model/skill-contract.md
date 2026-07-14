---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.22.0
tier: 1
---

# SkillContract

## Concept definition

A **SkillContract** is an operational contract for a discrete capability unit. It
separates two things that are frequently conflated:

- **Can do X** — the capability: the agent has the technical ability to perform an
  action
- **May do X under these conditions** — the operational envelope: the agent is permitted
  to perform that action under defined modalities, within a bounded scope, and subject
  to declared policy conditions

The SkillContract models the second. It is the governance surface of a capability, not
the capability's implementation.

## Trust significance

A trust decision cannot correctly evaluate whether an agent should be permitted to use
a capability without knowing:

- what modalities of input and output are in scope for that capability
- what authorization scope governs its use
- what policy conditions must be satisfied before it may be exercised

Without SkillContract-level precision, policies must either over-grant (permit the whole
capability when only part of its envelope is authorized) or produce indeterminate
decisions when scope details are missing. Both outcomes compromise the trust decision
chain.

The SkillContract is particularly important in peer-to-peer agent interactions where
neither party holds delegated authority over the other. In those cases, a
`PeerTrustRelation` establishes that trust exists between the parties; the SkillContract
defines what specifically may be done within that trust.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Capability` | SkillContract governs a capability. `capabilityRef` links to the underlying capability object. A capability may have multiple SkillContracts for different contexts. |
| `Policy` | `policyConditions` in a SkillContract reference or summarize the policy rules that gate exercise of the skill |
| `Authority` | The `authorizationScope` in a SkillContract must be consistent with an authority object in the governance context |
| `TrustDecision` | The Policy evaluation chain must resolve SkillContract conditions as part of producing a trust decision for an action |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `capabilityRef` | Yes | The capability this contract governs |
| `inputModes` | Yes | Accepted input modalities (e.g. `text`, `structured-data`, `file-reference`) |
| `outputModes` | Yes | Produced output modalities |
| `authorizationScope` | Yes | The authorization boundary for exercising this skill |
| `policyConditions` | No | Policy conditions that must be satisfied before exercise |
| `tags` | No | Classification tags for discovery and filtering |
| `examples` | No | Illustrative input/output examples |

## Design notes

**Modality-level granularity is trust-significant.** The same underlying capability
may produce very different risk profiles depending on whether its input is text (low
sanitization risk) or a file reference (SSRF, path traversal, redaction exposure). The
SkillContract makes this distinction explicit at the governance layer so policies and
evidence requirements can be calibrated accordingly.

**Authorization scope is distinct from capability scope.** A capability may be technically
capable of producing an effect across a wide range. The SkillContract's `authorizationScope`
defines the subset that is authorized, not the subset that is possible. Keeping these
separate prevents authorization creep through capability expansion.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Extension index: `docs/extensions/index.md`
