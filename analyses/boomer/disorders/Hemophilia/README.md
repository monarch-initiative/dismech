# Hemophilia

Boomer grounding analysis for [`kb/disorders/Hemophilia.yaml`](../../../../kb/disorders/Hemophilia.yaml).

- **Entry term:** [`MONDO:0018660`](http://purl.obolibrary.org/obo/MONDO_0018660) hemophilia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Hemophilia A | `MONDO:0010602` | hemophilia A | `AGREES` | ✓ DOID, NCIT, ORDO |
| Hemophilia B | `MONDO:0010604` | hemophilia B | `AGREES` | ✓ DOID, NCIT, ORDO |
| Hemophilia B Leyden | `MONDO:0850054` | hemophilia B leyden | `SILENT` | ✓ ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Hemophilia B Leyden** — ORDO (ORDO:617930)

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0010602` ≡ `OMIM:134500`

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
