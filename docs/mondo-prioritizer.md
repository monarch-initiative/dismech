# MONDO Prioritizer

!!! note "No longer the curation queue"

    The outstanding curation queue is now [`stubs/`](curation-stubs.md) — one
    YAML file per disease, edited by pull request. The prioritizer's ranked
    output is kept as a *browsable pool* for discovering MONDO concepts to
    nominate into that queue, but it is no longer the answer to "what should I
    curate next". Issue
    [#8969](https://github.com/monarch-initiative/dismech/issues/8969) records
    why: every cheap ontology feature the score can use (child count, synonym
    count, aggregator tags) correlates with *being a grouping* rather than with
    *being worth curating*, so the head of the ranking filled with umbrella
    terms no matter how the weights were tuned.

The MONDO prioritizer builds a candidate pool from MONDO disease rows rather than
from ad hoc checklist issues. It scores candidate diseases against local DisMech
coverage, then applies a small set of explicit specificity heuristics to suggest
whether a term should be curated as a root, lumped into a parent, or dropped.

The goal is practical queue construction:

- reward missing diseases that already have useful MONDO metadata
- reward external evidence signals when they are available in the input rows
- penalize terms that are already curated, obsolete, or likely bad roots
- make every score component inspectable and easy to retune

## CLI

```bash
uv run dismech-mondo-prioritize \
  examples/mondo_prioritizer_candidates.tsv \
  --format table
```

Example with a custom config and TSV output:

```bash
uv run dismech-mondo-prioritize \
  examples/mondo_prioritizer_candidates.tsv \
  --config examples/mondo_prioritizer_config.yaml \
  --format tsv \
  --output /tmp/mondo_priority.tsv
```

Generate the static website dashboard from the same scoring logic:

```bash
just gen-priority-dashboard
```

This writes `dashboard/priority.html` and `dashboard/priority.json`, and patches
`dashboard/index.html` with a link when that dashboard index already exists.

For a local-only run across all MONDO disease descendants currently missing from
`kb/disorders/`, use:

```bash
just gen-priority-dashboard-all-mondo
```

That flow first exports candidate rows from the local MONDO sqlite database at
`~/.data/oaklib/mondo.db`, then writes the resulting dashboard under
`tmp/priority-dashboard-all-mondo/`. The `tmp/` tree is gitignored so these
large artifacts stay out of GitHub by default.

## Candidate Export Sidecar

`scripts/export_mondo_priority_candidates.py --kb-dir kb/disorders` **drops**
already-curated roots before writing the TSV, so the exported rows are the
remaining queue only. That leaves the export unable to answer "how many disease
terms are already covered?" — a dropped row has no trace in the file, and a TSV
has nowhere to record one (a comment line would break `csv.DictReader`).

The exporter therefore writes a sidecar next to every export, named for it —
`candidates.tsv` → `candidates.meta.json`:

```json
{
  "disease_root_id": "MONDO:0000001",
  "kb_dir": "kb/disorders",
  "total_descendants": 27438,
  "excluded_curated": 2932,
  "exported_rows": 24506
}
```

The dashboard reads `excluded_curated` and counts it in **both** halves of the
coverage fraction: those terms are curated, and they were candidates. Without it
the headline reported `already_curated: 0` / `coverage_percent: 0.0` no matter
how much of MONDO the KB covered (issue #7425). A candidate file with no sidecar
— a hand-built TSV, or one exported without `--kb-dir` — is read as "nothing was
excluded", which is the correct reading for both.

## Expected Input

The prioritizer accepts `tsv`, `csv`, `json`, or `jsonl` candidate rows. The
only required fields are:

- `mondo_id`
- `label`

Optional fields become weighted signals when present:

- `definition`
- `synonyms`
- `parents`
- `xrefs`
- `child_count`
- `clingen_definitive_count`
- `clingen_strong_count`
- `subset_match_count`
- `orphanet_match_count`
- `is_obsolete`

Field aliases such as `id`, `name`, `disease_mondo`, and `term_label` are also
accepted. Multi-valued columns can use `;` or `|`.

## Scoring Dimensions

Default weights live in `conf/mondo_prioritizer.yaml`.

By default the scorer uses:

- `missing_from_dismech`: positive base reward for uncurated roots
- `has_definition`: reward for a candidate that already has a MONDO definition
- `synonym_count`, `xref_count`: small metadata completeness rewards
- `clingen_definitive_count`, `clingen_strong_count`: optional evidence boosts when those counts are supplied in the MONDO candidate export
- `subset_match_count`, `orphanet_match_count`: optional prioritization boosts when the upstream pipeline already tagged the disease as belonging to an important slice
- `already_curated_penalty`, `obsolete_penalty`: strong penalties for terms we should not queue

Count-based features are capped so a row with very large synonym or xref counts
does not dominate the queue.

## Specificity Heuristics

The prioritizer also emits a `specificity_bucket` and `recommended_action`.

Local MONDO coverage includes each entry's primary `disease_term`, its declared
`has_subtypes` terms, and `mappings.mondo_mappings` whose predicate is
`skos:exactMatch` or `skos:narrowMatch`. A `skos:broadMatch`, `skos:closeMatch`,
or `skos:relatedMatch` remains useful as a cross-reference, but does not mean the
mapped MONDO concept has itself been curated and therefore does not retire that
concept from the queue.

Default buckets are:

- `already_curated`
- `obsolete`
- `grouping_term`
- `subtype_series`
- `broad_parent`
- `over_specific_leaf`
- `root_candidate`

The default heuristic rules are intentionally conservative:

- `grouping_term`: regex match on high-confidence phrases such as `susceptibility`, `predisposition`, or `obsolete`
- `subtype_series`: label matches a configurable subtype suffix pattern such as `long QT syndrome 1` or `Noonan syndrome 1`, and the same stem appears multiple times
- `broad_parent`: candidate has many children and is not already classified as a subtype series or grouping term
- `over_specific_leaf`: leaf term with a long conjunction-heavy label, which is a useful review flag for phenotype-enumerating leaves

This does not try to solve lump-vs-split perfectly. It surfaces explicit review
recommendations such as `CURATE_ROOT_WITH_SUBTYPES`, `LUMP_INTO_PARENT`, and
`REVIEW_AGAINST_PARENT` so the queue is defensible and inspectable.

## Example Interpretation

With the bundled example candidates:

- `long QT syndrome` scores as a missing broad parent and is recommended as `CURATE_ROOT_WITH_SUBTYPES`
- `long QT syndrome 1` and `long QT syndrome 3` score as `LUMP_INTO_PARENT`
- `autism, susceptibility to, X-linked 3` is flagged as a `grouping_term`
- `Noonan syndrome` is heavily penalized as `ALREADY_CURATED`
- `obsolete unclassified cardiomyopathy` is dropped as obsolete

## Why This Helps

Issue-driven checklists are useful prompts, but they mix roots, subtype series,
grouping terms, and questionable leaves. A MONDO-first prioritizer gives us a
reusable way to:

- start from MONDO terms and metadata
- layer in optional external evidence counts
- compare against current DisMech coverage
- generate a tuneable queue with transparent reasons

That makes it easier to review prioritization choices and to adjust weights as
our curation objectives change.
