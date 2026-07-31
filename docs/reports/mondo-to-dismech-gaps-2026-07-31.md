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
| Covered disorder anchors | 1,579 |
| Anchors with ≥1 uncovered Mondo child | 796 |
| Total uncovered child subtypes | 4,813 |
| …from broad anchors (>15 children) | 1,388 (29%) — too-high anchor |
| …from clean anchors (1–15 children) | **3,425 (71%) — high-signal targets** |

## Read tiered (same broad-anchor caveat as the other audits)

**39 anchors have >15 uncovered children** — these are entries anchored to a broad Mondo
term (`Mediator_Complex_Neurodevelopmental_Disorder` → *congenital nervous system
disorder*, 192; `BBSome-Related_Retinitis_Pigmentosa` → *retinitis pigmentosa*, 101), so
"uncovered children" is really the whole family and the finding is an **anchoring problem**
(fix per [#7178](https://github.com/monarch-initiative/dismech/issues/7178)), not a
curation backlog. This is the same broad-anchor set the gene/phenotype/anchoring audits
flag — the through-line of #7175.

## High-signal curation targets (clean tier, 757 anchors)

Anchors with a small, reviewable set of uncovered Mondo subtypes. Representative:

| dismech entry (parent) | Uncovered Mondo subtypes (sample) |
|---|---|
| `Noonan_Syndrome` | Noonan syndrome 1, 2, 3, 4, 5 … |
| `Zellweger_Spectrum_Disorders` | peroxisome biogenesis disorder due to PEX1/2/3/5 defect … |
| `Meckel_Syndrome` | Meckel syndrome type 1, 2, 3, 4 … |
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
- **Coverage = disorder `disease_term` anchors** — a subtype curated only as a
  `has_subtypes` block (no own MONDO anchor) is not counted as "covered" and may appear as
  an uncovered child. So the raw list slightly over-states gaps for diseases that model
  subtypes internally; the TSV is a candidate list, not a defect list.
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
