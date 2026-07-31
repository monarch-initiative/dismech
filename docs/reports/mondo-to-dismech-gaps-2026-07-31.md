# Mondo → dismech curation targets (neighborhood gaps)

**Date:** 2026-07-31
**Issue:** [#7175](https://github.com/monarch-initiative/dismech/issues/7175) — tripartite gap-exchange (dismech ⇄ Monarch KG ⇄ Mondo)
**Scope:** bounded to the **neighborhood** of what dismech already curates (not all ~20k Mondo terms, most of which are out of dismech scope by design).
**Regenerate:**

```bash
uv run python scripts/mondo_to_dismech_gaps.py --tsv research/mondo_to_dismech_gaps.tsv
```

The reverse-direction flow: **Mondo → dismech**. For each MONDO term dismech uses as a
disorder `disease_term` anchor, it finds that term's direct `is_a` children in Mondo that
dismech does **not** curate — i.e. "dismech has the parent *X* but not its Mondo subtypes
*X1, X2 …*". High-signal curation targets with low noise, because coverage is scoped to
the descendants of already-curated terms.

## Headline

| Metric | Value |
|---|---|
| Covered anchors (disease + subtype level) | 2,354 |
| Disease-level anchors expanded | 1,585 |
| Anchors with ≥1 uncovered Mondo child | 702 |
| Total uncovered child subtypes | 3,929 |
| …from broad anchors (>15 children) | 1,225 (31%) — too-high anchor |
| …from clean anchors (1–15 children) | **2,704 (69%) — high-signal targets** |

> **Subtype-aware (updated).** The covered set now includes both disease-level
> `disease_term` anchors **and** `has_subtypes[].subtype_term` anchors, so a Mondo subtype
> dismech already curates inside a parent entry is no longer reported as uncovered. This
> removed ~880 already-curated rows (e.g. `Meckel_Syndrome` dropped from 14 uncovered
> children to 2). The tier split is emitted by `scripts/mondo_to_dismech_gaps.py`.

## Read tiered (same broad-anchor caveat as the other audits)

**34 anchors have >15 uncovered children** — these are entries anchored to a broad Mondo
term (`Mediator_Complex_Neurodevelopmental_Disorder` → *congenital nervous system
disorder*; `BBSome-Related_Retinitis_Pigmentosa` → *retinitis pigmentosa*), so
"uncovered children" is really the whole family and the finding is an **anchoring problem**
(fix per [#7178](https://github.com/monarch-initiative/dismech/issues/7178)), not a
curation backlog. This is the same broad-anchor set the gene/phenotype/anchoring audits
flag — the through-line of #7175.

## High-signal curation targets (clean tier, 668 anchors)

Anchors with a small, reviewable set of uncovered Mondo subtypes. Representative:

| dismech entry (parent) | Uncovered Mondo subtypes (sample) |
|---|---|
| `Noonan_Syndrome` | Noonan syndrome 1, 2, 3, 4, 5 … |
| `Zellweger_Spectrum_Disorders` | peroxisome biogenesis disorder due to PEX1/2/3/5 defect … |
| `Progressive_Myoclonus_Epilepsy` | MERRF, action myoclonus-renal failure, EPM3 … |
| `Common_Variable_Immunodeficiency` | CVID 1, 2, 3, 4 … |
| `Autosomal_Recessive_Congenital_Ichthyosis` | ARCI 1, 4A, 5, 8, 11 … |
| `Spinal_Muscular_Atrophy` | scapuloperoneal / segmental / Ryukyuan / FSH type … |
| `Age_Related_Macular_Degeneration` | AMD 1, 2, 3, 7; wet macular degeneration … |
| `Junctional_Epidermolysis_Bullosa` | Herlitz / non-Herlitz / with pyloric atresia … |
| `IgG4-Related_Disease` | IgG4-related kidney/aortitis/mesenteritis/pachymeningitis … |
| `Left_Ventricular_Noncompaction` | LVNC 1, 2 … |

Full list: `research/mondo_to_dismech_gaps.tsv`.

## Interpretation — most clean targets are *allelic/numbered series*

A large share of the uncovered children are **numbered allelic subtypes of a single
mechanism** (Noonan 1–5, CVID 1–4, ARCI 1–11, LVNC 1–2). Under the record-altitude policy
([#7178](https://github.com/monarch-initiative/dismech/issues/7178)) these are usually
**not** new standalone records: same mechanism graph → model as `has_subtypes` within the
existing parent entry, not N new files. So this list feeds curation as *"enrich the parent
entry's subtypes"* far more often than *"create N new entries"*. Genuinely mechanism-distinct
children (e.g. an IgG4 organ-specific manifestation, a syndromic vs non-syndromic split)
are the ones that may warrant their own entry.

## Caveats

- **`is_a` direct children only** — grandchildren and other-relation children are not
  enumerated (keeps the list to one level and high-precision).
- **Coverage = `disease_term` + `has_subtypes[].subtype_term` anchors** — subtypes curated
  inside a parent entry *with* their own MONDO `subtype_term` are now counted as covered.
  A subtype modeled with **no** MONDO anchor at all still can't be matched and may appear as
  an uncovered child, so the TSV remains a candidate list, not a defect list.
- **Broad anchors dominate the tail** — always read the clean tier; fix broad anchors first.

## Machine-readable worklist

`research/mondo_to_dismech_gaps.tsv` — `dismech_disorder`, `parent_mondo`, `parent_label`,
`uncovered_child_mondo`, `child_label` (one row per uncovered child).

## #7175 status

With this flow, all six directed gap-flows have a first reproducible pass:
dismech→Mondo (terms + groupings), Monarch KG⇄dismech (genes; phenotypes + subsumption),
and Mondo→dismech (this report). The recurring finding across every flow is that
**anchor quality gates interpretation** — the broad/mis-anchored entries are the highest
leverage fix and connect directly to the record-altitude decision in #7178.
