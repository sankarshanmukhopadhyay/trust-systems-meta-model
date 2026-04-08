---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# TSMM Binding: A2A Protocol

The Agent2Agent (A2A) protocol is an open protocol enabling communication and
interoperability between opaque agentic applications. Its foundational design
principle is that agents collaborate without exposing their internal state, memory, or
tools — each party is a black box to the other, with trust established through
structured discovery, capability negotiation, and authenticated interaction.

TSMM models the trust-significant invariants behind A2A's protocol elements. This
binding maps those invariants explicitly.

## Primary mappings

| A2A concept | TSMM abstraction | Binding notes |
|---|---|---|
| AgentCard (public) | `ServiceDescriptor` (`disclosurePolicy: public`) | Authenticity binding optional at public tier |
| AgentCard (authenticated extended) | `ServiceDescriptor` (`disclosurePolicy: authenticated`) | `authenticityBinding` required; extended metadata conditional on credential presentation |
| Skill | `SkillContract` | `inputModes` / `outputModes` / `tags` map directly; `authorizationScope` added by TSMM as the governance layer A2A does not explicitly model |
| `contextId` | `InteractionContext.id` | TSMM adds `inheritedAuthorityRefs`, `inheritedEvidenceRefs`, and `reAuthorizationPolicy` — the governance semantics that A2A's contextId implies but does not formalize |
| Task | `InteractionTask` | A2A's `Task` object maps to `InteractionTask`; TSMM adds explicit governance significance to each status transition |
| `input-required` task state | `InteractionTask` (`status: input-required`) + `AuthorizationCheckpoint` (`triggerCondition: input-required`) | TSMM treats this as a governance checkpoint, not a transport wait state |
| `auth-required` task state | `InteractionTask` (`status: auth-required`) + `AuthorizationCheckpoint` (`triggerCondition: auth-required` or `scope-exceeded`) | TSMM models the authority boundary event explicitly |
| Extensions + required/optional negotiation | `ExtensionContract` | `requiredness` / `negotiatedStatus` / `failureHandling` map the negotiation record; TSMM adds `resolutionRecord` for audit |
| Agent opacity invariant | `OpacityBoundary` | A2A's foundational design principle (agents do not expose internal state, tools, or memory) is modeled as a structural governance constraint with explicit `evidenceGap` and `trustScopeConstraint` |
| Agent-to-agent peer interaction | `PeerTrustRelation` | A2A assumes agents collaborate as peers; TSMM formalizes the trust basis (`credential-exchange`, `capability-negotiation`, `policy-acceptance`, `third-party-introduction`) and `trustScope` |
| Message/Artifact/Part (content exchange) | `ContentProvenancePolicy` | TSMM does not mirror A2A's wire payload model; it models the governance obligations governing payload content by modality |
| SSE streaming / push notification | `ObservabilityMode` | TSMM models governance consequences (auditability level, replay risk, user awareness) not delivery mechanics |
| Security schemes in AgentCard | `ServiceDescriptor.authenticityBinding` + `SkillContract.authorizationScope` + `AuthorizationCheckpoint` | Two-layer: declared security posture in the descriptor; runtime enforcement through skill authorization scope and checkpoint raising |
| Agent discovery | `ServiceDescriptor` (`disclosurePolicy: public`) | Public discovery requires no authentication; authenticated discovery maps to `disclosurePolicy: authenticated` with credential presentation |

## Why the mapping is not 1:1

A2A and TSMM operate at different layers. A2A is a protocol specification: it defines
wire formats, JSON-RPC methods, HTTP semantics, and SDK contracts. TSMM is a meta-model:
it defines the trust-semantic invariants that underlie those protocol elements.

Three structural differences are worth noting:

**TSMM adds governance structure A2A does not formalize.** A2A's `contextId` groups
messages and tasks but does not model which authority or evidence carries forward within
a context, or when re-authorization is required. TSMM's `InteractionContext` adds that
governance layer without changing A2A's wire behavior.

**TSMM does not model wire mechanics.** A2A's JSON-RPC method names (`tasks/send`,
`tasks/get`, `tasks/cancel`), SSE framing, and retry semantics are not represented in
TSMM. They belong to the protocol layer. TSMM models what those mechanics imply for
governance observability via `ObservabilityMode`.

**TSMM models what A2A takes for granted.** A2A's opacity invariant and peer-interaction
model are design principles, not protocol elements with explicit schema representation.
`OpacityBoundary` and `PeerTrustRelation` make those principles machine-readable
governance artifacts.

## Related artifacts

- Machine-readable binding: `bindings/a2a/tsmm-a2a-binding.json`
- Agent interaction extension: `docs/extensions/index.md`
- A2A protocol repository: `https://github.com/a2aproject/A2A`
