---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
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
