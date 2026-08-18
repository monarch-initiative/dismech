# Inborn Disorder of Methionine Cycle and Sulfur Amino Acid Metabolism

Boomer grounding analysis for [`kb/disorders/Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml`](../../../../kb/disorders/Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml).

- **Entry term:** [`MONDO:0019222`](http://purl.obolibrary.org/obo/MONDO_0019222) inborn disorder of methionine cycle and sulfur amino acid metabolism
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| CBS deficiency | `MONDO:0009352` | classic homocystinuria | `AGREES` |
| MTHFR deficiency | `MONDO:0009353` | homocystinuria due to methylene tetrahydrofolate reductase deficiency | `AGREES` |
| cblC disease | `MONDO:0010184` | methylmalonic aciduria and homocystinuria type cblC | `AGREES` |
| MAT I/III deficiency | `MONDO:0009607` | methionine adenosyltransferase deficiency | `AGREES` |

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
