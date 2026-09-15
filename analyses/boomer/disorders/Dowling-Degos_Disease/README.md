# Dowling-Degos Disease

Boomer grounding analysis for [`kb/disorders/Dowling-Degos_Disease.yaml`](../../../../kb/disorders/Dowling-Degos_Disease.yaml).

- **Entry term:** [`MONDO:0008371`](http://purl.obolibrary.org/obo/MONDO_0008371) Dowling-Degos disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| DDD1 | `MONDO:0024534` | Dowling-Degos disease 1 | `AGREES` | — no shared vocabulary |
| DDD2 | `MONDO:0014130` | Dowling-Degos disease 2 | `AGREES` | — no shared vocabulary |
| DDD4 | `MONDO:0014307` | Dowling-Degos disease 4 | `AGREES` | — no shared vocabulary |

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
