

# Slot: gene_set 


_Structured-source id of the gene set, e.g. MYGENESET:KEGG_ASTHMA. Resolves to references_cache/MYGENESET_<id>.md._





URI: [dismech:slot/gene_set](https://w3id.org/monarch-initiative/dismech/slot/gene_set)
Alias: gene_set

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneSetAssociation](../classes/GeneSetAssociation.md) | A curated link between this disease and an external gene set, referenced by i... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](../types/Uriorcurie.md) |
| Domain Of | [GeneSetAssociation](../classes/GeneSetAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeneSetAssociation](../classes/GeneSetAssociation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:gene_set |
| native | dismech:gene_set |




## LinkML Source

<details>
```yaml
name: gene_set
description: Structured-source id of the gene set, e.g. MYGENESET:KEGG_ASTHMA. Resolves
  to references_cache/MYGENESET_<id>.md.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: gene_set
owner: GeneSetAssociation
domain_of:
- GeneSetAssociation
range: uriorcurie
required: true

```
</details>