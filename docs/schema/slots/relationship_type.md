

# Slot: relationship_type 


_Controlled-vocabulary classification of the gene-disease relationship (e.g., causative, risk factor, modifier, somatic driver). Use this in addition to the free-text `association` slot when possible._





URI: [dismech:slot/relationship_type](https://w3id.org/monarch-initiative/dismech/slot/relationship_type)
Alias: relationship_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneDiseaseRelationshipEnum](../enums/GeneDiseaseRelationshipEnum.md) |
| Domain Of | [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| RISK_FACTOR |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:relationship_type |
| native | dismech:relationship_type |




## LinkML Source

<details>
```yaml
name: relationship_type
description: Controlled-vocabulary classification of the gene-disease relationship
  (e.g., causative, risk factor, modifier, somatic driver). Use this in addition to
  the free-text `association` slot when possible.
examples:
- value: RISK_FACTOR
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: relationship_type
domain_of:
- Genetic
range: GeneDiseaseRelationshipEnum

```
</details>