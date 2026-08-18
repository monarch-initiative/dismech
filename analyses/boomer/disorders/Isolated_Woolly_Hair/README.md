# Isolated Woolly Hair

Boomer grounding analysis for [`kb/disorders/Isolated_Woolly_Hair.yaml`](../../../../kb/disorders/Isolated_Woolly_Hair.yaml).

- **Entry term:** [`MONDO:0008686`](http://purl.obolibrary.org/obo/MONDO_0008686) isolated familial wooly hair disorder
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SAME_TERM 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| ARWH1 | `MONDO:0800312` | wooly hair, autosomal recessive 1, with or without hypotrichosis | `AGREES` |
| ARWH2 | `MONDO:0008686` | isolated familial wooly hair disorder | `SAME_TERM` |
| ADWH | `MONDO:0020717` | autosomal dominant wooly hair | `AGREES` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Isolated_Woolly_Hair` ≡ `MONDO:0008686`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
