# Citations for Research Query

**Query:** 
# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: Alzheimer Disease
- Hypothesis ID: glial_depression_in_ad_model
- Hypothesis label: Glial Inflammatory and ER-Stress Model of Depression in Alzheimer Disease
- Dataset inputs:

https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/41591_2025_4128_MOESM3_ESM.zip

- Target variables or genes:

Astro and Oligo depression PAC scores; HSPA5, DDIT3, ATF4, XBP1, MANF, NFKBIA, CHI3L1, SERPINA3

## Analysis objective

Input is the open Supplementary Data zip of He et al. 2026 Nat Med (PMID:42778763, doi:10.1038/s41591-025-04128-1), derived from the controlled PsychAD snRNA-seq cohort (synapse:syn60084804, 1,494 donors, DLPFC); do NOT attempt to access Synapse or any controlled data. The workbooks are .xlsx, so additionally preflight and record openpyxl (the only package added to the approved list). Record the zip sha256 and every sheet read. Supplementary Data 6 matrices are donor x 27-subclass average phenotype-associated-cell (PAC) scores keyed by donor ID only: they carry NO diagnosis, Braak, or resilience labels, and you must not infer or invent donor labels; restrict to tests that need none (within-donor paired contrasts across cell subclasses, cross-phenotype correlation of donors present in two sheets joined on donor ID, and gene-set overlap tests against the published DEG tables with an explicit gene universe). Treat every result as a re-analysis of published derived scores, not independent replication: it shares data lineage with the paper. Report effect sizes with BH correction, and state plainly where a result could only restate what the paper already computed. Objective: test whether the depression-within-Alzheimer glial signal is distinct from the general Alzheimer signal. (1) For donors present in both 'Avg. PAC scores DepressionMood' and 'Avg. PAC scores AD progression' (Supp Data 6), correlate each subclass's depression PAC score with its AD-progression PAC score (Spearman, BH); a distinct signal predicts weak correlation for Astro and Oligo. Also rank subclasses by mean absolute 'SHAP values DepressionMood'. (2) In Supp Data 3 (depression-PAC astrocyte DEGs and the AD-Depression Astro_WIF1 cluster genes) test enrichment of prespecified sets: unfolded protein response / ER stress (HSPA5, DDIT3, ATF4, ATF6, XBP1, ERN1, EIF2AK3, HSP90B1, PDIA4, PDIA6, CALR, DNAJB9, SEL1L, HERPUD1, MANF) and inflammatory signalling (NFKBIA, IL1B, IL6, CXCL8, TNF, STAT3, SOCS3, C3, CHI3L1, SERPINA3, CD44). (3) Compare depression astrocyte DEGs with Supp Data 7 'AD PAC DEGs' astrocyte rows: report overlap and a Jaccard index, and whether ER-stress genes are specific to the depression set. Use Supp Data 4 module GO enrichment only descriptively.

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts`

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
`kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts/raw/`; they are local/recoverable inputs and will not be
committed.

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts/raw` as `--cache-dir`; do not copy or
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
**Generated:** 2026-09-26T03:03:53.809776

1. PMID:42778763
2. PMID:31727394
3. PMID:42537476
4. PMID:42425961