# Human BioMolecular Atlas Program (HuBMAP)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

HuBMAP provides healthy human tissue maps at cellular and spatial resolution.
The Common Fund page describes HuBMAP as building tools, resources, and cell
atlases to determine how relationships between cells affect health. HuBMAP FAQ
material emphasizes quantitative spatial readouts of biomolecules such as
proteins, RNA, DNA, and metabolites, plus imaging and histology.

For dismech, HuBMAP is the reference context for asking: which cell type,
microenvironment, anatomic compartment, or tissue neighborhood is the disease
mechanism perturbing?

## Dismech Interpretation Pattern

Use HuBMAP as the healthy baseline and localization layer:

`healthy cell type / tissue neighborhood -> disease injury, activation,
senescence, immune infiltration, fibrosis, malignant transformation, or
developmental defect -> phenotype`

HuBMAP is especially useful when a disease entry has broad cell-type labels but
needs organ-specific cellular neighborhoods.

## Concrete Implementation Plan

**Mode:** benchmark dismech localization and teach cell-context curation.
HuBMAP is healthy tissue reference data, so its strongest role is checking
whether dismech mechanisms mention the right cells, compartments, and
neighborhoods.

**Required datasets and access path:**

- Use the HuBMAP Data Portal: https://portal.hubmapconsortium.org/ and the
  consortium data page: https://hubmapconsortium.org/hubmap-data/.
- Portal metadata can be browsed without login. The HuBMAP data page says users
  can browse donors, samples, datasets, collections, organs, specimen types,
  assay types, donor information, and affiliations. Processed data downloads
  require Globus login with institutional or eRA Commons credentials.
- Use the Human Reference Atlas and ASCT+B/HRA tools for anatomical structures,
  cell types, biomarkers, and spatial positions: https://humanatlas.io/.
- For each candidate dataset, record organ, assay, specimen type, donor
  metadata availability, protocol link, QC report link, and whether files are
  open or restricted.

**Tools and environment:**

- Portal search/API queries plus `pandas` for manifests.
- Vitessce for visual inspection, HRA Exploration User Interface for anatomical
  context, and `scanpy`/Seurat/squidpy for single-cell or spatial matrices when
  downloaded.
- Ontology mapping to UBERON and CL. Keep HuBMAP entity identifiers and HRA
  terms in a crosswalk rather than forcing every structure into free text.

**Curation targets:**

- `Chronic_Kidney_Disease`: glomerular, tubular, endothelial, pericyte, and
  immune localization of fibrosis/progression mechanisms.
- `Type_I_Diabetes`: beta cell, islet immune, endothelial, and stromal context.
- `Idiopathic_Pulmonary_Fibrosis`: alveolar epithelial injury, macrophage
  niche, fibroblast foci, and ECM deposition.
- `Ulcerative_Colitis`: epithelial barrier, immune infiltrate, crypt/stromal
  compartments, and mucosal repair.
- `Heart_Failure` and `Pancreatic_Ductal_Adenocarcinoma`: normal tissue
  baseline for remodeling or tumor microenvironment overlays.

**Code to write:**

- Add `src/dismech/commonfund/hubmap.py` to export dataset manifests by organ
  and assay with portal URL, HuBMAP id, organ, assay, file access status,
  protocol, QC URL, UBERON term, and CL/HRA cell terms if available.
- Add `scripts/hubmap_localization_audit.py` to compare dismech disease nodes
  against expected tissue/cell annotations and flag vague labels like
  "epithelial cells" when a more specific CL/HRA term is available.
- Add schema-review notes for spatial coordinates, healthy-reference datasets,
  organ maps, and dataset-level QC links.

**Graduate-student first pass:**

1. Pick one organ and one disease with a strong existing file: kidney/CKD,
   lung/IPF, colon/UC, or pancreas/T1D.
2. Build a HuBMAP manifest of 10 relevant healthy datasets and inspect one in
   Vitessce or HRA.
3. Annotate three dismech mechanism nodes with specific tissue and cell-type
   terms, then explicitly mark HuBMAP as localization/baseline evidence rather
   than disease causality.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How HuBMAP helps |
|---------|--------------------------------|------------------|
| `Chronic_Kidney_Disease` | Curated nodes: `Nephron Loss`, `Glomerulosclerosis`, `Tubulointerstitial Fibrosis`, `RAAS Activation` | Use kidney atlas context to place glomerular, tubular, endothelial, pericyte, and immune components of progression. |
| `Type_I_Diabetes` | Curated nodes: `Interferon-Driven Beta Cell Response`, `Autoimmune Destruction of Beta Cells`, `Insulin Deficiency`, `ER Stress and Unfolded Protein Response` | Pancreas/islet tissue maps can clarify beta-cell, immune-cell, endothelial, and stromal context. |
| `Idiopathic_Pulmonary_Fibrosis` | Curated nodes conform to `fibrotic_response`, including alveolar injury, macrophage amplification, fibroblast activation, and ECM deposition | Lung tissue maps can define the spatial transition from alveolar epithelial injury to fibroblast foci and gas-exchange failure. |
| `Ulcerative_Colitis` | Curated nodes: `Mucosal Inflammation`, `Epithelial Barrier Dysfunction`, `Loss of Keystone SCFA Producers`, `NLRP3 Inflammasome-Mediated Pyroptosis` | Healthy colon maps provide the epithelial, immune, and stromal baseline for disease overlay. |
| `Preeclampsia` | Curated nodes: `Defective Trophoblast Invasion and Spiral Artery Remodeling`, `Placental Anti-Angiogenic Factor Release`, `Maternal Endothelial Dysfunction` | Placental and vascular spatial context can support cell-neighborhood interpretation if relevant HuBMAP or companion tissue maps are available. |
| `Heart_Failure` | Curated nodes: `Myocardial Contractile Dysfunction`, `Neurohormonal Activation`, `Ventricular Remodeling`, `Fluid Retention` | Cardiac tissue maps can separate cardiomyocyte, fibroblast, vascular, and immune mechanisms in remodeling. |
| `Pancreatic_Ductal_Adenocarcinoma` | Curated nodes: `Desmoplastic Stroma`, `CAF-Mediated T Cell Exclusion`, `Immune Evasion` | HuBMAP can provide normal pancreas and duct/stroma spatial reference for tumor microenvironment interpretation. |

## High-Value Curation Work

- Add HuBMAP-backed `datasets` to entries where cell-type context drives the
  mechanism: kidney, pancreas, lung, colon, heart, and liver examples first.
- Create a disease overlay pattern: healthy HuBMAP tissue cell type -> disease
  pathophysiology node -> phenotype or histopathology feature.
- Use HuBMAP anatomical structure, cell type, and biomarker concepts to improve
  dismech `cell_types`, `tissue_term`, and `histopathology` curation.
- Avoid using healthy tissue maps as evidence that a disease mechanism occurs;
  they support localization and baseline interpretation, while disease samples
  or functional studies support causal claims.

## Fit for RFA-RM-26-017

Best partner datasets:

- HuBMAP + SenNet: senescent cell states in healthy tissue coordinates.
- HuBMAP + GTEx: spatial/single-cell context plus tissue expression/eQTLs.
- HuBMAP + HMP/iHMP: mucosal host-microbiome tissue context.
- HuBMAP + SMaHT: somatic variants localized to tissue and cell lineages.

## Sources

- NIH Common Fund HuBMAP: https://commonfund.nih.gov/hubmap
- HuBMAP portal: https://portal.hubmapconsortium.org/
- HuBMAP data page: https://hubmapconsortium.org/hubmap-data/
- Human Reference Atlas: https://humanatlas.io/
- HuBMAP FAQ: https://commonfund.nih.gov/HuBMAP/frequently-asked-questions
