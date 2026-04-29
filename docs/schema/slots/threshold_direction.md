

# Slot: threshold_direction 


_Whether the threshold activates when the variable goes above or below the value._





URI: [dismech:slot/threshold_direction](https://w3id.org/monarch-initiative/dismech/slot/threshold_direction)
Alias: threshold_direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  yes  |






## Properties

* Range: [ThresholdDirectionEnum](../enums/ThresholdDirectionEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:threshold_direction |
| native | dismech:threshold_direction |




## LinkML Source

<details>
```yaml
name: threshold_direction
description: Whether the threshold activates when the variable goes above or below
  the value.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: threshold_direction
domain_of:
- ModelVariableDescriptor
range: ThresholdDirectionEnum

```
</details>