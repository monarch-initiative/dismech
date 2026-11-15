---
title: IMPC Knockouts and Disease Mechanism
status: IN_PROGRESS
description: >-
  Can International Mouse Phenotyping Consortium knockouts illuminate the
  mechanisms of Mendelian and complex diseases? A corpus-wide comparison of
  IMPC phenotype calls with dismech gene-disease pairs, phenotypes and
  pathophysiology nodes.
tags:
- models
- animal-models
- mouse
- impc
- mammalian-phenotype
diseases:
- Hermansky_Pudlak_Syndrome
- Griscelli_Syndrome_Type_1
- Chediak-Higashi_Syndrome
- Gray_Platelet_Syndrome
- Sitosterolemia
- X-Linked_Hypophosphatemia
- Hypertrophic_Cardiomyopathy_4
- Alport_Syndrome
- Diamond-Blackfan_Anemia
---

# IMPC Knockouts and Disease Mechanism

**Bottom line:** IMPC knockouts are good at saying a disease gene matters, and
in which broad body system, but they rarely reach the mechanism a dismech
entry describes. Across 3,625 germline causative gene-disease pairs, 52% have
at least one significant IMPC call. For those, the mouse hits 30% of the organ
systems the human entry's phenotypes touch, against 22% for a randomly chosen
IMPC gene, so concordance is real but modest. In only 48 pairs (3%) does an
IMPC call name a cell type or process that one of the entry's own
pathophysiology nodes binds, and nearly all of those are blood-cell,
platelet, immune or pigmentation disorders, which are the places the IMPC
pipeline measures cells. For susceptibility, risk and modifier genes
(the complex-disease case) the excess over random is smaller still: 0.28
against 0.24. The gene-function half of this question, what knockouts say
about molecular and cellular function at all, is in the companion
[ai-gene-review `projects/IMPC.md`](https://github.com/ai4curation/ai-gene-review/blob/main/projects/IMPC.md);
its main result explains this one: no IMPC call is defined on a molecular
function, and its cellular calls are almost all blood counts.

## Question

Can IMPC knockouts elucidate the mechanisms of disease, either Mendelian or
otherwise? We split this into three things a knockout could contribute to a
dismech entry:

1. **Coverage.** Has the mouse ortholog been phenotyped, and in a genotype
   relevant to the human disease (heterozygotes for a dominant disease)?
2. **Phenotype concordance.** Does the knockout reproduce the organ systems the
   human disease affects, more than an arbitrary knockout would?
3. **Mechanism contact.** Does any IMPC call land on a cell type or biological
   process that the entry's pathophysiology graph names?

## Method

[`IMPC/impc_disease_concordance.py`](IMPC/impc_disease_concordance.py) walks
every `kb/disorders/` entry and takes each germline `genetic:` row bound to an
`hgnc:` gene (`CAUSATIVE`, or `SUSCEPTIBILITY` / `RISK_FACTOR` / `MODIFIER`).
It maps the human symbol to the mouse gene through IMPC's own gene table and
joins the IMPC significant calls (fetched 2026-11-15, 67,350 calls on 8,429
genes).

- **Systems.** Each HPO phenotype is lifted to its organ-system class (children
  of `HP:0000118`, HP 2026-09-01) and compared with the IMPC top-level MP
  categories through the hand-curated
  [`IMPC/hp_mp_system_map.yaml`](IMPC/hp_mp_system_map.yaml). Systems IMPC
  cannot test (neoplasm, breast, voice, constitutional, cellular) are dropped
  from the denominator. Recall is the share of the entry's testable systems the
  mouse hits; the baseline is the mean recall of 300 random IMPC genes against
  the same entry.
- **Mechanism contact.** Each IMPC call's MP term is expanded to the CL, GO and
  UBERON terms named in its OWL logical definition (MP 2026-10-29). A pair has
  contact when a CL term matches a `cell_types` binding exactly, or a GO term is
  a `biological_processes` binding or one of its ancestors (GO 2026-07-26).

Per-pair results are in [`IMPC/results/pairs.tsv`](IMPC/results/pairs.tsv);
the generated report is [`IMPC/results/CONCORDANCE.md`](IMPC/results/CONCORDANCE.md).

## Results

| | Causative | Susceptibility / risk / modifier |
|---|---:|---:|
| Gene-disease pairs | 3,625 | 812 |
| Mouse ortholog in IMPC's gene table | 3,537 (98%) | 769 (95%) |
| Phenotyped by IMPC | 2,045 (56%) | 407 (50%) |
| At least one significant call | 1,888 (52%) | 370 (46%) |
| ...including a lethality call | 1,034 (55%) | 114 (31%) |
| Mean organ-system recall | 0.30 | 0.28 |
| Mean recall of random IMPC genes | 0.22 | 0.24 |
| Pairs above their random baseline | 1,027 (54%) | 185 (50%) |
| Mechanism contact (CL or GO shared with a node) | 48 (3%) | 13 (4%) |

**Half the Mendelian disease genes have no IMPC data.** 1,580 causative pairs
have a mouse ortholog that IMPC has not phenotyped. Diamond-Blackfan anaemia is
an example: of its 15 genes, only *Rps26* has been phenotyped, and its calls
(behaviour and hearing) miss the blood entirely.

**Lethality is the most common thing IMPC says about a disease gene.** 55% of
causative pairs with any call include a lethality call. That is informative
about essentiality, but it also means the adult screen ran on heterozygotes or
did not run, so the phenotypes a viable human patient has are often never
tested in the null mouse.

**Genotype matters and is often mismatched.** For autosomal-dominant pairs
with a call, 54% have at least one heterozygote call; the rest are homozygous
nulls standing in for a heterozygous human genotype.

**System concordance is only modestly above chance.** The median pair beats its
random baseline by 0.03. A gene with many calls overlaps almost any phenotype
profile, which is why a baseline is needed at all. Alport syndrome shows the
spread: *Col4a5* and *Col4a3* knockouts hit renal and eye phenotypes (recall
0.6), while *Col4a4* reaches only the eye (0.2).

**Recorded loss of function does not raise concordance.** Pairs whose
pathophysiology node records `LOSS_OF_FUNCTION` or `PARTIAL_LOSS_OF_FUNCTION`
reach 0.28 against a 0.22 baseline; gain-of-function, dominant-negative,
neomorphic and hypermorphic pairs reach 0.29 against 0.21. A knockout should
model a loss-of-function disease better, so the absence of a difference says
the system-level measure is too coarse to see it, not that the biology does not
matter. Only 781 of the 3,625 causative pairs record an impact at all, 22 of
them `UNKNOWN`.

**Mechanism contact clusters where IMPC counts cells.** The 48 causative
contacts are mostly platelet (`CL:0000233`, 10 pairs), erythrocyte
(`CL:0000232`, 8), monocyte and neutrophil, T, B and NK cell subsets, and melanosome
organization (`GO:0032438`, 8 pairs) or transport. The disorders are what that
predicts: Hermansky-Pudlak syndrome (five genes), Griscelli syndrome types 1
and 2, Chédiak-Higashi syndrome, gray platelet syndrome, ETV6- and
MPIG6B-related thrombocytopenias, hereditary spherocytosis, CARD11, CD28 and
BACH2 immunodeficiencies, and sitosterolemia (red-cell and platelet indices).
Outside blood and pigment the contacts are single organ processes: cardiac
muscle contraction for ALPK3 and MYBPC3 cardiomyopathies, bone mineralization
for X-linked hypophosphatemia, heart looping for TBX20.

## Answer, as far as it goes

- **Mendelian disease: a phenotype check, rarely a mechanism.** An IMPC
  knockout can confirm that loss of the gene disturbs the right system and
  stage, and for blood, immune and pigmentation disorders it can reach the
  affected cell. It cannot place the gene's product in a pathophysiology node:
  that needs the molecular and cellular readouts IMPC does not make.
- **Complex disease: weaker still.** Susceptibility and risk genes are null
  knocked out, where the human effect is usually a small change in dosage or
  regulation, and system concordance is barely above random.
- **Where it is most useful for dismech:** an `animal_models` record with
  `modeled_mechanisms` that `RECAPITULATES` or `PARTIALLY_RECAPITULATES` an
  organ-level node, with `model_scale` stated honestly (usually `ORGANISM` or
  `TISSUE`) and a `limitations` note on zygosity and allele type. A clear
  discordance (a null mouse that misses the defining human system) is a
  candidate `FAILS_TO_RECAPITULATE` link or a `HUMAN_MODEL_MISMATCH`
  discussion, but only once the line was actually tested for that system: an
  IMPC "no call" is not a negative result if the relevant procedure was not
  run.

## Caveats

- CL matching is exact, without the CL hierarchy, so contact is undercounted
  where a node binds a parent or child of the IMPC cell type.
- The system map is coarse by design; a phenotype-level comparison (MP to HP
  through uPheno) would be sharper and is planned.
- Gene mapping uses IMPC's human-symbol field; 1:many orthologs are pooled.
- dismech phenotype lists are curated from human literature and are uneven
  across entries, which affects recall in both directions.
- IMPC is predominantly C57BL/6N, early adult, and null alleles; the analysis
  says nothing about knock-in models of patient variants.

## How this relates to existing projects

- [`COMMONFUND/KOMP2.md`](COMMONFUND/KOMP2.md) proposed a ten-gene IMPC
  concordance pass and a `komp2.py` helper. This project runs that comparison
  corpus-wide and supplies the worklist (`pairs.tsv`). Its evidence wording
  still describes IMPC evidence as `PARTIAL`, a `supports` value that has been
  retired; the right encoding is `SUPPORT` with `evidence_source:
  MODEL_ORGANISM` and, where the inference is indirect, `directness: INDIRECT`.
- [`MODEL_ORGANISM_ASSAYS.md`](MODEL_ORGANISM_ASSAYS.md) is designing the
  readout slots (IMPReSS parameter, MP result term) an IMPC call would land in.
  Its phase 3 depends on this project's calls.

## Plan

- [x] Corpus-wide coverage, system concordance and mechanism-contact pass.
- [ ] Replace exact CL matching with CL closure, and the system map with
      MP-to-HP phenotype matching, and rerun.
- [ ] Separate "not tested" from "tested, no call" per system, using IMPC
      statistical-result data, so discordances can be read as negative
      evidence.
- [ ] Decide how an IMPC call is cited. IMPC gene pages have no PMID, so an
      evidence item cannot quote one today. The structured-source framework
      (`src/dismech/structured_sources/`) could pre-cache one quotable record
      per gene, as it does for `ORPHA:` and `CGGV:`; that needs a design
      decision before any KB entry cites IMPC data.
- [ ] Pilot on the 48 mechanism-contact pairs: add or extend `animal_models`
      records with `modeled_mechanisms`, `model_scale` and `limitations`, once
      the citation question is settled.
- [ ] For complex-disease genes, compare with GWAS effect direction where
      dismech records one, and with heterozygote calls only.

## Reproduce

Raw downloads go to the git-ignored `.cache/impc/`.

```bash
uv run python projects/IMPC/fetch_impc.py
curl -sSL -o .cache/impc/mp.owl https://purl.obolibrary.org/obo/mp.owl
curl -sSL -o .cache/impc/go-basic.obo https://purl.obolibrary.org/obo/go/go-basic.obo
curl -sSL -o .cache/impc/hp.obo https://purl.obolibrary.org/obo/hp.obo
uv run python projects/IMPC/impc_disease_concordance.py
```

## Key literature

Titles verified against PubMed; background only, not used as KB evidence.

- PMID:28650483 Meehan TF et al. 2017. Disease model discovery from 3,328 gene
  knockouts by The International Mouse Phenotyping Consortium.
- PMID:32005800 Cacheiro P et al. 2020. Human and mouse essentiality screens as
  a resource for disease gene discovery.
- PMID:36305825 Groza T et al. 2023. The International Mouse Phenotyping
  Consortium: comprehensive knockout phenotyping underpinning the study of
  human disease.
- PMID:37160609 da Silva-Buttkus P et al. 2023. Knockout mouse models as a
  resource for the study of rare diseases.
- PMID:27626380 Dickinson ME et al. 2016. High-throughput discovery of novel
  developmental phenotypes.
