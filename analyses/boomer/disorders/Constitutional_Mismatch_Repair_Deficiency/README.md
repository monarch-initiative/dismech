# Constitutional Mismatch Repair Deficiency

Boomer grounding analysis for [`kb/disorders/Constitutional_Mismatch_Repair_Deficiency.yaml`](../../../../kb/disorders/Constitutional_Mismatch_Repair_Deficiency.yaml).

- **Entry term:** [`MONDO:0031219`](http://purl.obolibrary.org/obo/MONDO_0031219) mismatch repair cancer syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CMMRD1 | `MONDO:0010159` | mismatch repair cancer syndrome 1 | `AGREES` | — no shared vocabulary |
| CMMRD2 | `MONDO:0030840` | mismatch repair cancer syndrome 2 | `AGREES` | — no shared vocabulary |
| CMMRD3 | `MONDO:0030841` | mismatch repair cancer syndrome 3 | `AGREES` | — no shared vocabulary |
| CMMRD4 | `MONDO:0030843` | mismatch repair cancer syndrome 4 | `AGREES` | — no shared vocabulary |

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
