# IFT140-related Recessive Ciliopathy

Boomer grounding analysis for [`kb/disorders/IFT140-related_Recessive_Ciliopathy.yaml`](../../../../kb/disorders/IFT140-related_Recessive_Ciliopathy.yaml).

- **Entry term:** [`MONDO:0100509`](http://purl.obolibrary.org/obo/MONDO_0100509) IFT140-related recessive ciliopathy
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Non-syndromic RP80 | `MONDO:0054708` | retinitis pigmentosa 80 | `AGREES` | — no shared vocabulary |

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
