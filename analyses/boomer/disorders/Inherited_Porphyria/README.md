# Inherited Porphyria

Boomer grounding analysis for [`kb/disorders/Inherited_Porphyria.yaml`](../../../../kb/disorders/Inherited_Porphyria.yaml).

- **Entry term:** [`MONDO:0019142`](http://purl.obolibrary.org/obo/MONDO_0019142) inherited porphyria
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Acute Intermittent Porphyria | `MONDO:0008294` | acute intermittent porphyria | `AGREES` |
| Porphyria due to ALA Dehydratase Deficiency | `MONDO:0013000` | porphyria due to ALA dehydratase deficiency | `AGREES` |
| Hereditary Coproporphyria | `MONDO:0007369` | hereditary coproporphyria | `AGREES` |
| Variegate Porphyria | `MONDO:0008297` | variegate porphyria | `AGREES` |
| Familial Porphyria Cutanea Tarda | `MONDO:0008296` | familial porphyria cutanea tarda | `AGREES` |
| Hepatoerythropoietic Porphyria | `MONDO:0019799` | hepatoerythropoietic porphyria | `AGREES` |
| Erythropoietic Protoporphyria | `MONDO:0001676` | erythropoietic protoporphyria | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
