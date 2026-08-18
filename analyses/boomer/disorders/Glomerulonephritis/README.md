# Glomerulonephritis

Boomer grounding analysis for [`kb/disorders/Glomerulonephritis.yaml`](../../../../kb/disorders/Glomerulonephritis.yaml).

- **Entry term:** [`MONDO:0002462`](http://purl.obolibrary.org/obo/MONDO_0002462) glomerulonephritis
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 6, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| IgA Nephropathy | `MONDO:0005342` | IgA glomerulonephritis | `AGREES` |
| Membranous Nephropathy | `MONDO:0005376` | membranous glomerulonephritis | `AGREES` |
| Lupus Nephritis | `MONDO:0005556` | lupus nephritis | `AGREES` |
| Post-Streptococcal GN | `MONDO:0001870` | acute poststreptococcal glomerulonephritis | `AGREES` |
| Anti-GBM Disease | `MONDO:0009303` | anti-glomerular basement membrane disease | `SILENT` |
| ANCA-Associated GN | `MONDO:0019988` | pauci-immune glomerulonephritis with ANCA | `AGREES` |
| Membranoproliferative GN | `MONDO:0002461` | membranoproliferative glomerulonephritis | `AGREES` |

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
