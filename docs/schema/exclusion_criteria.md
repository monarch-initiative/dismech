

# Slot: exclusion_criteria 


_Exclusion criteria for a definition or criteria set_





URI: [dismech:exclusion_criteria](https://w3id.org/monarch-initiative/dismech/exclusion_criteria)
Alias: exclusion_criteria

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  no  |






## Properties

* Range: [CriteriaItem](CriteriaItem.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:exclusion_criteria |
| native | dismech:exclusion_criteria |




## LinkML Source

<details>
```yaml
name: exclusion_criteria
description: Exclusion criteria for a definition or criteria set
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: exclusion_criteria
domain_of:
- Definition
- CriteriaSet
range: CriteriaItem
multivalued: true
inlined: true
inlined_as_list: true

```
</details>