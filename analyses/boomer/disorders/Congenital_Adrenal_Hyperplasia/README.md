# Congenital Adrenal Hyperplasia

Boomer grounding analysis for [`kb/disorders/Congenital_Adrenal_Hyperplasia.yaml`](../../../../kb/disorders/Congenital_Adrenal_Hyperplasia.yaml).

- **Entry term:** [`MONDO:0018479`](http://purl.obolibrary.org/obo/MONDO_0018479) congenital adrenal hyperplasia
- **Grounded subtypes:** 8
- **Verdicts:** AGREES 8

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Classic 21-OHD | `MONDO:0008728` | classic congenital adrenal hyperplasia due to 21-hydroxylase deficiency | `AGREES` |
| Salt-Wasting 21-OHD | `MONDO:0017839` | classic congenital adrenal hyperplasia due to 21-hydroxylase deficiency, salt wasting form | `AGREES` |
| Simple-Virilizing 21-OHD | `MONDO:0017840` | classic congenital adrenal hyperplasia due to 21-hydroxylase deficiency, simple virilizing form | `AGREES` |
| Nonclassic 21-OHD | `MONDO:0023601` | non-classic congenital adrenal hyperplasia | `AGREES` |
| 11B-OHD | `MONDO:0008729` | congenital adrenal hyperplasia due to 11-beta-hydroxylase deficiency | `AGREES` |
| 17A-OHD | `MONDO:0008730` | congenital adrenal hyperplasia due to 17-alpha-hydroxylase deficiency | `AGREES` |
| 3B-HSD | `MONDO:0008727` | congenital adrenal hyperplasia due to 3-beta-hydroxysteroid dehydrogenase deficiency | `AGREES` |
| Lipoid CAH | `MONDO:0008725` | congenital lipoid adrenal hyperplasia due to STAR deficency | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
