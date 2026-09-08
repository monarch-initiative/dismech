# Kallmann Syndrome

Boomer grounding analysis for [`kb/disorders/Kallmann_Syndrome.yaml`](../../../../kb/disorders/Kallmann_Syndrome.yaml).

- **Entry term:** [`MONDO:0018800`](http://purl.obolibrary.org/obo/MONDO_0018800) Kallmann syndrome
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ANOS1 | `MONDO:0010635` | hypogonadotropic hypogonadism 1 with or without anosmia | `AGREES` | ✓ NCIT |
| FGFR1 | `MONDO:0007844` | hypogonadotropic hypogonadism 2 with or without anosmia | `AGREES` | silent (DOID) |
| FGF8 | `MONDO:0012988` | hypogonadotropic hypogonadism 6 with or without anosmia | `AGREES` | silent (DOID, MESH) |
| CHD7 | `MONDO:0012880` | hypogonadotropic hypogonadism 5 with or without anosmia | `AGREES` | silent (DOID, MESH) |
| SPRY4 | `MONDO:0014102` | hypogonadotropic hypogonadism 17 with or without anosmia | `AGREES` | silent (DOID) |

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
