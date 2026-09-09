# Congenital Stationary Night Blindness

Boomer grounding analysis for [`kb/disorders/Congenital_Stationary_Night_Blindness.yaml`](../../../../kb/disorders/Congenital_Stationary_Night_Blindness.yaml).

- **Entry term:** [`MONDO:0016293`](http://purl.obolibrary.org/obo/MONDO_0016293) congenital stationary night blindness
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| cCSNB | `MONDO:0010690` | congenital stationary night blindness 1A | `AGREES` | ✓ DOID |
| icCSNB | `MONDO:0010241` | congenital stationary night blindness 2A | `AGREES` | ✓ DOID |
| Riggs | `MONDO:0012498` | congenital stationary night blindness autosomal dominant 1 | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0016293` ≡ `DOID:0050534`
- `MONDO:0016293` ≡ `icd11f:122338861`

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
