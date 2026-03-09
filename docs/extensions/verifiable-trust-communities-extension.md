---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Verifiable Trust Communities Extension

## 1. Purpose

This extension adapts TSMM to **Verifiable Trust Communities (VTCs)**.

A VTC is not merely a list of participants. It is a governed trust environment with rules for membership, standing, recognition, evidence, sanctions, and effects.

## 2. Why this is an extension

Community formation, membership semantics, federation, and sanctions are critical for VTCs but are not universal across all trust systems. They should therefore remain outside the TSMM core unless repeated cross-domain usage proves they are foundational.

## 3. Extension abstractions

### 3.1 Community
A **Community** is a bounded trust domain with a defined purpose, governance model, trust posture, and participation rules.

### 3.2 Membership
A **Membership** links an entity to a community under explicit admission criteria, obligations, validity conditions, and status.

### 3.3 Standing
A **Standing** expresses whether a member is in good standing, probationary standing, suspended standing, revoked standing, or another defined status.

### 3.4 Charter
A **Charter** captures the governing rules, decision rights, review cadence, dispute process, and change control model of the community.

### 3.5 Recognition
A **Recognition** expresses whether one community, participant, or verifier accepts another community's assertions, membership states, or evidence under stated conditions.

### 3.6 Boundary Rule
A **Boundary Rule** defines the conditions under which external members, claims, or communities are admitted, recognized, bridged, or rejected.

### 3.7 Sanction
A **Sanction** is a policy-governed adverse state change such as warning, probation, scoped suspension, full suspension, or exclusion.

### 3.8 Remediation Path
A **Remediation Path** defines how a participant can restore standing or recover membership after a sanction or assessment failure.

## 4. Relationship to TSMM core

- A **Community** operates within a TSMM **Governance Context** and may publish one or more **Profiles**.
- A **Membership** results from **Assessment**, **Verification**, and **Trust Decision**.
- **Standing** influences which **Effects** are permitted for a member.
- A **Recognition** acts as a policy-governed bridge between communities or trust domains.
- A **Sanction** and **Remediation Path** are modeled through lifecycle events and decision-linked effects.

## 5. Design guidance

### 5.1 Make membership first-class
Do not collapse membership into a loose role label. Membership has basis, scope, duration, obligations, and review cadence.

### 5.2 Separate community assertion from local trust decision
A community may assert that a member is in good standing. A relying party may still apply additional policy before allowing a local effect.

### 5.3 Model boundaries explicitly
Inter-community trust is where the weirdness starts. Recognition, federation, and boundary rules should be explicit rather than implied.

### 5.4 Treat sanctions as operational states
Trust communities do not only admit or reject. They warn, suspend, narrow scope, require remediation, and restore standing under conditions.

## 6. Example evaluation flow

1. Applicant submits membership evidence.
2. Community profile defines admission requirements.
3. Assessment and verification evaluate the submission.
4. Trust decision admits, rejects, or requests remediation.
5. Membership is issued with a standing state.
6. Boundary rules govern whether external communities recognize that state.

## 7. Non-goals

This extension does not prescribe one governance philosophy, one charter model, or one federation method. It provides a portable structure for **verifiable community participation under rules and evidence**.
