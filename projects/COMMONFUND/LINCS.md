# Library of Integrated Network-Based Cellular Signatures (LINCS)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

LINCS is mechanistically valuable because it measures how cells respond to
perturbagens. The Common Fund page describes LINCS as a library of changes that
occur when different cell types are exposed to perturbagens that disrupt normal
cellular function, integrating data across cell types, perturbagens, and
cellular response measurements. LINCS/L1000 data provide gene-expression
signatures for many perturbagens, doses, time points, and cell lines.

For dismech, LINCS can test whether a perturbation mimics or reverses a disease
mechanism state.

## Dismech Interpretation Pattern

Use LINCS for perturbation-to-mechanism interpretation:

`disease mechanism signature -> LINCS perturbagen or genetic perturbation
signature -> reversal, mimicry, or pathway concordance -> treatment hypothesis,
mechanism validation, or adverse-event hypothesis`

Cell type matters. A reversal signature in an irrelevant cell line should be
treated as hypothesis-generating.

## Concrete Implementation Plan

**Mode:** benchmark perturbation interpretation. LINCS should test whether
dismech can turn a disease mechanism signature into a perturbagen hypothesis
with explicit direction, cell-line relevance, and target/pathway caveats.

**Required datasets and access path:**

- Use LINCS/CLUE data guidance and GEO accessions. The CLUE GEO guide states
  that LINCS-funded CMap L1000 data are publicly available in GEO, including
  Phase I `GSE92742`, Phase II `GSE70138`, RNAi/CRISPR subset `GSE106127`, and
  contest dataset `GSE92743`.
- Use Level 5 consensus signatures for first-pass mechanism matching; use lower
  levels only when auditing replicate or QC behavior.
- Use CLUE tools for interactive L1000 queries when acceptable; use GEO bulk
  matrices and metadata for reproducible dismech reports.
- Always record perturbagen, dose, time, cell line, signature level, GEO
  accession, and whether the perturbation is chemical or genetic.

**Tools and environment:**

- Python with `cmapPy` for GCT/GCTX matrices, `pandas`, `numpy`, and
  `scipy`; or R with clue/lincs-compatible matrix tooling.
- Gene-set scoring using signed disease mechanism signatures: up genes, down
  genes, expected pathway direction, and cell-type filter.
- IDG/Pharos and DrugCentral/ChEMBL crosswalks for target annotations.

**Curation targets:**

- Oncology benchmark: `Chronic_Myeloid_Leukemia`,
  `BRAF_V600_Mutant_Melanoma`, `ALK_Rearranged_NSCLC`,
  `RET_Rearranged_NSCLC`, and `FGFR_Altered_Urothelial_Carcinoma`.
- Immune/inflammatory benchmark: `Rheumatoid_Arthritis`,
  `Systemic_Lupus_Erythematosus`, and `Type_I_Diabetes`.
- Signaling/overgrowth benchmark: `PTEN_Hamartoma_Tumor_Syndrome` and
  `CLOVES_Syndrome`.

**Code to write:**

- Add `src/dismech/commonfund/lincs.py` for loading L1000 metadata and Level 5
  signatures, scoring disease gene sets, and returning top mimic/reversal
  perturbagens.
- Add `scripts/lincs_dismech_signature_benchmark.py` that builds signatures
  from selected dismech mechanism genes and emits a report with cell-line
  relevance and IDG target annotations.
- Add schema-review notes for perturbation signatures, dose/time metadata,
  cell-line models, and directionality of computational evidence.

**Graduate-student first pass:**

1. Select one disease with a clean pathway signature, such as CML, BRAF-mutant
   melanoma, SLE interferon activation, or PTEN/PI3K activation.
2. Create a signed gene set from dismech and primary literature.
3. Query LINCS Level 5 signatures for reversal and mimicry. Keep the top hits
   only if the cell line and perturbagen mechanism are biologically plausible.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How LINCS helps |
|---------|--------------------------------|-----------------|
| `BRAF_V600_Mutant_Melanoma` | Curated nodes: `BRAF V600 Oncogenic Mutation`, `Constitutive MAPK Pathway Activation`, `Acquired MAPK Reactivation and Bypass Resistance`, `Immune Evasion via PD-L1 Upregulation` | LINCS can test MAPK inhibitor response, bypass activation, and combination perturbation signatures. |
| `Chronic_Myeloid_Leukemia` | Curated nodes: `Constitutive Tyrosine Kinase Activation`, `RAS-MAPK Pathway Hyperactivation`, `PI3K-AKT Pathway Activation`, `JAK-STAT Pathway Activation` | Use imatinib/dasatinib signatures as a reference pattern for disease-state reversal. |
| `Rheumatoid_Arthritis` | Curated nodes: `Autoimmune Response`, `Inflammatory Cytokine Production`, `Synovial Hyperplasia`, `JAK/STAT Signaling`, `NF-kB Activation` | LINCS can prioritize perturbagens that reverse inflammatory cytokine or JAK/STAT signatures. |
| `Systemic_Lupus_Erythematosus` | Curated nodes: `Type I Interferon Pathway Activation`, `TLR7/TLR9-Mediated Nucleic Acid Sensing`, `NETosis and Neutrophil Extracellular Trap Formation`, `Epigenetic Dysregulation and T Cell Metabolic Reprogramming` | Perturbation signatures can test interferon/TLR pathway modulation and candidate immunometabolic interventions. |
| `Type_I_Diabetes` | Curated nodes: `Interferon-Driven Beta Cell Response`, `Autoimmune Destruction of Beta Cells`, `ER Stress and Unfolded Protein Response` | Candidate use: beta-cell stress reversal and immune-modulatory perturbation signatures. |
| `Pancreatic_Ductal_Adenocarcinoma` | Curated nodes: `KRAS Oncogene Activation`, `Desmoplastic Stroma`, `CAF-Mediated T Cell Exclusion`, `Immune Evasion` | LINCS can support drug repurposing and KRAS pathway modifier hypotheses, with cell-line relevance caveats. |
| `PTEN_Hamartoma_Tumor_Syndrome` | Curated nodes: `PTEN loss and PI3K AKT mTOR activation`, `Hamartomatous tissue overgrowth`, `Multiorgan cancer predisposition` | Perturbation signatures can test PI3K/AKT/mTOR inhibitors and pathway modifiers. |

## High-Value Curation Work

- Add a LINCS interpretation field pattern in project reports, not necessarily
  disorder YAML first: disease node, expected direction, perturbagen, cell line,
  signature direction, and confidence.
- Start with diseases that already have clear pathway nodes and treatments:
  CML, BRAF melanoma, FGFR/ALK/RET cancers, RA, SLE, and T1D.
- Use LINCS as computational or in vitro evidence depending on the underlying
  dataset and experiment, never as human clinical evidence by default.
- Pair LINCS with IDG for target prioritization and with MoTrPAC for
  exercise/drug signature comparisons.

## Fit for RFA-RM-26-017

Best partner datasets:

- LINCS + IDG: perturbation signatures plus druggable target annotations.
- LINCS + MoTrPAC: drug/exercise signature overlap.
- LINCS + Bridge2AI: AI-ready perturbation interpretation.
- LINCS + GTEx/HuBMAP: tissue and cell-type plausibility filters.

## Sources

- NIH Common Fund LINCS: https://commonfund.nih.gov/LINCS
- LINCS project L1000 data guidance: https://lincsproject.org/LINCS/tools/workflows/find-the-best-place-to-obtain-the-lincs-l1000-data/
- CLUE GEO L1000 guide: https://clue.io/geo-guide
- GEO GSE92742: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE92742
- GEO GSE70138: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE70138
- LINCS health relevance: https://commonfund.nih.gov/library-integrated-network-based-cellular-signatures-lincs/health-relevance
