# Autosomal Dominant Progressive External Ophthalmoplegia

Boomer grounding analysis for [`kb/disorders/Autosomal_Dominant_Progressive_External_Ophthalmoplegia.yaml`](../../../../kb/disorders/Autosomal_Dominant_Progressive_External_Ophthalmoplegia.yaml).

- **Entry term:** [`MONDO:0008003`](http://purl.obolibrary.org/obo/MONDO_0008003) autosomal dominant progressive external ophthalmoplegia
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 5, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PEOA1 | `MONDO:0024528` | progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 1 | `AGREES` |
| PEOA2 | `MONDO:0012238` | progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 2 | `AGREES` |
| PEOA3 | `MONDO:0012241` | progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 3 | `AGREES` |
| PEOA4 | `MONDO:0012415` | progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 4 | `AGREES` |
| PEOA5 | `MONDO:0013117` | progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal dominant 5 | `AGREES` |
| PEOA6 | `MONDO:0014062` | mitochondrial DNA deletion syndrome with progressive myopathy | `SILENT` |

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
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
