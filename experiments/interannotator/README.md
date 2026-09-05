# Inter-annotator consistency studies

How much of a dismech entry is determined by the evidence, and how much by the
curator? Each study here curates one disease twice, independently, and measures
where the two versions agree.

## Comparisons

| Study | Disease | Curators | Phenotype agreement (strict / subsumption-aware) | Band agreement |
|---|---|---|---|---|
| [`FG_Syndrome_1/`](FG_Syndrome_1/) | FG syndrome 1 (`MONDO:0010590`) | A: merged [#7254](https://github.com/monarch-initiative/dismech/pull/7254) · B: independent | 0.484 / 0.766–0.812 | 25/31 = 0.806 |
| [`Rienhoff_Syndrome/`](Rienhoff_Syndrome/) | Rienhoff syndrome (`MONDO:0014262`) | A: merged [#7345](https://github.com/monarch-initiative/dismech/pull/7345) post-#7228 · B: closed [#7322](https://github.com/monarch-initiative/dismech/pull/7322) (MAXO→NCIT remapped for metrics) | 0.531 / 0.840–0.833 | 14/17 = 0.824 |

## Layout

`compare.py` is shared tooling and lives at this level. Everything else is
per-comparison and lives in a subdirectory named for the disease slug (matching
its `kb/disorders/` stem):

```
interannotator/
├── README.md                     this index
├── compare.py                    shared metric script
└── <Disease_Slug>/
    ├── FINDINGS.md               the report
    ├── metrics.txt               compare.py output, as run
    ├── <Disease_Slug>.curator-A.<provenance>.yaml
    └── <Disease_Slug>.curator-B.<provenance>.yaml
```

Snapshots keep the disease in the filename even though the folder repeats it, so
a YAML that gets downloaded or attached somewhere still identifies itself. The
`<provenance>` suffix records where the version came from (`merged-pr7254`,
`independent`, …). If the same disease is studied more than once, suffix the
folder rather than overwriting: `<Disease_Slug>-run2/`.

## Running a comparison

```bash
uv run python experiments/interannotator/compare.py \
  experiments/interannotator/<Disease_Slug>/<...>.curator-A.<...>.yaml \
  experiments/interannotator/<Disease_Slug>/<...>.curator-B.<...>.yaml \
  | tee experiments/interannotator/<Disease_Slug>/metrics.txt
```

Subsumption-aware phenotype matching shells out to OAK per term and takes a
couple of minutes; `--no-ontology` skips it and reports strict term identity only.

## Adding a new study

1. **Curate independently.** The second curator must not open the first entry, or
   the first curator's deep-research report, until their own version passes schema,
   term, and reference validation. Partial independence is fine — but record
   exactly what leaked, and which metrics it invalidates. Every study so far has
   had some leakage.
2. **Snapshot both versions verbatim**, and record the commit each came from.
   Verify the KB-derived snapshot is byte-identical to its source (`diff -q`).
3. **Run `compare.py`**, saving output to `metrics.txt`. Quote its numbers in the
   report rather than recomputing them by hand.
4. **Write `FINDINGS.md`.** State the contamination limits before the results, not
   after. Separate *defects* (violations of the project's own evidence rules) from
   *differences* (defensible curator choices) — the two warrant different follow-up.
5. **Update the table above.**

## Notes carried across studies

Findings that generalise beyond a single disease. Add to this as studies accumulate.

- **Strict term-identity Jaccard understates agreement on this KB** and should not
  be reported alone. In the FG syndrome 1 study it scored 0.484 where
  subsumption-aware agreement was 0.766–0.812; the gap is entirely
  parent/child pairs (`Hypotonia`↔`Neonatal hypotonia`) and roll-up-vs-split
  choices (`Abnormality of the eye` ↔ four specific ocular terms).
- **Agreement tracks the source, not the curator.** Divergence concentrates where
  the literature says "were frequent" without a count, and collapses wherever a
  denominator is stated.
- **A coarse action vocabulary hides disagreement.** Agreement measured at the
  ontology-term level can overstate agreement about the underlying content, because
  two curators can bind the same catch-all term to different things. In the FG
  syndrome 1 study, 7 shared NCIT treatment ids reduced to 4 genuine agreements once
  the names behind them were read: `NCIT:C15747` Supportive Care absorbed both bowel
  management and audiology surveillance, and `NCIT:C15302` Physical Therapy was a
  pure collision. Report id-level and content-level agreement separately; the former
  alone is not a measure of curator agreement.
- **Independent re-curation and code review catch different things.** Review
  checks whether a snippet supports its claim; it is far less likely to notice
  that a better, more specific source exists and was not cited. That class of
  defect survived three review rounds and an approval in the FG syndrome 1 study.

- **Shared mechanism modules inflate pathograph agreement.** When both curators
  independently `conforms_to` the same module (Rienhoff → `aortopathy_tgfbeta_dysregulation`),
  terminal node names and the aortopathy chain converge for institutional reasons, not
  free invention. Score module-scaffolded arms separately from disease-specific nodes.
- **Accidental dual curation can be a cleaner natural experiment than a planned re-curation.**
  Rienhoff's two same-day PRs (#7322 and #7345) show no evidence of cross-reading and
  better independence than FG, where curator B had read A's PR description. Still record
  shared scaffolding (GeneReviews, modules) honestly.
- **Ontology-era mismatch needs an explicit remap step.** B was MAXO-era; A was post-#7228
  NCIT. Keep the original snapshot, mechanically remap with the project map for id-level
  metrics, and never compute treatment Jaccard across mixed vocabularies.
