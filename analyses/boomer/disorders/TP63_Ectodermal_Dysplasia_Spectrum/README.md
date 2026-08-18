# TP63-Related Ectodermal Dysplasia Spectrum

Boomer grounding analysis for [`kb/disorders/TP63_Ectodermal_Dysplasia_Spectrum.yaml`](../../../../kb/disorders/TP63_Ectodermal_Dysplasia_Spectrum.yaml).

- **Entry term:** [`MONDO:1040001`](http://purl.obolibrary.org/obo/MONDO_1040001) TP63-related ectodermal dysplasia spectrum with limb and orofacial malformations
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AEC | `MONDO:0007124` | ankyloblepharon-ectodermal defects-cleft lip/palate syndrome | `AGREES` |
| EEC3 | `MONDO:0011428` | ectrodactyly, ectodermal dysplasia, and cleft lip-palate syndrome 3 | `AGREES` |
| ADULT | `MONDO:0007072` | ADULT syndrome | `AGREES` |
| LMS | `MONDO:0011334` | limb-mammary syndrome | `SILENT` |
| RHS | `MONDO:0007508` | Rapp-Hodgkin syndrome | `AGREES` |

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
