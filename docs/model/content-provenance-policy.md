---
owner: maintainers
last_reviewed: 2026-04-08
applicable_version: v0.16.0
tier: 1
---

# ContentProvenancePolicy

## Concept definition

A **ContentProvenancePolicy** is a governance policy specifying what must be known and
verified about interaction payload content before it can be acted upon, stored, or
forwarded. It is defined per content modality — text, structured data, file references,
audio/video, embedded UI, or other — because trust obligations differ by modality.

ContentProvenancePolicy is explicitly **not** a wire-level content type model. TSMM
does not model MIME types, JSON schemas, or encoding formats. It models the governance
envelope: provenance requirements, sanitization obligations, redaction rules, and
evidence capture obligations that apply to content of a given modality when exchanged
between agents.

## Trust significance

Content exchanged between agents carries its own trust surface, independent of the
agents' identity and authorization. An agent that is authorized to call a skill may
still present content that:

- cannot be attributed to a known source (provenance gap)
- contains injected or malformed data that must be sanitized (sanitization risk)
- contains sensitive fields that must not be logged or forwarded (redaction obligation)
- must leave an evidence trail for auditability (evidence capture obligation)

ContentProvenancePolicy makes these obligations explicit at the governance layer, so
they can be evaluated as part of the trust decision chain rather than left to ad hoc
implementation choices. The four key obligations by modality:

| Modality | Primary risk | Governance obligation |
|---|---|---|
| `text` | Prompt injection, unattributed claims | Provenance attribution, sanitization |
| `structured-data` | Schema manipulation, injection | Schema validation, sanitization, provenance |
| `file-reference` | SSRF, path traversal, opaque payload | Reference scope restriction, sanitization, hash capture |
| `audio-video` | Deepfake, unverifiable content | Provenance chain, redaction review |
| `embedded-ui` | Clickjacking, script injection | Strict sanitization, execution scope limits |

## Relationship to existing TSMM abstractions

| TSMM abstraction | Relationship |
|---|---|
| `Policy` | ContentProvenancePolicy is a specialised policy. It governs the evaluation of payload content rather than the evaluation of an action or authority. It may be referenced from a governing Policy object. |
| `Evidence` | `evidenceCaptureObligation` defines what evidence must be produced when content is processed. The captured evidence becomes part of the trust decision audit trail. |
| `Control` | Sanitization and redaction rules are controls in the TSMM sense: safeguards that reduce defined risks. |
| `SkillContract` | A SkillContract governs what a capability may do; ContentProvenancePolicy governs what the content exchanged in exercising that capability must satisfy. |
| `OpacityBoundary` | OpacityBoundary constrains what can be known about an agent's internals. ContentProvenancePolicy constrains what must be known about content exchanged between agents. The two are complementary. |

## Key properties

| Property | Required | Description |
|---|---|---|
| `id` | Yes | Unique identifier |
| `applicableModalities` | Yes | Modalities governed: `text`, `structured-data`, `file-reference`, `audio-video`, `embedded-ui`, `other` |
| `provenanceRequirements` | Yes | What must be known about content origin before use |
| `sanitizationRequired` | Yes | Whether content must be sanitized before processing or forwarding |
| `redactionRules` | No | Rules for redacting sensitive content before storage or evidence capture |
| `evidenceCaptureObligation` | Yes | Minimum evidence record required when content of this modality is processed |

## Design notes

**Modality-specificity is the design.** A single ContentProvenancePolicy covers one
or more modalities. Implementations that apply different trust obligations to different
modalities should define separate policy objects per modality group. This keeps
governance obligations traceable to the specific content type they govern.

**Provenance requirement is not authentication.** Requiring that content be attributable
to a declared source is a provenance check. It is distinct from the authentication of
the agent that sent it. An authenticated agent can send unauthenticated content; the
ContentProvenancePolicy governs the content independently of the agent's identity.

**Evidence capture is not optional.** The `evidenceCaptureObligation` is required
precisely because it is the governance record that content was received, evaluated, and
processed. Implementations that skip evidence capture for "low-risk" content modalities
create selective audit gaps that erode the integrity of the full evidence chain.

## Related artifacts

- Schema: `schemas/tsmm-agent-interaction-extension.schema.json`
- Example: `examples/agent-interaction-a2a-binding-instance.json`
- A2A binding: `docs/bindings/a2a-binding.md`
- Extension index: `docs/extensions/index.md`
