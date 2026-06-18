

# Slot: controls 


_Experimental controls, comparators, or counterfactual arms_





URI: [dismech:slot/controls](https://w3id.org/monarch-initiative/dismech/slot/controls)
Alias: controls

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExperimentalControl](../classes/ExperimentalControl.md) |
| Domain Of | [Experiment](../classes/Experiment.md) |

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
| self | dismech:controls |
| native | dismech:controls |




## LinkML Source

<details>
```yaml
name: controls
description: Experimental controls, comparators, or counterfactual arms
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: controls
domain_of:
- Experiment
range: ExperimentalControl
multivalued: true
inlined: true
inlined_as_list: true

```
</details>