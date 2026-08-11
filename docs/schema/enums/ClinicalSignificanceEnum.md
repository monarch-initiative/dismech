# Enum: ClinicalSignificanceEnum 




_The clinical significance of a variant for a condition (ACMG guidelines)_



URI: [dismech:enum/ClinicalSignificanceEnum](https://w3id.org/monarch-initiative/dismech/enum/ClinicalSignificanceEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PATHOGENIC | GENO:0000840 | Variant is pathogenic for the condition (ACMG class 5) | Title: Pathogenic<br>|
| LIKELY_PATHOGENIC | GENO:0000841 | Variant is likely pathogenic for the condition (ACMG class 4) | Title: Likely pathogenic<br>|
| BENIGN | GENO:0000843 | Variant is benign for the condition (ACMG class 1) | Title: Benign<br>|
| LIKELY_BENIGN | GENO:0000844 | Variant is likely benign for the condition (ACMG class 2) | Title: Likely benign<br>|
| UNCERTAIN_SIGNIFICANCE | GENO:0000845 | Clinical significance of the variant is uncertain (ACMG class 3) | Title: Uncertain significance<br>|




## Slots

| Name | Description |
| ---  | --- |
| [clinical_significance](../slots/clinical_significance.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalSignificanceEnum
description: The clinical significance of a variant for a condition (ACMG guidelines)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PATHOGENIC:
    text: PATHOGENIC
    description: Variant is pathogenic for the condition (ACMG class 5)
    meaning: GENO:0000840
    title: Pathogenic
    aliases:
    - pathogenic_for_condition
  LIKELY_PATHOGENIC:
    text: LIKELY_PATHOGENIC
    description: Variant is likely pathogenic for the condition (ACMG class 4)
    meaning: GENO:0000841
    title: Likely pathogenic
    aliases:
    - likely_pathogenic_for_condition
  BENIGN:
    text: BENIGN
    description: Variant is benign for the condition (ACMG class 1)
    meaning: GENO:0000843
    title: Benign
    aliases:
    - benign_for_condition
  LIKELY_BENIGN:
    text: LIKELY_BENIGN
    description: Variant is likely benign for the condition (ACMG class 2)
    meaning: GENO:0000844
    title: Likely benign
    aliases:
    - likely_benign_for_condition
  UNCERTAIN_SIGNIFICANCE:
    text: UNCERTAIN_SIGNIFICANCE
    description: Clinical significance of the variant is uncertain (ACMG class 3)
    meaning: GENO:0000845
    title: Uncertain significance
    aliases:
    - has_uncertain_significance_for_condition

```
</details>