# Methods

## Source data (single input, shared lineage - re-analysis, not replication)
- He et al. 2026, Nature Medicine. PMID:42778763; doi:10.1038/s41591-025-04128-1.
- Input: Supplementary Data zip `41591_2025_4128_MOESM3_ESM.zip` (sha256 `27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865`).
- Underlying cohort: PsychAD snRNA-seq, human dorsolateral prefrontal cortex (DLPFC),
  1,494 donors (synapse:syn60084804). The controlled cohort was NOT accessed; only
  the open Supplementary workbooks (.xlsx) were used.
- Package added to approved list for reading .xlsx: openpyxl (preflighted).

## Sample inclusion / exclusion
- "Samples" = donors in Supplementary Data 6 sheet 'Avg. PAC scores AD progression'
  (n=581), used for the within-donor correlation objective. Donors carry ID only; no
  diagnosis/Braak/resilience labels are present, so donors were NOT assigned to groups
  and no label-dependent test was run. No donor excluded (all rows have complete
  numeric PAC vectors). See samples.csv.

## Normalization / transform state
- All quantities are PUBLISHED derived scores; no re-normalization or re-transform was
  applied. PAC (phenotype-associated-cell) scores are used as provided. DEG effect
  sizes are the published log2(fold change); no re-scaling.
- Fig.3f median-PAC cells contained a stray leading-comma text artifact in the
  'AD strict median PAC score' column; values were parsed by stripping the leading
  comma/whitespace and casting to float (no numeric change).

## Identifier / probe mapping and aggregation
- Gene symbols used as provided in the workbooks (one row per gene per subclass block).
- Reactive-astrocyte marker sets are prespecified (Liddelow-type axis). Mapping rules:
  * H2-T23 (mouse MHC class-I) -> human ortholog HLA-E (class A1).
  * IIGP1 -> no 1:1 human ortholog -> SKIPPED.
- pan-reactive (13): LCN2,STEAP4,S1PR3,TIMP1,HSPB1,CXCL10,CD44,OSMR,CP,SERPINA3,ASPG,VIM,GFAP
- A1/neurotoxic (10 after mapping): C3,HLA-E,SERPING1,GBP2,FBLN5,UGT1A1,FKBP5,AMIGO2,PSMB8,SRGN
- A2/neuroprotective (12): CLCF1,TGM1,PTX3,S100A10,SPHK1,CD109,PTGS2,EMP1,SLC10A6,TM4SF1,B3GNT5,CD14
- individual: CRYAB, MAOB, CHI3L1

## Astrocyte DEG tables used (identified from each workbook 'key' sheet)
- Supplementary Data 7 'AD PAC DEGs', Astrocyte block (AD-PAC+ vs AD-PAC-, PAC-level;
  1,171 significant genes) -- PRIMARY for objective 2.
- Supplementary Data 1 'Fig. 2f', Astrocytes donor-level and PAC-level (AD vs Control;
  significant genes only).
- Supplementary Data 3 'Depression PAC DEGs in Astrocyte' (phenotype = Depression, not
  AD; included for completeness and marked as such).
- (Excluded from astrocyte set: Supp Data 2 'Fig. 3g' and 'Fig. 3d' are neuronal-only
  DEG tables; Supp Data 3 'Upregulated genes in AD-Depr.-AstroWIF1' is a one-directional
  cluster-marker list, not a two-sided DEG table.)

## Statistical tests
1. Objective 1: report published Fig.3f adjusted P and (strict - resilient) median PAC
   difference for Astro among all subclasses (re-statement of published values).
2. Objective 2:
   - Overlap enrichment (one-sided Fisher exact, 'greater') of each marker set among the
     1,171 astrocyte DEGs, with explicit background = union of all genes reported across
     the 21 subclass blocks of Supp Data 7 'AD PAC DEGs' (11,145 genes = genes tested/
     detected in >=1 PsychAD subclass DE model).
   - Directional A2-vs-A1 Fisher exact ('greater') among marker genes that are
     significant astrocyte DEGs, testing whether A2 markers preferentially fall in the
     "higher-in-resilient" direction. Direction is INFERRED: Fig.3f shows resilient
     donors have LOWER Astro PAC, so down-in-AD-PAC (log2FC<0) is treated as the
     resilient-like direction and up (log2FC>0) as the impaired/strict-like direction.
     This inference is a chained assumption, NOT a direct resilient-vs-strict astrocyte
     measurement (no such astrocyte DEG table exists in the supplement).
   - EMP1 (A2) and FKBP5 (A1) reported explicitly.
3. Objective 3: Spearman correlation of donor Astro PAC vs every excitatory (EN_*) and
   inhibitory (IN_*) subclass in 'Avg. PAC scores AD progression' (n=581 donors, all
   pairs complete).

## Multiple-testing and effect-size conventions
- Multiple testing: Benjamini-Hochberg FDR (statsmodels fdr_bh) applied within each
  results table (gene_results per dataset/comparison; enrichment across its tests;
  correlations across the 17 subclasses).
- Effect-size convention: published log2(fold change) is the primary DEG effect size;
  ordinary fold change = 2^log2FC is also reported. Group means and Cohen's d are NOT
  recoverable from published summary statistics (no per-cell/per-donor expression
  matrix; donors unlabeled) and are left blank, by design. Group sizes reflect the
  documented balanced donor subsets (Supp Data 5 'PAC number': AD 100 vs 100;
  Depression/Mood 100 vs 100) for PAC-level comparisons; blank for donor-level.
- Correlation effect size: Spearman rho.

## Determinism
- No random operations. Stable mergesort ordering; inputs read from the fixed-checksum
  zip. Re-running regenerates byte-identical samples.csv and gene_results.csv.
