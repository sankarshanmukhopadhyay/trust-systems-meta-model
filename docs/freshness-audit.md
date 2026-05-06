---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 2
---

# TSMM Documentation Freshness Audit

## Audit date

2026-03-19

## Baseline findings before v0.3.0

### P1 issues

- no docs landing page for GitHub Pages
- no explicit documentation governance document
- no glossary despite domain-specific terminology
- no security reporting guidance
- no freshness metadata on most documents
- no release artifact file inside the repo
- missing DCAS crosswalk even though adjacent repos clearly implied additional abstractions

### P2 issues

- schema and examples did not model profile, requirement, governance context, or assessment explicitly
- crosswalk set was incomplete for the uploaded repo set

## Remediation in v0.3.0

- added `docs/index.md` and `_config.yml`
- added `docs/documentation-governance.md`
- added `docs/glossary.md`
- added `SECURITY.md`
- added document frontmatter with owner, version, review date, and tier
- added `releases/v0.3.0.md` and `VERSION`
- added `docs/crosswalks/dcas-crosswalk.md`
- expanded core model, schema, and examples

## Release gate outcome

- no P0 documentation defects identified
- internal path references reviewed and corrected
- JSON examples validated against the updated schema

## v0.5.0 additions

The release introduced new model, conformance, evaluation, security, and pattern documents. Freshness checks should confirm that these remain consistent with the schema, examples, release notes, and README navigation.

## v0.6.0 additions

The release added implementer-readiness artifacts and extended the multi-agent governance model. New documents include the conformance self-assessment checklist, the getting-started implementer guide, the multi-agent coordination pattern, the multi-agent extension schema and example, the OpenID Federation crosswalk, and the schema coverage validation script. All new documents carry current version frontmatter. Existing documents were updated to current version metadata. Release notes check confirmed no broken internal links introduced.

## v0.8.0 additions

The release deepened the effect-centered evaluation logic and extension framing. Freshness checks should confirm that those conceptual additions remain aligned with later conformance, registry, and graph artifacts.

## v0.9.0 additions

The release added the executable graph layer, graph validator, and reusable profile instances. Freshness checks should confirm that the graph schema, examples, README navigation, and documentation site continue to describe the same allowed topology shape.

## v0.10.0 additions

The release introduced bindings, the registry format, and the graph renderer. Freshness checks should confirm that all published bindings remain machine-readable, all registry examples validate, and all binding and registry documentation paths remain accurate.

## v0.11.0 additions

The release closes the binding catalog gap for DCAS and Verifiable Trust Communities, adds an agentic conformance profile, extends registry indexing to include agentic instances, and enhances the graph renderer with clustering and profile annotation. Freshness checks should confirm that the README, docs home, glossary, checklist, implementer guide, and registry example all reference the new artifacts consistently.

## v0.12.0 additions

The release adds typed agent operating posture and attention-governance concepts to the agentic extension. Freshness checks should confirm that the schema, worked example, README navigation, docs home, roadmap, and crosswalk set all reference `agentClass`, `controlMode`, and `attentionPolicies` consistently.

## v0.13.0 additions

The release adds the Agent Interaction Extension with seven new trust-semantic abstractions for agent-to-agent interaction. New Tier 1 documents: `docs/model/service-descriptor.md`, `docs/model/skill-contract.md`, `docs/model/interaction-context.md`, `docs/model/authorization-checkpoint.md`, `docs/model/extension-contract.md`, `docs/model/opacity-boundary.md`, `docs/model/peer-trust-relation.md`. New schema: `schemas/tsmm-agent-interaction-extension.schema.json`. New example: `examples/agent-interaction-extension-instance.json`. Freshness checks should confirm that all seven model documents, the schema, the example, the glossary additions, the conformance checklist Agent Interaction Extension tier, `docs/extensions/index.md`, `README.md` navigation, and `docs/index.md` all reference the same seven abstraction names and schema properties consistently. The v0.14.0 A2A binding will extend this surface — alignment checks between the v0.13.0 extension documents and the binding draft should be completed before that release.

## v0.14.0 additions

The release completes the Agent Interaction Extension with three deferred abstractions and delivers the A2A binding. New Tier 1 documents: `docs/model/interaction-task.md`, `docs/model/content-provenance-policy.md`, `docs/model/observability-mode.md`. New binding documents: `docs/bindings/a2a-binding.md`, `docs/crosswalks/a2a-crosswalk.md`. Machine-readable binding: `bindings/a2a/tsmm-a2a-binding.json`. Extended example: `examples/agent-interaction-a2a-binding-instance.json`. Freshness checks should confirm that all ten Agent Interaction Extension model documents, the schema, both examples, the glossary (ten terms total), the conformance checklist (AI-1 through AI-21), the bindings index, and the A2A binding and crosswalk are mutually consistent. The A2A binding notes that it covers the protocol as of March 2026 and should be refreshed if the A2A specification changes materially.

## v0.19.0 additions

The release operationalizes runtime assurance and documentation integrity. New machine-readable artifacts include `schemas/tsmm-runtime-governance.schema.json`, `schemas/tsmm-decision-receipt.schema.json`, `examples/runtime-governance-boundary-instance.json`, `examples/decision-receipt-runtime-example.json`, and `examples/systems/revocation-propagation-system.json`. New documentation includes `docs/model/runtime-governance-envelope.md`, `docs/model/decision-receipt.md`, `docs/conformance/runtime-governance-test-profile.md`, `docs/getting-started/implementation-paths.md`, and `docs/examples/runtime-governance-walkthrough.md`.

Freshness review outcome for v0.19.0:

- repository `VERSION` updated to `v0.19.0`
- markdown frontmatter refreshed to `last_reviewed: 2026-05-05`
- stale `applicable_version: v0.16.0` and `v0.17.0` markers normalized to `v0.19.0`
- README release badge and current-version statement updated
- docs index updated with runtime governance entry points
- conformance profile set updated with runtime governance obligations
- validation scripts extended to cover the new runtime governance and decision receipt artifacts

Release gate outcome:

- no stale release badge references to `v0.17.0` remain in README
- no markdown frontmatter retains `applicable_version: v0.16.0`
- new schemas are covered by examples and validation vectors
- runtime assurance artifacts are linked from documentation navigation

## v0.20.0 harmonization review

Freshness review outcome for v0.20.0:

- repository `VERSION` updated to `v0.20.0`;
- TSMM schema `$id` values moved away from placeholder `example.org` identifiers to release-pinned repository URLs;
- Trust Infrastructure Schemas alignment docs, binding, constraints, crosswalks, and cross-repo examples added;
- assurance terminology clarified so TSMM profile posture is not conflated with TIS AL1-AL4 assurance rigor;
- documentation index and binding index refreshed for GitHub Pages navigation.
