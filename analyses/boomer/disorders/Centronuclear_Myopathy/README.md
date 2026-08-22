# Centronuclear Myopathy

Boomer grounding analysis for [`kb/disorders/Centronuclear_Myopathy.yaml`](../../../../kb/disorders/Centronuclear_Myopathy.yaml).

- **Entry term:** [`MONDO:0018947`](http://purl.obolibrary.org/obo/MONDO_0018947) centronuclear myopathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| XLMTM | `MONDO:0010683` | X-linked myotubular myopathy | `AGREES` | ✓ DOID, ICD10CM, ORDO |
| AD-CNM | `MONDO:0008048` | autosomal dominant centronuclear myopathy | `AGREES` | ✓ DOID, ORDO |
| AR-CNM | `MONDO:0009709` | myopathy, centronuclear, 2 | `AGREES` | ✓ DOID |
| RYR1-CNM | `MONDO:0015705` | autosomal recessive centronuclear myopathy | `AGREES` | ✓ DOID, ORDO, icd11f |
| SPEG-CNM | `MONDO:0014418` | myopathy, centronuclear, 5 | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0008048` ≡ `DOID:0111217`

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
