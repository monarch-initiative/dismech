# Episodic Ataxia

Boomer grounding analysis for [`kb/disorders/Episodic_Ataxia.yaml`](../../../../kb/disorders/Episodic_Ataxia.yaml).

- **Entry term:** [`MONDO:0016227`](http://purl.obolibrary.org/obo/MONDO_0016227) hereditary episodic ataxia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| EA1 | `MONDO:0008047` | episodic ataxia type 1 | `AGREES` | ✓ DOID, ORDO |
| EA2 | `MONDO:0007163` | episodic ataxia type 2 | `AGREES` | ✓ DOID, ORDO |

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
