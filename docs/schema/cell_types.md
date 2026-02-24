

# Slot: cell_types 



URI: [dismech:cell_types](https://w3id.org/monarch-initiative/dismech/cell_types)
Alias: cell_types

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |






## Properties

* Range: [CellTypeDescriptor](CellTypeDescriptor.md)

* Multivalued: True





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
- Pathophysiology
- Biochemical
range: CellTypeDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>