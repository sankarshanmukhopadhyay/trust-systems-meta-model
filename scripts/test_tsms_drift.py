#!/usr/bin/env python3
import importlib.util, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('drift', ROOT/'scripts/check_tsms_drift.py')
drift=importlib.util.module_from_spec(spec); spec.loader.exec_module(drift)
receipt=json.loads((ROOT/'model/tsms-baseline-receipt.json').read_text())
baselines={c['id']:c for c in receipt['components']}
cases=[
 ('validation/tsms/drift/exact-baseline.json','UNCHANGED'),
 ('validation/tsms/drift/same-version-different-commit.json','REVIEW_REQUIRED'),
 ('validation/tsms/drift/unavailable-remote.json','INDETERMINATE'),
]
failures=[]; results=[]
precedence={'UNCHANGED':0,'REVIEW_REQUIRED':1,'UNSUPPORTED':2,'INDETERMINATE':3}
for path,expected in cases:
    data=json.loads((ROOT/path).read_text()); dispositions=[]
    for current in data['components']:
        disposition,_=drift.classify(baselines[current['id']],current); dispositions.append(disposition)
    actual=max(dispositions,key=lambda x:precedence[x])
    results.append({'fixture':path,'expected':expected,'actual':actual,'status':'pass' if actual==expected else 'fail'})
    if actual!=expected: failures.append(f'{path}: expected {expected}, got {actual}')
out={'profile':'tsms-drift-pressure-tests','status':'fail' if failures else 'pass','results':results}
(ROOT/'artifacts/validation').mkdir(parents=True,exist_ok=True)
(ROOT/'artifacts/validation/tsms-drift-tests.json').write_text(json.dumps(out,indent=2)+'\n')
if failures: print('\n'.join(failures)); sys.exit(1)
print('TSMS drift pressure tests: PASS')
