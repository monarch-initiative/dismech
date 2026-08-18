# Appendiceal Neoplasm

Boomer grounding analysis for [`kb/disorders/Appendiceal_Neoplasm.yaml`](../../../../kb/disorders/Appendiceal_Neoplasm.yaml).

- **Entry term:** [`MONDO:0001236`](http://purl.obolibrary.org/obo/MONDO_0001236) appendiceal neoplasm
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Adenocarcinoma | `MONDO:0006087` | appendix adenocarcinoma | `AGREES` |
| Goblet Cell Adenocarcinoma | `MONDO:0018017` | goblet cell carcinoma | `AGREES` |
| Neuroendocrine Tumor | `MONDO:0015066` | neuroendocrine tumor of the appendix, well differentiated, low or intermediate grade | `AGREES` |

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
