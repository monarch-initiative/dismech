# Auditory Neuropathy

Boomer grounding analysis for [`kb/disorders/Auditory_Neuropathy.yaml`](../../../../kb/disorders/Auditory_Neuropathy.yaml).

- **Entry term:** [`MONDO:0021944`](http://purl.obolibrary.org/obo/MONDO_0021944) auditory neuropathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| AUNA1 | `MONDO:0012196` | autosomal dominant auditory neuropathy 1 | `AGREES` | silent (MESH) |
| AUNA2 | `MONDO:0957279` | auditory neuropathy, autosomal dominant 2 | `AGREES` | — no shared vocabulary |
| AUNA3 | `MONDO:0859235` | auditory neuropathy, autosomal dominant 3 | `AGREES` | — no shared vocabulary |
| DFNB9 | `MONDO:0010986` | autosomal recessive nonsyndromic hearing loss 9 | `AGREES` | — no shared vocabulary |
| AUNX1 | `MONDO:0010378` | X-linked hereditary sensory and autonomic neuropathy with hearing loss | `AGREES` | silent (MESH) |

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
