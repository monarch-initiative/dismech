# Benign Neonatal Seizures

Boomer grounding analysis for [`kb/disorders/Benign_Neonatal_Seizures.yaml`](../../../../kb/disorders/Benign_Neonatal_Seizures.yaml).

- **Entry term:** [`MONDO:0016027`](http://purl.obolibrary.org/obo/MONDO_0016027) benign neonatal seizures
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| KCNQ2-BFNS | `MONDO:0007365` | seizures, benign familial neonatal, 1 | `AGREES` | — no shared vocabulary |
| KCNQ3-BFNS | `MONDO:0007366` | seizures, benign familial neonatal, 2 | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0016027` ≡ `DOID:14264`

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
