# Genital Lichen Sclerosus

Boomer grounding analysis for [`kb/disorders/Genital_Lichen_Sclerosus.yaml`](../../../../kb/disorders/Genital_Lichen_Sclerosus.yaml).

- **Entry term:** [`MONDO:0007899`](http://purl.obolibrary.org/obo/MONDO_0007899) lichen sclerosus et atrophicus
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Vulvar Lichen Sclerosus | `MONDO:0006491` | vulvar lichen sclerosus | `AGREES` |
| Penile Lichen Sclerosus | `MONDO:0001725` | balanitis xerotica obliterans | `SILENT` |

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
