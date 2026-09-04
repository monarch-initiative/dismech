# Hemochromatosis

Boomer grounding analysis for [`kb/disorders/Hemochromatosis.yaml`](../../../../kb/disorders/Hemochromatosis.yaml).

- **Entry term:** [`MONDO:0006507`](http://purl.obolibrary.org/obo/MONDO_0006507) hereditary hemochromatosis
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0021001` | hemochromatosis type 1 | `AGREES` | ✓ DOID, NCIT |
| Type 2A | `MONDO:0011216` | hemochromatosis type 2A | `AGREES` | ✓ DOID |
| Type 2B | `MONDO:0013220` | hemochromatosis type 2B | `AGREES` | ✓ DOID |
| Type 3 | `MONDO:0011417` | hemochromatosis type 3 | `AGREES` | ✓ DOID |

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
