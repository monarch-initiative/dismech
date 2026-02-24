

# Slot: genes 



URI: [dismech:genes](https://w3id.org/monarch-initiative/dismech/genes)
Alias: genes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [Subtype](Subtype.md) |  |  no  |
| [GeneticContext](GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |






## Properties

* Range: [GeneDescriptor](GeneDescriptor.md)

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