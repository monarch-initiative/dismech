# Directional ICD enrichment

> The [subsequent Boomer batch](../../runs/pending/README.md) has now attempted
> every new and stale input. The preservation and `STALE_INPUT` counts below
> describe the import stage; all 177 stale inputs subsequently timed out in
> full joint searches and now have explicitly provisional current outputs.

The first Mendelian import on 2026-09-08 enriched **1,000 inputs** with **1,271
mapping hypotheses**. Only entries with `category: Mendelian` were changed.
The [initial audit](../README.md) remains available as a historical snapshot.

| Coverage among 1,550 grounded Mendelian entries | Before | After |
|---|---:|---:|
| Any ICD term in the input | 96 (6.2%) | 1,005 (64.8%) |
| WHO ICD-10 | 0 | 999 (64.5%) |
| ICD10CM | 96 (6.2%) | 97 (6.3%) |
| No ICD term in the input | 1,454 | 545 |

WHO and CM coverage overlap. Counts include codes reached through grounded
subtypes, so they exceed the initial parent-only ORDO coverage. Four explicit
direct ICD10CM assertions were imported: dystrophic epidermolysis bullosa,
epidermolysis bullosa simplex, MELAS syndrome, and familial hemiplegic migraine.

## Mapping semantics and review

Each ORDO node already included in a Mendelian input is queried for ICD mapping
assertions in its local OAK snapshot. Both semantic-sql `object` and `value`
columns are read. Obsolete ORDO nodes are excluded. WHO `ICD-10:` targets are
normalized to `ICD10:`; **ICD10CM is never aliased to WHO ICD10**.

| Source assertion S→T | Boomer hypothesis | Prior |
|---|---|---:|
| `skos:exactMatch` | S equivalent to T | 0.95 |
| `skos:broadMatch` | S proper subclass of T | 0.90 |
| `skos:narrowMatch` | T proper subclass of S | 0.90 |

These are explicit modeling priors in [config.yaml](../config.yaml), not measured
probabilities. Each mapping is one retractable hypothesis; broad/narrow mappings
are not expanded into high-probability identity claims. Duplicate source paths to
the same logical fact do not multiply its prior. Existing probabilities remain
unchanged. The added hypotheses comprise 1,217 broad, 47 exact, and seven narrow
assertions, including subtype mappings.

Hard target hierarchy edges come only from each classification's own hierarchy.
Code-string prefixes are not used to infer ancestry. Namespace groups prevent
distinct codes within a vocabulary from becoming equivalent; they do not prohibit
subclass relations. The WHO and CM namespaces have separate groups and no inferred
crosswalk between them.

**Twenty assertions remain for review**, explicitly listed in
[import-decisions.tsv](../import-decisions.tsv):

* Seven direct mappings cite ORPHA for an ICD10CM target, requiring verification
  of vocabulary identity and direction. These include the reversed-direction
  concerns for Fabry, Alagille, and Angelman. Their curated YAMLs were not changed.
* Three direct `closeMatch` assertions have no supported logical translation in
  this importer. Close similarity is not promoted to equivalence.
* One direct mapping has unspecified provenance.
* Nine ORDO mapping assertions target qualified or unrepresented WHO codes:
  `E72.0+`, `E85.4+`, `I68.0*`, `N16.3*`, `F72.8`, and `N04.1`.
  Qualifiers are retained for review, not stripped to manufacture a class match.

## Labels, sources, and configuration

WHO labels and superclass links come from the official
[2019 ClaML download, including COVID-19 updates](https://icdcdn.who.int/icd10/index.html).
`prepare_icd10.py` verifies the pinned ZIP, extracts Class preferred labels and
SuperClass links into a deterministic local OBO projection, and verifies that
projection's checksum. OAK's Pronto adapter reads the resulting 11,539 classes.
Inclusions, exclusions, coding instructions and optional modifiers are not
projected as subclass axioms. This is a hierarchy analysis, not a coding engine.

Existing local source names such as `sqlite:obo:icd10cm` are reused from
`conf/oak_config.yaml`. Its OLS validation adapters do not replace the local
graph snapshots needed for Boomer. WHO preparation and priors are analysis-local;
the disease schema and validator ontology set have not been extended.

[import-sources.json](../import-sources.json) records the WHO archive and OBO
checksums, priors, and ORDO/ICD10CM snapshot hashes. The source dates differ and
the ORDO snapshot is a MONDO source extract; separate mapping paths are not
assumed to be statistically independent evidence.

## Regeneration and saved results

```bash
cd analyses
just boomer-prepare-icd10      # explicit pinned WHO download, only needed for setup
just boomer-enrich-icd10       # additive migration of existing Mendelian inputs
just boomer-icd10-coverage     # regenerate current coverage
```

The migration validates all selected inputs against Boomer's model before writing
any changes. It leaves existing assertions, labels, and probabilities unchanged.
The initial 1,000 YAML diffs contain **only additions**, with no removed lines.
Repeated migration against unchanged sources produces identical bytes.

At the import stage, all 371 saved solutions remained byte-identical. Of these,
**177 had changed inputs**: their index status was `STALE_INPUT`, `n_retracted`
was `NA`, and their
README starts with a warning that the retained result applies to the old input.
[updates.json](../updates.json) records before/after input hashes, previous index
values, and preserved solution hashes. The other 823 changed inputs remain
`NOT_RUN`. No new solver verdicts are asserted by this migration.

The additive command rejects changed source snapshots or further changes to a
previously migrated input. For source refreshes that remove or change assertions,
regenerate inputs fully with `build_analyses.py --with-icd10`; the ordinary
`boomer-disorders`, `boomer-expand-mendelian`, and `boomer-one` recipes now enable
this option. Full input regeneration can be reviewed in a separate output folder
with `--inputs-only`; it refuses to leave old solutions beside replaced inputs.
Archive or reconcile migration reports before applying a new migration.

`just boomer-one <slug>` explicitly regenerates and solves that entry and updates
its index row while preserving the other rows. Future solver reports count
rejected high-prior directional mappings as well as equivalences. Solving has a
timeout; reducing the `-C` clique limit can discard interacting hypotheses and is
not a semantics-preserving performance fix.

## Current data

* [coverage.tsv](coverage.tsv): all 1,728 indexed entries. Filter `mendelian=1`
  and empty `boomer_icd10_terms` for the 545 still lacking ICD in their inputs.
* [mappings.tsv](mappings.tsv): parent mapping routes available in source data,
  including assertions awaiting review; this is not the importer acceptance list.
* [missing-mendelian.txt](missing-mendelian.txt): 538 entries lacking ICD in both
  their current input and all audited parent mapping routes. The other seven
  lacking ICD in their input have parent mapping candidates in the audit.
* [summary.json](summary.json): current counts with separate WHO and CM totals.

The 12 Mendelian entries without primary MONDO grounding remain outside the
1,550-entry denominator. Missing coverage is not proof that no ICD code exists.
