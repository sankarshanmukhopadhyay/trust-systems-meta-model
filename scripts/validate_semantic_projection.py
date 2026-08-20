#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator
root=Path(__file__).resolve().parents[1]
registry=json.loads((root/'model/semantic-concepts.json').read_text())
reg_schema=json.loads((root/'schemas/tsmm-semantic-concept-registry.schema.json').read_text())
projection=json.loads((root/'bindings/tis/tsmm-tis-semantic-projection.json').read_text())
proj_schema=json.loads((root/'schemas/semantic-projection.schema.json').read_text())
for obj,schema,label in [(registry,reg_schema,'semantic registry'),(projection,proj_schema,'TIS projection')]:
    errors=list(Draft202012Validator(schema).iter_errors(obj))
    if errors: raise SystemExit(label+': '+errors[0].message)
ids=[x['id'] for x in registry['concepts']]
if len(ids)!=len(set(ids)): raise SystemExit('duplicate TSMM semantic identifiers')
known=set(ids)
unknown=sorted({x['conceptId'] for x in projection['mappings']}-known)
if unknown: raise SystemExit('projection references unknown concepts: '+', '.join(unknown))

(root/'artifacts/portfolio').mkdir(parents=True,exist_ok=True)
evidence={'repository':'trust-systems-meta-model','semanticAuthority':'trust-systems-meta-model','targetRepository':'trust-infrastructure-schemas','relationship':'informative-alignment','inverseRelationship':'normative-dependency','unknownConceptReferences':0,'authorityConflicts':0,'status':'pass'}
(root/'artifacts/portfolio/portfolio-alignment.json').write_text(json.dumps(evidence,indent=2)+'\n')
print(f'Semantic projection: PASS ({len(ids)} concepts, {len(projection["mappings"])} TIS mappings)')
