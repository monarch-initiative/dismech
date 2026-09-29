# Hypokalemic Periodic Paralysis

Boomer grounding analysis for [`kb/disorders/Hypokalemic_Periodic_Paralysis.yaml`](../../../../kb/disorders/Hypokalemic_Periodic_Paralysis.yaml).

- **Entry term:** [`MONDO:0008223`](http://purl.obolibrary.org/obo/MONDO_0008223) hypokalemic periodic paralysis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0042979` | hypokalemic periodic paralysis, type 1 | `AGREES` | — no shared vocabulary |
| Type 2 | `MONDO:0013234` | hypokalemic periodic paralysis, type 2 | `AGREES` | silent (MESH) |

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
