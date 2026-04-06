# Organ Fibrosis Collaboration (Saez-Rodriguez Lab)

## Overview

Integrate the dismech knowledge base with the **cross-organ fibrosis atlas** from
the Saez-Rodriguez lab (Heidelberg / EMBL-EBI), an open single-cell resource
mapping shared and organ-specific fibrotic gene programs across heart, liver,
kidney, and lung.

The atlas provides quantitative molecular data (gene signatures, TF activities,
cell-cell communication, fibroblast subpopulations) while dismech provides
structured, evidence-backed disease mechanism context (causal chains, phenotypes,
treatments, clinical trials). The two are complementary: the atlas answers "what
changes?" and dismech answers "why it matters clinically."

## The Organ Fibrosis Atlas

**Resource:** https://organfibrosis.saezlab.org/
**Preprint:** Küchenhoff, Kim, Lanzer, Kretzler, Ramirez Flores & Saez-Rodriguez.
"Shared and organ-specific gene expression programs of fibrotic diseases."
bioRxiv 2026.03.09.709232v1.
**Code:** https://github.com/saezlab/organfibrosis
**License:** CC-BY-NC 4.0 (data), GPL-3.0 (code)

### What it provides

| Aspect | Detail |
|--------|--------|
| Scale | >5 million cells, 20 studies, 25+ disease etiologies |
| Organs | Heart, liver, kidney, lung |
| Data type | Single-cell / single-nucleus RNA-seq meta-analysis |
| Key outputs | Cross-organ gene expression programs, disease fibroblast subpopulations with ECM signatures, organ-specific vs conserved TF activity profiles, intercellular communication patterns |
| Pipeline | Snakemake, standard scRNA-seq tooling (likely scanpy/decoupler/liana ecosystem) |
| Interactive | Dash-based web app for gene-of-interest queries across fibrotic tissues |

### Related Saez lab resources

- **Kidney fibrosis multi-omics model** ([GitHub](https://github.com/saezlab/kidneyfibrosis_multiomicsmodel_paper)):
  14,000+ biomolecules across 7 time points post-TGF-β stimulation; temporal
  fibrosis marker discovery
- **Liver disease atlas** ([GitHub](https://github.com/saezlab/liver-disease-atlas)):
  Cross-species (human/mouse) chronic liver disease transcriptomics
- **ReHeaT** ([GitHub](https://github.com/saezlab/reheat)):
  Reference heart failure transcriptome

## Existing dismech coverage

### Disorders with explicit fibrotic mechanisms (21 files mention myofibroblasts/stellate cells)

| Disorder | Organ | Fibrosis mechanism |
|----------|-------|--------------------|
| **Liver Cirrhosis** | Liver | HSC → myofibroblast transdifferentiation, collagen/ECM deposition |
| **Primary Myelofibrosis** | Bone marrow | TGF-β/PDGF/bFGF → reticulin/collagen deposition |
| **Systemic Sclerosis** | Skin, lung, heart, kidney | Multi-organ fibrosis via myofibroblast activation |
| **Chronic Kidney Disease** | Kidney | Tubulointerstitial fibrosis |
| **Hepatitis B/C** | Liver | Viral-driven hepatic fibrosis |
| **Heart Failure** | Heart | Cardiac fibrosis/remodeling |
| **Dilated Cardiomyopathy** | Heart | Myocardial fibrosis |
| **Hypertensive Heart Disease** | Heart | Pressure-overload cardiac fibrosis |
| **Chronic Pancreatitis** | Pancreas | Pancreatic stellate cell activation |
| **Bird Fancier's Lung** | Lung | Hypersensitivity pneumonitis → pulmonary fibrosis |
| **IgG4-Related Disease** | Multi-organ | Storiform fibrosis |
| **Crohn Disease** | GI tract | Intestinal stricturing/fibrosis |
| **Polycystic Kidney Disease** | Kidney | Cystic renal fibrosis |
| **Cystic Fibrosis** | Lung, pancreas, liver | Epithelial-driven (not fibroblast-centric) |

### Broader fibrosis mentions

- 71 disorder files mention "fibrosis"
- 130 files mention TGF or collagen
- 68 files mention extracellular matrix

### Key gap: no Idiopathic Pulmonary Fibrosis (IPF) entry

IPF is the prototypical fibrotic lung disease and a major focus of the organ
fibrosis atlas. Creating this entry would be a high-value first deliverable.

## Integration strategy

### Value exchange

| dismech → Atlas | Atlas → dismech |
|----------------|-----------------|
| Curated disease mechanisms with causal chains and PMID evidence | Quantitative gene signatures per cell type per organ |
| Ontology-grounded cell types (CL), processes (GO), genes (HGNC) | Disease fibroblast subpopulation definitions |
| Treatment-mechanism linkages (drug → target pathway → phenotype) | Cross-organ conserved vs organ-specific programs |
| Clinical trial connections to fibrotic phenotypes | TF activity profiles and intercellular communication data |
| Comorbidity trajectories between fibrotic diseases | Validated gene sets for computational model enrichment |

### Alignment points

The dismech schema already supports everything needed for integration:

1. **Cell types** → CellTypeDescriptor with CL ontology. Atlas fibroblast
   subpopulations (e.g., ECM-producing disease fibroblasts) can be mapped to CL
   terms and added to pathophysiology entries.

2. **Gene signatures** → GeneDescriptor with HGNC. Cross-organ fibrosis genes
   identified by the atlas can populate `genes` slots in pathophysiology entries.

3. **Biological processes** → BiologicalProcessDescriptor with GO. Conserved
   fibrotic programs (ECM organization, TGF-β signaling, wound healing) already
   have GO terms.

4. **Datasets** → Dataset class with `SINGLE_CELL_RNA_SEQ` type. Atlas study
   accessions (GEO/Zenodo) can be referenced directly.

5. **Computational models** → ComputationalModel class. The Saez lab's
   multi-omics network models and TF activity inference could be represented.

6. **Cross-organ comparison** → The `comorbidities` field and Disease Trajectories
   integration can capture cross-organ fibrotic progression patterns.

---

## Tasks

### Tier 1: Low Effort (data annotation, new entries)

- [ ] Create IPF (Idiopathic Pulmonary Fibrosis) disorder entry — the archetypal fibrotic lung disease and central to the atlas
- [ ] Add Zenodo/GEO dataset references from the organ fibrosis atlas to existing entries (Liver Cirrhosis, Heart Failure, Dilated Cardiomyopathy, CKD)
- [ ] Enrich fibroblast/myofibroblast cell type descriptors in existing entries with CL terms for disease fibroblast subpopulations identified by the atlas
- [ ] Add cross-references between existing fibrotic disorders (comorbidities section) reflecting shared transcriptomic programs

### Tier 2: Medium Effort (new entries, deeper annotation)

- [ ] Create NASH/MASLD entry — major liver fibrosis etiology covered by the atlas
- [ ] Create Diabetic Nephropathy entry — kidney fibrosis etiology covered by the atlas
- [ ] Enrich Heart Failure and Dilated Cardiomyopathy with cardiac fibrosis gene signatures from atlas
- [ ] Add conserved fibrotic TF activity profiles (TF → target gene → biological process chains) to pathophysiology entries
- [ ] Add intercellular communication patterns (e.g., fibroblast ↔ macrophage crosstalk) as pathophysiology mechanisms with cell_types and biological_processes
- [ ] Reference Saez lab kidney fibrosis multi-omics model as a ComputationalModel entry in CKD

### Tier 3: High Effort (schema-level, cross-cutting)

- [ ] Define a "Conserved Fibrotic Response" shared pathophysiology module reusable across organ-specific entries (TGF-β activation → myofibroblast differentiation → ECM deposition → tissue stiffening)
- [ ] Add atlas-derived gene program annotations (co-expressed gene sets) — may need schema extension for GeneProgram class (synergy with VIRTUAL_CELL project)
- [ ] Integrate spatial transcriptomics data when atlas expands to spatial modality
- [ ] Cross-link fibrotic disease comorbidities with Disease Trajectories EHR data (synergy with COMORBIDITIES project)

### Tier 4: Aspirational (collaborative research)

- [ ] Joint validation: use dismech causal chains to interpret atlas gene signatures (which genes fall on known mechanism paths?)
- [ ] Use atlas data to discover novel cell types involved in dismech-curated mechanisms
- [ ] Propose shared fibrosis mechanisms as drug targets: cross-reference atlas conserved programs with dismech treatment entries
- [ ] Contribute dismech disease-context annotations back to the atlas as structured metadata
- [ ] Explore MorPhiC iPSC perturbation data for fibrosis-relevant genes (ISL1 for cardiac, NKX2-1 for lung)

---

## Cross-project synergies

| Project | Synergy |
|---------|---------|
| **VIRTUAL_CELL** | GeneProgram class needed for both; CELLxGENE datasets overlap with atlas source data; scGPT embeddings for fibroblast subpopulations |
| **COMORBIDITIES** | Cross-organ fibrotic progression (liver → cardiac, kidney → cardiac) informed by both EHR trajectories and atlas shared programs |
| **GWAS_MECHANISMS** | Fibrosis GWAS loci can be mapped to atlas cell-type-specific expression to assign mechanism context |

## Contact / Collaboration

- **PI:** Julio Saez-Rodriguez (EMBL-EBI, saezrodriguez@ebi.ac.uk)
- **First authors:** Leonie Küchenhoff, Gahyun Kim (Heidelberg)
- **Key collaborator:** Matthias Kretzler (Michigan, kidney fibrosis expertise)
- **Resource:** https://organfibrosis.saezlab.org/
- **Code:** https://github.com/saezlab/organfibrosis

## Notes

### 2026-03-12 (Project Creation)

Project created to explore collaboration with Saez-Rodriguez lab organ fibrosis atlas.

**Key observations:**
1. The preprint was posted March 9, 2026 — only 3 days ago. This is an ideal time
   to reach out for collaboration before publication.
2. dismech already has substantial fibrotic disease coverage (21 files with
   myofibroblast/stellate cell mechanisms, 71 files mentioning fibrosis).
3. The atlas covers 4 organs (heart, liver, kidney, lung) — dismech has entries for
   fibrotic diseases in all 4 but lacks IPF, the archetypal pulmonary fibrosis.
4. Schema is fully ready: CellTypeDescriptor, GeneDescriptor, Dataset (with
   scRNA-seq type), ComputationalModel all exist. No schema changes needed for
   Tier 1-2 work.
5. The Saez lab ecosystem (decoupler for TF/pathway activity, liana for cell-cell
   communication, liver disease atlas, ReHeaT) provides multiple integration
   points beyond the organ fibrosis atlas itself.
6. CC-BY-NC 4.0 license on the data is compatible with knowledge base annotation
   (citing/referencing, not redistributing raw data).
