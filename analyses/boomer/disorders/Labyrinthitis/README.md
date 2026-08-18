# Labyrinthitis

Boomer grounding analysis for [`kb/disorders/Labyrinthitis.yaml`](../../../../kb/disorders/Labyrinthitis.yaml).

- **Entry term:** [`MONDO:0002008`](http://purl.obolibrary.org/obo/MONDO_0002008) labyrinthitis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Viral labyrinthitis | `MONDO:0001507` | viral labyrinthitis | `AGREES` |
| Bacterial (suppurative) labyrinthitis | `MONDO:0001739` | purulent labyrinthitis | `AGREES` |
| Serous labyrinthitis | `MONDO:0002006` | serous labyrinthitis | `AGREES` |

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
