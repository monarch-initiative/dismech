# Amyloidosis

Boomer grounding analysis for [`kb/disorders/Amyloidosis.yaml`](../../../../kb/disorders/Amyloidosis.yaml).

- **Entry term:** [`MONDO:0019065`](http://purl.obolibrary.org/obo/MONDO_0019065) amyloidosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| AL | `MONDO:0019438` | AL amyloidosis | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |
| ATTRwt | `MONDO:0018018` | wild type ATTR amyloidosis | `AGREES` | ✓ DOID, ICD10CM, ORDO |
| AA | `MONDO:0019439` | AA amyloidosis | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0019438` ≡ `icd11f:1061366491`

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
