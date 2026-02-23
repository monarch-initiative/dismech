# Enum: ComorbidityDirectionEnum 




_Directionality of a comorbidity/trajectory association_



URI: [dismech:ComorbidityDirectionEnum](https://w3id.org/monarch-initiative/dismech/ComorbidityDirectionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| A_BEFORE_B | None | A precedes B |
| B_BEFORE_A | None | B precedes A |
| BIDIRECTIONAL | None | Evidence supports both directions |
| SAME_TIME | None | Co-incident or same-time association |
| UNKNOWN | None | Directionality is unknown or not established |




## Slots

| Name | Description |
| ---  | --- |
| [directionality](directionality.md) | Direction of a comorbidity/trajectory association |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ComorbidityDirectionEnum
description: Directionality of a comorbidity/trajectory association
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  A_BEFORE_B:
    text: A_BEFORE_B
    description: A precedes B
  B_BEFORE_A:
    text: B_BEFORE_A
    description: B precedes A
  BIDIRECTIONAL:
    text: BIDIRECTIONAL
    description: Evidence supports both directions
  SAME_TIME:
    text: SAME_TIME
    description: Co-incident or same-time association
  UNKNOWN:
    text: UNKNOWN
    description: Directionality is unknown or not established

```
</details>