# Methods

## Provenance and lineage
Input: He et al. 2026, Nature Medicine (PMID 42778763; doi:10.1038/s41591-025-04128-1),
Supplementary Data zip `41591_2025_4128_MOESM3_ESM.zip`
(sha256 `27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865`,
13,893,637 bytes). These are the published, already-derived phenotype-associated-cell
(PAC) scores and DEG tables from the controlled PsychAD snRNA-seq cohort
(synapse:syn60084804, 1,494 donors, DLPFC). No controlled/Synapse data were accessed.
Every result below is a RE-ANALYSIS of published derived scores and shares data
lineage with the paper; it is not an independent replication.

## Sheets read
- Supplementary_Data_6.xlsx: 'Avg. PAC scores DepressionMood' (210 donors x 27 subclasses),
  'Avg. PAC scores AD progression' (581 donors x 27 subclasses),
  'SHAP values DepressionMood' (210 rows x 27 subclasses).
- Supplementary_Data_3.xlsx: 'Depression PAC DEGs in Astrocyt' (depression-PAC+ vs
  depression-PAC- astrocyte DEGs), 'Upregulated genes in AD-Depr.-A'
  (AD-Depression Astro_WIF1 cluster up-genes, Fig. 4F),
  'Downregulated genes in AD-Depr.' (AD-Depression Oligo_OPALIN cluster down-genes).
- Supplementary_Data_7.xlsx: 'AD PAC DEGs', astrocyte block (columns 0-4).

## Sample inclusion/exclusion
Samples are donors identified by donor ID only. Supplementary Data 6 carries NO
diagnosis/Braak/resilience labels, so no donor labels were inferred or invented.
Analyses were restricted to tests needing no labels:
(1) within-cohort cross-phenotype correlation on the intersection of donors present
in both the DepressionMood and AD-progression PAC sheets (n=208 common donors);
(2) gene-set overlap/enrichment against published DEG tables. Donors present in only
one PAC sheet are recorded in samples.csv as excluded from the correlation with reason.

## Source normalization / transforms
PAC scores and SHAP values are used exactly as published (no re-normalization,
scaling, or transform). DEG gene symbols are upper-cased and whitespace-stripped for
set operations; no probe mapping is needed (tables are already gene-symbol level).
Header rows in Supp Data 3/7 are located by the 'Gene Name' marker; the astrocyte
block of Supp Data 7 is located by the 'Astrocyte' label in the block-label row.

## Statistical tests
1. Subclass correlation: Spearman rho between each subclass's DepressionMood PAC score
   and AD-progression PAC score across the 208 common donors (27 tests). A DISTINCT
   depression signal predicts weak correlation for Astro and Oligo.
2. Subclass importance: subclasses ranked by mean absolute SHAP value (DepressionMood).
3. Gene-set enrichment: one-sided Fisher exact test (alternative='greater') for
   over-representation of two prespecified sets - UPR/ER-stress
   (HSPA5,DDIT3,ATF4,ATF6,XBP1,ERN1,EIF2AK3,HSP90B1,PDIA4,PDIA6,CALR,DNAJB9,SEL1L,HERPUD1,MANF)
   and inflammatory signalling
   (NFKBIA,IL1B,IL6,CXCL8,TNF,STAT3,SOCS3,C3,CHI3L1,SERPINA3,CD44) - in
   (a) depression-PAC astrocyte DEGs and (b) the AD-Depression Astro_WIF1 up-cluster.
   Two explicit gene universes are reported: 'deg_union' = union of all loaded DEG-table
   genes plus the prespecified sets (N=2499; DEG-restricted, conservative) and
   'genomic_19000' = ~19,000 protein-coding-gene background (sensitivity).
4. Overlap: intersection, union and Jaccard index of depression-PAC astrocyte DEGs vs
   Supp Data 7 AD-PAC astrocyte DEGs; ER-stress gene membership compared across sets to
   assess depression-specificity.

## Multiple testing and effect sizes
Benjamini-Hochberg FDR is applied within each family (27 correlation tests; 8 enrichment
tests). Effect-size conventions: Spearman rho (correlation), odds ratio (enrichment),
Jaccard index (overlap), and paired Cohen's d = mean(depPAC-ADprogPAC)/SD of the paired
difference (reported per subclass in gene_results.csv). Fold change and log2 mean
difference in gene_results.csv are computed on the ABSOLUTE subclass mean PAC scores and
are undefined (NaN) when a mean is zero; these are provided for schema completeness and
are not the primary effect size for signed PAC scores.

## Determinism
No random operations. Rows sorted by stable keys; inputs read from the fixed cached zip.
Re-running analysis.py on the same cache produces byte-identical tabular outputs.
