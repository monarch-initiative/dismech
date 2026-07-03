# Enum: BiomarkerReadoutRelationshipEnum 




_Relationship between a biomarker and the pathograph node it reports on_



URI: [dismech:enum/BiomarkerReadoutRelationshipEnum](https://w3id.org/monarch-initiative/dismech/enum/BiomarkerReadoutRelationshipEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| READOUT_OF | None | The biomarker directly or indirectly measures the linked event or mechanism | Title: Readout of<br>|
| CORRELATES_WITH | None | The biomarker is statistically or clinically associated with the linked event... | Title: Correlates with<br>|
| PREDICTS | None | The biomarker predicts a later event, endpoint, or clinical outcome | Title: Predicts<br>|
| PHARMACODYNAMIC_MARKER_OF | None | The biomarker reports biological response to a treatment or intervention at t... | Title: Pharmacodynamic marker of<br>|




## Slots

| Name | Description |
| ---  | --- |
| [relationship](../slots/relationship.md) | Controlled relationship between a biomarker and the pathograph node it report... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: BiomarkerReadoutRelationshipEnum
description: Relationship between a biomarker and the pathograph node it reports on
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  READOUT_OF:
    text: READOUT_OF
    description: The biomarker directly or indirectly measures the linked event or
      mechanism
    title: Readout of
  CORRELATES_WITH:
    text: CORRELATES_WITH
    description: The biomarker is statistically or clinically associated with the
      linked event or endpoint
    title: Correlates with
  PREDICTS:
    text: PREDICTS
    description: The biomarker predicts a later event, endpoint, or clinical outcome
    title: Predicts
  PHARMACODYNAMIC_MARKER_OF:
    text: PHARMACODYNAMIC_MARKER_OF
    description: The biomarker reports biological response to a treatment or intervention
      at the linked node
    title: Pharmacodynamic marker of

```
</details>