# Plasma Cell Neoplasm

Boomer grounding analysis for [`kb/disorders/Plasma_Cell_Neoplasm.yaml`](../../../../kb/disorders/Plasma_Cell_Neoplasm.yaml).

- **Entry term:** [`MONDO:0004959`](http://purl.obolibrary.org/obo/MONDO_0004959) plasma cell neoplasm
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 5, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Monoclonal Gammopathy of Uncertain Significance | `MONDO:0004225` | monoclonal gammopathy of uncertain significance | `SILENT` | silent (DOID, MESH, NCIT) |
| Smoldering Plasma Cell Myeloma | `MONDO:0005235` | smoldering plasma cell myeloma | `AGREES` | ✓ NCIT |
| Plasma Cell Myeloma | `MONDO:0009693` | plasma cell myeloma | `AGREES` | ✓ MESH, NCIT, ORDO |
| Plasma Cell Leukemia | `MONDO:0018689` | plasma cell leukemia | `AGREES` | ✓ DOID, MESH, NCIT, ORDO |
| Plasmacytoma | `MONDO:0005615` | plasmacytoma | `AGREES` | ✓ DOID, MESH, NCIT, ORDO |
| Non-amyloid Monoclonal Immunoglobulin Deposition Disease | `MONDO:0019463` | non-amyloid monoclonal immunoglobulin deposition disease | `AGREES` | ✓ ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0009693` ≡ `icd11f:526287100`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

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
