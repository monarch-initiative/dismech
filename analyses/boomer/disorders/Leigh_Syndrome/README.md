# Leigh Syndrome

Boomer grounding analysis for [`kb/disorders/Leigh_Syndrome.yaml`](../../../../kb/disorders/Leigh_Syndrome.yaml).

- **Entry term:** [`MONDO:0009723`](http://purl.obolibrary.org/obo/MONDO_0009723) Leigh syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MILS | `MONDO:0016814` | maternally-inherited Leigh syndrome | `AGREES` | silent (MESH, ORDO) |
| French-Canadian | `MONDO:0009069` | congenital lactic acidosis, Saguenay-Lac-Saint-Jean type | `AGREES` | silent (DOID, MESH, OMIM, ORDO) |
| Leigh with cardiomyopathy | `MONDO:0019083` | Leigh syndrome with cardiomyopathy | `AGREES` | ✓ icd11f |
| Adult | `MONDO:0008069` | necrotizing encephalomyelopathy, subacute, of Leigh, adult | `AGREES` | silent (MESH, OMIM) |

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
