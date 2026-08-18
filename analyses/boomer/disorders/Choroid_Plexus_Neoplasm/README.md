# Choroid Plexus Neoplasm

Boomer grounding analysis for [`kb/disorders/Choroid_Plexus_Neoplasm.yaml`](../../../../kb/disorders/Choroid_Plexus_Neoplasm.yaml).

- **Entry term:** [`MONDO:0016717`](http://purl.obolibrary.org/obo/MONDO_0016717) choroid plexus neoplasm
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| CPP | `MONDO:0009837` | choroid plexus papilloma | `AGREES` |
| aCPP | `MONDO:0002684` | atypical choroid plexus papilloma | `AGREES` |
| CPC | `MONDO:0016718` | choroid plexus carcinoma | `AGREES` |

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
