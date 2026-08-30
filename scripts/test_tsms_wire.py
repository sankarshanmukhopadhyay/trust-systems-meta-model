#!/usr/bin/env python3
import copy, json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
case=json.loads((ROOT/'model/tsms-wire-001.json').read_text())

def decide(inp,semantic=True,contracts=True,governance=True):
    return 'PERMIT' if semantic and contracts and governance and inp.get('authority') and inp.get('delegation') and inp.get('requestedEffect') in inp.get('scope',[]) and inp.get('evidenceBundle') and inp.get('relationshipState')=='current' else 'REJECT'
base=case['input']; tests=[('valid',base,'PERMIT',{}),('missing authority',{**base,'authority':None},'REJECT',{}),('missing delegation',{**base,'delegation':None},'REJECT',{}),('out of scope',{**base,'requestedEffect':'urn:example:effect:delete-record'},'REJECT',{}),('missing evidence',{**base,'evidenceBundle':None},'REJECT',{}),('revoked relationship',{**base,'relationshipState':'revoked'},'REJECT',{}),('semantic unresolved',base,'REJECT',{'semantic':False}),('contract unavailable',base,'REJECT',{'contracts':False}),('governance binding absent',base,'REJECT',{'governance':False})]
results=[]; failures=[]
for name,inp,expected,flags in tests:
    actual=decide(inp,**flags); results.append({'case':name,'expected':expected,'actual':actual,'status':'pass' if actual==expected else 'fail'})
    if actual!=expected: failures.append(name)
out={'profile':'tsms-wire-pressure-tests','status':'fail' if failures else 'pass','results':results}; p=ROOT/'artifacts/e2e/TSMS-WIRE-001/pressure-tests.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n')
if failures: print('FAIL: '+','.join(failures)); sys.exit(1)
print('TSMS-WIRE-001 pressure tests: PASS')
