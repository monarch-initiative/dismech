# Ritscher-Schinzel Syndrome

Boomer grounding analysis for [`kb/disorders/Ritscher-Schinzel_Syndrome.yaml`](../../../../kb/disorders/Ritscher-Schinzel_Syndrome.yaml).

- **Entry term:** [`MONDO:0019078`](http://purl.obolibrary.org/obo/MONDO_0019078) Ritscher-Schinzel syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| RSS1 | `MONDO:0009073` | Ritscher-Schinzel syndrome 1 | `AGREES` |
| RSS2 | `MONDO:0010499` | Ritscher-Schinzel syndrome 2 | `AGREES` |
| RSS3 | `MONDO:0030864` | Ritscher-Schinzel syndrome 3 | `AGREES` |

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
