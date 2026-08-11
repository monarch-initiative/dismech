# Enum: FunctionalImpactEnum 




_Directional or qualitative functional consequence of a variant or genetic context._



URI: [dismech:enum/FunctionalImpactEnum](https://w3id.org/monarch-initiative/dismech/enum/FunctionalImpactEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| LOSS_OF_FUNCTION | None | Complete or partial reduction of normal gene product function | Title: Loss of function<br>|
| GAIN_OF_FUNCTION | None | Increased, novel, or constitutive gene product function | Title: Gain of function<br>|
| PARTIAL_LOSS_OF_FUNCTION | None | Hypomorphic reduction of normal gene product function | Title: Partial loss of function<br>|
| DOMINANT_NEGATIVE | None | Mutant product interferes with the remaining wild-type product | Title: Dominant negative<br>|
| HYPERMORPHIC | None | Increased normal gene product activity | Title: Hypermorphic<br>|
| NEOMORPHIC | None | Novel gene product activity not present in the wild type | Title: Neomorphic<br>|
| UNKNOWN | None | Functional impact is not known | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [functional_impact_category](../slots/functional_impact_category.md) | Controlled functional impact category for a genetic context |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: FunctionalImpactEnum
description: Directional or qualitative functional consequence of a variant or genetic
  context.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  LOSS_OF_FUNCTION:
    text: LOSS_OF_FUNCTION
    description: Complete or partial reduction of normal gene product function.
    title: Loss of function
  GAIN_OF_FUNCTION:
    text: GAIN_OF_FUNCTION
    description: Increased, novel, or constitutive gene product function.
    title: Gain of function
  PARTIAL_LOSS_OF_FUNCTION:
    text: PARTIAL_LOSS_OF_FUNCTION
    description: Hypomorphic reduction of normal gene product function.
    title: Partial loss of function
  DOMINANT_NEGATIVE:
    text: DOMINANT_NEGATIVE
    description: Mutant product interferes with the remaining wild-type product.
    title: Dominant negative
  HYPERMORPHIC:
    text: HYPERMORPHIC
    description: Increased normal gene product activity.
    title: Hypermorphic
  NEOMORPHIC:
    text: NEOMORPHIC
    description: Novel gene product activity not present in the wild type.
    title: Neomorphic
  UNKNOWN:
    text: UNKNOWN
    description: Functional impact is not known.
    title: Unknown

```
</details>