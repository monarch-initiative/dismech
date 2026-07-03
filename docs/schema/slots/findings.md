

# Slot: findings 


_Key findings or claims extracted from this source (publication or dataset)_





URI: [dismech:slot/findings](https://w3id.org/monarch-initiative/dismech/slot/findings)
Alias: findings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalModel](../classes/ExperimentalModel.md) | A disease-relevant non-animal experimental model system |  no  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [PublicationReference](../classes/PublicationReference.md) | A reference to a publication with associated findings |  no  |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Finding](../classes/Finding.md) |
| Domain Of | [Dataset](../classes/Dataset.md), [ExperimentalModel](../classes/ExperimentalModel.md), [ComputationalModel](../classes/ComputationalModel.md), [PublicationReference](../classes/PublicationReference.md) |

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
| self | dismech:findings |
| native | dismech:findings |




## LinkML Source

<details>
```yaml
name: findings
description: Key findings or claims extracted from this source (publication or dataset)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: findings
domain_of:
- Dataset
- ExperimentalModel
- ComputationalModel
- PublicationReference
range: Finding
multivalued: true
inlined: true
inlined_as_list: true

```
</details>