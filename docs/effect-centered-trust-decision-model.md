# TSMM Effect-Centered Trust Decision Model

## 1. Purpose

This document explains the trust-decision logic at the heart of TSMM.

The governing question is:

> Should a system allow a specific effect to occur right now, given the acting role, bounded authority, artifact state, policy, controls, evidence, and verification results?

That question is the main hinge of the model.

## 2. Why effect comes first

Traditional identity systems often ask:

- who is this?

That is useful, but insufficient.

TSMM centers a harder and more operational question:

- what effect is being attempted
- by whom
- in what role
- under what bounded authority
- with what claims and artifacts
- under which policy
- against which threats
- supported by what evidence
- with what verification result

That is the difference between a static identity lens and a runtime legitimacy lens.

## 3. Trust decision inputs

A TSMM trust decision may take inputs from the following categories.

### 3.1 Actor context
- entity identity or identifier
- role
- delegated or direct status
- authority source

### 3.2 Authority context
- scope
- time bounds
- conditions
- obligations
- revocation state
- delegation chain

### 3.3 Artifact and claim context
- artifact type
- claim content
- signatures
- freshness
- provenance
- binding integrity

### 3.4 Policy context
- acceptance criteria
- warning thresholds
- local trust anchors
- allowlists or denylists
- mandatory review gates
- fail-open or fail-closed behavior

### 3.5 Control and threat context
- active controls
- known threat patterns
- residual risk
- environmental constraints

### 3.6 Evidence and verification context
- evidence sufficiency
- verification success or failure
- conformance or assurance level
- unresolved exceptions

### 3.7 Lifecycle context
- issuance
- expiry
- suspension
- transfer
- revocation
- reassessment
- remediation status

## 4. Decision outputs

A TSMM trust decision may produce one or more outputs.

- **accept**
- **accept with warning**
- **deny**
- **defer**
- **quarantine**
- **downgrade**
- **route to human review**
- **require stronger evidence**
- **require stronger control posture**

The right output depends on both risk and effect sensitivity.

## 5. Effect classes

Not all effects are equal. TSMM encourages implementations to classify effects explicitly.

### 5.1 Informational effects
Examples:
- display a badge
- surface metadata
- show a registry result

### 5.2 Interaction effects
Examples:
- allow a fetch
- enable a workflow step
- accept a signal in UI logic

### 5.3 Transactional effects
Examples:
- allow transfer
- authorize submission
- accept a signed action
- commit a record change

### 5.4 Rights-affecting effects
Examples:
- deny an entitlement
- alter a formal status
- revoke access
- trigger a compliance action

The more sensitive the effect, the more bounded and evidenced the decision should be.

## 6. Decision flow

```text
1. Identify attempted effect
2. Determine acting entity and role
3. resolve claimed authority and constraints
4. inspect relevant artifacts and claims
5. apply policy to the context
6. evaluate controls against threats
7. assess evidence and verification results
8. check lifecycle state and revocation conditions
9. produce trust decision
10. allow, deny, downgrade, or route the effect
```

That sequence is intentionally plain. Fancy words are not a substitute for operational logic.

## 7. A practical formula

A compact way to think about it is:

**Effect legitimacy = bounded authority + policy fit + verified artifacts and claims + sufficient controls and evidence - unresolved threat and lifecycle risk**

This is not math. It is disciplined common sense with a cleaner suit on.

## 8. Worked mini-scenarios

### 8.1 Trust registry query
An operator exposes a signed metadata response.  
The relying system validates freshness, signature, and declared constraints.  
Policy accepts the result for informational use but not for high-risk automated gating.  
**Trust decision:** accept with bounded use.  
**Effect:** show registry result, but do not auto-approve onboarding.

### 8.2 Consumer trust signal
A marketplace fetches ERC-8004 metadata.  
Integrity checks pass, but finality evidence is weak and local policy requires stronger proof for transfer-related UI actions.  
**Trust decision:** downgrade.  
**Effect:** show a warning, suppress strong trust badge.

### 8.3 Delegated agent
A software agent attempts an action on behalf of a principal.  
The authority artifact shows scope for information retrieval only, not state mutation.  
**Trust decision:** deny.  
**Effect:** state-changing action blocked.

## 9. Design guidance

Implementations based on TSMM should:

- classify effects explicitly
- treat authority as bounded, not ambient
- preserve local policy sovereignty
- keep lifecycle and revocation in the decision loop
- avoid binary trust where warning or downgrade is more honest
- maintain traceable evidence for consequential decisions

## 10. Relationship to the rest of the model

The trust-decision model depends on the core abstractions in `docs/core-model.md` and the canonical relationships in `docs/relationship-model.md`.

Those two documents explain what the pieces are and how they fit together.  
This document explains how the machine should think when an effect is on the line.
