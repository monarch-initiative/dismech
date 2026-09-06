# Androgen Insensitivity Syndrome

Boomer grounding analysis for [`kb/disorders/Androgen_Insensitivity_Syndrome.yaml`](../../../../kb/disorders/Androgen_Insensitivity_Syndrome.yaml).

- **Entry term:** [`MONDO:0019154`](http://purl.obolibrary.org/obo/MONDO_0019154) androgen insensitivity syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CAIS | `MONDO:0021023` | complete androgen insensitivity syndrome | `AGREES` | ✓ DOID, ICD10CM, NCIT, ORDO |
| PAIS | `MONDO:0010720` | partial androgen insensitivity syndrome | `AGREES` | ✓ DOID, ICD10CM, NCIT, ORDO |

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
