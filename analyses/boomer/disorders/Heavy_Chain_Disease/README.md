# Heavy Chain Disease

Boomer grounding analysis for [`kb/disorders/Heavy_Chain_Disease.yaml`](../../../../kb/disorders/Heavy_Chain_Disease.yaml).

- **Entry term:** [`MONDO:0019464`](http://purl.obolibrary.org/obo/MONDO_0019464) heavy chain disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Alpha-HCD | `MONDO:0015045` | alpha-heavy chain disease | `AGREES` |
| Gamma-HCD | `MONDO:0015046` | gamma-heavy chain disease | `AGREES` |
| Mu-HCD | `MONDO:0015044` | mu-heavy chain disease | `AGREES` |

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
