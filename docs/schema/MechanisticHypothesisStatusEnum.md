# Enum: MechanisticHypothesisStatusEnum 




_Curation/maturity status for a disease-level mechanistic hypothesis_



URI: [dismech:MechanisticHypothesisStatusEnum](https://w3id.org/monarch-initiative/dismech/MechanisticHypothesisStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CANONICAL | None | Widely accepted explanatory model used as the default disease mechanism |
| ALTERNATIVE | None | Plausible competing or superimposed hypothesis with supporting evidence |
| EMERGING | None | Early-stage hypothesis with limited or recently reported evidence |
| DEPRECATED | None | Historical hypothesis no longer supported as the current model |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: MechanisticHypothesisStatusEnum
description: Curation/maturity status for a disease-level mechanistic hypothesis
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CANONICAL:
    text: CANONICAL
    description: Widely accepted explanatory model used as the default disease mechanism
  ALTERNATIVE:
    text: ALTERNATIVE
    description: Plausible competing or superimposed hypothesis with supporting evidence
  EMERGING:
    text: EMERGING
    description: Early-stage hypothesis with limited or recently reported evidence
  DEPRECATED:
    text: DEPRECATED
    description: Historical hypothesis no longer supported as the current model

```
</details>