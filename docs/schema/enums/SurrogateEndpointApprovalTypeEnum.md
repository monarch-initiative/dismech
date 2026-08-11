# Enum: SurrogateEndpointApprovalTypeEnum 




_Regulatory approval pathway context represented in the FDA surrogate endpoint table_



URI: [dismech:enum/SurrogateEndpointApprovalTypeEnum](https://w3id.org/monarch-initiative/dismech/enum/SurrogateEndpointApprovalTypeEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ACCELERATED | None | Endpoint may support accelerated approval in the curated context | Title: Accelerated<br>|
| TRADITIONAL | None | Endpoint may support traditional approval in the curated context | Title: Traditional<br>|
| ACCELERATED_OR_TRADITIONAL | None | Endpoint may support accelerated or traditional approval depending on context... | Title: Accelerated or traditional<br>|
| TRADITIONAL_AND_MONOGRAPH | None | Endpoint appears in FDA table as traditional and monograph | Title: Traditional and monograph<br>|




## Slots

| Name | Description |
| ---  | --- |
| [approval_type](../slots/approval_type.md) | FDA approval pathway context for the surrogate endpoint row |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SurrogateEndpointApprovalTypeEnum
description: Regulatory approval pathway context represented in the FDA surrogate
  endpoint table
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ACCELERATED:
    text: ACCELERATED
    description: Endpoint may support accelerated approval in the curated context
    title: Accelerated
  TRADITIONAL:
    text: TRADITIONAL
    description: Endpoint may support traditional approval in the curated context
    title: Traditional
  ACCELERATED_OR_TRADITIONAL:
    text: ACCELERATED_OR_TRADITIONAL
    description: Endpoint may support accelerated or traditional approval depending
      on context of use
    title: Accelerated or traditional
  TRADITIONAL_AND_MONOGRAPH:
    text: TRADITIONAL_AND_MONOGRAPH
    description: Endpoint appears in FDA table as traditional and monograph
    title: Traditional and monograph

```
</details>