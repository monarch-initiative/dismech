# Mediator Complex Neurodevelopmental Disorder

Boomer grounding analysis for [`kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml`](../../../../kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml).

- **Entry term:** [`MONDO:0002320`](http://purl.obolibrary.org/obo/MONDO_0002320) congenital nervous system disorder
- **Grounded subtypes:** 4
- **Verdicts:** SILENT 3, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MED13 | `MONDO:0032485` | intellectual developmental disorder 61 | `SILENT` | silent (DOID) |
| MED13L | `MONDO:0014773` | cardiac anomalies - developmental delay - facial dysmorphism syndrome | `AGREES` | — no shared vocabulary |
| MED12 | `MONDO:0100000` | MED12-related intellectual disability syndrome | `SILENT` | — no shared vocabulary |
| MED23 | `MONDO:0013651` | intellectual disability, autosomal recessive 18 | `SILENT` | silent (DOID) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
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
