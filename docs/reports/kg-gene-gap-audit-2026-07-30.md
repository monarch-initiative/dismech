# Monarch KG ⇄ dismech gene–disease comparison

**Date:** 2026-07-30
**Issue:** [#7175](https://github.com/monarch-initiative/dismech/issues/7175) — tripartite gap-exchange (dismech ⇄ Monarch KG ⇄ Mondo)
**Scope:** the 1,063 `kb/disorders` entries with a MONDO primary anchor **and** curated genes (`genetic[].gene_term`).
**Source:** Monarch v3 API (`api-v3.monarchinitiative.org`), Causal + Correlated gene-to-disease edges.
**Regenerate:**

```bash
uv run python scripts/kg_gene_gap_audit.py --tsv research/kg_gene_gap.tsv   # resumable via local cache
```

This is the **Monarch KG ⇄ dismech** flow of #7175 (two directions at once). For each
disease it diffs dismech's curated gene set against the KG's gene–disease edges for the
same MONDO term:

- **`kg_only`** — KG links the gene, dismech does not → **dismech coverage gap**
- **`dismech_only`** — dismech curates the gene, KG does not → **dismech → KG candidate** (or to verify)
- **`overlap`** — agreement

## Headline

| Metric | Value |
|---|---|
| Diseases compared (MONDO + genes) | **1,063** |
| …with ≥1 KG gene edge | 944 |
| …with **no** KG gene edge | 119 |
| dismech gene assertions | 2,699 |
| KG gene assertions | 6,342 |
| Overlap | 1,896 |
| `kg_only` (raw) | 4,446 |
| `dismech_only` | **803** |

## The raw `kg_only` is inflated by broad anchors — tier before reading it

**28 diseases return >30 KG genes and contribute 2,970 (67%) of the raw `kg_only`.**
These are entries anchored to a broad grouping/parent MONDO term, so the KG returns the
whole family's genes — an **anchoring problem, not a per-disease gene gap**. This
independently cross-validates the [Mondo-anchoring audit](mondo-anchoring-audit-2026-07-30.md):
e.g. `ANK2_Related_…` and `BLOC1S1-related_…` both anchor to MONDO:0100038 (complex NDD)
and both return the same 250 genes — the exact shared-anchor pair flagged there.

| Tier (by KG gene count) | Diseases | Reading |
|---|---|---|
| no KG gene edge | 119 | dismech-original curation, or the MONDO term has no KG genes |
| **broad-anchor (n_kg > 30)** | **28** | broad/mis-anchor — fix the anchor, don't chase "gaps" |
| **clean (1–30)** | **916** | interpretable; **clean `kg_only` = 1,476 real coverage-gap candidates** |

Worst broad anchors: `PGM2L1_Deficiency` (MONDO:0700092, 637 KG genes vs 1 dismech),
`Mediator_Complex_Neurodevelopmental_Disorder` (388), `Epilepsy` (MONDO:0005027, 215),
`Inherited_Retinal_Dystrophy` (193), `MYO6_Hearing_Loss` (145). (Full list in the TSV
where `n_kg > 30`.)

## A. dismech coverage gaps (KG has the gene, dismech doesn't)

From the **clean** subset (interpretable), the highest-value examples where dismech is
under-curated relative to the KG:

- **`Glioma`** (MONDO:0021042): KG adds BRAF, KRAS, FGFR1/3, NF2, NTRK2, TP53, ROS1, MYB…
- **`Type_2_Diabetes_Mellitus`** (MONDO:0005148): KG adds the MODY/T2D panel — GCK, HNF1A/1B/4A, ABCC8, PDX1, NEUROD1, IRS1/2…
- **`Brugada_Syndrome`** (MONDO:0015263): dismech 1 gene vs KG 22 (the SCN/CACN/KCN channel panel)
- **`Congenital_Hypothyroidism`**, **`Kallmann_Syndrome`**, **`Nephronophthisis`**,
  **`Jeune_Asphyxiating_Thoracic_Dystrophy`**, **`Inherited_Ichthyosis`** — each missing
  much of the KG's established gene panel.

## B. Zero-overlap disagreements (both have genes, none shared) — 32

The most diagnostic tier. Two distinct causes, which must be told apart:

**B1 — genuine dismech gaps (dismech missing the canonical gene(s)):**
- **`Lynch_Syndrome`** (MONDO:0005835): dismech has only **RPS20**; KG has the canonical
  MMR set **MLH1, MSH2, MSH6, PMS2, EPCAM** — a clear, important gap.
- **`Medullary_Thyroid_Carcinoma`** (MONDO:0015277): dismech has RAS genes; KG has **RET**
  (the defining MTC gene).
- **`Ewing_Sarcoma`** (MONDO:0012817): dismech has STAG2/TP53/CDKN2A; KG has the defining
  fusion genes **EWSR1, FLI1, ERG, ETV1/4**.
- **`Diffuse_Large_B_Cell_Lymphoma`**: dismech MYD88; KG **BCL2, BCL6, ALK, XPO1**.

**B2 — anchoring mismatch (dismech curates a valid but different aspect, or the anchor is
too generic):**
- **`Chemotherapy_Induced_Neutropenia`** → MONDO:0001475 (generic *neutropenia*): dismech
  has the pharmacogenomic **UGT1A1**; KG returns the **congenital** neutropenia panel
  (ELANE, HAX1, G6PC3…). The dismech concept is anchored to a too-generic term.
- **`Chemotherapy_Induced_Diarrhea`** → MONDO:0001673 (*diarrheal disease*): dismech
  UGT1A1/DPYD (pharmacogenomic) vs KG congenital-diarrhea genes — same too-generic anchor,
  reinforcing the diarrheal-disease finding in the anchoring audit's Tier 3.
- **`Type_I_Diabetes`**: dismech autoimmune-susceptibility panel (CTLA4, PTPN22, INS,
  IL2RA…) vs KG HNF1A/IL6 — different, both defensible; a modeling/framing difference.

(Full 32 in the script output and TSV.)

## C. `dismech_only` — genes dismech curates that the KG lacks (803)

The reverse direction — potential **dismech → KG contributions**, or curation to verify.
This set is less noisy than raw `kg_only` (a dismech entry rarely over-lists genes). It
includes legitimately dismech-specific curation (e.g. the Type I Diabetes autoimmune
panel above) and is the natural feed for a dismech → Monarch KG hand-off. Per-disease
values are the `dismech_only` column of the TSV.

## Caveats

- **Anchor quality gates everything.** Read tiered — never the raw `kg_only`. Broad/mis-anchored
  entries (§ tier table) must be fixed at the anchor before any gene-gap reading is valid.
- **Causal + Correlated only.** Other edge types (GenotypeToDisease, variant-level) are not
  counted; a gene present only via those routes reads as `kg_only`/`dismech_only` here.
- **Curation intent differs from the KG.** dismech genes carry a `relationship_type`
  (causal / susceptibility / modifier); the KG mixes causal and correlated. Some
  disagreements are framing, not error (see B2).

## Machine-readable worklist

`research/kg_gene_gap.tsv` — one row per disease: `disorder`, `mondo_id`, `n_dismech`,
`n_kg`, `n_overlap`, `kg_only`, `dismech_only` (gene lists as `HGNC:id(SYMBOL)`).

## Follow-ups (#7175)

- Same diff for **disease → phenotype** (HP) edges — the other large KG↔dismech axis.
- Feed §A/§B1 into curation; feed §C into a dismech → KG contribution set.
- Fix the 28 broad anchors (overlaps the record-altitude policy call, [#7178](https://github.com/monarch-initiative/dismech/issues/7178)).
