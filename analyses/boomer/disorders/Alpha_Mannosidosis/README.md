# Alpha-mannosidosis

Boomer grounding analysis for [`kb/disorders/Alpha_Mannosidosis.yaml`](../../../../kb/disorders/Alpha_Mannosidosis.yaml).

- **Entry term:** [`MONDO:0009561`](http://purl.obolibrary.org/obo/MONDO_0009561) alpha-mannosidosis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Infantile form | `MONDO:0017732` | alpha-mannosidosis, infantile form | `AGREES` |
| Adult form | `MONDO:0017733` | alpha-mannosidosis, adult form | `AGREES` |

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
