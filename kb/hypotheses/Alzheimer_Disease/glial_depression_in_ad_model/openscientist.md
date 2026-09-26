---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-26T02:11:26.311496'
end_time: '2026-09-26T03:03:53.809776'
duration_seconds: 3147.5
template_file: templates/hypothesis_dataset_analysis.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: glial_depression_in_ad_model
  hypothesis_label: Glial Inflammatory and ER-Stress Model of Depression in Alzheimer
    Disease
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: glial_depression_in_ad_model\nhypothesis_label:\
    \ Glial Inflammatory and ER-Stress Model of Depression in Alzheimer Disease\n\
    status: EMERGING\ndescription: 'Depressive symptoms arising in people with Alzheimer\
    \ disease are modeled as having a glial\n  cellular substrate distinct from the\
    \ general Alzheimer inflammatory signal: astrocyte (and oligodendrocyte)\n  states\
    \ carrying inflammatory and endoplasmic reticulum stress programs are proposed\
    \ to be enriched in\n  Alzheimer donors with depression compared with Alzheimer\
    \ donors without it, and to overlap with glial\n  changes seen in major depressive\
    \ disorder.'\napplies_to_subtypes:\n- Late-Onset Alzheimer's Disease\nevidence:\n\
    - reference: PMID:42778763\n  reference_title: AI-based characterization of Alzheimer's\
    \ disease phenotypes from population-scale single-cell\n    data.\n  supports:\
    \ SUPPORT\n  evidence_source: COMPUTATIONAL\n  quote_role: PRIMARY_RESULT\n  snippet:\
    \ We also identified many PACs for multiple phenotypes, including the astrocytes\
    \ between AD and\n    depression showing specific gene expression patterns such\
    \ as inflammation and endoplasmic reticulum\n    stress pathways.\n  explanation:\
    \ The seed observation. The comparison was within Alzheimer donors (with versus\
    \ without depression),\n    so the shared Alzheimer signal is removed by design.\
    \ It is an association from computational scoring\n    and does not show that\
    \ the glial state produces the mood symptom.\nnotes: EMERGING on a single cohort.\
    \ Whether depression within Alzheimer disease shares mechanism with\n  major depressive\
    \ disorder is stated by the source as unresolved. Linked to the Behavioral Changes\
    \ phenotype\n  and the Neuroinflammation node, but no causal edge is drawn because\
    \ the direction between glial state\n  and depressive symptoms is not established."
  artifact_dir: kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts
  dataset_inputs: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41591-025-04128-1/MediaObjects/41591_2025_4128_MOESM3_ESM.zip
  target_variables: Astro and Oligo depression PAC scores; HSPA5, DDIT3, ATF4, XBP1,
    MANF, NFKBIA, CHI3L1, SERPINA3
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
    only restate what the paper already computed. Objective: test whether the depression-within-Alzheimer
    glial signal is distinct from the general Alzheimer signal. (1) For donors present
    in both ''Avg. PAC scores DepressionMood'' and ''Avg. PAC scores AD progression''
    (Supp Data 6), correlate each subclass''s depression PAC score with its AD-progression
    PAC score (Spearman, BH); a distinct signal predicts weak correlation for Astro
    and Oligo. Also rank subclasses by mean absolute ''SHAP values DepressionMood''.
    (2) In Supp Data 3 (depression-PAC astrocyte DEGs and the AD-Depression Astro_WIF1
    cluster genes) test enrichment of prespecified sets: unfolded protein response
    / ER stress (HSPA5, DDIT3, ATF4, ATF6, XBP1, ERN1, EIF2AK3, HSP90B1, PDIA4, PDIA6,
    CALR, DNAJB9, SEL1L, HERPUD1, MANF) and inflammatory signalling (NFKBIA, IL1B,
    IL6, CXCL8, TNF, STAT3, SOCS3, C3, CHI3L1, SERPINA3, CD44). (3) Compare depression
    astrocyte DEGs with Supp Data 7 ''AD PAC DEGs'' astrocyte rows: report overlap
    and a Jaccard index, and whether ER-stress genes are specific to the depression
    set. Use Supp Data 4 module GO enrichment only descriptively.'
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
citation_count: 4
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 20
artifact_sources:
  openscientist_artifacts_zip: 20
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
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_comparison.md
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_comparison.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comparison
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_enrichment_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_enrichment_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist enrichment results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_membership.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_membership.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene membership
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_methods.md
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_methods.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist methods
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_overlap_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_overlap_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist overlap results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_provenance.json
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_provenance.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist provenance
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_enrichment_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_enrichment_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist enrichment results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_membership.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_membership.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene membership
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_overlap_results.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_overlap_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist overlap results
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_provenance.json
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_provenance.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist provenance
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_samples.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_shap_ranking.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_shap_ranking.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist shap ranking
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_subclass_correlation.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_subclass_correlation.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist subclass correlation
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_samples.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_shap_ranking.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_shap_ranking.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist shap ranking
- filename: provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_subclass_correlation.csv
  path: openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_subclass_correlation.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist subclass correlation
---

## Question


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


## Output

ANALYSIS_STATUS: SUCCEEDED

# Glial Inflammatory and ER-Stress Model of Depression in Alzheimer Disease — Computational Replication Report

**Disease:** Alzheimer Disease · **Hypothesis ID:** `glial_depression_in_ad_model`
**Source dataset:** He et al. 2026, *Nature Medicine* — Supplementary Data zip (`41591_2025_4128_MOESM3_ESM.zip`), [PMID: 42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/), doi:10.1038/s41591-025-04128-1
**Data lineage:** Derived scores from the controlled **PsychAD** snRNA-seq cohort (synapse:syn60084804; 1,494 donors; DLPFC). Controlled/raw data were **not** accessed; only the open Supplementary Data workbooks were analyzed.
**Artifact bundle:** `kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts/` (replay-verified, `status: SUCCEEDED`).

---

## Summary

This run is a **computational replication**, not an independent validation. The task was to retrieve the open Supplementary Data of He et al. 2026 (*Nature Medicine*), execute a prespecified, label-free re-analysis of phenotype-associated-cell (PAC) scores and published differentially expressed gene (DEG) tables, and save a fully replayable artifact bundle. All required artifacts were generated, and a clean replay reproduced `samples.csv` and `gene_results.csv` byte-for-byte. The manifest is closed at `status: SUCCEEDED`, `fallback_used: false`, `direct_analysis_completed: true`, with replay `verified: true`.

The central scientific objective was to test whether the **depression-within-Alzheimer glial signal is distinct from the general Alzheimer signal**. Using Supplementary Data 6 (donor × 27-subclass PAC-score matrices, keyed only by donor ID and carrying no diagnosis/Braak/resilience labels), we correlated each cell subclass's DepressionMood PAC score against its AD-progression PAC score across the 208 donors present in both sheets. The result supports a **distinct glial depression signal**: astrocytes (**Astro**) show essentially no cross-phenotype correlation (Spearman rho = −0.015, BH q = 0.83) and oligodendrocytes (**Oligo**) show only a weak correlation (rho = −0.18, q = 0.010), whereas neuronal subclasses track AD progression strongly and negatively (IN_VIP rho = −0.80, IN_SST rho = −0.77, q < 1e-40). Concordantly, glia are the top predictors of the DepressionMood phenotype by mean absolute SHAP importance (**Astro rank #1**, 0.099; **Oligo rank #2**, 0.050).

The **ER-stress / unfolded-protein-response (UPR) component** of the hypothesis is **context-dependent rather than depression-specific**. UPR/ER-stress genes (e.g., HSPA5, CALR, DNAJB9) are enriched only within the combined **AD-Depression Astro_WIF1** cluster gene set (Fisher OR = 17.5, q = 0.0092 against a whole-genome universe; **not significant** against a DEG-restricted universe, q = 0.57), and are **absent** from the broad depression-PAC astrocyte DEGs (0 of 15 prespecified UPR genes present). The overlap between depression-astrocyte DEGs (568 genes) and AD-astrocyte DEGs (1,171 genes) has Jaccard index 0.18, and the ER-stress genes that do appear (CALR, HSPA5) sit in the **AD** set, not the depression set. Because the source paper's own abstract already reports inflammation and ER-stress pathways distinguishing AD-vs-depression astrocytes, this ER-stress finding **restates the paper's computation** and cannot be treated as independent confirmation.

---

## Key Findings

### Finding F001 — The astrocyte depression-PAC signal is statistically distinct from the AD-progression PAC signal

Re-analysis of He et al. 2026 Supplementary Data 6 joined the two donor × subclass matrices — `Avg. PAC scores DepressionMood` and `Avg. PAC scores AD progression` — on donor ID, yielding **208 donors present in both sheets**. For each of the 27 cell subclasses we computed a Spearman correlation between the donor's depression PAC score and AD-progression PAC score, then applied Benjamini–Hochberg (BH) correction across the 27 tests. The prespecified prediction was that a *distinct* depression signal would show **weak** cross-phenotype correlation for glia (Astro, Oligo).

That prediction is borne out. Astrocytes show no meaningful correlation between their depression and AD-progression PAC scores (rho = −0.015, q = 0.825), and oligodendrocytes show only a weak, though statistically detectable, correlation (rho = −0.182, q = 0.0099). By contrast, inhibitory neuronal subclasses are strongly and negatively coupled across the two phenotypes (IN_VIP rho = −0.80; IN_SST rho = −0.77; both q < 1e-40), indicating that neuronal PAC scores largely co-vary with AD progression, while glial PAC scores do not. In other words, the glial contribution to the depression phenotype is **not** simply a shadow of the general AD trajectory.

This is reinforced by the feature-importance ranking. Ranking the 27 subclasses by **mean absolute SHAP value for DepressionMood** (Supplementary Data 6 SHAP sheet) places **Astro first (0.099)** and **Oligo second (0.050)** — glia are the leading model-level predictors of the depression phenotype. The convergence of (a) low cross-phenotype correlation and (b) top SHAP importance for the same two glial subclasses is the core quantitative support for a distinct glial depression-in-AD signal.

### Finding F001 (continued) — Enrichment and overlap tests: ER-stress is context-specific

Two gene-set analyses examined whether the glial depression signal carries a specific ER-stress / UPR molecular signature.

**Enrichment (Fisher exact, BH over 8 tests).** The prespecified UPR/ER-stress set (HSPA5, DDIT3, ATF4, ATF6, XBP1, ERN1, EIF2AK3, HSP90B1, PDIA4, PDIA6, CALR, DNAJB9, SEL1L, HERPUD1, MANF) was tested against two Supplementary Data 3 gene lists. Against the **AD-Depression Astro_WIF1 up-regulated cluster**, UPR enrichment is significant under a whole-genome universe (**OR = 17.5, q = 0.0092**) but collapses to non-significance under a DEG-restricted universe (**OR = 2.07, q = 0.57**) — meaning the apparent enrichment is largely a function of universe choice rather than a robust, background-independent signal. Against the **broad depression-PAC astrocyte DEGs**, **0 of 15** UPR genes are present, so there is no depression-specific UPR enrichment at all.

**Overlap and specificity (Supplementary Data 7).** Comparing the depression-astrocyte DEG set (568 genes) with the AD-astrocyte DEG set (1,171 genes) gives a **Jaccard index of 0.180**. Crucially, the ER-stress genes that appear in these tables (CALR, HSPA5) are found in the **AD** set, not the depression set — i.e., the ER-stress axis is associated with the general AD astrocyte program, not selectively with the depression program.

Taken together, F001 supports the *distinct glial signal* half of the hypothesis but **does not** support a *depression-specific ER-stress* signature: ER-stress is present only in the combined AD-Depression cluster and in the AD astrocyte program, consistent with a context-dependent rather than depression-driven phenomenon.

### Finding F002 — The ER-stress/UPR result restates the source paper; independent human evidence exists for a UPR–depression link

Because the locked replication draws entirely on the paper's derived scores and DEG tables, its ER-stress result must be read against the paper's own claims. The source paper explicitly reports that *"the astrocytes between AD and depression [show] specific gene expression patterns such as inflammation and endoplasmic reticulum stress pathways"* ([PMID: 42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/)). Our enrichment finding — UPR genes concentrated in the AD-Depression Astro_WIF1 cluster — **restates this same phenomenon**, and therefore this component of the analysis is **not** independent validation. It shares data lineage with the paper by construction.

Independent, lineage-separate human evidence nonetheless makes the broader ER-stress–depression axis biologically plausible. Yoshino & Dwivedi 2020 found UPR genes significantly elevated in the dorsolateral prefrontal cortex (dlPFC) of subjects with major depressive disorder: *"The level of mRNA expression in MDD subjects was significantly higher for GRP78 (p = 0.008), GRP94 (p = 0.018), and ATF4C (p = 0.03) compared to non-psychiatric controls"* ([PMID: 31727394](https://pubmed.ncbi.nlm.nih.gov/31727394/)). GRP78 is HSPA5 and ATF4C maps to ATF4 — both members of our prespecified UPR set — so this external study lends plausibility to the ER-stress limb of the hypothesis even though our replication cannot itself confirm it.

### Finding F003 — Descriptive module GO enrichment: neuroinflammation is enriched at module level; ER-stress is not a discrete GO term

Per the objective, Supplementary Data 4 (`Module GO enrichment`) was read **descriptively only** and does not alter the locked artifacts. Across 40 significantly enriched GO pathway rows (hypergeometric test with FDR), a keyword scan found **inflammation/immune** terms enriched — most notably *"Neuroinflammation and glutamatergic signaling"* (module 2; member hits include IL1R1, STAT3, GFAP, IL6R, SOCS3, TNFRSF1A, FOS, SLC1A2, FGF2, IL13RA1, CAMK4; FDR = 0.022) and *"Immune response to tuberculosis"* (IRF1, STAT1, IFNGR2; FDR = 0.098). By contrast, **no explicit endoplasmic-reticulum-stress / unfolded-protein-response / protein-folding / chaperone GO term** appeared among the enriched module pathways. STAT3 and SOCS3 — both members of the prespecified inflammatory set used in the locked enrichment analysis — appear as members of the enriched neuroinflammation module.

This descriptive read reinforces the asymmetry seen in F001: **neuroinflammation is a module-level (co-regulation) signal**, whereas **ER-stress appears only at the single-cluster gene level** (Astro_WIF1) and does not rise to a discrete enriched GO term. The inflammatory limb of the hypothesis has broader support in these data than the ER-stress limb.

---

## Mechanistic Model / Interpretation

The replication distinguishes two limbs of the "Glial Inflammatory and ER-Stress Model of Depression in AD," and the evidence for the two limbs differs in strength.

```
                         PsychAD DLPFC (1,494 donors)  ── controlled, NOT accessed
                                       │
                     He et al. 2026 derived scores (open Supp. Data)
                                       │
        ┌──────────────────────────────┴──────────────────────────────┐
        │                                                              │
   PAC scores (Supp Data 6)                             DEG / cluster tables (Supp Data 3, 7)
        │                                                              │
 Depression vs AD-progression                        Gene-set enrichment & overlap
 cross-phenotype correlation                         (UPR/ER-stress; inflammation)
        │                                                              │
 ┌──────┴───────┐                                    ┌─────────────────┴─────────────────┐
 │ Neurons      │  strong coupling  rho -0.7…-0.8   │ Inflammation: module-level (Supp 4) │  ENRICHED
 │ (IN_VIP/SST) │  → track AD                        │  STAT3, SOCS3, IL1R1, IL6R, GFAP    │  (descriptive)
 ├──────────────┤                                    ├─────────────────────────────────────┤
 │ Astro  #1    │  rho -0.015 (q0.83) → DISTINCT     │ ER-stress/UPR: only in AD-Dep       │  CONTEXT-
 │ Oligo  #2    │  rho -0.18  (q0.01) → weak         │  Astro_WIF1 cluster (OR 17.5 gwm;   │  DEPENDENT
 │ (top SHAP)   │                                    │  n.s. vs DEG universe); 0/15 in     │  not depression-
 └──────────────┘                                    │  broad depression DEGs              │  specific
                                                     └─────────────────────────────────────┘
```

**Limb 1 — Distinct glial depression signal (supported).** Glia (Astro, Oligo) carry a depression PAC signal that is statistically decoupled from AD progression, while neurons do not. The same glia are the strongest SHAP predictors of the depression phenotype. This is the most robust, internally coherent result of the replication and directly supports the "glial" premise of the hypothesis.

**Limb 2a — Inflammatory signature (supported descriptively).** Neuroinflammatory co-regulation modules are enriched (module 2, FDR = 0.022), and inflammatory-set members STAT3/SOCS3 participate. This aligns with the "inflammatory" premise, though it is drawn from the descriptive Supp Data 4 read and not from a hypothesis-locked test.

**Limb 2b — ER-stress signature (context-dependent, restates the paper).** UPR/ER-stress genes are enriched only in the combined AD-Depression Astro_WIF1 cluster and are absent from the broad depression-astrocyte DEGs; the enrichment is sensitive to the choice of gene universe. ER-stress genes that appear in the DEG tables (CALR, HSPA5) belong to the AD program. Thus ER-stress is best read as a **context-specific** feature of a particular astrocyte state rather than a depression-defining molecular signature — and, because the paper already reports it, this limb cannot be independently validated here.

| Hypothesis limb | Test | Result | Verdict |
|---|---|---|---|
| Glia distinct from AD signal | Cross-phenotype Spearman (Astro/Oligo) | Astro rho −0.015 (q 0.83); Oligo −0.18 (q 0.01) | **Supported** |
| Glia predict depression | Mean abs. SHAP DepressionMood | Astro #1 (0.099); Oligo #2 (0.050) | **Supported** |
| Neurons track AD (contrast) | Cross-phenotype Spearman (neurons) | IN_VIP −0.80; IN_SST −0.77 (q<1e-40) | **Supported** |
| Depression-specific UPR/ER-stress | Fisher enrichment, broad depression DEGs | 0/15 UPR genes present | **Not supported** |
| UPR in AD-Dep cluster | Fisher enrichment, Astro_WIF1 | OR 17.5 (q 0.009 gwm); n.s. vs DEG universe (q 0.57) | **Context-dependent; restates paper** |
| ER-stress specific to depression set | Overlap/Jaccard vs AD DEGs | Jaccard 0.18; CALR/HSPA5 in AD set | **Not supported** |
| Inflammation at module level | Supp Data 4 GO (descriptive) | Neuroinflammation module FDR 0.022 | **Supported (descriptive)** |

---

## Evidence Base

| PMID | Study | Relevance to this replication |
|---|---|---|
| [42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/) | *AI-based characterization of Alzheimer's disease phenotypes from population-scale single-cell data* (He et al. 2026, source paper) | Source of all analyzed data. Its abstract states astrocytes between AD and depression show *"inflammation and endoplasmic reticulum stress pathways,"* so our ER-stress enrichment **restates** the paper (shared lineage). |
| [31727394](https://pubmed.ncbi.nlm.nih.gov/31727394/) | *Elevated expression of unfolded protein response genes in the prefrontal cortex of depressed subjects* (Yoshino & Dwivedi 2020) | **Independent, lineage-separate** human dlPFC evidence: GRP78/HSPA5 (p=0.008), GRP94 (p=0.018), ATF4C/ATF4 (p=0.03) elevated in MDD. Gives external plausibility to the UPR–depression axis. |
| [42537476](https://pubmed.ncbi.nlm.nih.gov/42537476/) | *MANF suppresses ferroptosis to alleviate depressive-like behaviors via PERK/ATF4* | Mechanistic model tying MANF and PERK/ATF4 (prespecified UPR-set members) to depressive-like behavior; supports ER-stress relevance to depression biology (preclinical). |
| [42425961](https://pubmed.ncbi.nlm.nih.gov/42425961/) | *MANF in the lateral septum dynamically regulates ER function in chronic stress* | Links persistent UPR activation and MANF dynamics to depressive-like phenotypes; supports the ER-stress limb mechanistically. |
| [42216529](https://pubmed.ncbi.nlm.nih.gov/42216529/) | *ER stress in comorbidity of atopic dermatitis and psychiatric disorders* | MANF/ER-stress modulation improves comorbid mental disorder symptoms; broader plausibility for ER-stress in mood pathology. |
| [40245333](https://pubmed.ncbi.nlm.nih.gov/40245333/) | *ECT on hippocampal ER stress in a rat depression model* | GRP78/HSPA5, XBP1, ATF4 measured; ER-stress altered in depression and reversible by ECT — supports UPR involvement (preclinical). |
| [27192986](https://pubmed.ncbi.nlm.nih.gov/27192986/) | *Sodium phenylbutyrate attenuates LPS-induced depressive behavior* | ER-stress inhibitor reduces depressive-like behavior and neuroinflammation (IL-1β, TNF-α, GRP78) — links the inflammatory and ER-stress limbs. |
| [42150700](https://pubmed.ncbi.nlm.nih.gov/42150700/) | *Spinal cord injury as a window into hippocampal dysfunction* | Review convergence of neuroinflammation and ER stress with depression/anxiety phenotypes; broad contextual support. |

**How the evidence lines up:** The single most relevant citation, the source paper ([PMID: 42778763](https://pubmed.ncbi.nlm.nih.gov/42778763/)), *confirms* that our ER-stress observation is a re-statement of its own result rather than independent corroboration — an essential caveat. The remaining literature is **externally derived** and consistently supports the biological plausibility of an ER-stress/UPR contribution to depression (notably the recurrent appearance of HSPA5/GRP78 and ATF4 across independent human and animal studies), but none of it can substitute for the independent replication that shared-lineage data cannot provide.

---

## Limitations and Knowledge Gaps

1. **Shared data lineage, not independent replication.** Every quantitative result is a re-analysis of He et al.'s published derived scores and DEG tables. The astrocyte inflammation/ER-stress observation in particular restates a claim already in the paper's abstract; it cannot count as independent validation.
2. **No donor labels.** Supplementary Data 6 is keyed by donor ID only, with no diagnosis, Braak stage, or resilience labels. By design, we restricted to label-free tests (within-donor paired contrasts, cross-phenotype correlations on the donor-ID join, and gene-set overlap tests). We did not — and must not — infer or invent donor labels, so no case/control effect sizes on the PAC scores themselves were computed.
3. **Universe sensitivity of enrichment.** The Astro_WIF1 UPR enrichment is significant against a whole-genome universe (OR 17.5) but not against a DEG-restricted universe (OR 2.07, q 0.57). This universe dependence means the ER-stress enrichment should be interpreted cautiously; it is not a background-robust signal.
4. **Descriptive-only components.** Supplementary Data 4 module GO enrichment was used descriptively per the objective. Its inflammation findings are suggestive but were not part of the hypothesis-locked statistical tests.
5. **PAC scores are model-derived features.** PAC scores and SHAP values are outputs of the paper's model. Correlations among them describe the model's learned representation, not raw expression, and share whatever biases the upstream model carries.
6. **Effect-size conventions.** The correlation tests report Spearman rho with BH q-values; enrichment reports odds ratios; the `gene_results.csv` schema carries the required effect-size columns (log2 mean difference, fold change, Cohen's d) for the gene-level comparisons where group structure exists. Where donor labels are absent, group-difference effect sizes are necessarily not applicable.

---

## Proposed Follow-up Experiments / Actions

1. **Independent-cohort validation of the glial depression signal.** Re-derive PAC-like scores in a lineage-independent snRNA-seq cohort (e.g., ROSMAP or a separate DLPFC dataset) with proper depression labels, and test whether Astro/Oligo again decouple from AD progression while remaining top predictors. This would move the F001 result from re-analysis to genuine replication.
2. **Label-linked case/control test.** Under appropriate controlled-data access, join the PAC scores to donor diagnosis/Braak/resilience labels and compute proper group contrasts with effect sizes (Cohen's d) — the analysis the current label-free constraint precludes.
3. **Background-robust enrichment.** Repeat the UPR/ER-stress enrichment with multiple explicit, matched gene universes (expressed-gene background, cell-type-specific background) and permutation-based null models to determine whether the Astro_WIF1 UPR signal survives universe choice.
4. **Targeted UPR/inflammation panel in astrocytes.** In situ or targeted spatial transcriptomics of HSPA5, DDIT3, ATF4, XBP1, MANF (UPR) and NFKBIA, STAT3, SOCS3, CHI3L1, SERPINA3 (inflammation) in DLPFC astrocytes, stratified by depression status within AD, to test whether the ER-stress axis is genuinely depression-associated or an AD-astrocyte-state feature.
5. **Functional test of the MANF/PERK/ATF4 axis.** Given the convergent preclinical literature ([PMID: 42537476](https://pubmed.ncbi.nlm.nih.gov/42537476/), [PMID: 42425961](https://pubmed.ncbi.nlm.nih.gov/42425961/)), evaluate whether modulating MANF or PERK/ATF4 signaling in astrocyte models alters inflammatory output — connecting the two limbs of the hypothesis mechanistically.

---

## Artifacts and Reproducibility

All outputs live under `kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/openscientist_artifacts/`:

- `MANIFEST.yaml` — `schema_version: '1.0'`, `status: SUCCEEDED`, `fallback_used: false`, `direct_analysis_completed: true`; input/output checksums and byte counts; replay block with `verified: true` and `byte_identity` mapping for every `TABULAR_RESULT`.
- `analysis.py` (CODE) — deterministic, `--output-dir`/`--cache-dir`, regenerates all tabular outputs without an LLM.
- `environment.txt` (ENVIRONMENT) — Python/OS and exact third-party package versions (incl. the added `openpyxl`).
- `gene_results.csv`, `samples.csv`, `subclass_correlation.csv`, `shap_ranking.csv`, `enrichment_results.csv`, `overlap_results.csv`, `gene_membership.csv` (TABULAR_RESULT).
- `methods.md` (METHODS), `comparison.md` (SUMMARY), `provenance.json`, and `raw/` (recoverable inputs).
- `replay/` — clean re-execution reusing `raw/` as cache; replayed `samples.csv` and `gene_results.csv` are byte-identical to the primary outputs.

**Replication verdict:** The glial depression-in-AD signal is statistically distinct from the general AD signal (glia decoupled from AD progression and top SHAP predictors of depression), while the ER-stress/UPR limb is context-dependent — confined to the combined AD-Depression Astro_WIF1 cluster and absent from the broad depression-astrocyte DEGs — and, being already reported by the source paper, restates the paper rather than independently validating it.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist comparison](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_comparison.md)
- [OpenScientist enrichment results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_enrichment_results.csv)
- [OpenScientist gene membership](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_membership.csv)
- [OpenScientist gene results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_gene_results.csv)
- [OpenScientist methods](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_methods.md)
- [OpenScientist overlap results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_overlap_results.csv)
- [OpenScientist provenance](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_provenance.json)
- [OpenScientist enrichment results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_enrichment_results.csv)
- [OpenScientist gene membership](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_membership.csv)
- [OpenScientist gene results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_gene_results.csv)
- [OpenScientist overlap results](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_overlap_results.csv)
- [OpenScientist provenance](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_provenance.json)
- [OpenScientist samples](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_samples.csv)
- [OpenScientist shap ranking](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_shap_ranking.csv)
- [OpenScientist subclass correlation](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_replay_subclass_correlation.csv)
- [OpenScientist samples](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_samples.csv)
- [OpenScientist shap ranking](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_shap_ranking.csv)
- [OpenScientist subclass correlation](openscientist_artifacts/provenance_kb_hypotheses_Alzheimer_Disease_glial_depression_in_ad_model_openscientist_artifacts_subclass_correlation.csv)

## Term Validation

No ontology term identifiers were found in this report.