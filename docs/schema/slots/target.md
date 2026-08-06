

# Slot: target 


_The name of the target element in a causal relationship_





URI: [dismech:slot/target](https://w3id.org/monarch-initiative/dismech/slot/target)
Alias: target

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  yes  |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |
| [CausalEdge](../classes/CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  no  |
| [PhenotypeReadout](../classes/PhenotypeReadout.md) | Links an investigation-readout phenotype (an abnormal electrophysiology, func... |  yes  |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  yes  |
| [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  yes  |
| [ModelMechanismLink](../classes/ModelMechanismLink.md) | Links an experimental model to a specific pathophysiology mechanism node, wit... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [ExperimentalReadout](../classes/ExperimentalReadout.md), [CausalEdge](../classes/CausalEdge.md), [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md), [ModelMechanismLink](../classes/ModelMechanismLink.md), [BiomarkerReadout](../classes/BiomarkerReadout.md), [PhenotypeReadout](../classes/PhenotypeReadout.md) |

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
- PhenotypeReadout
range: string
required: true

```
</details>