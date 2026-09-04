# Crigler-Najjar Syndrome

Boomer grounding analysis for [`kb/disorders/Crigler-Najjar_Syndrome.yaml`](../../../../kb/disorders/Crigler-Najjar_Syndrome.yaml).

- **Entry term:** [`MONDO:0009044`](http://purl.obolibrary.org/obo/MONDO_0009044) Crigler-Najjar syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0021020` | Crigler-Najjar syndrome type 1 | `AGREES` | ✓ ORDO, icd11f |
| Type 2 | `MONDO:0011725` | Crigler-Najjar syndrome type 2 | `AGREES` | ✓ ORDO, icd11f |

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
