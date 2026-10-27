# Spinal Muscular Atrophy

Boomer grounding analysis for [`kb/disorders/Spinal_Muscular_Atrophy.yaml`](../../../../kb/disorders/Spinal_Muscular_Atrophy.yaml).

- **Entry term:** [`MONDO:0001516`](http://purl.obolibrary.org/obo/MONDO_0001516) spinal muscular atrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| SMA Type 1 (Werdnig-Hoffmann) | `MONDO:0009669` | spinal muscular atrophy, type 1 | `AGREES` | ✓ DOID, NCIT, icd11f |
| SMA Type 2 | `MONDO:0009673` | spinal muscular atrophy, type II | `AGREES` | ✓ DOID, icd11f |
| SMA Type 3 (Kugelberg-Welander) | `MONDO:0009672` | spinal muscular atrophy, type III | `AGREES` | ✓ DOID, NCIT, icd11f |
| SMA Type 4 | `MONDO:0010056` | spinal muscular atrophy, type IV | `AGREES` | ✓ DOID, icd11f |

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
