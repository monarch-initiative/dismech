# Noonan Syndrome with Multiple Lentigines

Boomer grounding analysis for [`kb/disorders/Noonan_Syndrome_with_Multiple_Lentigines.yaml`](../../../../kb/disorders/Noonan_Syndrome_with_Multiple_Lentigines.yaml).

- **Entry term:** [`MONDO:0007893`](http://purl.obolibrary.org/obo/MONDO_0007893) Noonan syndrome with multiple lentigines
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| LPRD1 | `MONDO:0100082` | LEOPARD syndrome 1 | `AGREES` | ✓ DOID |
| LPRD2 | `MONDO:0012691` | LEOPARD syndrome 2 | `AGREES` | ✓ DOID |
| LPRD3 | `MONDO:0013380` | LEOPARD syndrome 3 | `AGREES` | ✓ DOID |

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
