# analyses/

Generated analysis artifacts, organised by the thing analysed rather than by the
run that produced them.

Each subdirectory is one analysis *kind*; within it, results are laid out per
entity so a curator can navigate straight to the disease they care about:

```
analyses/<kind>/<entity-type>/<NAME>/
```

Every folder holds a human-readable `README.md` summary alongside the raw inputs
and outputs, so a result can be read without rerunning anything, and rerun
without reconstructing anything. The scripts that generate each tree are
committed under `<kind>/scripts/` — nothing here should be hand-edited, and
everything here should regenerate.

| Kind | What it analyses |
|---|---|
| [`boomer/`](boomer/) | Whether dismech's curated structure is logically consistent with MONDO's, resolved with the BOOMER probabilistic ontology-alignment solver. |

## How this differs from the neighbouring trees

`CLAUDE.md` already fixes the meaning of several directories, and this one sits
deliberately between them:

- **`research/`** is *only* deep-research provider outputs consumed as curation
  inputs. Nothing generated belongs there.
- **`docs/reports/`** is prose analysis *of the KB's content* — what the
  knowledge base says about biology.
- **`experiments/`** is measurements *about* the KB as an artifact —
  inter-annotator agreement, curation-methodology pilots. One question, one run,
  one `FINDINGS.md`.
- **`analyses/`** (here) is standing, regenerable, per-entity output. Not a
  finished study with a conclusion, but a tree you re-run against the current KB
  and browse by disease.

The distinction that matters in practice: an `experiments/` run is a snapshot
that stays fixed once written, because its `FINDINGS.md` reports what was true
that day. An `analyses/` tree is meant to be regenerated and to drift with the
KB.

## Derived, but committed

These outputs are generated, and committed anyway, for the same reason
`references_cache/` and `cache/**/*.csv` are: so a result is reviewable in a diff
and reproducible without the local ontology builds the generators need. Regenerate
them with the scripts rather than editing them by hand.
