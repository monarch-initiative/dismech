

# Slot: gene_sets 


_Curated links from this disease to external gene sets, each referenced by its structured-source id (MYGENESET:<id>, resolving to references_cache/MYGENESET_<id>.md). Membership and the curated GO interpretation live upstream / in the cache file; this slot records only the precise disease<->set link and its semantics, and is the anchor for BP alignment (`just genesets-align`)._





URI: [dismech:slot/gene_sets](https://w3id.org/monarch-initiative/dismech/slot/gene_sets)
Alias: gene_sets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneSetAssociation](../classes/GeneSetAssociation.md) |
| Domain Of | [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:gene_sets |
| native | dismech:gene_sets |




## LinkML Source

<details>
```yaml
name: gene_sets
description: Curated links from this disease to external gene sets, each referenced
  by its structured-source id (MYGENESET:<id>, resolving to references_cache/MYGENESET_<id>.md).
  Membership and the curated GO interpretation live upstream / in the cache file;
  this slot records only the precise disease<->set link and its semantics, and is
  the anchor for BP alignment (`just genesets-align`).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: gene_sets
domain_of:
- Disease
range: GeneSetAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>