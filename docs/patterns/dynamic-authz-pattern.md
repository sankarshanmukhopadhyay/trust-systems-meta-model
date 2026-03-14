---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
status: experimental
status_note: >
  This pattern maps a runtime evaluation concept onto TSMM abstractions using
  existing core objects. It does not introduce new schema primitives. Promotion
  of dynamic authorization concepts into core is deferred pending implementation
  experience. See docs/model/dynamic-authorization-framing.md before reading
  this document.
---

# Dynamic Authorization Pattern

## Pattern summary

A Policy Enforcement Point intercepts a request, passes a structured authorization query to a Policy Decision Point, receives a structured decision with obligations, and permits or denies the effect. The PDP's evaluation is governed by policy administered under a TSMM governance context.

## Read first

This pattern assumes familiarity with TSMM's position on dynamic authorization. Read `docs/model/dynamic-authorization-framing.md` before using this pattern in an implementation design.

## TSMM mapping

- **Entity + Role + Authority**: the subject making the request and the bounded authority that makes the request potentially valid
- **Artifact**: the resource or target object the request concerns
- **Governance Context + Profile + Policy**: administered in the PAP; shape what decisions the PDP is permitted to produce
- **Evidence + Lifecycle state**: retrieved by the PIP to inform PDP evaluation
- **Verification**: the PDP evaluation — the computation that produces a structured decision from a request and a policy
- **Trust Decision**: the outcome of PDP evaluation (permit, deny, indeterminate, notApplicable)
- **Effect**: the operational consequence permitted or denied; carrying class, action, status, and any obligation conditions
- **Control**: obligations attached to a permit decision that the PEP must fulfill

## Key structural rules

**The PDP evaluates; the PEP enforces.** Policy evaluation and policy enforcement are separated concerns. A PEP that modifies a decision rather than enforcing it as produced is an authorization bypass, not a graceful degradation.

**Obligations are not optional.** A permit decision carrying an obligation that the PEP cannot fulfill must be treated as deny. An unfulfilled obligation is a governance gap, not an acceptable partial compliance.

**The governance context shapes the policy; the policy does not define its own governance context.** The PAP operates within a TSMM governance context. That context determines what policies are permissible, how they are versioned, and who may administer them. Policy correctness within the PDP does not substitute for governance legitimacy in the PAP.

**Context is broader than attributes.** The PIP retrieves attribute values for PDP evaluation. But TSMM context includes lifecycle state (revocation, suspension, expiry) and evidence quality, which are not always expressible as simple attributes. Implementations should treat lifecycle state as a first-class input to PDP evaluation, not as an attribute that may or may not be present.

**Effect retains its TSMM structure.** A dynamic authorization decision produces an effect. That effect should carry TSMM's `class`, `action`, and `status` distinctions — not collapse to a binary permit flag. Allow informational use but deny rights-affecting action is a meaningful governance output that a binary flag cannot express.

## Sequence

```text
Request arrives at PEP
  -> PEP constructs authorization query:
       subject attributes (entity, role, authority scope)
       action attributes (requested operation)
       resource attributes (artifact or target)
       environment attributes (execution context, lifecycle state)
  -> PEP submits query to PDP

PDP evaluates:
  -> retrieves additional attributes from PIP
       (evidence state, artifact validity, lifecycle events)
  -> evaluates applicable Policy under Governance Context and Profile
  -> produces structured decision:
       outcome: permit | deny | indeterminate | notApplicable
       obligations: conditions PEP must fulfill
       advice: non-mandatory guidance

PEP receives decision:
  -> if permit with obligations: fulfill obligations or treat as deny
  -> if permit without obligations: allow Effect (class, action, status)
  -> if deny: block Effect, record Trust Decision
  -> if indeterminate: escalate to human review or apply deny-safe default
  -> if notApplicable: apply governance-defined default (typically deny-safe)

Trust Decision and Effect are recorded:
  -> decision outcome, policy reference, effect class/action/status retained
  -> obligations fulfilled or denial reason retained as Evidence
```

## Example scenario

A verifiable credential verifier intercepts a relying party request to accept a credential for a high-assurance transaction. The PEP submits a query: subject is the relying party (role: verifier), action is credential acceptance, resource is the credential artifact, environment includes current assurance level requirement and credential revocation state.

The PDP evaluates the reliance policy under the governance context (a regulated trust registry program). The credential's revocation state is retrieved from the PIP. The policy requires assurance level AL2 and a valid revocation check. The PDP produces: permit, with obligation to log the acceptance and notify the governance hub.

The PEP fulfills the obligation (logs and notifies), then permits the effect: `class: reliance`, `action: accept-credential-for-high-assurance-transaction`, `status: active`.

## TSMM core mappings

- The authorization query maps to the implicit inputs of a TSMM `Trust Decision`: entity, role, authority, artifact, policy, context, evidence, and verification results
- The PDP decision maps to a TSMM `Trust Decision` with `outcome`, `policyRef`, and `effectRefs`
- Obligations map to conditions in TSMM `Authority` objects or action requirements on `Effect` objects
- The PIP retrieval maps to TSMM `Evidence` and `Lifecycle Event` lookups feeding into `Verification`
- The PAP maps to where TSMM `Policy`, `Profile`, and `Requirement` objects are administered under `Governance Context`

## Non-goals

This pattern does not define PDP wire protocols, attribute schema formats, policy language syntax, or specific OPA/Cedar/XACML implementation guidance. It addresses the trust governance layer: how a dynamic authorization decision fits within the TSMM governance chain, what structural rules it must respect, and what it must preserve from the TSMM effect model.
