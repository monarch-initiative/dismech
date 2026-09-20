# PRKAG2 Cardiac Syndrome

Boomer grounding analysis for [`kb/disorders/PRKAG2_Cardiac_Syndrome.yaml`](../../../../kb/disorders/PRKAG2_Cardiac_Syndrome.yaml).

- **Entry term:** [`MONDO:0800484`](http://purl.obolibrary.org/obo/MONDO_0800484) PRKAG2-related cardiomyopathy
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Lethal Congenital | `MONDO:0009867` | lethal congenital glycogen storage disease of heart | `AGREES` | — no shared vocabulary |

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
