

# Slot: experiment_type 


_Ontology-backed descriptor for the overall experiment or study design. Prefer OBI terms when available; assay-level details should go in the `assays` slot._





URI: [dismech:slot/experiment_type](https://w3id.org/monarch-initiative/dismech/slot/experiment_type)
Alias: experiment_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Descriptor](../classes/Descriptor.md) |
| Domain Of | [Experiment](../classes/Experiment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:experiment_type |
| native | dismech:experiment_type |




## LinkML Source

<details>
```yaml
name: experiment_type
description: Ontology-backed descriptor for the overall experiment or study design.
  Prefer OBI terms when available; assay-level details should go in the `assays` slot.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: experiment_type
domain_of:
- Experiment
range: Descriptor
inlined: true

```
</details>