# Malaria

Boomer grounding analysis for [`kb/disorders/Malaria.yaml`](../../../../kb/disorders/Malaria.yaml).

- **Entry term:** [`MONDO:0005136`](http://purl.obolibrary.org/obo/MONDO_0005136) malaria
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Plasmodium falciparum malaria | `MONDO:0005920` | Plasmodium falciparum malaria | `AGREES` | ✓ DOID, MESH, NCIT |
| Plasmodium vivax malaria | `MONDO:0005921` | Plasmodium vivax malaria | `AGREES` | ✓ DOID, MESH, NCIT |
| Cerebral malaria | `MONDO:0005625` | cerebral malaria | `AGREES` | ✓ DOID, MESH, NCIT |
| Recurrent vivax malaria | `MONDO:0005921` | Plasmodium vivax malaria | `AGREES` | ✓ DOID, MESH, NCIT |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Malaria#Recurrent vivax malaria` ≡ `MONDO:0005921`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
