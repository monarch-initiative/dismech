# Microcephalic Osteodysplastic Primordial Dwarfism Type I

Boomer grounding analysis for [`kb/disorders/Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I.yaml`](../../../../kb/disorders/Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I.yaml).

- **Entry term:** [`MONDO:0008871`](http://purl.obolibrary.org/obo/MONDO_0008871) microcephalic osteodysplastic primordial dwarfism type I
- **Grounded subtypes:** 1
- **Verdicts:** SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MOPD III | `MONDO:0008873` | microcephalic osteodysplastic primordial dwarfism, type 3 | `SILENT` | — no shared vocabulary |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
