

# Slot: organism 


_The organism from which samples were derived_





URI: [dismech:slot/organism](https://w3id.org/monarch-initiative/dismech/slot/organism)
Alias: organism

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
| Range | [OrganismDescriptor](../classes/OrganismDescriptor.md) |
| Domain Of | [Dataset](../classes/Dataset.md), [ExperimentalModel](../classes/ExperimentalModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:organism |
| native | dismech:organism |




## LinkML Source

<details>
```yaml
name: organism
description: The organism from which samples were derived
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: organism
domain_of:
- Dataset
- ExperimentalModel
range: OrganismDescriptor
inlined: true

```
</details>