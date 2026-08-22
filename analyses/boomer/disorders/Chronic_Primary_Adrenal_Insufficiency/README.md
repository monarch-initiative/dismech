# Chronic Primary Adrenal Insufficiency

Boomer grounding analysis for [`kb/disorders/Chronic_Primary_Adrenal_Insufficiency.yaml`](../../../../kb/disorders/Chronic_Primary_Adrenal_Insufficiency.yaml).

- **Entry term:** [`MONDO:0015129`](http://purl.obolibrary.org/obo/MONDO_0015129) chronic primary adrenal insufficiency
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Autoimmune Adrenalitis | `MONDO:0100480` | autoimmune primary adrenal insufficiency | `AGREES` | ✓ NCIT, ORDO |

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
