# Autoimmune Polyendocrinopathy

Boomer grounding analysis for [`kb/disorders/Autoimmune_Polyendocrinopathy.yaml`](../../../../kb/disorders/Autoimmune_Polyendocrinopathy.yaml).

- **Entry term:** [`MONDO:0017278`](http://purl.obolibrary.org/obo/MONDO_0017278) autoimmune polyendocrinopathy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0009411` | autoimmune polyendocrine syndrome type 1 | `AGREES` |
| Type 2 | `MONDO:0010012` | autoimmune polyendocrinopathy type 2 | `AGREES` |
| Type 3 | `MONDO:0016422` | autoimmune polyendocrinopathy type 3 | `AGREES` |
| Type 4 | `MONDO:0016423` | autoimmune polyendocrinopathy type 4 | `AGREES` |

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
