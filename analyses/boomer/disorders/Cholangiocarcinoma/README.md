# Cholangiocarcinoma

Boomer grounding analysis for [`kb/disorders/Cholangiocarcinoma.yaml`](../../../../kb/disorders/Cholangiocarcinoma.yaml).

- **Entry term:** [`MONDO:0019087`](http://purl.obolibrary.org/obo/MONDO_0019087) cholangiocarcinoma
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Intrahepatic | `MONDO:0003210` | intrahepatic cholangiocarcinoma | `AGREES` | ✓ DOID, NCIT |
| Perihilar | `MONDO:0003345` | hilar cholangiocarcinoma | `AGREES` | ✓ DOID, MESH, NCIT |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0003210` ≡ `icd11f:387909164`

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
