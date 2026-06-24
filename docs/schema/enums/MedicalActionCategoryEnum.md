# Enum: MedicalActionCategoryEnum 




_Broad functional category for a clinical action currently represented in the treatments section. Specific actions such as genetic counseling should be represented by treatment_term, while this category stays at the level needed for validation and rendering._



URI: [dismech:enum/MedicalActionCategoryEnum](https://w3id.org/monarch-initiative/dismech/enum/MedicalActionCategoryEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| THERAPEUTIC | NCIT:C49236 | An action intended to treat, prevent, mitigate, or manage disease processes, ... | Title: Therapeutic Procedure<br>|
| DIAGNOSTIC | NCIT:C18020 | A diagnostic procedure or testing action used to establish or refine a diagno... | Title: Diagnostic Procedure<br>|
| SCREENING | NCIT:C15419 | Screening or surveillance intended to detect disease, risk, or early manifest... | Title: Disease Screening<br>|
| MONITORING | NCIT:C61256 | Clinical, laboratory, imaging, or longitudinal follow-up used to observe dise... | Title: Monitoring<br>|
| COUNSELING_INFORMATIONAL | NCIT:C61547 | Counseling, education, risk communication, cascade-testing support, or reprod... | Title: Counseling<br>|




## Slots

| Name | Description |
| ---  | --- |
| [action_category](../slots/action_category.md) | Optional high-level category for a clinical action in the treatments section |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: MedicalActionCategoryEnum
description: Broad functional category for a clinical action currently represented
  in the treatments section. Specific actions such as genetic counseling should be
  represented by treatment_term, while this category stays at the level needed for
  validation and rendering.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  THERAPEUTIC:
    text: THERAPEUTIC
    description: An action intended to treat, prevent, mitigate, or manage disease
      processes, complications, or symptoms. These actions may link to pathophysiology
      nodes or phenotypes through target_mechanisms or target_phenotypes.
    meaning: NCIT:C49236
    title: Therapeutic Procedure
  DIAGNOSTIC:
    text: DIAGNOSTIC
    description: A diagnostic procedure or testing action used to establish or refine
      a diagnosis. These actions should not use target_mechanisms or target_phenotypes
      because they do not treat pathophysiology nodes or phenotypes.
    meaning: NCIT:C18020
    title: Diagnostic Procedure
  SCREENING:
    text: SCREENING
    description: Screening or surveillance intended to detect disease, risk, or early
      manifestations. These actions should not use target_mechanisms or target_phenotypes.
    meaning: NCIT:C15419
    title: Disease Screening
  MONITORING:
    text: MONITORING
    description: Clinical, laboratory, imaging, or longitudinal follow-up used to
      observe disease status or complications. These actions should not use target_mechanisms
      or target_phenotypes.
    meaning: NCIT:C61256
    title: Monitoring
  COUNSELING_INFORMATIONAL:
    text: COUNSELING_INFORMATIONAL
    description: Counseling, education, risk communication, cascade-testing support,
      or reproductive planning actions. Use this broad category for genetic counseling
      and related informational interventions. These actions should not use target_mechanisms
      or target_phenotypes because they do not directly modify disease pathophysiology
      or phenotypes.
    meaning: NCIT:C61547
    title: Counseling

```
</details>