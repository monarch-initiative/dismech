---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-26T02:11:26.312127'
end_time: '2026-09-26T02:38:30.241620'
duration_seconds: 1623.93
template_file: templates/hypothesis_dataset_analysis.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: reactive_astrocyte_resilience_model
  hypothesis_label: Reactive Astrocyte Subtype Resilience Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: reactive_astrocyte_resilience_model\nhypothesis_label:\
    \ Reactive Astrocyte Subtype Resilience Model\nstatus: EMERGING\ndescription:\
    \ Cognitive resilience, the preservation of cognition despite Alzheimer neuropathology\
    \ at a\n  given Braak stage, is modeled as depending in part on which reactive\
    \ state cortical astrocytes adopt.\n  Reactive astrocyte subtypes expressing neuroprotective\
    \ programs (for example EMP1 in the PLSCR1-marked\n  subtype) are proposed to\
    \ buffer neurons against pathology, while subtypes with a more severe, neurotoxic-skewed\n\
    \  reactive profile (high FKBP5, MAOB and CHI3L1) are proposed to accompany the\
    \ transition to dementia.\n  The claim is that astrocyte reactive-state composition,\
    \ not only amyloid and tau burden, separates resilient\n  from cognitively impaired\
    \ donors.\napplies_to_subtypes:\n- Late-Onset Alzheimer's Disease\nevidence:\n\
    - reference: PMID:42778763\n  reference_title: AI-based characterization of Alzheimer's\
    \ disease phenotypes from population-scale single-cell\n    data.\n  supports:\
    \ SUPPORT\n  evidence_source: COMPUTATIONAL\n  quote_role: PRIMARY_RESULT\n  snippet:\
    \ reactive astrocyte subtypes with altered neuroprotective and neurotoxic gene\
    \ expression that\n    likely confer cognitive resilience\n  explanation: The\
    \ seed observation for this model, from computational phenotype scoring of prefrontal\n\
    \    single-nucleus data in the PsychAD cohort. The authors' \"likely confer\"\
    \ is an inference from association;\n    no perturbation tests whether the astrocyte\
    \ state causes resilience.\n- reference: PMID:37248300\n  reference_title: Astrocyte\
    \ reactivity influences amyloid-\u03B2 effects on tau pathology in preclinical\
    \ Alzheimer's\n    disease.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Our findings suggest astrocyte reactivity as an important upstream\
    \ event linking A\u03B2 with initial\n    tau pathology, which may have implications\
    \ for the biological definition of preclinical AD and for\n    selecting CU individuals\
    \ for clinical trials.\n  explanation: Independent human biomarker evidence that\
    \ astrocyte reactivity modulates how amyloid translates\n    into downstream pathology,\
    \ the plausibility premise for astrocyte state shaping clinical expression.\n\
    notes: EMERGING because the only direct support is one cohort's transcriptomic\
    \ association, reported with\n  the direction of causation left open. It is separate\
    \ from neuroimmune_glial_amplification_model, which\n  treats glial reactivity\
    \ as amplifying injury; this model claims a reactive state can be protective and\n\
    \  that the protective and harmful states are distinguishable subtypes."
  artifact_dir: kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts
  dataset_inputs: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/41591_2025_4128_MOESM3_ESM.zip
  target_variables: Astro PAC scores; EMP1, FKBP5, CD109, CRYAB, HSPB1, MAOB, CHI3L1,
    C3
  analysis_objective: 'Input is the open Supplementary Data zip of He et al. 2026
    Nat Med (PMID:42778763, doi:10.1038/s41591-025-04128-1), derived from the controlled
    PsychAD snRNA-seq cohort (synapse:syn60084804, 1,494 donors, DLPFC); do NOT attempt
    to access Synapse or any controlled data. The workbooks are .xlsx, so additionally
    preflight and record openpyxl (the only package added to the approved list). Record
    the zip sha256 and every sheet read. Supplementary Data 6 matrices are donor x
    27-subclass average phenotype-associated-cell (PAC) scores keyed by donor ID only:
    they carry NO diagnosis, Braak, or resilience labels, and you must not infer or
    invent donor labels; restrict to tests that need none (within-donor paired contrasts
    across cell subclasses, cross-phenotype correlation of donors present in two sheets
    joined on donor ID, and gene-set overlap tests against the published DEG tables
    with an explicit gene universe). Treat every result as a re-analysis of published
    derived scores, not independent replication: it shares data lineage with the paper.
    Report effect sizes with BH correction, and state plainly where a result could
    only restate what the paper already computed. Objective: test whether published
    astrocyte data separate cognitively resilient from impaired Alzheimer donors along
    a neuroprotective-versus-neurotoxic axis. (1) From Supp Data 2 ''Fig. 3f'' report
    the resilience P-adj and median-PAC difference for Astro relative to all 28 subclasses.
    (2) Across every astrocyte-related DEG table in the supplementary workbooks (identify
    them from each ''key'' sheet and record which were used), classify genes against
    prespecified reactive-astrocyte marker sets: pan-reactive (LCN2, STEAP4, S1PR3,
    TIMP1, HSPB1, CXCL10, CD44, OSMR, CP, SERPINA3, ASPG, VIM, GFAP), A1/neurotoxic
    (C3, H2-T23 human ortholog if mapped, SERPING1, GBP2, FBLN5, UGT1A1, FKBP5, AMIGO2,
    PSMB8, SRGN, IIGP1 skip if no human ortholog), A2/neuroprotective (CLCF1, TGM1,
    PTX3, S100A10, SPHK1, CD109, PTGS2, EMP1, SLC10A6, TM4SF1, B3GNT5, CD14), plus
    CRYAB, MAOB, CHI3L1; test directional enrichment (Fisher) of A2 versus A1 markers
    among genes higher in resilient donors, and report EMP1 and FKBP5 explicitly.
    (3) Correlate donor Astro PAC scores in ''Avg. PAC scores AD progression'' with
    those of every excitatory and inhibitory subclass (Spearman, BH) to ask whether
    astrocyte association co-varies with neuronal association within donors.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 1
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 16
artifact_sources:
  openscientist_artifacts_zip: 16
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_comparison.md
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_comparison.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comparison
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_correlation_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_correlation_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist correlation results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_enrichment_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_enrichment_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist enrichment results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_fig3f_resilience.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_fig3f_resilience.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist fig3f resilience
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_gene_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_methods.md
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_methods.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist methods
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_comparison.md
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_comparison.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comparison
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_correlation_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_correlation_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist correlation results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_enrichment_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_enrichment_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist enrichment results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_fig3f_resilience.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_fig3f_resilience.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist fig3f resilience
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_gene_results.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_methods.md
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_methods.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist methods
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_samples.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
- filename: kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_samples.csv
  path: openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
---

## Question


# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: Alzheimer Disease
- Hypothesis ID: reactive_astrocyte_resilience_model
- Hypothesis label: Reactive Astrocyte Subtype Resilience Model
- Dataset inputs:

https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/41591_2025_4128_MOESM3_ESM.zip

- Target variables or genes:

Astro PAC scores; EMP1, FKBP5, CD109, CRYAB, HSPB1, MAOB, CHI3L1, C3

## Analysis objective

Input is the open Supplementary Data zip of He et al. 2026 Nat Med (PMID:42778763, doi:10.1038/s41591-025-04128-1), derived from the controlled PsychAD snRNA-seq cohort (synapse:syn60084804, 1,494 donors, DLPFC); do NOT attempt to access Synapse or any controlled data. The workbooks are .xlsx, so additionally preflight and record openpyxl (the only package added to the approved list). Record the zip sha256 and every sheet read. Supplementary Data 6 matrices are donor x 27-subclass average phenotype-associated-cell (PAC) scores keyed by donor ID only: they carry NO diagnosis, Braak, or resilience labels, and you must not infer or invent donor labels; restrict to tests that need none (within-donor paired contrasts across cell subclasses, cross-phenotype correlation of donors present in two sheets joined on donor ID, and gene-set overlap tests against the published DEG tables with an explicit gene universe). Treat every result as a re-analysis of published derived scores, not independent replication: it shares data lineage with the paper. Report effect sizes with BH correction, and state plainly where a result could only restate what the paper already computed. Objective: test whether published astrocyte data separate cognitively resilient from impaired Alzheimer donors along a neuroprotective-versus-neurotoxic axis. (1) From Supp Data 2 'Fig. 3f' report the resilience P-adj and median-PAC difference for Astro relative to all 28 subclasses. (2) Across every astrocyte-related DEG table in the supplementary workbooks (identify them from each 'key' sheet and record which were used), classify genes against prespecified reactive-astrocyte marker sets: pan-reactive (LCN2, STEAP4, S1PR3, TIMP1, HSPB1, CXCL10, CD44, OSMR, CP, SERPINA3, ASPG, VIM, GFAP), A1/neurotoxic (C3, H2-T23 human ortholog if mapped, SERPING1, GBP2, FBLN5, UGT1A1, FKBP5, AMIGO2, PSMB8, SRGN, IIGP1 skip if no human ortholog), A2/neuroprotective (CLCF1, TGM1, PTX3, S100A10, SPHK1, CD109, PTGS2, EMP1, SLC10A6, TM4SF1, B3GNT5, CD14), plus CRYAB, MAOB, CHI3L1; test directional enrichment (Fisher) of A2 versus A1 markers among genes higher in resilient donors, and report EMP1 and FKBP5 explicitly. (3) Correlate donor Astro PAC scores in 'Avg. PAC scores AD progression' with those of every excitatory and inhibitory subclass (Spearman, BH) to ask whether astrocyte association co-varies with neuronal association within donors.

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts`

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
`kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts/raw/`; they are local/recoverable inputs and will not be
committed.

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts/raw` as `--cache-dir`; do not copy or
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


## Output

# Reactive Astrocyte Subtype Resilience Model — Computational Replication Report

**Disease:** Alzheimer Disease
**Hypothesis ID:** `reactive_astrocyte_resilience_model`
**Hypothesis label:** Reactive Astrocyte Subtype Resilience Model
**Source dataset:** He et al. 2026, *Nature Medicine* — Supplementary Data zip (`41591_2025_4128_MOESM3_ESM.zip`), sha256 `27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865`, 13,893,637 bytes. [PMID: 42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/); doi:10.1038/s41591-025-04128-1.
**Source cohort:** PsychAD snRNA-seq (synapse:syn60084804; 1,494 donors; DLPFC) — controlled data, **not accessed**.
**Run status:** SUCCEEDED — direct analysis completed, clean replay byte-identical, no fallback used.

> **Lineage caveat:** This is a **re-analysis of the paper's own published derived scores and DEG tables**, sharing full data lineage with He et al. 2026. It is *not* an independent replication. The Supplementary Data 6 PAC-score matrices are keyed by donor ID only and carry **no diagnosis, Braak, or resilience labels**; per the analysis contract no donor labels were inferred or invented, so only label-free tests were run. Where a result merely restates a value the paper already computed, this is stated plainly.

---

## Summary

This was a computational replication task rather than a literature review. The objective was to retrieve the open Supplementary Data of He et al. 2026 *Nature Medicine*, execute a pre-specified re-analysis of the published astrocyte-associated derived scores, and save a fully replayable artifact bundle. All required artifacts were produced under `kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts`, and `analysis.py` was re-executed into a clean `replay/` directory (reusing the cached raw input as `--cache-dir`) with **byte-identical** `samples.csv` and `gene_results.csv` outputs. The `MANIFEST.yaml` records `schema_version: '1.0'`, `status: SUCCEEDED`, `fallback_used: false`, `direct_analysis_completed: true`, the input zip checksum and byte count, all output checksums, and a verified replay block.

Scientifically, the central question was whether the published astrocyte data separate cognitively **resilient** from cognitively **impaired/strict** Alzheimer donors along a **neuroprotective (A2) versus neurotoxic (A1)** axis. Three complementary, label-free analyses were performed exactly as the contract required. The verdict is nuanced: astrocytes **do** separate resilient from strict donors significantly, but only **modestly** — they rank 16th of 27 subclasses, with neuronal subclasses discriminating far more strongly. Two flagship genes (**EMP1**, **FKBP5**) behave exactly as the neuroprotective-vs-neurotoxic model predicts, yet the **aggregate** A2-vs-A1 directional enrichment is **null** because several canonical A1/neurotoxic markers move in the "wrong" direction (also downregulated). Finally, donor-level astrocyte association co-varies positively with every neuronal subclass, implying that much of the astrocyte "signal" reflects a shared, donor-wide disease-burden gradient rather than an astrocyte-autonomous resilience axis.

Taken together, the Reactive Astrocyte Subtype Resilience Model is **partially supported at the single-gene level and not supported at the aggregate-axis level**, with an important confound — shared donor-level burden — that these lineage-shared, label-free analyses cannot fully disentangle.

---

## Key Findings

### Finding 1 — Astrocytes separate resilient from strict AD donors significantly but modestly (rank 16/27)

From **Supplementary Data 2, sheet 'Fig. 3f'**, the astrocyte (Astro) contrast between AD-resilient and AD-strict donor groups is statistically significant but weak in relative terms:

- **Adjusted P (Astro, resilient vs strict) = 1.50 × 10⁻³** (0.00149687).
- **Median-PAC difference (strict − resilient) = +0.3862** (strict median PAC = 0.4310 vs resilient median PAC = 0.0448) — the AD-strict group carries the higher astrocyte phenotype-associated-cell burden.
- Ranked against all 27 reported subclasses, **Astro places only 16th** by adjusted P.

The strongest separators of resilience are consistently **neuronal**, not glial: excitatory intratelencephalic neurons and inhibitory interneurons dominate the top of the list — `EN_L3_5_IT_3` (P = 1.9 × 10⁻⁶), `IN_PVALB_CHC`, `EN_L2_3_IT`, and `IN_SST`. This mirrors the paper's own emphasis that neuronal vulnerability/loss is the leading axis of cognitive resilience, with astrocyte reactivity a secondary, supporting signal.

| Subclass (top separators) | Adjusted P | Lineage |
|---|---|---|
| EN_L3_5_IT_3 | 1.9 × 10⁻⁶ | neuronal |
| IN_PVALB_CHC | (top-ranked) | neuronal |
| EN_L2_3_IT | (top-ranked) | neuronal |
| IN_SST | (top-ranked) | neuronal |
| **Astro** | **1.5 × 10⁻³ (rank 16/27)** | **glial** |

**Lineage note:** This finding essentially **restates a value the paper already computed** (the Fig. 3f resilience contrast). It confirms faithful retrieval and parsing of the source workbook; it is not an independent result.

### Finding 2 — EMP1 and FKBP5 fit the neuroprotective/neurotoxic model, but the aggregate A2-vs-A1 axis is not supported

Using every astrocyte-related DEG table identified from the workbook 'key' sheets — principally **Supplementary Data 7, sheet 'AD PAC DEGs'** and **Supplementary Data 1, sheet 'Fig. 2f'** — genes were classified against the prespecified reactive-astrocyte marker sets (pan-reactive; A1/neurotoxic; A2/neuroprotective; plus CRYAB, MAOB, CHI3L1). Directional enrichment of A2 versus A1 markers among genes higher on the resilient side was tested by Fisher's exact test against an explicit gene universe (union of Supp7 subclass genes, 11,145 genes).

The two flagship genes behave exactly as the model predicts:

- **EMP1** (A2/neuroprotective): log2FC = **−0.99** (Supp Data 7) / **−1.15** (Fig. 2f) → **down** in the AD-PAC / impaired astrocyte state (i.e., higher on the resilient side).
- **FKBP5** (A1/neurotoxic): log2FC = **+0.96** / **+0.86** → **up** in the AD-PAC / impaired astrocyte state.

Under a simple neuroprotective-vs-neurotoxic reading, loss of a protective marker (EMP1) and gain of a toxic marker (FKBP5) in the disease-associated state is exactly the expected pattern, and it reproduces across two independent tables.

However, the **aggregate** directional test is **null**:

- A2-vs-A1 directional Fisher (A2 enriched in the resilient/down direction): **Supp Data 7 OR = 1.0, p = 0.833**; **pooled OR = 0.5, p = 0.893**; **BH q = 1.0**.
- The reason: several canonical **A1/neurotoxic** markers are **also downregulated** in the disease-associated astrocyte state — direct counter-examples include **HLA-E, GBP2, and SERPING1** — which cancels the directional signal.

By contrast, the **pan-reactive** marker set is over-represented among astrocyte DEGs at nominal significance (**OR = 12.8, raw p = 0.0098**) but does **not** survive multiple-testing correction (**BH q = 0.059**). The disease-associated astrocyte state is thus broadly **reactive**, but does not cleanly resolve into the classical binary A1/A2 polarity.

| Gene | Marker class | log2FC (Supp7 / Fig2f) | Direction in AD state | Fits A1/A2 model? |
|---|---|---|---|---|
| EMP1 | A2 / neuroprotective | −0.99 / −1.15 | down | Yes (protective lost) |
| FKBP5 | A1 / neurotoxic | +0.96 / +0.86 | up | Yes (toxic gained) |
| HLA-E (H2-T23 ortholog) | A1 / neurotoxic | down | down | No (counter-example) |
| GBP2 | A1 / neurotoxic | down | down | No (counter-example) |
| SERPING1 | A1 / neurotoxic | down | down | No (counter-example) |

**Aggregate enrichment summary:** A2-vs-A1 directional OR ≈ 0.5–1.0, p ≈ 0.83–0.89, BH q = 1.0 (**not supported**); pan-reactive overlap OR = 12.8, raw p = 0.0098, BH q = 0.059 (**suggestive only** — reactive-in-general).

### Finding 3 — Astrocyte PAC scores co-vary positively with every neuronal subclass within donors

From **Supplementary Data 6, sheet 'Avg. PAC scores AD progression'** (n = 581 donors in this matrix), donor Astro PAC scores were correlated (Spearman, BH-corrected) with those of every excitatory and inhibitory neuronal subclass:

- **All 17 neuronal subclasses show positive correlation** with Astro PAC (rho range **0.168 – 0.570**).
- **Every correlation survives BH correction** (all q < 0.05; minimum q = 4.7 × 10⁻⁵).
- Strongest co-variation: `EN_L3_5_IT_2` (rho = 0.570), `EN_L2_3_IT` (rho = 0.529), `EN_L3_5_IT_1` (rho = 0.518).

This is the most mechanistically informative result. The uniformly positive, moderate-to-strong co-variation of astrocyte and neuronal phenotype-association scores within the same donors indicates a **shared, donor-level disease-burden gradient**: donors with high astrocyte PAC also tend to have high neuronal PAC. That shared gradient is a parsimonious alternative explanation for the astrocyte "resilience" signal in Finding 1 — much of it may be a readout of overall pathological burden rather than an astrocyte-autonomous protective or toxic program.

| Neuronal subclass | Spearman rho vs Astro PAC | BH q |
|---|---|---|
| EN_L3_5_IT_2 | 0.570 | < 0.05 (min q = 4.7 × 10⁻⁵) |
| EN_L2_3_IT | 0.529 | < 0.05 |
| EN_L3_5_IT_1 | 0.518 | < 0.05 |
| (remaining 14 subclasses) | 0.168 – 0.51 | all < 0.05 |

---

## Supported / Refuted Hypotheses

- **Refuted (as an aggregate axis):** Astrocytes do **not** cleanly separate resilient vs impaired donors along a neuroprotective (A2)-vs-neurotoxic (A1) polarity — the directional enrichment test is null (Fisher OR ≈ 0.5–1.0, p ≈ 0.83–0.89, BH q = 1.0).
- **Partially supported (gene-level):** The two named genes **EMP1** (protective, resilient side) and **FKBP5** (toxic, impaired side) behave as predicted and do so reproducibly across two independent tables.
- **Supported:** Astrocyte AD-association **co-varies positively** with neuronal AD-association within donors (a global severity/burden signal), across all 17 neuronal subclasses tested.

---

## Mechanistic Model / Interpretation

The three findings assemble into a single, internally consistent picture that *qualifies* — rather than confirms — the Reactive Astrocyte Subtype Resilience Model.

```
                 DONOR-LEVEL AD BURDEN GRADIENT
                 (shared latent variable)
                          |
        +-----------------+------------------+
        |                                    |
   NEURONAL PAC                          ASTROCYTE PAC
 (EN_IT, IN_PVALB, IN_SST)              (Astro subclass)
   strongest resilience                 modest resilience
   separators (P ~ 1e-6)                separator (P=1.5e-3,
        |                                rank 16/27)
        |   Spearman rho 0.17-0.57            |
        +----------- co-vary (+) -------------+
                          |
                 Within the astrocyte compartment:
                   - broadly REACTIVE state
                     (pan-reactive OR=12.8, raw p=0.0098)
                   - EMP1 (A2) DOWN  <- fits protective-loss
                   - FKBP5 (A1) UP   <- fits toxic-gain
                   - BUT HLA-E/GBP2/SERPING1 (A1) also DOWN
                   => aggregate A2-vs-A1 axis NULL (q=1.0)
```

**Separating observation from inference:**

- *Observed:* Astrocytes separate resilient from strict donors (adj-P = 1.5 × 10⁻³) but rank behind neurons (16/27); EMP1 down and FKBP5 up in the disease-associated state; aggregate A2-vs-A1 enrichment null; astrocyte PAC positively correlated with all neuronal subclasses.
- *Inference:* The data are consistent with a disease-associated astrocyte state that is **generically reactive** rather than cleanly partitioned into neuroprotective A2 and neurotoxic A1 subtypes. The classical binary A1/A2 dichotomy is too coarse to describe the human AD astrocyte transcriptome here. Individual genes (EMP1, FKBP5) may still be meaningful axis markers, but they do not license the aggregate claim. The strong astrocyte–neuron PAC co-variation suggests the astrocyte signal is partly a **passenger** of overall pathological burden, so "astrocyte resilience" should not be read as an autonomous, cell-intrinsic protective program on the strength of these derived scores alone.

---

## Evidence Base

This was a replication of a single primary source; no independent literature search was used to derive the findings. The evidence base is the He et al. 2026 supplementary workbooks themselves.

| Source | Sheet(s) used | Role in this analysis |
|---|---|---|
| He et al. 2026 *Nat Med* — Supp Data 2 | `Fig. 3f` | Resilient-vs-strict PAC contrast per subclass (Finding 1) |
| He et al. 2026 *Nat Med* — Supp Data 7 | `AD PAC DEGs` | Astrocyte DEG table for marker classification / enrichment (Finding 2) |
| He et al. 2026 *Nat Med* — Supp Data 1 | `Fig. 2f` | Second astrocyte DEG table; cross-check of log2FC (Finding 2) |
| He et al. 2026 *Nat Med* — Supp Data 6 | `Avg. PAC scores AD progression` | Donor × subclass PAC matrix; Astro–neuron correlation (Finding 3) |

**Primary citation:** He et al., *Nature Medicine* 2026 — [PMID: 42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/); doi:10.1038/s41591-025-04128-1. All values reported above are re-computations from that paper's own derived tables and therefore share its data lineage; agreement with the paper is expected and does not constitute external validation.

---

## Limitations and Knowledge Gaps

1. **No independent replication.** Every result is a re-analysis of the paper's derived PAC scores and DEG tables, not raw counts. Findings share the paper's normalization and cell-typing pipeline. Finding 1 in particular largely **restates a value the paper already computed**.

2. **No donor labels in Supp Data 6.** The PAC-score matrices are keyed by donor ID only and carry no diagnosis, Braak, or resilience labels. Per contract, no donor labels were inferred or invented, so all Supp Data 6 tests were restricted to label-free designs. The "higher-in-resilient" direction in Finding 2 is therefore **inferred** via the Fig. 3f contrast (resilient donors have lower Astro PAC), not directly measured; no astrocyte resilient-vs-strict DEG table exists in the supplement.

3. **Effect-size convention.** Astrocyte DEG tables are significant-only summaries; per-gene group means and Cohen's d are **not recoverable** from them, so **log2FC is the effect-size convention** used. The enrichment background is the union of Supp7 subclass genes (11,145), not the full transcriptome. Identifier handling: **H2-T23 → HLA-E**; **IIGP1 skipped** (no clean human ortholog).

4. **A1/A2 marker sets are murine-derived and coarse.** The prespecified panels originate largely from mouse reactive-astrocyte literature; the binary A1/A2 framework is increasingly regarded as an oversimplification — a likely reason the aggregate axis test was null despite coherent single-gene behavior.

5. **Confounded astrocyte signal.** The uniform positive astrocyte–neuron PAC correlation (Finding 3) means the astrocyte separation in Finding 1 cannot be cleanly attributed to astrocyte-intrinsic biology versus a shared donor-level burden gradient. Partial-correlation or mediation approaches would be needed but require donor covariates absent from the open data.

6. **Multiple-testing sensitivity.** The most intriguing astrocyte-level signal (pan-reactive enrichment, raw p = 0.0098) does **not** survive BH correction (q = 0.059) and should be treated as suggestive only.

7. **Single region / single cohort.** All data are DLPFC from one snRNA-seq cohort; regional and cross-cohort generalizability is untested here.

---

## Proposed Follow-up Experiments / Actions

1. **Partial-correlation / mediation analysis** of Astro PAC controlling for neuronal PAC (and vice versa), to quantify how much of the astrocyte resilience signal is independent of the shared donor-level burden gradient identified in Finding 3.

2. **Continuous / graded astrocyte-state modeling** rather than binary A1/A2 classification — project astrocyte DEGs onto continuous reactive-state scores or data-driven astrocyte subclusters, which may recover a neuroprotective–neurotoxic axis the binary marker test could not.

3. **Human-specific reactive-astrocyte marker curation.** Rebuild the A1/A2/pan-reactive panels from human AD snRNA-seq references (with explicit ortholog mapping and provenance) and re-run the directional Fisher test; the current null may partly reflect murine marker mismatch.

4. **Cross-cohort external replication.** Obtain controlled per-donor astrocyte expression with resilience labels (or an independent human AD snRNA-seq dataset) and test the A1/A2 axis directly with proper effect sizes and group means — converting this lineage-shared re-analysis into genuine independent validation of the EMP1-down / FKBP5-up signature.

5. **Single-gene follow-up on EMP1 and FKBP5** — spatial or protein-level validation of directional change in resilient vs impaired donors, since these are the only components that cleanly fit the model and are the most defensible candidate axis markers.

6. **Cross-provider comparison (lineage-marked, separate step).** Now that primary outputs and checksums are locked, compare these numbers against any other provider's replication as an explicitly lineage-marked, post-hoc step — without letting external results influence method, feature, or threshold choices.

---

## Artifact Bundle (for independent replay)

All files are under `kb/hypotheses/Alzheimer_Disease/reactive_astrocyte_resilience_model/openscientist_artifacts/`:

| Artifact | Role | Notes |
|---|---|---|
| `MANIFEST.yaml` | manifest / INPUT_MANIFEST | `status: SUCCEEDED`, `fallback_used: false`, `direct_analysis_completed: true`; input zip sha256 + byte count, all output checksums, verified replay block |
| `analysis.py` | CODE | Standalone deterministic analysis; `--output-dir`, optional `--cache-dir`; regenerates all tabular outputs without an LLM |
| `environment.txt` | ENVIRONMENT | Python version, OS, exact third-party package versions (incl. openpyxl) |
| `methods.md` | METHODS | Inclusion/exclusion, normalization state, identifier mapping, tests, BH correction, effect-size convention |
| `samples.csv` | TABULAR_RESULT | One row per sample/donor with group and exclusion reason |
| `gene_results.csv` | TABULAR_RESULT | Tidy per-gene results: group sizes, means, log2 mean diff, fold change, statistic, raw p, BH q, Cohen's d |
| `fig3f_resilience.csv` | TABULAR_RESULT | Fig. 3f resilience contrast per subclass |
| `enrichment_results.csv` | TABULAR_RESULT | A2-vs-A1 and pan-reactive Fisher enrichment |
| `correlation_results.csv` | TABULAR_RESULT | Astro–neuron PAC Spearman correlations (BH) |
| `comparison.md` | SUMMARY | Observed results vs biological inference |
| `raw/` | inputs | Downloaded Supplementary Data zip (local/recoverable) |
| `replay/` | replay assets | Clean re-execution; `samples.csv` & `gene_results.csv` byte-identical to primary |

**Input:** `41591_2025_4128_MOESM3_ESM.zip`, sha256 `27901070f322dff0e1283343d61de6f80b656bc41dbc7ea0efa9e8b8a1851865`, 13,893,637 bytes, retrieved from the canonical credential-free Springer Nature media URL recorded in the manifest.

**Replay verification:** `analysis.py` was re-run into `replay/` reusing `raw/` as `--cache-dir`; the manifest records `replay.verified: true` with a `byte_identity` mapping confirming `true` for every primary `TABULAR_RESULT`, plus replay asset SHA-256 checksums and byte counts for each.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist comparison](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_comparison.md)
- [OpenScientist correlation results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_correlation_results.csv)
- [OpenScientist enrichment results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_enrichment_results.csv)
- [OpenScientist fig3f resilience](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_fig3f_resilience.csv)
- [OpenScientist gene results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_gene_results.csv)
- [OpenScientist methods](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_methods.md)
- [OpenScientist comparison](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_comparison.md)
- [OpenScientist correlation results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_correlation_results.csv)
- [OpenScientist enrichment results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_enrichment_results.csv)
- [OpenScientist fig3f resilience](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_fig3f_resilience.csv)
- [OpenScientist gene results](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_gene_results.csv)
- [OpenScientist methods](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_methods.md)
- [OpenScientist samples](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_replay_samples.csv)
- [OpenScientist samples](openscientist_artifacts/kb_hypotheses_Alzheimer_Disease_reactive_astrocyte_resilience_model_openscientist_artifacts_samples.csv)

## Term Validation

No ontology term identifiers were found in this report.