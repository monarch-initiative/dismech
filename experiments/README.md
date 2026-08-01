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

Each experiment gets a subdirectory containing, at minimum, a `FINDINGS.md`
stating what was measured, how, and what the limits of the measurement are.
Where an experiment computes metrics, the script that computes them belongs
here too, so the numbers can be regenerated rather than trusted.

| Experiment | Question |
|---|---|
| [`interannotator/`](interannotator/) | How much of a dismech entry is determined by the evidence, and how much by the curator? Two independent curations of FG syndrome 1 (`MONDO:0010590`), compared. |
