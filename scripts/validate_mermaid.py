#!/usr/bin/env python3
import json, re, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
blocks=[]
for p in root.rglob("*.md"):
    if any(x in p.parts for x in ("vendor","node_modules","_site")): continue
    text=p.read_text(encoding="utf-8")
    for i,m in enumerate(re.finditer(r"```mermaid\s*\n(.*?)```", text, re.S),1):
        code=m.group(1).strip()
        ok=bool(code) and code.splitlines()[0].split()[0] in {"flowchart","graph","sequenceDiagram","stateDiagram-v2","classDiagram","erDiagram","journey","gantt","pie","mindmap","timeline"}
        blocks.append({"file":str(p.relative_to(root)),"index":i,"ok":ok,"first_line":code.splitlines()[0] if code else ""})
out=root/"artifacts/validation/mermaid-validation.json"; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"diagram_count":len(blocks),"results":blocks},indent=2)+"\n")
failed=[b for b in blocks if not b["ok"]]
print(f"Validated {len(blocks)} Mermaid diagrams")
if failed:
    print(json.dumps(failed,indent=2)); sys.exit(1)
