

# Slot: triggers 



URI: [dismech:slot/triggers](https://w3id.org/monarch-initiative/dismech/slot/triggers)
Alias: triggers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TriggerDescriptor](../classes/TriggerDescriptor.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [Pathophysiology](../classes/Pathophysiology.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: Viral Infections}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:triggers |
| native | dismech:triggers |




## LinkML Source

<details>
```yaml
name: triggers
examples:
- value: '[{preferred_term: Viral Infections}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: triggers
domain_of:
- ExperimentalPerturbation
- Pathophysiology
range: TriggerDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>