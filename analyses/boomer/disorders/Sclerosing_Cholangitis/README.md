# Sclerosing Cholangitis

Boomer grounding analysis for [`kb/disorders/Sclerosing_Cholangitis.yaml`](../../../../kb/disorders/Sclerosing_Cholangitis.yaml).

- **Entry term:** [`MONDO:0018646`](http://purl.obolibrary.org/obo/MONDO_0018646) sclerosing cholangitis
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Primary sclerosing cholangitis | `MONDO:0013433` | primary sclerosing cholangitis | `AGREES` | ✓ DOID, ORDO |
| Secondary sclerosing cholangitis | `MONDO:0018647` | secondary sclerosing cholangitis | `AGREES` | ✓ ORDO |
| IgG4-related sclerosing cholangitis | `MONDO:0018645` | IgG4-related sclerosing cholangitis | `AGREES` | ✓ ORDO |
| Neonatal ichthyosis-sclerosing cholangitis syndrome | `MONDO:0011874` | neonatal ichthyosis-sclerosing cholangitis syndrome | `AGREES` | ✓ ORDO |
| Isolated neonatal sclerosing cholangitis | `MONDO:0018816` | isolated neonatal sclerosing cholangitis | `AGREES` | ✓ ORDO |

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
