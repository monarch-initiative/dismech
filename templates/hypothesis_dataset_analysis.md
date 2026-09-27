---
analysis_contract: required
---

# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: {disease_name}
- Hypothesis ID: {hypothesis_group_id}
- Hypothesis label: {hypothesis_label}
- Dataset inputs:

{dataset_inputs}

- Target variables or genes:

{target_variables}

## Analysis objective

{analysis_objective}

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`{artifact_dir}`

This path is relative to your working directory. Use it as given: do not turn it
into an absolute path or write the bundle anywhere else, because only files
inside your job workspace are returned with the job.

First create the directory and preflight all required imports and remote input
URLs. Record canonical credential-free URLs, never tokens or signed query
parameters. If an import, download, parse, sample-classification,
identifier-mapping, or analysis step fails, write `MANIFEST.yaml` with
`status: FAILED`, the failed step, and a diagnostically useful error with
credentials, patient identifiers, and other sensitive values redacted. Then
stop. Do not answer from memory, switch to literature synthesis, invent
results, or present proposed code as executed.

If the run succeeds, the artifact directory must contain:

- `MANIFEST.yaml`, in exactly the shape shown under "Manifest schema" below.
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
`{artifact_dir}/raw/`; they are local/recoverable inputs and will not be
committed.

## Manifest schema

The runner checks `MANIFEST.yaml` mechanically, so field names matter: a field
spelled differently from this schema counts as missing. Use these names exactly.
Store every `sha256` as exactly 64 lowercase hexadecimal characters, with no
`sha256:` prefix (the field name supplies the algorithm), and every
`byte_count` as a positive integer.

Top level, all required:

- `schema_version: '1.0'`
- `provider`: your provider name, for example `openscientist`
- `status: SUCCEEDED`
- `fallback_used: false`
- `direct_analysis_completed: true`
- `inputs`: a non-empty list, one entry per file you actually downloaded
- `outputs`: a non-empty list, one entry per file you produced
- `replay`: the replay record described in the next section

Also record `started_at` and `finished_at` (UTC), the exact `comparison`, and
`limitations`.

Each `inputs` entry, all required:

- `identifier`: the accession or other stable identifier, for example
  `geo:GSE5281`
- `canonical_url`: the credential-free URL you retrieved it from (`uri` is
  accepted instead)
- `retrieved_at`: UTC retrieval time (`retrieval_time_utc` is accepted instead)
- `local_path`: its path relative to the artifact directory, beneath `raw/`
- `sha256` and `byte_count` of the downloaded file

Each `outputs` entry, all required:

- `path`: relative to the artifact directory, not beneath `raw/`, `local/`,
  `controlled/`, or `replay/`
- `role`: the bundle must include distinct `CODE`, `ENVIRONMENT`, and
  `TABULAR_RESULT` roles. Other useful roles include `METHODS`, `SUMMARY`,
  `FIGURE`, `INPUT_MANIFEST`, and `PREFLIGHT`.
- `sha256` and `byte_count`

**A source you did not download does not go in `inputs`.** Every `inputs` entry
must carry the checksum and size of a retrieved file, so an entry with a null
`sha256` or `byte_count` fails the check. A source that belongs to the lineage
but was not retrieved (a controlled-access cohort you were told not to access, a
dataset that could not be reached, a source you only cite) goes in a separate
top-level `unretrieved_sources` list. Each entry needs an `identifier` and a
`reason`, and may add a `canonical_url`. Give it no `sha256`, `byte_count`, or
`local_path`.

Worked example (checksums shortened here for readability; write all 64
characters):

```yaml
schema_version: '1.0'
provider: openscientist
status: SUCCEEDED
fallback_used: false
direct_analysis_completed: true
started_at: '2026-09-26T10:02:11Z'
finished_at: '2026-09-26T10:41:57Z'
comparison: AD versus control, prefrontal cortex astrocytes
limitations: Pseudobulk over donors; no covariate adjustment beyond sex.
inputs:
- identifier: geo:GSE5281
  canonical_url: https://ftp.ncbi.nlm.nih.gov/geo/series/GSE5nnn/GSE5281/matrix/GSE5281_series_matrix.txt.gz
  retrieved_at: '2026-09-26T10:03:40Z'
  local_path: raw/GSE5281_series_matrix.txt.gz
  sha256: 3f1c...e9a0
  byte_count: 48213377
unretrieved_sources:
- identifier: synapse:syn60084804
  canonical_url: https://www.synapse.org/Synapse:syn60084804
  reason: Controlled-access PsychAD cohort; not accessed, as instructed.
outputs:
- path: analysis.py
  role: CODE
  sha256: 9b0d...41c2
  byte_count: 8123
- path: environment.txt
  role: ENVIRONMENT
  sha256: 11aa...07fe
  byte_count: 412
- path: samples.csv
  role: TABULAR_RESULT
  sha256: 5e6f...d310
  byte_count: 20417
- path: gene_results.csv
  role: TABULAR_RESULT
  sha256: c7d8...a992
  byte_count: 3310
replay:
  command: python analysis.py --output-dir replay --cache-dir raw
  verified: true
  byte_identity:
    samples.csv: true
    gene_results.csv: true
  assets:
  - path: replay/samples.csv
    role: TABULAR_RESULT
    sha256: 5e6f...d310
    byte_count: 20417
  - path: replay/gene_results.csv
    role: TABULAR_RESULT
    sha256: c7d8...a992
    byte_count: 3310
```

## Replay

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `{artifact_dir}/raw` as `--cache-dir`; do not copy or
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
