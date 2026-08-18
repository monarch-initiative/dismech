# Toxic Shock Syndrome

Boomer grounding analysis for [`kb/disorders/Toxic_Shock_Syndrome.yaml`](../../../../kb/disorders/Toxic_Shock_Syndrome.yaml).

- **Entry term:** [`MONDO:0001881`](http://purl.obolibrary.org/obo/MONDO_0001881) toxic shock syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Staphylococcal TSS | `MONDO:0020545` | staphylococcal toxic-shock syndrome | `AGREES` |
| Streptococcal TSS | `MONDO:0020544` | streptococcal toxic-shock syndrome | `AGREES` |

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
