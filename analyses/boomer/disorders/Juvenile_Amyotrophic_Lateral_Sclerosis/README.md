# Juvenile Amyotrophic Lateral Sclerosis

Boomer grounding analysis for [`kb/disorders/Juvenile_Amyotrophic_Lateral_Sclerosis.yaml`](../../../../kb/disorders/Juvenile_Amyotrophic_Lateral_Sclerosis.yaml).

- **Entry term:** [`MONDO:0017593`](http://purl.obolibrary.org/obo/MONDO_0017593) juvenile amyotrophic lateral sclerosis
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 4, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ALS2 | `MONDO:0008780` | amyotrophic lateral sclerosis type 2, juvenile | `AGREES` | — no shared vocabulary |
| ALS4 | `MONDO:0011223` | amyotrophic lateral sclerosis type 4 | `SILENT` | silent (ORDO) |
| ALS5 | `MONDO:0011196` | amyotrophic lateral sclerosis type 5 | `AGREES` | — no shared vocabulary |
| ALS16 | `MONDO:0013715` | amyotrophic lateral sclerosis type 16 | `AGREES` | — no shared vocabulary |
| ALS27 | `MONDO:0859529` | amyotrophic lateral sclerosis 27, juvenile | `SILENT` | — no shared vocabulary |
| JALS with dementia | `MONDO:0008781` | juvenile amyotrophic lateral sclerosis with dementia | `AGREES` | — no shared vocabulary |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
