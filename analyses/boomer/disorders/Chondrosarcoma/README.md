# Chondrosarcoma

Boomer grounding analysis for [`kb/disorders/Chondrosarcoma.yaml`](../../../../kb/disorders/Chondrosarcoma.yaml).

- **Entry term:** [`MONDO:0008977`](http://purl.obolibrary.org/obo/MONDO_0008977) chondrosarcoma
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Dedifferentiated | `MONDO:0005013` | dedifferentiated chondrosarcoma | `AGREES` | ✓ DOID, NCIT |
| Mesenchymal | `MONDO:0006853` | mesenchymal chondrosarcoma | `AGREES` | ✓ DOID, MESH, NCIT |
| Clear Cell | `MONDO:0003684` | clear cell chondrosarcoma | `AGREES` | ✓ DOID, NCIT |
| Periosteal | `MONDO:0003680` | periosteal chondrosarcoma | `AGREES` | ✓ DOID, NCIT |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0003680` ≡ `DOID:5859`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
