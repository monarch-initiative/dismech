# Mediator Complex Neurodevelopmental Disorder

Boomer grounding analysis for [`kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml`](../../../../kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml).

- **Entry term:** [`MONDO:0002320`](http://purl.obolibrary.org/obo/MONDO_0002320) congenital nervous system disorder
- **Grounded subtypes:** 12
- **Verdicts:** SILENT 11, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MED13 | `MONDO:0032485` | intellectual developmental disorder 61 | `SILENT` | silent (DOID) |
| MED13L | `MONDO:0014773` | cardiac anomalies - developmental delay - facial dysmorphism syndrome | `AGREES` | — no shared vocabulary |
| MED12 | `MONDO:0100000` | MED12-related intellectual disability syndrome | `SILENT` | — no shared vocabulary |
| MED23 | `MONDO:0013651` | intellectual disability, autosomal recessive 18 | `SILENT` | silent (DOID) |
| CDK8 | `MONDO:0032897` | intellectual developmental disorder with hypotonia and behavioral abnormalities | `SILENT` | — no shared vocabulary |
| CDK19 | `MONDO:0030059` | developmental and epileptic encephalopathy, 87 | `SILENT` | silent (DOID) |
| MED12L | `MONDO:0030030` | Nizon-Isidor syndrome | `SILENT` | — no shared vocabulary |
| MED17 | `MONDO:0013351` | infantile cerebral and cerebellar atrophy with postnatal progressive microcephaly | `SILENT` | silent (DOID) |
| MED11 | `MONDO:0957225` | neurodegeneration with developmental delay, early respiratory failure, myoclonic seizures, and brain abnormalities | `SILENT` | — no shared vocabulary |
| MED27 | `MONDO:0859137` | neurodevelopmental disorder with spasticity, cataracts, and cerebellar hypoplasia | `SILENT` | — no shared vocabulary |
| MED25 | `MONDO:0014643` | congenital cataract-microcephaly-nevus flammeus simplex-severe intellectual disability syndrome | `SILENT` | — no shared vocabulary |
| MED16 | `MONDO:0979227` | Guillouet-Gordon syndrome | `SILENT` | — no shared vocabulary |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

11 subtype(s) are `SILENT`: MONDO asserts no path between the
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
