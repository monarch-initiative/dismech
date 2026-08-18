# Hereditary Elliptocytosis

Boomer grounding analysis for [`kb/disorders/Hereditary_Elliptocytosis.yaml`](../../../../kb/disorders/Hereditary_Elliptocytosis.yaml).

- **Entry term:** [`MONDO:0017319`](http://purl.obolibrary.org/obo/MONDO_0017319) hereditary elliptocytosis
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| EL1 | `MONDO:0012731` | elliptocytosis 1 | `AGREES` |
| EL2 | `MONDO:0007533` | elliptocytosis 2 | `AGREES` |
| EL3 | `MONDO:0054780` | elliptocytosis 3 | `AGREES` |
| SAO | `MONDO:0008165` | southeast Asian ovalocytosis | `AGREES` |
| Thermal-sensitive HE | `MONDO:0009334` | hemolytic anemia with thermal sensitivity of red cells | `AGREES` |

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
