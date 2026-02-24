# Enum: AssociationSignalMethodEnum 




_Method used to derive an association signal_



URI: [dismech:AssociationSignalMethodEnum](https://w3id.org/monarch-initiative/dismech/AssociationSignalMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EHR_TEMPORAL_COMORBIDITY | None | EHR-derived temporal comorbidity/trajectory signal |
| EHR_COHORT_ASSOCIATION | None | EHR-derived cohort association (non-temporal) |
| LITERATURE_ASSOCIATION | None | Association reported in the literature |
| COMPUTATIONAL_INFERENCE | None | Computational inference or enrichment |
| OTHER | None | Other or unspecified method |




## Slots

| Name | Description |
| ---  | --- |
| [method](method.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AssociationSignalMethodEnum
description: Method used to derive an association signal
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  EHR_TEMPORAL_COMORBIDITY:
    text: EHR_TEMPORAL_COMORBIDITY
    description: EHR-derived temporal comorbidity/trajectory signal
  EHR_COHORT_ASSOCIATION:
    text: EHR_COHORT_ASSOCIATION
    description: EHR-derived cohort association (non-temporal)
  LITERATURE_ASSOCIATION:
    text: LITERATURE_ASSOCIATION
    description: Association reported in the literature
  COMPUTATIONAL_INFERENCE:
    text: COMPUTATIONAL_INFERENCE
    description: Computational inference or enrichment
  OTHER:
    text: OTHER
    description: Other or unspecified method

```
</details>