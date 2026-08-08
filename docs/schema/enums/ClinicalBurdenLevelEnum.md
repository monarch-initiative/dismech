# Enum: ClinicalBurdenLevelEnum 




_Coarse disease-level assessment of the typical clinical burden imposed by a disease, considering functional impact, morbidity, duration, monitoring/treatment burden, and expected long-term consequences. This is distinct from phenotype-level severity._



URI: [dismech:enum/ClinicalBurdenLevelEnum](https://w3id.org/monarch-initiative/dismech/enum/ClinicalBurdenLevelEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| LOW | None | Typical cases impose limited functional impact, morbidity, management burden,... | Title: Low<br>|
| MODERATE | None | Typical cases impose clinically meaningful but not usually life-threatening o... | Title: Moderate<br>|
| HIGH | None | Typical cases impose substantial morbidity, disability, intensive management ... | Title: High<br>|
| VARIABLE | None | Clinical burden varies widely across patients, subtypes, stages, or contexts,... | Title: Variable<br>|
| UNKNOWN | None | The typical clinical burden is not established or has not been assessed | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [burden_level](../slots/burden_level.md) | Coarse disease-level clinical burden category |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalBurdenLevelEnum
description: Coarse disease-level assessment of the typical clinical burden imposed
  by a disease, considering functional impact, morbidity, duration, monitoring/treatment
  burden, and expected long-term consequences. This is distinct from phenotype-level
  severity.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  LOW:
    text: LOW
    description: Typical cases impose limited functional impact, morbidity, management
      burden, or long-term consequences.
    title: Low
  MODERATE:
    text: MODERATE
    description: Typical cases impose clinically meaningful but not usually life-threatening
      or highly disabling burden.
    title: Moderate
  HIGH:
    text: HIGH
    description: Typical cases impose substantial morbidity, disability, intensive
      management needs, major long-term consequences, or mortality risk.
    title: High
  VARIABLE:
    text: VARIABLE
    description: Clinical burden varies widely across patients, subtypes, stages,
      or contexts, and no single low/moderate/high level is representative.
    title: Variable
  UNKNOWN:
    text: UNKNOWN
    description: The typical clinical burden is not established or has not been assessed.
    title: Unknown

```
</details>