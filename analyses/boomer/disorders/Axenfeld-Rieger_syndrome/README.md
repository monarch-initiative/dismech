# Axenfeld-Rieger_syndrome

Boomer grounding analysis for [`kb/disorders/Axenfeld-Rieger_syndrome.yaml`](../../../../kb/disorders/Axenfeld-Rieger_syndrome.yaml).

- **Entry term:** [`MONDO:0019187`](http://purl.obolibrary.org/obo/MONDO_0019187) Axenfeld-Rieger syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Axenfeld-Rieger Syndrome Type 1 (RIEG1) | `MONDO:0008386` | Axenfeld-Rieger syndrome type 1 | `AGREES` | ✓ DOID, NCIT |
| Axenfeld-Rieger Syndrome Type 2 (RIEG2) | `MONDO:0011097` | Axenfeld-Rieger syndrome type 2 | `AGREES` | ✓ DOID |
| Axenfeld-Rieger Syndrome Type 3 (RIEG3) | `MONDO:0011233` | Axenfeld-Rieger syndrome type 3 | `AGREES` | ✓ DOID |

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
