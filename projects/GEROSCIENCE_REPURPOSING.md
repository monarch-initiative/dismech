---
title: 'Geroscience Repurposing: FDA-Approved Drugs Against the Hallmarks of Aging'
status: IN_PROGRESS
description: Curating the nine FDA-approved candidate gerotherapeutics prioritized by Kulkarni et al. 2022 into the hallmark-of-aging mechanism modules, so that "drug X targets hallmark Y" is a queryable treatment link rather than a claim in a review table.
modules:
- cellular_senescence
- deregulated_nutrient_sensing
- disabled_macroautophagy
- epigenetic_alterations
- genomic_instability_aging
- gut_dysbiosis
- inflammaging
- loss_of_proteostasis
- mitochondrial_dysfunction
- stem_cell_exhaustion
- telomere_attrition
---

# Geroscience Repurposing: FDA-Approved Drugs Against the Hallmarks of Aging

## Overview

Geroscience holds that biological aging is the dominant modifiable risk factor
for the major chronic diseases, and that targeting it should delay several of
them at once. A drug that does this is a *gerotherapeutic*. The practical
question is which of the drugs we already have is the best candidate to test,
and that question has an answer with a method behind it: Kulkarni, Aleksic,
Berger, Sierra, Kuchel and Barzilai, [Geroscience-guided repurposing of
FDA-approved drugs to target aging](https://pubmed.ncbi.nlm.nih.gov/35343051/)
(*Aging Cell* 2022, `PMID:35343051`), screened DrugAge for compounds that
significantly extend rodent lifespan, kept only the FDA-approved ones, and
scored the survivors on a 12-point scale.

This project brings that result into dismech. The KB already has the hallmarks
of aging as mechanism modules under `kb/modules/`. What it largely lacked was
the drug side: as of the start of this project, **9 of 13 aging-related modules
carried no `treatments` at all**, so a query like "what pharmacologic
interventions act on inflammaging?" returned nothing, even though the answer is
well documented.

The unit of work here is a **treatment with `target_mechanisms`** on an aging
module — a specific drug asserted to act on a specific hallmark node, with an
effect direction and cited, snippet-verified evidence. That turns a review
table's tick mark into something the pathograph can draw and a query can reach.

## Why the review's own scoring is recorded but not curated as evidence

The 12-point score is a *prioritization*, not a mechanistic claim, and it is a
snapshot: the authors themselves note that "future studies may change the
priority order for drugs that did not receive points due to the paucity of
clinical data." Several drugs score 0 on human endpoints because nobody has run
the trial at the right dose in the right population — not because the trial was
run and was negative. Aspirin is the clearest case: the animal work uses
anti-inflammatory doses, while every large human trial used antiplatelet doses,
which the authors argue is the wrong comparison rather than a refutation.

So the ranking lives in this project file and in module treatment
`description` prose. **Evidence items cite the primary studies**, which is where
the mechanism claims actually are. Citing the review for a mechanism it merely
tabulates would put a secondary source where a primary one belongs.

## The scoring framework

An ordinal 12-point scale, split evenly so that a drug with a strong basic
rationale but no human data is not penalized for the gap:

| Half | Component | Points |
|---|---|---|
| Preclinical (6) | Hallmarks of aging attenuated | 2 if ≥3 hallmarks, 1 if <3 |
| | Preclinical healthspan / age-related disease | 2 |
| | Preclinical lifespan | 2 if significant in the NIA Interventions Testing Program, 1 if outside it |
| Clinical (6) | Healthspan: targets an age-related disease that is *not* the drug's indication | 3 if RCT, 1 if observational |
| | Mortality: reduces all-cause or off-target-disease death | 3 if RCT, 1 if observational |

The ITP distinction matters and is worth preserving in curation prose. The
Interventions Testing Program uses genetically heterogeneous UM-HET3 mice,
replicated across three sites, and is the reason a lifespan claim from it
outranks a single-lab result.

## The ranking

| Rank | Drug / class | Hallmarks | Preclin. healthspan | Preclin. lifespan | Human healthspan | Human mortality | Score |
|---|---|---|---|---|---|---|---|
| 1 | SGLT2 inhibitors | 2 | 2 | 2 | 3 | 3 | **12** |
| 2 | Metformin | 2 | 2 | 1 | 3 | 3 | **11** |
| 3= | Acarbose | 2 | 2 | 2 | 3 | 0 (not assessed) | **9** |
| 3= | Rapamycin / rapalogs | 2 | 2 | 2 | 3 | 0 (not assessed) | **9** |
| 3= | Methylene blue | 2 | 2 | 2 | 3 | 0 (not assessed) | **9** |
| 6 | ACE inhibitors / ARBs | 2 | 2 | 1 | 3 | 0 | **8** |
| 7 | Dasatinib + quercetin (senolytics) | 2 | 2 | 1 | 1 | 0 (not assessed) | **6** |
| 8 | Aspirin | 2 | 2 | 2 | 0 (not assessed) | 0 (not assessed) | **6** |
| 9 | N-acetyl cysteine | 1 | 2 | 2 | 0 (not assessed) | 0 (not assessed) | **5** |

Note the difference between the two zeros. ACEi/ARB scores 0 on mortality
because the studies exist and were **predominantly negative**; acarbose,
rapamycin, methylene blue, senolytics, aspirin and NAC score 0 because the
question was **not assessed**. Only the first is evidence against.

## Drug × module matrix

Which hallmark modules each candidate has a documented mechanistic claim
against, mapped onto `kb/modules/`. `✓` = curated as a treatment with
`target_mechanisms`; `·` = claim documented in the source literature, not yet
curated; blank = no applicable studies found.

| Module | SGLT2i | Metformin | Acarbose | Rapamycin | Methylene blue | ACEi/ARB | D+Q | Aspirin | NAC |
|---|---|---|---|---|---|---|---|---|---|
| `deregulated_nutrient_sensing` | · | ✓ | · | ✓ | | | · | · | |
| `disabled_macroautophagy` | ✓ | ✓ | | · | | · | | ✓ | |
| `inflammaging` | | ✓ | · | · | | · | ✓ | · | |
| `mitochondrial_dysfunction` | · | ✓ | | | ✓ | | · | | · |
| `gut_dysbiosis` | | ✓ | ✓ | | | | · | · | |
| `cellular_senescence` | | · | | · | · | | ✓ | · | |
| `stem_cell_exhaustion` | | ✓ | | · | | | | | |
| `genomic_instability_aging` | | · | | · | | | · | · | |
| `epigenetic_alterations` | | | · | | | | | · | |
| `loss_of_proteostasis` | | · | · | · | · | | | | |
| `telomere_attrition` | | · | | | | | | | |

The empty cells are informative and should not be filled in speculatively. The
review records "No applicable studies" for many drug × hallmark pairs — SGLT2
inhibitors and methylene blue against epigenetics and stem-cell renewal, ACEi
and NAC against most hallmarks — and the newer or less-studied agents are
simply thinner than metformin and rapamycin, not proven inactive there.

## Curation status

- [x] Survey aging-module treatment coverage (9 of 13 modules had none)
- [x] `inflammaging` — metformin, senolytics (D+Q)
- [x] `gut_dysbiosis` — metformin, acarbose
- [x] `disabled_macroautophagy` — aspirin, metformin, SGLT2 inhibition
- [x] `mitochondrial_dysfunction` — methylene blue, metformin
- [x] `stem_cell_exhaustion` — metformin preconditioning
- [ ] `genomic_instability_aging` — rapamycin (Werner fibroblasts), aspirin (UVB DNA damage)
- [ ] `epigenetic_alterations` — acarbose (PDX-1 methylation), aspirin (colonic hypermethylation)
- [ ] `loss_of_proteostasis` — rapamycin, metformin (UPR via AMPK/ERK1/2)
- [ ] `cellular_senescence` — extend beyond D+Q to metformin, rapamycin, methylene blue senomorphic effects
- [ ] `telomere_attrition` — metformin; thin evidence, may stay uncurated
- [ ] `deregulated_nutrient_sensing` — add acarbose (insulin/IGF-1) and SGLT2i (AMP/ATP ratio, mTORC1)
- [ ] Consider a `Gerotherapeutics` grouping over modules carrying these treatments

## Curation notes

**Effect direction is where the honesty lives.** `MODULATES` is the right value
more often than it is comfortable. Methylene blue improves mitochondrial
respiration but its effect on reactive oxygen species runs in *opposite*
directions depending on the substrate, so its link to
`Bioenergetic Decline and Oxidative Stress` is `MODULATES`, and the entry
carries a second evidence item quoting the unfavorable half of the result.
Curating it as `RESTORES` with only the favorable quote would have been
schema-valid and wrong.

**`directness: INDIRECT` is the tool for the lifespan-to-mechanism leap.** That
canagliflozin extends median male lifespan by 14% does not show the benefit runs
through autophagy. The lifespan result belongs in the entry — it is why the drug
is worth curating at all — but as `INDIRECT` support, not as evidence for the
mechanism link.

**Watch `evidence_source` on human-cell studies.** Much of the strongest
metformin evidence comes from human T cells or adipose explants treated *ex
vivo*. That is `IN_VITRO`, not `HUMAN_CLINICAL`, however human the donor. Xu et
al. 2018 needs splitting into two items for this reason: the human-explant
senolytic result is `IN_VITRO`, the mouse survival result `MODEL_ORGANISM`.

**Sex dimorphism is a real finding, not a caveat to drop.** Acarbose extends
median male lifespan by 16–17% and female by 4–5%; canagliflozin extends male
lifespan and not female at all. Where the source reports it, keep it in the
evidence `explanation`.

**One drug legitimately appears against several modules.** Metformin is curated
against inflammaging, macroautophagy, mitochondrial dysfunction, gut dysbiosis
and stem-cell exhaustion. This is not duplication: Bharath et al. found the
autophagic and mitochondrial actions run "largely in parallel" rather than one
through the other, so they are separate mechanistic claims that happen to share
a drug.

## Open questions

- **Should there be a gerotherapeutic module?** The candidates share a target
  (aging) but not a mechanism, and a module is a conserved *pathological
  process*, not a drug class. A `Grouping` over the hallmark modules is the
  better fit; recorded as a checklist item above rather than assumed.
- **ACEi/ARB is the awkward case.** It scores 8, but its renoprotection is
  explained by hemodynamics rather than by gerotherapeutic action — the review
  says so explicitly. Curating it against an aging hallmark on the strength of
  its score would overstate the evidence.
- **RTB101 / dactolisib** was excluded from the ranking for not being
  FDA-approved, despite phase 2b/3 respiratory-infection results in older
  adults. If it is ever curated, the exclusion reason should be recorded so it
  is not mistaken for a negative result.

## Sources

- Kulkarni AS, Aleksic S, Berger DM, Sierra F, Kuchel GA, Barzilai N.
  Geroscience-guided repurposing of FDA-approved drugs to target aging: A
  proposed process and prioritization. *Aging Cell*. 2022;21(4):e13596.
  `PMID:35343051`, [doi:10.1111/acel.13596](https://doi.org/10.1111/acel.13596).
- Primary studies are cited per-claim in the module `evidence` blocks; see
  `git log` on `kb/modules/` and the history records under
  `history/modules/` for the per-session curation record.
