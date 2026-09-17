# Craniometaphyseal Dysplasia

Boomer grounding analysis for [`kb/disorders/Craniometaphyseal_Dysplasia.yaml`](../../../../kb/disorders/Craniometaphyseal_Dysplasia.yaml).

- **Entry term:** [`MONDO:0015465`](http://purl.obolibrary.org/obo/MONDO_0015465) craniometaphyseal dysplasia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| AD-CMD | `MONDO:0007397` | craniometaphyseal dysplasia, autosomal dominant | `AGREES` | ✓ DOID |
| AR-CMD | `MONDO:0009035` | craniometaphyseal dysplasia, autosomal recessive | `AGREES` | ✓ DOID |

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
