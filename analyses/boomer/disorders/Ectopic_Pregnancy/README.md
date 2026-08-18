# Ectopic Pregnancy

Boomer grounding analysis for [`kb/disorders/Ectopic_Pregnancy.yaml`](../../../../kb/disorders/Ectopic_Pregnancy.yaml).

- **Entry term:** [`MONDO:0000755`](http://purl.obolibrary.org/obo/MONDO_0000755) ectopic pregnancy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Tubal | `MONDO:0043762` | tubal pregnancy | `AGREES` |
| Interstitial | `MONDO:0044101` | pregnancy, cornual | `AGREES` |
| Ovarian | `MONDO:0044098` | ovarian ectopic pregnancy | `AGREES` |
| Abdominal | `MONDO:0043759` | abdominal ectopic pregnancy | `AGREES` |

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
