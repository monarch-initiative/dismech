# Autoimmune Encephalitis

Boomer grounding analysis for [`kb/disorders/Autoimmune_Encephalitis.yaml`](../../../../kb/disorders/Autoimmune_Encephalitis.yaml).

- **Entry term:** [`MONDO:0020640`](http://purl.obolibrary.org/obo/MONDO_0020640) autoimmune encephalitis
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Anti-NMDA Receptor Encephalitis | `MONDO:0021081` | anti-NMDA receptor encephalitis | `SILENT` | ✓ NCIT, ORDO |
| LGI1-Antibody Encephalitis | `MONDO:0015592` | limbic encephalitis with LGI1 antibodies | `SILENT` | — no shared vocabulary |
| CASPR2-Antibody Encephalitis | `MONDO:0017179` | limbic encephalitis with caspr2 antibodies | `SILENT` | — no shared vocabulary |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Anti-NMDA Receptor Encephalitis** — NCIT (NCIT:C94853), ORDO (ORDO:217253)

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
