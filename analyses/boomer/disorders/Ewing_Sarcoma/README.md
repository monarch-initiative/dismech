# Ewing Sarcoma

Boomer grounding analysis for [`kb/disorders/Ewing_Sarcoma.yaml`](../../../../kb/disorders/Ewing_Sarcoma.yaml).

- **Entry term:** [`MONDO:0012817`](http://purl.obolibrary.org/obo/MONDO_0012817) Ewing sarcoma
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Osseous Ewing Sarcoma | `MONDO:0002625` | Ewing sarcoma of bone | `AGREES` | ✓ DOID, NCIT |
| Extraosseous Ewing Sarcoma | `MONDO:0018270` | extraskeletal Ewing sarcoma | `AGREES` | ✓ DOID, NCIT |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
