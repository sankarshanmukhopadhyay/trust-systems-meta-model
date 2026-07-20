---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 0
---


# Capability Negotiation Model

Capability negotiation separates what a system advertises from what a requester is allowed to use. This is the key governance move in agentic systems: a published capability is not an authorization decision.

TSMM v0.19.0 generalizes the A2A Skill and extension declaration pattern into a reusable capability-governance contract. The model applies to agents, registries, verifiers, orchestration layers, and any service that exposes policy-bound actions.

## Capability layers

| Layer | Meaning | Governance question |
| --- | --- | --- |
| Advertised capability | Provider claims it can do something | Is the claim visible and attributable? |
| Discoverable capability | Requester may see the capability | Is disclosure authorized? |
| Negotiated capability | Parties agree on modes and extensions | Are input/output modes and extensions compatible? |
| Authorized capability | Policy permits use in context | Does the requester have authority for this effect? |
| Executed capability | Capability is invoked | Was execution bounded by the negotiated contract? |
| Evidenced capability | Evidence exists for audit/replay | Can the decision and output be inspected? |

## Extension negotiation

A2A demonstrates an important pattern: extensions are identified by URI, can be required or optional, and require explicit client opt-in. TSMM generalizes this into `requestedExtensions`, `acceptedExtensions`, `rejectedExtensions`, and `requiredExtensionsMissing`.

## Normative requirements

- Capability negotiation **MUST** identify requester, provider, skill or capability reference, policy scope, and decision reference.
- Required extensions that are missing **MUST** result in `rejected` or `review-required`.
- Accepted modes **MUST** be a subset of requested modes or be explained through a constraint.
- Negotiation outcomes **SHOULD** produce evidence references suitable for audit.
- Capability acceptance **MUST NOT** be interpreted as permission to perform downstream effects unless an authorization decision also exists.

## Schema and example

- Schema: `schemas/tsmm-capability-negotiation.schema.json`
- Example: `examples/capability-negotiation-instance.json`
- Valid vector: `validation/test_vectors/valid/capability-negotiation-valid.json`
- Invalid vector: `validation/test_vectors/invalid/capability-negotiation-required-extension-missing.json`
