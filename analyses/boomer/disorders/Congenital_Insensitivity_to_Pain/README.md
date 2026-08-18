# Congenital Insensitivity to Pain

Boomer grounding analysis for [`kb/disorders/Congenital_Insensitivity_to_Pain.yaml`](../../../../kb/disorders/Congenital_Insensitivity_to_Pain.yaml).

- **Entry term:** [`MONDO:0015364`](http://purl.obolibrary.org/obo/MONDO_0015364) hereditary sensory and autonomic neuropathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HSAN IV | `MONDO:0009746` | hereditary sensory and autonomic neuropathy type 4 | `AGREES` | ✓ DOID, ORDO, icd11f |
| HSAN V | `MONDO:0012092` | hereditary sensory and autonomic neuropathy type 5 | `AGREES` | ✓ DOID, ORDO, icd11f |
| SCN9A AR-CIP | `MONDO:0009459` | channelopathy-associated congenital insensitivity to pain, autosomal recessive | `SILENT` | ✓ ORDO |
| HSAN VII | `MONDO:0014244` | hereditary sensory and autonomic neuropathy type 7 | `AGREES` | ✓ DOID, ORDO |
| HSAN VIII | `MONDO:0014662` | congenital insensitivity to pain-hypohidrosis syndrome | `AGREES` | ✓ DOID, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **SCN9A AR-CIP** — ORDO (ORDO:88642)

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
