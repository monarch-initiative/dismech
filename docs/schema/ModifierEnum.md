# Enum: ModifierEnum 




_Qualifiers for direction, intensity, or pathological state of a descriptor_



URI: [dismech:ModifierEnum](https://w3id.org/monarch-initiative/dismech/ModifierEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| INCREASED | None | Upregulated, hyperactive, elevated, or excessive |
| DECREASED | None | Downregulated, hypoactive, reduced, or deficient |
| ABNORMAL | None | Qualitatively abnormal (e |
| DYSREGULATED | None | Regulation is impaired (may be increased or decreased) |
| ABSENT | None | Not occurring or not present |




## Slots

| Name | Description |
| ---  | --- |
| [modifier](modifier.md) | Directional or qualitative modifier for a descriptor (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ModifierEnum
description: Qualifiers for direction, intensity, or pathological state of a descriptor
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  INCREASED:
    text: INCREASED
    description: Upregulated, hyperactive, elevated, or excessive
  DECREASED:
    text: DECREASED
    description: Downregulated, hypoactive, reduced, or deficient
  ABNORMAL:
    text: ABNORMAL
    description: Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
  DYSREGULATED:
    text: DYSREGULATED
    description: Regulation is impaired (may be increased or decreased)
  ABSENT:
    text: ABSENT
    description: Not occurring or not present

```
</details>