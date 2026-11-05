# Entry growth: Neuroblastoma (MONDO:0005072)

How the neuroblastoma entry grew, measured at each of the 56 commits that
touched `kb/disorders/Neuroblastoma.yaml` from its first version to the pinned
commit.

| | |
|---|---|
| **Entry** | `kb/disorders/Neuroblastoma.yaml`, `MONDO:0005072` |
| **Pinned commit** | `a162fb4f54e6a33633f699dcc398b5df0085e695` (2026-11-03, #16320) |
| **Commits measured** | 56, from `43e111b7047` (2026-01-25) to the pin |
| **Measured** | 2026-11-05, with the repository's code at `199eb7af890` |
| **Output** | `metrics.tsv`, as run; columns are defined in [`../README.md`](../README.md) |

```bash
uv run python experiments/entry_growth/metrics.py kb/disorders/Neuroblastoma.yaml \
  --until a162fb4f54e6a33633f699dcc398b5df0085e695 \
  > experiments/entry_growth/Neuroblastoma/metrics.tsv
```

The pin is the newest commit to change the entry as of 2026-11-05. A later run,
pinned to a later commit, extends the series and compares against the last row
here.

## The entry at three points

The middle column is the last version before 15 October 2026, when a run of
commits about this entry alone began.

| Metric | First version (2026-01-25) | 2026-08-29 | Pin (2026-11-03) |
|---|---|---|---|
| Lines | 293 | 797 | 17,227 |
| Pathophysiology nodes | 3 | 3 | 38 |
| Phenotypes | 7 | 7 | 16 |
| Phenotypes with a causal in-edge | 0 | 0 | 14 |
| Graph edges (all predicates) | 1 | 5 | 66 |
| Causal edges | 1 | 2 | 45 |
| Evidence items | 2 | 30 | 723 |
| Unique PMIDs cited | 2 | 9 | 281 |
| Unique references cited | 2 | 9 | 290 |
| Nodes conforming to a module | 0 | 0 | 6 |
| Modules conformed to | 0 | 0 | 4 |
| Treatments | 6 | 7 | 13 |
| Differential diagnoses | 0 | 0 | 13 |
| Discussions | 0 | 0 | 6 |

## Which commits did it

`disorder_files_changed` separates the commits into three groups.

- **25 January to 29 August 2026: 20 commits.** Sixteen were sweeps that changed
  between 26 and 1,653 disorder files at once, three changed 7 to 15 files
  (#6462, #7114, #9719), and one changed this file alone (#1918). Together they
  took the entry from 293 to 797 lines and from 2 to 30 evidence items. It kept
  3 pathophysiology nodes and 7 phenotypes throughout, none of them causally
  connected.
- **15 to 29 October 2026: 35 commits** (#14386 to #15887), each changing this
  file and no other disorder file. They added 693 of the 721 evidence items,
  272 of the 279 PMIDs and 16,430 of the 16,934 lines gained since the first
  version, and all 35 of the pathophysiology nodes gained. These are the PRs of
  the neuroblastoma curation project tracked in #14976, authored with Claude
  Code.
- **3 November 2026: the pin** (#16320), which changed 185 disorder files to fix
  snippets for a stricter reference validator. No count in this entry moved.

Within the October commits, four steps changed the shape of the graph rather
than its size:

| Commit | PR | Change |
|---|---|---|
| `93c7a8d9bd1` | #15079 | Phenotypes 7 → 15 |
| `cb82bbd6d5b` | #15105 | First conformance: 2 nodes, 1 module |
| `fcc1b51fa00` | #15356 | Phenotypes with a causal in-edge 1 → 14 of 16 |
| `e93f0d582ae` | #15336 | Modules conformed to 2 → 4 |

The series is not monotonic. #15320 removed 3 evidence items and 67 lines, and
four other commits each removed between 1 and 16 lines.

## Limits of the measurement

- **One instrument, today's.** Every version is measured with the graph
  builder and the connectivity function as they stand at `199eb7af890`. A
  figure an older PR quoted from an older tool may not match its row.
- **Size and wiring, not correctness.** The counts say how much the entry
  contains and how it is connected. They do not say whether a claim is right
  or whether a snippet supports it; validation and review answer those.
- **What counts as an evidence item.** Any mapping carrying both `reference`
  and `supports`, wherever it sits in the entry. PMIDs that appear only in
  prose, such as `notes`, are not counted.
- **What counts as connected.** Only the causal predicates (`causes`,
  `leads_to`, `triggers`, `exacerbates`). A treatment edge or a readout pointing
  at a phenotype does not connect it.
- **Commit groups.** `disorder_files_changed` is taken against each commit's
  first parent. None of the 56 commits is a merge, so this is each commit's
  whole change. The file was never renamed: `git log --follow` returns the same
  56 commits.
