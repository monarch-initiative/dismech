---
title: Estrogen Signalling Gap Filling
status: IN_PROGRESS
description: >-
  Close the gap between how often dismech talks about estrogen and how rarely it
  binds the receptor. Twelve entries annotate the estrogen receptor signaling
  pathway on a mechanism node; one puts a receptor gene on a node.
tags: [MECHANISM_GAP, ENDOCRINE, ENDOCRINE_DISRUPTION]
diseases:
- 46_XX_Gonadal_Dysgenesis
- Aromatase_Deficiency
- Breast_Carcinoma
- Breast_Fibroadenoma
- ER_Positive_Breast_Cancer
- Endometrial_Carcinoma
- Endometrial_Endometrioid_Adenocarcinoma
- Estrogen_Resistance_Syndrome
- Heart_Failure
- Lymphangioleiomyomatosis
- Osteoporosis
- PIK3CA_Mutant_Breast_Cancer
- Premenstrual_Dysphoric_Disorder
- Skeletal_Fluorosis
- Testicular_Sex_Cord_Stromal_Neoplasm
- Triple_Negative_Breast_Cancer
modules:
- cdk46_inhibitor_resistance
- cholestatic_liver_injury
- deep_placentation_defect
- deregulated_nutrient_sensing
- osteoporosis_bone_resorption
- sex_steroid_driven_proliferation
---

# Estrogen Signalling Gap Filling

Estrogen receptor 1 is among the most heavily assayed targets in ToxCast and the
receptor the US endocrine-disruptor screening statute was written around
(the evidence for both claims is in
[Endocrine Disruptor Screening History](#endocrine-disruptor-screening-history)
below). It has almost no presence in the dismech pathograph. This project closes that gap, and
this page is the scope and worklist for it.

The measurement behind that claim is
[the coverage census](../docs/reports/estrogen-signalling-coverage-census-2026-09-29.md),
regenerated with `just estrogen-census`. The numbers below move with every
curation PR, so read the report for current figures rather than trusting a
number quoted here.

## What the census found

Six tiers over `kb/disorders/`, loosest to strictest. When the gap was first
measured, 115 entries mentioned estrogen somewhere and 57 built a
pathophysiology node around it, but only 12 bound `GO:0030520` *estrogen
receptor signaling pathway*, and exactly **one** put a receptor gene on a
pathograph node.

The gap was between those last two: the pathway was recorded and the receptor
driving it was not. That is what the ToxCast mapping needs and what this project
was mostly about. The pathograph worklist below closed it, and the node-bound
count has moved off one. Read the census report for current figures.

## Endocrine Disruptor Screening History

The opening claim of this page, that estrogen receptor 1 is among the most
heavily assayed ToxCast targets and the receptor the US screening statute was
written around, rests on five independent lines of evidence. They are worth
keeping separate because they carry different weight. Every identifier below was
confirmed against PubMed for identifier and exact title on 2026-09-29.

**The screening mandate names estrogen in the statute.** The Food Quality
Protection Act of 1996 amended the Federal Food, Drug, and Cosmetic Act to
require EPA to develop a screening program determining whether substances "may
have an effect in humans that is similar to an effect produced by a naturally
occurring estrogen" (21 U.S.C. 346a(p)(1), quoted in 80 FR 35350, 2015-06-19).
Androgen and thyroid screening entered later, through the advisory committee that
designed the program, not through the enabling text. Estrogen is the endocrine
axis the regulation was written around.

**The receptor has the deepest validated assay stack of any endocrine target.**
OECD maintains three guidelines for it: TG 455 for receptor transactivation,
TG 493 for human recombinant receptor binding, and TG 440 for the rodent
uterotrophic bioassay. Two of the three are *performance-based*, meaning the
pathway is characterised well enough that new assays can be validated against a
standard rather than adopted individually. TG 440 records that the bioassay
"originated in the 1930's and was first standardized for screening by an expert
committee in 1962", and its modern international ring trial was published across
four papers in *Environmental Health Perspectives*: phase 1 ([PMID:11564613](https://pubmed.ncbi.nlm.nih.gov/11564613/)), the
programme overview ([PMID:12948895](https://pubmed.ncbi.nlm.nih.gov/12948895/)), the phase 2 dose-response studies
([PMID:12948896](https://pubmed.ncbi.nlm.nih.gov/12948896/)) and the phase 2 coded single-dose studies ([PMID:12948897](https://pubmed.ncbi.nlm.nih.gov/12948897/)). A
fifth paper covers the dietary phytoestrogen confound ([PMID:12948898](https://pubmed.ncbi.nlm.nih.gov/12948898/)).

**ToxCast built its first pathway model on this receptor, and it is the only
endocrine target where high-throughput data replaced a guideline animal study.**
Judson and colleagues integrated 18 in vitro assays spanning receptor binding,
dimerisation, chromatin binding, transactivation and receptor-dependent
proliferation into a single pathway model ([PMID:26272952](https://pubmed.ncbi.nlm.nih.gov/26272952/)), closing with the
observation that the approach "is generalizable to any molecular pathway" — the
estrogen receptor was the proving ground. Browne and colleagues then reported
that "EPA is accepting ToxCast ER model data for 1812 chemicals as alternatives
for EDSP Tier 1 ER binding, ER transactivation, and uterotrophic assays"
([PMID:26066997](https://pubmed.ncbi.nlm.nih.gov/26066997/); cite alongside its correction, [PMID:28767231](https://pubmed.ncbi.nlm.nih.gov/28767231/)). The androgen
receptor model that followed used 11 assays ([PMID:27933809](https://pubmed.ncbi.nlm.nih.gov/27933809/)). Assay-minimisation
work ran in the same order, estrogen in 2017 ([PMID:28993267](https://pubmed.ncbi.nlm.nih.gov/28993267/)) and androgen in 2020
([PMID:32798611](https://pubmed.ncbi.nlm.nih.gov/32798611/)).

**The modelling consortia ran estrogen first and named the successor after it.**
CERAPP pooled 17 groups across the US and Europe, 48 models, and screened 32,464
structures against a training set drawn from the ToxCast data ([PMID:26908244](https://pubmed.ncbi.nlm.nih.gov/26908244/)).
CoMPARA applied the same methodology to the androgen receptor four years later
([PMID:32074470](https://pubmed.ncbi.nlm.nih.gov/32074470/)). No comparable consortium exists for any other endocrine
receptor.

**The receptor dominates the mechanistic pathway literature.** In the AOP-Wiki
snapshot of 2026-09-15, 26 of 597 Adverse Outcome Pathways declare an
estrogen-receptor-related molecular initiating event, drawn from 8 distinct key
events — more than the androgen receptor (16) or the aryl hydrocarbon receptor
(23), and comparable to the whole thyroid axis (25) despite that axis spanning
seven target proteins. This is cited as evidence of how heavily the receptor has
been studied. **Mapping those pathways onto dismech entries is not in this
project's scope**, and is tracked separately alongside the ToxCast work in #12858
and #12682.

The historical reason for all of this is chemical promiscuity rather than
regulatory accident. The founding xenoestrogen observations were incidental
contamination findings — nonylphenol leaching from modified polystyrene
([PMID:1935846](https://pubmed.ncbi.nlm.nih.gov/1935846/)) and bisphenol A from autoclaved polycarbonate ([PMID:8504731](https://pubmed.ncbi.nlm.nih.gov/8504731/)) — and
Katzenellenbogen set out the underlying argument the same decade in "The
structural pervasiveness of estrogenic activity" ([PMID:8593885](https://pubmed.ncbi.nlm.nih.gov/8593885/)): the receptor's
ligand tolerance is broad enough that structurally unrelated industrial chemicals
hit it. Shanle and Xu's review of endocrine disrupting chemicals targeting this
signalling pathway is the best single entry point ([PMID:21053929](https://pubmed.ncbi.nlm.nih.gov/21053929/)).

### Two things not to claim

- **These AOPs are not the most OECD-endorsed — they are the least.** None of the
  26 carries WPHA/WNT endorsement; the endorsed endocrine set is androgen
  receptor, aromatase, thyroperoxidase, deiodinase and sodium-iodide symporter.
  The strongest estrogen pathways sit at *Under Review*. "Most studied" and "most
  formally endorsed" point in opposite directions here.
- **The 40-endpoint figure for ESR1 is ours, not the literature's.** It is
  computed from the ToxCast assay annotation table. Present it as a derived count
  with the invitrodb version stated, never as a citation. No published source
  ranks ToxCast targets by endpoint count; the citable within-programme
  comparison is 18 assays in the estrogen model against 11 in the androgen model.

## Scope

In scope:

- Binding ESR1 or ESR2 on the pathophysiology nodes that already carry
  `GO:0030520`, where the literature supports it.
- Wiring the receptor into the pathograph for entries that bind it in `genetic:`
  only.
- Curating estrogen resistance syndrome (MONDO:0014148), the one disease where
  the receptor sits on a mechanism node by definition. Curated as
  Estrogen_Resistance_Syndrome; its stub was added and retired in the same PR.
- Deciding whether estrogen receptor signalling needs its own mechanism module.
  This is the one item still open; everything above it is worked.

Not in scope, and deliberately left to the issues that already own them: the
estrogen-adjacent findings listed under *Related issues* below.

## The pathograph worklist

Each row is a research task, not a mechanical backfill. A `genes:` descriptor
asserts that this receptor drives this mechanism in this disease, so each one
needs a source read at the time of writing and an evidence item quoting it.

Three traps apply throughout:

- **A gene binding only has to be self-consistent to validate.** `just
  validate-terms` checks that a `term.label` is HGNC's canonical label for the
  CURIE; it does not check that the gene is the one the node means. ESR1
  (`hgnc:3467`) and ESR2 (`hgnc:3468`) are paralogues with different tissue
  distributions, so the wrong one passes every gate while making a false claim.
  Run `just list-gene-term-mismatches` on each changed file.
- **The direction of the claim has to match.** A receptor-activation node and a
  loss-of-signalling node are opposite claims about the same gene. Evidence for
  one does not support the other.
- **A node that should stay unbound is a finished task,** provided `notes`
  records the search actually run and what it returned.

### Nodes binding the pathway with no gene

All twelve rows are worked. Six took a receptor binding and six are recorded
declines; each decline carries its reason and the searches run in the node's
`notes`.

| Entry | Node | Outcome | PR |
| --- | --- | --- | --- |
| ER_Positive_Breast_Cancer | ESR1 Mutation-Driven Endocrine Resistance | ESR1 bound | #13116 |
| ER_Positive_Breast_Cancer | Estrogen Receptor Activation | ESR1 bound | #13116 |
| Breast_Carcinoma | ER and HER2 Receptor Heterogeneity | declined, three receptors would belong equally | #13128 |
| Breast_Fibroadenoma | Dysregulated Stromal Estrogen Signaling and ECM Organization | declined, MED12 is the causal gene | #13128 |
| PIK3CA_Mutant_Breast_Cancer | Endocrine Resistance | declined, PIK3CA acts on the receptor | #13128 |
| Triple_Negative_Breast_Cancer | Loss of Hormone Receptor Signaling | declined, the receptor is not expressed | #13128 |
| Endometrial_Carcinoma | Unopposed Estrogen Signaling | ESR1 bound | #13132 |
| Endometrial_Endometrioid_Adenocarcinoma | Unopposed Estrogen Signaling | ESR1 bound | #13132 |
| Aromatase_Deficiency | Estrogen Deficiency and Androgen Excess | declined, ligand-supply defect | #13151 |
| Heart_Failure | Loss of Myocardial Oestrogen Receptor Signalling | ESR1 and ESR2 bound | #13151 |
| Lymphangioleiomyomatosis | Estrogen-Driven LAM Cell Survival and Dissemination | ESR1 bound | #13151 |
| Testicular_Sex_Cord_Stromal_Neoplasm | Estrogen-Mediated Clinical Manifestations | declined, ligand excess on two unlocalized tissues | #13151 |

The `46_XX_Gonadal_Dysgenesis` row the issue also listed was not gene-less: it
already carried `genes: PSMC3IP`, and that correction is recorded in #13132.

The six declines are exactly the six rows the census still reports as binding
the pathway with no receptor gene on any node. That table is a record of
decisions taken, not of work outstanding.

### Bound in `genetic:` only

Five entries bound ESR1 without the gene reaching any mechanism node, and all
five are now dispositioned.

| Entry | Outcome | PR |
| --- | --- | --- |
| ER_Positive_Breast_Cancer | wired by the receptor bindings above | #13116 |
| Breast_Carcinoma | not wired; the pathophysiology models dissemination and carries no hormone-driven node | #13128 |
| Osteoporosis | ESR1 wired on RANKL/OPG Dysregulation | #13159 |
| Premenstrual_Dysphoric_Disorder | not wired; a preliminary intron-4 association, and the target node binds the generic steroid pathway | #13159 |
| Skeletal_Fluorosis | not wired; a single unreplicated protective allele and no estrogen-dependent mechanism in the entry | #13159 |

A genotype-association paper does not by itself support a causal edge, so
three of the five stop at a recorded reason rather than an edge. That was the
expected outcome for this half of the worklist.

### Already on the pathograph

46_XX_Gonadal_Dysgenesis was the single entry binding a receptor gene on a
pathophysiology node, via ESR2, when this project started. It was the pattern
the rest of the worklist was trying to reach, and it is no longer alone.

## Modules

Six modules mention estrogen or the receptor. **None binds either gene.** Only
sex_steroid_driven_proliferation binds `GO:0030520`.

| Module | Mention is | Binds `GO:0030520` |
| --- | --- | --- |
| sex_steroid_driven_proliferation | core to the module's mechanism | yes |
| cdk46_inhibitor_resistance | core to the module's mechanism | no |
| osteoporosis_bone_resorption | core to the module's mechanism | no |
| cholestatic_liver_injury | incidental | no |
| deregulated_nutrient_sensing | incidental | no |
| deep_placentation_defect | only in quoted source metadata | no |

Issue #12925 names the first two and deep_placentation_defect. The census finds
three more. Two of those, cholestatic_liver_injury and
deregulated_nutrient_sensing, are incidental mentions and are listed here only
so a later reader does not have to re-derive that they were considered.
deep_placentation_defect names ESR1 only inside a `reference_title` and a quoted
`snippet`, so the module cites a paper about the receptor rather than modelling
it.

osteoporosis_bone_resorption is the one worth attention. It treats estrogen
withdrawal as a named upstream driver across several nodes, and it is a
non-proliferative bone mechanism, which is exactly the territory the open module
question below asks about.

## Open question: does estrogen receptor signalling need its own module?

Undecided, and this project should not pre-empt it.
sex_steroid_driven_proliferation is the nearest existing module, but it is
scoped to proliferation of a hormone-responsive tissue and tagged `ONCOLOGY`.
The non-proliferative mechanisms in the corpus — myocardial signalling in
Heart_Failure, bone in Osteoporosis, the CNS mechanisms in
Premenstrual_Dysphoric_Disorder — sit outside that scope.

The census adds one fact the question was framed without: bone already has a
module home in osteoporosis_bone_resorption, which models estrogen withdrawal
without binding the receptor. Whether that argues for a new module, for widening
an existing one, or for neither is a curation call to make after the worklist
above has been worked, since that is what shows whether these mechanisms cluster
or are one-offs.

**The worklist is now worked, so the question is answerable.** What it produced:
three non-proliferative receptor bindings in different tissues (myocardium in
Heart_Failure, bone lining cells in Osteoporosis, and the systemic
loss-of-signalling state in Estrogen_Resistance_Syndrome), against four
proliferative ones that already have `sex_steroid_driven_proliferation` as a
home. **Decided: no estrogen receptor signalling module in dismech.** Three tissues
and one monogenic receptor disease do not cluster tightly enough to earn one.
Below the shared node the three diverge immediately - to profibrotic effectors in
`Heart_Failure`, to RANKL/OPG dysregulation in `Osteoporosis`, and to six
target-tissue arms in `Estrogen_Resistance_Syndrome` - so what they have in
common is a single node and nothing after it. A module here earns its place by
saving conforming entries from duplicating a shared chain, and one node is
thinner than that. `Estrogen_Resistance_Syndrome` could not conform in any case,
because the existing module's chain is sustained signalling driving mitosis and
that disease is loss of signalling.

The receptor-keyed view is real, but its home is elsewhere. dismech organises on
the disease, and its modules on the outcome; the receptor is the axis ToxCast
assays and AOP initiating events are keyed on. That view is now tracked as
[EnviroMech issue #3](https://github.com/monarch-initiative/enviromech/issues/3),
where the fan-out across tissues is the object of interest rather than a reason
the cluster is too thin.

`sex_steroid_driven_proliferation#Nuclear Steroid Receptor Hyperactivation`
accordingly keeps no receptor gene, and its node `notes` now records why: the
receptor is the substitution a conforming entry makes, so naming one would fix
the choice the module leaves open.

## Related issues

Cross-referenced, not absorbed. Each is its own issue and none overlaps the
pathograph work above.

| Issue | Subject |
| --- | --- |
| #6338 | Sex-hormone modulation of dopaminergic mechanisms in Parkinson disease |
| #5848 | Endometriosis / adenomyosis divergence |
| #6190 | The same source paper, a second scan hit |
| #7365 | PCOS insulin resistance |
| #7038 | PCOS mitophagy |
| #11705 | `NCIT:C15599`, a menopause-scoped hormone replacement term used by 46 entries for growth hormone, thyroid and adrenal replacement |

Issue #11705 has a direct consequence for any treatment this project adds: use
`NCIT:C15986` Pharmacotherapy with a `therapeutic_agent`, or `NCIT:C15445` where
the axis is unspecified. Do not reintroduce the menopause-scoped `NCIT:C15599`
for a non-menopausal indication.

## Related project pages

This project **cross-references** the estrogen mentions already in other project
pages and supersedes none of them. Each is tracking something other than
estrogen signalling.

- `CHRONIC.md` carries one table row for Endometriosis whose mechanism column
  reads "Ectopic endometrium, estrogen dependence". That is a chronic-disease
  tracking row, not receptor curation.
- `GWAS_MECHANISMS.md` names Oestradiol once, as one of 28 UK Biobank serum
  biomarkers. That is the hormone as a GWAS trait, not the receptor. Issue
  #12925 describes this as an estrogen mention, which it is, but it is the
  ligand rather than anything this project curates.
- `REACTOME_DISEASES.md` carries an unchecked box for "estrogen-receptor
  positive breast cancer (DOID:0060075)". ER_Positive_Breast_Cancer is curated
  in dismech and is the first entry on this project's worklist. Whether that box
  is therefore checkable depends on what Reactome coverage means in that
  project, which is its owner's call, not this one's.

## Regenerating the census

```bash
just estrogen-census                   # markdown to stdout
just estrogen-census --format tsv      # one row per entry
just estrogen-census --out docs/reports/estrogen-signalling-coverage-census-<date>.md
```

The script reads only committed YAML. It is offline, report-only, and exits 0.
