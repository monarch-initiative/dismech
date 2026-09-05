# Shwachman-Diamond syndrome

Boomer grounding analysis for [`kb/disorders/Shwachman-Diamond_Syndrome.yaml`](../../../../kb/disorders/Shwachman-Diamond_Syndrome.yaml).

- **Entry term:** [`MONDO:0009833`](http://purl.obolibrary.org/obo/MONDO_0009833) Shwachman-Diamond syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| SBDS-related | `MONDO:0044204` | Shwachman-Diamond syndrome 1 | `AGREES` | — no shared vocabulary |
| DNAJC21-related | `MONDO:0700311` | DNAJC21-related Shwachman Diamond syndrome | `AGREES` | — no shared vocabulary |

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
