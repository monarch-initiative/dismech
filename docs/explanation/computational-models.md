# Computational Models and Causal Perturbation Analysis

## Overview

Some dismech disorder entries reference SBML (Systems Biology Markup Language) models that capture the quantitative dynamics of disease mechanisms as ordinary differential equations (ODEs). The **dismech-perturb** framework connects these models back to the clinical knowledge in the YAML, answering questions like:

> "If gene X is lost or environmental parameter Y changes, which phenotypes activate, how severely, and through which mechanistic path?"

This bridges two representations that are usually disconnected: the qualitative causal graph in the YAML (mechanisms, phenotypes, evidence) and the quantitative simulation from the ODE model.

## Data Sources

The system is fully data-driven, with no disease-specific Python code. Three data sources work together:

### 1. Disorder YAML (`kb/disorders/*.yaml`)

The pathophysiology section provides the qualitative causal graph. Each mechanism can declare `downstream` edges pointing to other mechanisms or phenotypes:

```yaml
pathophysiology:
- name: Secondary Hyperparathyroidism
  description: >
    Declining calcitriol and hyperphosphatemia stimulate PTH secretion...
  downstream:
  - target: RANKL/OPG Imbalance
    description: Elevated PTH increases RANKL and suppresses OPG
    causal_link_type: DIRECT
  - target: Bone Pain
    description: PTH-driven high-turnover bone disease
    causal_link_type: INDIRECT_KNOWN_INTERMEDIATES
    intermediate_mechanisms:
    - increased bone resorption
```

These edges form a directed graph from root causes through mechanisms to clinical phenotypes (HP terms). The `causal_link_type` field indicates whether the edge is direct or passes through known/unknown intermediates.

### 2. SBML Model + Extension (`models/`)

The base ODE model (e.g., Peterson-Riggs 2010 for CKD-MBD) is stored as BioModels SBML XML. Some pathophysiology mechanisms aren't captured by the base model. Extension models in Antimony format add missing species and reactions:

```
models/
  BIOMD0000000613.xml           # Base SBML (Ca/PO4/PTH/bone dynamics)
  BIOMD0000000613.ext.ant       # Extension (FGF23, Klotho, VascCa, Sclerostin)
  BIOMD0000000613.config.yaml   # Sidecar configuration
```

The base and extension models run as a coupled simulation with bidirectional feedback at each timestep.

### Variable Mapping via `dataset_identifier`

Each `ModelVariable` in the YAML can carry a `dataset_identifier` — the native name of that variable in the model file. This is model-format-agnostic (works for SBML species, COBRA reaction IDs, database columns, etc.) and is scoped to the parent `ComputationalModel`:

```yaml
computational_models:
- name: Peterson-Riggs Calcium Homeostasis
  model_id: BIOMD0000000613
  variables:
  - name: Plasma_Ca
    dataset_identifier: P            # SBML species name in this model
    unit: mg/dL
    mappings_list:
    - term: { id: LOINC:17861-6, label: "Calcium:MCnc:Pt:Ser/Plas:Qn" }
  - name: BMD
    dataset_identifier: Qbone
    unit: relative
    mappings_list:
    - preferred_term: Reduced bone mineral density
      term: { id: HP:0004349, label: "Reduced bone mineral density" }
      threshold: 0.85                # Phenotype activates below this ratio
      threshold_direction: below
      severity_scale:
      - { threshold: 0.85, name: mild }
      - { threshold: 0.70, name: moderate }
      - { threshold: 0.50, name: severe }
  - name: Vascular_Calcification
    dataset_identifier: VascCa
    notes: Extension model species
    mappings_list:
    - preferred_term: Arterial calcification
      term: { id: HP:0003207, label: "Arterial calcification" }
      threshold: 50
      threshold_direction: above
      severity_scale:
      - { threshold: 50, name: mild }
      - { threshold: 150, name: moderate }
      - { threshold: 300, name: severe }
```

Phenotype thresholds live directly on the HP term mappings — when a variable's value crosses the threshold in the specified direction, the phenotype activates. Multiple HP terms on a single variable get independent thresholds (e.g., BMD maps to both "Reduced bone mineral density" at 0.85 and "Pathologic fracture" at 0.70).

If two models use different internal names for the same biological quantity, each `ComputationalModel` entry has its own `variables` list with its own `dataset_identifier`.

### 3. Model Configuration Sidecar (`models/*.config.yaml`)

Contains simulation-specific plumbing: gene-to-parameter mappings, scenarios, and coupling config:

```yaml
gene_effects:
  CASR:
    parameter: T61        # SBML parameter controlling PTH secretion floor
    LoF: 3.0              # Loss-of-function multiplier
    GoF: 0.3              # Gain-of-function multiplier (calcimimetic)

scenarios:
  CASR_LoF:
    label: "CASR loss-of-function"
    gene: CASR
    effect: LoF
    gfr: 2.0
    causal_root: Secondary Hyperparathyroidism

coupling:
  dt_hours: 168
  base_to_extension:
    ECCPhos: ECCPhos_ext
    PTH: PTH_ext
```

## How It Works

```
Gene/Environment Perturbation
        │
        ▼
┌─── Model Config ───┐     ┌──── Disorder YAML ────────────────────┐
│ gene → parameter   │     │ pathophysiology[].downstream → graph  │
│ coupling config    │     │ computational_models[].variables:     │
└────────┬───────────┘     │   dataset_identifier → model species  │
         │                 │   mappings_list → HP terms + thresholds│
         ▼                 └────────┬──────────────────────────────┘
┌─── ODE Simulation ─┐             │
│ SBML + Extension   │             │
│ coupled run        │             │
│ → variable values  │             │
└────────┬───────────┘             │
         │                         │
         ▼                         ▼
┌─── Phenotype Mapper ─────────────────────────────┐
│ variable thresholds → HP terms + severity        │
│ causal chain trace → mechanistic explanation     │
└──────────────────────────────────────────────────┘
```

1. A perturbation (gene LoF/GoF, parameter change, or GFR level) modifies an ODE model parameter
2. The coupled ODE simulation runs to steady state
3. Final variable values are looked up via `dataset_identifier` from the YAML
4. HP term mappings with thresholds determine which phenotypes activate and at what severity
5. The causal graph (`pathophysiology[].downstream`) is traced from the perturbation root

## CLI Usage

```bash
# Single gene perturbation
just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --gene CASR --effect LoF

# Named scenario from config
just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --scenario CASR_LoF

# Environmental perturbation (high phosphate diet)
just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --param OralPhos=2.0

# All scenarios with gene-phenotype matrix
just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --all

# Adjust CKD severity (GFR: 6.0=healthy, 2.0=CKD3b, 1.0=CKD4)
just perturb kb/disorders/CKD-Mineral_Bone_Disorder.yaml --gene CASR --effect LoF --gfr 1.0
```

## Exemplar: CKD-Mineral Bone Disorder

CKD-MBD is the first disorder fully wired for perturbation analysis. It demonstrates the framework's capabilities.

### The Model

The base model is Peterson-Riggs 2010 (BioModels BIOMD0000000613), a 12-compartment ODE model of calcium-phosphate-PTH-bone dynamics. The extension adds FGF23, soluble Klotho, vascular calcification, and sclerostin — species critical to CKD-MBD pathophysiology but absent from the 2010 model.

### The Causal Graph

Seven pathophysiology mechanisms form the backbone, with `downstream` edges connecting them:

```
Kidney G3P Sensing ──► Phosphate Retention & FGF23 Axis
                            │
                ┌───────────┼───────────────┐
                ▼           ▼               ▼
        Calcitriol    Secondary HPT    Vascular
        Deficiency         │           Calcification
           │         ┌─────┼─────┐         │
           │         ▼     ▼     ▼         ▼
           │     RANKL/  Bone  LVH    Bone-Vascular
           │     OPG    Pain          Paradox
           │      │                      │
           │      ├──► ↓BMD ◄────────────┘
           │      └──► Fractures
           │
           ├──► Proximal Myopathy
           └──► Short Stature
```

Phenotypes (HP terms) sit at the leaves. Each edge carries a `causal_link_type` and optional `intermediate_mechanisms` for transparency.

### Supported Perturbations

Seven genes map to model parameters, covering both the base SBML and the Antimony extension:

| Gene | Parameter | Model | Effect |
|------|-----------|-------|--------|
| CASR | T61 (PTH floor) | Base | LoF raises PTH; GoF (calcimimetic) lowers it |
| CYP27B1 | Species A (1α-hydroxylase) | Base | LoF reduces calcitriol |
| CYP24A1 | T69 (calcitriol degradation) | Base | LoF slows degradation |
| KL | kin_Klotho | Extension | LoF reduces Klotho signaling |
| SLC20A1 | kin_VascCa | Extension | GoF increases vascular phosphate uptake |
| SOST | kin_SOST | Extension | LoF reduces sclerostin |
| GPD1 | kin_FGF23 | Extension | LoF reduces FGF23 production |

Environmental scenarios include high-phosphate diet, low-calcium diet, phosphate binder therapy, and calcimimetic treatment.

### Example Output

```
PERTURBATION: CASR loss-of-function
Gene: CASR
GFR: 2.0

  Variable                        Unperturbed    Perturbed     Change
  PTH (pg/mL)                           85.97        92.86      +8.0%
  Bone Ca store                      17812.83     17435.46      -2.1%
  Vasc. Calcification                  132.66       141.41      +6.6%
  Sclerostin (pmol/L)                 2893.25      3108.71      +7.4%

  ACTIVATED PHENOTYPES:
    [           mild] HP:0003207 Arterial calcification (value: 141.4)
    [           mild] HP:0001712 Left ventricular hypertrophy (value: 141.4)
    [           mild] HP:0002653 Bone pain (value: 92.9)

  CAUSAL CHAINS (top 3):
    1. Secondary HPT → Vascular Calcification → Bone-Vascular Paradox → ↓BMD
    2. Secondary HPT → RANKL/OPG Imbalance → ↓BMD
    3. Secondary HPT → RANKL/OPG Imbalance → Pathological Fractures
```

## Adding Perturbation Support to Other Disorders

A disorder becomes perturbable when it has:

1. **`computational_models[].model_id`** in the YAML — references an SBML model
2. **`computational_models[].variables`** with `dataset_identifier` and HP term `mappings_list` with thresholds
3. **`pathophysiology[].downstream`** edges — the qualitative causal graph
4. **A model config sidecar** in `models/` — gene-to-parameter mappings, scenarios, coupling

The framework is generic. No Python code changes are needed to add a new disorder — only data files. The minimum viable config needs:

- An SBML file (download from BioModels or author in Antimony)
- Variables in the YAML with `dataset_identifier` mapping to model species and HP term thresholds
- A `*.config.yaml` with `gene_effects` and `coupling` for simulation plumbing
- `downstream` edges in the disorder YAML connecting mechanisms to phenotypes

## Dependencies

- **tellurium** — SBML/Antimony simulation via libroadrunner (optional; gracefully skipped if not installed)
- **networkx** — used by the base `dismech.graph` module
- **typer** — CLI interface
- **pyyaml** — YAML parsing

Install tellurium with: `uv pip install tellurium`
