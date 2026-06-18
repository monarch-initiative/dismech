# Enum: SurrogateEndpointValidationLevelEnum 




_BEST-aligned regulatory validation level inferred or curated for a surrogate endpoint_



URI: [dismech:enum/SurrogateEndpointValidationLevelEnum](https://w3id.org/monarch-initiative/dismech/enum/SurrogateEndpointValidationLevelEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| VALIDATED_SURROGATE_ENDPOINT | None | Supported by clinical data providing strong evidence that the endpoint predic... | Title: Validated surrogate endpoint<br>|
| REASONABLY_LIKELY_SURROGATE_ENDPOINT | None | Supported by strong mechanistic and/or epidemiologic rationale, but without s... | Title: Reasonably likely surrogate endpoint<br>|
| CONTEXT_DEPENDENT_SURROGATE_ENDPOINT | None | Validation and approval pathway depend on context of use, disease setting, ef... | Title: Context-dependent surrogate endpoint<br>|




## Slots

| Name | Description |
| ---  | --- |
| [endpoint_validation_level](../slots/endpoint_validation_level.md) | BEST-aligned validation level inferred or curated for the surrogate endpoint |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SurrogateEndpointValidationLevelEnum
description: BEST-aligned regulatory validation level inferred or curated for a surrogate
  endpoint
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  VALIDATED_SURROGATE_ENDPOINT:
    text: VALIDATED_SURROGATE_ENDPOINT
    description: Supported by clinical data providing strong evidence that the endpoint
      predicts clinical benefit
    title: Validated surrogate endpoint
  REASONABLY_LIKELY_SURROGATE_ENDPOINT:
    text: REASONABLY_LIKELY_SURROGATE_ENDPOINT
    description: Supported by strong mechanistic and/or epidemiologic rationale, but
      without sufficient clinical validation for full surrogate validation
    title: Reasonably likely surrogate endpoint
  CONTEXT_DEPENDENT_SURROGATE_ENDPOINT:
    text: CONTEXT_DEPENDENT_SURROGATE_ENDPOINT
    description: Validation and approval pathway depend on context of use, disease
      setting, effect size, duration, residual uncertainty, and available therapy
    title: Context-dependent surrogate endpoint

```
</details>