# Juvenile Idiopathic Arthritis

Boomer grounding analysis for [`kb/disorders/Juvenile_Idiopathic_Arthritis.yaml`](../../../../kb/disorders/Juvenile_Idiopathic_Arthritis.yaml).

- **Entry term:** [`MONDO:0011429`](http://purl.obolibrary.org/obo/MONDO_0011429) juvenile idiopathic arthritis
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Oligoarticular | `MONDO:0019433` | oligoarticular juvenile idiopathic arthritis | `AGREES` |
| Polyarticular RF-negative | `MONDO:0018456` | polyarticular juvenile idiopathic arthritis | `AGREES` |
| Polyarticular RF-positive | `MONDO:0018456` | polyarticular juvenile idiopathic arthritis | `AGREES` |
| Enthesitis-related | `MONDO:0019437` | enthesitis-related juvenile idiopathic arthritis | `AGREES` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Juvenile_Idiopathic_Arthritis#Polyarticular RF-negative` ≡ `MONDO:0018456`

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
