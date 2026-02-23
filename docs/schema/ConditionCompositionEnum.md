# Enum: ConditionCompositionEnum 




_Composition type for a composite condition descriptor_



URI: [dismech:ConditionCompositionEnum](https://w3id.org/monarch-initiative/dismech/ConditionCompositionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SINGLE | None | Single condition (default) |
| UNION | None | Union of multiple component conditions |
| CATEGORY | None | Category code encompassing multiple conditions |
| OVERLAPS | None | Overlapping condition set (non-exhaustive) |
| SUBSET_OF | None | Subset of a broader condition group |
| OTHER | None | Other or unspecified composition |




## Slots

| Name | Description |
| ---  | --- |
| [composition](composition.md) | Composition type for a composite condition descriptor |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ConditionCompositionEnum
description: Composition type for a composite condition descriptor
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  SINGLE:
    text: SINGLE
    description: Single condition (default)
  UNION:
    text: UNION
    description: Union of multiple component conditions
  CATEGORY:
    text: CATEGORY
    description: Category code encompassing multiple conditions
  OVERLAPS:
    text: OVERLAPS
    description: Overlapping condition set (non-exhaustive)
  SUBSET_OF:
    text: SUBSET_OF
    description: Subset of a broader condition group
  OTHER:
    text: OTHER
    description: Other or unspecified composition

```
</details>