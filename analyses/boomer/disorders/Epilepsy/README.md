# Epilepsy

Boomer grounding analysis for [`kb/disorders/Epilepsy.yaml`](../../../../kb/disorders/Epilepsy.yaml).

- **Entry term:** [`MONDO:0005027`](http://purl.obolibrary.org/obo/MONDO_0005027) epilepsy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Juvenile Myoclonic Epilepsy | `MONDO:0009696` | juvenile myoclonic epilepsy | `AGREES` |
| Juvenile Absence Epilepsy | `MONDO:0800453` | juvenile absence epilepsy | `AGREES` |
| Epilepsy with Myoclonic-Atonic Seizures | `MONDO:0014633` | epilepsy with myoclonic atonic seizures | `AGREES` |
| Self-Limited Neonatal Epilepsy | `MONDO:0016027` | benign neonatal seizures | `AGREES` |
| SYNGAP1-related Disorder | `MONDO:0012960` | intellectual disability, autosomal dominant 5 | `AGREES` |

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
