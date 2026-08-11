# Enum: ClinicalBenefitLinkageEnum 




_How a surrogate endpoint is linked to clinical benefit in the regulatory context_



URI: [dismech:enum/ClinicalBenefitLinkageEnum](https://w3id.org/monarch-initiative/dismech/enum/ClinicalBenefitLinkageEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| KNOWN_TO_PREDICT_CLINICAL_BENEFIT | None | FDA table approval context indicates the endpoint is known to predict clinica... | Title: Known to predict clinical benefit<br>|
| REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT | None | FDA table approval context indicates the endpoint is reasonably likely to pre... | Title: Reasonably likely to predict clinical benefit<br>|
| CONTEXT_DEPENDENT | None | Clinical-benefit linkage depends on context of use and approval pathway | Title: Context dependent<br>|




## Slots

| Name | Description |
| ---  | --- |
| [clinical_benefit_linkage](../slots/clinical_benefit_linkage.md) | How the surrogate endpoint is linked to clinical benefit in the regulatory co... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalBenefitLinkageEnum
description: How a surrogate endpoint is linked to clinical benefit in the regulatory
  context
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  KNOWN_TO_PREDICT_CLINICAL_BENEFIT:
    text: KNOWN_TO_PREDICT_CLINICAL_BENEFIT
    description: FDA table approval context indicates the endpoint is known to predict
      clinical benefit for the curated context
    title: Known to predict clinical benefit
  REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT:
    text: REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT
    description: FDA table approval context indicates the endpoint is reasonably likely
      to predict clinical benefit
    title: Reasonably likely to predict clinical benefit
  CONTEXT_DEPENDENT:
    text: CONTEXT_DEPENDENT
    description: Clinical-benefit linkage depends on context of use and approval pathway
    title: Context dependent

```
</details>