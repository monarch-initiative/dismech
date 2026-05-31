# Gabriella Miller Kids First (Kids First)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

Kids First is mechanistically important because it connects pediatric genomes,
structural birth defects, childhood cancer, family data, and phenotype data.
The Common Fund page frames the program around shared genetic pathways between
childhood cancer and congenital anomalies. It reports public release of data
from 36 projects and nearly 30,000 genomes through the Kids First Data Resource
Portal.

For dismech, this is a direct bridge from cohort-scale pediatric variation to
curated mechanism graphs.

## Dismech Interpretation Pattern

Use Kids First data to interpret pediatric genotype-phenotype findings:

`germline, de novo, somatic, structural, or copy-number variant -> affected
developmental or tumor suppressor pathway -> cell lineage defect, tumor
initiation, malformation, or predisposition -> pediatric phenotype`

Family-based WGS is especially useful for separating inherited predisposition,
de novo developmental mechanisms, and tumor-acquired events.

## Concrete Implementation Plan

**Mode:** both teach and benchmark. Kids First can teach pediatric
variant-to-mechanism curation, and dismech can benchmark whether variants from
pediatric cancer and structural birth defect cohorts are interpreted as
developmental, tumor, germline predisposition, or somatic second-hit mechanisms.

**Required datasets and access path:**

- Use the Kids First Data Resource Portal:
  https://portal.kidsfirstdrc.org/ and DRC site:
  https://kidsfirstdrc.org/.
- Use the Common Fund access FAQ for authoritative access rules:
  https://commonfund.nih.gov/kidsfirst/faq. It states that individual-level
  BAM/FASTQ/VCF files and clinical/phenotype metadata are accessed through the
  portal and require dbGaP approval before individual-level genomic sequence
  access.
- Use CAVATICA for cloud analysis after access approval:
  https://www.cavatica.org/ and https://docs.cavatica.org/. CAVATICA docs state
  that controlled Kids First data require Gen3 and dbGaP permissions, while
  public/open data can still be used with a CAVATICA account.
- Use the Kids First X01 projects page to select stable projects and dbGaP
  accessions: https://commonfund.nih.gov/kidsfirst/X01Projects.

**Tools and environment:**

- Portal search/file repository, dbGaP DAR workflow, CAVATICA workspaces, and
  Seven Bridges/CWL tools for approved analyses.
- Variant interpretation stack: VEP or SnpEff, ClinVar, gnomAD, MARRVEL,
  Matchmaker/Monarch-style phenotype links, HPO mapping, CNV/SV annotation, and
  fusion callers for tumor projects.
- No individual-level genomic or clinical data should be committed to dismech.
  Only stable study accessions, public metadata, and literature-supported
  findings belong in YAML.

**Curation targets:**

- Pediatric cancers: `Wilms_Tumor`, `Neuroblastoma`,
  `Atypical_Teratoid_Rhabdoid_Tumor`, `Retinoblastoma`, and `Ewing_Sarcoma`.
- Structural birth defects and cancer-predisposition/developmental syndromes:
  `22q11.2_Deletion_Syndrome`, `Frontonasal_Dysplasia`, neural tube defects,
  craniofacial disorders, congenital heart defects, and renal malformations.
- Mechanism categories to distinguish: germline predisposition, de novo
  developmental variant, copy-number dosage, structural rearrangement/fusion,
  somatic second hit, and tumor subtype driver.

**Code to write:**

- Add `src/dismech/commonfund/kids_first.py` to ingest project-level metadata:
  study id, dbGaP accession, disease/condition, file types, family structure,
  access level, CAVATICA availability, and candidate dismech files.
- Add `scripts/kids_first_variant_mechanism_template.py` to generate review
  worksheets for variant class -> gene/pathway -> developmental/tumor mechanism
  -> phenotype/HPO -> evidence.
- Add schema-review notes for family structure, pediatric cohort metadata,
  structural variants, tumor/germline distinction, and controlled-access flags.

**Graduate-student first pass:**

1. Pick one Kids First project from the X01 page and record dbGaP accession,
   condition, data types, family structure, and data use limits.
2. Before variant analysis, draft the expected developmental or tumor mechanism
   graph from existing literature.
3. Use approved access only inside CAVATICA. Export back to dismech only
   aggregate, non-identifying, literature-supported mechanism findings.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How Kids First helps |
|---------|--------------------------------|----------------------|
| `Wilms_Tumor` | Curated nodes: `WT1 Inactivation`, `WTX (AMER1) Inactivation`, `CTNNB1 Activating Mutation`, `Canonical Wnt Signaling Hyperactivation`, `Blocked Nephron Differentiation`, `IGF2 Loss of Imprinting`, `MicroRNA Processing Defect` | Strongest pediatric cancer/development pilot. Kids First can connect kidney developmental variants, birth defects, and tumor subtypes. |
| `Neuroblastoma` | Curated nodes: `Neural Crest Developmental Arrest`, `MYCN-Driven Proliferation`, `ALK Signaling Activation` | Good shared developmental-cancer example: neural crest lineage disruption plus oncogenic amplification/signaling. |
| `Atypical_Teratoid_Rhabdoid_Tumor` | Curated nodes: `SMARCB1 or SMARCA4 Inactivation`, `SWI/SNF Chromatin Remodeling Defect`, `Subtype-Specific Enhancer Dysregulation`, `Aggressive Tumor Cell Proliferation` | Use Kids First WGS to connect chromatin remodeling genes, early-onset tumor biology, and developmental context. |
| `Retinoblastoma` | Curated nodes: `RB1 Tumor Suppressor Inactivation`, `Loss of Cell Cycle Checkpoint Control`, `Uncontrolled Retinal Cell Proliferation` | Family data can distinguish germline predisposition and somatic second-hit mechanisms. |
| `Ewing_Sarcoma` | Curated nodes: `EWS-FLI1 Fusion Oncogene`, `Aberrant Transcriptional Regulation`, `Blocked Differentiation` | Structural variant and fusion interpretation pilot: translocation -> fusion TF -> enhancer/program rewiring -> tumor state. |
| `22q11.2_Deletion_Syndrome` | Curated nodes: `TBX1 haploinsufficiency and pharyngeal arch development`, `Cardiac neural crest migration defect`, `Thymic hypoplasia and T-cell immunodeficiency` | Represents structural birth defect mechanisms where CNV dosage affects developmental fields. |
| `Frontonasal_Dysplasia` | Curated nodes: `ALX transcription factor disruption`, `Cranial neural crest migration and survival defects`, `BMP signaling dysregulation in neural crest cells` | Good congenital anomaly example for cranial neural crest mechanism mapping. |
| Yet to curate: neural tube defects | Candidate mechanisms: folate/planar-cell-polarity or chromatin variant -> failed neural tube closure -> spina bifida/anencephaly phenotype | Kids First X01 projects include structural pediatric defect cohorts that could drive new dismech entries. |

## High-Value Curation Work

- Add Kids First-backed `datasets` to high-priority pediatric cancer entries:
  `Wilms_Tumor`, `Neuroblastoma`, `Atypical_Teratoid_Rhabdoid_Tumor`,
  `Retinoblastoma`, and `Ewing_Sarcoma`.
- Create a pediatric variant interpretation pattern that distinguishes:
  germline predisposition, de novo developmental variation, somatic tumor
  second hits, structural variants, and fusion events.
- Crosswalk Kids First phenotypes to HPO terms and dismech disease entries,
  but keep case-level privacy and access constraints outside disease YAML unless
  the dataset release explicitly permits open metadata.
- Use KOMP2 and GTEx as companion sources when a Kids First variant needs gene
  function or tissue-expression support.

## Fit for RFA-RM-26-017

Best partner datasets:

- Kids First + KOMP2: pediatric candidate variants with mouse phenotype support.
- Kids First + GTEx: tissue-expression interpretation of candidate genes.
- Kids First + 4DN: structural variant and enhancer-rewiring interpretation.
- Kids First + Bridge2AI: AI-ready pediatric variant-to-mechanism metadata.

## Sources

- NIH Common Fund Kids First: https://commonfund.nih.gov/kidsfirst
- Kids First Data Resource Portal: https://kidsfirstdrc.org/
- Kids First Portal: https://portal.kidsfirstdrc.org/
- Kids First access FAQ: https://commonfund.nih.gov/kidsfirst/faq
- Kids First X01 projects: https://commonfund.nih.gov/kidsfirst/X01Projects
- CAVATICA: https://www.cavatica.org/
- NICHD Kids First overview: https://www.nichd.nih.gov/research/supported/gm-kidsfirst
