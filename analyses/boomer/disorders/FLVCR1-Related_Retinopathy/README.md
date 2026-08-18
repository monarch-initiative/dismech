# FLVCR1-Related Retinopathy with or without Ataxia

Boomer grounding analysis for [`kb/disorders/FLVCR1-Related_Retinopathy.yaml`](../../../../kb/disorders/FLVCR1-Related_Retinopathy.yaml).

- **Entry term:** [`MONDO:0100449`](http://purl.obolibrary.org/obo/MONDO_0100449) FLVCR1-related retinopathy with or without ataxia
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PCARP | `MONDO:0012177` | posterior column ataxia-retinitis pigmentosa syndrome | `AGREES` | — no shared vocabulary |

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
