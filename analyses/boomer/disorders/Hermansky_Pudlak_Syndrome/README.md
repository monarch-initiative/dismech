# Hermansky-Pudlak Syndrome

Boomer grounding analysis for [`kb/disorders/Hermansky_Pudlak_Syndrome.yaml`](../../../../kb/disorders/Hermansky_Pudlak_Syndrome.yaml).

- **Entry term:** [`MONDO:0019312`](http://purl.obolibrary.org/obo/MONDO_0019312) Hermansky-Pudlak syndrome
- **Grounded subtypes:** 11
- **Verdicts:** AGREES 11

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HPS-1 | `MONDO:0008748` | Hermansky-Pudlak syndrome 1 | `AGREES` | ✓ DOID, NCIT |
| HPS-2 | `MONDO:0011997` | Hermansky-Pudlak syndrome 2 | `AGREES` | ✓ DOID, NCIT, ORDO |
| HPS-3 | `MONDO:0013555` | Hermansky-Pudlak syndrome 3 | `AGREES` | ✓ DOID |
| HPS-4 | `MONDO:0013556` | Hermansky-Pudlak syndrome 4 | `AGREES` | ✓ DOID |
| HPS-5 | `MONDO:0013557` | Hermansky-Pudlak syndrome 5 | `AGREES` | ✓ DOID |
| HPS-6 | `MONDO:0013558` | Hermansky-Pudlak syndrome 6 | `AGREES` | ✓ DOID, NCIT |
| HPS-7 | `MONDO:0013559` | Hermansky-Pudlak syndrome 7 | `AGREES` | ✓ DOID, ORDO |
| HPS-8 | `MONDO:0013560` | Hermansky-Pudlak syndrome 8 | `AGREES` | ✓ DOID |
| HPS-9 | `MONDO:0013606` | Hermansky-Pudlak syndrome 9 | `AGREES` | ✓ DOID |
| HPS-10 | `MONDO:0014885` | Hermansky-Pudlak syndrome 10 | `AGREES` | ✓ ORDO |
| HPS-11 | `MONDO:0030903` | Hermansky-Pudlak syndrome 11 | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0011997` ≡ `ORDO:183678`

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
