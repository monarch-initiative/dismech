# Methods

Replication target: hypothesis `calcium_clearance_failure_model`
("Impaired Calcium Clearance and ECM-Calcium Coupling Model"), Duchenne Muscular Dystrophy.
Everything below was executed by `analysis.py` in this directory.

## Data retrieval

| Input | Canonical URL | Bytes | SHA-256 |
|---|---|---|---|
| `GSE299627_RAW.tar` | https://ftp.ncbi.nlm.nih.gov/geo/series/GSE299nnn/GSE299627/suppl/GSE299627_RAW.tar | 27361280 | 42784c15527ca3e43a465f2e22744be7bc8040faa60816c5b86d963e2394eb07 |
| `hgnc_complete_set.txt` | https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt | 17037207 | 46b83736ec351f15e22331575dce2f08416c5233765b26a08c65e6b42e56b651 |

Both retrieved 2025-11-25 (UTC) with credential-free URLs. No series matrix file exists for
GSE299627, so the six per-sample supplementary count files inside the archive are the only
gene-level source. No read alignment was performed.

## Sample inclusion and group assignment

All six samples of GSE299627 were included; none were excluded. Groups were assigned from the
GEO per-sample characteristics (`genotype`, `cell line`), not from the data:

- healthy: GSM9042255 (WT1), GSM9042256 (WT2), GSM9042257 (WT3); cell line AB1190, genotype wildtype
- DMD: GSM9042258 (DMD1), GSM9042259 (DMD2), GSM9042260 (DMD3); cell line AB1071, genotype DMD

All samples: Homo sapiens, skeletal muscle (paravertebral), skeletal myoblasts, untreated,
platform GPL34284 (Illumina NovaSeq X Plus), BioProject PRJNA1275763. Per-sample rows are in
`samples.csv`. Exactly one comparison was run: DMD versus healthy.

## Source normalization state and matrix assembly

Each supplementary file is a featureCounts table with columns
`Geneid, Chr, Start, End, Strand, Length, <sample>`. The final column holds **raw, unnormalized
integer counts**; no transform was applied upstream. Each file has 57,500 rows and the `Geneid`
order is identical across all six files (verified in code). The seventh column of each file was
taken as that sample's count vector, giving a 57,500 x 6 raw count matrix (`count_matrix.csv`).

Per-sample library sizes (sum of raw counts):

| Sample | Library size |
|---|---|
| GSM9042255 (WT1) | 56,867,332 |
| GSM9042256 (WT2) | 65,129,734 |
| GSM9042257 (WT3) | 37,149,584 |
| GSM9042258 (DMD1) | 46,859,442 |
| GSM9042259 (DMD2) | 42,971,971 |
| GSM9042260 (DMD3) | 46,407,012 |

## Identifier type and mapping

The count files use **Ensembl gene IDs without version suffixes** (for example `ENSG00000223972`).
They were mapped to HGNC symbols with the HGNC complete set (`hgnc_complete_set.txt`): records with
`status == "Approved"` and a non-missing `ensembl_gene_id` were kept, giving 42,808 Ensembl-to-symbol
pairs. Where one Ensembl gene ID appeared in more than one HGNC record, the record with the
lexicographically smallest `hgnc_id` was kept (deterministic tie-break).

- 40,950 of 57,500 Ensembl IDs mapped to an approved HGNC symbol.
- 16,550 Ensembl IDs had no approved symbol. These were **kept** in the matrix under their Ensembl
  ID so that genome-wide counts are complete.
- Counts for Ensembl IDs sharing one symbol are summed. In this dataset **0 symbols received counts
  from more than one Ensembl ID**, so the aggregation step changed no value here; the rule is stated
  because it is part of the pipeline.
- Features after aggregation: 57,500.

## Filtering

Stated rule, applied once, before any statistical modelling: keep a feature if its **raw count is
at least 10 in at least 3 of the 6 samples** (3 = the smaller group size).

- Features before filtering: 57,500
- Features after filtering: 17,977 (`count_matrix_filtered.csv`)

Target genes removed by this filter are reported in `target_gene_results.csv` with
`status = "present in matrix but removed by the low-expression filter"` and their raw group means,
not omitted.

## Normalization, model and testing

- Tool: **PyDESeq2 0.6.0** (the DESeq2 method implemented in Python). Exact versions of every
  imported package are in `environment.txt`.
- Normalization: **DESeq2 median-of-ratios size factors**. Fitted size factors:
  GSM9042255 1.163205, GSM9042256 1.400245, GSM9042257 0.781115,
  GSM9042258 0.978818, GSM9042259 0.900637, GSM9042260 0.922338.
- Model: negative-binomial GLM, design `~group`, reference level `healthy`,
  contrast `group: DMD vs healthy`. Gene-wise dispersion with the parametric trend fit and empirical
  Bayes shrinkage, Cook's-distance refitting enabled.
- Test: **Wald test** on the `group_DMD_vs_healthy` coefficient. No t-test on raw counts was used
  anywhere.
- Multiple testing: **Benjamini-Hochberg** across all 17,977 tested genes.
  DESeq2 independent filtering was **disabled** (`independent_filter=False`) so that every tested
  gene, including low-expressed target genes, receives a non-missing q-value. Cook's-distance
  outlier filtering was left on.
- Significance threshold: BH q < 0.05.

## Effect-size conventions

- `log2_fold_change`: DESeq2 Wald coefficient, **DMD relative to healthy**. Negative means lower in
  DMD. This is the primary effect size and the one compared with the published values.
- `log2_mean_difference`: `log2(mean normalized DMD + 1) - log2(mean normalized healthy + 1)`.
- `fold_change`: `(mean normalized DMD + 1) / (mean normalized healthy + 1)`, ordinary (linear) scale.
- `cohens_d`: computed on `log2(normalized count + 1)` with the pooled standard deviation,
  `(mean_DMD - mean_healthy) / s_pooled`, n1 = n2 = 3. With three replicates of a single cell line
  per group the within-group variance is a technical/passage variance, so these d values are large
  and should not be read as between-donor effect sizes.
- Group means reported in the tables are means of DESeq2-normalized counts.

## Determinism

`analysis.py` uses no random number generation and writes no timestamps into its outputs. It
accepts `--output-dir` and `--cache-dir`; with a populated cache it re-reads the identical input
bytes instead of downloading. The replay under `replay/` regenerated byte-identical
`samples.csv`, `count_matrix.csv`, `count_matrix_filtered.csv`, `normalized_counts.csv`,
`gene_results.csv`, `target_gene_results.csv` and `replication_check.csv`.

## Limitation of the design (mandatory)

Each group is a single immortalized cell line (healthy AB1190, DMD AB1071), so the three samples
per group are replicates of one donor background rather than independent donors. Every
differential-expression result from this design is confounded with cell-line identity, and the
analysis cannot attribute any difference to dystrophin deficiency as opposed to donor genotype,
immortalization history, or passage. This is a property of the design, not a caveat attached to
individual genes. The comparison is not n = 6 independent samples.

## Scope limit (mandatory)

Transcript abundance is not pump activity and not calcium flux. Nothing in this dataset can show
that sarcoplasmic reticulum calcium clearance is impaired, that SERCA function is reduced, or that
the clearance-based model is correct. The permitted conclusions concern transcript levels of the
named genes in these two cell lines. Any statement about calcium handling is an inference that this
dataset cannot test.
