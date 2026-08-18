# Capillary Malformation-Arteriovenous Malformation Syndrome

Boomer grounding analysis for [`kb/disorders/Capillary_Malformation-Arteriovenous_Malformation_Syndrome.yaml`](../../../../kb/disorders/Capillary_Malformation-Arteriovenous_Malformation_Syndrome.yaml).

- **Entry term:** [`MONDO:0012016`](http://purl.obolibrary.org/obo/MONDO_0012016) capillary malformation-arteriovenous malformation syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| CM-AVM1 | `MONDO:0020783` | capillary malformation-arteriovenous malformation 1 | `AGREES` |
| CM-AVM2 | `MONDO:0020785` | capillary malformation-arteriovenous malformation 2 | `AGREES` |

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
