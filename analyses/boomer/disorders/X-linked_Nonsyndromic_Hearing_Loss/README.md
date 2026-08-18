# X-linked Nonsyndromic Hearing Loss

Boomer grounding analysis for [`kb/disorders/X-linked_Nonsyndromic_Hearing_Loss.yaml`](../../../../kb/disorders/X-linked_Nonsyndromic_Hearing_Loss.yaml).

- **Entry term:** [`MONDO:0019586`](http://purl.obolibrary.org/obo/MONDO_0019586) X-linked nonsyndromic hearing loss
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| DFNX1 | `MONDO:0010577` | hearing loss, X-linked 1 | `AGREES` |
| DFNX2 | `MONDO:0010576` | X-linked mixed hearing loss with perilymphatic gusher | `AGREES` |
| DFNX4 | `MONDO:0010238` | hearing loss, X-linked 4 | `AGREES` |
| DFNX5 | `MONDO:0010378` | X-linked hereditary sensory and autonomic neuropathy with hearing loss | `AGREES` |
| DFNX6 | `MONDO:0010484` | hearing loss, X-linked 6 | `AGREES` |

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
