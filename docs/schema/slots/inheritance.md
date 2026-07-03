

# Slot: inheritance 



URI: [dismech:slot/inheritance](https://w3id.org/monarch-initiative/dismech/slot/inheritance)
Alias: inheritance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [Disease](../classes/Disease.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Inheritance](../classes/Inheritance.md) |
| Domain Of | [Subtype](../classes/Subtype.md), [Genetic](../classes/Genetic.md), [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| Autosomal Dominant |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:inheritance |
| native | dismech:inheritance |




## LinkML Source

<details>
```yaml
name: inheritance
examples:
- value: Autosomal Dominant
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: inheritance
domain_of:
- Subtype
- Genetic
- Disease
range: Inheritance
multivalued: true
inlined: true
inlined_as_list: true

```
</details>