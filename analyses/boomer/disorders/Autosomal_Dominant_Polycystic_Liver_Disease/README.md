# Autosomal dominant polycystic liver disease

Boomer grounding analysis for [`kb/disorders/Autosomal_Dominant_Polycystic_Liver_Disease.yaml`](../../../../kb/disorders/Autosomal_Dominant_Polycystic_Liver_Disease.yaml).

- **Entry term:** [`MONDO:0000447`](http://purl.obolibrary.org/obo/MONDO_0000447) autosomal dominant polycystic liver disease
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PCLD1 | `MONDO:0008265` | polycystic liver disease 1 | `AGREES` |
| PCLD2 | `MONDO:0014860` | polycystic liver disease 2 | `AGREES` |

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
