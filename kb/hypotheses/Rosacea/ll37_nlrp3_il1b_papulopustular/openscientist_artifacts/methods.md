# Methods — GSE155141 replication (ll37_nlrp3_il1b_papulopustular)

## Dataset
- **Accession:** GEO `GSE155141` — "Paired transcriptomic and proteomic analysis
  implicates IL-1β in the pathogenesis of papulopustular rosacea explants [RNA-seq]".
- **Platform:** GPL16791 (Illumina HiSeq 2500), human (taxid 9606), facial-skin explants.
- **Source processing state (as provided by submitter):** raw integer gene-level
  counts. Reads mapped to hg38 with STAR; read pairs counted against
  `gencode.v27.annotation.gtf` with `htseq-count`. Gene identifiers are HGNC symbols.
  Files are supplied **un-normalized** (raw counts).

## Inputs retrieved (credential-free NCBI GEO URLs)
- `matrix/GSE155141_series_matrix.txt.gz` — sample metadata / group assignment.
- `suppl/GSE155141_rawCount_rosacea_no_Tx.txt.gz` — 5 lesional samples (S1–S5).
- `suppl/GSE155141_rawCount_nonlesional_noTx_IL1.txt.gz` — 10 samples
  (5 non-lesional untreated + 5 non-lesional IL-1β).

## Sample inclusion / exclusion
- **Design:** 5 subjects (S1–S5), each contributing 3 explant conditions:
  lesional (no treatment), non-lesional (no treatment), non-lesional + 50 ng/mL
  IL-1β for 24 h. 15 samples total.
- **Inclusion:** all 15 samples are included; none excluded. Each condition group
  has n = 5, one sample per subject, enabling paired analysis.
- Raw-count files are headerless tab-delimited tables; column 0 is the gene symbol
  and remaining columns are counts ordered by subject 1–5 (per submitter note
  "sample ordered by 1-5").

## Sample classification / column assignment
- `rawCount_rosacea_no_Tx` columns 1–5 → lesional S1–S5.
- `rawCount_nonlesional_noTx_IL1` columns 1–5 → non-lesional untreated S1–S5;
  columns 6–10 → non-lesional IL-1β-treated S1–S5.
- The untreated-vs-IL1β column split was **empirically verified**: canonical
  NF-κB/IL-1 response genes are elevated in columns 6–10 relative to 1–5
  (mean CPM ratios: SOD2 2.38×, CCL20 2.90×, IL1B 2.22×, NFKBIA 1.91×,
  CXCL8 1.78×, TNFAIP3 1.62×), consistent with IL-1β stimulation.
- GSM↔column mapping is hard-coded from the series-matrix `!Sample_geo_accession`
  order and recorded per sample in `samples.csv`.

## Identifier / probe mapping and aggregation
- Features are already HGNC gene symbols (no probe mapping needed).
- The 56,614 gene symbols are unique in both files (no duplicate symbols), and the
  gene order is identical across files, so no cross-file aggregation is required.
- The 8 target genes (NLRP3, CASP1, PYCARD, IL1B, IL18, IL1RN, CAMP, KLK5) are each
  present exactly once.

## Normalization and transform
- Library-size scaling to counts-per-million (CPM): `CPM = count / colsum * 1e6`
  using each sample's total counts over all 56,614 genes.
- Transform: `log2(CPM + 1)`. Group means and the paired test operate on this
  log2(CPM+1) scale.

## Statistical tests
- Two prespecified paired contrasts, pairing by subject (S1–S5):
  1. **lesional_vs_nonlesional** — lesional (test) vs paired non-lesional untreated (ref).
  2. **il1b_vs_untreated_nonlesional** — non-lesional IL-1β (test) vs paired non-lesional untreated (ref).
- Test: two-sided paired t-test (`scipy.stats.ttest_rel`) on log2(CPM+1) values,
  n = 5 pairs per contrast.
- **Every target gene is reported regardless of significance.**

## Multiple-testing correction
- Benjamini–Hochberg FDR (`statsmodels multipletests, method="fdr_bh"`) applied
  **within each contrast across the 8 target genes** → `q_value`.

## Effect-size convention
- `log2_mean_diff = mean_group2 − mean_group1` (test minus reference) on log2(CPM+1).
- `fold_change = 2 ** log2_mean_diff` (linear-scale fold change of the log2 means;
  > 1 means higher in the test group).
- `cohens_d` = paired standardized effect `d_z = mean(diff) / sd(diff, ddof=1)`,
  where `diff = test − reference` across the 5 subject pairs; positive = up in test.

## Determinism
- No randomness, no LLM. `analysis.py` accepts `--output-dir` and `--cache-dir`,
  reuses cached raw inputs when present, and regenerates byte-identical
  `samples.csv` and `gene_results.csv`. A clean replay reusing `raw/` as cache was
  verified byte-identical (see `MANIFEST.yaml` → `replay`).

## Limitations
- n = 5 per group; paired t-tests are low-powered and per-gene, not a full RNA-seq
  DE model (e.g., DESeq2/limma-voom). Results are gene-targeted replication metrics,
  not genome-wide DE.
- CPM+log2 is a simple within-file normalization; no between-file batch adjustment
  is applied, though the paired lesional/non-lesional contrast spans two files.
- Subjects S1 and S5 reuse identical library barcodes in the sample descriptions
  but carry distinct subject ages (82 vs 73) and GSM accessions; they are treated
  as 5 distinct subjects per GEO metadata.
