

# Slot: operator 


_Boolean operator for a branch node in a membership-criteria expression. Present on branch nodes; absent on leaf nodes._





URI: [dismech:slot/operator](https://w3id.org/monarch-initiative/dismech/slot/operator)
Alias: operator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LogicalOperatorEnum](../enums/LogicalOperatorEnum.md) |
| Domain Of | [LogicalCriterion](../classes/LogicalCriterion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:operator |
| native | dismech:operator |




## LinkML Source

<details>
```yaml
name: operator
description: Boolean operator for a branch node in a membership-criteria expression.
  Present on branch nodes; absent on leaf nodes.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: operator
domain_of:
- LogicalCriterion
range: LogicalOperatorEnum

```
</details>