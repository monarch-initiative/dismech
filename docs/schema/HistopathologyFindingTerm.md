# Enum: HistopathologyFindingTerm 




_A histopathologic finding term from NCIT. Includes morphologic findings, architectural patterns, growth patterns, cellular features, and grading. Rooted at NCIT:C35867 (Morphologic Finding) and NCIT:C18000 (Histologic Grade)._



URI: [dismech:HistopathologyFindingTerm](https://w3id.org/monarch-initiative/dismech/HistopathologyFindingTerm)


_This is a dynamic enum_







## Comments

* NCIT:C35867 Morphologic Finding - architectural patterns, dysplasia, necrosis, etc.
* NCIT:C18000 Histologic Grade - Fuhrman, Nottingham, WHO grades, etc.
* Also includes HP terms for rosettes (HP:0031925-HP:0031930)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: HistopathologyFindingTerm
description: A histopathologic finding term from NCIT. Includes morphologic findings,
  architectural patterns, growth patterns, cellular features, and grading. Rooted
  at NCIT:C35867 (Morphologic Finding) and NCIT:C18000 (Histologic Grade).
comments:
- NCIT:C35867 Morphologic Finding - architectural patterns, dysplasia, necrosis, etc.
- NCIT:C18000 Histologic Grade - Fuhrman, Nottingham, WHO grades, etc.
- Also includes HP terms for rosettes (HP:0031925-HP:0031930)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
reachable_from:
  source_nodes:
  - NCIT:C35867
  - NCIT:C18000
  - NCIT:C4741
  - NCIT:C7062
  - NCIT:C36289
  - NCIT:C19955
  - NCIT:C188218
  - HP:0025461
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>