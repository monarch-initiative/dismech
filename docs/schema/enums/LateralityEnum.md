# Enum: LateralityEnum 




_Laterality qualifier for anatomical structures or procedures_



URI: [dismech:enum/LateralityEnum](https://w3id.org/monarch-initiative/dismech/enum/LateralityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| LEFT | None | Left side of the body | Title: Left<br>|
| RIGHT | None | Right side of the body | Title: Right<br>|
| BILATERAL | None | Both sides of the body | Title: Bilateral<br>|




## Slots

| Name | Description |
| ---  | --- |
| [laterality](../slots/laterality.md) | Laterality qualifier (left, right, or bilateral) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: LateralityEnum
description: Laterality qualifier for anatomical structures or procedures
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  LEFT:
    text: LEFT
    description: Left side of the body
    title: Left
  RIGHT:
    text: RIGHT
    description: Right side of the body
    title: Right
  BILATERAL:
    text: BILATERAL
    description: Both sides of the body
    title: Bilateral

```
</details>