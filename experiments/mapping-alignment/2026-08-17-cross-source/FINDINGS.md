# dismech direct external mappings vs MONDO's own xrefs

**Run date:** 2026-08-17
**KB state:** `d1f1d3c78e` (main, after #8671)
**MONDO:** local semantic-sql build, `~/.data/oaklib/mondo.db`, retrieved 2026-08-11
**Tooling:** [`crosssource_audit.py`](../scripts/crosssource_audit.py)

## Question

A dismech entry reaches an external vocabulary two ways: directly, through
`mappings.icd10cm_mappings` / `icd11f_mappings` / `ncit_mappings`; and
transitively, through its `disease_term`, since MONDO carries its own
`skos:exactMatch` and `oio:hasDbXref` links to OMIM, ORDO, DOID, UMLS, SNOMED,
ICD and NCIT.

Where both routes reach the same vocabulary but land on different terms, the two
assertions compete. How often does that happen, and does it matter?

## Results

**7 disagreements** across the whole KB. Only **1** has dismech asserting
`exactMatch` — the rest are `close`/`narrow`/`broadMatch`, where a different term
is not a contradiction.

| Entry | dismech | MONDO's xref | Reading |
|---|---|---|---|
| `Malignant_Peritoneal_Mesothelioma` | `NCIT:C9350` (**exactMatch**) | `NCIT:C8704` | Two exact identity claims to different NCIT terms — the one real conflict |
| `Aflatoxin_Related_HCC` | `NCIT:C3099` (closeMatch) | `NCIT:C27922` | dismech points at generic HCC; MONDO's aflatoxin-specific term is more precise |
| `Angelman_Syndrome` | `ICD10CM:Q93.5` (narrowMatch) | `ICD10:Q93.51` | Parent code vs child code — granularity |
| `Epidermolysis_Bullosa` | `ICD10CM:Q81.9` (closeMatch) | `ICD10:Q81` | Granularity |
| `Hodgkin_Lymphoma` | `ICD10CM:C81.9` (closeMatch) | `ICD10:C81` | Granularity |
| `CINCA_Syndrome` | `NCIT:C84657` (broadMatch) | `NCIT:C116380` | Correctly recorded as broader |
| `MSI_High_Colorectal_Cancer` | `NCIT:C2955` (closeMatch) | `NCIT:C4978` | Molecular subtype vs parent |

## Interpretation

This is a **negative result for the solver**, and worth recording as one.

Six of seven are granularity differences that the `mapping_predicate` already
records honestly — an `ICD10CM` parent code and MONDO's child code are both
correct statements, and dismech's `narrowMatch`/`closeMatch` says so. There is no
inconsistency for a reasoner to resolve.

The remaining case is a two-line check, not a search problem.

The `Aflatoxin_Related_HCC` row is a direct follow-on from #8671: that PR
regrounded the entry from generic HCC to `MONDO:0003245`
*aflatoxin-related hepatocellular carcinoma*, but left the NCIT mapping pointing
at `NCIT:C3099` *Hepatocellular Carcinoma*. MONDO's own xref for the new term is
`NCIT:C27922`. Worth following up, and a reminder that regrounding an entry can
leave its sibling mappings stale.

## Limits of this measurement

- **Prefix normalisation is a heuristic.** dismech writes `icd11f:` where MONDO
  writes `icd11.foundation:`, and `ICD10CM:` against MONDO's `ICD10:`. Those are
  collapsed before comparison (see `PREFIX_ALIASES`). ICD-10-CM is a US clinical
  modification of ICD-10 and the two code sets are not identical, so treating
  them as one vocabulary slightly overstates comparability.
- **Only entries that make a direct mapping are in scope** — a few dozen. Most of
  the KB reaches external vocabularies through MONDO only, and has nothing to
  disagree with.
- **Granularity is judged from the predicate, not the code hierarchy.** The
  script does not check that `ICD10:Q93.51` is genuinely under `ICD10CM:Q93.5`;
  the "granularity" reading in the table above is a human one.

## Reproducing

```bash
uv run python experiments/mapping-alignment/scripts/crosssource_audit.py \
    --out experiments/mapping-alignment/2026-08-17-cross-source/disagreements.tsv
```

No solver required.
