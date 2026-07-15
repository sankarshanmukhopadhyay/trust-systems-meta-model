#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
p=Path('governance/repository-authority.yaml')
if not p.exists(): raise SystemExit('missing authority declaration')
d=yaml.safe_load(p.read_text())
required=['repository','portfolio_tier','lifecycle','role','authority','dependencies','supersession_policy','revocation_or_withdrawal_policy']
missing=[x for x in required if x not in d]
if missing: raise SystemExit('missing fields: '+', '.join(missing))
if d['portfolio_tier']!='flagship' or d['lifecycle']!='active': raise SystemExit('invalid flagship lifecycle')
own=set(d['authority'].get('owns',[])); no=set(d['authority'].get('does_not_own',[]))
if own & no: raise SystemExit('conflicting authority claims: '+', '.join(sorted(own&no)))
print('Repository governance declaration: PASS')
