# Houge-Janssens Syndrome

Boomer grounding analysis for [`kb/disorders/Houge-Janssens_Syndrome.yaml`](../../../../kb/disorders/Houge-Janssens_Syndrome.yaml).

- **Entry term:** [`MONDO:0957553`](http://purl.obolibrary.org/obo/MONDO_0957553) Houge-Janssens syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Houge-Janssens syndrome type 2 (PPP2R1A) | `MONDO:0014605` | Houge-Janssens syndrome 2 | `AGREES` |
| Houge-Janssens syndrome type 3 (PPP2CA) | `MONDO:0032697` | Houge-Janssens syndrome 3 | `AGREES` |
| Houge-Janssens syndrome type 4 (PPP2R5C) | `MONDO:0978293` | Houge-Janssens syndrome 4 | `AGREES` |

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
