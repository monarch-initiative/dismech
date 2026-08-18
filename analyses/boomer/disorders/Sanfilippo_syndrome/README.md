# Sanfilippo syndrome

Boomer grounding analysis for [`kb/disorders/Sanfilippo_syndrome.yaml`](../../../../kb/disorders/Sanfilippo_syndrome.yaml).

- **Entry term:** [`MONDO:0018937`](http://purl.obolibrary.org/obo/MONDO_0018937) mucopolysaccharidosis type 3
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| MPS IIIA | `MONDO:0009655` | mucopolysaccharidosis type 3A | `AGREES` |
| MPS IIIB | `MONDO:0009656` | mucopolysaccharidosis type 3B | `AGREES` |
| MPS IIIC | `MONDO:0009657` | mucopolysaccharidosis type 3C | `AGREES` |
| MPS IIID | `MONDO:0009658` | mucopolysaccharidosis type 3D | `AGREES` |

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
