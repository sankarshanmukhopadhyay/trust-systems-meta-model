#!/usr/bin/env python3
import importlib.util, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('drift', ROOT/'scripts/check_tsms_drift.py')
drift=importlib.util.module_from_spec(spec); spec.loader.exec_module(drift)
receipt=json.loads((ROOT/'model/tsms-baseline-receipt.json').read_text()); baselines={c['id']:c for c in receipt['components']}
base=baselines['tsmm']; digest='a'*64

def state(**changes):
    value={'id':'tsmm','repository':base['repository'],'version':base['version'],'commit':base['commit'],'role':base['role'],'remoteEvidenceStatus':'available','declarationPath':'model/tsms-stack.json','baselineDeclarationDigest':digest,'declarationDigest':digest}
    value.update(changes); return value
cases=[
 ('exact authoritative state',state(),'UNCHANGED'),
 ('same version declaration drift',state(declarationDigest='b'*64),'REVIEW_REQUIRED'),
 ('version change',state(version='v0.25.0'),'REVIEW_REQUIRED'),
 ('authority role change',state(role='changed-role'),'REVIEW_REQUIRED'),
 ('same version commit drift',state(commit='1'*40),'REVIEW_REQUIRED'),
 ('unavailable remote',state(remoteEvidenceStatus='unavailable'),'INDETERMINATE'),
 ('missing VERSION',state(version=None,remoteEvidenceStatus='unavailable'),'INDETERMINATE'),
 ('missing declaration',state(declarationDigest=None,remoteEvidenceStatus='unavailable'),'INDETERMINATE'),
 ('malformed declaration',state(remoteEvidenceStatus='unavailable'),'INDETERMINATE'),
]
failures=[]; results=[]
for name,current,expected in cases:
    actual,_=drift.classify(base,current); results.append({'case':name,'expected':expected,'actual':actual,'status':'pass' if actual==expected else 'fail'})
    if actual!=expected: failures.append(f'{name}: expected {expected}, got {actual}')
unknown={'id':'other','repository':'example/other','version':'v1','commit':'1'*40,'role':'other','remoteEvidenceStatus':'available'}
actual,_=drift.classify(base,unknown); results.append({'case':'unknown component','expected':'UNSUPPORTED','actual':actual,'status':'pass' if actual=='UNSUPPORTED' else 'fail'})
if actual!='UNSUPPORTED': failures.append(f'unknown component: expected UNSUPPORTED, got {actual}')
out={'profile':'tsms-authoritative-drift-pressure-tests','status':'fail' if failures else 'pass','results':results}
(ROOT/'artifacts/validation').mkdir(parents=True,exist_ok=True); (ROOT/'artifacts/validation/tsms-drift-tests.json').write_text(json.dumps(out,indent=2)+'\n')
if failures: print('\n'.join(failures)); sys.exit(1)
print('TSMS authoritative drift pressure tests: PASS')
