# experiments/

Curation-methodology experiments: measurements *about* the knowledge base rather
than content *of* it.

Nothing here is part of the KB. Files in this tree are deliberately outside
`kb/disorders/`, `kb/modules/`, and `kb/groupings/` so that no validator,
`just` recipe, or test in `tests/test_data.py` picks them up — several are
snapshots of Disease entries that would otherwise collide on the unique-`name`
check.

This is also not `research/`, which per `CLAUDE.md` holds deep-research provider
outputs consumed as curation inputs. An experiment here may *cite* a report in
`research/`, but its own artifacts live in this tree.

## Layout

Each experiment *type* gets a subdirectory holding its shared tooling and an index
`README.md`. Within that, each individual run gets its own subdirectory containing
its inputs and a `FINDINGS.md` stating what was measured, how, and what the limits
of the measurement are. Scripts that compute metrics are committed alongside, so
numbers can be regenerated rather than trusted.

| Experiment | Question | Runs |
|---|---|---|
| [`interannotator/`](interannotator/) | How much of a dismech entry is determined by the evidence, and how much by the curator? Each run curates one disease twice, independently, and measures where the versions agree. | 1 |
