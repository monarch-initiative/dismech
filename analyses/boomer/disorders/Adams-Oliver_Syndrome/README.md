# Adams-Oliver Syndrome

Boomer grounding analysis for [`kb/disorders/Adams-Oliver_Syndrome.yaml`](../../../../kb/disorders/Adams-Oliver_Syndrome.yaml).

- **Entry term:** [`MONDO:0007034`](http://purl.obolibrary.org/obo/MONDO_0007034) Adams-Oliver syndrome
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AOS1 | `MONDO:0024506` | Adams-Oliver syndrome 1 | `AGREES` |
| AOS2 | `MONDO:0013635` | Adams-Oliver syndrome 2 | `AGREES` |
| AOS3 | `MONDO:0013895` | Adams-Oliver syndrome 3 | `AGREES` |
| AOS4 | `MONDO:0014124` | Adams-Oliver syndrome 4 | `AGREES` |
| AOS5 | `MONDO:0014459` | Adams-Oliver syndrome 5 | `AGREES` |
| AOS6 | `MONDO:0014703` | Adams-Oliver syndrome 6 | `AGREES` |

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
