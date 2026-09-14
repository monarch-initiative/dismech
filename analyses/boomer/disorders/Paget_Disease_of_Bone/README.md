# Paget Disease of Bone

Boomer grounding analysis for [`kb/disorders/Paget_Disease_of_Bone.yaml`](../../../../kb/disorders/Paget_Disease_of_Bone.yaml).

- **Entry term:** [`MONDO:0005382`](http://purl.obolibrary.org/obo/MONDO_0005382) bone Paget disease
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| SQSTM1-related | `MONDO:0011183` | Paget disease of bone 2, early-onset | `AGREES` | ✓ DOID |
| ZNF687-related | `MONDO:0014792` | Paget disease of bone 6 | `AGREES` | ✓ DOID |

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
