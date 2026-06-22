# Enum: BiomarkerReadoutDirectionEnum 




_Direction of association between biomarker value/presence and the linked event or endpoint_



URI: [dismech:enum/BiomarkerReadoutDirectionEnum](https://w3id.org/monarch-initiative/dismech/enum/BiomarkerReadoutDirectionEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| POSITIVE | None | Higher biomarker value or stronger presence tracks with more of the linked ev... | Title: Positive<br>|
| NEGATIVE | None | Higher biomarker value or stronger presence tracks with less of the linked ev... | Title: Negative<br>|
| PRESENT_ABSENT | None | Biomarker presence or absence, rather than monotonic level, is the interpreta... | Title: Present/absent<br>|
| THRESHOLD_DEPENDENT | None | Interpretation depends on threshold, range, genotype, assay, or clinical cont... | Title: Threshold dependent<br>|




## Slots

| Name | Description |
| ---  | --- |
| [direction](../slots/direction.md) | Direction of association between the biomarker value/presence and the linked ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: BiomarkerReadoutDirectionEnum
description: Direction of association between biomarker value/presence and the linked
  event or endpoint
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  POSITIVE:
    text: POSITIVE
    description: Higher biomarker value or stronger presence tracks with more of the
      linked event
    title: Positive
  NEGATIVE:
    text: NEGATIVE
    description: Higher biomarker value or stronger presence tracks with less of the
      linked event
    title: Negative
  PRESENT_ABSENT:
    text: PRESENT_ABSENT
    description: Biomarker presence or absence, rather than monotonic level, is the
      interpretable signal
    title: Present/absent
  THRESHOLD_DEPENDENT:
    text: THRESHOLD_DEPENDENT
    description: Interpretation depends on threshold, range, genotype, assay, or clinical
      context
    title: Threshold dependent

```
</details>