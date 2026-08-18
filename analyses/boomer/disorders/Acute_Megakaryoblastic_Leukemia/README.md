# Acute Megakaryoblastic Leukemia

Boomer grounding analysis for [`kb/disorders/Acute_Megakaryoblastic_Leukemia.yaml`](../../../../kb/disorders/Acute_Megakaryoblastic_Leukemia.yaml).

- **Entry term:** [`MONDO:0018872`](http://purl.obolibrary.org/obo/MONDO_0018872) acute megakaryoblastic leukemia
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Down Syndrome-Associated AMKL | `MONDO:0020526` | acute megakaryoblastic leukemia in down syndrome | `AGREES` | ✓ ORDO |
| Non-Down Syndrome AMKL | `MONDO:0018004` | acute megakaryoblastic leukemia without down syndrome | `AGREES` | ✓ ORDO |
| RBM15::MRTFA-Rearranged AMKL | `MONDO:0018436` | megakaryoblastic acute myeloid leukemia with t(1;22)(p13;q13) | `SILENT` | silent (ORDO) |
| Adult AMKL | `MONDO:0971091` | acute megakaryoblastic leukemia in adult | `AGREES` | ✓ ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

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
