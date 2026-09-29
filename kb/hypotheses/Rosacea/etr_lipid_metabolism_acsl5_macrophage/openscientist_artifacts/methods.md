# Methods — ETR vs healthy-control contrast in GSE65914

## Dataset
- **Series:** GSE65914 ("Th1/Th17 Immune Response in Rosacea"; PubMed 25848978).
- **Platform:** GPL570 — Affymetrix Human Genome U133 Plus 2.0 Array (54,675 probe sets).
- **Tissue / organism:** Human facial skin biopsies, *Homo sapiens*.
- **Retrieved inputs (canonical, credential-free URLs):**
  - Series matrix: `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65914/matrix/GSE65914_series_matrix.txt.gz`
  - Platform annotation: `https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz`

## Sample inclusion / exclusion
The series contains 58 arrays across four `group:` levels (from
`!Sample_characteristics_ch1`):
- `Healthy volunteer` — n = 20 → assigned **control** (included)
- `erythematotelangiectatic rosacea (ETR)` — n = 14 → assigned **ETR** (included)
- `papulopustular rosacea (PPR)` — n = 12 → **excluded** (not part of the
  prespecified ETR-vs-healthy-control contrast)
- `phymatous rosacea (PhR)` — n = 12 → **excluded** (same reason)

Group assignment uses an exact string match on the curated `group:` characteristic.
Each subject contributes two arrays (`_1` / `_2` suffix); arrays are treated as
independent observations for this prespecified sample-level contrast (see
Limitations). Final contrast: **ETR n = 14 vs control n = 20**. One row per
array (included or excluded) is recorded in `samples.csv`.

## Source normalization state and transform decisions
Values in the series matrix are strictly positive with a compact range
(~2 to ~15, maximum < 16), which is the signature of GEO-supplied,
**already-normalized log2-scale** expression. **No additional normalization or
transformation was applied.** Because values are already log2, the difference of
group means is directly the log2 mean difference, and ordinary fold change is
`2 ** (log2 mean difference)`.

## Identifier / probe mapping and aggregation
- Probe→gene mapping uses the curated `Gene symbol` column of the GPL570 SOFT
  annotation. Probes annotated to multiple genes carry `///`-joined symbols; a
  probe matches a target gene if that symbol appears in the split list. (CD68 is
  covered only by the multi-gene probe `203507_at` =
  `LOC101928634///SNORA67///CD68`.)
- Probes mapped per target gene (`probe_gene_map.csv`):
  - ACSL5: 218322_s_at, 222592_s_at
  - ACADVL: 200710_at
  - PPARG: 208510_s_at
  - CPT1A: 203633_at, 203634_s_at, 210687_at, 210688_s_at
  - CD68: 203507_at
  - CD163: 203645_s_at, 215049_x_at, 216233_at
  - CD86: 205685_at, 205686_s_at, 210895_s_at
- **Aggregation:** gene-level expression = arithmetic **mean of all mapped probes**
  per sample, computed on the log2 scale.

## Statistical tests
- **Contrast per gene:** two-sample **Welch's t-test** (unequal variance;
  `scipy.stats.ttest_ind(equal_var=False)`) comparing ETR vs control gene-level
  log2 expression.
- **Effect size:** **Cohen's d** with pooled standard deviation over both groups,
  oriented as ETR − control (positive = higher in ETR).
- **Fold change:** `log2_mean_diff = mean_ETR − mean_control`;
  `fold_change = 2 ** log2_mean_diff`.
- **Multiple-testing correction:** Benjamini–Hochberg FDR across the 7-gene
  prespecified set (`statsmodels multipletests method='fdr_bh'`), reported as
  `q_value_BH`.
- **Within-ETR association:** **Spearman rank correlation** of gene-level ACSL5
  vs each macrophage marker (CD68, CD163, CD86) across the 14 ETR arrays
  (`scipy.stats.spearmanr`); BH-FDR across the 3 correlations.

## Material parameters / determinism
- Fixed target-gene order: ACSL5, ACADVL, PPARG, CPT1A, CD68, CD163, CD86.
- Input SHA-256 integrity is verified on every run; probe order is sorted for
  determinism. No randomness is used. Outputs are byte-reproducible.

## Outputs
- `samples.csv`, `gene_results.csv`, `spearman_acsl5_macrophage.csv`,
  `probe_gene_map.csv`.
