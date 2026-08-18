# Carnitine Palmitoyltransferase II Deficiency

Boomer grounding analysis for [`kb/disorders/Carnitine_Palmitoyltransferase_II_Deficiency.yaml`](../../../../kb/disorders/Carnitine_Palmitoyltransferase_II_Deficiency.yaml).

- **Entry term:** [`MONDO:0015515`](http://purl.obolibrary.org/obo/MONDO_0015515) carnitine palmitoyltransferase II deficiency
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Myopathic | `MONDO:0009704` | carnitine palmitoyl transferase II deficiency, myopathic form | `AGREES` |
| Severe infantile | `MONDO:0010914` | carnitine palmitoyl transferase II deficiency, severe infantile form | `AGREES` |
| Lethal neonatal | `MONDO:0012136` | carnitine palmitoyl transferase II deficiency, neonatal form | `AGREES` |

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
