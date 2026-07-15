#!/usr/bin/env python3
from pathlib import Path
import json
p=Path('data/portfolio-relationships.json')
d=json.loads(p.read_text())
required={'source_repository','target_repository','relationship_type','authority_direction','artifact_mapping','compatibility_range','maturity','validation','known_limitations','supersession'}
for i,x in enumerate(d.get('relationships',[])):
 missing=required-set(x)
 if missing: raise SystemExit(f'relationship {i} missing: {sorted(missing)}')
 if x['source_repository']==x['target_repository']: raise SystemExit('self dependency is not permitted')
print(f"Portfolio relationships: PASS ({len(d.get('relationships',[]))} declarations)")
