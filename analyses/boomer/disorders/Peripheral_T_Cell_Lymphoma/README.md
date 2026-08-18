# Peripheral T-Cell Lymphoma

Boomer grounding analysis for [`kb/disorders/Peripheral_T_Cell_Lymphoma.yaml`](../../../../kb/disorders/Peripheral_T_Cell_Lymphoma.yaml).

- **Entry term:** [`MONDO:0015760`](http://purl.obolibrary.org/obo/MONDO_0015760) T-cell non-Hodgkin lymphoma
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PTCL-NOS | `MONDO:0004964` | peripheral T-cell lymphoma, not otherwise specified | `SILENT` |
| TFH Angioimmunoblastic-Type | `MONDO:0004977` | angioimmunoblastic T-cell lymphoma | `AGREES` |
| TFH Follicular-Type | `MONDO:0958095` | Nodal T-follicular helper cell lymphoma, follicular type | `AGREES` |
| ALK-Positive ALCL | `MONDO:0017602` | ALK-positive anaplastic large cell lymphoma | `AGREES` |
| ALK-Negative ALCL | `MONDO:0017603` | ALK-negative anaplastic large cell lymphoma | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
