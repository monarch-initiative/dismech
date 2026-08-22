# Kabuki Syndrome

Boomer grounding analysis for [`kb/disorders/Kabuki_Syndrome.yaml`](../../../../kb/disorders/Kabuki_Syndrome.yaml).

- **Entry term:** [`MONDO:0016512`](http://purl.obolibrary.org/obo/MONDO_0016512) Kabuki syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| KMT2D-related Kabuki syndrome | `MONDO:0007843` | Kabuki syndrome 1 | `AGREES` | — no shared vocabulary |
| KDM6A-related Kabuki syndrome | `MONDO:0010465` | Kabuki syndrome 2 | `AGREES` | — no shared vocabulary |

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
