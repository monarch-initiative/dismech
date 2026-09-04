# Diphtheria

Boomer grounding analysis for [`kb/disorders/Diphtheria.yaml`](../../../../kb/disorders/Diphtheria.yaml).

- **Entry term:** [`MONDO:0005504`](http://purl.obolibrary.org/obo/MONDO_0005504) diphtheria
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Faucial | `MONDO:0020860` | faucial diphtheria | `AGREES` | silent (NCIT) |
| Laryngeal | `MONDO:0020863` | laryngeal diphtheria | `AGREES` | ✓ ICD10CM, icd11f |
| Anterior nasal | `MONDO:0020838` | anterior nasal diphtheria | `AGREES` | ✓ NCIT |
| Nasopharyngeal | `MONDO:0020866` | nasopharyngeal diphtheria | `AGREES` | ✓ ICD10CM |
| Cutaneous | `MONDO:0001479` | cutaneous diphtheria | `AGREES` | ✓ ICD10CM, icd11f |

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
