# Familial Atrial Fibrillation

Boomer grounding analysis for [`kb/disorders/Familial_Atrial_Fibrillation.yaml`](../../../../kb/disorders/Familial_Atrial_Fibrillation.yaml).

- **Entry term:** [`MONDO:0018054`](http://purl.obolibrary.org/obo/MONDO_0018054) familial atrial fibrillation
- **Grounded subtypes:** 18
- **Verdicts:** AGREES 18

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| KCNQ1-related | `MONDO:0011857` | atrial fibrillation, familial, 3 | `AGREES` |
| KCNE2-related | `MONDO:0012677` | atrial fibrillation, familial, 4 | `AGREES` |
| KCNJ2-related | `MONDO:0013513` | atrial fibrillation, familial, 9 | `AGREES` |
| GJA5-related | `MONDO:0013544` | atrial fibrillation, familial, 11 | `AGREES` |
| NPPA-related | `MONDO:0012816` | atrial fibrillation, familial, 6 | `AGREES` |
| SCN5A-related | `MONDO:0013530` | atrial fibrillation, familial, 10 | `AGREES` |
| KCNA5-related | `MONDO:0012828` | atrial fibrillation, familial, 7 | `AGREES` |
| ABCC9-related | `MONDO:0013545` | atrial fibrillation, familial, 12 | `AGREES` |
| SCN1B-related | `MONDO:0014155` | atrial fibrillation, familial, 13 | `AGREES` |
| SCN2B-related | `MONDO:0014156` | atrial fibrillation, familial, 14 | `AGREES` |
| NUP155-related | `MONDO:0014340` | atrial fibrillation, familial, 15 | `AGREES` |
| MYL4-related | `MONDO:0015001` | atrial fibrillation, familial, 18 | `AGREES` |
| ATFB1-locus | `MONDO:0012066` | atrial fibrillation, familial, 1 | `AGREES` |
| ATFB2-locus | `MONDO:0012167` | atrial fibrillation, familial, 2 | `AGREES` |
| ATFB5-locus | `MONDO:0012678` | atrial fibrillation, familial, 5 | `AGREES` |
| ATFB8-locus | `MONDO:0013100` | atrial fibrillation, familial, 8 | `AGREES` |
| ATFB16-locus | `MONDO:0800349` | atrial fibrillation, familial, 16 | `AGREES` |
| ATFB17-locus | `MONDO:0800345` | atrial fibrillation, familial, 17 | `AGREES` |

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
