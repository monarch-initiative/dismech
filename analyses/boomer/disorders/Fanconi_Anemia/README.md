# Fanconi_Anemia

Boomer grounding analysis for [`kb/disorders/Fanconi_Anemia.yaml`](../../../../kb/disorders/Fanconi_Anemia.yaml).

- **Entry term:** [`MONDO:0019391`](http://purl.obolibrary.org/obo/MONDO_0019391) Fanconi anemia
- **Grounded subtypes:** 21
- **Verdicts:** AGREES 21

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| FA-A | `MONDO:0009215` | Fanconi anemia complementation group A | `AGREES` |
| FA-B | `MONDO:0010351` | Fanconi anemia complementation group B | `AGREES` |
| FA-C | `MONDO:0009213` | Fanconi anemia complementation group C | `AGREES` |
| FA-D1 | `MONDO:0011584` | Fanconi anemia complementation group D1 | `AGREES` |
| FA-D2 | `MONDO:0009214` | Fanconi anemia complementation group D2 | `AGREES` |
| FA-E | `MONDO:0010953` | Fanconi anemia complementation group E | `AGREES` |
| FA-F | `MONDO:0011325` | Fanconi anemia complementation group F | `AGREES` |
| FA-G | `MONDO:0013565` | Fanconi anemia complementation group G | `AGREES` |
| FA-I | `MONDO:0012186` | Fanconi anemia complementation group I | `AGREES` |
| FA-J | `MONDO:0012187` | Fanconi anemia complementation group J | `AGREES` |
| FA-L | `MONDO:0013566` | Fanconi anemia complementation group L | `AGREES` |
| FA-N | `MONDO:0012565` | Fanconi anemia complementation group N | `AGREES` |
| FA-O | `MONDO:0013248` | Fanconi anemia complementation group O | `AGREES` |
| FA-P | `MONDO:0013499` | Fanconi anemia complementation group P | `AGREES` |
| FA-Q | `MONDO:0014108` | Fanconi anemia complementation group Q | `AGREES` |
| FA-R | `MONDO:0014986` | Fanconi anemia complementation group R | `AGREES` |
| FA-S | `MONDO:0054748` | Fanconi anemia, complementation group S | `AGREES` |
| FA-T | `MONDO:0014638` | Fanconi anemia complementation group T | `AGREES` |
| FA-U | `MONDO:0014987` | Fanconi anemia complementation group U | `AGREES` |
| FA-V | `MONDO:0014985` | Fanconi anemia complementation group V | `AGREES` |
| FA-W | `MONDO:0044325` | Fanconi anemia, complementation group W | `AGREES` |

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
