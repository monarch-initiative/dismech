# Treacher Collins Syndrome

Boomer grounding analysis for [`kb/disorders/Treacher_Collins_Syndrome.yaml`](../../../../kb/disorders/Treacher_Collins_Syndrome.yaml).

- **Entry term:** [`MONDO:0002457`](http://purl.obolibrary.org/obo/MONDO_0002457) Treacher-Collins syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| TCS1 | `MONDO:0007944` | Treacher Collins syndrome 1 | `AGREES` |
| TCS2 | `MONDO:0013385` | Treacher Collins syndrome 2 | `AGREES` |
| TCS3 | `MONDO:0009558` | Treacher Collins syndrome 3 | `AGREES` |
| TCS4 | `MONDO:0030067` | Treacher Collins syndrome 4 | `AGREES` |

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
