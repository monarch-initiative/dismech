

# Slot: inheritance 



URI: [dismech:slot/inheritance](https://w3id.org/monarch-initiative/dismech/slot/inheritance)
Alias: inheritance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

* Range: [Inheritance](../classes/Inheritance.md)

* Multivalued: True





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