

# Slot: genes 



URI: [dismech:slot/genes](https://w3id.org/monarch-initiative/dismech/slot/genes)
Alias: genes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [AnimalModel](../classes/AnimalModel.md) |  |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |






## Properties

* Range: [GeneDescriptor](../classes/GeneDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: HLA-DQ2}, {preferred_term: INS}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:genes |
| native | dismech:genes |




## LinkML Source

<details>
```yaml
name: genes
examples:
- value: '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: genes
domain_of:
- GeneticContext
- Dataset
- Subtype
- Pathophysiology
- AnimalModel
range: GeneDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>