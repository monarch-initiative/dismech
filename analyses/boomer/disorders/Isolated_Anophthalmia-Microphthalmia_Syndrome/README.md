# Isolated Anophthalmia-Microphthalmia Syndrome

Boomer grounding analysis for [`kb/disorders/Isolated_Anophthalmia-Microphthalmia_Syndrome.yaml`](../../../../kb/disorders/Isolated_Anophthalmia-Microphthalmia_Syndrome.yaml).

- **Entry term:** [`MONDO:0016764`](http://purl.obolibrary.org/obo/MONDO_0016764) isolated anophthalmia-microphthalmia syndrome
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 8, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Colobomatous microphthalmia | `MONDO:0000170` | microphthalmia, isolated, with coloboma | `AGREES` |
| Posterior microphthalmia | `MONDO:0005514` | nanophthalmia | `AGREES` |
| MCOP1 | `MONDO:0009631` | isolated microphthalmia 1 | `SILENT` |
| MCOP2 | `MONDO:0012409` | isolated microphthalmia 2 | `AGREES` |
| MCOP3 | `MONDO:0012604` | isolated microphthalmia 3 | `AGREES` |
| MCOP4 | `MONDO:0013130` | isolated microphthalmia 4 | `AGREES` |
| MCOP5 | `MONDO:0012605` | isolated microphthalmia 5 | `SILENT` |
| MCOP6 | `MONDO:0013293` | isolated microphthalmia 6 | `AGREES` |
| MCOP7 | `MONDO:0013377` | isolated microphthalmia 7 | `AGREES` |
| MCOP8 | `MONDO:0014050` | isolated microphthalmia 8 | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
