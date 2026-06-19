# Enum: LogicalOperatorEnum 




_Boolean operator for a branch node in a nested membership-criteria expression (LogicalCriterion). Branch nodes set an operator and combine child operands; leaf nodes set a criterion_predicate instead._



URI: [dismech:enum/LogicalOperatorEnum](https://w3id.org/monarch-initiative/dismech/enum/LogicalOperatorEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| AND | None | All operands must hold (conjunction) |
| OR | None | At least one operand must hold (disjunction) |
| NOT | None | Negation |




## Slots

| Name | Description |
| ---  | --- |
| [operator](../slots/operator.md) | Boolean operator for a branch node in a membership-criteria expression |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: LogicalOperatorEnum
description: Boolean operator for a branch node in a nested membership-criteria expression
  (LogicalCriterion). Branch nodes set an operator and combine child operands; leaf
  nodes set a criterion_predicate instead.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  AND:
    text: AND
    description: All operands must hold (conjunction).
  OR:
    text: OR
    description: At least one operand must hold (disjunction).
  NOT:
    text: NOT
    description: Negation. Conventionally applied to a single operand (or to the conjunction
      of its operands).

```
</details>