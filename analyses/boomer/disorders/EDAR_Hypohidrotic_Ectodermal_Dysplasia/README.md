# EDAR-Related Hypohidrotic Ectodermal Dysplasia

Boomer grounding analysis for [`kb/disorders/EDAR_Hypohidrotic_Ectodermal_Dysplasia.yaml`](../../../../kb/disorders/EDAR_Hypohidrotic_Ectodermal_Dysplasia.yaml).

- **Entry term:** [`MONDO:0016535`](http://purl.obolibrary.org/obo/MONDO_0016535) hypohidrotic ectodermal dysplasia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AR | `MONDO:0016619` | autosomal recessive hypohidrotic ectodermal dysplasia | `AGREES` |
| AD | `MONDO:0015884` | autosomal dominant hypohidrotic ectodermal dysplasia | `AGREES` |

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
