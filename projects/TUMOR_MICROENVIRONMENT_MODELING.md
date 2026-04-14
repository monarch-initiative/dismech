# Tumor Microenvironment Modeling

## Overview

Explore how dismech's structured mechanism models can serve as a knowledge
substrate for computational tumor microenvironment (TME) modeling, especially
multiscale agent-based simulators, reinforcement-learning-guided therapy
optimization, and cancer digital twin frameworks.

The core idea is straightforward: dismech already encodes disease mechanisms as
cell types, biological processes, and downstream causal effects. Those graphs
are close to the rule systems that agent-based tumor simulators need, but they
are currently optimized for human-readable disease explanation rather than for
machine-actionable simulation. This project asks what is missing to bridge that
gap.

## STATUS

- [ ] Define a TME completeness rubric for existing cancer entries: immune, stromal, vascular, metabolic, spatial, macroenvironment
- [ ] Review the colorectal cancer entries against that rubric and document concrete missing mechanism actors
- [ ] Design a reusable `tumor_ecosystem` module analogous to `fibrotic_response` and `immune_checkpoint_blockade`
- [ ] Decide whether claim extraction in issue `#1100` should be the canonical interchange layer for simulation exports
- [ ] Specify a minimal simulator-facing rule schema beyond raw triples
- [ ] Prototype export of dismech mechanism graphs into a neutral `interaction_rules` format
- [ ] Map existing `immune_checkpoint_blockade` nodes into the broader tumor ecosystem module
- [ ] Identify high-value CRC additions: CAFs, TAMs, MDSCs, endothelial cells, hypoxia, angiogenesis, metabolic suppression, spatial niches
- [ ] Select 2-3 non-CRC cancer entries for the next TME-enrichment pilot
- [ ] Draft a small PhysiCell-oriented proof of concept showing how one curated mechanism chain becomes executable cell-cell rules

## Scientific Thesis

Cancer outcome depends on the interaction of four layers:

1. Tumor cells
2. The immune microenvironment
3. The stromal microenvironment
4. The systemic macroenvironment

The working thesis for this project is that tumor-targeted monotherapy fails
because genomic and epigenomic instability generate resistance heterogeneity
faster than tolerable tumor-cell-only drug combinations can suppress it.
Therapeutic strategy therefore has to shift from "kill the clone" to
"re-engineer the ecosystem."

Three motivating principles:

1. Tumor heterogeneity creates heterogeneous treatment response and resistance
   that cannot be managed with tumor-targeted combinations alone.
2. Drugs aimed at tumor cells also reshape immune, stromal, and systemic
   environments, sometimes in pro-tumor and sometimes in anti-tumor directions.
3. Better efficacy and tolerability should come from combination strategies that
   jointly target tumor cell state, the TME, and the macroenvironment to push
   the whole system toward a globally anti-tumor equilibrium.

## Why dismech Fits This Problem

dismech is already closer to simulator-ready knowledge than a literature review
or pathway diagram:

- Pathophysiology entries are structured causal chains rather than prose blobs.
- Mechanism modules already capture reusable cross-cell programs.
- Treatments can already point back to mechanism nodes through
  `target_mechanisms`.
- The planned claim-extraction work in issue `#1100` should make these chains
  serializable as machine-queryable interaction statements.

In other words, dismech can potentially become the mechanistic prior layer that
many TME simulators currently hand-author.

## Existing dismech Anchors

| Asset | Why it matters for this project |
|-------|--------------------------------|
| `kb/disorders/Colon_Adenocarcinoma.yaml` | Baseline tumor-intrinsic CRC entry; useful control case for what is currently tumor-centric |
| `kb/disorders/MSI_High_Colorectal_Cancer.yaml` | Already models inflamed CRC biology and conforms to `immune_checkpoint_blockade` |
| `kb/disorders/Metastatic_Colorectal_Cancer.yaml` | Already mentions angiogenesis, stromal cooperation, hepatic seed-and-soil biology |
| `kb/disorders/BRAF_V600E_Mutant_Colorectal_Cancer.yaml` and `kb/disorders/HER2_Positive_Colorectal_Cancer.yaml` | Existing molecular subtype coverage enables subtype-specific TME extension rather than starting from scratch |
| `kb/modules/immune_checkpoint_blockade.yaml` | Direct precedent for a reusable tumor-immune mechanism module |
| `kb/modules/fibrotic_response.yaml` | Strong precedent for a cross-disease conserved module with organ-specific substitution in conforming entries |

CRC is therefore the natural pilot. The KB already has subtype-level disease
coverage, at least one explicit tumor-immune module, and a metastatic entry that
starts to gesture toward stromal and vascular ecology.

## Active Computational Landscape

| Approach | What it contributes | Why it matters to dismech |
|----------|---------------------|---------------------------|
| [PhysiCell](https://physicell.org/) and recent [PhysiGym](https://connect.biorxiv.org/archive/show_cat.php?cat=scientific+communication+and+education) work | Large-scale 3D agent-based multicellular simulation, now with a Gymnasium-style RL bridge | dismech mechanism graphs could seed cell-cell interaction rules instead of writing them manually |
| [GigaTIME](https://www.microsoft.com/en-us/research/publication/multimodal-ai-generates-virtual-population-for-tumor-microenvironment-modeling/) | Virtual multiplex immunofluorescence from routine H&E at population scale | Solves TME state initialization and cohort-scale observation, not causal forward simulation |
| [TumorTwin](https://pubmed.ncbi.nlm.nih.gov/40342863/) and the broader [Computational Cancer Community](https://computational.cancer.gov/Community) | Modular patient-specific digital twin infrastructure and NCI-DOE ecosystem building | dismech could supply curated mechanistic priors and reusable disease modules into digital twin pipelines |
| [M4RL](https://pubmed.ncbi.nlm.nih.gov/40779623/) | Multiscale mathematical model-informed RL for glioblastoma treatment scheduling | Shows that therapy optimization becomes more powerful once tumor-TME dynamics are explicit |
| [SMMART](https://pubmed.ncbi.nlm.nih.gov/33772089/) | Serial biopsies and multi-omic analysis of treatment-driven tumor ecosystem adaptation | Supplies the empirical framing: tumors and their ecosystems adapt under therapy, so simulators need dynamic, not static, mechanism rules |

## Gap Analysis for Current CRC Coverage

The existing colorectal entries are a strong start, but they are not yet rich
enough to drive TME simulation without substantial hand engineering.

| Dimension | Current dismech CRC coverage | Major gaps for TME modeling |
|-----------|------------------------------|-----------------------------|
| Tumor-intrinsic programs | Strong: APC/WNT, KRAS/BRAF, HER2, MSI, metastasis | Needs tighter linkage from tumor genotype to secreted factors and phenotype switching |
| Adaptive immunity | Moderate: MSI-high CRC already models CD8 T-cell response and PD-L1-mediated adaptive resistance | Missing dendritic cell priming, Treg suppression, NK-cell activity, antigen presentation failure, immune exclusion states |
| Myeloid compartment | Weak | Need TAMs, MDSCs, neutrophils, inflammatory monocytes, cytokine loops, macrophage polarization logic |
| Stromal compartment | Weak to moderate: metastatic CRC mentions stromal cooperation and CAF-like support | Need explicit CAF states, ECM remodeling, stiffness, TGF-beta loops, fibroblast-immune crosstalk |
| Vasculature and hypoxia | Weak to moderate: metastatic CRC includes angiogenesis | Need endothelial cells, pericytes, perfusion failure, VEGF signaling, hypoxia-driven phenotype change |
| Metabolic suppression | Minimal | Need lactate, adenosine, glutamine competition, acidification, macrophage/T-cell metabolic rewiring |
| Spatial organization | Minimal | Need invasive margin vs core, immune-excluded vs inflamed vs desert states, liver metastatic niche geography |
| Macroenvironment | Minimal | Need microbiome, obesity/metabolic inflammation, liver systemic tolerance, bone marrow myelopoiesis, circulating mediators |

### Immediate CRC priorities

1. Add explicit immune suppressor and stromal effector cell types to the
   colorectal entries: CAFs, TAMs, MDSCs, Tregs, endothelial cells, pericytes.
2. Add missing processes that are central to simulator behavior:
   angiogenesis, hypoxia response, extracellular matrix remodeling, leukocyte
   trafficking, metabolic competition, and immune exclusion.
3. Represent organ-specific metastatic ecology in metastatic CRC, especially the
   liver niche, rather than treating metastasis as a tumor-cell-only phenotype.
4. Capture subtype-specific TME distinctions instead of one generic CRC
   environment. MSI-high, BRAF-mutant, HER2-positive, and metastatic CRC should
   not share the same default ecosystem logic.

## Proposed `tumor_ecosystem` Module

This should be a reusable mechanism module in `kb/modules/` using the same
schema as existing disorder entries.

### Design principles

1. Keep the module generic enough to reuse across solid tumors.
2. Let conforming entries substitute organ- and tumor-specific cell types.
3. Reuse existing module nodes where possible instead of duplicating them.
4. Separate minimal conserved logic from disease-specific specialization.

### Candidate conserved nodes

| Node | Role | Typical actors |
|------|------|----------------|
| Tumor Cell Diversification and Plasticity | trigger | tumor cell, cancer stem-like cell |
| Antigenicity and Immune Priming | early immune engagement | tumor cell, dendritic cell, CD8 T cell |
| Adaptive Immune Resistance | conserved immune evasion | tumor cell, exhausted T cell |
| Myeloid Recruitment and Immunosuppression | amplifier | TAM, MDSC, neutrophil |
| Stromal Activation and ECM Remodeling | amplifier | CAF, fibroblast, myofibroblast-like stromal cell |
| Angiogenesis and Hypoxic Adaptation | amplifier | endothelial cell, pericyte, tumor cell |
| Metabolic Competition and Immunosuppressive Metabolites | amplifier | tumor cell, T cell, macrophage |
| Spatial Exclusion / Barrier Formation | state-shaping | CAF, endothelial cell, ECM, T cell |
| Metastatic Niche Conditioning | dissemination support | tumor cell, organ-resident stromal/immune cells |
| Macroenvironmental Reinforcement | systemic feedback | bone marrow, liver, microbiome-linked immune tone, circulating cytokines |

### Relationship to existing modules

- `immune_checkpoint_blockade#Adaptive Immune Resistance` should remain a
  reusable conformance target inside the broader tumor ecosystem model.
- `fibrotic_response` is a useful design precedent for stromal remodeling and
  myofibroblast-like state transitions.
- A future `angiogenesis_inhibition` module would likely plug into this same
  ecosystem architecture.

## Export Format for Agent-Based Models and Digital Twins

Raw triples are necessary but not sufficient.

The claim-extraction roadmap in issue `#1100` is important because it should
produce machine-queryable statements such as:

`(cell_type_A, process_X, cell_type_B)`

However, a simulator needs more than that. It also needs direction, sign,
conditions, spatial scope, and action semantics.

### Recommended layered export

1. **Claim triples**
   Minimal extraction layer for indexing and search.
2. **Rule objects**
   Simulator-neutral mechanism objects with enough fields to execute or compile.
3. **Backend adapters**
   Translators from the neutral rule objects into PhysiCell, TumorTwin, or other
   framework-specific inputs.

### Minimal simulator-neutral rule schema

```json
{
  "disease": "MSI_High_Colorectal_Cancer",
  "module_node": "immune_checkpoint_blockade#Adaptive Immune Resistance",
  "source_cell_type": "tumor cell",
  "signal_or_process": "PD-L1 upregulation",
  "target_cell_type": "CD8-positive, alpha-beta T cell",
  "target_process": "T cell mediated cytotoxicity",
  "effect": "decrease",
  "context": {
    "anatomical_site": "colon tumor",
    "spatial_region": "tumor-immune interface",
    "disease_subtype": "MSI-high"
  },
  "evidence_weight": "high",
  "references": ["PMID:38762484"]
}
```

### What a PhysiCell-style importer would need

- Cell definitions derived from dismech cell type descriptors
- Secreted substrates or state variables derived from cytokines, metabolites, or
  signaling processes
- Update rules mapping mechanism objects to proliferation, death, motility,
  exhaustion, recruitment, or secretion parameter changes
- Therapy actions that toggle or attenuate specific mechanism nodes
- Spatial constraints that distinguish core, invasive margin, vasculature, and
  metastatic niche compartments

### Key point

dismech does not need to become the simulator. It needs to become the
mechanistic interchange layer between curation and simulation.

## Key References

- [PhysiCell: An open source physics-based cell simulator for 3-D multicellular systems](https://pmc.ncbi.nlm.nih.gov/articles/PMC5841829/)
- [PhysiCell project website](https://physicell.org/)
- [PhysiGym: bridging the gap between the Gymnasium reinforcement learning application interface and the PhysiCell agent-based model software](https://connect.biorxiv.org/archive/show_cat.php?cat=scientific+communication+and+education)
- [GigaTIME: multimodal AI generates virtual population for tumor microenvironment modeling](https://www.microsoft.com/en-us/research/publication/multimodal-ai-generates-virtual-population-for-tumor-microenvironment-modeling/)
- [GigaTIME coverage in Microsoft Research 2025 year in review](https://www.microsoft.com/en-us/research/story/microsoft-research-2025-a-year-in-review/)
- [TumorTwin: A python framework for patient-specific digital twins in oncology](https://pubmed.ncbi.nlm.nih.gov/40342863/)
- [Computational Resources for Cancer Research portal](https://computational.cancer.gov/)
- [M4RL: multiscale mathematical model-informed reinforcement learning optimizes combination treatment scheduling in glioblastoma evolution](https://pubmed.ncbi.nlm.nih.gov/40779623/)
- [SMMART serial-biopsy ecosystem analysis in advanced breast cancer](https://pubmed.ncbi.nlm.nih.gov/33772089/)
- [SMMART clinical trials research at OHSU](https://www.ohsu.edu/knight-cancer-institute/smmart-clinical-trials-research)

## Candidate Diseases for Expansion Beyond CRC

| Disease | Why TME enrichment is especially valuable |
|---------|-------------------------------------------|
| `Pancreatic_Ductal_Adenocarcinoma.yaml` and `Metastatic_Pancreatic_Adenocarcinoma.yaml` | Canonical desmoplastic, CAF-rich, immune-excluded tumor ecosystem |
| `Glioblastoma_IDH_Wildtype.yaml` | Direct fit for M4RL-style TAM-driven scheduling models and TumorTwin-style digital twins |
| `Hepatocellular_Carcinoma.yaml` | Strong interplay among tumor cells, fibrosis, angiogenesis, and the tolerogenic liver macroenvironment |
| `Non-Small_Cell_Lung_Cancer.yaml`, `EGFR_Mutant_NSCLC.yaml`, `KRAS_G12C_Mutant_NSCLC.yaml`, `Metastatic_NSCLC.yaml` | Mature immunotherapy and targeted-therapy landscape with clear TME-mediated response heterogeneity |
| `Triple_Negative_Breast_Cancer.yaml` and `HER2_Positive_Breast_Cancer.yaml` | Strong SMMART relevance and rich literature on subtype-specific immune and stromal response states |
| `Ovarian_High-Grade_Serous_Carcinoma.yaml` | Ascites, mesothelial interaction, immune dysfunction, and metastatic niche biology are central |
| `Clear_Cell_Renal_Cell_Carcinoma.yaml` and `Metastatic_Renal_Cell_Carcinoma.yaml` | Angiogenesis and immunotherapy are already central clinical levers, making ecosystem modeling highly actionable |

## Deliverables This Project Should Produce

1. A TME gap-analysis rubric for cancer entries in dismech
2. A reusable `tumor_ecosystem` mechanism module
3. A simulator-neutral interaction rule export format
4. A CRC pilot that shows the curation-to-simulation workflow end to end
5. A short list of next cancers where TME enrichment has the highest payoff

## Notes

### 2026-04-12

Project created to evaluate dismech as a mechanistic layer for tumor ecosystem
modeling.

Key observations:

1. CRC is the right pilot because the KB already contains a spectrum from
   baseline adenocarcinoma to MSI-high immune-responsive disease to metastatic
   seed-and-soil biology.
2. The existing `immune_checkpoint_blockade` module is already a genuine TME
   module, just a narrow one centered on adaptive immune resistance.
3. The biggest missing piece is not literature volume but representation:
   simulators need explicit actors, signals, states, and spatial context.
4. GigaTIME-like systems can help initialize or infer TME state from routine
   pathology, while PhysiCell, M4RL, and digital twin frameworks can use
   dismech-derived rules for forward simulation and intervention search.
5. The project should treat raw claim triples as an intermediate product, not
   the final export. Executable simulation rules need richer structure.
6. First high-confidence attachable PhysiCell anchors for dismech are already
   available in the official `grammar_samples` release: `epi_caf_invasion` and
   `pdac_therapy` for PDAC, plus `tumor_immune_base` and
   `tumor_immune_extended` as reusable tumor-immune exemplars.
