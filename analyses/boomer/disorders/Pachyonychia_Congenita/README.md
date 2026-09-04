# Pachyonychia Congenita

Boomer grounding analysis for [`kb/disorders/Pachyonychia_Congenita.yaml`](../../../../kb/disorders/Pachyonychia_Congenita.yaml).

- **Entry term:** [`MONDO:0016471`](http://purl.obolibrary.org/obo/MONDO_0016471) pachyonychia congenita
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PC-K6a | `MONDO:0014324` | pachyonychia congenita 3 | `AGREES` | — no shared vocabulary |
| PC-K6b | `MONDO:0014325` | pachyonychia congenita 4 | `AGREES` | — no shared vocabulary |
| PC-K16 | `MONDO:0008173` | pachyonychia congenita 1 | `AGREES` | — no shared vocabulary |
| PC-K17 | `MONDO:0008174` | pachyonychia congenita 2 | `AGREES` | — no shared vocabulary |

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
