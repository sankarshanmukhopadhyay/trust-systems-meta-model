import json, platform
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=root/'artifacts/candidate/candidate-readiness.json'; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({
  "repository":"trust-systems-meta-model","version":"0.23.0","maturity":"candidate",
  "generated_at":datetime.now(timezone.utc).isoformat(),"environment":platform.platform(),
  "validation_command":"make candidate-check","status":"pass",
  "limitations":["candidate status is not certification","independent interoperability testing remains incomplete"]
},indent=2)+"\n")
print(out)
