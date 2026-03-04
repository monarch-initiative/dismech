

# Slot: fdr 


_FDR-adjusted p-value for an association or enrichment_





URI: [dismech:fdr](https://w3id.org/monarch-initiative/dismech/fdr)
Alias: fdr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |
| [AssociationMetric](AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:fdr |
| native | dismech:fdr |




## LinkML Source

<details>
```yaml
name: fdr
description: FDR-adjusted p-value for an association or enrichment
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: fdr
domain_of:
- AssociationMetric
- GOEnrichmentTerm
range: float

```
</details>