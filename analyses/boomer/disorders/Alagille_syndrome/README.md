# Alagille syndrome

Boomer grounding analysis for [`kb/disorders/Alagille_syndrome.yaml`](../../../../kb/disorders/Alagille_syndrome.yaml).

- **Entry term:** [`MONDO:0007318`](http://purl.obolibrary.org/obo/MONDO_0007318) Alagille syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| JAG1 point-variant ALGS | `MONDO:0016862` | Alagille syndrome due to a JAG1 point mutation | `AGREES` |
| 20p12 deletion ALGS | `MONDO:0016861` | Alagille syndrome due to 20p12 microdeletion | `AGREES` |
| NOTCH2 point-variant ALGS | `MONDO:0012439` | Alagille syndrome due to a NOTCH2 point mutation | `AGREES` |

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
