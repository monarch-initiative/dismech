# Virtual Cell Alignment Project

## Overview
Align the dismech knowledge base with the CZI Virtual Cell initiative, enabling
disease mechanism data to connect with single-cell foundation models (scGPT, UCE,
TranscriptFormer, GREmLN, rBio) and the CELLxGENE Census data platform.

The CZI Virtual Cell project builds AI-based "digital twins" of human cells --
large neural-network models that simulate cellular behavior across molecular and
structural scales. dismech's structured disease pathophysiology data (cell types,
biological processes, gene products, perturbation targets) is a natural complement:
it provides the disease-context layer that virtual cell models need for translational
predictions.

## Key CZI Resources
- **CELLxGENE Discover**: Largest standardized single-cell data aggregation (tens of millions of cells)
- **CELLxGENE Census**: Computational query layer with Python/R APIs (TileDB-SOMA)
- **Virtual Cells Platform (VCP)**: Model hosting at virtualcellmodels.cziscience.com
- **Models**: scGPT, UCE, scGenePT, TranscriptFormer, GREmLN, rBio
- **Billion Cells Project**: 1B single-cell profiles mapping genetic perturbations

## Reference Papers
| Year | Paper | DOI/PMID |
|------|-------|----------|
| 2024 | How to build the virtual cell with AI | Cell 187(25):7045-7063, PMID:39672099 |
| 2024 | scGPT: single-cell foundation model | Nature Methods 21:1470-1480 |
| 2025 | Zero-shot evaluation of single-cell foundation models | Genome Biology, PMC12007350 |
| 2025 | Gene perturbation prediction vs linear baselines | Nature Methods |
| 2025 | GREmLN: graph-aware single-cell model | bioRxiv 2025.07.03.663009 |
| 2025 | rBio: reasoning model on virtual cell simulations | CZI blog + GitHub czi-ai/rbio |

---

## Tasks

### Tier 1: Low Effort (schema/config changes, data annotation)

- [x] Add `cellxgene:` prefix to schema for CELLxGENE dataset accessions
- [ ] Add CELLxGENE dataset references to disorders that already have `datasets` sections
- [ ] Add CELLxGENE dataset references to disorders with `cell_types` but no datasets
- [ ] Document CL term coverage: which dismech cell types have CELLxGENE representation

### Tier 2: Medium Effort (new data fields, cross-references)

- [ ] Add marker gene sets to CellTypeDescriptor entries (genes used by scGPT/UCE for cell identity)
- [ ] Cross-reference dismech biological_processes with GO terms used in scGenePT gene embeddings
- [ ] Link pathophysiology gene_products to perturbation datasets (e.g., Perturb-seq screens)
- [ ] Add `computational_models` section to Disease class for virtual cell model predictions
- [ ] Populate HCA project references (prefix exists but unused)

### Tier 3: High Effort (schema extensions, integrations)

- [ ] Schema extension: PerturbationPrediction class linking gene perturbations to predicted cell state changes
- [ ] CELLxGENE Census API integration for automated cell type enrichment of disorder files
- [ ] Rendering: cell-level molecular data views in HTML pages (embedding visualizations, gene programs)
- [ ] Schema extension: GeneProgram class for co-expression modules identified by TranscriptFormer
- [ ] Integration with rBio for automated perturbation reasoning over dismech gene targets
- [ ] Add support for embedding-based cell similarity annotations (UCE latent space distances)

### Tier 4: Aspirational (research directions)

- [ ] Map dismech treatment targets to virtual cell perturbation predictions (drug target -> predicted cell response)
- [ ] Use virtual cell models to predict novel cell types affected by disease mechanisms
- [ ] Connect comorbidity trajectories to shared cell-state perturbation signatures
- [ ] Validate dismech pathophysiology claims against scRNA-seq differential expression

---

# STATUS

## Tier 1 Progress
- [x] `cellxgene:` prefix added to schema (2026-03-07)
- [ ] CELLxGENE dataset annotation (0/N disorders)
- [ ] CL term coverage audit (0/N)

## Notes

### 2026-03-07 (Project Creation)

Project created to align dismech with CZI Virtual Cell initiative.

**Low-effort wins identified:**
1. Schema already has `SINGLE_CELL_RNA_SEQ` data type, `hca:` prefix, cell type descriptors with CL terms, and dataset infrastructure
2. Adding `cellxgene:` prefix is a one-line schema change
3. Several disorders already have datasets sections that could be augmented with CELLxGENE references
4. Cell type annotations in pathophysiology already use CL ontology terms that map directly to CELLxGENE cell type annotations

**Key gap:** No existing CELLxGENE references in any disorder file despite infrastructure support.

**Schema observations:**
- `DatasetTypeEnum` already includes `SINGLE_CELL_RNA_SEQ` and `SPATIAL_TRANSCRIPTOMICS`
- `SampleTypeDescriptor` already has `cell_type_term` (CL binding) and `tissue_term` (UBERON binding)
- `hca:` prefix configured but unused across all disorder files
- `cellxgene:` prefix missing entirely
