# Pericarditis

Boomer grounding analysis for [`kb/disorders/Pericarditis.yaml`](../../../../kb/disorders/Pericarditis.yaml).

- **Entry term:** [`MONDO:0005904`](http://purl.obolibrary.org/obo/MONDO_0005904) pericarditis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Recurrent pericarditis idiopathic | `MONDO:0016662` | idiopathic recurrent pericarditis | `SILENT` |
| Constrictive pericarditis | `MONDO:0006711` | constrictive pericarditis | `AGREES` |
| Tuberculous pericarditis | `MONDO:0005903` | pericardial tuberculosis | `AGREES` |

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
