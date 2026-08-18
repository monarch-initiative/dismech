# Progressive Familial Intrahepatic Cholestasis

Boomer grounding analysis for [`kb/disorders/Progressive_Familial_Intrahepatic_Cholestasis.yaml`](../../../../kb/disorders/Progressive_Familial_Intrahepatic_Cholestasis.yaml).

- **Entry term:** [`MONDO:0015762`](http://purl.obolibrary.org/obo/MONDO_0015762) progressive familial intrahepatic cholestasis
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PFIC1 | `MONDO:0008892` | progressive familial intrahepatic cholestasis type 1 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PFIC2 | `MONDO:0011156` | progressive familial intrahepatic cholestasis type 2 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PFIC3 | `MONDO:0011214` | progressive familial intrahepatic cholestasis type 3 | `AGREES` | ✓ DOID, ORDO, icd11f |
| PFIC4 | `MONDO:0014381` | cholestasis, progressive familial intrahepatic, 4 | `AGREES` | ✓ DOID, ORDO |
| PFIC5 | `MONDO:0014884` | cholestasis, progressive familial intrahepatic, 5 | `AGREES` | ✓ DOID, ORDO |
| MYO5B-related cholestasis | `MONDO:0018804` | MYO5B-related progressive familial intrahepatic cholestasis | `AGREES` | ✓ ORDO |
| USP53-related cholestasis | `MONDO:0030503` | cholestasis, progressive familial intrahepatic, 7, with or without hearing loss | `AGREES` | — no shared vocabulary |
| KIF12-related cholestasis | `MONDO:0030505` | cholestasis, progressive familial intrahepatic, 8 | `AGREES` | — no shared vocabulary |
| ZFYVE19-related cholestasis | `MONDO:0030800` | cholestasis, progressive familial intrahepatic, 9 | `AGREES` | — no shared vocabulary |

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
