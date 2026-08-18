# Cerebral Cavernous Malformation

Boomer grounding analysis for [`kb/disorders/Cerebral_Cavernous_Malformation.yaml`](../../../../kb/disorders/Cerebral_Cavernous_Malformation.yaml).

- **Entry term:** [`MONDO:0000820`](http://purl.obolibrary.org/obo/MONDO_0000820) cerebral cavernous malformation
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Familial cerebral cavernous malformation | `MONDO:0031037` | famililal cerebral cavernous malformations | `AGREES` |
| CCM1 | `MONDO:0020724` | cerebral cavernous malformation 1 | `AGREES` |
| CCM2 | `MONDO:0011304` | cerebral cavernous malformation 2 | `AGREES` |
| CCM3 | `MONDO:0011305` | cerebral cavernous malformation 3 | `AGREES` |

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
