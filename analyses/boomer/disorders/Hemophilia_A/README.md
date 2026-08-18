# Hemophilia A

Boomer grounding analysis for [`kb/disorders/Hemophilia_A.yaml`](../../../../kb/disorders/Hemophilia_A.yaml).

- **Entry term:** [`MONDO:0010602`](http://purl.obolibrary.org/obo/MONDO_0010602) hemophilia A
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Severe Hemophilia A | `MONDO:0015719` | severe hemophilia A | `AGREES` |
| Moderate Hemophilia A | `MONDO:0015720` | moderately severe hemophilia A | `AGREES` |
| Mild Hemophilia A | `MONDO:0015721` | mild hemophilia A | `AGREES` |

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
