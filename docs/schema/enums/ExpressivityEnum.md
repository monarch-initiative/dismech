# Enum: ExpressivityEnum 




_Expressivity classification for inheritance_



URI: [dismech:enum/ExpressivityEnum](https://w3id.org/monarch-initiative/dismech/enum/ExpressivityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| VARIABLE | None | Phenotype severity or features vary among individuals with the same variant | Title: Variable<br>|
| CONSISTENT | None | Phenotype is uniform among individuals with the same variant | Title: Consistent<br>|
| UNKNOWN | None | Expressivity has not been determined | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [expressivity](../slots/expressivity.md) | Expressivity classification for this inheritance pattern |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ExpressivityEnum
description: Expressivity classification for inheritance
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  VARIABLE:
    text: VARIABLE
    description: Phenotype severity or features vary among individuals with the same
      variant
    title: Variable
  CONSISTENT:
    text: CONSISTENT
    description: Phenotype is uniform among individuals with the same variant
    title: Consistent
  UNKNOWN:
    text: UNKNOWN
    description: Expressivity has not been determined
    title: Unknown

```
</details>