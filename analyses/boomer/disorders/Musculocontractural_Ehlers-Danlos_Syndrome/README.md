# Musculocontractural Ehlers-Danlos Syndrome

Boomer grounding analysis for [`kb/disorders/Musculocontractural_Ehlers-Danlos_Syndrome.yaml`](../../../../kb/disorders/Musculocontractural_Ehlers-Danlos_Syndrome.yaml).

- **Entry term:** [`MONDO:0011142`](http://purl.obolibrary.org/obo/MONDO_0011142) Ehlers-Danlos syndrome, musculocontractural type
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| mcEDS-CHST14 | `MONDO:0020681` | Ehlers-Danlos syndrome, musculocontractural type 1 | `AGREES` |
| mcEDS-DSE | `MONDO:0014236` | Ehlers-Danlos syndrome, musculocontractural type 2 | `AGREES` |

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
