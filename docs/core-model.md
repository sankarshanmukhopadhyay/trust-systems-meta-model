# TSMM Core Model

## 1. Purpose

The Trust Systems Meta Model (TSMM) provides an abstract model for how trust systems are structured and how they make operational decisions.

The model is built around a practical question:

> Under what bounded authority, policy, evidence, and verification conditions should a system allow a trust-relevant effect to occur?

TSMM is therefore not primarily identity-centered. It is **effect-centered**.

Identity matters. Roles matter. Authority matters. But the decisive unit of governance is the **effect** produced in context.

## 2. Core modeling thesis

A trust system is not only a mechanism for storing identifiers or publishing metadata.  
A trust system is a mechanism for:

1. representing participants and artifacts
2. expressing claims and constraints
3. applying policy and controls
4. mitigating threats
5. gathering evidence
6. verifying posture or validity
7. producing a trust decision
8. permitting, denying, degrading, or routing an effect

That chain is the operational heart of TSMM.

## 3. Primary abstractions

### 3.1 Entity
An **Entity** is any actor, component, or participant that can exist within a trust system.

Examples include:

- person
- organization
- software agent
- wallet
- registry operator
- verifier
- auditor
- indexer

An entity is a participant, not yet a permission.

### 3.2 Role
A **Role** is a context-specific capacity in which an entity acts.

Examples include:

- issuer
- subject
- operator
- verifier
- consumer
- delegate
- auditor
- trust anchor maintainer

Roles allow one entity to participate in multiple ways without collapsing everything into a single static identity bucket.

### 3.3 Authority
**Authority** is a bounded right, permission, mandate, or recognized competence attached to a role.

Typical attributes include:

- scope
- source
- time bounds
- conditions
- obligations
- delegation status
- revocation conditions

Authority is not equivalent to identity. This is one of the central non-negotiables of the model.

### 3.4 Artifact
An **Artifact** is any structured object that carries trust-relevant information.

Examples include:

- credential
- trust-list entry
- registry record
- signed response
- metadata document
- policy file
- conformance report
- attestation

Artifacts are the payload-bearing objects of the trust system.

### 3.5 Claim
A **Claim** is a proposition asserted by or about an entity, artifact, system, or state.

Examples include:

- this registry supports a defined assurance posture
- this agent is controlled by a specific principal
- this metadata is fresh within an accepted window
- this artifact conforms to a required schema

A claim is not automatically true. It is a statement subject to evaluation.

### 3.6 Policy
A **Policy** is a set of evaluation rules that governs interpretation, acceptance, rejection, downgrade, routing, or escalation.

Policy may be machine-readable, human-readable, or both.

Examples include:

- acceptance thresholds
- trust-context allowlists
- safe-fetch restrictions
- freshness windows
- fail-open or fail-closed behavior
- validator acceptance rules
- mandatory human-review triggers

Policy turns raw claims into governed decisions.

### 3.7 Control
A **Control** is a safeguard that reduces a defined risk or constrains an unsafe condition.

Examples include:

- signature verification
- rate limiting
- context allowlisting
- safe dereferencing sandbox
- anti-enumeration controls
- deterministic finality checks
- sender-constrained token requirements

Controls are the practical levers by which policy becomes enforceable.

### 3.8 Threat
A **Threat** is a modeled abuse case, harm scenario, failure mode, or adverse condition.

Examples include:

- spoofed metadata
- stale signal consumption
- mandate escalation
- enumeration attacks
- unsafe dereferencing
- Sybil-amplified reputation distortion
- bridge inconsistency

Threat modeling is a first-class input to TSMM, not a decorative appendix.

### 3.9 Evidence
**Evidence** is material used to substantiate a claim, control implementation, verification result, or level assertion.

Examples include:

- signed logs
- config snapshots
- test output
- CI results
- audit reports
- traceability records
- remediation records

In a trust system, unsupported confidence is just expensive optimism.

### 3.10 Verification
**Verification** is the process of evaluating whether claims, artifacts, controls, policies, or evidence satisfy defined conditions.

Examples include:

- schema validation
- signature verification
- conformance testing
- policy evaluation
- auditor review
- equivalence testing

Verification transforms assertions into assessable posture.

### 3.11 Level Framework
A **Level Framework** is a tiered model expressing progressively different rigor, trust posture, or implementation maturity.

Examples include:

- assurance levels
- conformance levels
- policy maturity bands
- risk-tier classes

TSMM treats level systems abstractly. It does not assume that all level schemes mean the same thing.

### 3.12 Trust Decision
A **Trust Decision** is the result of applying policy and verification to trust-relevant material.

Example outcomes include:

- accept
- reject
- accept with warning
- downgrade confidence
- quarantine
- escalate to human review
- require stronger evidence

Trust decisions are contextual, not universal.

### 3.13 Effect
An **Effect** is the operational consequence produced or blocked by a trust decision.

Examples include:

- show a trust cue
- allow a transaction
- deny an action
- expose a registry result
- block a fetch
- trigger manual review
- update a state record

Effects are where governance stops being philosophy and starts touching the machinery.

### 3.14 Lifecycle Event
A **Lifecycle Event** is a state-changing occurrence relevant to trust posture or authority.

Examples include:

- issuance
- registration
- delegation
- revocation
- expiry
- reassessment
- remediation closure
- policy change
- control rotation

Trust systems are dynamic. TSMM treats change as native rather than accidental.

## 4. Operating thesis in one line

TSMM can be compressed into this line:

> **An entity acting in a role exercises bounded authority through artifacts and claims that are evaluated under policy, controls, threats, evidence, and verification to determine whether an effect should occur.**

That sentence is a mouthful, but at least it earns its calories.

## 5. Why the model is effect-centered

Many digital systems still behave as though identity is enough. It is not.

The decisive question in a trust system is usually not:

- who are you?

The decisive question is:

- who is acting
- in what role
- under what authority
- with what evidence
- under what policy
- producing what effect
- and with what recourse if the effect is unsafe

TSMM therefore treats **effect** as the center of the model and **identity** as one supporting input among several.

## 6. Adjacent distinctions TSMM keeps separate

TSMM deliberately does not collapse the following into a single concept:

- **assurance** and **reputation**
- **conformance** and **authorization**
- **identity** and **authority**
- **claim** and **truth**
- **verification** and **effect**
- **operator posture** and **consumer interpretation**

That separation prevents a lot of conceptual soup.

## 7. Relationship entry point

For the formal relationship view, see `docs/relationship-model.md`.

For the trust-decision logic anchored around runtime effect, see `docs/effect-centered-trust-decision-model.md`.
