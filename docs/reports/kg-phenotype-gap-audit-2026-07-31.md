# Monarch KG ⇄ dismech disease–phenotype comparison

**Date:** 2026-07-31
**Issue:** [#7175](https://github.com/monarch-initiative/dismech/issues/7175) — tripartite gap-exchange (dismech ⇄ Monarch KG ⇄ Mondo)
**Scope:** the 1,609 `kb/disorders` entries with a MONDO primary anchor **and** curated phenotypes (`phenotypes[].phenotype_term`).
**Source:** Monarch v3 API, `DiseaseToPhenotypicFeatureAssociation` edges.
**Regenerate:**

```bash
uv run python scripts/kg_phenotype_gap_audit.py --tsv research/kg_phenotype_gap.tsv   # resumable via local cache
```

The disease→phenotype counterpart of the [gene–disease audit](kg-gene-gap-audit-2026-07-30.md).
For each disease it diffs dismech's HP terms against the KG's HPOA phenotype
annotations for the same MONDO term (exact HP-id match).

## Headline

| Metric | Value |
|---|---|
| Diseases compared (MONDO + phenotypes) | **1,609** |
| …with ≥1 KG phenotype edge | 1,346 |
| …with **no** KG phenotype edge | **263** |
| dismech HP assertions | 16,939 |
| KG HP assertions | **108,907** |
| Overlap (exact) | 10,944 |
| `kg_only` (raw) | 97,963 |
| `dismech_only` | **5,995** |
| Exact-match rate of dismech HP terms | **64.6%** |

## Read this differently from the gene audit

The phenotype axis is **not symmetric with genes**, and the raw `kg_only` must not be
read as "dismech gaps":

- **KG HPOA is ~6.4× denser than dismech** (108,907 vs 16,939). HPOA exhaustively lists
  every phenotype ever annotated to a disease; dismech deliberately curates a **selective,
  mechanistically-relevant subset**. So a large `kg_only` is mostly a **breadth
  difference by design**, not missing content.
- Consequently the actionable signals here are the *other* two: **`dismech_only`** (the
  dismech → KG direction) and the **263 sole-source diseases** (below).
- **Exact-ID matching is a lower bound.** HPO is deep; a dismech term that is a
  parent/child of the KG term reads as a mismatch. True semantic agreement is higher than
  the 64.6% exact rate. Subsumption-aware matching (via the HP hierarchy) is the main
  follow-up refinement.

**Sanity check (highest exact agreement):** the well-curated entries line up cleanly —
Fanconi Anemia 101 overlap, Alpha Mannosidosis 64/64, Takayasu Arteritis 52/52,
Cystinosis 57/57, Granulomatosis with Polyangiitis 63/65. Where dismech is thorough, it
matches HPOA nearly term-for-term.

## Subsumption-aware refinement (recommended reading)

Exact-ID matching is a lower bound. Re-scoring against the HP `is_a` hierarchy
(`scripts/kg_phenotype_subsumption.py`, run offline from the same cache — no extra API
calls) recovers granularity differences a dismech term shares with a parent/child KG term:

| Match class | Count | % of dismech HP |
|---|---|---|
| EXACT | 10,944 | 64.6% |
| + MORE_SPECIFIC (dismech finer than KG) | 864 | |
| + MORE_GENERAL (dismech coarser than KG) | 931 | |
| **= SEMANTIC overlap** | **12,739** | **75.2%** |
| UNMATCHED (truly novel dismech HP) | 4,200 | 24.8% |

**Exact 64.6% → subsumption-aware 75.2% (+10.6 pts).** So a tenth of the apparent
"disagreement" is just dismech and HPOA describing the same phenotype at different
granularity — real agreement, not a gap. The **4,200 UNMATCHED** terms are the refined,
higher-confidence dismech → KG contribution set (down from 5,995 raw `dismech_only`);
worklist in `research/kg_phenotype_subsumption.tsv` (`unmatched_terms` column). It stays
concentrated in the same sole-source diseases — Dravet (46 of 49 novel), Long COVID,
Multiple Sclerosis, Celiac, IBD, Murine Typhus, Monkeypox, AL Amyloidosis — confirming §A.

## Tiers by KG phenotype count

| Tier | Diseases | Reading |
|---|---|---|
| no KG phenotype edge | 263 | dismech is the **sole phenotype source** → dismech → KG candidates |
| broad (n_kg > 60) | 466 | HPOA-dense; contribute 79,267 (81%) of raw `kg_only` — breadth, not gaps |
| clean (1–60) | 880 | clean `kg_only` = 18,696 candidate enrichments (still breadth-caveated) |

## A. dismech as sole phenotype source (263) — strongest dismech → KG signal

Diseases where dismech curates phenotypes but the KG's HPOA has **none** for that MONDO
term. Strikingly, these skew toward **common/complex and infectious/acquired** conditions
— exactly where HPOA (built for rare/Mendelian disease) is thin and dismech adds value:

`Long_COVID` (23 HP), `Multiple_Sclerosis` (22), `Celiac_Disease` (22), `Ulcerative_Colitis`
(14), `Crohn_Disease`, `Murine_Typhus` (23), `Hantavirus_Pulmonary_Syndrome` (16),
`Monkeypox` (14), `Neurosarcoidosis` (14), `Organophosphate_Poisoning` (14),
`AL_Amyloidosis` (13), `Esophageal_Atresia` (15).

These are the cleanest whole-disease contributions to hand to Monarch/HPOA.

## B. `dismech_only` — phenotypes dismech curates that the KG lacks (5,995)

Per-disease phenotype-level contributions (or subsumption artifacts to verify). Top
contributors:

- **`Dravet_syndrome`** (MONDO:0100135): 48 dismech-only vs **1** KG phenotype — the MONDO
  term is essentially unannotated in HPOA; dismech has a full phenotype set.
- **`Fanconi_Anemia`**: 38 dismech-only *on top of* 101 overlap — rich in both directions.
- **`Hypochondroplasia`** (26), **`Crohn_Disease`** (24), **`COPA_Syndrome`** (18),
  **`Cardiospondylocarpofacial_Syndrome`** (20), **`MED13_Syndrome`** (17).

Some of the 5,995 will be granularity mismatches (dismech's term is a parent/child of an
HPOA term) rather than true novel annotations — subsumption-aware matching will separate
these. Until then, treat `dismech_only` as a **candidate** contribution set.

## C. Clean `kg_only` — candidate phenotype enrichments (18,696)

For the 880 clean-tier diseases, phenotypes HPOA annotates that dismech doesn't yet carry.
Given dismech's selective-curation design this is **optional enrichment**, not a defect —
useful as a curator prompt ("did we omit a mechanistically relevant phenotype?") rather
than a gap to close wholesale. Examples with modest, reviewable lists: `Blau_Syndrome`,
`Niemann-Pick_Disease_Type_B`, `neuroferritinopathy`, `Creatine_Transporter_Deficiency`,
`SETBP1_Disorder` (see the TSV's `kg_only` column).

## Caveats

- **Exact-ID match only** — a lower bound on agreement; subsumption not accounted for.
- **HPOA breadth ≠ dismech scope** — raw `kg_only` is a breadth difference by design;
  never read it as a gap count.
- **Broad anchors still noisy** — the 466 n_kg>60 entries include broad/grouping anchors
  (as in the gene and anchoring audits); fix the anchor before reading their `kg_only`.

## Machine-readable worklist

`research/kg_phenotype_gap.tsv` — one row per disease: `disorder`, `mondo_id`,
`n_dismech`, `n_kg`, `n_overlap`, `kg_only`, `dismech_only` (HP lists as `HP:id(label)`).

## Follow-ups (#7175)

- ✅ **Subsumption-aware matching** (HP hierarchy) — done (`kg_phenotype_subsumption.py`;
  see the refinement section above). Exact 64.6% → semantic 75.2%.
- Feed §A (263 sole-source) and the 4,200 subsumption-UNMATCHED terms into a dismech →
  Monarch/HPOA contribution set.
- Groupings/modules anchoring; **Mondo → dismech** curation-target direction (scope call pending).
