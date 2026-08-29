#!/usr/bin/env python3
import importlib.util, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('lineage',ROOT/'scripts/validate_tsms_baseline_lineage.py')
lineage=importlib.util.module_from_spec(spec); spec.loader.exec_module(lineage)
cases=[
 ('model/tsms-baseline-lineage.json','valid'),
 ('validation/tsms/lineage/duplicate-receipt-id.json','reject'),
 ('validation/tsms/lineage/broken-predecessor.json','reject'),
 ('validation/tsms/lineage/multiple-active.json','reject')
]
failures=[]; results=[]
for path,expected in cases:
    errors=lineage.validate(json.loads((ROOT/path).read_text()),ROOT)
    actual='reject' if errors else 'valid'
    results.append({'fixture':path,'expected':expected,'actual':actual,'errors':errors,'status':'pass' if actual==expected else 'fail'})
    if actual!=expected: failures.append(f'{path}: expected {expected}, got {actual}')
out={'profile':'tsms-baseline-lineage-pressure-tests','status':'fail' if failures else 'pass','results':results}
(ROOT/'artifacts/validation').mkdir(parents=True,exist_ok=True)
(ROOT/'artifacts/validation/tsms-baseline-lineage-tests.json').write_text(json.dumps(out,indent=2)+'\n')
if failures:
    print('\n'.join(failures)); sys.exit(1)
print('TSMS baseline lineage pressure tests: PASS')
