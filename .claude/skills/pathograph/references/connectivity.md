# Phenotype connectivity

`check-causal-targets` checks that declared targets resolve. It cannot detect a
phenotype nobody wrote an edge to. An entry may pass it with every phenotype
disconnected. Fixing one dangling target does not repair all absent edges.

```bash
just list-disconnected-phenotypes kb/disorders/MyDisease.yaml
just list-disconnected-phenotypes --format tsv
just list-disconnected-phenotypes --zero-only
just compliance-connectivity
just compliance-connectivity --list-unconnected
```

Both reports use `dismech.qc_plugins.causal_inlink_coverage`. The first is the
per-entry curation worklist; the second combines phenotype inlinks, gene
outlinks, and the aggregate compliance ratchet. Do not recompute a second metric.

## What counts as explaining a phenotype

The causal predicate set is `qc_plugins.CAUSAL_PREDICATES`. Treatment links say
that a phenotype is addressed; `phenotypes[].reports_on` carries an observational
readout; environmental `PREDISPOSES` and `MODULATES` links are noncommittal.
None of these counts as a causal explanation. Environmental `TRIGGERS` and
`EXACERBATES` do count. Subtype scoping does not create a connection.

The worklist distinguishes unexplained phenotypes by their existing attachment:
`ISOLATED`, `TREATED`, `READOUT`, `NONCAUSAL_INBOUND`, or `SEQUELA_SOURCE`.
These categories distinguish an entirely disconnected node from one the graph
knows about for another purpose. All remain causally unexplained by this metric.

## Interpret the floor correctly

`just compliance-connectivity` gates the **KB-wide aggregate** using
`min_compliance` in `conf/qc_config.yaml`. It is not a per-disease requirement.
Read the current configuration and report for the floor and counts, rather than
copying historical figures. Never lower the floor or set it to null to clear a
failure; the test `test_committed_causal_inlink_floor_is_set_and_never_lowered`
protects the ratchet. Sustained erosion calls for real curation over the worklist,
not arbitrary edges in whichever PR happened to fail.

`just list-disconnected-phenotypes` is report-only by default. Its `--strict`
and `--fail-under` options allow a deliberately chosen subset audit; they do not
change the corpus-wide policy. Genetic `mechanism_outlink` coverage is advisory
in the same compliance recipe (`--genes-fail-under` for an explicit audit).

## Curate the missing claim

Read the source for each candidate mechanism-to-phenotype edge. Record what is
supported and preserve uncertainty. A laboratory readout or a feature with an
unknown mechanism may legitimately remain unexplained. The report exists to
find curation work, not to make every node acquire an arrow.

Background: issues #11935 and #11934 motivated the per-entry worklist; the
Schizophrenia example showed why resolving one dangling target alone left six
phenotypes unwired. Use current entry content for present-day counts.
