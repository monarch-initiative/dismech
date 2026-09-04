# Autoimmune Lymphoproliferative Syndrome

Boomer grounding analysis for [`kb/disorders/Autoimmune_Lymphoproliferative_Syndrome.yaml`](../../../../kb/disorders/Autoimmune_Lymphoproliferative_Syndrome.yaml).

- **Entry term:** [`MONDO:0017979`](http://purl.obolibrary.org/obo/MONDO_0017979) autoimmune lymphoproliferative syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ALPS-FAS | `MONDO:1060194` | FAS-related autoimmune lymphoproliferative immune disorder | `AGREES` | — no shared vocabulary |
| ALPS-CASP10 | `MONDO:0011383` | autoimmune lymphoproliferative syndrome type 2A | `AGREES` | ✓ DOID, NCIT |

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
