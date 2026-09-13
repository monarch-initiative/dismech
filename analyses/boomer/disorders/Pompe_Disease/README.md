# Pompe Disease

Boomer grounding analysis for [`kb/disorders/Pompe_Disease.yaml`](../../../../kb/disorders/Pompe_Disease.yaml).

- **Entry term:** [`MONDO:0009290`](http://purl.obolibrary.org/obo/MONDO_0009290) glycogen storage disease II
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| IOPD | `MONDO:0017694` | glycogen storage disease due to acid maltase deficiency, infantile onset | `AGREES` | ✓ ORDO, icd11f |
| LOPD | `MONDO:0018485` | glycogen storage disease due to acid maltase deficiency, late-onset | `AGREES` | ✓ ORDO |

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
