# Geleophysic Dysplasia

Boomer grounding analysis for [`kb/disorders/Geleophysic_Dysplasia.yaml`](../../../../kb/disorders/Geleophysic_Dysplasia.yaml).

- **Entry term:** [`MONDO:0000127`](http://purl.obolibrary.org/obo/MONDO_0000127) geleophysic dysplasia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| GD1 | `MONDO:0009269` | geleophysic dysplasia 1 | `AGREES` |
| GD2 | `MONDO:0013612` | geleophysic dysplasia 2 | `AGREES` |
| GD3 | `MONDO:0054722` | geleophysic dysplasia 3 | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
