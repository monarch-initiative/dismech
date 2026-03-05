# Enum: AssociationMetricTypeEnum 




_Type of association metric_



URI: [dismech:AssociationMetricTypeEnum](https://w3id.org/monarch-initiative/dismech/AssociationMetricTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| OR | None | Odds ratio |
| AOR | None | Adjusted odds ratio |
| RR | None | Relative risk |
| HR | None | Hazard ratio |
| PREVALENCE | None | Prevalence proportion |
| INCIDENCE_RATE | None | Incidence rate |
| IRR | None | Incidence rate ratio |
| CHI_SQUARE | None | Chi-square association statistic |
| LOG_OBS_EXP_RATIO | None | Natural-log observed-to-expected co-occurrence ratio |
| OTHER | None | Other or unspecified metric |




## Slots

| Name | Description |
| ---  | --- |
| [metric_type](metric_type.md) | Metric type (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AssociationMetricTypeEnum
description: Type of association metric
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  OR:
    text: OR
    description: Odds ratio
  AOR:
    text: AOR
    description: Adjusted odds ratio
  RR:
    text: RR
    description: Relative risk
  HR:
    text: HR
    description: Hazard ratio
  PREVALENCE:
    text: PREVALENCE
    description: Prevalence proportion
  INCIDENCE_RATE:
    text: INCIDENCE_RATE
    description: Incidence rate
  IRR:
    text: IRR
    description: Incidence rate ratio
  CHI_SQUARE:
    text: CHI_SQUARE
    description: Chi-square association statistic
  LOG_OBS_EXP_RATIO:
    text: LOG_OBS_EXP_RATIO
    description: Natural-log observed-to-expected co-occurrence ratio
  OTHER:
    text: OTHER
    description: Other or unspecified metric

```
</details>