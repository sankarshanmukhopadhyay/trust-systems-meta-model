#!/usr/bin/env python3
import datetime, hashlib, json, pathlib, sys, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
CASE=json.loads((ROOT/'model/tsms-wire-001.json').read_text())
RECEIPT=json.loads((ROOT/'model/tsms-baseline-receipt.json').read_text())

def fetch(repo, commit, path):
    req=urllib.request.Request(f'https://raw.githubusercontent.com/{repo}/{commit}/{path}',headers={'User-Agent':'tsms-wire-001'})
    with urllib.request.urlopen(req,timeout=15) as r: return r.read().decode('utf-8')

def digest(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    components={c['id']:c for c in RECEIPT['components']}; evidence=[]
    try:
        tsmm=json.loads(fetch(components['tsmm']['repository'],components['tsmm']['commit'],'model/tsms-stack.json'))
        tis=json.loads(fetch(components['tis']['repository'],components['tis']['commit'],'model/tsms-compatibility.json'))
        tga=json.loads(fetch(components['tga']['repository'],components['tga']['commit'],'examples/tsms/golden-path.json'))
    except Exception as exc:
        print(f'TSMS-WIRE-001: INDETERMINATE ({type(exc).__name__})'); return 2
    tga_concepts=set(tga.get('semanticAuthority',{}).get('conceptIds',[])); required_concepts=set(CASE['requiredSemanticConcepts'])
    semantic_ok=required_concepts.issubset(tga_concepts)
    tis_contracts=set(tis.get('goldenPathContracts',[])); required_contracts=set(CASE['requiredPortableContracts']); contracts_ok=required_contracts.issubset(tis_contracts)
    governance_ok=tga.get('artifactId')==CASE['requiredGovernanceArtifact'] and set(tga.get('portableContractAuthority',{}).get('contracts',[]))>=required_contracts
    inp=CASE['input']; decision='PERMIT' if semantic_ok and contracts_ok and governance_ok and inp.get('authority') and inp.get('delegation') and inp.get('requestedEffect') in inp.get('scope',[]) and inp.get('evidenceBundle') and inp.get('relationshipState')=='current' else 'REJECT'
    for cid,obj,path in [('tsmm',tsmm,'model/tsms-stack.json'),('tis',tis,'model/tsms-compatibility.json'),('tga',tga,'examples/tsms/golden-path.json')]:
        c=components[cid]; evidence.append({'component':cid,'repository':c['repository'],'commit':c['commit'],'version':c['version'],'declarationPath':path,'declarationDigest':digest(obj)})
    out={'profile':'TSMS-WIRE-001','transactionId':CASE['transactionId'],'baselineReceipt':CASE['baselineReceipt'],'componentEvidence':evidence,'checks':{'semanticResolution':semantic_ok,'portableContracts':contracts_ok,'governanceBinding':governance_ok},'inputDigest':digest(inp),'decision':decision,'expectedDecision':CASE['expectedDecision'],'status':'PASS' if decision==CASE['expectedDecision'] else 'FAIL','executedAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    p=ROOT/'artifacts/e2e/TSMS-WIRE-001/wire-transaction-receipt.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(out,indent=2)+'\n')
    print(f"TSMS-WIRE-001: {out['status']} / {decision}"); return 0 if out['status']=='PASS' else 1
if __name__=='__main__': sys.exit(main())
