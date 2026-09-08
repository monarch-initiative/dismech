# Brown-Vialetto-Van Laere Syndrome

Boomer grounding analysis for [`kb/disorders/Brown-Vialetto-Van_Laere_Syndrome.yaml`](../../../../kb/disorders/Brown-Vialetto-Van_Laere_Syndrome.yaml).

- **Entry term:** [`MONDO:0008891`](http://purl.obolibrary.org/obo/MONDO_0008891) riboflavin transporter deficiency
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Brown-Vialetto-van Laere syndrome 1 | `MONDO:0024537` | Brown-Vialetto-van Laere syndrome 1 | `AGREES` | ✓ DOID, ORDO |
| Brown-Vialetto-van Laere syndrome 2 | `MONDO:0013867` | Brown-Vialetto-van Laere syndrome 2 | `AGREES` | ✓ DOID, ORDO |

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
