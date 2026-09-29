# Thrombophilia

Boomer grounding analysis for [`kb/disorders/Thrombophilia.yaml`](../../../../kb/disorders/Thrombophilia.yaml).

- **Entry term:** [`MONDO:0002305`](http://purl.obolibrary.org/obo/MONDO_0002305) thrombophilia
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Factor V Leiden Thrombophilia | `MONDO:0008560` | thrombophilia due to activated protein C resistance | `AGREES` | ✓ DOID, MESH |
| Prothrombin G20210A Thrombophilia | `MONDO:0008559` | thrombophilia due to thrombin defect | `AGREES` | ✓ DOID |
| Antithrombin III Deficiency | `MONDO:0013144` | hereditary antithrombin deficiency | `AGREES` | ✓ DOID, MESH |
| Protein C Deficiency | `MONDO:0019145` | hereditary thrombophilia due to congenital protein C deficiency | `AGREES` | ✓ DOID, MESH, NCIT, icd11f |
| Protein S Deficiency | `MONDO:0019144` | hereditary thrombophilia due to congenital protein S deficiency | `AGREES` | ✓ DOID, icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0019145` ≡ `MESH:C535424`

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
