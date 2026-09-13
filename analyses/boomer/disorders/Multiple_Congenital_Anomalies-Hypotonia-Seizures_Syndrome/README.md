# Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome

Boomer grounding analysis for [`kb/disorders/Multiple_Congenital_Anomalies-Hypotonia-Seizures_Syndrome.yaml`](../../../../kb/disorders/Multiple_Congenital_Anomalies-Hypotonia-Seizures_Syndrome.yaml).

- **Entry term:** [`MONDO:0100247`](http://purl.obolibrary.org/obo/MONDO_0100247) multiple congenital anomalies-hypotonia-seizures syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MCAHS1 | `MONDO:0013563` | multiple congenital anomalies-hypotonia-seizures syndrome 1 | `AGREES` | ✓ DOID |
| MCAHS2 | `MONDO:0010466` | multiple congenital anomalies-hypotonia-seizures syndrome 2 | `AGREES` | ✓ DOID |
| MCAHS3 | `MONDO:0014165` | multiple congenital anomalies-hypotonia-seizures syndrome 3 | `AGREES` | ✓ DOID |

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
