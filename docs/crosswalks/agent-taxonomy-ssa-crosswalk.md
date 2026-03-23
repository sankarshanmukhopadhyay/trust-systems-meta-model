---
owner: maintainers
last_reviewed: 2026-03-19
applicable_version: v0.14.0
tier: 1
---

# Crosswalk: Taxonomy for Agent Systems and Self-Sovereign Attention to TSMM

## Purpose

This crosswalk records how two external conceptual inputs map into TSMM v0.12.0:

- **Taxonomy for Agent Systems (T4AS)**
- **A Stack for Self-Sovereign Attention (SSA)**

The aim is not to import those documents wholesale. The aim is to identify where they sharpen TSMM’s agentic extension and where they expose modeling gaps worth closing.

## Main correspondences

| External concept | TSMM interpretation | v0.12.0 response |
|---|---|---|
| Agent role persistence | delegated actor identity with policy-bearing context | clarified through agent classification guidance |
| Bot / robot as acting totality | bounded actor plus capability and execution context | kept in extension framing rather than core |
| Workspace as execution boundary | execution context plus resource and policy boundary | already aligned; emphasized in docs |
| Digital twin | identity-proxy agent acting for a principal | new `agentClass` support |
| Virtual assistant | execution agent under bounded delegation | new `agentClass` support |
| PAM side-car | predictive agent in a non-interruptive control posture | new `controlMode` and `agentClass` support |
| Unified feed / attention routing | policy-governed signal admission and prioritization | new attention-governance framing and `attentionPolicies` object |
| dynamic unavailability / latest reasonable moment | execution-context-aware routing constraints | modeled as policy plus execution context |

## Interpretation

The T4AS document makes the strongest contribution in how it separates kinds of acting components and insists on architectural clarity between generation, orchestration, and execution boundaries. The SSA stack makes the strongest contribution in showing that identity proxying, predictive side-cars, and attention gateways are not abstract edge cases. They are practical design patterns that need governance.

## What TSMM takes from this

v0.12.0 does three things in response:

1. adds a machine-readable way to classify agent operating posture
2. adds an explicit control-mode field for agent behavior posture
3. adds a machine-readable attention-policy object so signal admission and interruption control can be documented as governed action paths

## Source links

- Stack for Self-Sovereign Attestation: `https://docs.google.com/document/d/1bEIZzmv42eDNypMGBtPEceo9yudvMowIHjTuwqo5pVo/`
- Taxonomy for Agent Systems: `https://docs.google.com/document/d/1a-Rn9V4UgtXs9EYniTAyjvG93QfzzenXfUNK3nW_Sss/`


These sources are referenced for conceptual alignment only and are not normative dependencies of TSMM.
