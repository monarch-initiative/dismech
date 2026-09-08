# Hunter syndrome

Boomer grounding analysis for [`kb/disorders/Hunter_syndrome.yaml`](../../../../kb/disorders/Hunter_syndrome.yaml).

- **Entry term:** [`MONDO:0010674`](http://purl.obolibrary.org/obo/MONDO_0010674) mucopolysaccharidosis type 2
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Neuronopathic | `MONDO:0016315` | mucopolysaccharidosis type 2, severe form | `AGREES` | ✓ ORDO |
| Non-neuronopathic | `MONDO:0016316` | mucopolysaccharidosis type 2, attenuated form | `AGREES` | ✓ ORDO |

## What boomer did

The solver has **not been run** for this input. No mapping acceptance,
retraction, posterior probability or global-consistency result is asserted.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).
