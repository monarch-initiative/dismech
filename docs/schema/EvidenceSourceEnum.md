# Enum: EvidenceSourceEnum 




_The provenance/source of the evidence item_



URI: [dismech:EvidenceSourceEnum](https://w3id.org/monarch-initiative/dismech/EvidenceSourceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| HUMAN_CLINICAL | None | Human clinical observations (patients, cohorts, case reports, clinical trials... |
| MODEL_ORGANISM | None | In vivo animal evidence (mouse, zebrafish, primate, veterinary case series in... |
| IN_VITRO | None | In vitro or ex vivo assays (cell culture, organoids, tissue slices, biochemic... |
| COMPUTATIONAL | None | In silico/modeling studies (simulation, docking, ML predictions, network infe... |
| OTHER | None | Evidence not fitting the above (e |




## Slots

| Name | Description |
| ---  | --- |
| [evidence_source](evidence_source.md) | Origin of the evidence item (human clinical, model organism, in vitro, or com... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: EvidenceSourceEnum
description: The provenance/source of the evidence item
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  HUMAN_CLINICAL:
    text: HUMAN_CLINICAL
    description: Human clinical observations (patients, cohorts, case reports, clinical
      trials, epidemiology)
  MODEL_ORGANISM:
    text: MODEL_ORGANISM
    description: In vivo animal evidence (mouse, zebrafish, primate, veterinary case
      series including dog/cat/horse, other non-human animal models etc.)
  IN_VITRO:
    text: IN_VITRO
    description: In vitro or ex vivo assays (cell culture, organoids, tissue slices,
      biochemical assays)
  COMPUTATIONAL:
    text: COMPUTATIONAL
    description: In silico/modeling studies (simulation, docking, ML predictions,
      network inference) even when using clinical data inputs
  OTHER:
    text: OTHER
    description: Evidence not fitting the above (e.g., expert consensus without data,
      image atlases without cohort context)

```
</details>