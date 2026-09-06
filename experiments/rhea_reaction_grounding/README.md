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

`coverage.py` is shared across runs. It reads only, uses dismech's own YAML loader, and
takes both paths as arguments:

```bash
python3 coverage.py --kb-root kb --rhea2go 2026-09-06/rhea2go.tsv
```

## Runs

| Run | KB commit | Headline |
|---|---|---|
| [`2026-09-06/`](2026-09-06/) | `d985fb64` | 43.8% of molecular-function terms reachable; **0%** of biological-process terms; 99.9% of mappings undirected; 24.6% of reachable terms ambiguous |

## Reading these numbers

Two cautions carry across every run:

- Coverage measures what is **derivable from already-curated GO terms**. A curator assigning
  a Rhea ID by hand from UniProt could exceed it. These figures bound automated backfill and
  mechanical validation, not what curation could achieve.
- Availability is not appropriateness. That a GO term maps to a reaction says nothing about
  whether that reaction is the right claim for the node carrying it.
