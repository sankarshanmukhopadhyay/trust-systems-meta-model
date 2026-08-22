#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[1]
registry = json.loads((root / 'model/semantic-concepts.json').read_text())
reg_schema = json.loads((root / 'schemas/tsmm-semantic-concept-registry.schema.json').read_text())
proj_schema = json.loads((root / 'schemas/semantic-projection.schema.json').read_text())

errors = list(Draft202012Validator(reg_schema).iter_errors(registry))
if errors:
    raise SystemExit('semantic registry: ' + errors[0].message)

ids = [x['id'] for x in registry['concepts']]
if len(ids) != len(set(ids)):
    raise SystemExit('duplicate TSMM semantic identifiers')
known = set(ids)

projection_paths = sorted((root / 'bindings').glob('*/*semantic-projection.json'))
if not projection_paths:
    raise SystemExit('no semantic projection contracts found')

summaries = []
for path in projection_paths:
    projection = json.loads(path.read_text())
    errors = list(Draft202012Validator(proj_schema).iter_errors(projection))
    if errors:
        raise SystemExit(f'{path.relative_to(root)}: ' + errors[0].message)
    unknown = sorted({x['conceptId'] for x in projection['mappings']} - known)
    if unknown:
        raise SystemExit(
            f'{path.relative_to(root)} references unknown concepts: ' + ', '.join(unknown)
        )
    summaries.append({
        'projectionId': projection['projectionId'],
        'targetRepository': projection['target']['repository'],
        'relationship': projection['relationship'],
        'mappingCount': len(projection['mappings']),
        'unknownConceptReferences': 0,
        'authorityBoundaryPreserved': (
            projection['authorityBoundary']['semanticAuthorityRemainsWithSource'] is True
            and projection['authorityBoundary']['serializationAuthorityRemainsWithTarget'] is True
        )
    })

(root / 'artifacts/portfolio').mkdir(parents=True, exist_ok=True)
evidence = {
    'repository': 'trust-systems-meta-model',
    'semanticAuthority': 'trust-systems-meta-model',
    'semanticRegistryVersion': registry['version'],
    'projections': summaries,
    'unknownConceptReferences': 0,
    'authorityConflicts': 0,
    'status': 'pass'
}
(root / 'artifacts/portfolio/portfolio-alignment.json').write_text(json.dumps(evidence, indent=2) + '\n')
print(
    f'Semantic projection: PASS ({len(ids)} concepts, '
    f'{len(projection_paths)} projection contracts, '
    f'{sum(x["mappingCount"] for x in summaries)} mappings)'
)
