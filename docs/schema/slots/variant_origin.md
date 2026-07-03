

# Slot: variant_origin 


_The origin of disease-associated variation in this gene (germline, somatic, de novo, or both). Bound to GENO allele origin terms._





URI: [dismech:slot/variant_origin](https://w3id.org/monarch-initiative/dismech/slot/variant_origin)
Alias: variant_origin

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VariantOriginEnum](../enums/VariantOriginEnum.md) |
| Domain Of | [GeneticContext](../classes/GeneticContext.md), [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| SOMATIC |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:variant_origin |
| native | dismech:variant_origin |




## LinkML Source

<details>
```yaml
name: variant_origin
description: The origin of disease-associated variation in this gene (germline, somatic,
  de novo, or both). Bound to GENO allele origin terms.
examples:
- value: SOMATIC
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: variant_origin
domain_of:
- GeneticContext
- Genetic
range: VariantOriginEnum

```
</details>