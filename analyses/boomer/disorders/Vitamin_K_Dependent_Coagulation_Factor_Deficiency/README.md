# Vitamin K-Dependent Coagulation Factor Deficiency

Boomer grounding analysis for [`kb/disorders/Vitamin_K_Dependent_Coagulation_Factor_Deficiency.yaml`](../../../../kb/disorders/Vitamin_K_Dependent_Coagulation_Factor_Deficiency.yaml).

- **Entry term:** [`MONDO:0015722`](http://purl.obolibrary.org/obo/MONDO_0015722) congenital vitamin K-dependent coagulation factors deficiency
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| VKCFD1 | `MONDO:0010187` | vitamin K-dependent clotting factors, combined deficiency of, type 1 | `AGREES` | ✓ DOID |
| VKCFD2 | `MONDO:0011837` | vitamin K-dependent clotting factors, combined deficiency of, type 2 | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0015722` ≡ `ORDO:169826`

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
