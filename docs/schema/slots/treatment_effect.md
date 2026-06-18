

# Slot: treatment_effect 


_How the treatment affects the targeted mechanism_





URI: [dismech:slot/treatment_effect](https://w3id.org/monarch-initiative/dismech/slot/treatment_effect)
Alias: treatment_effect

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TreatmentEffectEnum](../enums/TreatmentEffectEnum.md) |
| Domain Of | [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:treatment_effect |
| native | dismech:treatment_effect |




## LinkML Source

<details>
```yaml
name: treatment_effect
description: How the treatment affects the targeted mechanism
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: treatment_effect
domain_of:
- TreatmentMechanismTarget
range: TreatmentEffectEnum

```
</details>