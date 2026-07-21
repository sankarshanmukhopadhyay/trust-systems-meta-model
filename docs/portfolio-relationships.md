---
title: Portfolio relationships
parent: Documentation
nav_order: 8
permalink: /portfolio-relationships.html
---
# Portfolio relationships

```mermaid
flowchart LR
  GAAM[GAAM governance and authority model] -->|informative alignment| TSMM[TSMM canonical semantics]
  TSMM -->|informative alignment| TIS[TIS portable schema contracts]
  TIS -->|supports| TGA[Trust Graph Artifacts]
  TSMM -->|supports| TGA
  TGA -->|produces executable evidence| ASSURE[Conformance and assurance systems]
  ASSURE -->|assurance feedback| TSMM
  ASSURE -->|assurance feedback| TIS
```

The arrows describe bounded relationships, not shared release authority. TSMM does not own TIS serialization decisions, and TIS does not redefine TSMM canonical semantics.
