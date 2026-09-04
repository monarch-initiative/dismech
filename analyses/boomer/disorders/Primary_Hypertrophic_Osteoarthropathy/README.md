# Primary Hypertrophic Osteoarthropathy

Boomer grounding analysis for [`kb/disorders/Primary_Hypertrophic_Osteoarthropathy.yaml`](../../../../kb/disorders/Primary_Hypertrophic_Osteoarthropathy.yaml).

- **Entry term:** [`MONDO:0016620`](http://purl.obolibrary.org/obo/MONDO_0016620) primary hypertrophic osteoarthropathy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PHOAR1 | `MONDO:0024546` | hypertrophic osteoarthropathy, primary, autosomal recessive, 1 | `AGREES` | — no shared vocabulary |
| PHOAR2 | `MONDO:0013756` | hypertrophic osteoarthropathy, primary, autosomal recessive, 2 | `AGREES` | — no shared vocabulary |
| PHOAD | `MONDO:0008172` | hypertrophic osteoarthropathy, primary, autosomal dominant | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0016620` ≡ `ORDO:2796`

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
