# Disorder of Catecholamine Synthesis

Boomer grounding analysis for [`kb/disorders/Disorder_of_Catecholamine_Synthesis.yaml`](../../../../kb/disorders/Disorder_of_Catecholamine_Synthesis.yaml).

- **Entry term:** [`MONDO:0017759`](http://purl.obolibrary.org/obo/MONDO_0017759) disorder of catecholamine synthesis
- **Grounded subtypes:** 5
- **Verdicts:** SILENT 4, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Aromatic L-amino acid decarboxylase deficiency | `MONDO:0012084` | aromatic L-amino acid decarboxylase deficiency | `AGREES` | ✓ ORDO, icd11f |
| Tyrosine hydroxylase deficiency | `MONDO:0011551` | TH-deficient dopa-responsive dystonia | `SILENT` | silent (ORDO) |
| Autosomal recessive GTP cyclohydrolase I deficiency | `MONDO:0100184` | GTP cyclohydrolase I deficiency | `SILENT` | — no shared vocabulary |
| Sepiapterin reductase deficiency | `MONDO:0012994` | dopa-responsive dystonia due to sepiapterin reductase deficiency | `SILENT` | silent (ORDO) |
| DNAJC12-related monoamine synthesis disorder | `MONDO:0044304` | hyperphenylalaninemia due to DNAJC12 deficiency | `SILENT` | silent (ORDO) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

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
