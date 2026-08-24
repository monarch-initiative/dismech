# Enum: ComorbidityEffectDirectionEnum 




_The sign (effect direction) of a comorbidity/trajectory association - whether the presence of one condition raises or lowers the risk, incidence, or severity of the other. This is orthogonal to ComorbidityDirectionEnum, which captures only the temporal ordering (which condition comes first), not whether the effect is positive or inverse. A conventional risk comorbidity (A increases risk of B) is RISK; the cancer/Alzheimer's-disease inverse correlation is PROTECTIVE._



URI: [dismech:enum/ComorbidityEffectDirectionEnum](https://w3id.org/monarch-initiative/dismech/enum/ComorbidityEffectDirectionEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| RISK | None | Positive association: the presence of one condition increases the risk, incid... | Title: Risk (positive) association<br>|
| PROTECTIVE | None | Inverse association: the presence of one condition is associated with a reduc... | Title: Protective (inverse) association<br>|
| MIXED | None | The effect direction is not uniform: it is protective in some contexts (subty... | Title: Mixed / direction-dependent association<br>|
| NO_ASSOCIATION | None | Evidence indicates no significant association in either direction (a null res... | Title: No association<br>|
| UNKNOWN | None | The effect direction (risk vs ||




## Slots

| Name | Description |
| ---  | --- |
| [effect_direction](../slots/effect_direction.md) | The sign of the association - whether one condition raises (RISK) or lowers (... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ComorbidityEffectDirectionEnum
description: The sign (effect direction) of a comorbidity/trajectory association -
  whether the presence of one condition raises or lowers the risk, incidence, or severity
  of the other. This is orthogonal to ComorbidityDirectionEnum, which captures only
  the temporal ordering (which condition comes first), not whether the effect is positive
  or inverse. A conventional risk comorbidity (A increases risk of B) is RISK; the
  cancer/Alzheimer's-disease inverse correlation is PROTECTIVE.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  RISK:
    text: RISK
    description: 'Positive association: the presence of one condition increases the
      risk, incidence, or severity of the other. This is the conventional comorbidity
      direction and the default for most curated pairs.'
    title: Risk (positive) association
  PROTECTIVE:
    text: PROTECTIVE
    description: 'Inverse association: the presence of one condition is associated
      with a reduced risk or incidence of the other (e.g., the reciprocal cancer/Alzheimer''s-disease
      inverse correlation, atopy and glioma, balancing-selection heterozygote advantage).
      Quantitatively an odds ratio / hazard ratio / relative risk below 1.'
    title: Protective (inverse) association
  MIXED:
    text: MIXED
    description: 'The effect direction is not uniform: it is protective in some contexts
      (subtype, direction, population) and risk-conferring in others (e.g., Parkinson''s
      disease shows an inverse association with most cancers but a positive association
      with melanoma). Use the per-signal effect_direction and notes to record the
      split.'
    title: Mixed / direction-dependent association
  NO_ASSOCIATION:
    text: NO_ASSOCIATION
    description: Evidence indicates no significant association in either direction
      (a null result). Useful for recording examined-but-refuted pairs.
    title: No association
  UNKNOWN:
    text: UNKNOWN
    description: The effect direction (risk vs. protective) has not been established.

```
</details>