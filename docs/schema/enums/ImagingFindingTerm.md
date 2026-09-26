# Enum: ImagingFindingTerm 




_An in-vivo imaging finding term. Imaging findings are drawn from the NCIT Imaging Finding branch (NCIT:C176708 / NCIT:C199145) and, because most radiologic observations coincide with a described phenotype, from the HP Phenotypic abnormality branch (HP:0000118) - e.g. white-matter lesions, atrophy, hyperintensity. Binding is RECOMMENDED (not REQUIRED): many specific radiologic appearances lack a dedicated NCIT/HP term and are left to preferred_term until a radiology ontology (e.g. RadLex via BioPortal) is wired in._



URI: [dismech:enum/ImagingFindingTerm](https://w3id.org/monarch-initiative/dismech/enum/ImagingFindingTerm)
## Enumeration Source
**Reachable From:**
- **Nodes:** NCIT:C176708, NCIT:C199145, HP:0000118
- **Via:** rdfs:subClassOf




_This is a dynamic enum_










## Comments

* NCIT:C176708 Imaging Finding - imaging observations
* NCIT:C199145 Clinical Finding Detected by Imaging
* HP:0000118 Phenotypic abnormality - imaging-observable phenotypes (atrophy, white-matter lesions, hyperintensity)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ImagingFindingTerm
description: 'An in-vivo imaging finding term. Imaging findings are drawn from the
  NCIT Imaging Finding branch (NCIT:C176708 / NCIT:C199145) and, because most radiologic
  observations coincide with a described phenotype, from the HP Phenotypic abnormality
  branch (HP:0000118) - e.g. white-matter lesions, atrophy, hyperintensity. Binding
  is RECOMMENDED (not REQUIRED): many specific radiologic appearances lack a dedicated
  NCIT/HP term and are left to preferred_term until a radiology ontology (e.g. RadLex
  via BioPortal) is wired in.'
comments:
- NCIT:C176708 Imaging Finding - imaging observations
- NCIT:C199145 Clinical Finding Detected by Imaging
- HP:0000118 Phenotypic abnormality - imaging-observable phenotypes (atrophy, white-matter
  lesions, hyperintensity)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
reachable_from:
  source_nodes:
  - NCIT:C176708
  - NCIT:C199145
  - HP:0000118
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>