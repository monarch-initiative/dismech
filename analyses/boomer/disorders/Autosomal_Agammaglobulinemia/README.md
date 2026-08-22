# Autosomal Agammaglobulinemia

Boomer grounding analysis for [`kb/disorders/Autosomal_Agammaglobulinemia.yaml`](../../../../kb/disorders/Autosomal_Agammaglobulinemia.yaml).

- **Entry term:** [`MONDO:0011096`](http://purl.obolibrary.org/obo/MONDO_0011096) autosomal agammaglobulinemia
- **Grounded subtypes:** 12
- **Verdicts:** AGREES 8, SILENT 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| AGM1 | `MONDO:0020729` | autosomal recessive agammaglobulinemia 1 | `AGREES` | — no shared vocabulary |
| AGM2 | `MONDO:0013287` | agammaglobulinemia 2, autosomal recessive | `AGREES` | — no shared vocabulary |
| AGM3 | `MONDO:0013288` | agammaglobulinemia 3, autosomal recessive | `AGREES` | — no shared vocabulary |
| AGM4 | `MONDO:0013289` | agammaglobulinemia 4, autosomal recessive | `AGREES` | — no shared vocabulary |
| AGM5 | `MONDO:0013290` | agammaglobulinemia 5, autosomal dominant | `AGREES` | — no shared vocabulary |
| AGM6 | `MONDO:0012987` | agammaglobulinemia 6, autosomal recessive | `AGREES` | — no shared vocabulary |
| AGM7 | `MONDO:0014083` | agammaglobulinemia 7, autosomal recessive | `AGREES` | — no shared vocabulary |
| AGM8 | `MONDO:0014840` | agammaglobulinemia 8, autosomal dominant | `AGREES` | — no shared vocabulary |
| AGM8B | `MONDO:0859234` | agammaglobulinemia 8b, autosomal recessive | `SILENT` | — no shared vocabulary |
| AGM9 | `MONDO:0030519` | agammaglobulinemia 9, autosomal recessive | `SILENT` | silent (ORDO) |
| AGM10 | `MONDO:0030529` | agammaglobulinemia 10, autosomal dominant | `SILENT` | — no shared vocabulary |
| FNIP1 | `MONDO:0100432` | FNIP1-associated syndrome | `SILENT` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0013287` ≡ `DOID:0081135`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

4 subtype(s) are `SILENT`: MONDO asserts no path between the
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
