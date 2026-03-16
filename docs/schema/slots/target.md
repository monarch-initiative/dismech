

# Slot: target 


_The name of the target element in a causal relationship_





URI: [dismech:slot/target](https://w3id.org/monarch-initiative/dismech/slot/target)
Alias: target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  yes  |
| [CausalEdge](../classes/CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:target |
| native | dismech:target |




## LinkML Source

<details>
```yaml
name: target
description: The name of the target element in a causal relationship
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: target
domain_of:
- CausalEdge
- TreatmentMechanismTarget
range: string
required: true

```
</details>