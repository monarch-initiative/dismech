# Galactosemia

Boomer grounding analysis for [`kb/disorders/Galactosemia.yaml`](../../../../kb/disorders/Galactosemia.yaml).

- **Entry term:** [`MONDO:0018116`](http://purl.obolibrary.org/obo/MONDO_0018116) galactosemia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Classic Galactosemia | `MONDO:0009258` | classic galactosemia | `AGREES` |
| Galactokinase Deficiency | `MONDO:0009255` | galactokinase deficiency | `AGREES` |
| Epimerase Deficiency | `MONDO:0009257` | galactose epimerase deficiency | `AGREES` |

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
