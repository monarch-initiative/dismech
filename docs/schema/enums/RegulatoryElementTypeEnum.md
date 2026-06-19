# Enum: RegulatoryElementTypeEnum 




_Type of gene regulatory element disrupted by a non-coding variant._



URI: [dismech:enum/RegulatoryElementTypeEnum](https://w3id.org/monarch-initiative/dismech/enum/RegulatoryElementTypeEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PROMOTER | None | Promoter-proximal element overlapping the transcription start site, containin... | Title: Promoter<br>|
| ENHANCER | None | Distal regulatory element that upregulates transcriptional activity | Title: Enhancer<br>|
| SILENCER | None | Regulatory element that represses or silences gene transcription | Title: Silencer<br>|
| INSULATOR | None | Boundary element (often CTCF-bound) that compartmentalizes adjacent gene regu... | Title: Insulator<br>|
| TAD_BOUNDARY | None | Topologically associating domain boundary | Title: TAD boundary<br>|
| LOCUS_CONTROL_REGION | None | A cluster of regulatory elements that controls expression of a gene cluster (... | Title: Locus control region<br>|




## Slots

| Name | Description |
| ---  | --- |
| [regulatory_element_type](../slots/regulatory_element_type.md) | Type of gene regulatory element disrupted by a non-coding variant (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: RegulatoryElementTypeEnum
description: Type of gene regulatory element disrupted by a non-coding variant.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PROMOTER:
    text: PROMOTER
    description: Promoter-proximal element overlapping the transcription start site,
      containing core TF binding elements (TATA, CAAT, GC, CACCC boxes).
    title: Promoter
  ENHANCER:
    text: ENHANCER
    description: Distal regulatory element that upregulates transcriptional activity.
      May be cell-type-specific or shared across cell types.
    title: Enhancer
  SILENCER:
    text: SILENCER
    description: Regulatory element that represses or silences gene transcription.
    title: Silencer
  INSULATOR:
    text: INSULATOR
    description: Boundary element (often CTCF-bound) that compartmentalizes adjacent
      gene regulatory domains and limits enhancer-promoter interactions.
    title: Insulator
  TAD_BOUNDARY:
    text: TAD_BOUNDARY
    description: Topologically associating domain boundary. Structural element maintaining
      chromatin loop domains; disruption can cause enhancer adoption or ectopic regulatory
      interactions.
    title: TAD boundary
  LOCUS_CONTROL_REGION:
    text: LOCUS_CONTROL_REGION
    description: A cluster of regulatory elements that controls expression of a gene
      cluster (e.g., the beta-globin LCR).
    title: Locus control region

```
</details>