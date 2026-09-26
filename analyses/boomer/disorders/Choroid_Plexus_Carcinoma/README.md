# Choroid Plexus Carcinoma

Boomer grounding analysis for [`kb/disorders/Choroid_Plexus_Carcinoma.yaml`](../../../../kb/disorders/Choroid_Plexus_Carcinoma.yaml).

- **Entry term:** [`MONDO:0016718`](http://purl.obolibrary.org/obo/MONDO_0016718) choroid plexus carcinoma
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Childhood | `MONDO:0002685` | childhood choroid plexus carcinoma | `AGREES` | ✓ NCIT |
| Li-Fraumeni-Associated | `MONDO:0018875` | Li-Fraumeni syndrome | `SILENT` | silent (DOID, MESH, NCIT, ORDO, icd11f) |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0018875` ≡ `DOID:3012`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
