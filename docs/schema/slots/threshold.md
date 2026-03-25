

# Slot: threshold 


_Numeric threshold at which this mapping activates (e.g., a phenotype becomes clinically relevant when the variable crosses this value)._





URI: [dismech:slot/threshold](https://w3id.org/monarch-initiative/dismech/slot/threshold)
Alias: threshold

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  yes  |
| [SeverityTier](../classes/SeverityTier.md) | A threshold-severity pair defining one tier in a severity scale |  yes  |






## Properties

* Range: [Float](../types/Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:threshold |
| native | dismech:threshold |




## LinkML Source

<details>
```yaml
name: threshold
description: Numeric threshold at which this mapping activates (e.g., a phenotype
  becomes clinically relevant when the variable crosses this value).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: threshold
domain_of:
- SeverityTier
- ModelVariableDescriptor
range: float

```
</details>