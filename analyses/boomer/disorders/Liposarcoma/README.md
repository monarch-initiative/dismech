# Liposarcoma

Boomer grounding analysis for [`kb/disorders/Liposarcoma.yaml`](../../../../kb/disorders/Liposarcoma.yaml).

- **Entry term:** [`MONDO:0005060`](http://purl.obolibrary.org/obo/MONDO_0005060) liposarcoma
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| WDLPS | `MONDO:0005103` | well-differentiated liposarcoma | `AGREES` | ✓ ORDO |
| DDLPS | `MONDO:0020563` | dedifferentiated liposarcoma | `AGREES` | ✓ DOID, NCIT, ORDO |
| MLPS | `MONDO:0013280` | myxoid liposarcoma | `AGREES` | ✓ DOID, MESH, NCIT |
| PLPS | `MONDO:0020562` | pleomorphic liposarcoma | `AGREES` | ✓ DOID, NCIT, ORDO |

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
