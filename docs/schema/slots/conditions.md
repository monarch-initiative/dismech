

# Slot: conditions 


_Experimental conditions or disease states represented_





URI: [dismech:slot/conditions](https://w3id.org/monarch-initiative/dismech/slot/conditions)
Alias: conditions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalModel](../classes/ExperimentalModel.md) | A disease-relevant non-animal experimental model system |  no  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Dataset](../classes/Dataset.md), [ExperimentalModel](../classes/ExperimentalModel.md) |

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
| self | dismech:conditions |
| native | dismech:conditions |




## LinkML Source

<details>
```yaml
name: conditions
description: Experimental conditions or disease states represented
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: conditions
domain_of:
- Dataset
- ExperimentalModel
range: string
multivalued: true

```
</details>