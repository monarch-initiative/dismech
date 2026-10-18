# Guillain-Barre Syndrome

Boomer grounding analysis for [`kb/disorders/Guillain_Barre_Syndrome.yaml`](../../../../kb/disorders/Guillain_Barre_Syndrome.yaml).

- **Entry term:** [`MONDO:0016218`](http://purl.obolibrary.org/obo/MONDO_0016218) Guillain-Barre syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Acute Inflammatory Demyelinating Polyradiculoneuropathy | `MONDO:0020347` | acute inflammatory demyelinating polyradiculoneuropathy | `AGREES` | ✓ NCIT, ORDO |
| Acute Motor Axonal Neuropathy | `MONDO:0020349` | acute motor axonal neuropathy | `AGREES` | ✓ NCIT, ORDO |
| Acute Motor and Sensory Axonal Neuropathy | `MONDO:0020348` | acute motor and sensory axonal neuropathy | `AGREES` | ✓ NCIT, ORDO |
| Miller Fisher Syndrome | `MONDO:0005851` | Miller Fisher syndrome | `SILENT` | ✓ DOID, MESH, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Miller Fisher Syndrome** — DOID (DOID:12889), MESH (MESH:D019846), ORDO (ORDO:98919)

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
