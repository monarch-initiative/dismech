

# Slot: module 


_Reference to a mechanism module in kb/modules/ (filename stem, without .yaml, optionally with a "#Node Name" anchor). Used by CONFORMS_TO_MODULE criteria and by differentiating mechanisms._





URI: [dismech:slot/module](https://w3id.org/monarch-initiative/dismech/slot/module)
Alias: module

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |
| [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) | A mechanism or feature that distinguishes a grouping member from its siblings... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [LogicalCriterion](../classes/LogicalCriterion.md), [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:module |
| native | dismech:module |




## LinkML Source

<details>
```yaml
name: module
description: Reference to a mechanism module in kb/modules/ (filename stem, without
  .yaml, optionally with a "#Node Name" anchor). Used by CONFORMS_TO_MODULE criteria
  and by differentiating mechanisms.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: module
domain_of:
- LogicalCriterion
- DifferentiatingMechanism
range: string

```
</details>