# Primary Hypertrophic Osteoarthropathy

Boomer grounding analysis for [`kb/disorders/Primary_Hypertrophic_Osteoarthropathy.yaml`](../../../../kb/disorders/Primary_Hypertrophic_Osteoarthropathy.yaml).

- **Entry term:** [`MONDO:0016620`](http://purl.obolibrary.org/obo/MONDO_0016620) primary hypertrophic osteoarthropathy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PHOAR1 | `MONDO:0024546` | hypertrophic osteoarthropathy, primary, autosomal recessive, 1 | `AGREES` |
| PHOAR2 | `MONDO:0013756` | hypertrophic osteoarthropathy, primary, autosomal recessive, 2 | `AGREES` |
| PHOAD | `MONDO:0008172` | hypertrophic osteoarthropathy, primary, autosomal dominant | `AGREES` |

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
