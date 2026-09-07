# rhea_reaction_grounding/

**Question.** Could dismech ground its mechanism nodes in
[Rhea](https://www.rhea-db.org/) biochemical reactions, and how much of the KB would that
actually reach?

dismech carries no Rhea identifiers. Issue
[#973](https://github.com/monarch-initiative/dismech/issues/973) proposes adding a
`reactions:` slot bound to Rhea CURIEs; the thread's open objection is that the coverage is
unknown. Runs here measure coverage before any schema commitment is made.

Nothing in this directory modifies the schema, `kb/`, `conf/`, or any cache. These are
measurements, not curation.

## Method

Rhea and dismech share no identifier, so the measurable bridge is
[`rhea2go.tsv`](https://ftp.expasy.org/databases/rhea/tsv/rhea2go.tsv) — Rhea reactions
mapped to GO terms, which dismech already curates in its `molecular_functions` and
`biological_processes` slots. Each run pins its own `rhea2go.tsv` snapshot by sha256, since
the upstream URL is unversioned.

Two scripts are shared across runs. Both read only and use dismech's own YAML loader.

`coverage.py` measures how much of the KB's GO annotation Rhea can reach:

```bash
python3 coverage.py --kb-root kb --rhea2go 2026-09-07-coverage/rhea2go.tsv
```

`concordance.py` tests whether a reached reaction is the *right* one, by checking the
entry's curated ChEBI biomarker against the reaction's ChEBI participants:

```bash
python3 concordance.py --out-dir 2026-09-07-biomarker-concordance
```

`ambiguity.py` enumerates the MF terms that map to several reactions and separates those
whose reactions share a substrate core from those that are genuinely different chemistry:

```bash
python3 ambiguity.py --out-dir 2026-09-07-mapping-ambiguity
```

## Runs

| Run | KB commit | Headline |
|---|---|---|
| [`2026-09-07-coverage/`](2026-09-07-coverage/) | `d985fb64` | 43.8% of molecular-function terms reachable; **0%** of biological-process terms; 99.9% of mappings undirected; 24.6% of reachable terms ambiguous |
| [`2026-09-07-biomarker-concordance/`](2026-09-07-biomarker-concordance/) | `d985fb64` | 107 entries pair a mappable MF term with a ChEBI biomarker; **42 (39.3%)** have a biomarker that is a participant of the mapped reaction; 35 of those monogenic |
| [`2026-09-07-mapping-ambiguity/`](2026-09-07-mapping-ambiguity/) | `d985fb64` | 70 ambiguous MF terms, but only **104 of 1,358** annotation instances (7.7%); 36 share a substrate core, 33 are genuinely disjoint (45 instances, 3.3%) |

## Reading these numbers

Two cautions carry across every run:

- Coverage measures what is **derivable from already-curated GO terms**. A curator assigning
  a Rhea ID by hand from UniProt could exceed it. These figures bound automated backfill and
  mechanical validation, not what curation could achieve.
- Availability is not appropriateness. That a GO term maps to a reaction says nothing about
  whether that reaction is the right claim for the node carrying it. The concordance run
  probes appropriateness on one axis, but a non-match there is a lead to read, not a verdict.
