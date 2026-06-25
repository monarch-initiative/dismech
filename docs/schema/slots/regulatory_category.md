

# Slot: regulatory_category 


_Functional classification of a variant's impact on gene expression, using the LOE/mLOE/GOE framework (Cheng et al. 2024, PMID:38436667) or traditional coding categories (LOF/GOF/DN)._





URI: [dismech:slot/regulatory_category](https://w3id.org/monarch-initiative/dismech/slot/regulatory_category)
Alias: regulatory_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](../classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |  no  |
| [FunctionalEffect](../classes/FunctionalEffect.md) | Describes the functional consequence of a genetic variant, including regulato... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [RegulatoryVariantCategoryEnum](../enums/RegulatoryVariantCategoryEnum.md) |
| Domain Of | [Variant](../classes/Variant.md), [FunctionalEffect](../classes/FunctionalEffect.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:regulatory_category |
| native | dismech:regulatory_category |




## LinkML Source

<details>
```yaml
name: regulatory_category
description: Functional classification of a variant's impact on gene expression, using
  the LOE/mLOE/GOE framework (Cheng et al. 2024, PMID:38436667) or traditional coding
  categories (LOF/GOF/DN).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: regulatory_category
domain_of:
- Variant
- FunctionalEffect
range: RegulatoryVariantCategoryEnum

```
</details>