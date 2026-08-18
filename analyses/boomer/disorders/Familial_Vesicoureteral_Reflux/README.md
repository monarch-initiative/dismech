# Familial Vesicoureteral Reflux

Boomer grounding analysis for [`kb/disorders/Familial_Vesicoureteral_Reflux.yaml`](../../../../kb/disorders/Familial_Vesicoureteral_Reflux.yaml).

- **Entry term:** [`MONDO:0017329`](http://purl.obolibrary.org/obo/MONDO_0017329) familial vesicoureteral reflux
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| VUR1 | `MONDO:0008653` | vesicoureteral reflux 1 | `AGREES` |
| VUR2 | `MONDO:0012573` | vesicoureteral reflux 2 | `AGREES` |
| VUR3 | `MONDO:0013356` | vesicoureteral reflux 3 | `AGREES` |
| VUR4 | `MONDO:0013682` | vesicoureteral reflux 4 | `AGREES` |
| VUR5 | `MONDO:0013683` | vesicoureteral reflux 5 | `AGREES` |
| VUR6 | `MONDO:0013684` | vesicoureteral reflux 6 | `AGREES` |
| VUR7 | `MONDO:0014161` | vesicoureteral reflux 7 | `AGREES` |
| VUR8 | `MONDO:0014422` | vesicoureteral reflux 8 | `AGREES` |
| VURX | `MONDO:0010755` | vesicoureteral reflux, X-linked | `AGREES` |

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
