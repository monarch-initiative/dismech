# Antiphospholipid Syndrome

Boomer grounding analysis for [`kb/disorders/Antiphospholipid_Syndrome.yaml`](../../../../kb/disorders/Antiphospholipid_Syndrome.yaml).

- **Entry term:** [`MONDO:8000010`](http://purl.obolibrary.org/obo/MONDO_8000010) antiphospholipid syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Primary antiphospholipid syndrome | `MONDO:0005204` | primary antiphospholipid syndrome | `AGREES` |
| Secondary antiphospholipid syndrome | `MONDO:0021008` | secondary antiphospholipid syndrome | `AGREES` |
| Catastrophic antiphospholipid syndrome | `MONDO:0018737` | catastrophic antiphospholipid syndrome | `AGREES` |

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
