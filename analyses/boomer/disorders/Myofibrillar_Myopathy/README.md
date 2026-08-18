# Myofibrillar Myopathy

Boomer grounding analysis for [`kb/disorders/Myofibrillar_Myopathy.yaml`](../../../../kb/disorders/Myofibrillar_Myopathy.yaml).

- **Entry term:** [`MONDO:0018943`](http://purl.obolibrary.org/obo/MONDO_0018943) myofibrillar myopathy
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 9, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MFM1 | `MONDO:0011076` | myofibrillar myopathy 1 | `AGREES` | ✓ DOID, ORDO |
| MFM2 | `MONDO:0012130` | myofibrillar myopathy 2 | `SILENT` | ✓ DOID, ORDO |
| MFM3 | `MONDO:0012215` | myofibrillar myopathy 3 | `AGREES` | ✓ DOID, ORDO |
| MFM4 | `MONDO:0012277` | myofibrillar myopathy 4 | `AGREES` | ✓ DOID, ORDO |
| MFM5 | `MONDO:0012289` | myofibrillar myopathy 5 | `AGREES` | ✓ DOID, ORDO |
| MFM6 | `MONDO:0013061` | myofibrillar myopathy 6 | `AGREES` | ✓ DOID, ORDO |
| MFM7 | `MONDO:0014922` | myofibrillar myopathy 7 | `AGREES` | ✓ DOID |
| MFM8 | `MONDO:0014993` | myofibrillar myopathy 8 | `AGREES` | ✓ DOID |
| MFM10 | `MONDO:0033620` | myofibrillar myopathy 10 | `AGREES` | ✓ DOID |
| MFM11 | `MONDO:0030927` | myofibrillar myopathy 11 | `AGREES` | ✓ DOID |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **MFM2** — DOID (DOID:0080093), ORDO (ORDO:399058)

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0012215` ≡ `MESH:C000598645`
- `MONDO:0012215` ≡ `MESH:C535906`
- `MONDO:0012215` ≡ `ORDO:98911`

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
