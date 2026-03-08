# GWAS Mechanisms: Gene-Program-Trait Causal Modeling

## Overview

Use DisMech as a validation/interpretation layer for computational pipelines that discover
causal gene-to-trait relationships via GWAS, Perturb-seq, and causal modeling. The pilot
application is the Ota et al. (Nature 2025) framework that builds three-layer causal graphs:

```
Gene (regulator) --[β]--> Program --[effect]--> Trait/Phenotype
                          ↑
Gene (member) ----[γ]----/
```

This project covers: (1) validating pipeline outputs against curated pathophysiology,
(2) curating blood/hematological disorders to improve coverage, (3) building tooling
to map between pipeline entities and dismech ontology terms, and (4) extending to
other cell types and trait domains as new Perturb-seq datasets emerge.

## Background: Ota et al. (Nature 2025)

**Paper**: "Causal modelling of gene effects from regulators to programs to traits"
- Ota M, Spence JP, Zeng T, Dann E, Milind N, Marson A, Pritchard JK
- Nature 650:399-408 (Feb 2026; online Dec 10, 2025)
- DOI: [10.1038/s41586-025-09866-3](https://www.nature.com/articles/s41586-025-09866-3)
- PMID: 41372418 | PMCID: PMC12893915
- bioRxiv: [2025.01.22.634424v1](https://www.biorxiv.org/content/10.1101/2025.01.22.634424v1)

**Key methodology:**
- 60 gene programs from consensus NMF on K562 Perturb-seq (Replogle et al. 2022; 9,866 genes)
- Gene-trait effect sizes from UK Biobank LoF burden tests (454K participants) via GeneBayes
- S-LDSC to identify traits where K562 chromatin explains heritability
- Multiple regression modeling gene effects on programs and program effects on traits
- 73% accuracy predicting effect directions for top MCH GWAS hits

**Key biological findings:**
- SUPT5H regulates hemoglobin production, cell cycle, and autophagy simultaneously
- Programs capture biologically meaningful co-regulation modules
- Regulators of a program vs. member genes can have distinct trait relationships

## Related Work

| Paper | Year | Key Contribution |
|-------|------|-----------------|
| Spence, Mostafavi, Ota, Pritchard - Nature | 2025 | Companion: "Specificity, length and luck drive gene rankings" - GWAS vs burden tests prioritize different genes |
| Zhu, Dann, ..., Ota, Pritchard, Marson - bioRxiv | 2025 | Follow-up: Genome-scale Perturb-seq in primary CD4+ T cells (22M cells, 4 donors) |
| Zeng, Spence, Mostafavi, Pritchard - Nat Genet | 2024 | GeneBayes: empirical Bayes framework for LoF effect size estimation |
| Mani et al. - Nature | 2024 | CAD GWAS signals converge onto endothelial cell programs (variant-to-gene-to-program) |
| Replogle et al. - Cell | 2022 | Original genome-scale K562 Perturb-seq dataset |
| Qi et al. - Trends Genet | 2024 | Review: from genetic associations to genes (QTL colocalization, fine-mapping, networks) |
| Costanzo et al. - Nat Genet | 2025 | Perspective: standardizing effector gene predictions from GWAS |

## Assets

| Asset | Path | Contents |
|-------|------|----------|
| Paper PDF | `docs/assets/Causal modelling of gene effects from regulators to programs to traits.pdf` | Full text |
| Table S1 | `docs/assets/Ota_2025_TableS1.xlsx` | 60 programs: GO annotations, top genes, TFs, marker coexpression |
| Table S2 | `docs/assets/Ota_2025_TableS2.xlsx` | 54 traits: RBC (12), other blood (10), serum biomarkers (28), anthropometric (4) |
| Table S3 | `docs/assets/Ota_2025_TableS3.xlsx` | S-LDSC heritability enrichment by cell type and trait |
| Table S4 | `docs/assets/Ota_2025_TableS4.xlsx` | Alternate program annotations (variant analysis) |
| Table S5 | `docs/assets/Ota_2025_TableS5.xlsx` | Perturb-seq dataset descriptions (5 datasets) |
| Integration plan | `docs/causal-modeling-integration-plan.md` | Detailed plan for dismech as validation resource |

## External Code Repositories

- [GeneBayes](https://github.com/tkzeng/GeneBayes) - empirical Bayes framework (Zeng et al.)
- [specificity_length_luck](https://github.com/jeffspence/specificity_length_luck) - companion paper code
- [GWT_perturbseq_analysis_2025](https://github.com/emdann/GWT_perturbseq_analysis_2025) - T cell follow-up
- No dedicated repo for the main Ota et al. analysis code (as of Feb 2026)

## Existing Blood/Hematological Disorders in KB

| Disorder | File | Relevance |
|----------|------|-----------|
| Sickle Cell Disease | Sickle_Cell_Disease.yaml | Hemoglobin, erythrocytes, MCH |
| Autoimmune Hemolytic Anemia | Autoimmune_Hemolytic_Anemia.yaml | RBC destruction, hemolysis |
| G6PD Deficiency | Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml | RBC fragility, oxidative stress |
| Hemochromatosis | Hemochromatosis.yaml | Iron metabolism |
| Fanconi Anemia | Fanconi_Anemia.yaml | Bone marrow failure |
| Polycythemia Vera | Polycythemia_Vera.yaml | Erythrocytosis, JAK2 |
| Essential Thrombocythemia | Essential_Thrombocythemia.yaml | Platelet production |
| Primary Myelofibrosis | Primary_Myelofibrosis.yaml | Bone marrow fibrosis |
| CML | Chronic_Myeloid_Leukemia.yaml | Myeloid proliferation |
| CLL | Chronic_Lymphocytic_Leukemia.yaml | Lymphocyte count |
| Immune Thrombocytopenia | Immune_Thrombocytopenia.yaml | Platelet destruction |
| Hemophilia A/B | Hemophilia_A.yaml, Hemophilia_B.yaml | Coagulation |

## Key Programs Relevant to DisMech Disorders

| Program | Annotation | GO Term | DisMech Diseases |
|---------|------------|---------|------------------|
| P4 | Cell cycle (S phase, DNA replication) | DNA replication | CML, Retinoblastoma |
| P6 | Cell cycle (G2M checkpoint) | G2M checkpoint | Cancers |
| P12 | Myeloid | purine nucleotide metabolic process | CML, AML, myeloproliferative |
| P16 | Autophagosome | autophagosome | Crohn's, neurodegeneration |
| P27 | Platelet activation (Mega, IKZF1) | platelet activation | ITP, Essential Thrombocythemia |
| P28 | RBC (glycoproteins) | HEME_METABOLISM | Sickle Cell, Thalassemia |
| P35 | TNF signaling (stress response) | TNFA_SIGNALING_VIA_NFKB | Autoimmune diseases |
| P40 | Hemoglobin synthesis | HEME_METABOLISM | Sickle Cell, Thalassemia, Anemia |
| P45 | TNF signaling (apoptosis) | TNFA_SIGNALING_VIA_NFKB | SLE, RA |
| P46 | Cholesterol biosynthesis | cholesterol biosynthesis | CAD, Familial Hypercholesterolemia |

## Traits (54 total from Table S2)

### RBC Traits (12) - primary focus
Reticulocyte count, Mean reticulocyte volume, Mean sphered cell volume, Immature reticulocyte
fraction (IRF), High light scatter reticulocyte count, RBC count, MCV, MCH, MCHC, RDW,
Haematocrit, Haemoglobin concentration

### Other Blood Traits (10)
WBC count, Platelet count, Platelet crit, MPV, Platelet distribution width, Lymphocyte count,
Monocyte count, Neutrophil count, Eosinophil count, Basophil percentage

### Serum Biomarkers (28)
Albumin, ALP, ALT, ApoA, ApoB, AST, Direct bilirubin, Urea, Calcium, Cholesterol, Creatinine,
CRP, Cystatin C, GGT, Glucose, HbA1c, HDL, IGF-1, LDL, Oestradiol, Phosphate, SHBG,
Total bilirubin, Testosterone, Total protein, Triglycerides, Urate, Vitamin D

### Anthropometric (4)
Sitting height, Birth weight, BMI, Heel BMD

---

# TASKS

## Phase 1: Blood Disorder Curation Gap-Fill
Priority: curate missing blood disorders that are highly relevant to the 12 RBC traits.

- [ ] Alpha Thalassemia
- [ ] Beta Thalassemia
- [ ] Iron Deficiency Anemia
- [ ] Aplastic Anemia
- [ ] Myelodysplastic Syndromes
- [ ] Diamond-Blackfan Anemia
- [ ] Congenital Dyserythropoietic Anemia
- [ ] Hereditary Spherocytosis

## Phase 2: Trait-to-HPO Mapping
Map all 54 traits from Table S2 to HPO terms (increased/decreased variants).

- [ ] Create trait_to_hpo.yaml mapping file for RBC traits (12)
- [ ] Create mappings for other blood traits (10)
- [ ] Create mappings for serum biomarkers (28)
- [ ] Create mappings for anthropometric traits (4)

Example mapping needed:
```yaml
MCH:
  trait_name: "Mean corpuscular haemoglobin"
  lof_trait_id: 30050
  hpo_decreased: HP:0025066  # Decreased mean corpuscular hemoglobin
  hpo_increased: HP:0025065  # Increased mean corpuscular hemoglobin
  related_disorders:
    - Sickle_Cell_Disease
    - Beta_Thalassemia
```

## Phase 3: Program-to-GO Mapping
Map all 60 programs to proper GO terms (many currently use Hallmark gene set names).

- [ ] Resolve HALLMARK_* annotations to GO terms
- [ ] Validate GO terms via OAK
- [ ] Create program_go_mapping.yaml

## Phase 4: Proof-of-Concept Validation (MCH/RDW/IRF)
Manual validation of top gene-program-trait relationships for the three blood traits.

- [ ] Extract top 20 genes per trait from paper/supplements
- [ ] For each gene-program-trait triple, check if dismech documents the relationship
- [ ] Classify as CONFIRMED / PARTIAL / NOVEL / CONTRADICTED
- [ ] Write validation report

## Phase 5: Automated Validation Pipeline
Build tooling to systematically match pipeline outputs against dismech.

- [ ] Export dismech blood disorders to queryable format (gene, GO, HP indexed)
- [ ] Implement gene-program-trait matching logic
- [ ] Generate validation report with coverage statistics
- [ ] Identify curation gaps from NOVEL findings

## Phase 6: Extend to T Cell / Immune Traits
Leverage the Zhu/Dann et al. CD4+ T cell Perturb-seq follow-up.

- [ ] Obtain T cell program definitions when published
- [ ] Map immune traits to HPO terms
- [ ] Validate against dismech autoimmune disease entries (20+ curated)
- [ ] Compare K562 vs T cell program overlap

## Phase 7: Schema Enhancements
Address dismech schema gaps identified in the integration plan.

- [ ] Add systematic `modifier` (INCREASED/DECREASED) to phenotype entries
- [ ] Add genes to pathophysiology biological_process entries where missing
- [ ] Consider `gene` slot on BiologicalProcessDescriptor for explicit gene-process links

---

# NOTES

## Zhu/Dann T Cell Follow-up: Traits and Diseases

The T cell paper takes a different approach from the K562 paper. Rather than directly
modeling continuous GWAS traits, it tests:

1. **Cytokine readouts** (30 genes): IFN-gamma, TNF, IL-4, IL-5, IL-13, IL-10, IL-2, IL-16, IL-21, CCL3, CCL4, CCL5, CXCL8, TGF-beta, etc.
2. **Th1/Th2 polarization signatures** from published bulk RNA-seq
3. **CD4+ T cell aging signatures** from OneK1K cohort (782 donors)
4. **Lymphocyte counts** from UK Biobank (Backman et al. 2021 exome data)
5. **GWAS gene enrichment** for 14 autoimmune diseases via Open Targets

**Autoimmune diseases tested:**
| Disease | Open Targets ID | In dismech KB? |
|---------|----------------|----------------|
| Rheumatoid arthritis | EFO_0000685 | Yes |
| SLE | MONDO_0007915 | Yes |
| IBD | EFO_0003767 | Yes (Crohn's + UC) |
| Multiple sclerosis | MONDO_0005301 | Yes |
| Type 1 diabetes | MONDO_0005147 | Yes |
| Psoriasis | EFO_0000676 | Yes |
| Ankylosing spondylitis | EFO_0003898 | Yes |
| Asthma | MONDO_0004979 | Yes |
| Hashimoto's thyroiditis | EFO_0003779 | Yes |
| Crohn's disease | EFO_0000384 | Yes |
| Ulcerative colitis | EFO_0000729 | Yes |
| Celiac disease | EFO_0001060 | Yes |
| Atopic eczema | EFO_0000274 | Yes (Atopic_Dermatitis) |
| Autoimmune disease (general) | EFO_0005140 | — |

**Key findings:**
- 111 regulator clusters from 3,341 perturbations of 1,860 regulators
- Cluster 110 (12 genes incl. MAP3K8, CHD7, ITK): massive enrichment for asthma (OR=20.4), atopic eczema (OR=24.3), psoriasis (OR=17.6)
- Cluster 79 (Th17; IRF4, BATF, STAT3, IPMK): Crohn's (OR=58.2), eczema (OR=38.1)
- Cluster 59 (IL10, BACH2, REL, CTLA4, CD28): broad enrichment across IBD, psoriasis, MS

**Key methodological difference:** Uses GWAS gene enrichment per cluster (via Open Targets)
rather than direct trait-effect modeling. Also uses pert2state models for aging/polarization.

**GitHub repo:** https://github.com/emdann/GWT_perturbseq_analysis_2025
- Supplementary tables in `metadata/suppl_tables/`
- Full clustering results: `clustering_results_and_annotations.csv`
- Autoimmune enrichment: `cluster_autoimmune_enrichment_results.suppl_table.csv`

## Blood Disorder KB Readiness Assessment

| Disorder | Genes | GO Procs | Modifiers | Traceability | Notes |
|----------|-------|----------|-----------|-------------|-------|
| CML | 1 (BCR-ABL1) | 6 | 5 (INC/DEC/ABN) | **Excellent** | Best candidate |
| Polycythemia Vera | 1 (JAK2) | 4 | 4 | Good | Clean JAK2→erythropoiesis chain |
| Essential Thrombocythemia | 3 (JAK2/CALR/MPL) | 3 | 3 | Good | Platelet lineage |
| Primary Myelofibrosis | 4 | 4 | 4 | Good | Fibrosis mechanism |
| Fanconi Anemia | 22+ | 16 | 0 | Good (complex) | Many-to-many |
| Hemochromatosis | 1 (HFE) | 5 | 0 | Good (implicit) | Missing biochemical section |
| G6PD Deficiency | 1 | 5 | 0 | Partial | Needs modifiers |
| Sickle Cell Disease | 3 (HBB+mods) | 4 | 0 | Partial | Imprecise GO terms |
| AIHA | 0 | 3 | 0 | Poor | No gene anchor |
| ITP | 0 | 4 | 0 | Poor | No gene anchor |

**Best candidates for K562/blood validation:** CML, PV, ET, PMF (myeloproliferative neoplasms)
**Best candidates for T cell/immune validation:** All 14 autoimmune diseases already in KB

---

## 2026-02-14 - T cell/autoimmune validation completed

**Result:** 2.7% gene confirmation rate (11/408 genes across 12 diseases, 146 significant pairs).

This reflects a gene coverage gap, not contradictions. dismech has 3-11 genes per disease
(the classic GWAS hits) while the pipeline tests hundreds from Open Targets. The confirmed
genes (PTPN22, CTLA4, IL2RA, IL4, IL23R, etc.) are exactly the well-documented ones.

**Key outputs:**
- Validation report: `docs/gwas-tcell-validation-report.md`
- Validation script: `scripts/validate_tcell_clusters.py`
- Data: `docs/assets/zhu_dann_2025/`

**Top curation targets identified:** EGR2, BACH2, ETS1, IRF4, TNFAIP3, IKZF1, CD28,
STAT3, GATA3, SMAD3, IL10 -- all well-known autoimmune genes missing from dismech.

**Cluster 79 (Th17: IRF4, BATF, STAT3, JUNB)** is the standout -- OR=58.2 for Crohn's,
38.1 for eczema, 26.9 for psoriasis. Th17 pathophysiology should be strengthened across entries.

**Missing KB entry:** Atopic Dermatitis/Eczema (16 significant pairs, strong pipeline signal).

**Next steps:** Add pleiotropic autoimmune genes to relevant entries; curate Atopic Dermatitis;
strengthen Th17 pathophysiology in Crohn's, Psoriasis, Ankylosing Spondylitis.

## 2026-02-14 - Mechanism-level gap filling

Addressed GO term and cell type gaps across autoimmune entries to enable mechanism-level
matching against Zhu/Dann T cell clusters.

**Asthma.yaml** (most significant changes):
- Added `biological_processes` GO terms to ALL 4 existing pathophysiology entries:
  - Airway Inflammation: GO:0006954 inflammatory response, GO:0002437 inflammatory response to antigenic stimulus
  - Bronchoconstriction: GO:0006939 smooth muscle contraction
  - Mucus Overproduction: GO:0070254 mucus secretion
  - Airway Remodeling: GO:0048771 tissue remodeling
- Added NEW pathophysiology entry: "Type 2 Immune Response / Th2 Signaling"
  - 5 GO biological_processes: GO:0042092, GO:0045064, GO:0035771, GO:0035708, GO:0032633
  - 6 genes: IL4, IL13, IL4R, STAT6, IL5, GATA3 (with HGNC IDs)
  - 4 cell types: Th2 cell, ILC2, mast cell, eosinophil
  - Downstream links to Airway Inflammation and Mucus Overproduction
  - This directly enables matching against Cluster 85 (STAT6, IL4R, RBPJ)

**Psoriasis.yaml**:
- Added GO:0072538 (T-helper 17 type immune response) to IL-23/IL-17 Axis entry
- Added cell types (Th17 cell, dendritic cell) that were missing

**Ankylosing_Spondylitis.yaml**:
- Added GO:0072538 to IL-23/IL-17 Axis Activation entry
- Changed cell type from generic CD4+ T helper to specific T-helper 17 cell
- Added dendritic cell

**Rheumatoid_Arthritis.yaml**:
- Added biological_processes to Autoimmune Response (had Th17 cell type but zero GO terms)
- GO:0072538 (T-helper 17 type immune response) + GO:0006954 (inflammatory response)

**Multiple_Sclerosis.yaml**:
- Added NEW pathophysiology entry: "Th1/Th17-Mediated Neuroinflammation"
  - GO:0072538 (Th17 immune response), GO:0006954 (inflammatory response)
  - Cell types: T-helper 17 cell, T-helper 1 cell
  - Downstream link to Inflammatory Lesions
  - Evidence from PMID:32801039 (Moser et al. 2020) and PMID:21338381 (Jadidi-Niaragh 2011)
- Added biological_processes + cell_types to Inflammatory Lesions entry

**Systemic_Lupus_Erythematosus.yaml**:
- Added biological_processes to Formation of Immune Complexes (GO:0002377, GO:0006958, GO:0019724)

**Hashimotos_Thyroiditis.yaml**:
- Added biological_processes to Lymphocytic Infiltration (GO:0006954, GO:0002250)

**Ulcerative_Colitis.yaml**:
- Added biological_processes to Dysregulated Immune Response (GO:0042092, GO:0006954)

**NEW: Atopic_Dermatitis.yaml** (complete new entry):
- 4 pathophysiology mechanisms with GO terms, cell types, evidence
- 5 phenotypes with HP terms, 5 genetic entries, 3 environmental factors, 5 treatments
- Evidence from PMID:16550169, PMID:30819278, PMID:21388665
- Enables matching against Cluster 79 (Th17, OR=38.1) and Cluster 85 (Th2)

**Validation improvement:** 13 diseases evaluated (up from 12), 162 cluster-disease pairs (up from 146)

**Remaining gaps:**
- [x] Add pleiotropic autoimmune genes (EGR2, BACH2, ETS1, IRF4, STAT3, etc.) across entries → DONE (see below)
- [ ] Epigenetic regulation mechanism (clusters 38, 59) - not documented in any entry
- [ ] T cell metabolic reprogramming / mTOR (cluster 100) - undocumented

## 2026-02-14 - Pleiotropic gene additions (batch 1: 6 genes)

Added BACH2, TNFAIP3, STAT3, IL10, CD28, EGR2 across 12 disease files.
Result: 17 confirmed genes, 4.0% rate.

## 2026-02-14 - Pleiotropic gene additions (batch 2: 10 genes)

Added 10 more pleiotropic GWAS genes across all 12 autoimmune disease files:
- ETS1 (10 diseases), IRF4 (9), IRF8 (7), SATB1 (8), IKZF1 (8)
- SMAD3 (8), REL (6), PRDM1 (6), PTPN22 extension (6 new), IL21R (4)

**Result: 26 confirmed genes, 6.1% rate** (up from 4.0%)

Per-disease rates: Celiac 29.6%, Psoriasis 25.0%, MS 19.1%, SLE 19.4%, T1D 18.9%,
AS 17.6%, Crohn's 15.3%, AD 15.2%, UC 15.5%, Hashimoto's 12.8%, RA 12.0%, Asthma 10.6%

Top remaining novel genes (diminishing returns): IL2RA extension, FOSL2, IL7R, ADO,
FADS2, BCL2L11, PRKCB - these are less established classical autoimmune GWAS hits.

**Remaining mechanistic gaps:**
- [x] Epigenetic regulation (clusters 38/59) → Added to RA and SLE
- [x] T cell metabolic reprogramming (cluster 100) → Added to SLE (combined entry)
- [ ] IL2RA extension to remaining diseases (already in T1D, needs 8+ more)
- [ ] Additional epigenetic entries could be added to MS, Crohn's, psoriasis

## 2026-02-14 - Epigenetic/metabolic mechanism entries

Added two new pathophysiology entries to capture cross-cutting regulatory mechanisms
from Zhu/Dann clusters 38, 59, and 100:

**Rheumatoid_Arthritis.yaml**:
- "Epigenetic Dysregulation of T Cell Function" with GO:0006338 (chromatin remodeling),
  GO:0040029 (epigenetic regulation of gene expression), GO:0030217 (T cell differentiation)
- Cell types: Th17, CD4+ helper T cell
- Downstream link to Autoimmune Response

**Systemic_Lupus_Erythematosus.yaml**:
- "Epigenetic Dysregulation and T Cell Metabolic Reprogramming" with GO:0040029, GO:0030217
- Notes cluster 100 OR=3.7 for SLE (strongest metabolic/stress signal)
- Downstream link to Autoantibody Production

These entries enable mechanism-level matching for clusters 38 (MLL2 complex; DOT1L, MEN1),
59 (RNF20, HDAC7), and 100 (ATF4, GLS, CBLB) against dismech pathophysiology GO terms.

## 2026-02-14 - Project created
- Found existing detailed integration plan at `docs/causal-modeling-integration-plan.md`
- Supplementary tables S1-S5 already downloaded (S3-S5 were not noted in the plan doc)
- Table S3 contains S-LDSC heritability enrichment (cell type specificity) - important for identifying which traits are well-modeled by K562
- Table S4 appears to be an alternate program annotation (variant analysis)
- Table S5 describes the Perturb-seq datasets used (5 datasets including K562 genome-wide)
- No dedicated GitHub repo for main analysis code exists yet
- T cell follow-up (Zhu/Dann et al. Dec 2025) has a GitHub repo and would extend this to immune traits
- Companion paper (Spence et al.) on gene ranking biases is relevant context
- 12 existing blood/hematological disorders in KB provide reasonable starting coverage
- Key gap: Thalassemia (alpha/beta), Iron Deficiency Anemia, Aplastic Anemia not yet curated
