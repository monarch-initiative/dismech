# Autosomal Recessive Non-Syndromic Intellectual Disability

Boomer grounding analysis for [`kb/disorders/Autosomal_Recessive_Non-Syndromic_Intellectual_Disability.yaml`](../../../../kb/disorders/Autosomal_Recessive_Non-Syndromic_Intellectual_Disability.yaml).

- **Entry term:** [`MONDO:0019502`](http://purl.obolibrary.org/obo/MONDO_0019502) autosomal recessive non-syndromic intellectual disability
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 10

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MRT1 | `MONDO:0009580` | intellectual disability, autosomal recessive 1 | `AGREES` | ✓ DOID |
| MRT2 | `MONDO:0011828` | intellectual disability, autosomal recessive 2 | `AGREES` | ✓ DOID |
| MRT3 | `MONDO:0012037` | intellectual disability, autosomal recessive 3 | `AGREES` | ✓ DOID |
| MRT5 | `MONDO:0012613` | intellectual disability, autosomal recessive 5 | `AGREES` | ✓ DOID |
| MRT6 | `MONDO:0012614` | intellectual disability, autosomal recessive 6 | `AGREES` | ✓ DOID |
| MRT7 | `MONDO:0012615` | intellectual disability, autosomal recessive 7 | `AGREES` | ✓ DOID |
| MRT13 | `MONDO:0013173` | intellectual disability, autosomal recessive 13 | `AGREES` | ✓ DOID |
| MRT15 | `MONDO:0013624` | Rafiq syndrome | `AGREES` | ✓ DOID |
| MRT18 | `MONDO:0013651` | intellectual disability, autosomal recessive 18 | `AGREES` | ✓ DOID |
| MRT57 | `MONDO:0014962` | intellectual disability, autosomal recessive 57 | `AGREES` | ✓ DOID |

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
