# Free Sialic Acid Storage Disease

Boomer grounding analysis for [`kb/disorders/Free_Sialic_Acid_Storage_Disease.yaml`](../../../../kb/disorders/Free_Sialic_Acid_Storage_Disease.yaml).

- **Entry term:** [`MONDO:0019366`](http://purl.obolibrary.org/obo/MONDO_0019366) free sialic acid storage disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Infantile Free Sialic Acid Storage Disease | `MONDO:0010027` | free sialic acid storage disease, infantile form | `AGREES` | ✓ ORDO |
| Salla Disease | `MONDO:0011449` | Salla disease | `AGREES` | ✓ ORDO |
| Intermediate Severe Salla Disease | `MONDO:0017737` | intermediate severe Salla disease | `AGREES` | ✓ ORDO |

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
