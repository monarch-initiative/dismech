# Sarcoglycanopathy

Boomer grounding analysis for [`kb/disorders/Sarcoglycanopathy.yaml`](../../../../kb/disorders/Sarcoglycanopathy.yaml).

- **Entry term:** [`MONDO:0016140`](http://purl.obolibrary.org/obo/MONDO_0016140) sarcoglycanopathy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| SGCA | `MONDO:0011968` | autosomal recessive limb-girdle muscular dystrophy type 2D | `AGREES` | ✓ ORDO |
| SGCB | `MONDO:0011423` | autosomal recessive limb-girdle muscular dystrophy type 2E | `AGREES` | ✓ ORDO |
| SGCG | `MONDO:0009677` | autosomal recessive limb-girdle muscular dystrophy type 2C | `AGREES` | ✓ ORDO |
| SGCD | `MONDO:0011028` | autosomal recessive limb-girdle muscular dystrophy type 2F | `AGREES` | ✓ ORDO |

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
