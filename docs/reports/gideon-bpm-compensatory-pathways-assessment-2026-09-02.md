# GIDEON / Between-Pathway Models: relevance assessment for dismech

**Date:** 2026-09-02
**Source paper:** Garcia JJ, Yu KM, Freudenreich CH, Cowen LJ. *A novel ILP framework
to identify compensatory pathways in genetic interaction networks with GIDEON.*
Bioinformatics 2026;42(Suppl 2):btag385. DOI:
[10.1093/bioinformatics/btag385](https://doi.org/10.1093/bioinformatics/btag385)
(open access, CC-BY). Code and full BPM set:
[github.com/jocelynjgarcia/GIDEON](https://github.com/jocelynjgarcia/GIDEON),
archived at [doi:10.5281/zenodo.20130057](https://doi.org/10.5281/zenodo.20130057).
**Status:** analysis note — no KB content change proposed in this report.

## What the paper does

GIDEON (Genetic Interaction-Driven Extraction of Optimal Networks) mines the
genome-scale *S. cerevisiae* genetic interaction network (Costanzo et al. 2016,
pairwise double-knockout fitness for nearly all non-essential gene pairs) for
**Between-Pathway Models (BPMs)**: paired gene sets where negative (synthetic-sick)
interactions run *between* the two sets and positive interactions run *within*
each set. That motif is the graph signature of **compensatory pathways** — knocking
out one gene from each pathway disables both routes and makes the cell sick, while
two knockouts within one pathway leave the other route intact.

Two methodological contributions:

1. **A gene-centered ILP.** Rather than one global optimization that converges on
   the same best BPM repeatedly (the failure mode of the prior Liany et al. 2022
   ILP, which had to delete discovered edges from the network to make progress),
   GIDEON solves a separate ILP per gene, constrained so that gene is the primary
   contributor to its BPM's objective. Interactions can therefore appear in
   multiple BPMs — biologically right, since real pathways share components.
2. **Distribution-informed (DI) edge weights.** Epistasis for a pair is scored as
   the residual from a linear regression over each component gene's *whole marginal
   distribution* of double-knockout fitnesses, rather than from a two-gene
   multiplicative null alone. This needs only single- and double-mutant fitness
   values (no array-position/batch metadata), and improves competitor methods too.

Results: 3,215 diverse BPMs versus 1,027 (LocalCut) and 750 (Liany-ILP), with 1,220
BPMs whose two modules are enriched for the same function versus 301 and 33. A
highlighted novel BPM ties **aromatic amino acid biosynthesis** to **ergosterol
biosynthesis** (TKL1-centered; strong interactions among ERG3, ERG6, TRP3, ARV1,
ARO7), which the authors read as a lead for antifungal combination targeting. The
discussion flags the human direction: the new genome-scale human genetic
interaction map (Billmann et al., Cell 2026) and cancer synthetic-lethality
prediction (Fong et al. 2025; Liany et al. 2024 ASTER) as the translation path.

## Why this is relevant to dismech

Pathway-level compensation is the systems-biology face of several things dismech
already models explicitly:

- **Synthetic lethality as therapy.** A clinically exploited BPM is exactly what
  `kb/modules/dna_repair_synthetic_lethality.yaml` curates: HRR/FA-BRCA deficiency
  in one "pathway" makes tumors dependent on the backup route that PARP inhibition
  then removes. The BRCA/PARP axis is the flagship human instance of the motif
  GIDEON finds at scale in yeast. Conforming entries (ovarian HGSC, TNBC,
  BRCA-mutant prostate cancer, etc.) already carry the treatment
  `target_mechanisms` pattern for it.
- **Digenic and oligogenic inheritance.** A Mendelian digenic disorder
  (`HP:0010984`, worked exemplar `PRPH2-Related_Retinopathy`) is a germline BPM
  hit: one damaging variant in each of two compensating components, neither
  sufficient alone. The paper's Fig. 1 paralog pair (two genes that buffer each
  other so neither shows single-gene interactions) is likewise the abstract form
  of dismech's `MODIFIER`/`SUSCEPTIBILITY`/`COOPERATING` gene relationship types
  and the `COOPERATING_HIT` allelic role — and one mechanistic reading of
  incomplete penetrance.
- **Antifungal target modules.** The ergosterol side of the highlighted BPM lands
  on modules dismech already has (`fungal_ergosterol_synthesis_inhibition`,
  `fungal_membrane_ergosterol_binding`, `antifungal_intrinsic_resistance_gating`).
  A validated aromatic-amino-acid-biosynthesis co-target would be a candidate
  future antimicrobial target module in the `projects/ANTIMICROBIAL.md` family —
  but today it is a yeast-model lead, not a curated therapy.
- **Mechanism modules generally.** A BPM module (a coherent gene set acting as one
  functional unit) is a data-driven analog of a dismech mechanism module. The
  compensation *relation between* two modules, however, has no first-class slot in
  the schema — see the gap note below.

## What dismech should and should not take from it

**Not KB content, directly.** GIDEON's 3,215 BPMs are computational predictions in
baker's yeast, most without human disease correlates. dismech's evidence policy
(PMID + exact snippet, `evidence_source` classifying the study) would grade any
BPM-derived claim as `COMPUTATIONAL` at best, and the yeast→human step is
precisely the `HUMAN_MODEL_MISMATCH` situation the discussion machinery exists
for. Nothing in this paper warrants new disorder entries or new evidence items.

**Plausible uses, in rough priority order:**

1. **Hypothesis leads for curated entries.** Where a dismech entry already carries
   a digenic/oligogenic claim or an unexplained modifier gene, a conserved yeast
   BPM containing the orthologs is legitimate supporting context for a
   `discussions` item (`kind: KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH`) with
   `proposed_experiments` — the published BPM set is browsable per gene, and the
   paper is citable (`PMID` pending indexing; DOI available now).
2. **A schema question worth recording, not solving here.** dismech can say a
   treatment *targets* a mechanism and an exposure *protects against* one, but
   cannot say mechanism/pathway A *compensates for* B — the relation underlying
   synthetic lethality, digenicity, and paralog buffering alike. Today that lives
   in prose (`description`, module `notes`). If compensatory structure recurs as
   a curation need, it belongs in the design-decision register as an open
   decision (candidate shape: an inter-node or inter-module link class with a
   `COMPENSATES_FOR` predicate, evidence-bearing like `ModelMechanismLink`),
   rather than being improvised per entry.
3. **Human genetic interaction data as a future structured source.** The Billmann
   et al. 2026 human GI map (and ASTER-style clinically oriented SL predictions)
   is the dataset to watch: if cancer entries start citing human GI screens for
   synthetic-lethality claims, a structured source or `datasets:` convention for
   GI screens would follow the existing `verify-datasets` discipline. Premature
   until a curation PR actually needs it.

**Recommendation:** file this as background reading for the synthetic-lethality
and digenic-inheritance curation areas; take no schema or KB action now. If a
curator hits the "compensates-for" expressivity wall in a real entry, that is the
trigger to open the design-register question in item 2.
