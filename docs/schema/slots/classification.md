

# Slot: classification 


_Classification scheme this subtype belongs to (e.g., 'complementation_group', 'pathway_tier', 'histological', 'molecular', 'clinical_phenotype')._





URI: [dismech:slot/classification](https://w3id.org/monarch-initiative/dismech/slot/classification)
Alias: classification

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Subtype](../classes/Subtype.md), [LogicalCriterion](../classes/LogicalCriterion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:classification |
| native | dismech:classification |




## LinkML Source

<details>
```yaml
name: classification
description: Classification scheme this subtype belongs to (e.g., 'complementation_group',
  'pathway_tier', 'histological', 'molecular', 'clinical_phenotype').
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: classification
domain_of:
- Subtype
- LogicalCriterion
range: string

```
</details>