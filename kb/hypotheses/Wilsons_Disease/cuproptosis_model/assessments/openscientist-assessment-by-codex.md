# Codex assessment of the OpenScientist report

## Verdict

**Weakly supported and unresolved.** Cuproptosis is a real, experimentally
defined mechanism, and one ATP7B-null mouse/HepG2 study makes it a credible
Wilson disease lead. The committed evidence does not yet demonstrate the
distinctive mechanism in human Wilson tissue—or completely even in the cited
Wilson models.

## Why the grade is lower than the provider's

The foundational study defines cuproptosis by copper binding lipoylated
TCA-cycle proteins, lipoylated-protein aggregation, iron-sulfur-protein loss,
proteotoxic stress, and respiration dependence (PMID:35298263). The
Wilson-specific paper reports selected protein abundance changes, copper
injury, ionophore enhancement, chelator rescue, and hub-gene knockdowns
(PMID:41230834). Those findings are suggestive but the abstract does not report
the defining aggregation and iron-sulfur-loss sequence or a pathway-specific
rescue.

The report's more elaborate synthesis is not demonstrated:

- GSE125637 is a four-versus-four, single-age mouse liver comparison from a
  metabolic study.
- GSE197406 contains seven transplant livers from acute or chronic liver
  failure and eight resection controls—not a staged longitudinal series.
- A liver-cancer study of ferroptosis inducers and FDX1 degradation
  (PMID:37277863) supplies a possible experiment, not a resolution of Wilson
  mRNA/protein discordance.
- Copper-DLAT binding in kidney fibrosis (PMID:39120696), mitochondrial-copper
  removal, and exchangeable-copper severity associations are compatible with
  multiple copper-toxicity mechanisms and are not cuproptosis-specific.

The report is right to retain two decisive gaps: no human Wilson liver evidence
of lipoylated-protein aggregation and no neurological Wilson evidence.

## Dataset and execution audit

The report claims direct analyses of GSE197406 and GSE125637, but its bundle has
no input manifest, sample table, code, environment, probe mapping, result table,
or execution log. The structured assessment therefore records both computations
as `REPORTED_ONLY` / `UNVERIFIABLE`, not successful analyses.

A separate checksum-pinned reanalysis confirmed the deposited samples and
platforms and exposed material discrepancies:

- GSE125637 is an Affymetrix Mouse Genome 430 2.0 microarray (GPL1261), not the
  “mouse RNA-seq” described by the report.
- In GSE197406, both officially annotated DLD probes decrease and all three DLAT
  probes increase. The report gives the opposite direction for each gene. Some
  GLS and PDHA1 numbers resemble individual probes, but no selection rule is
  documented.
- In the four untreated Atp7b-null versus four wild-type mouse samples, Fdx1 is
  lower (Welch p=0.0426). The report's p≈0.039 comes from an undisclosed
  equal-variance test. Neither gene-level aggregation nor any annotated Gls
  probe approaches the reported p=0.006. Dlst is positive at gene level, and
  its highest-expression probe is strongly upregulated rather than downregulated.
- Neither dataset is longitudinal, and GSE197406 has important clinical
  confounding: the controls are resection specimens and differ substantially in
  age from the Wilson explant cohort.

These checks do not refute the cuproptosis hypothesis. They do mean the report's
transcriptomic values and stage narrative cannot be treated as independently
reproducible evidence.

## Additional curation guardrails

The proposed GO mappings include errors. GO:0018169 is ribosomal
S6-glutamic-acid ligase activity, not protein lipoylation (GO:0009249), and
GO:0015037 is not a usable FDX1 reductase mapping in the repository's GO
release. The claimed 96-paper corpus is also not auditable from the 20 unique
PMIDs exposed in the committed artifacts.

Keep the hypothesis **EMERGING** and phrase the existing model data as
“compatible with” or “suggestive of” cuproptosis. Do not promote the proposed
stage model, feedback loop, ontology terms, or human relevance without the
normal evidence workflow.

The authoritative structured dispositions are in
`openscientist-assessment-by-codex.yaml`.
