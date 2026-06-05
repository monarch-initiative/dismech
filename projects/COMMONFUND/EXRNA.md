# Extracellular RNA Communication (exRNA)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

exRNA is mechanistically useful when extracellular RNAs are interpreted as
signals or cargo in cell-to-cell communication, not only as diagnostic
biomarkers. The Common Fund page describes exRNA as RNA exported outside cells,
often associated with extracellular vesicles or other carriers, with program
outputs including standards, a portal, tools, reagents, and cataloged exRNA
molecules in human biofluids such as plasma, saliva, and urine from more than
2,000 donors.

For dismech, exRNA can connect tissue injury, tumor state, immune activation,
pregnancy complications, and organ dysfunction to measurable biofluid signals.

## Dismech Interpretation Pattern

Use exRNA data in two layers:

`disease tissue or cell state -> released RNA/carrier signal in biofluid ->
biomarker or communication effect -> downstream immune, stromal, vascular, or
metabolic mechanism`

Evidence should distinguish exRNA as a correlative biomarker from exRNA as an
active mediator. Many entries will only justify biomarker curation at first.

## Concrete Implementation Plan

**Mode:** mostly teach dismech. exRNA should teach dismech how to represent a
biofluid RNA signal as biomarker, cargo, or mediator. It can benchmark dismech
later by asking whether known biofluid signatures are mapped back to plausible
source tissues and mechanisms.

**Required datasets and access path:**

- Use the exRNA Portal data page: https://exrna.org/resources/data/ and the
  exRNA Atlas: https://exrna-atlas.org/.
- The Atlas page states that it contains small RNA sequencing and qPCR-derived
  exRNA profiles from human and mouse biofluids, uniformly processed with the
  exceRpt small RNA-seq pipeline and ERCC quality metrics.
- Prioritize Atlas v3.0 hg38 data for plasma, serum, saliva, urine, and CSF.
  The Atlas page says these five biofluids account for most Atlas samples and
  are available through a public FTP while the site is being updated.
- Use GEO accessions linked from Atlas studies when adding stable `datasets` to
  disease YAML; the Atlas citation guidance asks users to cite exRNA.org and
  GEO accession numbers for specific datasets.

**Tools and environment:**

- Python/R with `pandas`, `scanpy` or base Bioconductor tooling for count
  matrices, and DESeq2/edgeR for small RNA differential abundance if raw or
  count-level data are available.
- exceRpt pipeline only if reprocessing is necessary; otherwise use Atlas
  processed outputs to avoid unnecessary pipeline drift.
- miRNA/gene-target resources should be used only as hypothesis generators.
  Target prediction alone should not be converted into a mechanism assertion.

**Curation targets:**

- `Preeclampsia`: placental exRNA and maternal endothelial dysfunction as a
  biomarker layer over anti-angiogenic factor release.
- `Pancreatic_Ductal_Adenocarcinoma` and `Gastric_Cancer_H_pylori_Associated`:
  tumor/stromal exRNA as liquid-biopsy evidence, with active communication
  claims only when recipient-cell effects are experimentally shown.
- `Alzheimer_Disease`, `Type_2_Diabetes_Mellitus`, `Systemic_Lupus_Erythematosus`,
  `Glaucoma`, and kidney-transplant/CKD-related entries: biofluid signatures as
  tissue-injury or immune-activation readouts.

**Code to write:**

- Add `src/dismech/commonfund/exrna.py` to ingest Atlas study metadata and
  produce disease-candidate manifests with study id, GEO accession, biofluid,
  organism, condition, RNA class, pipeline version, and sample count.
- Add an `exrna_biomarker_evidence.tsv` template with fields for producing
  cell/tissue, carrier, RNA species, recipient cell, measured disease state,
  and evidence level: biomarker-only, transport/cargo, or functional mediator.
- Add schema-review notes for `SMALL_RNA_SEQ`, `QPCR`, `BIOFLUID_BIOMARKER`,
  and carrier metadata.

**Graduate-student first pass:**

1. In the Atlas, filter to one biofluid and one disease area, preferably plasma
   cancer, urine kidney disease, CSF neurodegeneration, or pregnancy-related
   plasma/serum.
2. Export study metadata and GEO accessions; do not start with miRNA target
   prediction.
3. For the top 10 RNAs, classify each as source-tissue marker, disease-state
   marker, or experimentally supported mediator, then map only supported claims
   into dismech.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How exRNA helps |
|---------|--------------------------------|-----------------|
| `Preeclampsia` | Curated nodes: `Defective Trophoblast Invasion and Spiral Artery Remodeling`, `Placental Anti-Angiogenic Factor Release`, `Maternal Endothelial Dysfunction` | Strong biofluid pilot: placental exRNAs could be represented as early biomarkers of anti-angiogenic and endothelial injury mechanisms. |
| `Pancreatic_Ductal_Adenocarcinoma` | Curated nodes: `KRAS Oncogene Activation`, `Desmoplastic Stroma`, `CAF-Mediated T Cell Exclusion`, `Immune Evasion` | Candidate addition: tumor/stromal exRNA cargo as a liquid-biopsy readout of KRAS pathway activity, desmoplasia, or immune exclusion. |
| `Gastric_Cancer_H_pylori_Associated` | Curated nodes: `CagA-Mediated Oncogenic Signaling`, `VacA-Induced Cellular Damage`, `Chronic Inflammation (Correa Cascade)` | exRNA could provide a blood or gastric-fluid marker layer for inflammation-to-cancer progression. |
| `Alzheimer_Disease` | Curated nodes include `Amyloid Plaque Formation`, `Neurofibrillary Tangle Formation`, `Synaptic Dysfunction`, `Neuroinflammation` | Candidate addition: neuronal or glial exRNA as a biofluid window into neurodegenerative cell-state changes. |
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Mitochondrial Dysfunction and Oxidative Stress` | exRNA can be used as biomarker evidence for beta-cell stress, adipose inflammation, or endothelial complications, if disease-specific studies are selected. |
| `Systemic_Lupus_Erythematosus` | Current disease file exists; candidate mechanisms include interferon activation, immune-complex inflammation, and renal involvement | exRNA may help represent circulating immune-cell activation and organ-specific injury signatures. |
| `Glaucoma` | Current disease file exists | The exRNA program specifically mentions glaucoma among diseases with potential exRNA biomarkers; dismech could connect ocular fluid exRNA signals to retinal ganglion cell stress or trabecular meshwork dysfunction. |

## High-Value Curation Work

- Add a biomarker curation pattern for biofluid exRNA: source fluid, carrier if
  known, RNA species, measured condition, and whether it is merely diagnostic or
  experimentally mediating a mechanism.
- Add exRNA-backed `datasets` to one pregnancy complication, one cancer, one
  neurodegenerative disorder, and one metabolic disease entry.
- Use `biochemical` or `datasets` first. Add pathophysiology nodes only when
  evidence shows exRNA cargo changes recipient cell behavior.
- For active communication mechanisms, curate the full chain:
  producing cell type -> exRNA carrier -> recipient cell type -> changed
  biological process -> phenotype.

## Fit for RFA-RM-26-017

Best partner datasets:

- exRNA + Metabolomics Workbench: multimodal biofluid signatures.
- exRNA + iHMP/HMP: host-microbiome effects on biofluid RNAs.
- exRNA + HuBMAP: source-tissue and source-cell annotation.
- exRNA + Bridge2AI: AI-ready biomarker metadata and responsible model use.

## Sources

- NIH Common Fund exRNA: https://commonfund.nih.gov/Exrna
- exRNA Portal: https://exrna.org/
- exRNA data page: https://exrna.org/resources/data/
- exRNA Atlas: https://exrna-atlas.org/
- exRNA review: https://pmc.ncbi.nlm.nih.gov/articles/PMC11735951/
