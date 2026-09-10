# Central Nervous System Germ Cell Tumor

Boomer grounding analysis for [`kb/disorders/Central_Nervous_System_Germ_Cell_Tumor.yaml`](../../../../kb/disorders/Central_Nervous_System_Germ_Cell_Tumor.yaml).

- **Entry term:** [`MONDO:0003000`](http://purl.obolibrary.org/obo/MONDO_0003000) central nervous system germ cell tumor
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Central Nervous System Germinoma | `MONDO:0002999` | central nervous system germinoma | `AGREES` | ✓ DOID, NCIT |
| Central Nervous System Nongerminomatous Germ Cell Tumor | `MONDO:0020574` | central nervous system nongerminomatous germ cell tumor | `AGREES` | ✓ NCIT |
| Central Nervous System Embryonal Carcinoma | `MONDO:0018843` | embryonal carcinoma of the central nervous system | `AGREES` | ✓ DOID, NCIT |
| Central Nervous System Teratoma | `MONDO:0002718` | central nervous system teratoma | `AGREES` | ✓ DOID, NCIT |

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
