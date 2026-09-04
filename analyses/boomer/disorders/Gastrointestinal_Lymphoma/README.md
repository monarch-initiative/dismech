# Gastrointestinal Lymphoma

Boomer grounding analysis for [`kb/disorders/Gastrointestinal_Lymphoma.yaml`](../../../../kb/disorders/Gastrointestinal_Lymphoma.yaml).

- **Entry term:** [`MONDO:0004699`](http://purl.obolibrary.org/obo/MONDO_0004699) gastrointestinal lymphoma
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Gastric | `MONDO:0001059` | gastric lymphoma | `AGREES` | ✓ NCIT |
| Small Intestine | `MONDO:0001852` | small intestine lymphoma | `AGREES` | ✓ NCIT |
| Colon | `MONDO:0002035` | colon lymphoma | `AGREES` | ✓ NCIT |
| Esophagus | `MONDO:0001188` | esophagus lymphoma | `AGREES` | ✓ NCIT |
| Rectum | `MONDO:0002166` | rectum lymphoma | `AGREES` | ✓ NCIT |

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
