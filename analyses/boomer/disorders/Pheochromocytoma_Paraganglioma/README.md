# Pheochromocytoma and Paraganglioma

Boomer grounding analysis for [`kb/disorders/Pheochromocytoma_Paraganglioma.yaml`](../../../../kb/disorders/Pheochromocytoma_Paraganglioma.yaml).

- **Entry term:** [`MONDO:0035540`](http://purl.obolibrary.org/obo/MONDO_0035540) pheochromocytoma-paraganglioma
- **Grounded subtypes:** 7
- **Verdicts:** SILENT 7

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PGL1 | `MONDO:0008192` | pheochromocytoma/paraganglioma syndrome 1 | `SILENT` | — no shared vocabulary |
| PGL2 | `MONDO:0011121` | pheochromocytoma/paraganglioma syndrome 2 | `SILENT` | — no shared vocabulary |
| PGL3 | `MONDO:0011544` | pheochromocytoma/paraganglioma syndrome 3 | `SILENT` | — no shared vocabulary |
| PGL4 | `MONDO:0007273` | pheochromocytoma/paraganglioma syndrome 4 | `SILENT` | — no shared vocabulary |
| PGL5 | `MONDO:0013602` | pheochromocytoma/paraganglioma syndrome 5 | `SILENT` | — no shared vocabulary |
| MAX-related | `MONDO:0700346` | MAX-related tumor predisposition | `SILENT` | — no shared vocabulary |
| TMEM127-related | `MONDO:0700345` | TMEM127-related tumor predisposition | `SILENT` | — no shared vocabulary |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

7 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
