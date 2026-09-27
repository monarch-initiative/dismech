

# Slot: histopathology 


_Histopathologic findings including microscopic morphology, architectural patterns, cellular features, growth patterns, histologic grading, and immunophenotype._





URI: [dismech:slot/histopathology](https://w3id.org/monarch-initiative/dismech/slot/histopathology)
Alias: histopathology

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [HistopathologyFinding](../classes/HistopathologyFinding.md) |
| Domain Of | [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Separate from phenotypes as these are tissue-level microscopic observations
* Use NCIT terms from the Histopathology Result branch (C83490) - Morphologic Finding (C35867), Immunophenotypic Finding (C40998), Ultrastructural Finding (C43265), Staining Intensity (C127762), or Histologic Grade (C18000)
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
  patterns, cellular features, growth patterns, histologic grading, and immunophenotype.
comments:
- Separate from phenotypes as these are tissue-level microscopic observations
- Use NCIT terms from the Histopathology Result branch (C83490) - Morphologic Finding
  (C35867), Immunophenotypic Finding (C40998), Ultrastructural Finding (C43265), Staining
  Intensity (C127762), or Histologic Grade (C18000)
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