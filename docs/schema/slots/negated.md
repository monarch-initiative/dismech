

# Slot: negated 


_If true, this leaf criterion is negated (the constraint must NOT hold). An alternative to wrapping the node in a NOT operator._





URI: [dismech:slot/negated](https://w3id.org/monarch-initiative/dismech/slot/negated)
Alias: negated

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
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
| self | dismech:negated |
| native | dismech:negated |




## LinkML Source

<details>
```yaml
name: negated
description: If true, this leaf criterion is negated (the constraint must NOT hold).
  An alternative to wrapping the node in a NOT operator.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: negated
domain_of:
- LogicalCriterion
range: boolean

```
</details>