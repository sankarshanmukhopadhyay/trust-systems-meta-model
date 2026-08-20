#!/usr/bin/env python3
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
v=(root/"VERSION").read_text().strip()
checks={
 "README.md": f"Current version:** `v{v}`",
 "governance/repository-authority.yaml": f"current_version: \"v{v}\"",
 "releases/index.md": f"v{v}",
}
for f,needle in checks.items():
    t=(root/f).read_text()
    if needle not in t: raise SystemExit(f"{f} does not declare v{v}")
print(f"Version consistency: PASS (v{v})")
