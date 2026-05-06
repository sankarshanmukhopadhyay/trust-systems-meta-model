---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# TSMM Glossary

## Assessment
A structured evaluation activity that tests or reviews whether requirements, controls, claims, or profiles are satisfied.

## AuthorizationCheckpoint
A first-class trust event representing a runtime authorization challenge that interrupts or pauses an interaction pending resolution. An AuthorizationCheckpoint is structurally distinct from policy evaluation: it signals that the inputs required for evaluation are absent or insufficient and that the interaction cannot proceed until the gap is resolved. Trigger conditions include `policy-gap`, `auth-required`, `input-required`, and `scope-exceeded`. See `docs/model/authorization-checkpoint.md`.

## Artifact
A structured object that carries trust-relevant information, such as metadata, a policy file, a registry record, a credential, or a conformance report.

## Authority
A bounded right, mandate, or recognized competence attached to a role.

## Claim
A proposition asserted by or about an entity, artifact, system, or state.

## ContentProvenancePolicy
A governance policy specifying what must be known and verified about interaction payload content before it can be acted upon, stored, or forwarded. Defined per content modality (text, structured-data, file-reference, audio-video, embedded-ui, other). Models provenance requirements, sanitization obligations, redaction rules, and evidence capture obligations — not wire-level content type details. See `docs/model/content-provenance-policy.md`.

## Control
A safeguard that reduces a defined risk or constrains unsafe behavior.

## Agent Class
A typed descriptor for the operating posture of an agentic actor. TSMM defines five classes: identity-proxy, execution, predictive, coordination, and attention-gateway. Agent class is used alongside control mode to make explicit what kind of role an agent fills and under what governance shape it operates. See `docs/model/agent-role-classification.md`.

## Attention Policy
An extension object that governs how inbound signals are admitted, deferred, summarized, rerouted, or rejected before reaching a principal or downstream decision layer. An attention policy records the delivery mode, interruption budget, escalation rule, and signal source for a given attention-gateway agent. See `docs/model/attention-governance.md`.

## Control Mode
A descriptor for the human-oversight shape of an agent's runtime behavior. TSMM defines four control modes: human-in-loop, human-on-loop, sidecar, and fully-bounded-autonomous. Control mode makes the governance posture of agent behavior explicit so that policy, evidence, and oversight requirements can be aligned to it. See `docs/model/agent-role-classification.md`.

## Dynamic Authorization
A family of approaches to access control in which authorization decisions are made at runtime by evaluating contextual attributes against an externalized policy. The canonical architecture separates policy administration (PAP), policy decision (PDP), policy enforcement (PEP), and policy information retrieval (PIP). Within TSMM, dynamic authorization is a runtime evaluation specialization of the Policy → Trust Decision → Effect chain, not a replacement framing for it. See `docs/model/dynamic-authorization-framing.md`.

## Effect
The downstream consequence a system permits, denies, downgrades, routes, or records after a trust decision.

## Entity
A participant in the trust system, such as a person, organization, software agent, verifier, or registry operator.

## Evidence
Material used to substantiate a claim, control implementation, requirement outcome, or assessment result.

## Evidence Artifact
A typed, structured output produced by an operational system, authorized actor, or assessment process to demonstrate that a rule was checked, a behavior occurred, or a condition holds. Evidence artifacts specialize the Evidence abstraction with production context, artifact type, integrity anchors, and traceability fields. Defined types include reconciliation, drift, attestation, and conformance. See `docs/model/evidence-artifact.md`.

## ExtensionContract
A protocol-neutral abstraction for negotiated extension compatibility in agent or protocol interactions. Captures extension URI, version, requiredness, negotiated status (`accepted`, `degraded`, `rejected`, `not-attempted`), and failure handling. The negotiation record is governance-relevant: silent capability downgrade without a recorded failure signal creates an audit gap. Generalizes across A2A, MCP, OpenID Federation, and any extension-carrying protocol. See `docs/model/extension-contract.md`.

## Governance Context
The governing environment within which trust decisions are made, including legal, institutional, contractual, and ecosystem constraints.

## Level Framework
A tiered expression of expected rigor or trust posture, such as assurance levels or conformance levels.

## InteractionContext
A session or conversation scope that groups tasks, messages, and trust decisions into a shared governance envelope. Extends `ExecutionContext` to the session level: captures accumulated governance state across a sequence of interactions, including what authority and evidence carry forward and what conditions trigger re-authorization. See `docs/model/interaction-context.md`.

## InteractionTask
A durable, stateful work unit with governance-significant state transitions (submitted, working, input-required, auth-required, completed, cancelled, failed), artifact accumulation, and cancellation/continuation semantics. Distinct from `ExecutionContext` (per-evaluation operational parameters) and `InteractionContext` (session-level governance envelope). The `auth-required` and `input-required` states link to an `AuthorizationCheckpoint`. See `docs/model/interaction-task.md`.

## Lifecycle Event
A state change relevant to trust posture, such as issuance, revocation, expiry, reassessment, or remediation closure.

## Open Trust Artifact Model (OTAM)
A shorthand for the canonical trust artifact layer implemented in the `trust-infrastructure-schemas` repository. OTAM expresses concrete machine-readable formats for assurance declarations, conformance statements, governance credentials, and related trust artifacts. TSMM does not replace OTAM; it supplies the abstract semantics those artifacts instantiate.

## Policy
Rules that govern how the system evaluates trust-relevant inputs and chooses an outcome.

## Policy Administration Point (PAP)
The component where policies are authored, versioned, and governed. In TSMM terms, where Policy, Profile, and Requirement objects are defined under a Governance Context. See `docs/model/dynamic-authorization-framing.md`.

## Policy Decision Point (PDP)
The component that evaluates a policy against a specific authorization request and produces a structured decision. In TSMM terms, the evaluation step within Trust Decision production. See `docs/model/dynamic-authorization-framing.md`.

## Policy Enforcement Point (PEP)
The component that enforces a policy decision by permitting or blocking an effect and fulfilling any obligations attached to the decision. See `docs/model/dynamic-authorization-framing.md`.

## Policy Information Point (PIP)
The component that retrieves contextual attribute data to support PDP evaluation. In TSMM terms, the retrieval of Evidence, Artifact state, and Lifecycle Event data. See `docs/model/dynamic-authorization-framing.md`.

## ObservabilityMode
The governance observability properties of an interaction delivery channel — what can be known about delivery, timing, and progress given the channel's delivery model (`synchronous`, `streaming`, `polling`, `push-callback`). Properties include `auditabilityLevel` (full / partial / metadata-only / none), `replayRisk`, `userAwarenessModel` (real-time / delayed / opaque), and required compensating controls. Models governance implications, not transport mechanics. See `docs/model/observability-mode.md`.

## OpacityBoundary
A structural governance constraint declaring what is deliberately not observable about an agent's operation and the trust and evidence implications of that non-observability. TSMM models what is observable; OpacityBoundary models what is structurally unknowable and how trust decisions must be scoped accordingly. Properties include `opaqueComponents` (internalState, toolSet, memory, reasoningTrace), `evidenceGap`, `trustScopeConstraint`, and optional `mitigations`. See `docs/model/opacity-boundary.md`.

## PeerTrustRelation
A trust relationship between lateral agents operating as peers with no pre-existing hierarchical relationship. Structurally parallel to but distinct from `Delegation`: where Delegation is vertical (principal → sub-agent), a PeerTrustRelation is lateral (peer ↔ peer) and neither party holds authority over the other. Trust basis may be `credential-exchange`, `capability-negotiation`, `policy-acceptance`, or `third-party-introduction`. See `docs/model/peer-trust-relation.md`.

## Profile
A packaged set of requirements, controls, or evaluation expectations defined for a particular context or implementation class.

## Requirement
A normative or expected condition that a system, artifact, process, or participant should satisfy.

## Role
A context-specific capacity in which an entity acts.

## ServiceDescriptor
A trust-relevant capability disclosure artifact whose visibility is policy-bound and whose authenticity may be signed. The structured surface through which an agent, service, or system publishes what it is, what it can do, and how it can be reached — under a declared disclosure policy (`public`, `authenticated`, or `restricted`). Generalizes Agent Card, OpenID Federation entity statement, and TRQP ecosystem descriptor constructs. See `docs/model/service-descriptor.md`.

## SkillContract
An operational contract for a discrete capability unit, separating what an entity can do (capability) from what it may do under defined modalities, scopes, and policy conditions (operational envelope). A SkillContract governs a `Capability` object and defines `inputModes`, `outputModes`, `authorizationScope`, and applicable `policyConditions`. See `docs/model/skill-contract.md`.

## Threat
A modeled harm, abuse case, or failure mode.

## Trust Decision
The evaluated outcome produced under policy, evidence, verification, and context.

## Verification
A process that checks validity, conformance, integrity, or other required conditions.


## v0.19.0 agent interaction governance terms

### Discovery Governance

A TSMM model surface for describing how descriptors are discovered, who mediates them, what access policy applies, how freshness is evaluated, what integrity controls are required, and what happens when discovery fails.

### Capability Negotiation

A TSMM model surface for determining whether an advertised capability becomes discoverable, negotiated, authorized, executed, and evidenced under policy.

### Task Evidence Lifecycle

A TSMM model surface for treating task state transitions as governance-relevant events that require evidence, receipts, artifacts, or review triggers.

### Authenticated Extended Descriptor

A descriptor whose fuller contents are disclosed only after authentication or authorization. Generalizes the A2A authenticated extended Agent Card pattern.

### Required Extension Failure

A negotiation condition where a requester requires an extension that the provider does not support or cannot authorize. In TSMM, this must lead to rejection or review rather than silent downgrade.
