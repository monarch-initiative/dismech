# Mycosis Fungoides

Boomer grounding analysis for [`kb/disorders/Mycosis_Fungoides.yaml`](../../../../kb/disorders/Mycosis_Fungoides.yaml).

- **Entry term:** [`MONDO:0009691`](http://purl.obolibrary.org/obo/MONDO_0009691) mycosis fungoides
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Folliculotropic | `MONDO:0015808` | folliculotropic mycosis fungoides | `SILENT` | ✓ NCIT, icd11f |
| Localized Pagetoid Reticulosis | `MONDO:0015809` | localized pagetoid reticulosis | `SILENT` | ✓ MESH, NCIT |
| Granulomatous Slack Skin | `MONDO:0018031` | granulomatous slack skin disease | `SILENT` | ✓ NCIT |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Folliculotropic** — NCIT (NCIT:C35685), icd11f (icd11f:1335995469)
- **Localized Pagetoid Reticulosis** — MESH (MESH:D056267), NCIT (NCIT:C35794)
- **Granulomatous Slack Skin** — NCIT (NCIT:C35464)

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
