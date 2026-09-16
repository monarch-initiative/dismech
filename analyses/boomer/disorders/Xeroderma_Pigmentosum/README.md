# Xeroderma Pigmentosum

Boomer grounding analysis for [`kb/disorders/Xeroderma_Pigmentosum.yaml`](../../../../kb/disorders/Xeroderma_Pigmentosum.yaml).

- **Entry term:** [`MONDO:0019600`](http://purl.obolibrary.org/obo/MONDO_0019600) xeroderma pigmentosum
- **Grounded subtypes:** 8
- **Verdicts:** AGREES 8

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| XP-A | `MONDO:0010210` | xeroderma pigmentosum group A | `AGREES` | ✓ DOID, NCIT |
| XP-B | `MONDO:0012531` | xeroderma pigmentosum group B | `AGREES` | ✓ DOID, NCIT |
| XP-C | `MONDO:0010211` | xeroderma pigmentosum group C | `AGREES` | ✓ DOID, NCIT |
| XP-D | `MONDO:0010212` | xeroderma pigmentosum group D | `AGREES` | ✓ DOID, NCIT |
| XP-E | `MONDO:0010213` | xeroderma pigmentosum group E | `AGREES` | ✓ DOID, NCIT |
| XP-F | `MONDO:0010215` | xeroderma pigmentosum group F | `AGREES` | ✓ DOID, NCIT |
| XP-G | `MONDO:0010216` | xeroderma pigmentosum group G | `AGREES` | ✓ DOID, NCIT |
| XP-V | `MONDO:0010214` | xeroderma pigmentosum variant type | `AGREES` | ✓ DOID, NCIT |

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
