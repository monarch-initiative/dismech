# Senior-Loken Syndrome

Boomer grounding analysis for [`kb/disorders/Senior-Loken_Syndrome.yaml`](../../../../kb/disorders/Senior-Loken_Syndrome.yaml).

- **Entry term:** [`MONDO:0017842`](http://purl.obolibrary.org/obo/MONDO_0017842) Senior-Loken syndrome
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SLSN1 | `MONDO:0009962` | Senior-Loken syndrome 1 | `AGREES` |
| SLSN5 | `MONDO:0012225` | Senior-Loken syndrome 5 | `AGREES` |
| SLSN6 | `MONDO:0012433` | Senior-Loken syndrome 6 | `AGREES` |
| SLSN7 | `MONDO:0013326` | Senior-Loken syndrome 7 | `AGREES` |
| SLSN8 | `MONDO:0014579` | Senior-Loken syndrome 8 | `AGREES` |

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
