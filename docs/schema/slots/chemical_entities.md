

# Slot: chemical_entities 



URI: [dismech:slot/chemical_entities](https://w3id.org/monarch-initiative/dismech/slot/chemical_entities)
Alias: chemical_entities

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
| Range | [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [Pathophysiology](../classes/Pathophysiology.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: Plasmalogen}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:chemical_entities |
| native | dismech:chemical_entities |




## LinkML Source

<details>
```yaml
name: chemical_entities
examples:
- value: '[{preferred_term: Plasmalogen}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: chemical_entities
domain_of:
- ExperimentalPerturbation
- Pathophysiology
range: ChemicalEntityDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>