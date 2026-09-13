# Non-Syndromic X-Linked Intellectual Disability

Boomer grounding analysis for [`kb/disorders/Non-Syndromic_X-Linked_Intellectual_Disability.yaml`](../../../../kb/disorders/Non-Syndromic_X-Linked_Intellectual_Disability.yaml).

- **Entry term:** [`MONDO:0019181`](http://purl.obolibrary.org/obo/MONDO_0019181) non-syndromic X-linked intellectual disability
- **Grounded subtypes:** 8
- **Verdicts:** AGREES 8

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MRX21 | `MONDO:0010256` | intellectual disability, X-linked 21 | `AGREES` | ✓ DOID |
| MRX30 | `MONDO:0010361` | intellectual disability, X-linked 30 | `AGREES` | ✓ DOID |
| MRX41 | `MONDO:0010451` | intellectual disability, X-linked 41 | `AGREES` | ✓ DOID |
| MRX58 | `MONDO:0010266` | intellectual disability, X-linked 58 | `AGREES` | ✓ DOID |
| MRX9 | `MONDO:0010660` | intellectual disability, X-linked 9 | `AGREES` | ✓ DOID |
| MRX63 | `MONDO:0010313` | intellectual disability, X-linked 63 | `AGREES` | ✓ DOID |
| FRAXE | `MONDO:0010659` | FRAXE intellectual disability | `AGREES` | silent (DOID, ORDO) |
| ARX-related | `MONDO:0010317` | intellectual disability, X-linked, with or without seizures, ARX-related | `AGREES` | ✓ DOID |

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
