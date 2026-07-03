

# Slot: perturbations 


_Gene knockouts, reaction deletions, or parameter changes modeling the disease_





URI: [dismech:slot/perturbations](https://w3id.org/monarch-initiative/dismech/slot/perturbations)
Alias: perturbations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  yes  |
| [ExperimentalControl](../classes/ExperimentalControl.md) | A comparator or control condition for an experiment, such as an isogenic wild... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneDescriptor](../classes/GeneDescriptor.md) |
| Domain Of | [Experiment](../classes/Experiment.md), [ExperimentalControl](../classes/ExperimentalControl.md), [ComputationalModel](../classes/ComputationalModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:perturbations |
| native | dismech:perturbations |




## LinkML Source

<details>
```yaml
name: perturbations
description: Gene knockouts, reaction deletions, or parameter changes modeling the
  disease
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: perturbations
domain_of:
- Experiment
- ExperimentalControl
- ComputationalModel
range: GeneDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>