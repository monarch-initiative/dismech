# Wolfram Syndrome

Boomer grounding analysis for [`kb/disorders/Wolfram_Syndrome.yaml`](../../../../kb/disorders/Wolfram_Syndrome.yaml).

- **Entry term:** [`MONDO:0018105`](http://purl.obolibrary.org/obo/MONDO_0018105) Wolfram syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| WS1 | `MONDO:0009101` | Wolfram syndrome 1 | `AGREES` | ✓ DOID |
| WS2 | `MONDO:0011502` | Wolfram syndrome 2 | `AGREES` | ✓ DOID |

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
