# Enum: DietaryModificationActionEnum 




_Action applied to a food or beverage as part of a dietary treatment_



URI: [dismech:enum/DietaryModificationActionEnum](https://w3id.org/monarch-initiative/dismech/enum/DietaryModificationActionEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ADD | None | Increase intake or deliberately include the specified food or beverage | Title: Add<br>|
| RESTRICT | None | Limit intake of the specified food or beverage without full elimination | Title: Restrict<br>|
| AVOID | None | Eliminate or strictly avoid the specified food or beverage | Title: Avoid<br>|
| SUBSTITUTE | None | Use the specified food or beverage as a replacement within a dietary regimen | Title: Substitute<br>|




## Slots

| Name | Description |
| ---  | --- |
| [action](../slots/action.md) | The dietary action being applied |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DietaryModificationActionEnum
description: Action applied to a food or beverage as part of a dietary treatment
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ADD:
    text: ADD
    description: Increase intake or deliberately include the specified food or beverage
    title: Add
  RESTRICT:
    text: RESTRICT
    description: Limit intake of the specified food or beverage without full elimination
    title: Restrict
  AVOID:
    text: AVOID
    description: Eliminate or strictly avoid the specified food or beverage
    title: Avoid
  SUBSTITUTE:
    text: SUBSTITUTE
    description: Use the specified food or beverage as a replacement within a dietary
      regimen
    title: Substitute

```
</details>