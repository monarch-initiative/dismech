# Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy

Boomer grounding analysis for [`kb/disorders/Adult-Onset_Autosomal_Dominant_Demyelinating_Leukodystrophy.yaml`](../../../../kb/disorders/Adult-Onset_Autosomal_Dominant_Demyelinating_Leukodystrophy.yaml).

- **Entry term:** [`MONDO:0008215`](http://purl.obolibrary.org/obo/MONDO_0008215) adult-onset autosomal dominant demyelinating leukodystrophy
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Upstream Deletion-Related ADLD | `MONDO:0700286` | leukodystrophy, demyelinating, adult-onset, autosomal dominant, atypical | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0008215` ≡ `DOID:0051015`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
