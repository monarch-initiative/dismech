# Pontocerebellar Hypoplasia

Boomer grounding analysis for [`kb/disorders/Pontocerebellar_Hypoplasia.yaml`](../../../../kb/disorders/Pontocerebellar_Hypoplasia.yaml).

- **Entry term:** [`MONDO:0020135`](http://purl.obolibrary.org/obo/MONDO_0020135) pontocerebellar hypoplasia
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PCH1A | `MONDO:0011866` | pontocerebellar hypoplasia type 1A | `AGREES` |
| PCH1B | `MONDO:0013853` | pontocerebellar hypoplasia type 1B | `AGREES` |
| PCH2 | `MONDO:0016759` | pontocerebellar hypoplasia type 2 | `AGREES` |
| PCH4 | `MONDO:0009166` | pontocerebellar hypoplasia type 4 | `AGREES` |
| PCH6 | `MONDO:0012683` | pontocerebellar hypoplasia type 6 | `AGREES` |
| PCH10 | `MONDO:0014349` | pontocerebellar hypoplasia type 10 | `AGREES` |

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
