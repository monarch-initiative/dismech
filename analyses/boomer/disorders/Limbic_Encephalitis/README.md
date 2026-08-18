# Limbic Encephalitis

Boomer grounding analysis for [`kb/disorders/Limbic_Encephalitis.yaml`](../../../../kb/disorders/Limbic_Encephalitis.yaml).

- **Entry term:** [`MONDO:0015588`](http://purl.obolibrary.org/obo/MONDO_0015588) limbic encephalitis
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Autoimmune Limbic Encephalitis | `MONDO:0850097` | autoimmune limbic encephalitis | `AGREES` |
| Classic Paraneoplastic Limbic Encephalitis | `MONDO:0015590` | classic paraneoplastic limbic encephalitis | `AGREES` |
| Limbic Encephalitis with LGI1 Antibodies | `MONDO:0015592` | limbic encephalitis with LGI1 antibodies | `SILENT` |
| Limbic Encephalitis with CASPR2 Antibodies | `MONDO:0017179` | limbic encephalitis with caspr2 antibodies | `AGREES` |

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
