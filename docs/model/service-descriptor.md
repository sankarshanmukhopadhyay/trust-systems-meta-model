---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 1
---

# ServiceDescriptor

## Concept definition

A **ServiceDescriptor** is a trust-relevant capability disclosure artifact whose
visibility is policy-bound and whose authenticity may be signed. It is the structured
surface through which an agent, service, or system publishes what it is, what it can do,
and how it can be reached — under a declared disclosure policy that governs who may
see what.

The abstraction is intentionally protocol-neutral. It generalizes:

- the **Agent Card** in the A2A protocol (public and authenticated-extended variants)
- **entity statements** in OpenID Federation
- **ecosystem descriptor** constructs in TRQP
- any structured identity-and-capability disclosure artifact used to initiate trust
  establishment before an interaction begins

## Trust significance

A ServiceDescriptor is not merely an artifact. It is the governance anchor for
pre-interaction trust. Before any SkillContract is exercised, before any
InteractionContext is opened, a counterparty must be able to determine who it is
dealing with, on what terms, and with what degree of assurance.

Three trust-relevant properties make the ServiceDescriptor distinct from a generic
artifact:

1. **Disclosure policy.** The descriptor declares the visibility scope of its content:
   `public` (no authentication required), `authenticated` (extended metadata available
   after credential presentation), or `restricted` (access governed by explicit policy).
   This is a governance decision, not a transport detail.

2. **Authenticity binding.** The descriptor may carry a reference to an integrity or
   signing mechanism — a JWK thumbprint, a DID verification method, or a trust anchor
   reference — that allows counterparties to verify that the descriptor was produced by
   the declared entity. An unauthenticated ServiceDescriptor provides capability
   discovery; an authenticated one provides trust establishment.

3. **Versioning and expiry.** Descriptors are versioned and may carry an `expiresAt`
   value. A counterparty must track version and expiry as governance-relevant state,
   not merely informational metadata.

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Artifact` | ServiceDescriptor is a specialization: an artifact whose trust-significance includes disclosure policy, authenticity binding, and capability scope |
| `Entity` | A ServiceDescriptor carries an `entityRef` — it discloses properties of the entity, but is not the entity itself |
| `Capability` | A ServiceDescriptor may list or reference capabilities; `SkillContract` elaborates those capabilities into operational contracts |
| `GovernanceContext` | The disclosure policy and access controls of a ServiceDescriptor are governed by a GovernanceContext |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `entityRef` | Yes | The entity whose capabilities this descriptor discloses |
| `disclosurePolicy` | Yes | `public`, `authenticated`, or `restricted` |
| `version` | Yes | Descriptor version string |
| `providerRef` | No | The organizational or system provider |
| `endpointSet` | No | Published endpoint URIs |
| `supportedTransports` | No | Transport protocols the entity accepts |
| `authenticityBinding` | No | Signing or integrity mechanism reference |
| `expiresAt` | No | Descriptor expiry timestamp |

## Design notes

**Generalizes, does not replicate.** The ServiceDescriptor should not import
A2A-specific fields such as `capabilities` arrays, `defaultInputModes`, or JSON-RPC
method sets. Those are protocol-layer details. The abstraction captures the
trust-significant invariants: disclosure posture, authenticity, and capability scope.
Protocol-level details belong in the A2A binding.

**Authenticity is optional by design.** A `public` ServiceDescriptor with no
authenticity binding is a valid TSMM construct for open capability advertisement. Trust
decisions that require binding to a verified entity must use an `authenticated` or
`restricted` descriptor with a populated `authenticityBinding`.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Extension index: `docs/extensions/index.md`
