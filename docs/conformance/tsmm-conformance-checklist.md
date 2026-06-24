---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# TSMM Conformance Self-Assessment Checklist

## Purpose

This checklist provides a structured self-assessment tool for implementations claiming conformance with a TSMM profile. It translates the normative requirements in the three profile documents into a concrete yes/no review format.

For each item, mark the result as **Yes**, **No**, or **N/A with justification**. A conformant implementation must satisfy all required items at the target profile tier and all tiers below it.

---

## Tier 1: Minimal Profile

Reference: `docs/conformance/tsmm-profile-minimal.md`

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| M-1 | At least one entity with a defined type and identifier is present | | |
| M-2 | At least one role is attached to an entity | | |
| M-3 | At least one bounded authority is linked to a role | | |
| M-4 | At least one policy governing a trust decision is defined | | |
| M-5 | At least one trust decision with a defined outcome is present | | |
| M-6 | At least one effect is linked from the trust decision | | |
| M-7 | All JSON instances validate against the applicable TSMM schema without errors | | |

**Minimal Profile outcome:** All M-1 through M-7 items satisfied = Minimal Profile conformant.

---

## Tier 2: Operational Profile

Reference: `docs/conformance/tsmm-profile-operational.md`

*Requires Minimal Profile baseline. Complete Tier 1 before proceeding.*

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| O-1 | All Minimal Profile items are satisfied | | |
| O-2 | A governance context is defined and linked to at least one policy | | |
| O-3 | At least one profile with associated requirements is defined | | |
| O-4 | Lifecycle events are defined for at least suspension, revocation, or expiry for applicable entities or artifacts | | |
| O-5 | At least one verification process is defined with a method and result | | |
| O-6 | At least one threat or failure mode relevant to the system is documented | | |
| O-7 | Trust decisions reference the policies that produced them | | |
| O-8 | Effects are differentiated (i.e., the system distinguishes allow, deny, downgrade, or route as appropriate to the use case) | | |

**Operational Profile outcome:** All O-1 through O-8 items satisfied = Operational Profile conformant.

---

## Tier 3: Assured Profile

Reference: `docs/conformance/tsmm-profile-assured.md`

*Requires Operational Profile baseline. Complete Tier 2 before proceeding.*

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| A-1 | All Operational Profile items are satisfied | | |
| A-2 | An evidence package is present and linked to at least one requirement, control, or claim | | |
| A-3 | At least one structured assessment is defined with a method and a result | | |
| A-4 | Verification inputs and outcomes are traceable to specific trust decisions | | |
| A-5 | Controls are explicitly mapped to threat classes or failure modes | | |
| A-6 | A human review, remediation, or exception escalation path is defined | | |
| A-7 | Evidence is sufficient to reproduce or audit the assessment result without relying solely on declarative claims | | |

**Assured Profile outcome:** All A-1 through A-7 items satisfied = Assured Profile conformant.

---

## Extension checklists

### Agentic AI Extension

Reference: `docs/extensions/agentic-ai-extension.md`

Use this checklist in addition to the applicable base profile checklist when an implementation uses the agentic extension.

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| AE-1 | Every agent has a defined delegation from an originating principal | | |
| AE-2 | No agent authority is inferred from identity alone | | |
| AE-3 | Each delegation has a bounded scope and a defined revocation status | | |
| AE-4 | Capability is bound to a risk tier for every agent that takes rights-affecting actions | | |
| AE-5 | Oversight mode is set explicitly for every action | | |
| AE-6 | A trace record is produced for every executed action | | |
| AE-7 | For multi-agent coordination: sub-delegation permission is explicitly granted rather than inferred | | |
| AE-8 | For multi-agent coordination: oversight mode escalates to the strictest mode present in the delegation chain | | |

#### Agent classification and attention governance *(v0.12.0)*

Reference: `docs/model/agent-role-classification.md`, `docs/model/attention-governance.md`

Use these additional items when an implementation uses the agent classification or attention governance concepts introduced in v0.12.0.

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| AC-1 | Agent class is declared for each agent in scope | | |
| AC-2 | Control mode is declared and is consistent with the oversight mode assigned to governed actions | | |
| AC-3 | Representation scope is documented for identity-proxy agents | | |
| AC-4 | Where an attention-gateway agent is present, an attention policy with a defined escalation rule is associated with it | | |
| AC-5 | Interruption budget and delivery mode are documented for attention policies that govern rights-affecting or time-sensitive signals | | |

### Verifiable Trust Communities Extension

Reference: `docs/extensions/verifiable-trust-communities-extension.md`

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| VTC-1 | Each community has a defined charter and at least one boundary rule | | |
| VTC-2 | Membership standing is tracked and can reflect active, suspended, or expelled states | | |
| VTC-3 | Recognition between communities is explicit and revocable | | |
| VTC-4 | Sanctions and remediation paths are defined | | |

### Assurance Extension

Reference: `docs/extensions/assurance-extension.md`

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| AS-1 | Assurance activities reference a defined level framework | | |
| AS-2 | Assurance outcomes are linked to trust decisions | | |
| AS-3 | Evidence referenced in assurance activities exists and is retrievable | | |

### Agent Interaction Extension *(v0.13.0)*

Reference: `docs/model/service-descriptor.md`, `docs/model/skill-contract.md`, `docs/model/interaction-context.md`, `docs/model/authorization-checkpoint.md`, `docs/model/extension-contract.md`, `docs/model/opacity-boundary.md`, `docs/model/peer-trust-relation.md`

Use this checklist in addition to the applicable base profile checklist when an implementation uses the agent interaction extension. Items prefixed with the abstraction name apply only when that abstraction is in use.

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| AI-1 | *(ServiceDescriptor)* Every agent or service that initiates or accepts agent-to-agent interactions has a ServiceDescriptor with a declared `disclosurePolicy` | | |
| AI-2 | *(ServiceDescriptor)* Authenticated or restricted ServiceDescriptors carry an `authenticityBinding` reference | | |
| AI-3 | *(SkillContract)* Every capability exercised in an agent interaction has a corresponding SkillContract with explicit `inputModes`, `outputModes`, and `authorizationScope` | | |
| AI-4 | *(SkillContract)* The `authorizationScope` in each SkillContract is consistent with an authority object in the applicable governance context | | |
| AI-5 | *(PeerTrustRelation)* Lateral agent interactions where neither party is subordinate are governed by a PeerTrustRelation rather than a Delegation | | |
| AI-6 | *(PeerTrustRelation)* The `trustScope` of every PeerTrustRelation is explicitly bounded; trust does not generalise beyond the declared scope | | |
| AI-7 | *(InteractionContext)* Multi-turn or session-scoped agent interactions are governed by an InteractionContext with explicit `inheritedAuthorityRefs` and a `reAuthorizationPolicy` | | |
| AI-8 | *(InteractionContext)* Session expiry is treated as a governance boundary: inherited authority and evidence cannot be used after `expiresAt` without re-verification | | |
| AI-9 | *(AuthorizationCheckpoint)* Any point where an interaction pauses pending authorization resolution is modeled as an AuthorizationCheckpoint with a recorded `triggerCondition` and `status` | | |
| AI-10 | *(AuthorizationCheckpoint)* `scope-exceeded` checkpoints are not resolved by credential supply alone; resolution requires principal escalation or scope reduction | | |
| AI-11 | *(OpacityBoundary)* Every agent whose internal state, tool set, memory, or reasoning trace is not observable to counterparties has an OpacityBoundary with a specific `evidenceGap` and `trustScopeConstraint` | | |
| AI-12 | *(OpacityBoundary)* Trust decisions about opaque agents are scoped to what is declared in the `trustScopeConstraint`; they do not assert claims about unobservable components | | |
| AI-13 | *(ExtensionContract)* Every extension negotiated in an interaction is recorded with `requiredness`, `negotiatedStatus`, and `failureHandling` | | |
| AI-14 | *(ExtensionContract)* A `required` extension with `negotiatedStatus: rejected` or `degraded` and `failureHandling: continue` produces an explicit governance record justifying continuation | | |

#### Agent Interaction Extension additions *(v0.14.0)*

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| AI-15 | *(InteractionTask)* Every bounded work unit in an agent interaction is modeled as an InteractionTask with an explicit `status` and a reference to its governing `InteractionContext` | | |
| AI-16 | *(InteractionTask)* Tasks with `status: auth-required` or `input-required` reference an active `AuthorizationCheckpoint` via `authorizationCheckpointRef` | | |
| AI-17 | *(InteractionTask)* Cancelled tasks carry a `cancellationReason`; the governance record does not contain open tasks with terminal status and no recorded reason | | |
| AI-18 | *(ContentProvenancePolicy)* A ContentProvenancePolicy is defined for each content modality exchanged in the interaction | | |
| AI-19 | *(ContentProvenancePolicy)* The `evidenceCaptureObligation` is implemented; evidence records for processed content can be produced on demand | | |
| AI-20 | *(ObservabilityMode)* An ObservabilityMode is declared for each delivery channel used in the interaction | | |
| AI-21 | *(ObservabilityMode)* All `requiredCompensatingControls` identified in the ObservabilityMode are implemented; channels with `auditabilityLevel: none` are not used without explicit governance justification | | |

### Dynamic Authorization Pattern *(experimental)*

Reference: `docs/patterns/dynamic-authz-pattern.md`

Read `docs/model/dynamic-authorization-framing.md` before completing this checklist. The `experimental` status means promotion to core is deferred, not that the pattern is unsuitable for use.

For agentic system implementations, also read `docs/model/agentic-authz-analysis.md`. The DA checklist covers the evaluation layer. The AE checklist (above) covers the governance envelope. Both must be completed for an agentic system implementation that uses dynamic authorization.

| # | Requirement | Satisfied? | Notes |
|---|---|---|---|
| DA-1 | Policy administration (PAP), decision (PDP), and enforcement (PEP) concerns are separated in the implementation architecture | | |
| DA-2 | PDP evaluation is governed by a TSMM Policy operating under a defined Governance Context | | |
| DA-3 | PIP attribute retrieval includes lifecycle state (revocation, suspension, expiry) as a first-class input, not as an optional attribute | | |
| DA-4 | Obligations attached to permit decisions are enforced by the PEP; an unfulfilled obligation is treated as deny | | |
| DA-5 | Effect objects retain TSMM class, action, and status structure; permit decisions are not reduced to binary flags | | |
| DA-6 | Indeterminate and notApplicable decisions have a defined governance-safe default behavior | | |
| DA-7 | Trust decisions and effects produced by the PDP/PEP are recorded with policy reference and decision outcome | | |
| DA-8 | *(Agentic systems only)* The governance envelope is in place before the PDP layer: delegation model, oversight mode, risk-tier-driven policy selection, and trace records as structured TSMM Evidence are all defined independently of the authorization evaluation | | |

---

## How to use this checklist

1. Identify the target conformance profile (Minimal, Operational, or Assured).
2. Complete all checklist items at the target tier and all tiers below it.
3. Complete extension checklists for any extensions in scope.
4. Document any No or N/A responses with a justification. A No response is a gap that must be remediated before claiming conformance at that tier.
5. Retain the completed checklist as part of the implementation evidence package.

This checklist is a self-assessment tool. It does not constitute third-party certification or independent assurance.


## Agentic profile overlay

Reference: `docs/conformance/tsmm-profile-agentic.md`

Use this section when TSMM governs delegated or agentic action. This overlay may be applied alongside the Operational or Assured baseline.

- [ ] Delegation artifacts are explicit, reviewable, and revocable
- [ ] Oversight mode is declared for governed action classes
- [ ] Risk tiers are documented with rationale
- [ ] Trace records preserve action, context, and resulting effect references
- [ ] Multi-agent coordination boundaries are documented where relevant

## v0.19.0 agent interaction conformance checklist

An implementation claiming alignment with the v0.19.0 agent interaction surfaces SHOULD demonstrate:

- descriptor discovery mode and source are identified;
- authenticated or restricted descriptors have access policy and integrity controls;
- descriptor freshness and failure behavior are explicit;
- capability negotiation records requested and accepted modes;
- required extension failures cause rejection or review;
- capability acceptance is linked to an authorization scope and policy decision;
- task transitions to `auth-required`, `completed`, `failed`, `canceled`, and `rejected` produce the required evidence;
- evidence references are suitable for audit or replay.
