# Dystrophic Epidermolysis Bullosa

Boomer grounding analysis for [`kb/disorders/Dystrophic_Epidermolysis_Bullosa.yaml`](../../../../kb/disorders/Dystrophic_Epidermolysis_Bullosa.yaml).

- **Entry term:** [`MONDO:0006543`](http://purl.obolibrary.org/obo/MONDO_0006543) epidermolysis bullosa dystrophica
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| DDEB | `MONDO:0007549` | generalized dominant dystrophic epidermolysis bullosa | `AGREES` |
| RDEB-sev gen | `MONDO:0009179` | recessive dystrophic epidermolysis bullosa | `AGREES` |
| RDEB-intermediate | `MONDO:0019522` | recessive dystrophic epidermolysis bullosa-generalized other | `AGREES` |
| RDEB-Inversa | `MONDO:0019310` | recessive dystrophic epidermolysis bullosa inversa | `AGREES` |

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
