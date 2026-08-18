# Inborn Disorder of Bile Acid Synthesis

Boomer grounding analysis for [`kb/disorders/Inborn_Disorder_of_Bile_Acid_Synthesis.yaml`](../../../../kb/disorders/Inborn_Disorder_of_Bile_Acid_Synthesis.yaml).

- **Entry term:** [`MONDO:0019218`](http://purl.obolibrary.org/obo/MONDO_0019218) inborn disorder of bile acid synthesis
- **Grounded subtypes:** 6
- **Verdicts:** SILENT 5, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| BASD Type 1 | `MONDO:0011906` | congenital bile acid synthesis defect 1 | `SILENT` |
| BASD Type 2 | `MONDO:0009339` | congenital bile acid synthesis defect 2 | `SILENT` |
| BASD Type 3 | `MONDO:0013439` | congenital bile acid synthesis defect 3 | `SILENT` |
| BASD Type 4 | `MONDO:0008967` | congenital bile acid synthesis defect 4 | `SILENT` |
| CTX | `MONDO:0008948` | cerebrotendinous xanthomatosis | `AGREES` |
| Bile acid conjugation defect 1 | `MONDO:0030991` | bile acid conjugation defect 1 | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

5 subtype(s) are `SILENT`: MONDO asserts no path between the
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
