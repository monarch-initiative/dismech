# Photosensitive Epilepsy

Boomer grounding analysis for [`kb/disorders/Photosensitive_Epilepsy.yaml`](../../../../kb/disorders/Photosensitive_Epilepsy.yaml).

- **Entry term:** [`MONDO:0015643`](http://purl.obolibrary.org/obo/MONDO_0015643) photosensitive epilepsy
- **Grounded subtypes:** 5
- **Verdicts:** SILENT 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Photosensitive Occipital Lobe Epilepsy | `MONDO:0100021` | photosensitive occipital lobe epilepsy | `SILENT` | — no shared vocabulary |
| Photosensitivity in Juvenile Myoclonic Epilepsy | `MONDO:0009696` | juvenile myoclonic epilepsy | `SILENT` | silent (DOID, ORDO, icd11f) |
| Photosensitivity as the Archetypal Syndrome, Jeavons Syndrome | `MONDO:0015346` | epilepsy with eyelid myoclonia | `SILENT` | silent (ORDO, icd11f) |
| Photosensitivity in Dravet Syndrome | `MONDO:0100135` | Dravet syndrome | `SILENT` | silent (DOID, icd11f) |
| Photosensitivity in the Progressive Myoclonic Epilepsies | `MONDO:0020074` | progressive myoclonus epilepsy | `SILENT` | silent (DOID, ORDO, icd11f) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

5 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
