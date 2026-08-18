# Noonan Syndrome

Boomer grounding analysis for [`kb/disorders/Noonan_Syndrome.yaml`](../../../../kb/disorders/Noonan_Syndrome.yaml).

- **Entry term:** [`MONDO:0018997`](http://purl.obolibrary.org/obo/MONDO_0018997) Noonan syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Noonan Syndrome 1 (PTPN11-related) | `MONDO:0008104` | Noonan syndrome 1 | `AGREES` |
| Noonan Syndrome with Multiple Lentigines | `MONDO:0007893` | Noonan syndrome with multiple lentigines | `SILENT` |

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
