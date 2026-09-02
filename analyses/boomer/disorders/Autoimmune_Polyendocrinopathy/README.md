# Autoimmune Polyendocrinopathy

Boomer grounding analysis for [`kb/disorders/Autoimmune_Polyendocrinopathy.yaml`](../../../../kb/disorders/Autoimmune_Polyendocrinopathy.yaml).

- **Entry term:** [`MONDO:0017278`](http://purl.obolibrary.org/obo/MONDO_0017278) autoimmune polyendocrinopathy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0009411` | autoimmune polyendocrine syndrome type 1 | `AGREES` | ✓ DOID, NCIT, ORDO |
| Type 2 | `MONDO:0010012` | autoimmune polyendocrinopathy type 2 | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |
| Type 3 | `MONDO:0016422` | autoimmune polyendocrinopathy type 3 | `AGREES` | ✓ ORDO, icd11f |
| Type 4 | `MONDO:0016423` | autoimmune polyendocrinopathy type 4 | `AGREES` | ✓ ORDO, icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0017278` ≡ `NCIT:C84576`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
