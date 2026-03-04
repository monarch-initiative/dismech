# Enum: ComputationalModelTypeEnum 




_Type of computational or in-silico model_



URI: [dismech:ComputationalModelTypeEnum](https://w3id.org/monarch-initiative/dismech/ComputationalModelTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| GENOME_SCALE_METABOLIC | None | Genome-scale metabolic reconstruction (e |
| FLUX_BALANCE_ANALYSIS | None | Constraint-based FBA model |
| KINETIC | None | ODE-based kinetic model with rate equations |
| AGENT_BASED | None | Agent-based simulation model |
| BOOLEAN_NETWORK | None | Boolean gene regulatory network |
| PHYSIOLOGICAL | None | Physiologically-based pharmacokinetic (PBPK) or organ model |
| DIGITAL_TWIN | None | Patient-specific computational model |
| MACHINE_LEARNING | None | ML/AI predictive model trained on disease data |
| PERTURBATION_PREDICTION | None | Cell-based perturbation models (CRISPR screens, chemical perturbations) with ... |
| FOUNDATION_MODEL | None | Pre-trained single-cell foundation models (scGPT, Geneformer, scGenePT) for p... |




## Slots

| Name | Description |
| ---  | --- |
| [model_type](model_type.md) | Type of computational model |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ComputationalModelTypeEnum
description: Type of computational or in-silico model
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  GENOME_SCALE_METABOLIC:
    text: GENOME_SCALE_METABOLIC
    description: Genome-scale metabolic reconstruction (e.g., Recon3D, Harvey)
  FLUX_BALANCE_ANALYSIS:
    text: FLUX_BALANCE_ANALYSIS
    description: Constraint-based FBA model
  KINETIC:
    text: KINETIC
    description: ODE-based kinetic model with rate equations
  AGENT_BASED:
    text: AGENT_BASED
    description: Agent-based simulation model
  BOOLEAN_NETWORK:
    text: BOOLEAN_NETWORK
    description: Boolean gene regulatory network
  PHYSIOLOGICAL:
    text: PHYSIOLOGICAL
    description: Physiologically-based pharmacokinetic (PBPK) or organ model
  DIGITAL_TWIN:
    text: DIGITAL_TWIN
    description: Patient-specific computational model
  MACHINE_LEARNING:
    text: MACHINE_LEARNING
    description: ML/AI predictive model trained on disease data
  PERTURBATION_PREDICTION:
    text: PERTURBATION_PREDICTION
    description: Cell-based perturbation models (CRISPR screens, chemical perturbations)
      with gene expression readouts
  FOUNDATION_MODEL:
    text: FOUNDATION_MODEL
    description: Pre-trained single-cell foundation models (scGPT, Geneformer, scGenePT)
      for perturbation response prediction

```
</details>