# Congenital Bilateral Absence of Vas Deferens

Boomer grounding analysis for [`kb/disorders/Congenital_Bilateral_Absence_of_Vas_Deferens.yaml`](../../../../kb/disorders/Congenital_Bilateral_Absence_of_Vas_Deferens.yaml).

- **Entry term:** [`MONDO:0018801`](http://purl.obolibrary.org/obo/MONDO_0018801) congenital bilateral absence of vas deferens
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CFTR-related | `MONDO:0010178` | congenital bilateral aplasia of vas deferens from CFTR mutation | `AGREES` | ✓ DOID |
| ADGRG2-related | `MONDO:0010511` | vas deferens, congenital bilateral aplasia of, X-linked | `AGREES` | ✓ DOID |

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
