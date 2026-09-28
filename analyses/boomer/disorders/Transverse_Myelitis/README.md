# Transverse Myelitis

Boomer grounding analysis for [`kb/disorders/Transverse_Myelitis.yaml`](../../../../kb/disorders/Transverse_Myelitis.yaml).

- **Entry term:** [`MONDO:0021553`](http://purl.obolibrary.org/obo/MONDO_0021553) transverse myelitis
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Acute TM | `MONDO:0015342` | acute transverse myelitis | `SILENT` | — no shared vocabulary |
| Idiopathic ATM | `MONDO:0015344` | idiopathic acute transverse myelitis | `SILENT` | — no shared vocabulary |
| MOG-IgG ATM | `MONDO:0035666` | acute transverse myelitis with anti-MOG antibodies | `SILENT` | — no shared vocabulary |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
