

# Slot: inheritance 



URI: [dismech:inheritance](https://w3id.org/monarch-initiative/dismech/inheritance)
Alias: inheritance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](Genetic.md) |  |  no  |
| [Disease](Disease.md) |  |  no  |
| [Subtype](Subtype.md) |  |  no  |






## Properties

* Range: [Inheritance](Inheritance.md)

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