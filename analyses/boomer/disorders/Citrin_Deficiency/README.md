# Citrin Deficiency

Boomer grounding analysis for [`kb/disorders/Citrin_Deficiency.yaml`](../../../../kb/disorders/Citrin_Deficiency.yaml).

- **Entry term:** [`MONDO:0016602`](http://purl.obolibrary.org/obo/MONDO_0016602) citrin deficiency
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| NICCD (Neonatal Intrahepatic Cholestasis caused by Citrin Deficiency) | `MONDO:0011601` | neonatal intrahepatic cholestasis due to citrin deficiency | `AGREES` |
| CTLN2 (Adult-onset Type II Citrullinemia) | `MONDO:0011326` | citrullinemia, type II, adult-onset | `AGREES` |

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
