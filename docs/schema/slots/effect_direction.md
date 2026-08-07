

# Slot: effect_direction 


_The sign of the association - whether one condition raises (RISK) or lowers (PROTECTIVE) the risk/incidence/severity of the other, is context-dependent (MIXED), null, or unknown. Orthogonal to `directionality` (temporal ordering). Defaults conceptually to RISK for conventional comorbidities; set PROTECTIVE for inverse associations such as the cancer/Alzheimer's-disease paradox._





URI: [dismech:slot/effect_direction](https://w3id.org/monarch-initiative/dismech/slot/effect_direction)
Alias: effect_direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ComorbidityEffectDirectionEnum](../enums/ComorbidityEffectDirectionEnum.md) |
| Domain Of | [ComorbidityAssociation](../classes/ComorbidityAssociation.md), [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:effect_direction |
| native | dismech:effect_direction |




## LinkML Source

<details>
```yaml
name: effect_direction
description: The sign of the association - whether one condition raises (RISK) or
  lowers (PROTECTIVE) the risk/incidence/severity of the other, is context-dependent
  (MIXED), null, or unknown. Orthogonal to `directionality` (temporal ordering). Defaults
  conceptually to RISK for conventional comorbidities; set PROTECTIVE for inverse
  associations such as the cancer/Alzheimer's-disease paradox.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: effect_direction
domain_of:
- ComorbidityAssociation
- AssociationSignal
range: ComorbidityEffectDirectionEnum

```
</details>