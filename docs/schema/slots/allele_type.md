

# Slot: allele_type 


_Type of allele or mutation (e.g., null, missense, splice_site, deletion, frameshift, nonsense, hypomorphic, structural_variant). Free text to accommodate the diversity of mutation nomenclature._





URI: [dismech:slot/allele_type](https://w3id.org/monarch-initiative/dismech/slot/allele_type)
Alias: allele_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |






## Properties

* Range: [String](../types/String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:allele_type |
| native | dismech:allele_type |




## LinkML Source

<details>
```yaml
name: allele_type
description: Type of allele or mutation (e.g., null, missense, splice_site, deletion,
  frameshift, nonsense, hypomorphic, structural_variant). Free text to accommodate
  the diversity of mutation nomenclature.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: allele_type
domain_of:
- GeneticContext
range: string

```
</details>