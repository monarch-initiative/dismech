# FAM111A-Related Skeletal Dysplasia

Boomer grounding analysis for [`kb/disorders/FAM111A-Related_Skeletal_Dysplasia.yaml`](../../../../kb/disorders/FAM111A-Related_Skeletal_Dysplasia.yaml).

- **Entry term:** [`MONDO:1060172`](http://purl.obolibrary.org/obo/MONDO_1060172) FAM111A-related skeletal dysplasia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| KCS2 | `MONDO:0007478` | autosomal dominant Kenny-Caffey syndrome | `AGREES` | — no shared vocabulary |
| OCS | `MONDO:0011215` | osteocraniostenosis | `AGREES` | — no shared vocabulary |

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
