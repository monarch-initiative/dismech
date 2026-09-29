# Otopalatodigital Spectrum Disorders

Boomer grounding analysis for [`kb/disorders/Otopalatodigital_Spectrum_Disorders.yaml`](../../../../kb/disorders/Otopalatodigital_Spectrum_Disorders.yaml).

- **Entry term:** [`MONDO:0018233`](http://purl.obolibrary.org/obo/MONDO_0018233) otopalatodigital syndrome spectrum disorder
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| OPD1 | `MONDO:0010704` | otopalatodigital syndrome type 1 | `AGREES` | ✓ DOID, ORDO |
| OPD2 | `MONDO:0010571` | otopalatodigital syndrome type 2 | `AGREES` | ✓ DOID, ORDO |
| FMD | `MONDO:0024550` | frontometaphyseal dysplasia 1 | `AGREES` | ✓ DOID |
| MNS | `MONDO:0010650` | Melnick-Needles syndrome | `AGREES` | ✓ DOID, ORDO |

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
