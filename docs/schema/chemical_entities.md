

# Slot: chemical_entities 



URI: [dismech:chemical_entities](https://w3id.org/monarch-initiative/dismech/chemical_entities)
Alias: chemical_entities

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |






## Properties

* Range: [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md)

* Multivalued: True





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
- Pathophysiology
range: ChemicalEntityDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>