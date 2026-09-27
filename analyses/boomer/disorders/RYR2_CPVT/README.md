# RYR2 CPVT

Boomer grounding analysis for [`kb/disorders/RYR2_CPVT.yaml`](../../../../kb/disorders/RYR2_CPVT.yaml).

- **Entry term:** [`MONDO:0017990`](http://purl.obolibrary.org/obo/MONDO_0017990) catecholaminergic polymorphic ventricular tachycardia
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CPVT1 | `MONDO:0011484` | catecholaminergic polymorphic ventricular tachycardia 1 | `AGREES` | ✓ DOID |
| CPVT2 | `MONDO:0012762` | catecholaminergic polymorphic ventricular tachycardia 2 | `AGREES` | ✓ DOID |
| CPVT3 | `MONDO:0013529` | catecholaminergic polymorphic ventricular tachycardia 3 | `AGREES` | ✓ DOID |
| CPVT4 | `MONDO:0013966` | catecholaminergic polymorphic ventricular tachycardia 4 | `AGREES` | ✓ DOID |
| CPVT5 | `MONDO:0014191` | catecholaminergic polymorphic ventricular tachycardia 5 | `AGREES` | ✓ DOID |

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
