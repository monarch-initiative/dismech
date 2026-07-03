

# Slot: assays 



URI: [dismech:slot/assays](https://w3id.org/monarch-initiative/dismech/slot/assays)
Alias: assays

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AssayDescriptor](../classes/AssayDescriptor.md) |
| Domain Of | [Experiment](../classes/Experiment.md), [ExperimentalReadout](../classes/ExperimentalReadout.md), [Pathophysiology](../classes/Pathophysiology.md), [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: Elevated Blood Glucose}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:assays |
| native | dismech:assays |




## LinkML Source

<details>
```yaml
name: assays
examples:
- value: '[{preferred_term: Elevated Blood Glucose}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: assays
domain_of:
- Experiment
- ExperimentalReadout
- Pathophysiology
- Biochemical
range: AssayDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>