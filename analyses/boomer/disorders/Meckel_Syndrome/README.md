# Meckel Syndrome

Boomer grounding analysis for [`kb/disorders/Meckel_Syndrome.yaml`](../../../../kb/disorders/Meckel_Syndrome.yaml).

- **Entry term:** [`MONDO:0018921`](http://purl.obolibrary.org/obo/MONDO_0018921) Meckel syndrome
- **Grounded subtypes:** 12
- **Verdicts:** AGREES 12

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Meckel syndrome, type 1 | `MONDO:0009571` | Meckel syndrome, type 1 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 2 | `MONDO:0011296` | Meckel syndrome, type 2 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 3 | `MONDO:0011821` | Meckel syndrome, type 3 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 4 | `MONDO:0012626` | Meckel syndrome, type 4 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 5 | `MONDO:0012695` | Meckel syndrome, type 5 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 6 | `MONDO:0012848` | Meckel syndrome, type 6 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 8 | `MONDO:0013482` | Meckel syndrome, type 8 | `AGREES` | ✓ DOID |
| Meckel syndrome, type 9 | `MONDO:0013630` | Meckel syndrome, type 9 | `AGREES` | — no shared vocabulary |
| Meckel syndrome, type 10 | `MONDO:0013609` | Meckel syndrome, type 10 | `AGREES` | — no shared vocabulary |
| Meckel syndrome, type 11 | `MONDO:0014164` | Meckel syndrome, type 11 | `AGREES` | — no shared vocabulary |
| Meckel syndrome 13 | `MONDO:0033044` | Meckel syndrome 13 | `AGREES` | ✓ DOID |
| Meckel syndrome 14 | `MONDO:0030819` | meckel syndrome 14 | `AGREES` | — no shared vocabulary |

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
