# Enum: ModifierEnum 




_Qualifiers for direction, intensity, or pathological state of a descriptor_



URI: [dismech:enum/ModifierEnum](https://w3id.org/monarch-initiative/dismech/enum/ModifierEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| INCREASED | None | Upregulated, hyperactive, elevated, or excessive | Title: Increased<br>|
| DECREASED | None | Downregulated, hypoactive, reduced, or deficient | Title: Decreased<br>|
| ABNORMAL | None | Qualitatively abnormal (e | Title: Abnormal<br>|
| DYSREGULATED | None | Regulation is impaired (may be increased or decreased) | Title: Dysregulated<br>|
| ABSENT | None | Not occurring or not present | Title: Absent<br>|




## Slots

| Name | Description |
| ---  | --- |
| [modifier](../slots/modifier.md) | Directional or qualitative modifier for a descriptor (e |










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
    title: Increased
  DECREASED:
    text: DECREASED
    description: Downregulated, hypoactive, reduced, or deficient
    title: Decreased
  ABNORMAL:
    text: ABNORMAL
    description: Qualitatively abnormal (e.g., misfolding, mislocalization, malformed)
    title: Abnormal
  DYSREGULATED:
    text: DYSREGULATED
    description: Regulation is impaired (may be increased or decreased)
    title: Dysregulated
  ABSENT:
    text: ABSENT
    description: Not occurring or not present
    title: Absent

```
</details>