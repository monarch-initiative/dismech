# Enum: SurrogateEndpointFootnoteEnum 




_Footnotes and symbols used in the FDA surrogate endpoint workbook_



URI: [dismech:enum/SurrogateEndpointFootnoteEnum](https://w3id.org/monarch-initiative/dismech/enum/SurrogateEndpointFootnoteEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| COMPOSITE_BIOMARKER_SURROGATE | None | Surrogate endpoint is part of a composite of biomarker surrogate endpoints | Title: Composite biomarker surrogate<br>|
| MECHANISM_AGNOSTIC | None | Many mechanisms of action are associated with the surrogate endpoint, so it i... | Title: Mechanism agnostic<br>|
| TUMOR_BURDEN_CONTEXT_DEPENDENT | None | Tumor-burden endpoints may support accelerated or traditional approval depend... | Title: Tumor burden context dependent<br>|
| ANTICIPATED_PRIMARY_EFFICACY_USE | None | FDA anticipates the endpoint could be appropriate as a primary efficacy endpo... | Title: Anticipated primary efficacy use<br>|
| BONE_MINERAL_DENSITY_CONTEXT | None | Bone mineral density footnote for male or glucocorticoid-induced osteoporosis... | Title: Bone mineral density context<br>|
| CLINICAL_ENDPOINTS_REQUIRED | None | Clinical endpoints were required for the approvals | Title: Clinical endpoints required<br>|
| ARRHYTHMIA_RESPONSE_DEFINITION | None | Specialized response definition footnote for supraventricular tachycardia end... | Title: Arrhythmia response definition<br>|




## Slots

| Name | Description |
| ---  | --- |
| [footnotes](../slots/footnotes.md) | FDA workbook footnote semantics attached to the source row |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SurrogateEndpointFootnoteEnum
description: Footnotes and symbols used in the FDA surrogate endpoint workbook
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  COMPOSITE_BIOMARKER_SURROGATE:
    text: COMPOSITE_BIOMARKER_SURROGATE
    description: Surrogate endpoint is part of a composite of biomarker surrogate
      endpoints
    title: Composite biomarker surrogate
  MECHANISM_AGNOSTIC:
    text: MECHANISM_AGNOSTIC
    description: Many mechanisms of action are associated with the surrogate endpoint,
      so it is not directly related to a particular causal pathway
    title: Mechanism agnostic
  TUMOR_BURDEN_CONTEXT_DEPENDENT:
    text: TUMOR_BURDEN_CONTEXT_DEPENDENT
    description: Tumor-burden endpoints may support accelerated or traditional approval
      depending on context of use
    title: Tumor burden context dependent
  ANTICIPATED_PRIMARY_EFFICACY_USE:
    text: ANTICIPATED_PRIMARY_EFFICACY_USE
    description: FDA anticipates the endpoint could be appropriate as a primary efficacy
      endpoint although it has not yet supported an approved NDA or BLA
    title: Anticipated primary efficacy use
  BONE_MINERAL_DENSITY_CONTEXT:
    text: BONE_MINERAL_DENSITY_CONTEXT
    description: Bone mineral density footnote for male or glucocorticoid-induced
      osteoporosis contexts
    title: Bone mineral density context
  CLINICAL_ENDPOINTS_REQUIRED:
    text: CLINICAL_ENDPOINTS_REQUIRED
    description: Clinical endpoints were required for the approvals
    title: Clinical endpoints required
  ARRHYTHMIA_RESPONSE_DEFINITION:
    text: ARRHYTHMIA_RESPONSE_DEFINITION
    description: Specialized response definition footnote for supraventricular tachycardia
      endpoint
    title: Arrhythmia response definition

```
</details>