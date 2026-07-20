---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# PeerTrustRelation

## Concept definition

A **PeerTrustRelation** models a trust relationship between lateral agents operating as
peers with no pre-existing hierarchical relationship. It captures how trust is
established and maintained between parties where neither holds authority over the other,
neither can be treated as a principal that has delegated rights downward, and both are
operating as independent agents in the same interaction.

PeerTrustRelation is a parallel trust relation type to the existing delegation model.
The delegation model is hierarchical: authority flows downward from principal to
sub-agent. PeerTrustRelation addresses a structurally different scenario: two agents
meeting as lateral peers, neither subordinate to the other, both with their own
governance envelopes.

## Trust significance

TSMM's existing `Delegation` abstraction is well-suited for principal-agent
relationships. What it does not model is the case where trust must be established
between parties at the same level: two buyer and supplier agents exchanging services,
two registry operators querying each other, or two specialized agents collaborating
on a task that neither can complete alone.

In all of these cases the question is not "has the principal delegated authority?" — it
is "on what basis do these peers extend trust to each other, and within what scope?"

PeerTrustRelation answers this with four trust basis types:

| Trust basis | Meaning |
|---|---|
| `credential-exchange` | Each party has verified the other's credential (DID, certificate, signed ServiceDescriptor) |
| `capability-negotiation` | Trust is established through ServiceDescriptor and SkillContract exchange at session initiation |
| `policy-acceptance` | Both parties have agreed to a shared policy or framework that governs the interaction |
| `third-party-introduction` | A trusted third party (trust registry, federation authority) has introduced or endorsed both parties |

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Delegation` | PeerTrustRelation is structurally parallel, not hierarchical. Both are trust relation types. Delegation is vertical (principal → sub-agent). PeerTrustRelation is lateral (peer ↔ peer). They coexist in the model. |
| `Authority` | A PeerTrustRelation is not an authority grant from one party to another. The `trustScope` describes what is trusted, but neither party holds authority over the other. |
| `ServiceDescriptor` | `capability-negotiation` trust basis relies on ServiceDescriptor and SkillContract exchange as the basis for peer trust establishment. |
| `GovernanceContext` | `governingPolicyRef` links the relation to a governing policy within a governance context. |
| `InteractionContext` | Peer trust relations are referenced from within an InteractionContext to establish the trust basis for session participants. |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `partyARefs` | Yes | First lateral party or parties (one or more entities) |
| `partyBRefs` | Yes | Second lateral party or parties |
| `trustBasis` | Yes | `credential-exchange`, `capability-negotiation`, `policy-acceptance`, or `third-party-introduction` |
| `trustScope` | Yes | Bounded description of what is trusted between these peers |
| `establishedAt` | Yes | When this peer trust relation was established |
| `conditionsForWithdrawal` | No | Conditions under which the relation may be revoked or suspended |
| `governingPolicyRef` | No | Policy governing the terms of this trust relation |

## Design notes

**Trust scope is bounded.** A PeerTrustRelation has an explicit `trustScope`. Trust
between two procurement agents does not generalize to trust between those agents for
identity-proxy operations, financial authorization outside the procurement domain, or
any other context. TSMM models this explicitly to prevent scope drift in governance
records.

**Neither party holds authority over the other.** This is the defining characteristic.
If one party holds governance authority over the other — if one can revoke, suspend, or
override the other — the relationship is not a peer relationship and should be modeled
with `Delegation` and `Authority` objects instead.

**Third-party introduction.** When `trustBasis` is `third-party-introduction`, the
`governingPolicyRef` should reference the policy or registry authority that endorsed
the introduction. This connects the peer trust relation to the broader governance
topology.

**Revocation is bilateral.** Either party may withdraw from a PeerTrustRelation.
`conditionsForWithdrawal` should reflect conditions that either party may invoke, not
only conditions imposed by one party on the other.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-extension-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md` *(v0.14.0)*
- Delegated agent pattern: `docs/patterns/delegated-agent-pattern.md`
- Extension index: `docs/extensions/index.md`
