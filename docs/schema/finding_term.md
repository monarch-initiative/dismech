

# Slot: finding_term 


_Ontology term for a histopathologic finding (from NCIT or HP)_





URI: [dismech:finding_term](https://w3id.org/monarch-initiative/dismech/finding_term)
Alias: finding_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |






## Properties

* Range: [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md)




## Comments

* Use NCIT terms from Morphologic Finding (C35867) or Histologic Grade (C18000)
* Use HP terms for rosettes and cell morphology abnormalities (HP:0025461 descendants)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:finding_term |
| native | dismech:finding_term |




## LinkML Source

<details>
```yaml
name: finding_term
description: Ontology term for a histopathologic finding (from NCIT or HP)
comments:
- Use NCIT terms from Morphologic Finding (C35867) or Histologic Grade (C18000)
- Use HP terms for rosettes and cell morphology abnormalities (HP:0025461 descendants)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: finding_term
domain_of:
- HistopathologyFinding
range: HistopathologyFindingDescriptor
inlined: true

```
</details>