# Porokeratosis

Boomer grounding analysis for [`kb/disorders/Porokeratosis.yaml`](../../../../kb/disorders/Porokeratosis.yaml).

- **Entry term:** [`MONDO:0006602`](http://purl.obolibrary.org/obo/MONDO_0006602) porokeratosis
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| DSAP | `MONDO:0019212` | disseminated superficial actinic porokeratosis | `AGREES` |
| Mibelli | `MONDO:0019141` | porokeratosis of Mibelli | `AGREES` |
| Linear | `MONDO:0023246` | linear porokeratosis | `AGREES` |
| PPPD | `MONDO:0008291` | porokeratosis plantaris palmaris et disseminata | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
