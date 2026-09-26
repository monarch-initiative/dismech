# Methods — GSE65391 interferon / plasmablast replication

## Data source (normalization state)
- Series: GSE65391 (pediatric SLE whole blood, Illumina HumanHT-12 v4, GPL10558).
- Expression matrix: GEO series matrix `GSE65391_series_matrix.txt.gz`. Values are the
  authors' processed, **log2-scale** normalized intensities (per-probe training/test
  ratio adjustment described in GEO `data_processing`). No further transform applied.
- Probe annotation: GEO `GPL10558.annot.gz` (GPL10558 annotation table, `Gene symbol`).

## Sample inclusion / exclusion
- Start: 996 arrays.
- Exclude `set == Technical_Replicate` (n=24) -> reason `technical_replicate`.
- Keep one array per (subject, visit); deterministic tie-break keeps the smallest
  GSM accession -> reason `duplicate_subject_visit` for any dropped array
  (none required: 0 duplicate subject-visit pairs remained after replicate removal).
- Included arrays: 972.
- Cross-sectional contrasts use each subject's **first included visit** only
  (minimum numeric `visit`; ties broken by GSM). Each subject contributes one sample.
- First-visit subjects: 204 (158 SLE, 46 Healthy).

## Probe -> gene mapping and aggregation
- Probes mapped to gene symbols via GPL10558 `Gene symbol`.
- When several probes map to one gene, the probe with the **highest mean expression
  across included samples** is used (tie-break: lexicographically smallest probe id).
- Probe selected per gene:
  - IFI27: ILMN_2058782
  - IFI44L: ILMN_1723912
  - IFIT1: ILMN_1707695
  - ISG15: ILMN_2054019
  - RSAD2: ILMN_1657871
  - SIGLEC1: ILMN_1725320
  - JCHAIN: ILMN_2105441
  - MZB1: ILMN_2193233
  - TNFRSF17: ILMN_1768016
- IGJ is not present in this GPL10558 annotation; the current symbol **JCHAIN**
  (ILMN_2105441) is used for the plasmablast J-chain gene.

## Composite interferon score
- `IFN6_SCORE` = mean of per-gene z-scores of IFI27, IFI44L, IFIT1, ISG15, RSAD2, SIGLEC1.
- Z-scores computed against the **Healthy first-visit** samples (mean and SD, ddof=1)
  per gene. The score is added as a row `IFN6_SCORE` in gene_results.csv.

## Contrasts (each reported for all target genes + IFN6_SCORE)
1. SLE vs Healthy (disease state), first visit.
2. Within SLE, SLEDAI>=6 vs SLEDAI<6 at first visit
   (SLEDAI>=6 n=94, SLEDAI<6 n=64).
3. Within SLE, biopsy-proven nephritis vs no nephritis at first visit
   (Nephritis n=33, NoNephritis n=125).

### Nephritis-class parsing (metadata ambiguity)
- Observed `nephritis_class` values within SLE first-visit:
  Prolif, Membr, Mesan, Proli+Membr (positive histologic LN classes),
  NoLN ("no lupus nephritis"), and "Data Not Available".
- **Nephritis** group = {Prolif, Membr, Mesan, Proli+Membr} (biopsy-proven LN class).
- **NoNephritis** group = {NoLN, "Data Not Available"} (no recorded positive LN class,
  matching the "not recorded / Not Applicable" rule). "Not Applicable" occurs only for
  Healthy samples and is therefore absent from this SLE-only contrast.

## Statistics
- Welch's two-sample t-test (unequal variance) for every gene/contrast.
- Effect size: pooled-SD Cohen's d, oriented as (group1 - group2) with group1 the
  "case" group (SLE / SLEDAI>=6 / Nephritis).
- `log2_mean_difference` = mean(group1) - mean(group2) (data already log2);
  `fold_change` = 2**log2_mean_difference (not biologically meaningful for the
  z-based IFN6_SCORE row, reported for schema completeness).
- Multiple testing: Benjamini-Hochberg FDR computed **within each contrast**
  across all rows (6 genes + IFN6_SCORE).

## Correlations (correlations.csv)
- Within SLE first-visit samples, Spearman correlation of IFN6_SCORE and plasmablast
  genes (JCHAIN, MZB1, TNFRSF17) against numeric sledai, ds_dna, c3, c4, neutrophil_count.
- Non-numeric or 'Not Applicable' clinical values treated as missing
  (pairwise-complete n reported). BH-FDR across all 20 feature x variable pairs.
- Note: `ds_dna` is largely reported as titers (e.g. "1:40"), "(-)", or
  "Data Not Available"; per the "non-numeric = missing" rule these become missing, so
  the numeric ds_dna sample size is small.
