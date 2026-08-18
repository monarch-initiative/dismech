# Familial Sleep-Related Hypermotor Epilepsy

Boomer grounding analysis for [`kb/disorders/Familial_Sleep_Related_Hypermotor_Epilepsy.yaml`](../../../../kb/disorders/Familial_Sleep_Related_Hypermotor_Epilepsy.yaml).

- **Entry term:** [`MONDO:0000030`](http://purl.obolibrary.org/obo/MONDO_0000030) familial sleep-related hypermotor epilepsy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0010899` | autosomal dominant nocturnal frontal lobe epilepsy 1 | `AGREES` |
| Type 2 | `MONDO:0011297` | autosomal dominant nocturnal frontal lobe epilepsy 2 | `AGREES` |
| Type 3 | `MONDO:0011545` | autosomal dominant nocturnal frontal lobe epilepsy 3 | `AGREES` |
| Type 4 | `MONDO:0012474` | autosomal dominant nocturnal frontal lobe epilepsy 4 | `AGREES` |
| Type 5 | `MONDO:0014002` | autosomal dominant nocturnal frontal lobe epilepsy 5 | `AGREES` |

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
