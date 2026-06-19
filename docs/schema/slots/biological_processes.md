

# Slot: biological_processes 



URI: [dismech:slot/biological_processes](https://w3id.org/monarch-initiative/dismech/slot/biological_processes)
Alias: biological_processes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  no  |
| [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) | A mechanism or feature that distinguishes a grouping member from its siblings... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [ExperimentalReadout](../classes/ExperimentalReadout.md), [Pathophysiology](../classes/Pathophysiology.md), [LogicalCriterion](../classes/LogicalCriterion.md), [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: TNF-alpha Production}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:biological_processes |
| native | dismech:biological_processes |




## LinkML Source

<details>
```yaml
name: biological_processes
examples:
- value: '[{preferred_term: TNF-alpha Production}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: biological_processes
domain_of:
- ExperimentalPerturbation
- ExperimentalReadout
- Pathophysiology
- LogicalCriterion
- DifferentiatingMechanism
range: BiologicalProcessDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>