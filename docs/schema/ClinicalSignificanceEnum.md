# Enum: ClinicalSignificanceEnum 




_The clinical significance of a variant for a condition (ACMG guidelines)_



URI: [dismech:ClinicalSignificanceEnum](https://w3id.org/monarch-initiative/dismech/ClinicalSignificanceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PATHOGENIC | GENO:0000840 | pathogenic_for_condition |
| LIKELY_PATHOGENIC | GENO:0000841 | likely_pathogenic_for_condition |
| BENIGN | GENO:0000843 | benign_for_condition |
| LIKELY_BENIGN | GENO:0000844 | likely_benign_for_condition |
| UNCERTAIN_SIGNIFICANCE | GENO:0000845 | has_uncertain_significance_for_condition |




## Slots

| Name | Description |
| ---  | --- |
| [clinical_significance](clinical_significance.md) |  |





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
    description: pathogenic_for_condition
    meaning: GENO:0000840
  LIKELY_PATHOGENIC:
    text: LIKELY_PATHOGENIC
    description: likely_pathogenic_for_condition
    meaning: GENO:0000841
  BENIGN:
    text: BENIGN
    description: benign_for_condition
    meaning: GENO:0000843
  LIKELY_BENIGN:
    text: LIKELY_BENIGN
    description: likely_benign_for_condition
    meaning: GENO:0000844
  UNCERTAIN_SIGNIFICANCE:
    text: UNCERTAIN_SIGNIFICANCE
    description: has_uncertain_significance_for_condition
    meaning: GENO:0000845

```
</details>