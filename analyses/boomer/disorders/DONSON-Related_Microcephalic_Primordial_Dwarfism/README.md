# DONSON-Related Microcephalic Primordial Dwarfism

Boomer grounding analysis for [`kb/disorders/DONSON-Related_Microcephalic_Primordial_Dwarfism.yaml`](../../../../kb/disorders/DONSON-Related_Microcephalic_Primordial_Dwarfism.yaml).

- **Entry term:** [`MONDO:0035534`](http://purl.obolibrary.org/obo/MONDO_0035534) DONSON-related microcephaly-short stature-limb abnormalities spectrum
- **Grounded subtypes:** 2
- **Verdicts:** SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MMS | `MONDO:0009619` | microcephaly-micromelia syndrome | `SILENT` | ✓ ORDO |
| MISSLA | `MONDO:0060533` | microcephaly, short stature, and limb abnormalities | `SILENT` | ✓ ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **MMS** — ORDO (ORDO:572768)
- **MISSLA** — ORDO (ORDO:572773)

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
