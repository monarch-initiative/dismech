# Morquio syndrome

Boomer grounding analysis for [`kb/disorders/Morquio_syndrome.yaml`](../../../../kb/disorders/Morquio_syndrome.yaml).

- **Entry term:** [`MONDO:0018938`](http://purl.obolibrary.org/obo/MONDO_0018938) mucopolysaccharidosis type 4
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type A | `MONDO:0009659` | mucopolysaccharidosis type 4A | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |
| Type B | `MONDO:0009660` | mucopolysaccharidosis type 4B | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |

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
