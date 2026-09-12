# Hereditary Angioedema

Boomer grounding analysis for [`kb/disorders/Hereditary_Angioedema.yaml`](../../../../kb/disorders/Hereditary_Angioedema.yaml).

- **Entry term:** [`MONDO:0019623`](http://purl.obolibrary.org/obo/MONDO_0019623) hereditary angioedema
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| C1-INH deficiency | `MONDO:0033946` | hereditary angioedema with C1Inh deficiency | `AGREES` | ✓ DOID, ORDO |
| Type 1 | `MONDO:0015053` | hereditary angioedema type 1 | `AGREES` | ✓ ORDO |
| Type 2 | `MONDO:0015054` | hereditary angioedema type 2 | `AGREES` | ✓ ORDO |
| Normal C1-INH | `MONDO:0100567` | hereditary angioedema with normal C1Inh | `AGREES` | ✓ ORDO |
| F12-related normal C1-INH | `MONDO:0012526` | hereditary angioedema type 3 | `AGREES` | ✓ DOID, MESH, ORDO |
| PLG-related normal C1-INH | `MONDO:0035220` | PLG-related hereditary angioedema with normal C1inh | `AGREES` | ✓ ORDO |
| Other normal C1-INH | `MONDO:0035734` | hereditary angioedema with normal C1inh not related to F12 or PLG variant | `AGREES` | ✓ ORDO |

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
