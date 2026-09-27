# Enum: HistopathologyFindingTerm 




_A histopathologic finding term from NCIT. Covers the full NCIT Histopathology Result branch (NCIT:C83490): morphologic findings, architectural/growth patterns, cellular features, grading, immunophenotype (IHC/flow markers), ultrastructure, and staining intensity._



URI: [dismech:enum/HistopathologyFindingTerm](https://w3id.org/monarch-initiative/dismech/enum/HistopathologyFindingTerm)
## Enumeration Source
**Reachable From:**
- **Nodes:** NCIT:C83490, NCIT:C35867, NCIT:C40998, NCIT:C43265, NCIT:C127762, NCIT:C18000, NCIT:C4741, NCIT:C7062, NCIT:C36289, NCIT:C19955, NCIT:C188218, NCIT:C37008, HP:0025461
- **Via:** rdfs:subClassOf




_This is a dynamic enum_










## Comments

* NCIT:C35867 Morphologic Finding - architectural patterns, dysplasia, necrosis, etc.
* NCIT:C18000 Histologic Grade - Fuhrman, Nottingham, WHO grades, etc.
* NCIT:C40998 Immunophenotypic Finding - IHC/flow markers (e.g., ER-positive by IHC, CD20-positive cells, loss of SDHB expression)
* NCIT:C43265 Ultrastructural Finding - electron-microscopy features (e.g., Weibel-Palade bodies, foot process effacement)
* NCIT:C127762 Staining Intensity - graded stain intensity readouts
* Also includes HP terms for rosettes (HP:0031925-HP:0031930)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: HistopathologyFindingTerm
description: 'A histopathologic finding term from NCIT. Covers the full NCIT Histopathology
  Result branch (NCIT:C83490): morphologic findings, architectural/growth patterns,
  cellular features, grading, immunophenotype (IHC/flow markers), ultrastructure,
  and staining intensity.'
comments:
- NCIT:C35867 Morphologic Finding - architectural patterns, dysplasia, necrosis, etc.
- NCIT:C18000 Histologic Grade - Fuhrman, Nottingham, WHO grades, etc.
- NCIT:C40998 Immunophenotypic Finding - IHC/flow markers (e.g., ER-positive by IHC,
  CD20-positive cells, loss of SDHB expression)
- NCIT:C43265 Ultrastructural Finding - electron-microscopy features (e.g., Weibel-Palade
  bodies, foot process effacement)
- NCIT:C127762 Staining Intensity - graded stain intensity readouts
- Also includes HP terms for rosettes (HP:0031925-HP:0031930)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
reachable_from:
  source_nodes:
  - NCIT:C83490
  - NCIT:C35867
  - NCIT:C40998
  - NCIT:C43265
  - NCIT:C127762
  - NCIT:C18000
  - NCIT:C4741
  - NCIT:C7062
  - NCIT:C36289
  - NCIT:C19955
  - NCIT:C188218
  - NCIT:C37008
  - HP:0025461
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>