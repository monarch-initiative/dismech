# Cellular Senescence Network (SenNet)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

SenNet is highly mechanistic because senescence is a cell state that can be a
trigger, amplifier, effector, or protective response depending on tissue and
context. The Common Fund page describes SenNet as an effort to identify and
characterize senescent cells across the body, health states, and lifespan, and
to provide atlases of senescent cells and the molecules they secrete.

Dismech can use SenNet to avoid treating senescence as a vague aging label.
Instead, senescence can be represented as a state transition with cell type,
secretome, tissue neighborhood, and disease consequence.

## Dismech Interpretation Pattern

Use SenNet data to specify where senescence sits in a disease pathograph:

`cellular stress or damage -> senescence induction -> SASP / immune recruitment
or immune evasion -> tissue remodeling, fibrosis, degeneration, cancer
promotion, or impaired repair`

Senescence should be curated with directionality: beneficial tumor suppression
or wound repair in one context can become chronic inflammatory amplification in
another.

## Concrete Implementation Plan

**Mode:** teach dismech. SenNet should teach a reusable, cell-type-specific
senescence module. It becomes a benchmark only after the module can be used to
interpret held-out SenNet cell states without flattening them into a generic
"aging" label.

**Required datasets and access path:**

- Start with the SenNet Data Sharing Portal:
  https://data.sennetconsortium.org/ and the software docs:
  https://docs.sennetconsortium.org/.
- Use the SenNet Data Overview and API Index from the documentation to identify
  published primary datasets by organism, tissue, assay, and status. The docs
  describe primary datasets from assays such as histology, single-cell RNA-seq,
  spatial transcriptomics, and proteomics.
- Use the SenNet Biomarkers tool from the docs as a curated source of candidate
  senescence markers, but validate each marker in tissue context before using it
  as mechanism evidence.
- Record per-dataset access status from the portal. Metadata and search are
  public, but individual files and derived objects should be treated according
  to portal-level access flags rather than assumed open.

**Tools and environment:**

- Python client around SenNet search/retrieval APIs, plus `pandas` and
  `requests` for metadata harvesting.
- For single-cell or spatial work: `scanpy`, `anndata`, `squidpy`, or Seurat in
  R, depending on released file format.
- Ontology mapping to CL, UBERON, GO, and dismech `cell_types`/`tissue_term`
  slots; keep biomarker panels separate from asserted mechanisms until a cell
  state and tissue neighborhood are explicit.

**Curation targets:**

- Create `kb/modules/cellular_senescence.yaml` with stress induction, DNA damage
  response, p53/p21 or p16/RB cell-cycle arrest, SASP, immune clearance,
  immune evasion, tissue remodeling, and functional decline.
- Add module specializations to `Osteoarthritis`, `Idiopathic_Pulmonary_Fibrosis`,
  `Chronic_Kidney_Disease`, and `Systemic_Sclerosis`.
- Use `Nestor-Guillermo_progeria_syndrome` and `Penttinen_Premature_Aging_Syndrome`
  as rare-disease anchors for premature senescence biology only where their
  existing mechanisms support that link.

**Code to write:**

- Add `src/dismech/commonfund/sennet.py` to harvest portal metadata into a
  manifest with dataset id, assay, species, organ, cell type if available,
  senescence marker panel, access status, and portal URL.
- Add `scripts/sennet_marker_to_module.py` to map SenNet biomarker terms to
  candidate dismech module nodes and flag unsupported generic claims.
- Add schema-review notes for assay types not yet covered by `DatasetTypeEnum`,
  especially histology/imaging and senescence biomarker panels.

**Graduate-student first pass:**

1. Pick one organ where dismech already has strong disease files, preferably
   lung, kidney, joint/cartilage, or skin.
2. Export 5-10 SenNet datasets for that organ, with assay, species, tissue,
   cell-type annotations, and access status.
3. For each senescent cell state, write the exact causal placement: upstream
   inducer, senescent cell type, secreted or contact-mediated effect, recipient
   cell/tissue, and disease phenotype.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How SenNet helps |
|---------|--------------------------------|------------------|
| `Osteoarthritis` | Curated nodes: `Cartilage Matrix Catabolism`, `Chondrocyte Senescence`, `Synovial Macrophage-Fibroblast Crosstalk`, `Subchondral Bone Remodeling` | Best immediate pilot. SenNet can add cell-state and secretome evidence for senescent chondrocytes and synovial inflammatory amplification. |
| `Idiopathic_Pulmonary_Fibrosis` | Curated nodes conform to `fibrotic_response`: `Repetitive alveolar epithelial injury and aberrant repair`, `Profibrotic macrophage recruitment and amplification`, `Fibroblast activation and myofibroblast differentiation`, `Excessive extracellular matrix deposition` | Add senescent alveolar epithelial or fibroblast states as upstream amplifiers of the fibrotic module. |
| `Chronic_Kidney_Disease` | Curated nodes: `Nephron Loss`, `Glomerulosclerosis`, `Tubulointerstitial Fibrosis`, `RAAS Activation` | Add tubular epithelial senescence and SASP-driven interstitial fibrosis as CKD progression mechanisms. |
| `Systemic_Sclerosis` | Curated nodes: `Vascular Injury and Endothelial Dysfunction`, `Immune Activation and Autoantibody Production`, `Fibroblast Activation and Fibrosis`, `Systemic Sclerosis-Associated Interstitial Lung Disease` | SenNet can distinguish senescent endothelial, immune, and fibroblast-like states in fibrotic disease. |
| `Nestor-Guillermo_progeria_syndrome` | Curated nodes: `BANF1 mutation`, `Impaired DNA binding by BAF`, `Nuclear envelope and chromatin dysregulation` | Use as a rare progeroid anchor for nuclear envelope dysfunction, DNA damage, and premature senescence. |
| `Penttinen_Premature_Aging_Syndrome` | Curated nodes: `PDGFRB Gain-of-Function Mutations`, `Constitutive PDGFRB Activation`, `Connective Tissue Degeneration`, `Osteopenia` | Candidate addition: aberrant PDGFRB signaling -> stromal senescence/remodeling -> premature-aging phenotype. |
| `Pancreatic_Ductal_Adenocarcinoma` | Curated nodes: `KRAS Oncogene Activation`, `Desmoplastic Stroma`, `CAF-Mediated T Cell Exclusion`, `Immune Evasion` | Senescence can be modeled as a tumor-suppressive barrier or SASP-driven stromal amplifier depending on stage. |

## High-Value Curation Work

- Create a `cellular_senescence` module with nodes for stress induction, cell
  cycle arrest, SASP, immune clearance failure, tissue remodeling, and
  functional decline.
- Add senescence-specialized child nodes to the existing `fibrotic_response`
  module rather than duplicating a separate fibrosis graph.
- Add SenNet-backed `datasets` to `Osteoarthritis`, `Idiopathic_Pulmonary_Fibrosis`,
  `Chronic_Kidney_Disease`, and `Systemic_Sclerosis`.
- Keep senescence evidence cell-type-specific. A generic p16/p21 signal is less
  useful than "senescent chondrocyte", "senescent alveolar epithelial cell", or
  "senescent tubular epithelial cell" attached to a tissue context.

## Fit for RFA-RM-26-017

Best partner datasets:

- SenNet + HuBMAP: senescence overlaid on healthy tissue maps.
- SenNet + GTEx: senescence-related expression signatures in tissue context.
- SenNet + SMaHT: somatic mutation burden and senescent cell states across age.
- SenNet + MoTrPAC: exercise-responsive modulation of aging and senescence
  pathways.

## Sources

- NIH Common Fund SenNet: https://commonfund.nih.gov/senescence
- SenNet FAQ: https://commonfund.nih.gov/senescence/foafaqs
- SenNet data portal: https://data.sennetconsortium.org/
- SenNet software and API docs: https://docs.sennetconsortium.org/
