# Enum: RegulatoryVariantCategoryEnum 




_Functional classification of non-coding gene regulatory variants based on their impact on gene expression patterns. Adapted from Cheng et al. 2024 (PMID:38436667). Includes traditional coding variant categories for completeness._



URI: [dismech:enum/RegulatoryVariantCategoryEnum](https://w3id.org/monarch-initiative/dismech/enum/RegulatoryVariantCategoryEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| LOE | None | Non-modular loss-of-expression | Title: Loss of expression<br>|
| mLOE | None | Modular loss-of-expression | Title: Modular loss of expression<br>|
| GOE | None | Gain-of-ectopic-expression | Title: Gain of ectopic expression<br>|
| LOF | None | Coding loss-of-function | Title: Loss of function<br>|
| GOF | None | Coding gain-of-function | Title: Gain of function<br>|
| DN | None | Dominant-negative | Title: Dominant negative<br>|




## Slots

| Name | Description |
| ---  | --- |
| [regulatory_category](../slots/regulatory_category.md) | Functional classification of a variant's impact on gene expression, using the... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: RegulatoryVariantCategoryEnum
description: Functional classification of non-coding gene regulatory variants based
  on their impact on gene expression patterns. Adapted from Cheng et al. 2024 (PMID:38436667).
  Includes traditional coding variant categories for completeness.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  LOE:
    text: LOE
    description: Non-modular loss-of-expression. Diminishes or abolishes gene expression
      across all cell types that intrinsically express the gene. Analogous to coding
      amorphic or hypomorphic loss-of-function.
    title: Loss of expression
    notes:
    - Defined in Cheng et al. 2024 (PMID:38436667) as non-modular LOE
    see_also:
    - PMID:38436667
  mLOE:
    text: mLOE
    description: Modular loss-of-expression. Diminishes or abolishes gene expression
      in only a subset of cell types or developmental windows. Represents a disease
      mechanism largely unique to non-coding regulatory variants.
    title: Modular loss of expression
    notes:
    - Defined in Cheng et al. 2024 (PMID:38436667) as modular LOE (mLOE)
    see_also:
    - PMID:38436667
  GOE:
    text: GOE
    description: Gain-of-ectopic-expression. Results in ectopic spatial and/or temporal
      expression of a gene. Can arise from enhancer adoption, novel TFBS creation,
      promoter switching, or repressor site disruption.
    title: Gain of ectopic expression
    notes:
    - Defined in Cheng et al. 2024 (PMID:38436667) as gain-of-ectopic-expression (GOE)
    see_also:
    - PMID:38436667
  LOF:
    text: LOF
    description: Coding loss-of-function. Loss of normal biological function via complete
      (amorphic) or partial (hypomorphic) loss of protein activity.
    title: Loss of function
  GOF:
    text: GOF
    description: Coding gain-of-function. Creates a protein with increased activity
      (hypermorphic) or entirely new function (neomorphic).
    title: Gain of function
  DN:
    text: DN
    description: Dominant-negative. Creates a protein that blocks the normal function
      of the remaining wild-type protein (antimorphic).
    title: Dominant negative

```
</details>