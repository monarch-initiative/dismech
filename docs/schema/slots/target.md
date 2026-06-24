

# Slot: target 


_The name of the target element in a causal relationship_





URI: [dismech:slot/target](https://w3id.org/monarch-initiative/dismech/slot/target)
Alias: target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalEdge](../classes/CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  no  |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  yes  |
| [ModelMechanismLink](../classes/ModelMechanismLink.md) | Links an experimental model to a specific pathophysiology mechanism node, wit... |  yes  |
| [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  yes  |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [ExperimentalReadout](../classes/ExperimentalReadout.md), [CausalEdge](../classes/CausalEdge.md), [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md), [ModelMechanismLink](../classes/ModelMechanismLink.md), [BiomarkerReadout](../classes/BiomarkerReadout.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










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
- ExperimentalPerturbation
- ExperimentalReadout
- CausalEdge
- TreatmentMechanismTarget
- ModelMechanismLink
- BiomarkerReadout
range: string
required: true

```
</details>