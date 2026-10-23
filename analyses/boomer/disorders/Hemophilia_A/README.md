# Hemophilia A

Boomer grounding analysis for [`kb/disorders/Hemophilia_A.yaml`](../../../../kb/disorders/Hemophilia_A.yaml).

- **Entry term:** [`MONDO:0010602`](http://purl.obolibrary.org/obo/MONDO_0010602) hemophilia A
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Severe Hemophilia A | `MONDO:0015719` | severe hemophilia A | `AGREES` | ✓ ORDO |
| Moderate Hemophilia A | `MONDO:0015720` | moderately severe hemophilia A | `AGREES` | ✓ ORDO |
| Mild Hemophilia A | `MONDO:0015721` | mild hemophilia A | `AGREES` | ✓ ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0010602` ≡ `OMIM:306700`

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
