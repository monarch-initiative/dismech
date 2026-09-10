# Undetermined Early-Onset Epileptic Encephalopathy

Boomer grounding analysis for [`kb/disorders/Undetermined_Early_Onset_Epileptic_Encephalopathy.yaml`](../../../../kb/disorders/Undetermined_Early_Onset_Epileptic_Encephalopathy.yaml).

- **Entry term:** [`MONDO:0018614`](http://purl.obolibrary.org/obo/MONDO_0018614) undetermined early-onset epileptic encephalopathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| DEE13 | `MONDO:0013801` | developmental and epileptic encephalopathy, 13 | `AGREES` | — no shared vocabulary |
| DEE21 | `MONDO:0014360` | developmental and epileptic encephalopathy, 21 | `AGREES` | — no shared vocabulary |
| DEE24 | `MONDO:0014377` | developmental and epileptic encephalopathy, 24 | `AGREES` | — no shared vocabulary |
| DEE25 | `MONDO:0014392` | developmental and epileptic encephalopathy, 25 | `AGREES` | — no shared vocabulary |
| DEE26 | `MONDO:0014477` | developmental and epileptic encephalopathy, 26 | `AGREES` | — no shared vocabulary |

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
