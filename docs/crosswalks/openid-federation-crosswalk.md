---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# TSMM Crosswalk: OpenID Federation

## Purpose

This document maps **OpenID Federation 1.0** to the Trust Systems Meta Model (TSMM).

OpenID Federation defines a mechanism for expressing, publishing, and resolving trust relationships between entities in an open federation, using signed entity statements, trust chains, trust marks, and trust anchors. It is widely deployed in academic identity federations, national eID ecosystems, and open banking contexts.

## Center of gravity

Within TSMM terms, OpenID Federation is primarily about:

- expressing hierarchical and delegated trust relationships between independently operated parties
- publishing machine-readable metadata subject to policy constraints
- resolving trust chains from leaf entities up to a trust anchor
- governing which entities are allowed to make what claims under which constraints

Its center of gravity is **chain-resolved authority under federated governance**.

## Crosswalk table

| TSMM concept | OpenID Federation instantiation |
|---|---|
| **Governance Context** | federation operator policies, trust anchor operating rules, and jurisdiction-specific metadata policy constraints |
| **Profile** | federation-specific metadata policy profiles applied by trust anchors or intermediate operators |
| **Requirement** | metadata policy claims (`policy` object in entity statements) that constrain permitted values for descendant entities |
| **Entity** | OpenID Connect entity (OP, RP, AS, federation operator, intermediate, trust anchor) identified by `iss` |
| **Role** | entity type expressed in `metadata` claim (`openid_provider`, `openid_relying_party`, `federation_entity`, etc.) |
| **Authority** | trust chain from leaf entity to trust anchor; authority is established by the chain resolving without error under the applicable metadata policy |
| **Artifact** | entity statement (self-signed or superior-signed JWT), trust mark JWT, resolved metadata document |
| **Claim** | individual claims within entity statements; metadata policy claim modifiers (`value`, `subset_of`, `superset_of`, `essential`) |
| **Policy** | metadata policy object expressed by superiors in the trust chain; also operator-level policy governing which intermediates may issue subordinate statements |
| **Control** | signing key requirements, `exp` and `iat` constraints, subordinate statement issuance controls, trust mark validity checks |
| **Threat** | compromised signing key, expired entity statement, unauthorized intermediate, trust mark forgery, chain resolution manipulation |
| **Evidence** | resolved entity statement chain, trust mark validation result, signed subordinate statement from a recognized federation operator |
| **Assessment** | trust chain resolution process; metadata policy merge and validation; trust mark claim evaluation |
| **Verification** | chain resolution to a known trust anchor; signature verification at each step; metadata policy constraint checking |
| **Level Framework** | trust mark schemes with tiered assurance levels (e.g., REFEDS assurance framework references embedded in entity statements) |
| **Trust Decision** | outcome of successful or failed chain resolution and metadata policy merge for a specific (RP, OP) pair |
| **Effect** | allow federation-scoped authentication or authorization; deny or downgrade if chain does not resolve; route to manual review if constraints are ambiguous |
| **Lifecycle Event** | entity statement issuance, key rotation, subordinate statement revocation, trust mark issuance or revocation, trust anchor update, federation decommissioning |

## Trust chain as chained authority

OpenID Federation's trust chain is the clearest real-world instantiation of TSMM's chained authority model. Each step in the chain corresponds to a bounded delegation:

- The **trust anchor** holds root authority within the federation.
- Each **intermediate** holds delegated authority to issue subordinate statements for entities it recognizes.
- The **leaf entity** holds authority bounded by the cumulative metadata policy applied through the chain.

A trust chain resolution failure is a TSMM trust decision with a `deny` or `downgrade` outcome.

## Metadata policy as distributed policy

OpenID Federation's metadata policy mechanism distributes policy evaluation across the chain. Superior entities express constraints as metadata policy modifiers. The resolved metadata document is the post-evaluation policy output. This maps to TSMM's model of policy governing effect production: the resolved metadata defines what the leaf entity is allowed to claim, and therefore what effects downstream relying parties may permit.

## Trust marks as verifiable claims with level framework binding

Trust marks in OpenID Federation are signed assertions from a recognized trust mark issuer, binding an entity to a defined assurance claim. Within TSMM, a trust mark is an **Artifact** carrying one or more **Claims**, issued under delegated **Authority**, evaluated against a **Level Framework** that the trust mark scheme defines.

## Practical takeaway

Projects implementing or evaluating OpenID Federation deployments can use TSMM to ask the following questions with more structural clarity:

- What authority does each intermediate hold, and is that authority bounded and revocable?
- What metadata policy constraints apply at each tier, and are they sufficient to govern the effects relying parties may produce?
- Is the trust chain resolution process a repeatable, auditable verification activity with a defined method and result?
- Are lifecycle events (key rotation, revocation, trust anchor updates) reflected in the lifecycle model and handled before they affect downstream relying parties?
- What trust decisions are possible beyond allow? Can a relying party downgrade, warn, or route based on chain resolution results that are technically valid but contextually insufficient?
