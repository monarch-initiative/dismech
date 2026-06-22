

# Slot: model_systems 


_Experimental model systems used or proposed for an experiment, using the ExperimentalModel pattern and optional NAMO alignment._





URI: [dismech:slot/model_systems](https://w3id.org/monarch-initiative/dismech/slot/model_systems)
Alias: model_systems

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  no  |
| [ExperimentalControl](../classes/ExperimentalControl.md) | A comparator or control condition for an experiment, such as an isogenic wild... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExperimentalModel](../classes/ExperimentalModel.md) |
| Domain Of | [Experiment](../classes/Experiment.md), [ExperimentalControl](../classes/ExperimentalControl.md) |

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
| self | dismech:model_systems |
| native | dismech:model_systems |




## LinkML Source

<details>
```yaml
name: model_systems
description: Experimental model systems used or proposed for an experiment, using
  the ExperimentalModel pattern and optional NAMO alignment.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: model_systems
domain_of:
- Experiment
- ExperimentalControl
range: ExperimentalModel
multivalued: true
inlined: true
inlined_as_list: true

```
</details>