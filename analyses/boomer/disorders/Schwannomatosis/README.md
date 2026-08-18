# Schwannomatosis

Boomer grounding analysis for [`kb/disorders/Schwannomatosis.yaml`](../../../../kb/disorders/Schwannomatosis.yaml).

- **Entry term:** [`MONDO:0008075`](http://purl.obolibrary.org/obo/MONDO_0008075) schwannomatosis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SMARCB1-related | `MONDO:0024517` | SMARCB1-related schwannomatosis | `AGREES` |
| LZTR1-related | `MONDO:0014299` | LZTR1-related schwannomatosis | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
