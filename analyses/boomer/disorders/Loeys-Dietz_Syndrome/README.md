# Loeys-Dietz Syndrome

Boomer grounding analysis for [`kb/disorders/Loeys-Dietz_Syndrome.yaml`](../../../../kb/disorders/Loeys-Dietz_Syndrome.yaml).

- **Entry term:** [`MONDO:0018954`](http://purl.obolibrary.org/obo/MONDO_0018954) Loeys-Dietz syndrome
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Loeys-Dietz Syndrome Type 1 | `MONDO:0012212` | Loeys-Dietz syndrome 1 | `AGREES` | ✓ DOID, NCIT |
| Loeys-Dietz Syndrome Type 2 | `MONDO:0012427` | Loeys-Dietz syndrome 2 | `AGREES` | ✓ DOID, NCIT |
| Loeys-Dietz Syndrome Type 3 | `MONDO:0013426` | aneurysm-osteoarthritis syndrome | `AGREES` | ✓ DOID |
| Loeys-Dietz Syndrome Type 4 | `MONDO:0013897` | Loeys-Dietz syndrome 4 | `AGREES` | ✓ DOID |
| Loeys-Dietz Syndrome Type 5 | `MONDO:0014262` | Rienhoff syndrome | `AGREES` | ✓ DOID |
| Loeys-Dietz Syndrome Type 6 | `MONDO:0030500` | Loeys-Dietz syndrome 6 | `AGREES` | ✓ DOID |

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
