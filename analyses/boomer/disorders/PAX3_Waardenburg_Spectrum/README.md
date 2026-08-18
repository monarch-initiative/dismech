# PAX3-Related Waardenburg Syndrome

Boomer grounding analysis for [`kb/disorders/PAX3_Waardenburg_Spectrum.yaml`](../../../../kb/disorders/PAX3_Waardenburg_Spectrum.yaml).

- **Entry term:** [`MONDO:0018094`](http://purl.obolibrary.org/obo/MONDO_0018094) Waardenburg syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| WS1 | `MONDO:0008670` | Waardenburg syndrome type 1 | `AGREES` |
| WS3 | `MONDO:0007862` | Waardenburg syndrome type 3 | `AGREES` |

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
