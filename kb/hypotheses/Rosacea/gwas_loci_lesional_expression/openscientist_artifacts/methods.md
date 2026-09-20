# Methods — Rosacea GWAS loci lesional expression (GSE65914)

## Data source
- **Series:** GEO **GSE65914**, "Th1/Th17 Immune Response in Rosacea".
- **Platform:** **GPL570** (Affymetrix Human Genome U133 Plus 2.0 Array).
- **Files retrieved (credential-free URLs):**
  - Expression: `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65914/matrix/GSE65914_series_matrix.txt.gz`
  - Probe→gene annotation: `https://ftp.ncbi.nlm.nih.gov/geo/platforms/GPLnnn/GPL570/annot/GPL570.annot.gz` (GEO annotation dated Aug 09 2016).

## Source normalization / transform state
- Per the series `!Sample_data_processing` field, values were produced with
  Affymetrix Expression Console using **RMA normalization**, i.e. already on a
  **log2 scale** (observed range ≈ 2–14). **No additional transform** was applied.
- Because data are log2, the **log2 mean difference** equals `mean_lesional − mean_control`
  and the **ordinary fold change** = `2^(log2 mean difference)`.

## Sample inclusion / exclusion
- All **58** samples were included; **no samples were excluded**.
- Groups were read verbatim from `!Sample_characteristics_ch1` (`group:` field) and mapped:
  - `Healthy volunteer` → **control** (n = 20)
  - `erythematotelangiectatic rosacea (ETR)` → **ETR** (n = 14)
  - `papulopustular rosacea (PPR)` → **PPR** (n = 12)
  - `phymatous rosacea (PhR)` → **PhR** (n = 12)
  - pooled rosacea = ETR ∪ PPR ∪ PhR (n = 38)
- Tissue: facial skin biopsy; organism: *Homo sapiens*. All rosacea biopsies are
  lesional; the contrast is **lesional vs healthy control**.
- **Note on replicates:** sample titles carry `_1`/`_2` suffixes per subject
  (technical/duplicate arrays). Each GEO sample (GSM) is treated as one row, matching
  the GEO sample count; see limitations (pseudoreplication).

## Identifier / probe mapping and aggregation
- Probe→gene mapping taken from the GPL570 `Gene symbol` column.
- Multi-gene probes (symbols joined by `///`) are assigned to **every** listed gene;
  a probe maps to a target gene if that symbol appears in its `///`-split list.
- **Aggregation:** for each gene and sample, matching probes are combined by the
  **arithmetic mean on the log2 scale**. Probe counts per gene are reported (`n_probes`).

## Target genes and locus class
- **Immune:** HLA-DRA, BTNL2, HLA-DRB1, HLA-DQB1, HLA-DQA1, IL13, IRF1, TLR1, TLR2, IRF4.
- **Pigmentation:** HERC2, OCA2, SLC45A2.

## Statistical tests
- **Contrast per gene × comparison** (4 comparisons: ETR, PPR, PhR, pooled — each vs control):
  **Welch's two-sample t-test** (`scipy.stats.ttest_ind`, `equal_var=False`) on gene-level
  log2 values.
- Reported per row: group sizes, group means (log2), log2 mean difference,
  ordinary fold change, t-statistic, raw p-value, BH q-value, Cohen's d.
- **Effect size:** Cohen's d with pooled SD (ddof = 1); **positive d = higher in lesional**.
- **Multiple testing:** Benjamini–Hochberg FDR (`statsmodels multipletests`, `fdr_bh`)
  applied **jointly across all 52 gene × comparison tests** (13 genes × 4 comparisons).
- **TLR1–TLR2 relationship:** **Spearman** rank correlation (`scipy.stats.spearmanr`)
  of gene-level TLR1 vs TLR2, computed across **all** samples, within **rosacea**, and
  within **control**. Difference between the rosacea and control Spearman coefficients was
  tested with **Fisher r-to-z** (`z = (atanh r1 − atanh r2)/sqrt(1/(n1−3)+1/(n2−3))`,
  two-sided normal p-value).

## Determinism
- No random components. Rows are sorted (samples by accession; gene results by gene then
  fixed comparison order). Floats rounded to 10 decimals with `\n` line terminators, giving
  byte-identical primary and replay outputs.
