# Trichothiodystrophy

Boomer grounding analysis for [`kb/disorders/Trichothiodystrophy.yaml`](../../../../kb/disorders/Trichothiodystrophy.yaml).

- **Entry term:** [`MONDO:0018053`](http://purl.obolibrary.org/obo/MONDO_0018053) trichothiodystrophy
- **Grounded subtypes:** 12
- **Verdicts:** AGREES 10, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Photosensitive TTD | `MONDO:0002470` | photosensitive trichothiodystrophy | `AGREES` | ✓ DOID |
| TTD1 (ERCC2) | `MONDO:0011125` | trichothiodystrophy 1, photosensitive | `AGREES` | ✓ DOID, NCIT |
| TTD2 (ERCC3) | `MONDO:0014615` | trichothiodystrophy 2, photosensitive | `AGREES` | ✓ DOID, NCIT |
| TTD3 (GTF2H5) | `MONDO:0014619` | trichothiodystrophy 3, photosensitive | `AGREES` | ✓ DOID, NCIT |
| TTD4 (MPLKIP) | `MONDO:0021013` | trichothiodystrophy 4, nonphotosensitive | `AGREES` | ✓ DOID, NCIT |
| TTD5 (RNF113A) | `MONDO:0010495` | trichothiodystrophy 5, nonphotosensitive | `AGREES` | ✓ DOID |
| TTD6 (GTF2E2) | `MONDO:0014841` | trichothiodystrophy 6, nonphotosensitive | `AGREES` | ✓ DOID |
| TTD7 (TARS1) | `MONDO:0032806` | trichothiodystrophy 7, nonphotosensitive | `AGREES` | ✓ DOID, NCIT |
| TTD8 (AARS1) | `MONDO:0030517` | trichothiodystrophy 8, nonphotosensitive | `AGREES` | ✓ DOID |
| TTD9 (MARS1) | `MONDO:0030518` | trichothiodystrophy 9, nonphotosensitive | `AGREES` | ✓ DOID |
| CARS1-Related MDBH | `MONDO:0030047` | microcephaly, developmental delay, and brittle hair syndrome | `SILENT` | — no shared vocabulary |
| DBR1-Related Sabinas TTD | `MONDO:0008886` | Sabinas brittle hair syndrome | `SILENT` | ✓ DOID, icd11f |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **DBR1-Related Sabinas TTD** — DOID (DOID:0111874), icd11f (icd11f:1722502589)

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.
