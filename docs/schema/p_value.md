

# Slot: p_value 


_P-value for an association or enrichment_





URI: [dismech:p_value](https://w3id.org/monarch-initiative/dismech/p_value)
Alias: p_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationMetric](AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |
| [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |






## Properties

* Range: [Float](Float.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:p_value |
| native | dismech:p_value |




## LinkML Source

<details>
```yaml
name: p_value
description: P-value for an association or enrichment
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: p_value
domain_of:
- AssociationMetric
- GOEnrichmentTerm
range: float

```
</details>