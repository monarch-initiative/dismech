# Undiagnosed Diseases Network (UDN)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

UDN is valuable because it starts from unresolved patients and forces the
mechanism graph to explain genotype, phenotype, biospecimen data, model
organism evidence, and diagnostic uncertainty together. The NIH Common Fund
describes UDN as a research study to improve diagnosis of rare and undiagnosed
conditions and to uncover underlying disease mechanisms. The UDN model combines
deep clinical phenotyping, genome or exome sequencing, metabolomics, model
organism studies, and expert cross-disciplinary review.

For dismech, UDN is both a source of missing rare disease targets and a test of
whether a mechanism graph helps interpret incomplete evidence.

## Dismech Interpretation Pattern

Use UDN as a rare-disease mechanism assembly workflow:

`patient HPO phenotype set -> candidate variant, gene, or biochemical
abnormality -> tissue expression and pathway plausibility -> model or omics
support -> curated disease mechanism graph or provisional open question`

UDN-style evidence should preserve uncertainty. A candidate gene, animal rescue,
and patient phenotype overlap are not the same as a fully established human
disease mechanism.

## Concrete Implementation Plan

**Mode:** benchmark rare-disease interpretation. UDN should test whether
dismech can assemble incomplete evidence into a transparent mechanism graph
with explicit uncertainty and open questions.

**Required datasets and access path:**

- Use public UDN resources first: the UDN site
  https://undiagnosed.hms.harvard.edu/, the genes-of-interest page
  https://undiagnosed.hms.harvard.edu/genes/, NHGRI overview pages, and UDN
  publications.
- Treat patient-level UDN genomic, phenotype, and clinical data as controlled
  research data, not as open datasets for this repo. Use dbGaP/approved UDN
  access only if the project obtains permissions.
- For dismech planning, use public gene lists, case reports, publications,
  model-organism studies, and aggregate descriptions. Do not store patient
  identifiers, pedigrees, raw variants, or clinical notes.
- Pair UDN candidate genes with KOMP2, GTEx, HuBMAP, Metabolomics Workbench,
  SMaHT, and 4DN according to the mechanism class.

**Tools and environment:**

- HPO/Phenopacket-style phenotype representation, Exomiser or similar
  phenotype-driven variant prioritization, VEP/SnpEff for variant annotation,
  ClinVar/OMIM/Orphanet/Monarch/MARRVEL for gene-disease context, and model
  organism resources for functional support.
- For repeat expansions and mosaicism, use assay-aware interpretation. Standard
  exome pipelines miss many repeat expansions and low-level mosaic variants.
- Evidence review should produce a candidate mechanism memo before any YAML
  edit.

**Curation targets:**

- Existing rare disease anchors: `CTCF-related_Neurodevelopmental_Disorder`,
  `Congenital_Insensitivity_to_Pain`, `Stargardt_Disease`, `Alport_Syndrome`,
  `Diamond-Blackfan_Anemia`, `CLOVES_Syndrome`, and
  `Pentanucleotide_Repeat_Familial_Adult_Myoclonus_Epilepsy`.
- New/provisional disease work: only when there is a public UDN-associated
  gene, patient phenotype pattern, model/functional support, and publication or
  preprint that can be cited.
- Mechanism categories: developmental transcription/chromatin, ion channel,
  retinal metabolism, basement membrane/ECM, ribosome/hematopoiesis, somatic
  mosaic signaling, repeat RNA toxicity, and inborn errors of metabolism.

**Code to write:**

- Add `src/dismech/commonfund/udn.py` to ingest public UDN gene lists and
  publications into a candidate-gene manifest with disease area, HPO terms if
  public, evidence type, and companion CF resources.
- Add `scripts/udn_candidate_mechanism_template.py` to generate review memos
  with HPO profile, gene/variant class, inheritance, tissue expression,
  functional/model evidence, rescue evidence, confidence, and open questions.
- Add schema-review notes for provisional disease mechanisms, evidence
  uncertainty, diagnostic workflow evidence, and candidate-gene status.

**Graduate-student first pass:**

1. Pick one public UDN gene or paper. Extract only public phenotype and
   mechanism evidence.
2. Map the HPO profile to existing dismech disease files or decide that a new
   provisional entry is needed.
3. Use two companion CF resources for support: KOMP2 for model phenotype, GTEx
   or HuBMAP for tissue context, Metabolomics Workbench for biochemical
   evidence, SMaHT for mosaicism, or 4DN for regulatory architecture.
4. Write a memo that ends with "mechanism supported", "mechanism plausible but
   unresolved", or "diagnostic association only".

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How UDN helps |
|---------|--------------------------------|---------------|
| `CTCF-related_Neurodevelopmental_Disorder` | Curated nodes: `CTCF Haploinsufficiency`, `Chromatin Architecture Disruption`, `Neurodevelopmental Gene Dysregulation`, `Abnormal Neural Progenitor Cell Development` | A model UDN-style interpretation: rare variant plus neurodevelopmental HPO profile plus chromatin mechanism, strengthened by GTEx/4DN/KOMP2 context. |
| `Congenital_Insensitivity_to_Pain` | Curated nodes include `Impaired nociceptor specification`, `NGF-TRKA trophic signaling failure`, `Developmental nociceptor apoptosis`, `Nav1.7 loss-of-function channelopathy`, `Nav1.9 depolarization-block channelopathy`, `Loss of protective pain perception` | UDN cases can separate multiple genetic routes to the same pain phenotype and test whether a patient's variant affects development, excitability, or trophic signaling. |
| `Stargardt_Disease` | Curated nodes: `ABCA4 transporter dysfunction`, `Retinoid-adduct retention and bisretinoid precursor formation`, `Lipofuscin and A2E accumulation in RPE`, `Secondary macular photoreceptor degeneration` | A strong ophthalmic rare-disease example for linking variant interpretation, biochemical mechanism, retinal phenotype, and potential treatment strategy. |
| `Alport_Syndrome` | Curated nodes: `Defective Type IV Collagen Network`, `GBM Structural Deterioration`, `Podocyte Injury and Loss`, `Glomerulosclerosis`, `Tubulointerstitial Fibrosis` | UDN-style analysis can connect renal, hearing, and ocular phenotypes to collagen network defects and family segregation. |
| `Diamond-Blackfan_Anemia` | Curated nodes: `Ribosomal Protein Haploinsufficiency`, `p53-Mediated Erythroid Apoptosis`, `GATA1 Translational Insufficiency` | A mechanistic rare hematology example where variant, marrow phenotype, ribosome biology, and model organism evidence can be integrated. |
| `CLOVES_Syndrome` | Curated nodes: `Somatic Mosaicism`, `Constitutive PI3K Activation`, `AKT/mTOR Pathway Hyperactivation`, `Aberrant Vascular Development`, `Lipomatous Overgrowth` | UDN can help diagnose hard mosaic cases where blood sequencing is negative but affected tissue carries the causal variant. |
| `Pentanucleotide_Repeat_Familial_Adult_Myoclonus_Epilepsy` | Curated module-linked mechanism: repeat expansion RNA toxicity in `fame_pentanucleotide_repeat_rna_toxicity` | UDN-style workups can capture repeat-expansion disorders that standard exome pipelines miss, then connect repeat RNA toxicity to epilepsy phenotypes. |
| Yet to curate: novel gene disease | Candidate pattern: rare damaging variant -> disrupted molecular function -> model organism phenotype or rescue -> human phenotype match -> provisional disorder entry | UDN is the most natural source for new dismech entries with explicit evidence tiers and open questions. |

## High-Value Curation Work

- Create a UDN intake template for candidate disease mechanisms: HPO profile,
  candidate gene/variant, inheritance, tissue expression, biochemical findings,
  model organism evidence, rescue evidence, and uncertainty status.
- Prioritize entries where dismech already has strong rare disease mechanisms:
  `CTCF-related_Neurodevelopmental_Disorder`,
  `Congenital_Insensitivity_to_Pain`, `Stargardt_Disease`, `Alport_Syndrome`,
  `Diamond-Blackfan_Anemia`, `CLOVES_Syndrome`, and repeat-expansion epilepsies.
- Use UDN to identify missing rare disorders, especially neurodevelopmental,
  metabolic, renal, hematologic, ophthalmic, and mosaic conditions.
- Keep diagnostic workflow evidence separate from mechanism evidence: a case
  diagnosis can motivate curation, but each mechanism edge still needs direct
  support.

## Fit for RFA-RM-26-017

Best partner datasets:

- UDN + KOMP2: candidate gene and model phenotype support.
- UDN + GTEx/HuBMAP: tissue expression and cell context.
- UDN + Metabolomics Workbench: biochemical diagnosis and pathway evidence.
- UDN + Kids First/SMaHT: pediatric, congenital, cancer, and mosaic disorders.
- UDN + Bridge2AI: AI-ready rare-disease evidence packages.

## Sources

- NIH Common Fund UDN: https://commonfund.nih.gov/Diseases
- UDN site: https://undiagnosed.hms.harvard.edu/
- NHGRI UDN overview: https://www.genome.gov/Funded-Programs-Projects/Undiagnosed-Diseases-Network
- UDN genes of interest: https://undiagnosed.hms.harvard.edu/genes/
