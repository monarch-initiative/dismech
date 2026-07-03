

# Slot: cell_types 



URI: [dismech:slot/cell_types](https://w3id.org/monarch-initiative/dismech/slot/cell_types)
Alias: cell_types

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalModel](../classes/ExperimentalModel.md) | A disease-relevant non-animal experimental model system |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CellTypeDescriptor](../classes/CellTypeDescriptor.md) |
| Domain Of | [ExperimentalModel](../classes/ExperimentalModel.md), [Pathophysiology](../classes/Pathophysiology.md), [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: Macrophage}, {preferred_term: T Cell}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:cell_types |
| native | dismech:cell_types |




## LinkML Source

<details>
```yaml
name: cell_types
examples:
- value: '[{preferred_term: Macrophage}, {preferred_term: T Cell}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: cell_types
domain_of:
- ExperimentalModel
- Pathophysiology
- Biochemical
range: CellTypeDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>