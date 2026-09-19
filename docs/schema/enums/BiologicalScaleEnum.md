# Enum: BiologicalScaleEnum 




_Biological scale of the substrate a pathophysiology node describes. A tag capturing which level of biological organisation the node is primarily situated at — molecular, cellular, tissue/organ, or organism. Each value covers both ongoing processes AND persistent states at that scale (a fusion protein exists / a cell population accumulates / an ectopic tissue persists / a metabolite is chronically elevated). See projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the survey that led to this enum design._



URI: [dismech:enum/BiologicalScaleEnum](https://w3id.org/monarch-initiative/dismech/enum/BiologicalScaleEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| MOLECULAR | None | Molecular scale — molecular activities (kinase activity, transcription factor... |
| CELLULAR | None | Cellular scale — cellular processes (differentiation, apoptosis, autophagy, i... |
| TISSUE | None | Tissue / organ scale — tissue processes (inflammation, fibrosis, granuloma fo... |
| ORGANISM | None | Organism scale — systemic / multi-organ / whole-body processes (DIC, cytokine... |




## Slots

| Name | Description |
| ---  | --- |
| [biological_scale](../slots/biological_scale.md) | Biological scale of the substrate this pathophysiology node primarily describ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: BiologicalScaleEnum
description: Biological scale of the substrate a pathophysiology node describes. A
  tag capturing which level of biological organisation the node is primarily situated
  at — molecular, cellular, tissue/organ, or organism. Each value covers both ongoing
  processes AND persistent states at that scale (a fusion protein exists / a cell
  population accumulates / an ectopic tissue persists / a metabolite is chronically
  elevated). See projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the survey that
  led to this enum design.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  MOLECULAR:
    text: MOLECULAR
    description: Molecular scale — molecular activities (kinase activity, transcription
      factor binding, ion transport, catalysis) or molecular states (a fusion protein
      exists, a chemical accumulates, an enzyme is functionally deficient, a gene
      carries a variant burden). Substrate is a molecule, complex, or genetic element.
  CELLULAR:
    text: CELLULAR
    description: Cellular scale — cellular processes (differentiation, apoptosis,
      autophagy, intracellular signaling) or cellular states (a cell population is
      in a maintained aberrant condition, an organelle is structurally disrupted,
      a cell type has accumulated). Substrate is a single cell or cell type.
  TISSUE:
    text: TISSUE
    description: Tissue / organ scale — tissue processes (inflammation, fibrosis,
      granuloma formation, neoplastic outgrowth) or tissue states (an ectopic tissue
      persists, an organ is malformed, a structural lesion exists). Substrate is a
      tissue, organ, or anatomical structure.
  ORGANISM:
    text: ORGANISM
    description: Organism scale — systemic / multi-organ / whole-body processes (DIC,
      cytokine storm, fever, cachexia) or systemic states (a metabolite is chronically
      elevated, the microbiome is dysbiotic, a syndromic developmental phenotype bundles
      multi-organ features). Substrate is the whole organism.

```
</details>