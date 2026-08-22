# Gastric Adenocarcinoma

Boomer grounding analysis for [`kb/disorders/Gastric_Adenocarcinoma.yaml`](../../../../kb/disorders/Gastric_Adenocarcinoma.yaml).

- **Entry term:** [`MONDO:0005036`](http://purl.obolibrary.org/obo/MONDO_0005036) gastric adenocarcinoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Intestinal | `MONDO:0005037` | gastric intestinal type adenocarcinoma | `AGREES` | ✓ NCIT |
| Diffuse | `MONDO:0005017` | diffuse gastric adenocarcinoma | `AGREES` | ✓ DOID, NCIT |
| HDGC | `MONDO:0007648` | hereditary diffuse gastric adenocarcinoma | `AGREES` | ✓ NCIT |

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
