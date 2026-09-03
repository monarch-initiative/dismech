# Galloway-Mowat syndrome

Boomer grounding analysis for [`kb/disorders/Galloway-Mowat_Syndrome.yaml`](../../../../kb/disorders/Galloway-Mowat_Syndrome.yaml).

- **Entry term:** [`MONDO:0009627`](http://purl.obolibrary.org/obo/MONDO_0009627) Galloway-Mowat syndrome
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 10

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| GAMOS1 | `MONDO:0033005` | Galloway-Mowat syndrome 1 | `AGREES` | ✓ DOID |
| GAMOS2 | `MONDO:0033006` | Galloway-Mowat syndrome 2, X-linked | `AGREES` | ✓ DOID |
| GAMOS3 | `MONDO:0033007` | Galloway-Mowat syndrome 3 | `AGREES` | ✓ DOID |
| GAMOS4 | `MONDO:0033008` | Galloway-Mowat syndrome 4 | `AGREES` | ✓ DOID |
| GAMOS5 | `MONDO:0033009` | Galloway-Mowat syndrome 5 | `AGREES` | ✓ DOID |
| GAMOS6 | `MONDO:0032691` | Galloway-Mowat syndrome 6 | `AGREES` | — no shared vocabulary |
| GAMOS7 | `MONDO:0032692` | Galloway-Mowat syndrome 7 | `AGREES` | — no shared vocabulary |
| GAMOS8 | `MONDO:0032693` | Galloway-Mowat syndrome 8 | `AGREES` | — no shared vocabulary |
| GAMOS9 | `MONDO:0030471` | Galloway-Mowat syndrome 9 | `AGREES` | — no shared vocabulary |
| GAMOS10 | `MONDO:0030476` | Galloway-Mowat syndrome 10 | `AGREES` | — no shared vocabulary |

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
