---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.19.0
tier: 1
---

# TSMM Operational Profile

## 1. Purpose

The Operational Profile defines a TSMM implementation that can support routine trust-relevant decision flows in a live system.

## 2. Required elements

| Requirement | Description |
|---|---|
| Minimal Profile baseline | All Minimal Profile requirements |
| Governance context | Explicit context for policy interpretation |
| Profile and requirements | Defined requirement bundle or baseline |
| Lifecycle tracking | Suspension, revocation, or expiry handling |
| Verification path | One or more verification processes |
| Threat awareness | At least a documented threat set or failure taxonomy |
| Publication surface | A discoverable publication pattern for trust-relevant system state, profile references, or evaluation outputs |

## 3. Suitable use cases

- trust registry operations
- credential verification systems
- delegated action controls
- consumer trust-signal handling
- publication-oriented agent and service profiles that need downstream assurance review

## 4. Operational expectations

An implementation claiming the Operational Profile should be able to show, in machine-readable or replayable form, at least the following:

- which operator or publisher is accountable for the described system surface
- which policy or profile bundle governs the published trust posture
- where evidence and assessment references live
- how revocation, expiry, or suspension state is surfaced to downstream consumers

## 5. Outcome

An Operational Profile implementation can do real work without pretending runtime legitimacy is solved by vibes and a dashboard.
