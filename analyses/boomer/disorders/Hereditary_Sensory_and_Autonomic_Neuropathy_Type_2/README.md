# Hereditary Sensory and Autonomic Neuropathy Type 2

Boomer grounding analysis for [`kb/disorders/Hereditary_Sensory_and_Autonomic_Neuropathy_Type_2.yaml`](../../../../kb/disorders/Hereditary_Sensory_and_Autonomic_Neuropathy_Type_2.yaml).

- **Entry term:** [`MONDO:0019941`](http://purl.obolibrary.org/obo/MONDO_0019941) hereditary sensory and autonomic neuropathy type 2
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HSAN2A | `MONDO:0024309` | neuropathy, hereditary sensory and autonomic, type 2A | `AGREES` | ✓ DOID |
| HSAN2B | `MONDO:0013142` | neuropathy, hereditary sensory and autonomic, type 2B | `AGREES` | ✓ DOID |
| HSAN2C | `MONDO:0013634` | neuropathy, hereditary sensory, type 2C | `AGREES` | ✓ DOID |

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
