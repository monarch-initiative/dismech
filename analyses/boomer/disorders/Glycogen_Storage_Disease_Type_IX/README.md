# Glycogen Storage Disease Type IX

Boomer grounding analysis for [`kb/disorders/Glycogen_Storage_Disease_Type_IX.yaml`](../../../../kb/disorders/Glycogen_Storage_Disease_Type_IX.yaml).

- **Entry term:** [`MONDO:0700291`](http://purl.obolibrary.org/obo/MONDO_0700291) glycogen storage disease IX
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| IXa1 | `MONDO:0010598` | glycogen storage disease IXa1 | `AGREES` | ✓ DOID |
| IXa2 | `MONDO:0100439` | glycogen storage disease IXa2 | `AGREES` | — no shared vocabulary |
| IXb | `MONDO:0009868` | glycogen storage disease IXb | `AGREES` | ✓ DOID, ORDO |
| IXc | `MONDO:0013091` | glycogen storage disease IXc | `AGREES` | ✓ DOID |
| IXd | `MONDO:0010362` | glycogen storage disease IXd | `SILENT` | ✓ DOID, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **IXd** — DOID (DOID:0111040), ORDO (ORDO:715)

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0010598` ≡ `DOID:0111042`
- `MONDO:0010598` ≡ `MESH:C564421`

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
