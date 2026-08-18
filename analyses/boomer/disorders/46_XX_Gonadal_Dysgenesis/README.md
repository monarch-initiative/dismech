# 46,XX Gonadal Dysgenesis

Boomer grounding analysis for [`kb/disorders/46_XX_Gonadal_Dysgenesis.yaml`](../../../../kb/disorders/46_XX_Gonadal_Dysgenesis.yaml).

- **Entry term:** [`MONDO:0009299`](http://purl.obolibrary.org/obo/MONDO_0009299) 46 XX gonadal dysgenesis
- **Grounded subtypes:** 11
- **Verdicts:** AGREES 10, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| ODG1 | `MONDO:0024463` | ovarian dysgenesis 1 | `AGREES` |
| ODG2 | `MONDO:0010349` | ovarian dysgenesis 2 | `AGREES` |
| ODG3 | `MONDO:0013689` | ovarian dysgenesis 3 | `AGREES` |
| ODG4 | `MONDO:0014520` | 46,XX ovarian dysgenesis-short stature syndrome | `SILENT` |
| ODG5 | `MONDO:0054666` | ovarian dysgenesis 5 | `AGREES` |
| ODG6 | `MONDO:0054850` | ovarian dysgenesis 6 | `AGREES` |
| ODG7 | `MONDO:0020857` | ovarian dysgenesis 7 | `AGREES` |
| ODG8 | `MONDO:0032590` | ovarian dysgenesis 8 | `AGREES` |
| ODG9 | `MONDO:0030506` | ovarian dysgenesis 9 | `AGREES` |
| ODG10 | `MONDO:0030736` | ovarian dysgenesis 10 | `AGREES` |
| ODG11 | `MONDO:0971176` | ovarian dysgenesis 11 | `AGREES` |

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
