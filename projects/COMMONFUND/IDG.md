# Illuminating the Druggable Genome (IDG)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

IDG is mechanistically useful because it connects understudied druggable
proteins to disease biology. The Common Fund page describes IDG as focusing on
understudied GPCRs, ion channels, and kinases, and on developing probes,
molecular tools, assays, transgenic mice, recombinant cell lines, data, and
digital resources. Pharos integrates data across many sources and exposes target
development levels.

Dismech can provide the disease-mechanism rationale for why an understudied
target matters.

## Dismech Interpretation Pattern

Use IDG to link disease mechanisms to actionable targets:

`pathophysiology node -> receptor, kinase, channel, or signaling protein ->
available ligand/probe/target-development evidence -> treatment hypothesis or
curation gap`

IDG is strongest where dismech already has a pathway node but weak treatment
mechanism annotation.

## Concrete Implementation Plan

**Mode:** benchmark dismech druggability interpretation. IDG/Pharos should test
whether dismech can start from a disease mechanism and return sensible target
classes, target development levels, probes, ligands, and treatment gaps.

**Required datasets and access path:**

- Use Pharos: https://pharos.nih.gov/ and API documentation:
  https://pharos.nih.gov/api.
- Use the current GraphQL endpoint for programmatic work:
  https://pharos-api.ncats.io/graphql. Pharos publications identify this as the
  GraphQL API and describe TCRD/Pharos target development levels.
- For each target, record symbol, UniProt if available, target family, target
  development level (`Tclin`, `Tchem`, `Tbio`, `Tdark`), disease associations,
  ligands, expression, and pathway annotations.
- Do not equate "druggable" with "therapeutic for this disease." A target needs
  a mapped dismech pathophysiology node and disease-relevant evidence.

**Tools and environment:**

- Python `requests` or a GraphQL client, with cached query outputs stored as
  generated artifacts rather than hand-written disease evidence.
- Optional bulk TCRD download only for large target audits; Pharos GraphQL is
  enough for first-pass disease-target reports.
- Crosswalk to HGNC, UniProt, ChEMBL/DrugCentral where needed, and MAXO
  treatments already curated in dismech.

**Curation targets:**

- Oncology benchmark set: `Chronic_Myeloid_Leukemia`, `ALK_Rearranged_NSCLC`,
  `RET_Rearranged_NSCLC`, `FGFR_Altered_Urothelial_Carcinoma`, and
  `BRAF_V600_Mutant_Melanoma`.
- Non-oncology pathway set: `CLOVES_Syndrome`, `Penttinen_Premature_Aging_Syndrome`,
  `Epilepsy`, pain disorders, fibrosis entries, and immune diseases.
- Add or repair treatment `mechanism_targets` where a drug acts on a named
  pathophysiology node.

**Code to write:**

- Add `src/dismech/commonfund/idg.py` with Pharos GraphQL query helpers for
  target detail and batch target-development-level lookup.
- Add `scripts/idg_target_audit.py` to scan dismech genes and treatments,
  return target class/TDL/ligand availability, and flag mechanism nodes that
  mention a targetable pathway but lack treatment annotations.
- Add tests with a mocked Pharos response so CI does not depend on live API
  availability.

**Graduate-student first pass:**

1. Build a 50-gene list from dismech mechanisms that name kinases, GPCRs, ion
   channels, nuclear receptors, and druggable enzymes.
2. Query Pharos for TDL and family. Split the list into established targets,
   chemical-probe targets, biology-only targets, and dark targets.
3. For five targets, write the full chain: disease mechanism node -> target ->
   ligand/probe or drug -> expected downstream phenotype change.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How IDG helps |
|---------|--------------------------------|---------------|
| `Chronic_Myeloid_Leukemia` | Curated nodes: `BCR-ABL1 Fusion Oncogene Formation`, `Constitutive Tyrosine Kinase Activation`, `RAS-MAPK Pathway Hyperactivation`, `PI3K-AKT Pathway Activation`, `JAK-STAT Pathway Activation` | Canonical targetable kinase contrast case; use it as the benchmark for mechanism-to-treatment curation. |
| `ALK_Rearranged_NSCLC` | Curated nodes: `ALK Gene Rearrangement`, `Constitutive ALK Signaling`, `Oncogene Addiction`, `ALK TKI Resistance` | Strong example of target class, resistance, and therapy linkage. |
| `RET_Rearranged_NSCLC` | Curated nodes: `RET Gene Rearrangement`, `Constitutive RET Signaling`, `Oncogene Addiction`, `RET Inhibitor Resistance` | Similar targetable kinase mechanism with specific inhibitors. |
| `FGFR_Altered_Urothelial_Carcinoma` | Curated nodes: `FGFR3 Constitutive Activation`, `RAS-MAPK Pathway Activation`, `PI3K-AKT Pathway Activation` | Good IDG-style target annotation around FGFR alterations and inhibitor therapy. |
| `BRAF_V600_Mutant_Melanoma` | Curated nodes: `BRAF V600 Oncogenic Mutation`, `Constitutive MAPK Pathway Activation`, `Acquired MAPK Reactivation and Bypass Resistance`, `Immune Evasion via PD-L1 Upregulation` | Use as a treatment-resistance and target-bypass model. |
| `CLOVES_Syndrome` | Curated nodes: `Constitutive PI3K Activation`, `AKT/mTOR Pathway Hyperactivation`, `Aberrant Vascular Development`; treatment `Alpelisib` | Non-cancer overgrowth example where druggable pathway logic applies to developmental mosaic disease. |
| `Penttinen_Premature_Aging_Syndrome` | Curated nodes: `PDGFRB Gain-of-Function Mutations`, `Constitutive PDGFRB Activation`, `Connective Tissue Degeneration`; treatments `Imatinib`, `Dasatinib` | Rare disease example where a targetable kinase mechanism is already explicit. |
| `Epilepsy` | Curated nodes: `Neuronal Hyperexcitability`, `Network Hyperexcitability`, `mTOR Pathway Hyperactivation` | Candidate IDG expansion: ion channel and GPCR target prioritization for subtype-specific mechanisms. |

## High-Value Curation Work

- Build an IDG target audit: dismech mechanisms mentioning kinases, GPCRs, or
  ion channels -> Pharos target development level -> treatment curation status.
- Add target-mechanism links in treatment entries where a drug clearly inhibits
  a curated pathophysiology node.
- Use CML, ALK/RET NSCLC, FGFR-altered urothelial carcinoma, and BRAF melanoma
  as reference patterns for targetable oncology mechanisms.
- Use IDG to find understudied targets for non-oncology mechanisms, especially
  pain, epilepsy, immune disease, fibrosis, and metabolic disease.

## Fit for RFA-RM-26-017

Best partner datasets:

- IDG + LINCS: target annotations plus cellular perturbation signatures.
- IDG + MoTrPAC: exercise-responsive druggable targets.
- IDG + SPARC: neuromodulation targets in autonomic and visceral disease.
- IDG + KOMP2: knockout phenotypes for understudied target genes.

## Sources

- NIH Common Fund IDG: https://commonfund.nih.gov/IDG/
- Pharos: https://pharos.nih.gov/
- Pharos API docs: https://pharos.nih.gov/api
- Pharos GraphQL endpoint: https://pharos-api.ncats.io/graphql
- IDG Pharos/TCRD overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC5210555/
