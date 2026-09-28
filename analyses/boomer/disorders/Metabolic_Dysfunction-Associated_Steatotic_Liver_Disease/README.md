# Metabolic Dysfunction-Associated Steatotic Liver Disease

Boomer grounding analysis for [`kb/disorders/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease.yaml`](../../../../kb/disorders/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease.yaml).

- **Entry term:** [`MONDO:0013209`](http://purl.obolibrary.org/obo/MONDO_0013209) metabolic dysfunction-associated steatotic liver disease
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MASH | `MONDO:0007027` | metabolic dysfunction-associated steatohepatitis | `AGREES` | ✓ DOID, NCIT, icd11f |

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
