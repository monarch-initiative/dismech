# Acrodysostosis

Boomer grounding analysis for [`kb/disorders/Acrodysostosis.yaml`](../../../../kb/disorders/Acrodysostosis.yaml).

- **Entry term:** [`MONDO:0019797`](http://purl.obolibrary.org/obo/MONDO_0019797) acrodysostosis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0007044` | Acrodysostosis 1 with or without hormone resistance | `AGREES` | — no shared vocabulary |
| Type 2 | `MONDO:0013822` | acrodysostosis 2 with or without hormone resistance | `AGREES` | — no shared vocabulary |

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
