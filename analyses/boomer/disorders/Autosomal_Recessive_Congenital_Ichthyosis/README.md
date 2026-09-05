# Autosomal Recessive Congenital Ichthyosis

Boomer grounding analysis for [`kb/disorders/Autosomal_Recessive_Congenital_Ichthyosis.yaml`](../../../../kb/disorders/Autosomal_Recessive_Congenital_Ichthyosis.yaml).

- **Entry term:** [`MONDO:0017265`](http://purl.obolibrary.org/obo/MONDO_0017265) autosomal recessive congenital ichthyosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Lamellar Ichthyosis | `MONDO:0017778` | lamellar ichthyosis | `SILENT` | ✓ ORDO, icd11f |
| Congenital Ichthyosiform Erythroderma | `MONDO:0019306` | congenital non-bullous ichthyosiform erythroderma | `AGREES` | ✓ ORDO, icd11f |
| Harlequin Ichthyosis | `MONDO:0009443` | autosomal recessive congenital ichthyosis 4B | `AGREES` | ✓ DOID, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Lamellar Ichthyosis** — ORDO (ORDO:313), icd11f (icd11f:600146417)

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

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
