# Yolk Sac Tumor

Boomer grounding analysis for [`kb/disorders/Yolk_Sac_Tumor.yaml`](../../../../kb/disorders/Yolk_Sac_Tumor.yaml).

- **Entry term:** [`MONDO:0005744`](http://purl.obolibrary.org/obo/MONDO_0005744) yolk sac tumor
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ovarian YST | `MONDO:0006344` | ovarian yolk sac tumor | `AGREES` |
| CNS YST | `MONDO:0016739` | yolk sac tumor of central nervous system | `AGREES` |

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
