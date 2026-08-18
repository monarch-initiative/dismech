# KCNH1 Associated Disorder

Boomer grounding analysis for [`kb/disorders/KCNH1_Associated_Disorder.yaml`](../../../../kb/disorders/KCNH1_Associated_Disorder.yaml).

- **Entry term:** [`MONDO:0100485`](http://purl.obolibrary.org/obo/MONDO_0100485) KCNH1 associated disorder
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| TBS | `MONDO:0012735` | Temple-Baraitser syndrome | `AGREES` |
| ZLS1 | `MONDO:0024526` | Zimmermann-Laband syndrome 1 | `AGREES` |

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
