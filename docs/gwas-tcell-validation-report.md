# Validation Report: Zhu/Dann T Cell Perturb-seq vs DisMech Autoimmune Entries

**Date:** 2026-02-14
**Pipeline:** Zhu, Dann, Ota, Pritchard, Marson et al. (bioRxiv Dec 2025)
**Method:** Genome-scale CRISPRi Perturb-seq in primary CD4+ T cells; 111 regulator clusters
tested for enrichment of GWAS disease genes (Open Targets, genetic_evidence >= 0.1)

## Summary

| Metric | Value |
|--------|-------|
| Diseases evaluated | 12 (of 14 tested; autoimmune umbrella excluded, atopic eczema not in KB) |
| Significant cluster-disease pairs (FDR < 0.05) | 146 |
| Unique GWAS genes tested | 408 |
| Genes confirmed in dismech | 11 (2.7%) |
| Genes novel to dismech | 405 (99.3%) |

### Per-Disease Confirmation Rates

| Disease | dismech Genes | Pairs | Confirmed | Novel | Rate |
|---------|--------------|-------|-----------|-------|------|
| Type 1 diabetes | 10 | 5 | 3 | 34 | 8.1% |
| Hashimoto's thyroiditis | 4 | 7 | 2 | 37 | 5.1% |
| Multiple sclerosis | 6 | 14 | 3 | 65 | 4.4% |
| SLE | 11 | 11 | 2 | 65 | 3.0% |
| Asthma | 6 | 13 | 3 | 110 | 2.7% |
| Rheumatoid arthritis | 9 | 15 | 3 | 139 | 2.1% |
| Psoriasis | 5 | 9 | 1 | 59 | 1.7% |
| Ulcerative colitis | 4 | 16 | 1 | 96 | 1.0% |
| IBD (merged) | 10 | 17 | 1 | 156 | 0.6% |
| Crohn's disease | 6 | 17 | 0 | 98 | 0.0% |
| Ankylosing spondylitis | 3 | 15 | 0 | 74 | 0.0% |
| Celiac disease | 4 | 7 | 0 | 27 | 0.0% |

### Confirmed Genes

These dismech-curated genes were rediscovered by the T cell Perturb-seq pipeline:

| Gene | Confirmed In | Role |
|------|-------------|------|
| PTPN22 | RA, Hashimoto's, T1D, SLE (12 pairs) | Shared autoimmune susceptibility; T cell signaling |
| CTLA4 | RA, Hashimoto's, T1D (5 pairs) | T cell co-inhibition; immune checkpoint |
| IL2RA | MS, T1D (5 pairs) | IL-2 receptor alpha; Treg homeostasis |
| IL4 | Asthma (4 pairs) | Th2 cytokine; allergic inflammation |
| STAT4 | RA, SLE (2 pairs) | Th1/Th17 signaling |
| IL13 | Asthma (2 pairs) | Th2 cytokine; allergic inflammation |
| IL23R | IBD (2 pairs) | Th17 differentiation |
| IL7R | MS (2 pairs) | T cell homeostasis |
| ORMDL3 | Asthma (1 pair) | ER stress, sphingolipid metabolism |
| TNFAIP3 | Psoriasis (1 pair) | NF-kB negative regulation (A20) |
| TNFRSF1A | MS (1 pair) | TNF receptor; neuroinflammation |

## Interpretation

### Why is the confirmation rate so low?

The 2.7% rate does **not** indicate contradiction. It reflects a **gene coverage gap** in dismech:

1. **dismech has 3-11 genes per disease** (median ~6), curated from classic GWAS papers and textbook genetics. These are the "greatest hits" -- HLA loci, PTPN22, IL23R, NOD2, etc.

2. **The pipeline tests hundreds of genes per disease** from Open Targets (genetic_evidence_score >= 0.1), including many more recent GWAS discoveries, rare variant associations, and genes with modest effect sizes.

3. **The "novel" genes are mostly real.** EGR2, BACH2, IRF4, STAT3, TNFAIP3, IKZF1, CD28, GATA3, SMAD3 are well-established autoimmune risk genes in the literature. They are "novel" only in the sense that dismech hasn't curated them yet.

### What does dismech confirm well?

The confirmed genes cluster into functional categories:
- **T cell signaling:** PTPN22, CTLA4, IL2RA, IL7R, CD28 (partial)
- **Cytokines:** IL4, IL13, IL23R
- **Transcription factors:** STAT4

These are exactly the genes where dismech has the strongest mechanistic documentation.

### What does dismech miss?

The top "novel" genes (appearing in 7+ diseases) reveal systematic gaps:

| Gene | #Diseases | Function | Gap Type |
|------|-----------|----------|----------|
| EGR2 | 12 | T cell anergy/tolerance | Known risk gene, not curated |
| BACH2 | 12 | Treg/effector balance, class switch | Known risk gene, curated only in T1D |
| ETS1 | 11 | T cell development, Th17 | Known risk gene, not curated |
| IRF4 | 10 | Plasma cell differentiation, Th17 | Known risk gene, curated only in Vitiligo |
| STAT3 | 8 | Th17 signaling, acute phase | Known risk gene, not curated |
| IKZF1 | 9 | Lymphocyte development (Ikaros) | Known risk gene, not curated |
| CD28 | 9 | T cell co-stimulation | Known risk gene, not curated |
| GATA3 | 7 | Th2 master regulator | Known risk gene, not curated |
| SMAD3 | 9 | TGF-beta signaling, Treg | Known risk gene, not curated |
| IL10 | 8 | Anti-inflammatory cytokine | Known risk gene, not curated |

## Actionable Findings

### 1. High-Priority Gene Additions

These genes should be added to the `genetic` sections of multiple dismech entries.
Ranked by number of diseases where they appear as GWAS hits downstream of T cell regulators:

**Tier 1 (10+ diseases):** EGR2, BACH2, IL2RA*, IL7R*, TNFAIP3*, ETS1, ADO, IRF4
**Tier 2 (7-9 diseases):** IKZF1, STAT3, CD28, SMAD3, SATB1, NFKBIA, GATA3, CD6, IRF8, IL10, RASGRP1, FOXO1, PTPN22*
**Tier 3 (5-6 diseases):** SOCS1, MAP3K8, RIPK2, BATF, IL2, FAS, BCL2L11, SH2B3

(*) Already curated in some diseases but missing from others.

### 2. Missing Disease: Atopic Dermatitis/Eczema

Atopic eczema was tested in the pipeline (16 significant pairs) but we have no KB entry. This is a high-priority curation target given:
- Cluster 79 (Th17; IRF4, BATF, STAT3): OR=38.1
- Cluster 110: OR=24.3
- Strong overlap with asthma genetics

### 3. Cluster 79 (Th17 Differentiation) is the Standout

This 6-gene cluster (IRF4, BATF, STAT3, JUNB, IPMK, NUP188) shows the strongest enrichment across diseases:
- Crohn's: OR=58.2
- Atopic eczema: OR=38.1
- Psoriasis: OR=26.9
- IBD: OR=24.0
- MS: OR=16.9
- Autoimmune (general): OR=9.0

dismech should ensure Th17 differentiation is prominently featured in the pathophysiology of Crohn's, Psoriasis, and Ankylosing Spondylitis.

### 4. Schema Gap: Gene-Disease Specificity

Many genes (PTPN22, IL2RA, BACH2) are shared across autoimmune diseases but dismech only records them in 1-4 entries. The pipeline data provides evidence for which diseases each gene is relevant to, with enrichment statistics. Consider:
- Systematic addition of pleiotropic autoimmune genes across all relevant entries
- Recording the T cell regulatory context (which cluster, which condition)

## Methods

### Data Sources
- **Zhu/Dann enrichment results:** `cluster_autoimmune_enrichment_results.suppl_table.csv` from [GitHub](https://github.com/emdann/GWT_perturbseq_analysis_2025)
- **Disease gene sets:** Open Targets Platform, genetic_evidence_score >= 0.1
- **dismech entries:** 12 autoimmune disorder YAML files from `kb/disorders/`

### Matching Logic
- Gene symbols from enrichment `intersecting_genes` matched against dismech `genetic[].name` and `pathophysiology[].genes[].name`
- Exact string match (case-sensitive)
- IBD umbrella mapped to union of Crohn's Disease + Ulcerative Colitis genes

### Limitations
- Only matches gene symbols in structured fields; does not search free-text descriptions
- dismech uses some non-standard gene names (e.g., "HLA-B27" vs "HLA-B", "BCR-ABL1")
- Does not assess whether dismech's pathophysiology *narratives* describe the gene's mechanism
- The pipeline's gene sets come from Open Targets (which includes GWAS + rare variant evidence), not just the T cell Perturb-seq results directly

## Data Files
- Validation script: `scripts/validate_tcell_clusters.py`
- Enrichment data: `docs/assets/zhu_dann_2025/cluster_autoimmune_enrichment_results.csv`
- Cluster annotations: `docs/assets/zhu_dann_2025/clustering_results_and_annotations.csv`
