#!/usr/bin/env python3
import json, pathlib, sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
SUITE=ROOT/'model/tsms-e2e-suite.json'
RECEIPT=ROOT/'model/tsms-baseline-receipt.json'
LINEAGE=ROOT/'model/tsms-baseline-lineage.json'
OUT=ROOT/'artifacts/e2e/TSMS-E2E-001/evidence-bundle.json'


def load(path): return json.loads(path.read_text())

def decision(case):
    permitted=all(case[k] for k in ('authority','delegationCurrent','scopeAllowed','evidenceComplete'))
    return 'PERMIT' if permitted else 'REJECT'

def main():
    suite,receipt,lineage=load(SUITE),load(RECEIPT),load(LINEAGE)
    errors=[]
    components={c['id']:c for c in receipt.get('components',[])}
    expected={'tsmm','tis','tga'}
    if set(components)!=expected: errors.append('baseline must contain exactly tsmm, tis and tga')
    if lineage.get('activeReceipt')!=receipt.get('receiptId'): errors.append('active lineage receipt does not match baseline receipt')
    if any(len(c.get('commit',''))!=40 for c in components.values()): errors.append('all component states must be pinned commits')
    semantic=suite['semanticAuthority']['requiredConceptIds']
    if len(semantic)!=len(set(semantic)) or not semantic: errors.append('semantic dependencies must be unique and non-empty')
    contracts=suite['portableContractAuthority']['requiredContracts']
    if len(contracts)!=len(set(contracts)) or not contracts: errors.append('portable contract dependencies must be unique and non-empty')
    if not suite['executableGovernance'].get('artifactId'): errors.append('executable governance artifact is required')

    cases=[]
    for case in suite.get('cases',[]):
        actual=decision(case)
        ok=actual==case.get('expected')
        cases.append({'id':case['id'],'expected':case['expected'],'actual':actual,'status':'pass' if ok else 'fail'})
        if not ok: errors.append(f"{case['id']}: expected {case['expected']}, got {actual}")

    evidence={
      'suiteId':suite['suiteId'],
      'caseId':suite['caseId'],
      'baselineReceipt':receipt['receiptId'],
      'componentStates':{k:{'version':v['version'],'commit':v['commit'],'role':v['role']} for k,v in components.items()},
      'checks':{
        'semanticLayer':'PASS' if semantic else 'FAIL',
        'portableContractLayer':'PASS' if contracts else 'FAIL',
        'executableGovernanceLayer':'PASS' if suite['executableGovernance'].get('artifactId') else 'FAIL',
        'baselineLineage':'PASS' if lineage.get('activeReceipt')==receipt.get('receiptId') else 'FAIL',
        'executionCases':'PASS' if all(c['status']=='pass' for c in cases) else 'FAIL'
      },
      'executionCases':cases,
      'overall':'PASS' if not errors else 'FAIL',
      'limitations':[
        'This first E2E slice validates the pinned cross-layer contract and governance decision semantics deterministically.',
        'Independent remote retrieval of TIS/TGA content and drift-to-renewal execution are separate follow-on tests.',
        'Repository validation is not external certification.'
      ]
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(evidence,indent=2)+'\n')
    if errors:
        print('\n'.join(errors)); return 1
    print('TSMS E2E TSMS-E2E-001: PASS'); return 0

if __name__=='__main__': sys.exit(main())
