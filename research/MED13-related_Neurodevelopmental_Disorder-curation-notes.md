# MED13-related neurodevelopmental disorder curation notes

Date: 2026-04-12
Issue: https://github.com/monarch-initiative/dismech/issues/1140

## Bottom line

`MED13-related neurodevelopmental disorder` should become both a disorder entry and a project note.

The disorder entry is justified now because the local repo triage already flags `MED13` as a `CRITICAL` missing anchor, the 2018 cohort defines a recognizable syndrome, later cases expand but do not dissolve that syndrome, and the 2026 cortical-neuron study gives a credible mechanism trunk for a first pathophysiology model.

The project note is still worth keeping because there is a real modeling decision to preserve: G2P points to the MED13-specific term `MONDO:0032485`, while the local ClinGen validity cache is attached to the broader umbrella `MONDO:0100038` `complex neurodevelopmental disorder`. That split should be documented explicitly rather than rediscovered later from raw spreadsheets.

## Why a disorder entry is warranted

- The local G2P triage row says `ADD_FIRST_GENE_DISEASE_ANCHOR` for `MED13`.
- The disease signal is not based on one isolated patient; it has a syndrome-defining cohort plus later phenotype-expansion reports.
- The mechanistic center is coherent enough for dismech: Mediator kinase-module dysfunction leading to developmental transcriptional dysregulation in cortical neurons.
- A conservative first entry can stay focused on developmental delay, intellectual disability, speech impairment, hypotonia, and behavioral or autism-spectrum features without overcommitting to rare severe presentations.

## Why a project note is also warranted

- The anchor choice needs explanation: specific MED13 disorder term versus broader ClinGen umbrella term.
- The first entry should state clearly that cardiac, hearing, and mitochondrial findings are spectrum extensions, not the primary mechanistic trunk.
- Missense-versus-truncating mechanism questions remain open enough that future curators will benefit from a preserved decision memo.

## Recommended first-entry scope

- Root the disorder at `MONDO:0032485` and gene `MED13` (`hgnc:22474`).
- Use a mechanism chain centered on:
  - Mediator kinase-module dysfunction
  - transcriptional dysregulation
  - impaired cortical neuron migration and projection
  - neurodevelopmental phenotypes
- Keep secondary multisystem findings conservative unless directly evidenced at the disease level.

## References to carry forward

- `research/MED13-related_Neurodevelopmental_Disorder-deep-research-codex.md`
- `docs/research/g2p_all_genes_row_triage_2026_03_28.tsv`
- `docs/research/g2p_all_genes_gene_summary_2026_03_28.tsv`
- `cache/clingen/gene_validity.csv`
