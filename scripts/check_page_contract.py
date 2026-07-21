#!/usr/bin/env python3
"""Validate the source-to-GitHub-Pages publication contract."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.bundle','vendor','node_modules','_site','scripts','validation','artifacts','.github'}
errors=[]
count=0
for path in sorted(ROOT.rglob('*.md')):
    if any(part in EXCLUDED for part in path.parts):
        continue
    text=path.read_text(encoding='utf-8',errors='replace')
    count+=1
    if not text.startswith('---\n'):
        errors.append(f'{path.relative_to(ROOT)}: missing front matter')
        continue
    end=text.find('\n---\n',4)
    if end<0:
        errors.append(f'{path.relative_to(ROOT)}: unterminated front matter')
        continue
    fm=text[4:end]
    if not re.search(r'^title:\s*\S+',fm,re.M):
        errors.append(f'{path.relative_to(ROOT)}: missing title')
    if path.is_relative_to(ROOT/'docs'):
        rel=path.relative_to(ROOT/'docs')
        expected='/documentation/' if rel.as_posix()=='index.md' else (f'/{rel.parts[0]}/' if rel.name=='index.md' else f'/{rel.with_suffix(".html").as_posix()}')
        match=re.search(r'^permalink:\s*(\S+)',fm,re.M)
        actual=match.group(1) if match else None
        if actual!=expected:
            errors.append(f'{path.relative_to(ROOT)}: permalink {actual!r}, expected {expected!r}')

# Explicit regression checks for reported 404s.
for required in ('/model/discovery-governance.html','/model/capability-negotiation.html'):
    if not any(re.search(rf'^permalink:\s*{re.escape(required)}$',p.read_text(encoding="utf-8",errors="replace"),re.M) for p in (ROOT/'docs').rglob('*.md')):
        errors.append(f'missing canonical route {required}')

if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'Validated publication metadata and canonical routes for {count} Markdown sources.')
