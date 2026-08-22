# Pontocerebellar Hypoplasia

Boomer grounding analysis for [`kb/disorders/Pontocerebellar_Hypoplasia.yaml`](../../../../kb/disorders/Pontocerebellar_Hypoplasia.yaml).

- **Entry term:** [`MONDO:0020135`](http://purl.obolibrary.org/obo/MONDO_0020135) pontocerebellar hypoplasia
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PCH1A | `MONDO:0011866` | pontocerebellar hypoplasia type 1A | `AGREES` | ✓ DOID |
| PCH1B | `MONDO:0013853` | pontocerebellar hypoplasia type 1B | `AGREES` | ✓ DOID |
| PCH2 | `MONDO:0016759` | pontocerebellar hypoplasia type 2 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PCH4 | `MONDO:0009166` | pontocerebellar hypoplasia type 4 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PCH6 | `MONDO:0012683` | pontocerebellar hypoplasia type 6 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PCH10 | `MONDO:0014349` | pontocerebellar hypoplasia type 10 | `AGREES` | ✓ DOID, ORDO |

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
