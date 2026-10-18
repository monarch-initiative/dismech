# Leiomyosarcoma

Boomer grounding analysis for [`kb/disorders/Leiomyosarcoma.yaml`](../../../../kb/disorders/Leiomyosarcoma.yaml).

- **Entry term:** [`MONDO:0005058`](http://purl.obolibrary.org/obo/MONDO_0005058) leiomyosarcoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SAME_TERM 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Uterine Leiomyosarcoma | `MONDO:0016262` | leiomyosarcoma of the corpus uteri | `AGREES` | ✓ NCIT |
| Retroperitoneal Leiomyosarcoma | `MONDO:0003370` | retroperitoneal leiomyosarcoma | `AGREES` | ✓ NCIT |
| Extremity or Truncal Leiomyosarcoma | `MONDO:0005058` | leiomyosarcoma | `SAME_TERM` | ✓ DOID, EFO, MESH, NCIT, ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Leiomyosarcoma#Extremity or Truncal Leiomyosarcoma` ≡ `MONDO:0005058`

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
