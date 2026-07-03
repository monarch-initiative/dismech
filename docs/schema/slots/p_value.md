

# Slot: p_value 


_P-value for an association or enrichment_





URI: [dismech:slot/p_value](https://w3id.org/monarch-initiative/dismech/slot/p_value)
Alias: p_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationMetric](../classes/AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |
| [GOEnrichmentTerm](../classes/GOEnrichmentTerm.md) | GO term enrichment result with statistical metrics |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [AssociationMetric](../classes/AssociationMetric.md), [GOEnrichmentTerm](../classes/GOEnrichmentTerm.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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