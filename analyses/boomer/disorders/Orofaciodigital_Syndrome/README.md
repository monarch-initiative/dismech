# Orofaciodigital Syndrome

Boomer grounding analysis for [`kb/disorders/Orofaciodigital_Syndrome.yaml`](../../../../kb/disorders/Orofaciodigital_Syndrome.yaml).

- **Entry term:** [`MONDO:0015375`](http://purl.obolibrary.org/obo/MONDO_0015375) orofaciodigital syndrome
- **Grounded subtypes:** 20
- **Verdicts:** AGREES 19, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| OFD I | `MONDO:0010702` | orofaciodigital syndrome I | `SILENT` | ✓ DOID, ORDO |
| OFD II | `MONDO:0009642` | orofaciodigital syndrome type II | `AGREES` | ✓ DOID, ORDO |
| OFD III | `MONDO:0009793` | orofaciodigital syndrome III | `AGREES` | ✓ DOID |
| OFD IV | `MONDO:0009794` | orofaciodigital syndrome IV | `AGREES` | ✓ DOID, ORDO |
| OFD V | `MONDO:0008267` | orofaciodigital syndrome V | `AGREES` | ✓ DOID, ORDO |
| OFD 6 | `MONDO:0010176` | orofaciodigital syndrome type 6 | `AGREES` | ✓ ORDO |
| OFD VII | `MONDO:0012049` | orofaciodigital syndrome VII | `AGREES` | ✓ DOID |
| OFD VIII | `MONDO:0010336` | orofaciodigital syndrome VIII | `AGREES` | ✓ DOID, ORDO |
| OFD IX | `MONDO:0009795` | orofaciodigital syndrome IX | `AGREES` | ✓ DOID, ORDO |
| OFD X | `MONDO:0008137` | orofaciodigital syndrome X | `AGREES` | ✓ DOID |
| OFD XI | `MONDO:0013035` | orofaciodigital syndrome XI | `AGREES` | ✓ DOID, ORDO |
| OFD 12 | `MONDO:0015421` | orofaciodigital syndrome type 12 | `AGREES` | silent (MESH) |
| OFD 14 | `MONDO:0014413` | orofaciodigital syndrome type 14 | `AGREES` | ✓ DOID, ORDO |
| OFD XV | `MONDO:0014932` | orofaciodigital syndrome XV | `AGREES` | — no shared vocabulary |
| OFD 16 | `MONDO:0033045` | orofaciodigital syndrome 16 | `AGREES` | ✓ DOID |
| OFD 17 | `MONDO:0033375` | orofaciodigital syndrome 17 | `AGREES` | ✓ DOID |
| OFD 18 | `MONDO:0054770` | orofaciodigital syndrome 18 | `AGREES` | ✓ DOID, ORDO |
| OFD 19 | `MONDO:0859310` | orofaciodigital syndrome 19 | `AGREES` | ✓ DOID |
| OFD 20 | `MONDO:0958230` | orofaciodigital syndrome 20 | `AGREES` | ✓ DOID |
| OFD 21 | `MONDO:0975827` | orofaciodigital syndrome 21 | `AGREES` | — no shared vocabulary |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **OFD I** — DOID (DOID:0060316), ORDO (ORDO:2750)

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
