

# Slot: molecular_functions 



URI: [dismech:slot/molecular_functions](https://w3id.org/monarch-initiative/dismech/slot/molecular_functions)
Alias: molecular_functions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MolecularFunctionDescriptor](../classes/MolecularFunctionDescriptor.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| [{preferred_term: Kinase Activity}] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:molecular_functions |
| native | dismech:molecular_functions |




## LinkML Source

<details>
```yaml
name: molecular_functions
examples:
- value: '[{preferred_term: Kinase Activity}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: molecular_functions
domain_of:
- Pathophysiology
range: MolecularFunctionDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>