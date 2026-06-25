

# Slot: target_gene 


_The gene whose transcript an antisense oligonucleotide targets (bindable to HGNC)._





URI: [dismech:slot/target_gene](https://w3id.org/monarch-initiative/dismech/slot/target_gene)
Alias: target_gene

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AntisenseOligonucleotideDetail](../classes/AntisenseOligonucleotideDetail.md) | Structured attributes specific to an antisense oligonucleotide (ASO) treatmen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneDescriptor](../classes/GeneDescriptor.md) |
| Domain Of | [AntisenseOligonucleotideDetail](../classes/AntisenseOligonucleotideDetail.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:target_gene |
| native | dismech:target_gene |




## LinkML Source

<details>
```yaml
name: target_gene
description: The gene whose transcript an antisense oligonucleotide targets (bindable
  to HGNC).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: target_gene
domain_of:
- AntisenseOligonucleotideDetail
range: GeneDescriptor
inlined: true

```
</details>