# Arterial Calcification of Infancy

Boomer grounding analysis for [`kb/disorders/Arterial_Calcification_of_Infancy.yaml`](../../../../kb/disorders/Arterial_Calcification_of_Infancy.yaml).

- **Entry term:** [`MONDO:0018870`](http://purl.obolibrary.org/obo/MONDO_0018870) arterial calcification of infancy
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ENPP1-related | `MONDO:0008817` | arterial calcification, generalized, of infancy, 1 | `AGREES` | — no shared vocabulary |
| ABCC6-related | `MONDO:0013768` | arterial calcification, generalized, of infancy, 2 | `AGREES` | — no shared vocabulary |

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
