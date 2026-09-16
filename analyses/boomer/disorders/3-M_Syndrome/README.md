# 3-M Syndrome

Boomer grounding analysis for [`kb/disorders/3-M_Syndrome.yaml`](../../../../kb/disorders/3-M_Syndrome.yaml).

- **Entry term:** [`MONDO:0007477`](http://purl.obolibrary.org/obo/MONDO_0007477) 3-M syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| 3M1 | `MONDO:0010117` | 3M syndrome 1 | `AGREES` | — no shared vocabulary |
| 3M2 | `MONDO:0013039` | 3M syndrome 2 | `AGREES` | silent (MESH) |
| 3M3 | `MONDO:0013627` | 3M syndrome 3 | `AGREES` | — no shared vocabulary |

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
