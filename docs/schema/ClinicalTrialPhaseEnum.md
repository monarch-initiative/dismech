# Enum: ClinicalTrialPhaseEnum 




_Clinical trial phase categories per FDA/NIH standards_



URI: [dismech:ClinicalTrialPhaseEnum](https://w3id.org/monarch-initiative/dismech/ClinicalTrialPhaseEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PHASE_I | None | Phase I - Initial safety and dosage assessment in small group (20-100 partici... |
| PHASE_II | None | Phase II - Efficacy and side effects assessment in larger group (100-500 part... |
| PHASE_III | None | Phase III - Efficacy confirmation and monitoring in large population (1000-50... |
| PHASE_IV | None | Phase IV - Post-market surveillance and additional benefits/risks studies |
| NOT_APPLICABLE | None | Trial does not follow standard FDA phase classification (e |




## Slots

| Name | Description |
| ---  | --- |
| [phase](phase.md) | Trial phase (Phase I, Phase II, Phase III, Phase IV, or Not Applicable) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalTrialPhaseEnum
description: Clinical trial phase categories per FDA/NIH standards
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PHASE_I:
    text: PHASE_I
    description: Phase I - Initial safety and dosage assessment in small group (20-100
      participants)
  PHASE_II:
    text: PHASE_II
    description: Phase II - Efficacy and side effects assessment in larger group (100-500
      participants)
  PHASE_III:
    text: PHASE_III
    description: Phase III - Efficacy confirmation and monitoring in large population
      (1000-5000 participants)
  PHASE_IV:
    text: PHASE_IV
    description: Phase IV - Post-market surveillance and additional benefits/risks
      studies
  NOT_APPLICABLE:
    text: NOT_APPLICABLE
    description: Trial does not follow standard FDA phase classification (e.g., observational,
      device studies)

```
</details>