# Zimmermann-Laband Syndrome

Boomer grounding analysis for [`kb/disorders/Zimmermann_Laband_Syndrome.yaml`](../../../../kb/disorders/Zimmermann_Laband_Syndrome.yaml).

- **Entry term:** [`MONDO:0000200`](http://purl.obolibrary.org/obo/MONDO_0000200) Zimmermann-Laband syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| ZLS1 | `MONDO:0024526` | Zimmermann-Laband syndrome 1 | `AGREES` |
| ZLS2 | `MONDO:0014646` | Zimmermann-Laband syndrome 2 | `AGREES` |
| ZLS3 | `MONDO:0032854` | Zimmermann-Laband syndrome 3 | `AGREES` |

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
