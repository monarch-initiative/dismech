

# Slot: gene_products 


_Gene products (proteins, fusion proteins, oncoproteins) involved in this pathophysiology mechanism. Use NCIT terms for specific proteins._





URI: [dismech:gene_products](https://w3id.org/monarch-initiative/dismech/gene_products)
Alias: gene_products

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |






## Properties

* Range: [GeneProductDescriptor](GeneProductDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: BCR-ABL1 fusion protein, term: {id: NCIT:C16325, label: BCR/ABL1 Fusion Protein}}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:gene_products |
| native | dismech:gene_products |




## LinkML Source

<details>
```yaml
name: gene_products
description: Gene products (proteins, fusion proteins, oncoproteins) involved in this
  pathophysiology mechanism. Use NCIT terms for specific proteins.
examples:
- value: '[{preferred_term: BCR-ABL1 fusion protein, term: {id: NCIT:C16325, label:
    BCR/ABL1 Fusion Protein}}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: gene_products
domain_of:
- Pathophysiology
range: GeneProductDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>