# Brittle Cornea Syndrome

Boomer grounding analysis for [`kb/disorders/Brittle_Cornea_Syndrome.yaml`](../../../../kb/disorders/Brittle_Cornea_Syndrome.yaml).

- **Entry term:** [`MONDO:0009242`](http://purl.obolibrary.org/obo/MONDO_0009242) brittle cornea syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| BCS1 | `MONDO:0024543` | brittle cornea syndrome 1 | `AGREES` | — no shared vocabulary |
| BCS2 | `MONDO:0013605` | brittle cornea syndrome 2 | `AGREES` | silent (DOID) |

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
