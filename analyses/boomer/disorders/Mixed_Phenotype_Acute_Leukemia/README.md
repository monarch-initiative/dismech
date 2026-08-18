# Mixed Phenotype Acute Leukemia

Boomer grounding analysis for [`kb/disorders/Mixed_Phenotype_Acute_Leukemia.yaml`](../../../../kb/disorders/Mixed_Phenotype_Acute_Leukemia.yaml).

- **Entry term:** [`MONDO:0020743`](http://purl.obolibrary.org/obo/MONDO_0020743) mixed phenotype acute leukemia
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| MPAL BCR-ABL1 | `MONDO:0850449` | mixed phenotype acute leukemia with BCR-ABL1 | `AGREES` |
| MPAL KMT2A | `MONDO:0850450` | mixed phenotype acute leukemia with MLL rearranged | `AGREES` |
| MPAL B/myeloid NOS | `MONDO:0850451` | mixed phenotype acute leukemia, B/myeloid | `AGREES` |
| MPAL T/myeloid NOS | `MONDO:0850452` | mixed phenotype acute leukemia,T/myeloid | `AGREES` |
| Acute undifferentiated leukemia | `MONDO:0020321` | acute undifferentiated leukemia | `SILENT` |

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
