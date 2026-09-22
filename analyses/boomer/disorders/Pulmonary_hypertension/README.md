# Pulmonary_hypertension

Boomer grounding analysis for [`kb/disorders/Pulmonary_hypertension.yaml`](../../../../kb/disorders/Pulmonary_hypertension.yaml).

- **Entry term:** [`MONDO:0005149`](http://purl.obolibrary.org/obo/MONDO_0005149) pulmonary hypertension
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Pulmonary Arterial Hypertension (PAH) | `MONDO:0015924` | pulmonary arterial hypertension | `AGREES` | ✓ icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0015924` ≡ `ORDO:182090`

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
