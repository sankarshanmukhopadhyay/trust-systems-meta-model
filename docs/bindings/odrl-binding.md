---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 1
title: TSMM to ODRL Binding
permalink: /bindings/odrl-binding.html
parent: Bindings
grand_parent: Documentation
---

# TSMM to ODRL Binding

## Purpose

This binding explains how **ODRL** can be used inside the TSMM stack.

ODRL is a machine-readable policy expression model for permissions, prohibitions, duties, parties, assets, actions, constraints, profiles, inheritance, and conflict handling. That makes it useful for one important part of trust infrastructure: **policy expression**. It does **not** make ODRL the whole trust model.

TSMM sits at the wider semantic layer. It still needs to represent who is accountable, what authority exists, how evidence travels, how assessments are produced, how revocation changes reliance, and what downstream effect a trust decision should trigger. ODRL helps with the policy object model inside that larger system.

## Binding posture

- **TSMM** supplies the semantic spine for trust systems.
- **ODRL** supplies a standards-based policy expression surface.
- **trust-infrastructure-schemas** can carry ODRL policy artifacts or references as canonical machine-readable contracts.
- **ANAB** can optionally reference ODRL-compatible policy artifacts where usage, disclosure, or notice conditions matter.

## Core mappings

| ODRL concept | TSMM concept | Binding strength | Why it matters |
| --- | --- | --- | --- |
| ODRL Policy | Policy | exact | Gives TSMM a portable machine-readable policy object. |
| ODRL Permission | Policy | approximate | Expresses allowed actions that feed later trust decisions. |
| ODRL Prohibition | Policy | approximate | Expresses disallowed actions and bounded effects. |
| ODRL Duty | Policy | approximate | Captures required actions or pre-conditions attached to policy evaluation. |
| ODRL Party / assigner / assignee | Subject | approximate | Preserves who issues or receives policy statements without collapsing TSMM role semantics. |
| ODRL Asset / target | composite trust object | composite | The governed object may be a service, credential, registry object, publication, or record. |
| ODRL Constraint | Policy | exact | Refines when a rule applies. |
| ODRL Profile | AssuranceProfile | approximate | Lets a bounded ecosystem publish extensions and interpretation constraints. |

## What this binding does not do

This binding does **not** claim that ODRL is sufficient for:

- runtime authorization and delegated authority chains
- assurance level semantics
- evidence bundle structure
- evaluator logic
- revocation propagation
- governance legitimacy or contestability

Those concerns remain TSMM-native or are handled by adjacent repos in the stack.

## Implementation pattern

A practical three-repo composition looks like this:

1. **TSMM** models the policy-bearing system and the surrounding governance, assurance, evidence, and effect semantics.
2. **trust-infrastructure-schemas** carries the canonical machine-readable ODRL policy reference or policy artifact contract.
3. **ANAB** optionally points to ODRL-compatible policy artifacts for disclosure, usage, notice, or operator-imposed restrictions without making ODRL a conformance precondition.

That keeps the architecture clean:

- ODRL expresses policy.
- TSMM explains the wider trust system.
- trust-infrastructure-schemas carries the policy artifacts.
- ANAB stays focused on controls, evidence, and assurance interpretation.

## Machine-readable artifacts

- Binding: `bindings/odrl/tsmm-odrl-binding.json`
- Constraint set: `bindings/odrl/constraints.json`
