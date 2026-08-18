# Invasive Candidiasis

Boomer grounding analysis for [`kb/disorders/Invasive_Candidiasis.yaml`](../../../../kb/disorders/Invasive_Candidiasis.yaml).

- **Entry term:** [`MONDO:0044067`](http://purl.obolibrary.org/obo/MONDO_0044067) candidiasis, invasive
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Candidemia | `MONDO:0044070` | candidemia | `AGREES` |

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
