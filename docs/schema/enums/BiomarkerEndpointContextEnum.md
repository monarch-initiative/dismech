# Enum: BiomarkerEndpointContextEnum 




_Endpoint or use context for a biomarker readout link_



URI: [dismech:enum/BiomarkerEndpointContextEnum](https://w3id.org/monarch-initiative/dismech/enum/BiomarkerEndpointContextEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| DIAGNOSTIC | None | Used to support diagnosis or disease classification | Title: Diagnostic<br>|
| PROGNOSTIC | None | Associated with future risk, disease severity, or clinical outcome | Title: Prognostic<br>|
| MONITORING | None | Used to track disease state or progression over time | Title: Monitoring<br>|
| PHARMACODYNAMIC | None | Used to track biological response to treatment or perturbation | Title: Pharmacodynamic<br>|
| CANDIDATE_SURROGATE | None | Potential surrogate endpoint candidate requiring explicit outcome-link eviden... | Title: Candidate surrogate<br>|




## Slots

| Name | Description |
| ---  | --- |
| [endpoint_context](../slots/endpoint_context.md) | Endpoint or use context for a biomarker readout link |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: BiomarkerEndpointContextEnum
description: Endpoint or use context for a biomarker readout link
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  DIAGNOSTIC:
    text: DIAGNOSTIC
    description: Used to support diagnosis or disease classification
    title: Diagnostic
  PROGNOSTIC:
    text: PROGNOSTIC
    description: Associated with future risk, disease severity, or clinical outcome
    title: Prognostic
  MONITORING:
    text: MONITORING
    description: Used to track disease state or progression over time
    title: Monitoring
  PHARMACODYNAMIC:
    text: PHARMACODYNAMIC
    description: Used to track biological response to treatment or perturbation
    title: Pharmacodynamic
  CANDIDATE_SURROGATE:
    text: CANDIDATE_SURROGATE
    description: Potential surrogate endpoint candidate requiring explicit outcome-link
      evidence
    title: Candidate surrogate

```
</details>