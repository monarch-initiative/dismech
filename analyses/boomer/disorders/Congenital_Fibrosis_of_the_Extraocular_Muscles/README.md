# Congenital Fibrosis of the Extraocular Muscles

Boomer grounding analysis for [`kb/disorders/Congenital_Fibrosis_of_the_Extraocular_Muscles.yaml`](../../../../kb/disorders/Congenital_Fibrosis_of_the_Extraocular_Muscles.yaml).

- **Entry term:** [`MONDO:0007614`](http://purl.obolibrary.org/obo/MONDO_0007614) congenital fibrosis of extraocular muscles
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CFEOM1 | `MONDO:0021083` | congenital fibrosis of extraocular muscles type 1 | `AGREES` | ✓ DOID |
| CFEOM2 | `MONDO:0011181` | fibrosis of extraocular muscles, congenital, 2 | `AGREES` | ✓ DOID |
| CFEOM3A | `MONDO:0010912` | fibrosis of extraocular muscles, congenital, 3A, with or without extraocular involvement | `AGREES` | ✓ DOID |
| CFEOM3B | `MONDO:0800209` | fibrosis of extraocular muscles, congenital, 3b | `AGREES` | — no shared vocabulary |
| CFEOM3C | `MONDO:0012262` | fibrosis of extraocular muscles, congenital, 3c | `AGREES` | ✓ DOID |
| CFEOM5 | `MONDO:0014538` | fibrosis of extraocular muscles, congenital, 5 | `AGREES` | ✓ DOID |
| Tukel syndrome | `MONDO:0012270` | Tukel syndrome | `AGREES` | ✓ DOID, icd11f |

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
