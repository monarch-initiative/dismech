# Wieacker-Wolff Syndrome Spectrum

Boomer grounding analysis for [`kb/disorders/Wieacker_Wolff_Syndrome.yaml`](../../../../kb/disorders/Wieacker_Wolff_Syndrome.yaml).

- **Entry term:** [`MONDO:0025445`](http://purl.obolibrary.org/obo/MONDO_0025445) Wieacker-Wolff syndrome (spectrum)
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Classic XLR WWS | `MONDO:0010758` | Wieacker-Wolff syndrome | `AGREES` | — no shared vocabulary |
| Female-restricted XLD WWS | `MONDO:0026762` | Wieacker-Wolff syndrome, female-restricted | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0010758` ≡ `ORDO:3454`

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
