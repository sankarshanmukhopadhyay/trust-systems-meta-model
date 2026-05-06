---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.20.0
tier: 1
---

# TIS Evidence Bundle Crosswalk

TSMM explains the semantic role of evidence. TIS packages evidence for validation, publication, audit, and replay.

| TSMM evidence idea | TIS artifact | Rule |
| --- | --- | --- |
| EvidenceArtifact | artifact reference | Preserve URI, media type, hash, freshness, role, and schema URI where available. |
| EvidenceBundle | evidence bundle manifest | Package the evidence set used for evaluation. |
| Assessment evidence | evaluation envelope evidence | Preserve evaluator output and checked controls. |
| Runtime evidence | decision receipt evidence | Preserve what was considered when the decision was made. |

Evidence is not merely attachment material. It is the audit substrate that makes a trust claim falsifiable.
