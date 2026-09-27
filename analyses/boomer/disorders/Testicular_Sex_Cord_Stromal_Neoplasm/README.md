# Testicular Sex Cord-Stromal Neoplasm

Boomer grounding analysis for [`kb/disorders/Testicular_Sex_Cord_Stromal_Neoplasm.yaml`](../../../../kb/disorders/Testicular_Sex_Cord_Stromal_Neoplasm.yaml).

- **Entry term:** [`MONDO:0003125`](http://purl.obolibrary.org/obo/MONDO_0003125) testicular sex cord-stromal neoplasm
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Leydig Cell Tumor | `MONDO:0003124` | testicular Leydig cell tumor | `AGREES` | ✓ DOID, NCIT |
| Sertoli Cell Tumor | `MONDO:0020808` | testicular sertoli cell tumor | `AGREES` | ✓ NCIT |
| Granulosa Cell Tumor | `MONDO:0003395` | testicular granulosa cell tumor | `AGREES` | ✓ NCIT |

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
