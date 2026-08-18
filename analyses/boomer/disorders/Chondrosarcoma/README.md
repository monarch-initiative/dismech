# Chondrosarcoma

Boomer grounding analysis for [`kb/disorders/Chondrosarcoma.yaml`](../../../../kb/disorders/Chondrosarcoma.yaml).

- **Entry term:** [`MONDO:0008977`](http://purl.obolibrary.org/obo/MONDO_0008977) chondrosarcoma
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Dedifferentiated | `MONDO:0005013` | dedifferentiated chondrosarcoma | `AGREES` |
| Mesenchymal | `MONDO:0006853` | mesenchymal chondrosarcoma | `AGREES` |
| Clear Cell | `MONDO:0003684` | clear cell chondrosarcoma | `AGREES` |
| Periosteal | `MONDO:0003680` | periosteal chondrosarcoma | `AGREES` |

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
