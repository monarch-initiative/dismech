# Diabetes mellitus

Boomer grounding analysis for [`kb/disorders/Diabetes_Mellitus.yaml`](../../../../kb/disorders/Diabetes_Mellitus.yaml).

- **Entry term:** [`MONDO:0005015`](http://purl.obolibrary.org/obo/MONDO_0005015) diabetes mellitus
- **Grounded subtypes:** 27
- **Verdicts:** AGREES 27

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| type 1 diabetes mellitus | `MONDO:0005147` | type 1 diabetes mellitus | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |
| latent autoimmune diabetes in adults | `MONDO:0850306` | latent autoimmune diabetes in adults | `AGREES` | ✓ DOID, icd11f |
| type 2 diabetes mellitus | `MONDO:0005148` | type 2 diabetes mellitus | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |
| lipoatrophic diabetes | `MONDO:0005827` | lipoatrophic diabetes | `AGREES` | ✓ DOID, MESH, NCIT |
| gestational diabetes | `MONDO:0005406` | gestational diabetes | `AGREES` | ✓ DOID, MESH, NCIT, icd11f |
| monogenic diabetes | `MONDO:0015967` | monogenic diabetes | `AGREES` | ✓ NCIT |
| neonatal diabetes mellitus | `MONDO:0016391` | neonatal diabetes mellitus | `AGREES` | ✓ DOID, NCIT, icd11f |
| transient neonatal diabetes mellitus | `MONDO:0020525` | transient neonatal diabetes mellitus | `AGREES` | ✓ DOID, NCIT, icd11f |
| permanent neonatal diabetes mellitus | `MONDO:0100164` | permanent neonatal diabetes mellitus | `AGREES` | ✓ DOID, NCIT, icd11f |
| maturity-onset diabetes of the young | `MONDO:0018911` | maturity-onset diabetes of the young | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 1 | `MONDO:0007452` | maturity-onset diabetes of the young type 1 | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 2 | `MONDO:0007453` | maturity-onset diabetes of the young type 2 | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 3 | `MONDO:0010894` | maturity-onset diabetes of the young type 3 | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 4 | `MONDO:0011667` | maturity-onset diabetes of the young type 4 | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 6 | `MONDO:0011668` | maturity-onset diabetes of the young type 6 | `AGREES` | ✓ DOID, NCIT |
| maturity-onset diabetes of the young type 7 | `MONDO:0012513` | maturity-onset diabetes of the young type 7 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young type 8 | `MONDO:0012348` | maturity-onset diabetes of the young type 8 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young type 9 | `MONDO:0012818` | maturity-onset diabetes of the young type 9 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young type 10 | `MONDO:0013240` | maturity-onset diabetes of the young type 10 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young type 11 | `MONDO:0013242` | maturity-onset diabetes of the young type 11 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young, type 12 | `MONDO:0978299` | maturity-onset diabetes of the young, type 12 | `AGREES` | — no shared vocabulary |
| maturity-onset diabetes of the young type 13 | `MONDO:0014589` | maturity-onset diabetes of the young type 13 | `AGREES` | ✓ DOID |
| maturity-onset diabetes of the young type 14 | `MONDO:0014674` | maturity-onset diabetes of the young type 14 | `AGREES` | ✓ DOID |
| renal cysts and diabetes syndrome | `MONDO:0007669` | renal cysts and diabetes syndrome | `AGREES` | ✓ NCIT |
| maternally-inherited diabetes and deafness | `MONDO:0010785` | maternally-inherited diabetes and deafness | `AGREES` | ✓ NCIT, icd11f |
| type 5 diabetes mellitus | `MONDO:1010179` | type 5 diabetes mellitus | `AGREES` | — no shared vocabulary |
| diabetic ketoacidosis | `MONDO:0012819` | diabetic ketoacidosis | `AGREES` | ✓ MESH |

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
