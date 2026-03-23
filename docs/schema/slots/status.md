

# Slot: status 


_Status or state of a clinical trial or other process_





URI: [dismech:slot/status](https://w3id.org/monarch-initiative/dismech/slot/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [MechanisticHypothesis](../classes/MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  yes  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| Recruiting |
| Completed |
| Terminated |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:status |
| native | dismech:status |




## LinkML Source

<details>
```yaml
name: status
description: Status or state of a clinical trial or other process
examples:
- value: Recruiting
- value: Completed
- value: Terminated
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: status
domain_of:
- ClinicalTrial
- MechanisticHypothesis
range: string

```
</details>