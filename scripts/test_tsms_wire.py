#!/usr/bin/env python3
import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]; case=json.loads((ROOT/'model/tsms-wire-001.json').read_text())
def decide(i,semantic=True,contracts=True,governance=True): return 'PERMIT' if semantic and contracts and governance and i.get('authority') and i.get('delegation') and i.get('requestedEffect') in i.get('scope',[]) and i.get('evidenceBundle') and i.get('relationshipState')=='current' else 'REJECT'
b=case['input']; tests=[('valid',b,'PERMIT',{}),('missing authority',{**b,'authority':None},'REJECT',{}),('missing delegation',{**b,'delegation':None},'REJECT',{}),('out of scope',{**b,'requestedEffect':'urn:example:effect:delete-record'},'REJECT',{}),('missing evidence',{**b,'evidenceBundle':None},'REJECT',{}),('revoked',{**b,'relationshipState':'revoked'},'REJECT',{}),('semantic unresolved',b,'REJECT',{'semantic':False}),('contract unavailable',b,'REJECT',{'contracts':False}),('governance absent',b,'REJECT',{'governance':False})]; results=[]; failures=[]
for name,i,expected,flags in tests:
 actual=decide(i,**flags); results.append({'case':name,'expected':expected,'actual':actual,'status':'pass' if actual==expected else 'fail'}); failures += [name] if actual!=expected else []
out={'profile':'tsms-wire-pressure-tests','status':'fail' if failures else 'pass','results':results}; p=ROOT/'artifacts/e2e/TSMS-WIRE-001/pressure-tests.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n')
if failures: print('FAIL: '+','.join(failures)); sys.exit(1)
print('TSMS-WIRE-001 pressure tests: PASS')
