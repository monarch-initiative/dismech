# D-2-Hydroxyglutaric Aciduria

Boomer grounding analysis for [`kb/disorders/D-2-Hydroxyglutaric_Aciduria.yaml`](../../../../kb/disorders/D-2-Hydroxyglutaric_Aciduria.yaml).

- **Entry term:** [`MONDO:0010924`](http://purl.obolibrary.org/obo/MONDO_0010924) D-2-hydroxyglutaric aciduria
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| D-2-HGA type I | `MONDO:0024554` | D-2-hydroxyglutaric aciduria 1 | `AGREES` |
| D-2-HGA type II | `MONDO:0013345` | d-2-hydroxyglutaric aciduria 2 | `AGREES` |

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
