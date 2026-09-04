# Congenital Dyserythropoietic Anemia

Boomer grounding analysis for [`kb/disorders/Congenital_Dyserythropoietic_Anemia.yaml`](../../../../kb/disorders/Congenital_Dyserythropoietic_Anemia.yaml).

- **Entry term:** [`MONDO:0019403`](http://purl.obolibrary.org/obo/MONDO_0019403) congenital dyserythropoietic anemia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CDA I | `MONDO:0020337` | congenital dyserythropoietic anemia type 1 | `AGREES` | ✓ DOID, ORDO |
| CDA II | `MONDO:0009134` | congenital dyserythropoietic anemia type 2 | `AGREES` | ✓ DOID, ORDO |
| CDA III | `MONDO:0007109` | congenital dyserythropoietic anemia type 3 | `AGREES` | ✓ DOID, ORDO |

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
