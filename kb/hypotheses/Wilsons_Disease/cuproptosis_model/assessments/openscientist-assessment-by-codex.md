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
