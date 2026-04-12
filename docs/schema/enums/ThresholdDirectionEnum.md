# Enum: ThresholdDirectionEnum 




_Whether a threshold activates when the variable goes above or below the value_



URI: [dismech:enum/ThresholdDirectionEnum](https://w3id.org/monarch-initiative/dismech/enum/ThresholdDirectionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| above | None | Activates when the variable exceeds the threshold |
| below | None | Activates when the variable falls below the threshold |




## Slots

| Name | Description |
| ---  | --- |
| [threshold_direction](../slots/threshold_direction.md) | Whether the threshold activates when the variable goes above or below the val... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ThresholdDirectionEnum
description: Whether a threshold activates when the variable goes above or below the
  value
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  above:
    text: above
    description: Activates when the variable exceeds the threshold
  below:
    text: below
    description: Activates when the variable falls below the threshold

```
</details>