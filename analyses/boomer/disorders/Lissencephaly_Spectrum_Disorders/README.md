# Lissencephaly Spectrum Disorders

Boomer grounding analysis for [`kb/disorders/Lissencephaly_Spectrum_Disorders.yaml`](../../../../kb/disorders/Lissencephaly_Spectrum_Disorders.yaml).

- **Entry term:** [`MONDO:0018838`](http://purl.obolibrary.org/obo/MONDO_0018838) lissencephaly spectrum disorders
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Classic/LIS1 | `MONDO:0015146` | classic lissencephaly | `AGREES` | ✓ ORDO |
| ARX-related | `MONDO:0010268` | X-linked lissencephaly with abnormal genitalia | `AGREES` | ✓ DOID, ORDO |
| RELN-related | `MONDO:0019450` | lissencephaly with cerebellar hypoplasia | `AGREES` | ✓ ORDO |
| Cobblestone | `MONDO:0018869` | cobblestone lissencephaly | `AGREES` | ✓ MESH, ORDO |

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
