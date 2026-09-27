# TGFBI Corneal Dystrophies

Boomer grounding analysis for [`kb/disorders/TGFBI_Corneal_Dystrophies.yaml`](../../../../kb/disorders/TGFBI_Corneal_Dystrophies.yaml).

- **Entry term:** [`MONDO:0000764`](http://purl.obolibrary.org/obo/MONDO_0000764) epithelial-stromal TGFBI dystrophy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| GCD1 | `MONDO:0007377` | granular corneal dystrophy type I | `AGREES` | ✓ DOID |
| GCD2 | `MONDO:0011855` | granular corneal dystrophy type II | `AGREES` | ✓ DOID |
| LCD1 | `MONDO:0007380` | lattice corneal dystrophy type I | `AGREES` | — no shared vocabulary |
| RBCD | `MONDO:0012043` | Reis-Bucklers corneal dystrophy | `AGREES` | ✓ DOID |
| TBCD | `MONDO:0011185` | Thiel-Behnke corneal dystrophy | `AGREES` | ✓ DOID |

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
