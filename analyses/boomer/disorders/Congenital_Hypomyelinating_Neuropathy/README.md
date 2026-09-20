# Congenital Hypomyelinating Neuropathy

Boomer grounding analysis for [`kb/disorders/Congenital_Hypomyelinating_Neuropathy.yaml`](../../../../kb/disorders/Congenital_Hypomyelinating_Neuropathy.yaml).

- **Entry term:** [`MONDO:0033352`](http://purl.obolibrary.org/obo/MONDO_0033352) neuropathy, congenital hypomelinating
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CHN1 | `MONDO:0011527` | Charcot-Marie-Tooth disease type 4E | `AGREES` | silent (DOID) |
| CHN2 | `MONDO:0020765` | neuropathy, congenital hypomyelinating, 2 | `AGREES` | silent (DOID) |
| CHN3 | `MONDO:0020766` | neuropathy, congenital hypomyelinating, 3 | `AGREES` | silent (DOID) |

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
