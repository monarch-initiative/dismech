# Citations for Research Query

**Query:** 
# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: Duchenne Muscular Dystrophy
- Hypothesis ID: calcium_clearance_failure_model
- Hypothesis label: Impaired Calcium Clearance and ECM-Calcium Coupling Model
- Dataset inputs:

geo:GSE299627 (human skeletal myoblast RNA-seq; Illumina NovaSeq X Plus, platform GPL34284; open access; BioProject PRJNA1275763; 6 samples GSM9042255-GSM9042260). There is NO series matrix file for this series. Gene-level counts are supplied only as six per-sample files inside the archive https://ftp.ncbi.nlm.nih.gov/geo/series/GSE299nnn/GSE299627/suppl/GSE299627_RAW.tar (27.4 MB), named GSM9042255_WT1.counts.txt.gz, GSM9042256_WT2.counts.txt.gz, GSM9042257_WT3.counts.txt.gz, GSM9042258_DMD1.counts.txt.gz, GSM9042259_DMD2.counts.txt.gz, GSM9042260_DMD3.counts.txt.gz. Per-sample GEO characteristics are: tissue (skeletal muscle, paravertebral), cell line (AB1190 for the three healthy samples, AB1071 for the three DMD samples), cell type (skeletal myoblasts), genotype (wildtype or DMD), treatment (untreated). Series overall design: "RNA Seq profiling of undifferentiated healthy and dystrophic human myoblasts". Do not attempt to align raw reads; use the supplied count files.

- Target variables or genes:

FBN1, FBN2, FBN3 (fibrillin genes; FBN1 and FBN2 are the reported finding); LTBP1, LTBP2, LTBP3, LTBP4 (fibrillin-binding ECM partners; LTBP4 is an established DMD modifier locus); ZNF277 (proposed conserved transcriptional regulator); ATP2A1, ATP2A2, ATP2A3 (SERCA paralogs); SLN, PLN, CASQ1, CASQ2 (sarcoplasmic reticulum calcium handling and SERCA regulators); CALM1, CALM2, CALM3 (calmodulin); RYR1, ITPR1 (sarcoplasmic reticulum calcium release); ORAI1, STIM1, TRPC1, TRPC3, TRPC6, PIEZO1 (sarcolemmal calcium entry routes, i.e. the competing entry-based model); DMD (positive control for the dystrophic genotype)

## Analysis objective

Prespecified differential-expression analysis of GSE299627, testing whether fibrillin-related ECM genes and sarcoplasmic-reticulum calcium-handling genes are coordinately downregulated in dystrophic human myoblasts, and whether the sarcolemmal calcium-entry genes of the competing model move in the same comparison.

RETRIEVAL AND MATRIX. Download GSE299627_RAW.tar, extract the six per-sample count files, and build one gene-by-sample count matrix. State explicitly which gene identifier type the count files use (Ensembl gene ID, Entrez ID, or symbol) and how you mapped it to HGNC symbols; when several identifiers map to one symbol, sum their counts and say so. Report the number of genes before and after filtering, and the per-sample library size.

GROUPS. Healthy = GSM9042255, GSM9042256, GSM9042257 (cell line AB1190, genotype wildtype). DMD = GSM9042258, GSM9042259, GSM9042260 (cell line AB1071, genotype DMD). One comparison only: DMD versus healthy.

METHOD. Filter low-expressed genes by a stated rule. Normalize and test with a named, versioned tool (DESeq2 or edgeR; record the exact version). Report the normalization method. Do not use an uncorrected t-test on raw counts.

REQUIRED REPORTING. For every gene in the target list, report, whether or not it reaches significance: normalized mean per group, log2 fold change (DMD relative to healthy), unadjusted p, and Benjamini-Hochberg adjusted p. A target gene absent from the matrix must be reported as absent, not omitted. Also report the genome-wide count of genes at BH-adjusted p < 0.05 in each direction.

POSITIVE CONTROL. Report DMD itself. The dystrophic line is expected to show reduced dystrophin expression; if it does not, say so prominently, because that would call the group labels into question.

REPLICATION CHECK. The source publication reports FBN1 log2 fold change -1.2 and FBN2 log2 fold change -0.9, both at p < 0.0001, from this dataset. Report your own values beside those and state plainly whether they agree. If they differ in magnitude, sign, or significance, report the discrepancy; do not adjust your pipeline to reproduce the published numbers and do not reconcile the difference by argument.

MANDATORY LIMITATION, to appear in the report body and in the manifest. Each group is a single immortalized cell line, so the three samples per group are replicates of one donor background rather than independent donors. Every differential-expression result from this design is therefore confounded with cell-line identity, and the analysis cannot attribute any difference to dystrophin deficiency as opposed to donor genotype, immortalization history, or passage. State this as a limitation of the design, not as a caveat on individual genes, and do not report the comparison as n=6 independent samples.

MANDATORY SCOPE LIMIT. Transcript abundance is not pump activity and not calcium flux. Do not conclude from this dataset that sarcoplasmic reticulum calcium clearance is impaired, that SERCA function is reduced, or that the clearance-based model is confirmed. The permitted conclusions concern transcript levels of the named genes in these two cell lines. Any statement about calcium handling must be labelled as an inference that this dataset cannot test.

ARTIFACTS. Save, under the artifact directory: the analysis code exactly as executed, an environment specification with tool versions, the assembled count matrix, the full genome-wide differential-expression table, a target-gene table, and a checksummed manifest of inputs and outputs sufficient for a clean replay.

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`kb/hypotheses/Duchenne_Muscular_Dystrophy/calcium_clearance_failure_model/openscientist_artifacts`

First create the directory and preflight all required imports and remote input
URLs. Record canonical credential-free URLs, never tokens or signed query
parameters. If an import, download, parse, sample-classification,
identifier-mapping, or analysis step fails, write `MANIFEST.yaml` with
`status: FAILED`, the failed step, and a diagnostically useful error with
credentials, patient identifiers, and other sensitive values redacted. Then
stop. Do not answer from memory, switch to literature synthesis, invent
results, or present proposed code as executed.

If the run succeeds, the artifact directory must contain:

- `MANIFEST.yaml`: `schema_version: '1.0'`, `status: SUCCEEDED`,
  `fallback_used: false`, `direct_analysis_completed: true`, UTC start/end
  times, every input
  accession and retrieval URL/date/checksum/byte count, all output paths and
  checksums, the exact comparison, and limitations. Store each manifest
  `sha256` as exactly 64 lowercase hexadecimal characters (the field name
  supplies the algorithm). Give every output a `role`; the bundle must include
  distinct `CODE`, `ENVIRONMENT`, and `TABULAR_RESULT` roles. Other useful roles
  include `METHODS`, `SUMMARY`, `FIGURE`, `INPUT_MANIFEST`, and `PREFLIGHT`.
- `analysis.py`: standalone deterministic analysis accepting `--output-dir`
  and optionally `--cache-dir`; it must retrieve or reuse exact inputs and
  regenerate all tabular outputs without an LLM.
- `environment.txt`: Python version, operating system, and exact versions of
  every imported third-party package.
- `methods.md`: sample inclusion/exclusion rules, source normalization state,
  transform decisions, identifier/probe mapping and aggregation rules,
  statistical tests, multiple-testing method, effect-size convention, and all
  material parameters.
- `samples.csv`: one row per included or excluded sample, with accession,
  dataset, organism, tissue, source metadata, assigned group, and exclusion
  reason.
- `gene_results.csv`: tidy results with one row per dataset/gene/comparison and
  group sizes, group means, log2 mean difference, ordinary fold change, test
  statistic, raw p-value, BH-adjusted q-value, and Cohen's d.
- `comparison.md`: a compact interpretation of the computed results, clearly
  separating observed results from biological inference.

Small diagnostic tables or figures may also be saved. Raw downloads must go in
`kb/hypotheses/Duchenne_Muscular_Dystrophy/calcium_clearance_failure_model/openscientist_artifacts/raw/`; they are local/recoverable inputs and will not be
committed.

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `kb/hypotheses/Duchenne_Muscular_Dystrophy/calcium_clearance_failure_model/openscientist_artifacts/raw` as `--cache-dir`; do not copy or
download raw inputs beneath the replay directory. Verify that the replayed
`samples.csv` and `gene_results.csv` are byte-identical to the primary outputs.
Under `replay`, record the exact nonempty replay `command`, `verified: true`, a
`byte_identity` mapping naming every `TABULAR_RESULT` primary path with value
`true`, and an `assets` list. Every replay asset entry must use its path beneath
`replay/`, a role, positive `byte_count`, and exact lowercase SHA-256. Include a
replay asset corresponding to every primary `TABULAR_RESULT`. Record checksum
and byte-count entries for every input, primary output, and replay asset in the
manifest.

Do not expose another provider's numerical results, derived tables, code, or
interpretation to this analysis before its primary outputs and checksums are
locked. Perform cross-provider comparison only afterward, as a separate,
lineage-marked step. Shared input accessions do not by themselves make analyses
dependent, but prior-provider results must not influence method, sample, feature,
probe, model, threshold, or parameter choices.

## Final response contract

Finish and close `MANIFEST.yaml` before emitting a success marker. After the
deep-research client captures your response, the hypothesis runner hashes the
exact manifest bytes and adds
`artifact_manifest_sha256: sha256:<64 lowercase hex>` to the report's YAML
frontmatter before invoking the gate. Do not invent this frontmatter field in
the response or modify the manifest after declaring success.

The first line must be exactly one of:

`ANALYSIS_STATUS: SUCCEEDED`

`ANALYSIS_STATUS: FAILED`

Use `SUCCEEDED` only after all required artifacts exist and the clean replay
matches. Summarize the actual comparison and point to the saved artifacts. On
failure, name the failed step and error only; do not provide a fallback
scientific verdict.

**Provider:** openscientist
**Generated:** 2026-11-25T06:29:29.663996

1. PMID:40661626
2. PMID:40979067