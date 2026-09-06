# Familial Thoracic Aortic Aneurysm and Aortic Dissection

Boomer grounding analysis for [`kb/disorders/Familial_Thoracic_Aortic_Aneurysm_and_Aortic_Dissection.yaml`](../../../../kb/disorders/Familial_Thoracic_Aortic_Aneurysm_and_Aortic_Dissection.yaml).

- **Entry term:** [`MONDO:0019625`](http://purl.obolibrary.org/obo/MONDO_0019625) familial thoracic aortic aneurysm and aortic dissection
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ACTA2-related | `MONDO:0012730` | aortic aneurysm, familial thoracic 6 | `AGREES` | — no shared vocabulary |
| MYH11-related | `MONDO:0007568` | aortic aneurysm, familial thoracic 4 | `AGREES` | — no shared vocabulary |
| MYLK-related | `MONDO:0013418` | aortic aneurysm, familial thoracic 7 | `AGREES` | — no shared vocabulary |
| PRKG1-related | `MONDO:0014187` | aortic aneurysm, familial thoracic 8 | `AGREES` | — no shared vocabulary |
| LOX-related | `MONDO:0014950` | aortic aneurysm, familial thoracic 10 | `AGREES` | — no shared vocabulary |
| MFAP5-related | `MONDO:0014514` | aortic aneurysm, familial thoracic 9 | `AGREES` | — no shared vocabulary |
| THSD4-related | `MONDO:0030731` | aortic aneurysm, familial thoracic 12 | `AGREES` | — no shared vocabulary |
| TGFBR2-candidate locus | `MONDO:0011770` | aortic aneurysm, familial thoracic 2 | `AGREES` | — no shared vocabulary |
| AAT1 linkage locus | `MONDO:0024559` | aortic aneurysm, familial thoracic 1 | `AGREES` | silent (ORDO) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
