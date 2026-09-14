# Myopathy, Lactic Acidosis, and Sideroblastic Anemia

Boomer grounding analysis for [`kb/disorders/Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml`](../../../../kb/disorders/Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml).

- **Entry term:** [`MONDO:0000863`](http://purl.obolibrary.org/obo/MONDO_0000863) myopathy, lactic acidosis, and sideroblastic anemia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MLASA1 | `MONDO:0024553` | myopathy, lactic acidosis, and sideroblastic anemia 1 | `AGREES` | ✓ DOID |
| MLASA2 | `MONDO:0013307` | myopathy, lactic acidosis, and sideroblastic anemia 2 | `AGREES` | ✓ DOID |
| MLASA3 | `MONDO:0010782` | myopathy, lactic acidosis, and sideroblastic anemia 3 | `AGREES` | ✓ DOID |

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
