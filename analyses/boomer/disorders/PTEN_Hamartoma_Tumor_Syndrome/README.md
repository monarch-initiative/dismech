# PTEN Hamartoma Tumor Syndrome

Boomer grounding analysis for [`kb/disorders/PTEN_Hamartoma_Tumor_Syndrome.yaml`](../../../../kb/disorders/PTEN_Hamartoma_Tumor_Syndrome.yaml).

- **Entry term:** [`MONDO:0017623`](http://purl.obolibrary.org/obo/MONDO_0017623) PTEN hamartoma tumor syndrome
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 3, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Cowden syndrome | `MONDO:0016063` | Cowden disease | `SILENT` | ✓ NCIT, ORDO |
| Bannayan-Riley-Ruvalcaba syndrome | `MONDO:0007924` | Bannayan-Riley-Ruvalcaba syndrome | `AGREES` | ✓ NCIT, ORDO |
| Proteus-like syndrome | `MONDO:0017571` | Proteus-like syndrome | `AGREES` | ✓ NCIT, ORDO |
| Lhermitte-Duclos disease | `MONDO:0019002` | Lhermitte-Duclos disease | `SILENT` | ✓ ORDO |
| SOLAMEN syndrome | `MONDO:0015293` | segmental outgrowth-lipomatosis-arteriovenous malformation-epidermal nevus syndrome | `AGREES` | ✓ ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Cowden syndrome** — NCIT (NCIT:C3076), ORDO (ORDO:201)
- **Lhermitte-Duclos disease** — ORDO (ORDO:65285)

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
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
