# Enum: NCITDiseaseOrFindingTerm




_An NCIT disease-oriented oncology term used for disease-level cancer mappings and subtype grounding, including neoplasm-by-morphology, special-category neoplasm, and clinically used disease/finding boundary concepts._



URI: [dismech:enum/NCITDiseaseOrFindingTerm](https://w3id.org/monarch-initiative/dismech/enum/NCITDiseaseOrFindingTerm)


_This is a dynamic enum_







## Comments

* Prefer MONDO for disease_term and subtype_term when an appropriate MONDO class exists.
* Use this range for supplemental NCIT disease mappings on cancer entries.
* Use this range for cancer subtype grounding when MONDO lacks the needed oncology refinement.
* Broad rooting across NCIT disease and neoplasm branches accommodates clinically important labels such as CMML-0/1/2.

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: NCITDiseaseOrFindingTerm
description: An NCIT disease-oriented oncology term used for disease-level cancer
  mappings and subtype grounding, including neoplasm-by-morphology, special-category
  neoplasm, and clinically used disease/finding boundary concepts.
comments:
- Prefer MONDO for disease_term and subtype_term when an appropriate MONDO class exists.
- Use this range for supplemental NCIT disease mappings on cancer entries.
- Use this range for cancer subtype grounding when MONDO lacks the needed oncology
  refinement.
- Broad rooting across NCIT disease and neoplasm branches accommodates clinically
  important labels such as CMML-0/1/2.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
reachable_from:
  source_nodes:
  - NCIT:C2991
  - NCIT:C4741
  - NCIT:C7062
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>
