# Citations for Research Query

**Query:** 
# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: Systemic Lupus Erythematosus
- Hypothesis ID: nucleic_acid_immune_complex_interferon_tissue_injury_model
- Hypothesis label: Nucleic-Acid Immune Complex, Interferon, and Tissue-Injury Model
- Dataset inputs:

geo:GSE65391 (whole-blood Illumina HumanHT-12 v4 arrays, GPL10558; open access; series matrix https://ftp.ncbi.nlm.nih.gov/geo/series/GSE65nnn/GSE65391/matrix/GSE65391_series_matrix.txt.gz; per-sample characteristics include disease state, subject, visit, set, sledai, nephritis_class, ds_dna, c3, c4, neutrophil_count)

- Target variables or genes:

IFI27, IFI44L, IFIT1, ISG15, RSAD2, SIGLEC1 (interferon signature); JCHAIN/IGJ, MZB1, TNFRSF17 (plasmablast signature); IFN6_SCORE composite

## Analysis objective

Prespecified analysis of the pediatric SLE whole-blood microarray cohort GSE65391 (Illumina GPL10558; series matrix), testing whether blood type I interferon signature tracks disease activity and nephritis or only disease presence. Sample rules: exclude samples whose characteristic 'set' is Technical_Replicate (keep one array per subject-visit); for all cross-sectional contrasts use each subject's first included visit only, so each subject contributes one sample. Map probes to gene symbols using the GPL10558 annotation; when several probes map to one gene, use the probe with the highest mean expression across included samples. Contrasts, each reported for every target gene and for the composite interferon score whether or not significant: (1) SLE versus Healthy (disease state), first visit; (2) within SLE, SLEDAI >= 6 versus SLEDAI < 6 at first visit; (3) within SLE, biopsy-proven nephritis (nephritis_class any recorded class) versus no nephritis (nephritis_class not recorded / Not Applicable) at first visit. Composite interferon score = mean of per-gene z-scores (z computed against the Healthy first-visit samples) of IFI27, IFI44L, IFIT1, ISG15, RSAD2, SIGLEC1; add it as a row in gene_results.csv with gene 'IFN6_SCORE'. Use Welch t-tests, BH across all rows within each contrast, Cohen's d. Additionally write correlations.csv: Spearman correlation, within SLE first-visit samples, of IFN6_SCORE and of the plasmablast genes JCHAIN (or IGJ), MZB1, TNFRSF17 against numeric sledai, ds_dna, c3, c4, and neutrophil_count, with n per pair and BH q-values. Treat non-numeric or 'Not Applicable' values as missing. Record in methods.md how many SLE subjects fall in each group and any metadata ambiguities (e.g. how nephritis class strings were parsed).

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`kb/hypotheses/Systemic_Lupus_Erythematosus/nucleic_acid_immune_complex_interferon_tissue_injury_model/openscientist_artifacts`

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
`kb/hypotheses/Systemic_Lupus_Erythematosus/nucleic_acid_immune_complex_interferon_tissue_injury_model/openscientist_artifacts/raw/`; they are local/recoverable inputs and will not be
committed.

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `kb/hypotheses/Systemic_Lupus_Erythematosus/nucleic_acid_immune_complex_interferon_tissue_injury_model/openscientist_artifacts/raw` as `--cache-dir`; do not copy or
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
**Generated:** 2026-09-26T01:57:37.087528

1. PMID:31167757
2. PMID:31209404
3. PMID:37099456