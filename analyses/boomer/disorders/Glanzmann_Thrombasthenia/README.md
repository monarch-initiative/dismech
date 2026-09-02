# Glanzmann Thrombasthenia

Boomer grounding analysis for [`kb/disorders/Glanzmann_Thrombasthenia.yaml`](../../../../kb/disorders/Glanzmann_Thrombasthenia.yaml).

- **Entry term:** [`MONDO:0100326`](http://purl.obolibrary.org/obo/MONDO_0100326) Glanzmann thrombasthenia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| GT1 | `MONDO:0031332` | Glanzmann thrombasthenia 1 | `AGREES` | — no shared vocabulary |
| GT2 | `MONDO:0031009` | Glanzmann thrombasthenia 2 | `AGREES` | — no shared vocabulary |

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
