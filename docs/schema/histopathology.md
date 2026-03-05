

# Slot: histopathology 


_Histopathologic findings including microscopic morphology, architectural patterns, cellular features, growth patterns, and histologic grading._





URI: [dismech:histopathology](https://w3id.org/monarch-initiative/dismech/histopathology)
Alias: histopathology

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](Disease.md) |  |  no  |






## Properties

* Range: [HistopathologyFinding](HistopathologyFinding.md)

* Multivalued: True




## Comments

* Separate from phenotypes as these are tissue-level microscopic observations
* Use NCIT Morphologic Finding (C35867) or Histologic Grade (C18000) terms
* {'For cancer': 'includes grade, differentiation, growth patterns, necrosis'}
* {'For other diseases': 'may include architectural changes, cellular infiltrates'}

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:histopathology |
| native | dismech:histopathology |




## LinkML Source

<details>
```yaml
name: histopathology
description: Histopathologic findings including microscopic morphology, architectural
  patterns, cellular features, growth patterns, and histologic grading.
comments:
- Separate from phenotypes as these are tissue-level microscopic observations
- Use NCIT Morphologic Finding (C35867) or Histologic Grade (C18000) terms
- '{''For cancer'': ''includes grade, differentiation, growth patterns, necrosis''}'
- '{''For other diseases'': ''may include architectural changes, cellular infiltrates''}'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: histopathology
domain_of:
- Disease
range: HistopathologyFinding
multivalued: true
inlined: true
inlined_as_list: true

```
</details>