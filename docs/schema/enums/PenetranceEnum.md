# Enum: PenetranceEnum 




_Penetrance classification for inheritance_



URI: [dismech:enum/PenetranceEnum](https://w3id.org/monarch-initiative/dismech/enum/PenetranceEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| COMPLETE | None | All individuals with the variant express the phenotype | Title: Complete<br>|
| INCOMPLETE | None | Not all individuals with the variant express the phenotype | Title: Incomplete<br>|
| UNKNOWN | None | Penetrance has not been determined | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [penetrance](../slots/penetrance.md) | Penetrance classification for this inheritance pattern |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: PenetranceEnum
description: Penetrance classification for inheritance
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  COMPLETE:
    text: COMPLETE
    description: All individuals with the variant express the phenotype
    title: Complete
  INCOMPLETE:
    text: INCOMPLETE
    description: Not all individuals with the variant express the phenotype
    title: Incomplete
  UNKNOWN:
    text: UNKNOWN
    description: Penetrance has not been determined
    title: Unknown

```
</details>