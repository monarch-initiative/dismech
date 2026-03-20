

# Slot: severity_scale 


_Ordered list of severity tiers, each a value-label pair. For "above" direction, higher values mean greater severity; for "below", lower values mean greater severity._





URI: [dismech:slot/severity_scale](https://w3id.org/monarch-initiative/dismech/slot/severity_scale)
Alias: severity_scale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, ... |  yes  |






## Properties

* Range: [SeverityTier](../classes/SeverityTier.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:severity_scale |
| native | dismech:severity_scale |




## LinkML Source

<details>
```yaml
name: severity_scale
description: Ordered list of severity tiers, each a value-label pair. For "above"
  direction, higher values mean greater severity; for "below", lower values mean greater
  severity.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: severity_scale
domain_of:
- ModelVariableDescriptor
range: SeverityTier
multivalued: true
inlined: true
inlined_as_list: true

```
</details>