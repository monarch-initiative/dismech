# Enum: AlgorithmValidationStatusEnum 




_Validation maturity of a phenotype algorithm / computable case definition._



URI: [dismech:enum/AlgorithmValidationStatusEnum](https://w3id.org/monarch-initiative/dismech/enum/AlgorithmValidationStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| PROPOSED | None | Drafted; never executed against data |
| UNVALIDATED | None | Executable but not yet evaluated against a gold-standard or labeled cohort |
| VALIDATED_AGAINST_GOLD_STANDARD | None | PPV/sensitivity characterized against a reference standard |




## Slots

| Name | Description |
| ---  | --- |
| [status](../slots/status.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AlgorithmValidationStatusEnum
description: Validation maturity of a phenotype algorithm / computable case definition.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PROPOSED:
    text: PROPOSED
    description: Drafted; never executed against data.
  UNVALIDATED:
    text: UNVALIDATED
    description: Executable but not yet evaluated against a gold-standard or labeled
      cohort.
  VALIDATED_AGAINST_GOLD_STANDARD:
    text: VALIDATED_AGAINST_GOLD_STANDARD
    description: PPV/sensitivity characterized against a reference standard.

```
</details>