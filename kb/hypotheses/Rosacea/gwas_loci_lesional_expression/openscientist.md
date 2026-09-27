---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T18:05:17.953763'
end_time: '2026-09-06T18:38:23.791222'
duration_seconds: 1985.84
template_file: templates/hypothesis_dataset_analysis.md
template_variables:
  disease_name: Rosacea
  category: Complex
  hypothesis_group_id: gwas_loci_lesional_expression
  hypothesis_label: Rosacea GWAS susceptibility loci act through altered expression
    in lesional skin, including a TLR1-TLR2 heterodimer axis
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: gwas_loci_lesional_expression\nhypothesis_label:\
    \ Rosacea GWAS susceptibility loci act through altered expression in lesional\
    \ skin, including\n  a TLR1-TLR2 heterodimer axis\nstatus: EMERGING\ndescription:\
    \ 'The genome-wide significant rosacea loci fall into two groups: immune (HLA-DRA/BTNL2,\
    \ the\n  HLA class II alleles, IL13, IRF1, TLR1) and pigmentation (IRF4, HERC2-OCA2,\
    \ SLC45A2). The hypothesis\n  is that the immune loci are expressed and differentially\
    \ regulated in lesional skin, so that germline\n  susceptibility acts through\
    \ the innate and adaptive inflammatory program modelled in this entry rather\n\
    \  than only through skin phototype. Aponte et al. found three loci (PSMB9-HLA-DMB,\
    \ HERC2-OCA2, NRXN3-DIO2)\n  differentially expressed in lesional versus non-lesional\
    \ skin, and Chang et al. localized HLA-DRA and\n  BTNL2 protein to the perifollicular\
    \ infiltrate, but the newer Million Veteran Program loci, TLR1 in\n  particular,\
    \ have never been tested this way. TLR1 is the obligate heterodimer partner of\
    \ TLR2 for triacylated\n  lipopeptide sensing, so a TLR1 risk allele would be\
    \ the first germline entry point into the TLR2-KLK5-LL-37\n  axis. An exploratory\
    \ analysis of the subtype-spanning biopsy series (GEO GSE65914) asks whether each\n\
    \  locus gene is differentially expressed in lesional skin by subtype, and whether\
    \ TLR1 and TLR2 are co-expressed\n  there. This hypothesis has no causal edges\
    \ of its own; it concerns the genetic entries. Downstream causal\n  edges that\
    \ belong to it would opt in via hypothesis_groups: [gwas_loci_lesional_expression].'\n\
    evidence:\n- reference: PMID:29771307\n  reference_title: Assessment of rosacea\
    \ symptom severity by genome-wide association study and expression\n    analysis\
    \ highlights immuno-inflammatory and skin pigmentation genes.\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: Genes within three loci (PSMB9-HLA-DMA,\
    \ HERC-OCA2 and NRX3-DIO2) were differentially expressed\n    in a previously\
    \ published clinical rosacea transcriptomics study that compared lesional to non-lesional\n\
    \    samples.\n  explanation: 'The precedent: GWAS loci already shown to change\
    \ expression in lesional skin, motivating\n    the same test for the remaining\
    \ loci.'\n- reference: PMID:25695682\n  reference_title: Assessment of the genetic\
    \ basis of rosacea by genome-wide association study.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Exploratory immunohistochemical analysis of HLA-DRA\
    \ and BTNL2 expression in papulopustular\n    rosacea lesions from six individuals,\
    \ including one with the rs763035 variant, revealed staining in\n    the perifollicular\
    \ inflammatory infiltrate of rosacea for both proteins.\n  explanation: Protein-level\
    \ lesional expression for the lead HLA-region locus.\nnotes: 'Exploratory dataset\
    \ run: geo:GSE65914 with target genes HLA-DRA, BTNL2, HLA-DRB1, HLA-DQB1, HLA-DQA1,\n\
    \  IL13, IRF1, TLR1, TLR2, IRF4, HERC2, OCA2, SLC45A2. The MVP loci come from\
    \ the GWAS Catalog (GCST90476178),\n  which this repository cannot yet cite directly\
    \ (see the dbgap:phs001672 dataset record).'"
  artifact_dir: kb/hypotheses/Rosacea/gwas_loci_lesional_expression/openscientist_artifacts
  dataset_inputs: geo:GSE65914
  target_variables: HLA-DRA, BTNL2, HLA-DRB1, HLA-DQB1, HLA-DQA1, IL13, IRF1, TLR1,
    TLR2, IRF4, HERC2, OCA2, SLC45A2
  analysis_objective: For each rosacea GWAS locus gene, a prespecified lesional-versus-healthy-control
    expression contrast in GSE65914, run separately for the erythematotelangiectatic,
    papulopustular and phymatous subtypes and for all rosacea pooled; then, across
    all samples, Spearman correlation of TLR1 with TLR2 expression and a test of whether
    the correlation differs between rosacea and control. Report every gene whether
    or not it reaches significance, and state which loci are immune versus pigmentation.
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
citation_count: 3
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 10
artifact_sources:
  openscientist_artifacts_zip: 10
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
- filename: comparison.md
  path: openscientist_artifacts/comparison.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comparison
- filename: gene_results.csv
  path: openscientist_artifacts/gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: methods.md
  path: openscientist_artifacts/methods.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist methods
- filename: replay/gene_results.csv
  path: openscientist_artifacts/replay/gene_results.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gene results
- filename: replay/samples.csv
  path: openscientist_artifacts/replay/samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
- filename: replay/tlr_correlation.csv
  path: openscientist_artifacts/replay/tlr_correlation.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist tlr correlation
- filename: samples.csv
  path: openscientist_artifacts/samples.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist samples
- filename: tlr_correlation.csv
  path: openscientist_artifacts/tlr_correlation.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist tlr correlation
artifact_manifest_sha256: sha256:9c9a14505be43a76a89916f4e93bc3137bec1db68a2beca3360b3f213dbcb6d7
---

## Question


# Hypothesis Dataset Replication

You are performing a computational replication for the Disorder Mechanisms
Knowledge Base. This is not a literature-review task. The run succeeds only if
you retrieve the stated datasets, execute the analysis, and save enough
artifacts for an independent replay.

## Target

- Disease: Rosacea
- Hypothesis ID: gwas_loci_lesional_expression
- Hypothesis label: Rosacea GWAS susceptibility loci act through altered expression in lesional skin, including a TLR1-TLR2 heterodimer axis
- Dataset inputs:

geo:GSE65914

- Target variables or genes:

HLA-DRA, BTNL2, HLA-DRB1, HLA-DQB1, HLA-DQA1, IL13, IRF1, TLR1, TLR2, IRF4, HERC2, OCA2, SLC45A2

## Analysis objective

For each rosacea GWAS locus gene, a prespecified lesional-versus-healthy-control expression contrast in GSE65914, run separately for the erythematotelangiectatic, papulopustular and phymatous subtypes and for all rosacea pooled; then, across all samples, Spearman correlation of TLR1 with TLR2 expression and a test of whether the correlation differs between rosacea and control. Report every gene whether or not it reaches significance, and state which loci are immune versus pigmentation.

## Runtime contract

Use the Python execution facility immediately. The approved, preflighted
packages are Python's standard library plus `GEOparse`, `requests`, `numpy`,
`pandas`, `scipy`, `statsmodels`, and `yaml`. Do not import `biomni.tool.*`, and
do not substitute a metadata search for downloading and analysing the data.

Write every generated file beneath this exact directory:

`kb/hypotheses/Rosacea/gwas_loci_lesional_expression/openscientist_artifacts`

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
`kb/hypotheses/Rosacea/gwas_loci_lesional_expression/openscientist_artifacts/raw/`; they are local/recoverable inputs and will not be
committed.

Before declaring success, execute `analysis.py` once more into a clean replay
subdirectory while reusing `kb/hypotheses/Rosacea/gwas_loci_lesional_expression/openscientist_artifacts/raw` as `--cache-dir`; do not copy or
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

# Rosacea GWAS Susceptibility Loci and Lesional Skin Expression — Computational Replication (GSE65914)

## Summary

This run is a computational replication for the Disorder Mechanisms Knowledge Base, testing the hypothesis that **rosacea GWAS susceptibility loci act through altered expression in lesional skin, including a TLR1–TLR2 heterodimer axis**. The analysis retrieved the transcriptomic dataset **GSE65914** (Affymetrix GPL570 platform, RMA-normalized log2 intensities), classified samples into healthy controls and the three clinical rosacea subtypes, and ran a prespecified lesional-versus-healthy-control expression contrast for each of 13 target genes — separately for the erythematotelangiectatic (ETR), papulopustular (PPR) and phymatous (PhR) subtypes and for all rosacea pooled. The dataset comprised **20 healthy controls, 14 ETR, 12 PPR, and 12 PhR** lesional biopsies.

The central result is that the **immune** rosacea GWAS-locus genes are robustly and consistently upregulated in lesional skin across all subtypes and in the pooled contrast, whereas the **pigmentation** loci are not upregulated (and, where they change, they trend modestly downward). In the pooled rosacea-vs-control comparison (Welch t-tests, BH-FDR across 52 tests), TLR2 rose by log2FC = +1.91 (q ≈ 0, Cohen's d = 4.02), HLA-DRA by +1.45 (d = 2.76), IRF1 by +1.41, HLA-DRB1 by +1.10, TLR1 by +1.00, HLA-DQB1 by +1.16, HLA-DQA1 by +1.25, and BTNL2 by +0.19 — all with BH q < 0.05. In contrast, IL13 and pooled IRF4 were unchanged, and the pigmentation loci HERC2 (log2FC = −0.20), OCA2 (−0.56) and SLC45A2 (n.s.) were not upregulated. For the TLR1–TLR2 heterodimer axis, TLR1 and TLR2 were strongly co-induced and positively correlated across all samples (Spearman ρ = 0.69, p = 2.1 × 10⁻⁹), but the strength of that correlation did **not** differ between rosacea and control (rosacea ρ = 0.35 vs control ρ = 0.52; Fisher r-to-z p = 0.47).

The mechanistic reading is therefore nuanced: the "GWAS-loci-act-through-lesional-expression" hypothesis is **supported for the immune loci** — including a genuinely co-induced TLR1–TLR2 pair — but **not supported for the pigmentation loci**, and the TLR1–TLR2 coupling itself is co-elevated rather than rewired in disease. An independent literature cross-check (performed only after the primary artifact checksums were locked) corroborates the direction of the computed TLR2 upregulation. All required artifacts were generated, and a clean replay reproduced the primary tabular outputs byte-for-byte, so the replication is recorded as **SUCCEEDED**.

## Key Findings

### Finding 1 — Immune GWAS loci are upregulated in lesional skin; pigmentation loci are not

The prespecified contrast partitions the 13 target genes cleanly along the immune-versus-pigmentation axis. The immune-annotated loci (the HLA class II cluster **HLA-DRA, HLA-DRB1, HLA-DQB1, HLA-DQA1**; the **BTNL2** locus adjacent to the MHC; the interferon regulatory factors **IRF1** and **IRF4**; the innate immune receptors **TLR1** and **TLR2**; and the Th2 cytokine **IL13**) behave as a coherent block of disease-upregulated transcripts, whereas the pigmentation loci (**HERC2, OCA2, SLC45A2**) do not track disease upward at all.

In the pooled rosacea-versus-control comparison, the largest and most statistically decisive effects were seen for **TLR2** (log2FC = +1.91, q ≈ 0, Cohen's d = 4.02) and the antigen-presentation gene **HLA-DRA** (log2FC = +1.45, q ≈ 0, d = 2.76). The interferon regulator **IRF1** was elevated (log2FC = +1.41, q ≈ 0, d = 2.03), as were the MHC class II genes **HLA-DRB1** (+1.10, q = 1.9 × 10⁻⁹), **HLA-DQB1** (+1.16, q = 2.5 × 10⁻⁶), and **HLA-DQA1** (+1.25, q = 4.5 × 10⁻⁴). The innate receptor **TLR1** was also significantly up (+1.00, q = 1.3 × 10⁻⁸), and even the small **BTNL2** effect reached significance (+0.19, q = 1.2 × 10⁻²). These are large effect sizes — several with Cohen's d well above 2 — indicating the upregulation is not a marginal statistical artifact but a dominant feature of the lesional transcriptome.

Two immune genes did **not** move: **IL13** was not significantly changed in the pooled contrast (q = 0.54), and **IRF4** was not significant when pooled (q = 0.09). Their inclusion in the target list reflects their GWAS annotation rather than a guaranteed lesional signal, and reporting them as null is part of honoring the "report every gene whether or not it reaches significance" requirement.

The **pigmentation loci moved in the opposite direction from the hypothesis**. Rather than being upregulated in lesional skin, **HERC2** was modestly down (log2FC = −0.20, q = 2.7 × 10⁻⁵), **OCA2** was down (−0.56, q = 7.8 × 10⁻³), and **SLC45A2** was not significant (q = 0.09). This dissociation is the crux of the finding: the lesional-expression mechanism captures the immune arm of rosacea genetics but does not explain the pigmentation-associated GWAS signals, whose disease relevance — if any — is not mediated through increased lesional-skin transcription.

The full pooled rosacea-vs-control results, with the immune/pigmentation annotation the objective requested, are summarized below.

| Gene | Locus class | Pooled log2FC | BH q-value | Cohen's d | Direction / significance |
|---|---|---|---|---|---|
| TLR2 | Immune (innate) | +1.91 | ≈ 0 | 4.02 | Up, significant |
| HLA-DRA | Immune (MHC-II) | +1.45 | ≈ 0 | 2.76 | Up, significant |
| IRF1 | Immune (IFN) | +1.41 | ≈ 0 | 2.03 | Up, significant |
| HLA-DQA1 | Immune (MHC-II) | +1.25 | 4.5 × 10⁻⁴ | — | Up, significant |
| HLA-DQB1 | Immune (MHC-II) | +1.16 | 2.5 × 10⁻⁶ | — | Up, significant |
| HLA-DRB1 | Immune (MHC-II) | +1.10 | 1.9 × 10⁻⁹ | — | Up, significant |
| TLR1 | Immune (innate) | +1.00 | 1.3 × 10⁻⁸ | — | Up, significant |
| BTNL2 | Immune (MHC region) | +0.19 | 1.2 × 10⁻² | — | Up, significant |
| IRF4 | Immune (IFN) | n.s. | 0.09 | — | Not significant (pooled) |
| IL13 | Immune (Th2) | n.s. | 0.54 | — | Not significant |
| HERC2 | Pigmentation | −0.20 | 2.7 × 10⁻⁵ | — | Down, significant |
| OCA2 | Pigmentation | −0.56 | 7.8 × 10⁻³ | — | Down, significant |
| SLC45A2 | Pigmentation | n.s. | 0.09 | — | Not significant |

### Finding 2 — TLR1 and TLR2 are co-induced but their coupling is not rewired in disease

The hypothesis specifically invokes a **TLR1–TLR2 heterodimer axis**. Because TLR1 and TLR2 form a functional heterodimer that senses triacylated bacterial lipopeptides, a natural expectation is that if the axis is engaged in disease, the two transcripts should co-vary. Across all samples (controls plus all rosacea subtypes), TLR1 and TLR2 expression were strongly positively correlated (Spearman ρ = 0.69, p = 2.1 × 10⁻⁹), consistent with co-regulation of the heterodimer components.

However, when the correlation was computed separately within groups, the coupling was **not stronger in disease**: the within-rosacea correlation (ρ = 0.35) was, if anything, numerically lower than the within-control correlation (ρ = 0.52), and a Fisher r-to-z test found no significant difference between the two (p = 0.47). The most parsimonious interpretation is that both TLR1 and TLR2 are elevated in lesional skin (their means shift up together, driving the strong pooled correlation), but the *degree of coordination* between the two transcripts is a stable property of the tissue that is not remodeled by the disease state. In other words, the TLR1–TLR2 axis is turned **up**, not **rewired**.

### Finding 3 — Independent literature corroborates the computed TLR2 upregulation

After the primary artifact checksums were locked, an external literature check was performed as a separate, lineage-marked step. This cross-check found independent, non-transcriptomic evidence agreeing with the direction of the GSE65914 result. A case-control immunohistochemistry study of rosacea biopsies versus normal skin reported that TLR2 protein is higher in rosacea, and a mechanistic review of rosacea pathogenesis stated that increased TLR2 expression has been identified in rosacea skin. Because this check was performed *after* the primary outputs and checksums were finalized, it did not influence any method, sample, probe, threshold, or parameter choice — it is a post-hoc validation, not an input to the analysis.

## Mechanistic Model / Interpretation

The pattern of results supports a specific, testable mechanistic model in which the **immune** subset of rosacea GWAS loci exerts its disease effect (at least in part) through elevated transcription in lesional skin, converging on an innate-immune and antigen-presentation program, while the **pigmentation** loci do not participate through this route.

```
                 Rosacea GWAS loci
                        |
        +---------------+----------------+
        |                                |
   IMMUNE loci                     PIGMENTATION loci
   (MHC-II, IRFs, TLRs)            (HERC2, OCA2, SLC45A2)
        |                                |
  UP in lesional skin              NOT up in lesional skin
  (all subtypes + pooled)          (HERC2/OCA2 modestly DOWN)
        |                                |
  Innate immunity +                No lesional-expression
  antigen presentation             mechanism detected here
        |
   TLR1 --+-- co-induced (both UP)
   TLR2 --+   rho=0.69 across all samples
              but coupling UNCHANGED
              (rosacea rho=0.35 vs control rho=0.52,
               Fisher r-to-z p=0.47)
```

The immune block can be read as several coordinated modules that are all up in lesional skin:

| Module | Genes | Pooled log2FC (direction) | Interpretation |
|---|---|---|---|
| Innate sensing | TLR2, TLR1 | +1.91, +1.00 (up) | Heightened bacterial-lipopeptide sensing at the epidermal/dermal interface |
| Antigen presentation (MHC-II) | HLA-DRA, HLA-DQA1, HLA-DQB1, HLA-DRB1, BTNL2 | +1.45, +1.25, +1.16, +1.10, +0.19 (up) | Increased professional/atypical antigen presentation and adaptive priming |
| Interferon regulation | IRF1 (up); IRF4 (n.s. pooled) | +1.41 (up); n.s. | IFN-driven transcriptional amplification of the immune program |
| Th2 cytokine | IL13 | n.s. | No detectable lesional Th2 signal in this contrast |
| Pigmentation | HERC2, OCA2, SLC45A2 | −0.20, −0.56, n.s. | Not upregulated; mechanism not via lesional expression |

The TLR1–TLR2 result refines the heterodimer hypothesis. The two receptors are genuinely co-induced — consistent with the idea that a TLR1/TLR2-sensed innate stimulus (e.g., triacylated lipopeptides from cutaneous microbes) is amplified in rosacea skin — but the analysis distinguishes **co-elevation** from **altered coupling**. Because the within-group correlations are statistically indistinguishable between rosacea and control, the data favor a model where disease raises the setpoint of both receptors in parallel without changing the tightness of their mutual regulation. This is an important mechanistic subtlety: therapeutic strategies aimed at "decoupling" TLR1 from TLR2 would not obviously find a disease-specific coupling defect to target, whereas strategies aimed at damping the overall elevation of the axis would.

Overall, the hypothesis "**GWAS loci act through altered expression in lesional skin, including a TLR1–TLR2 heterodimer axis**" is **partially supported**: strongly supported for the immune loci and for the existence of a co-induced TLR1–TLR2 axis, but not supported for the pigmentation loci and not supported for a disease-specific rewiring of TLR1–TLR2 coupling.

## Evidence Base

The primary evidence is the transcriptomic analysis of GSE65914 itself (see Findings 1–2). The literature below was consulted only after the primary artifact checksums were locked and serves as an independent, lineage-marked cross-check of the direction of the computed effects.

| Paper (PMID) | Type | How it relates to this analysis |
|---|---|---|
| [PMID: 29330632](https://pubmed.ncbi.nlm.nih.gov/29330632/) | Case-control IHC | Confirms TLR2 elevation in rosacea skin vs controls |
| [PMID: 25047092](https://pubmed.ncbi.nlm.nih.gov/25047092/) | Mechanistic review | States increased TLR2 expression is identified in rosacea skin |
| [PMID: 34352786](https://pubmed.ncbi.nlm.nih.gov/34352786/) | Mechanistic (keratinocytes) | Places TLR2 activation upstream of rosacea-relevant inflammation |

**Innate immunity in rosacea (case-control immunohistochemistry).** *Innate immunity in rosacea. Langerhans cells, plasmacytoid dendritic cells, Toll-like receptors and inducible nitric oxide synthase (iNOS) expression in skin specimens: case-control study* — [PMID: 29330632](https://pubmed.ncbi.nlm.nih.gov/29330632/). This study reports that "*Expression of TLR2, TLR4 and iNOS was higher in rosacea samples than in normal skin controls.*" This independent, protein-level case-control observation matches the direction of the computed transcriptomic contrast (TLR2 pooled rosacea-vs-control log2FC = +1.91, q ≈ 0, Cohen's d = 4.02), reinforcing that the GSE65914 signal reflects a real biological elevation rather than a normalization or probe artifact.

**Endoplasmic reticulum stress in rosacea (review).** *Endoplasmic reticulum stress: key promoter of rosacea pathogenesis* — [PMID: 25047092](https://pubmed.ncbi.nlm.nih.gov/25047092/). The review states that "*increased expression of toll-like receptor 2 (TLR2) has been identified in rosacea skin supporting the participation of the innate immune system.*" This corroborates the direction of the computed TLR2 upregulation and situates it within the broader innate-immune framing of rosacea pathogenesis.

**AhR regulation of TLR2-driven inflammation in keratinocytes.** *AhR Regulates Peptidoglycan-Induced Inflammatory Gene Expression in Human Keratinocytes* — [PMID: 34352786](https://pubmed.ncbi.nlm.nih.gov/34352786/). This mechanistic study notes that "excessive TLR2 activation can lead to inappropriate inflammation, which contributes to skin conditions such as rosacea," and shows AhR depletion increases TLR2 expression, suggesting negative-feedback control of TLR2. It provides upstream mechanistic context for why elevated TLR2 (as observed here) would be pathogenic and points to a regulatory node (AhR) whose perturbation could produce the observed elevation.

Together, the three papers consistently support the direction of the computed TLR2 result; none contradicts it. They do not directly test the pigmentation-locus dissociation or the TLR1–TLR2 coupling-invariance finding, which remain novel contributions of this replication.

## Limitations and Knowledge Gaps

- **Single dataset, single platform.** All conclusions rest on GSE65914 (Affymetrix GPL570). Cross-platform / cross-cohort replication (e.g., RNA-seq cohorts) was outside the dataset scope of this replication and would strengthen generalizability.
- **Expression is not causation.** The analysis demonstrates that immune GWAS-locus genes are upregulated in lesional skin, but it does not establish that the disease-associated *alleles* drive that expression change. An eQTL/colocalization analysis would be required to link the GWAS signal mechanistically to the lesional transcript, which this microarray-only design cannot do.
- **Bulk tissue, no cell-type resolution.** GSE65914 is bulk skin. The upregulation of MHC-II and TLR genes could reflect increased immune-cell infiltration rather than per-cell transcriptional change. Single-cell or deconvolution approaches are needed to separate composition from regulation.
- **Pigmentation-locus interpretation is bounded.** The modest downregulation of HERC2/OCA2 in lesional skin rules out a lesional-upregulation mechanism but does not exclude other routes (e.g., systemic, developmental, or expression in non-lesional contexts). The null/negative pigmentation result should be read as "no support for this specific mechanism," not "no role in rosacea."
- **Correlation-difference test is power-limited.** The Fisher r-to-z comparison of TLR1–TLR2 coupling (p = 0.47) is a null result in modestly sized groups; absence of a detectable difference is not proof of identical coupling. A larger cohort could reveal a subtle change.
- **Gene-to-probe aggregation and multiple testing.** Results depend on the probe-to-gene mapping and BH-FDR correction (52 tests) documented in `methods.md`; alternative aggregation rules could shift borderline calls (e.g., BTNL2, IRF4, SLC45A2).

## Proposed Follow-up Experiments / Actions

1. **Cross-cohort replication.** Repeat the identical prespecified contrast in an independent rosacea transcriptomic cohort (ideally RNA-seq) to confirm the immune-up / pigmentation-not-up dissociation and the TLR1–TLR2 co-induction.
2. **eQTL / colocalization.** Test whether rosacea GWAS lead variants colocalize with skin eQTLs for the immune target genes (particularly the MHC-II cluster, IRF1, TLR2), directly linking genotype to the observed lesional expression change.
3. **Single-cell / deconvolution.** Apply cell-type deconvolution or scRNA-seq to determine whether MHC-II and TLR upregulation reflects infiltration versus intrinsic keratinocyte/fibroblast regulation.
4. **Subtype-resolved modeling.** Formally test subtype × gene interaction (ETR vs PPR vs PhR) to identify whether any target gene is subtype-specific, complementing the per-subtype contrasts already computed.
5. **Mechanistic follow-up on TLR2 regulation.** Given the AhR–TLR2 negative-feedback link ([PMID: 34352786](https://pubmed.ncbi.nlm.nih.gov/34352786/)), test whether AhR-pathway activity is reduced in lesional skin, which could explain the observed TLR2 elevation.
6. **Functional TLR1/TLR2 heterodimer assay.** Because the transcripts are co-elevated but not rewired, directly assay heterodimer signaling capacity (e.g., response to Pam3CSK4) in rosacea vs control keratinocytes to test whether elevated expression translates into elevated function.

## Replication and Artifact Provenance

All required artifacts were produced beneath `kb/hypotheses/Rosacea/gwas_loci_lesional_expression/openscientist_artifacts/`, including `MANIFEST.yaml` (`status: SUCCEEDED`, `fallback_used: false`, `direct_analysis_completed: true`), `analysis.py` (standalone deterministic analysis with `--output-dir`/`--cache-dir`), `environment.txt`, `methods.md`, `samples.csv`, `gene_results.csv`, `tlr_correlation.csv`, and `comparison.md`. The analysis was re-executed into a clean `replay/` subdirectory reusing the existing `raw/` cache; the replayed `samples.csv` and `gene_results.csv` were verified byte-identical to the primary outputs, and the manifest records the replay command, `verified: true`, byte-identity mapping, and per-asset SHA-256 checksums and byte counts. The literature cross-check was performed only after the primary checksums were locked and is marked as a separate lineage step, so no prior-provider or post-hoc result influenced any method, sample, probe, threshold, or parameter choice.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist comparison](openscientist_artifacts/comparison.md)
- [OpenScientist gene results](openscientist_artifacts/gene_results.csv)
- [OpenScientist methods](openscientist_artifacts/methods.md)
- [OpenScientist gene results](openscientist_artifacts/replay/gene_results.csv)
- [OpenScientist samples](openscientist_artifacts/replay/samples.csv)
- [OpenScientist tlr correlation](openscientist_artifacts/replay/tlr_correlation.csv)
- [OpenScientist samples](openscientist_artifacts/samples.csv)
- [OpenScientist tlr correlation](openscientist_artifacts/tlr_correlation.csv)

## Term Validation

No ontology term identifiers were found in this report.