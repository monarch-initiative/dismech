

# Slot: case_fractions 


_Per-cohort estimates of the fraction of cases of a genetically heterogeneous disease attributable to this gene (the genetic-spectrum analog of population Prevalence records). Multivalued because the share varies by cohort/ancestry._





URI: [dismech:slot/case_fractions](https://w3id.org/monarch-initiative/dismech/slot/case_fractions)
Alias: case_fractions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneCaseFraction](../classes/GeneCaseFraction.md) |
| Domain Of | [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:case_fractions |
| native | dismech:case_fractions |




## LinkML Source

<details>
```yaml
name: case_fractions
description: Per-cohort estimates of the fraction of cases of a genetically heterogeneous
  disease attributable to this gene (the genetic-spectrum analog of population Prevalence
  records). Multivalued because the share varies by cohort/ancestry.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: case_fractions
domain_of:
- Genetic
range: GeneCaseFraction
multivalued: true
inlined: true
inlined_as_list: true

```
</details>