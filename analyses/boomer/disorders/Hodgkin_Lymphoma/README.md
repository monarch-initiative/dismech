# Hodgkin Lymphoma

Boomer grounding analysis for [`kb/disorders/Hodgkin_Lymphoma.yaml`](../../../../kb/disorders/Hodgkin_Lymphoma.yaml).

- **Entry term:** [`MONDO:0004952`](http://purl.obolibrary.org/obo/MONDO_0004952) Hodgkins lymphoma
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Classic HL | `MONDO:0009348` | classic Hodgkin lymphoma | `AGREES` |
| NLPHL | `MONDO:0044778` | nodular lymphocyte predominant Hodgkin lymphoma | `AGREES` |

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
