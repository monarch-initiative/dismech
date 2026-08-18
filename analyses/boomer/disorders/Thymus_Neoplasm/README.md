# Thymus Neoplasm

Boomer grounding analysis for [`kb/disorders/Thymus_Neoplasm.yaml`](../../../../kb/disorders/Thymus_Neoplasm.yaml).

- **Entry term:** [`MONDO:0005197`](http://purl.obolibrary.org/obo/MONDO_0005197) thymus neoplasm
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Thymoma | `MONDO:0006456` | thymoma | `AGREES` |
| Thymic carcinoma | `MONDO:0006451` | thymic carcinoma | `AGREES` |
| Thymic neuroendocrine tumors | `MONDO:0019964` | thymic neuroendocrine tumor | `AGREES` |

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
