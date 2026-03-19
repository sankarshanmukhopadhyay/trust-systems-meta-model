---
owner: maintainers
last_reviewed: 2026-03-19
applicable_version: v0.12.0
tier: 1
---

# TSMM Glossary

## Assessment
A structured evaluation activity that tests or reviews whether requirements, controls, claims, or profiles are satisfied.

## Artifact
A structured object that carries trust-relevant information, such as metadata, a policy file, a registry record, a credential, or a conformance report.

## Authority
A bounded right, mandate, or recognized competence attached to a role.

## Claim
A proposition asserted by or about an entity, artifact, system, or state.

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

## Governance Context
The governing environment within which trust decisions are made, including legal, institutional, contractual, and ecosystem constraints.

## Level Framework
A tiered expression of expected rigor or trust posture, such as assurance levels or conformance levels.

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

## Profile
A packaged set of requirements, controls, or evaluation expectations defined for a particular context or implementation class.

## Requirement
A normative or expected condition that a system, artifact, process, or participant should satisfy.

## Role
A context-specific capacity in which an entity acts.

## Threat
A modeled harm, abuse case, or failure mode.

## Trust Decision
The evaluated outcome produced under policy, evidence, verification, and context.

## Verification
A process that checks validity, conformance, integrity, or other required conditions.
