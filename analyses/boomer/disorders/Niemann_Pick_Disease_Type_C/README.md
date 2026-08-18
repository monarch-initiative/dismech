# Niemann-Pick Disease Type C

Boomer grounding analysis for [`kb/disorders/Niemann_Pick_Disease_Type_C.yaml`](../../../../kb/disorders/Niemann_Pick_Disease_Type_C.yaml).

- **Entry term:** [`MONDO:0018982`](http://purl.obolibrary.org/obo/MONDO_0018982) Niemann-Pick disease type C
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| NPC1 | `MONDO:0009757` | Niemann-Pick disease, type C1 | `AGREES` |
| NPC2 | `MONDO:0011873` | Niemann-Pick disease, type C2 | `AGREES` |

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
