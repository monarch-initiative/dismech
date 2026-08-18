# Cole-Carpenter syndrome

Boomer grounding analysis for [`kb/disorders/Cole-Carpenter_Syndrome.yaml`](../../../../kb/disorders/Cole-Carpenter_Syndrome.yaml).

- **Entry term:** [`MONDO:0016085`](http://purl.obolibrary.org/obo/MONDO_0016085) Cole-Carpenter syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CCS1 | `MONDO:0007204` | Cole-Carpenter syndrome 1 | `AGREES` | — no shared vocabulary |
| CCS2 | `MONDO:0014573` | Cole-Carpenter syndrome 2 | `AGREES` | — no shared vocabulary |

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
