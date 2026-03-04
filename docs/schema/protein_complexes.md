

# Slot: protein_complexes 


_Protein complexes that gene products participate in_





URI: [dismech:protein_complexes](https://w3id.org/monarch-initiative/dismech/protein_complexes)
Alias: protein_complexes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |






## Properties

* Range: [ProteinComplexDescriptor](ProteinComplexDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: FA nuclear complex, term: {id: "GO:0043240", label: "Fanconi anaemia nuclear complex"}}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:protein_complexes |
| native | dismech:protein_complexes |




## LinkML Source

<details>
```yaml
name: protein_complexes
description: Protein complexes that gene products participate in
examples:
- value: '[{preferred_term: FA nuclear complex, term: {id: "GO:0043240", label: "Fanconi
    anaemia nuclear complex"}}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: protein_complexes
domain_of:
- Pathophysiology
range: ProteinComplexDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>