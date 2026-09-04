# Familial Long QT Syndrome

Boomer grounding analysis for [`kb/disorders/Long_QT_Syndrome.yaml`](../../../../kb/disorders/Long_QT_Syndrome.yaml).

- **Entry term:** [`MONDO:0019171`](http://purl.obolibrary.org/obo/MONDO_0019171) familial long QT syndrome
- **Grounded subtypes:** 15
- **Verdicts:** AGREES 15

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0100316` | long QT syndrome 1 | `AGREES` | — no shared vocabulary |
| Type 2 | `MONDO:0013367` | long QT syndrome 2 | `AGREES` | — no shared vocabulary |
| Type 3 | `MONDO:0011377` | long QT syndrome 3 | `AGREES` | — no shared vocabulary |
| Type 4 | `MONDO:0800323` | long QT syndrome 4 | `AGREES` | — no shared vocabulary |
| Type 5 | `MONDO:0013372` | long QT syndrome 5 | `AGREES` | — no shared vocabulary |
| Type 6 | `MONDO:0013370` | long QT syndrome 6 | `AGREES` | — no shared vocabulary |
| Type 8 | `MONDO:0032756` | long QT syndrome 8 | `AGREES` | — no shared vocabulary |
| Type 9 | `MONDO:0012736` | long QT syndrome 9 | `AGREES` | — no shared vocabulary |
| Type 10 | `MONDO:0012737` | long QT syndrome 10 | `AGREES` | — no shared vocabulary |
| Type 11 | `MONDO:0012738` | long QT syndrome 11 | `AGREES` | — no shared vocabulary |
| Type 12 | `MONDO:0013062` | long QT syndrome 12 | `AGREES` | — no shared vocabulary |
| Type 13 | `MONDO:0013279` | long QT syndrome 13 | `AGREES` | — no shared vocabulary |
| Type 14 | `MONDO:0014548` | long QT syndrome 14 | `AGREES` | — no shared vocabulary |
| Type 15 | `MONDO:0014550` | long QT syndrome 15 | `AGREES` | — no shared vocabulary |
| Type 16 | `MONDO:0032915` | long QT syndrome 16 | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0019171` ≡ `ORDO:101016`

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
