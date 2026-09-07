# Osteochondrosis

Boomer grounding analysis for [`kb/disorders/Osteochondrosis.yaml`](../../../../kb/disorders/Osteochondrosis.yaml).

- **Entry term:** [`MONDO:0018381`](http://purl.obolibrary.org/obo/MONDO_0018381) osteochondrosis
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 5, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Legg-Calve-Perthes Disease | `MONDO:0007885` | Legg-Calve-Perthes disease | `AGREES` | ✓ DOID, ORDO |
| Osgood-Schlatter Disease | `MONDO:0004241` | Osgood-Schlatter disease | `AGREES` | ✓ NCIT, ORDO |
| Kohler Disease | `MONDO:0016086` | osteochondritis of tarsal/metatarsal bone | `AGREES` | ✓ DOID, ORDO |
| Freiberg Infraction | `MONDO:0023188` | Freiberg disease | `AGREES` | ✓ ORDO, icd11f |
| Scheuermann Kyphosis | `MONDO:0008410` | Scheuermann disease | `AGREES` | ✓ DOID, MESH, NCIT |
| Osteochondritis Dissecans | `MONDO:0017178` | osteochondritis dissecans | `SILENT` | ✓ icd11f |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Osteochondritis Dissecans** — icd11f (icd11f:467851106)

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
