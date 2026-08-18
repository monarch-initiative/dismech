# Bernard-Soulier Syndrome

Boomer grounding analysis for [`kb/disorders/Bernard-Soulier_Syndrome.yaml`](../../../../kb/disorders/Bernard-Soulier_Syndrome.yaml).

- **Entry term:** [`MONDO:0009276`](http://purl.obolibrary.org/obo/MONDO_0009276) Bernard-Soulier syndrome
- **Grounded subtypes:** 4
- **Verdicts:** SILENT 3, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| A1 | `MONDO:1060238` | MONDO:1060238 | `SILENT` |
| B | `MONDO:1060239` | MONDO:1060239 | `SILENT` |
| C | `MONDO:1060237` | MONDO:1060237 | `SILENT` |
| A2 | `MONDO:0007930` | Bernard-Soulier syndrome, type A2, autosomal dominant | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
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
