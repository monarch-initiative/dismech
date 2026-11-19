# Entry growth

How does one dismech entry grow as it is curated? Each run measures a single
entry at every commit that touched it, from its first version up to a pinned
commit, and reports the size and wiring of its pathograph at each step.

## Runs

| Run | Entry | Commits measured | Pinned at | At the pin |
|---|---|---|---|---|
| [`Neuroblastoma/`](Neuroblastoma/) | `kb/disorders/Neuroblastoma.yaml` (`MONDO:0005072`) | 56, 2026-01-25 to 2026-11-03 | `a162fb4f54e` | 38 pathophysiology nodes; 14 of 16 phenotypes causally connected; 723 evidence items citing 281 PMIDs |

## Layout

`metrics.py` is shared tooling and lives at this level. Each run is a
subdirectory named for the entry's file stem:

```
entry_growth/
├── README.md          this index
├── metrics.py         the metric script
└── <Entry>/
    ├── FINDINGS.md    the report: pin, command, results, limits
    └── metrics.tsv    metrics.py output, as run
```

A later measurement of the same entry, pinned to a later commit, goes in its
own folder (`<Entry>-run2/`) so the earlier run stays as its baseline.

## Running a measurement

```bash
uv run python experiments/entry_growth/metrics.py \
  kb/disorders/<Entry>.yaml --until <full commit SHA> \
  > experiments/entry_growth/<Entry>/metrics.tsv
```

`--format markdown` prints the same rows as a Markdown table. The script reads
each version with `git show <commit>:<path>`, so it needs a checkout whose
history reaches the pin; a shallow CI clone will not.

## Columns

| Column | Meaning |
|---|---|
| `commit`, `date`, `pr` | Short hash, committer date, and the PR number parsed from the subject's last `(#N)` (`-` when there is none) |
| `disorder_files_changed` | `kb/disorders/` files the commit changed against its first parent: 1 for a commit about this entry, hundreds for a sweep across the knowledge base |
| `lines` | Lines in the file |
| `pathophysiology_nodes`, `phenotypes`, `treatments`, `differential_diagnoses`, `discussions` | Rows in each section |
| `phenotype_nodes` | Phenotype nodes in the built causal graph; fewer than `phenotypes` when two rows share a name |
| `connected_phenotypes` | Phenotype nodes with at least one causal in-edge, counted by `dismech.qc_plugins.causal_inlink_coverage`, the function behind `just compliance-connectivity` |
| `graph_edges` | Every edge in the graph `dismech.graph.build_causal_graph` builds, whatever its predicate |
| `causal_edges` | Edges whose predicate is `causes`, `leads_to`, `triggers` or `exacerbates`, self-loops excluded |
| `evidence_items` | Mappings anywhere in the entry that carry both `reference` and `supports` |
| `unique_pmids`, `unique_references` | Distinct `reference` values on those items: `PMID:` ones, and all of them |
| `conforming_nodes`, `conformed_modules` | Pathophysiology nodes with at least one `conforms_to`, and the distinct modules they name |
| `note` | Empty when the version was measured; otherwise why it was not |

## What the numbers do and do not say

Every version is measured with the repository's code at the time of the run,
not with the tools as they stood at each commit. That keeps one instrument
across the series, but a figure quoted in an old PR can differ from its row
here.

The metrics count size and wiring. They do not measure whether a claim is
right, whether a snippet supports it, or whether the entry is better: a commit
that removes a wrong evidence item lowers `evidence_items`, and that can be the
best commit in the series. Read the series alongside the PRs it names.
