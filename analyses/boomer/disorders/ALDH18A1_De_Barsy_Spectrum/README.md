# ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum

Boomer grounding analysis for [`kb/disorders/ALDH18A1_De_Barsy_Spectrum.yaml`](../../../../kb/disorders/ALDH18A1_De_Barsy_Spectrum.yaml).

- **Entry term:** [`MONDO:0100126`](http://purl.obolibrary.org/obo/MONDO_0100126) P5CS deficiency
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SPG9A | `MONDO:0011006` | hereditary spastic paraplegia 9A | `AGREES` |
| SPG9B | `MONDO:0014702` | autosomal recessive complex spastic paraplegia type 9B | `AGREES` |
| ARCL3A | `MONDO:0009053` | ALDH18A1-related de Barsy syndrome | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
