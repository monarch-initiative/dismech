# Enum: ExperimentalModelTypeEnum 




_Broad disease-centric categories for experimental model systems, primarily non-animal systems curated in this section_



URI: [dismech:enum/ExperimentalModelTypeEnum](https://w3id.org/monarch-initiative/dismech/enum/ExperimentalModelTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ORGANOID | None | Self-organizing three-dimensional tissue model, often stem-cell-derived |
| ORGAN_ON_CHIP | None | Microfluidic organ- or tissue-on-chip model |
| CELL_LINE | None | Immortalized cell line-based disease model |
| IPSC_DERIVED_MODEL | None | Differentiated model derived from induced pluripotent stem cells |
| PRIMARY_CELL_CULTURE | None | Primary-cell or biopsy-derived culture system, including monolayers |
| CO_CULTURE | None | Host-microbe or multi-cell-type coculture system |
| OTHER | None | Other experimental model type not covered above |




## Slots

| Name | Description |
| ---  | --- |
| [experimental_model_type](../slots/experimental_model_type.md) | Broad category for an experimental model system |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ExperimentalModelTypeEnum
description: Broad disease-centric categories for experimental model systems, primarily
  non-animal systems curated in this section
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ORGANOID:
    text: ORGANOID
    description: Self-organizing three-dimensional tissue model, often stem-cell-derived
  ORGAN_ON_CHIP:
    text: ORGAN_ON_CHIP
    description: Microfluidic organ- or tissue-on-chip model
  CELL_LINE:
    text: CELL_LINE
    description: Immortalized cell line-based disease model
  IPSC_DERIVED_MODEL:
    text: IPSC_DERIVED_MODEL
    description: Differentiated model derived from induced pluripotent stem cells
  PRIMARY_CELL_CULTURE:
    text: PRIMARY_CELL_CULTURE
    description: Primary-cell or biopsy-derived culture system, including monolayers
  CO_CULTURE:
    text: CO_CULTURE
    description: Host-microbe or multi-cell-type coculture system
  OTHER:
    text: OTHER
    description: Other experimental model type not covered above

```
</details>