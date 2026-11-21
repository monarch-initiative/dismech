---
title: IMPC Knockouts and Disease Mechanism
status: IN_PROGRESS
description: >-
  Can International Mouse Phenotyping Consortium knockouts illuminate the
  mechanisms of Mendelian and complex diseases? A corpus-wide comparison of
  IMPC phenotype calls with dismech gene-disease pairs, phenotypes and
  pathophysiology nodes, an IMPC: reference source, and a pilot of
  IMPC-backed animal models.
tags:
- models
- animal-models
- mouse
- impc
- mammalian-phenotype
diseases:
- Hermansky_Pudlak_Syndrome
- Griscelli_Syndrome_Type_2
- Chediak-Higashi_Syndrome
- Oculocutaneous_Albinism
- Gray_Platelet_Syndrome
- Hyper-IgM_Syndrome_Type_2
- Sitosterolemia
- X-Linked_Hypophosphatemia
- Autosomal_Recessive_Hypophosphatemic_Rickets_1
- Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency
- Myeloperoxidase_Deficiency
- Pyrimidine_5_Nucleotidase_Deficiency
- Alport_Syndrome
- Diamond-Blackfan_Anemia
---

# IMPC Knockouts and Disease Mechanism

**Bottom line:** IMPC knockouts say a disease gene matters, and in which broad
body system, but they rarely reach the mechanism a dismech entry describes.
Across 3,625 germline causative gene-disease pairs, 57% of the mouse orthologs
have been phenotyped. For those, the knockout hits 24% of the organ systems the
human entry's phenotypes touch and IMPC tested, against 18% for a randomly chosen
phenotyped gene. At the level of individual phenotypes the figures are 6% against
4%. Two thirds of the human-affected systems were tested in the mouse and gave no
call. In 55 pairs (3%) an IMPC call names a cell type or process that one of the
entry's own pathophysiology nodes binds. Nearly all of those are blood-cell,
platelet, immune, pigmentation or bone-mineral disorders, the places where the
IMPC pipeline measures something close to the mechanism. For susceptibility, risk
and modifier genes (the complex-disease case) the excess over random is smaller
still. IMPC data can now be cited as `IMPC:MGI:<n>`, and a pilot adds 17
IMPC-backed animal models to 12 entries where the readout does measure the node.
The gene-function half of the question, what knockouts say about molecular and
cellular function at all, is in the companion
[ai-gene-review `projects/IMPC.md`](https://github.com/ai4curation/ai-gene-review/blob/main/projects/IMPC.md).
Its main result explains this one: no IMPC call is defined on a molecular
function, and its cellular calls are almost all blood counts.

## Question

Can IMPC knockouts elucidate the mechanisms of disease, either Mendelian or
otherwise? We split this into four things a knockout could contribute to a
dismech entry:

1. **Coverage.** Has the mouse ortholog been phenotyped, and in a genotype
   relevant to the human disease (heterozygotes for a dominant disease)?
2. **System concordance.** Does the knockout reproduce the organ systems the
   human disease affects, more than an arbitrary knockout would, counting only
   systems IMPC actually tested?
3. **Phenotype concordance.** Does it reproduce the individual phenotypes?
4. **Mechanism contact.** Does any IMPC call land on a cell type or biological
   process that the entry's pathophysiology graph names?

## Method

[`IMPC/impc_disease_concordance.py`](IMPC/impc_disease_concordance.py) walks
every `kb/disorders/` entry and takes each germline `genetic:` row bound to an
`hgnc:` gene (`CAUSATIVE`, or `SUSCEPTIBILITY` / `RISK_FACTOR` / `MODIFIER`).
It maps the human symbol to the mouse gene through IMPC's own gene table and
reads IMPC data release 25.0, pinned in `data/impc/MANIFEST.yaml`: every
significant call (83,166 rows, legacy EuroPhenome and MGP lines included), the
procedures and systems each colony was tested for, and viability.

- **Systems.** Each HPO phenotype is lifted to its organ-system class (children
  of `HP:0000118`, HP 2026-09-01) and compared with the IMPC top-level MP
  categories through the hand-curated
  [`IMPC/hp_mp_system_map.yaml`](IMPC/hp_mp_system_map.yaml). Each human system
  is then *hit*, *tested without a call*, or *never tested* for that gene.
  Recall is hits over tested systems, so an untested system is not counted as a
  miss. Systems IMPC cannot test at all (neoplasm, breast, voice,
  constitutional, cellular) are dropped.
- **Phenotypes.** Each HPO and MP term is reduced to the cell type, anatomical
  entity or process its OWL logical definition says the abnormality inheres in
  (HP 2026-09-01, MP 2026-10-29). A human phenotype is matched when an IMPC call
  for the gene shares a bearer with it, comparing cell types through the CL
  `is_a` hierarchy (CL 2026-06-08).
- **Mechanism contact.** A pair has contact when an IMPC call's MP definition
  names a CL term related by `is_a`, in either direction, to a node's
  `cell_types` binding, ignoring very general cells such as leukocyte. Contact
  also counts when the call names a GO process that is a node's
  `biological_processes` binding or one of its ancestors (GO 2026-07-26).
- **Baseline.** Every recall is set against the mean recall of 300 random
  phenotyped IMPC genes scored against the same entry, because a gene with many
  calls overlaps almost any profile.

Per-pair results are in [`IMPC/results/pairs.tsv`](IMPC/results/pairs.tsv);
the generated report is [`IMPC/results/CONCORDANCE.md`](IMPC/results/CONCORDANCE.md).

## Results

| | Causative | Susceptibility / risk / modifier |
|---|---:|---:|
| Gene-disease pairs | 3,625 | 812 |
| Mouse ortholog in IMPC's gene table | 3,537 (98%) | 769 (95%) |
| Phenotyped by IMPC | 2,068 (57%) | 413 (51%) |
| At least one significant call | 1,926 (53%) | 367 (45%) |
| ...including a lethality call | 1,049 (54%) | 119 (32%) |
| Heterozygotes also tested | 1,593 (77%) | 243 (59%) |
| Human systems hit / tested without call / untested | 19% / 67% / 14% | 17% / 67% / 16% |
| Mean system recall over tested systems | 0.24 | 0.22 |
| ...random phenotyped IMPC gene | 0.18 | 0.19 |
| Mean phenotype recall (shared bearer) | 0.061 | 0.078 |
| ...random phenotyped IMPC gene | 0.037 | 0.053 |
| Mean system recall, heterozygote calls only | 0.15 | 0.21 |
| Mechanism contact (CL or GO shared with a node) | 55 (3%) | 20 (5%) |

**Most human-affected systems were tested and came back normal.** Of the organ
systems a disease entry's phenotypes touch, IMPC tested 86% in the mouse, and
two thirds gave no call. Most of that is the expected gap between a human disease
and a young null mouse, not evidence against the mechanism. The pipeline ends in
early adulthood, runs one test per system, and uses null alleles on one inbred
background. But it is now visible per pair, which it was not when only
significant calls were compared.

**Concordance is modest at the system level and small at the phenotype level.**
The knockout beats a random gene by six points of system recall and about two of
phenotype recall. Phenotype matching through logical definitions is strict, so
the absolute numbers are low for every gene. The excess over baseline is the
measure to read.

**Lethality is the most common thing IMPC says about a disease gene.** 54% of
causative pairs with any call include a lethality call. That is informative about
essentiality, but it also means many adult phenotypes were read on heterozygotes
or not at all. Diamond-Blackfan anaemia is an example: of its 15 genes, only
*Rps26* has been phenotyped.

**Genotype matters.** For a dominant disease the heterozygote is the matching
genotype. Restricting to heterozygote calls drops causative recall from 0.24 to
0.15, and 77% of phenotyped causative pairs had heterozygotes tested at all.

**Recorded loss of function does not raise concordance.** Pairs whose
pathophysiology node records loss of function reach 0.23 against a 0.18
baseline. Gain-of-function, dominant-negative, neomorphic and hypermorphic pairs
reach 0.22 against 0.17. A knockout should model a loss-of-function disease
better, so the absence of a difference says these measures are too coarse to see
it, not that the biology does not matter. Only 781 of the 3,625 causative pairs
record an impact at all, 22 of them `UNKNOWN`.

**Mechanism contact clusters where IMPC counts cells.** The 55 causative
contacts are mostly platelets and erythrocytes (10 pairs each), monocytes,
neutrophils and T-cell subsets, melanosome organization (`GO:0032438`, 8 pairs)
and bone mineralization. Many raw contacts are coincidental: the matched cell
type is real but the call does not measure what the node claims. Others are the
wrong direction, where the human disease is gain-of-function and a null mouse
does not model it (WHIM syndrome, THPO-related thrombocythemia, KCNN4
stomatocytosis, STAT1 gain-of-function candidiasis). Reading the list by hand is
what the pilot below did.

## Citing IMPC: `IMPC:MGI:<n>`

dismech can now cite IMPC data directly. `src/dismech/structured_sources/impc.py`
builds one `references_cache/IMPC_MGI_<n>.md` record per mouse gene from the
release pinned in `data/impc/MANIFEST.yaml`. Each record has three quotable
tables: viability; phenotyping coverage, meaning which procedures each colony
went through and which top-level systems were tested and significant; and every
significant call. Coverage is what lets an entry say "haematology was run and
found nothing", not only "a call was made". Records are built on demand for
cited genes, never for all ~9,900:

```bash
just fetch-reference IMPC:MGI:2448554     # or: just impc-rebuild --id IMPC:MGI:2448554
just impc-refresh                         # download the pinned release reports
```

CLAUDE.md (*Citing an IMPC knockout record*) has the evidence pattern and the
rules: IMPC evidence is `MODEL_ORGANISM` evidence about a null allele;
`model_scale` comes from what the procedure measured; and an absent call counts
only where the coverage table shows the system was tested.

## Pilot: IMPC-backed animal models

The pilot took the mechanism-contact pairs and kept those where the human disease
is recessive or loss-of-function and the IMPC readout measures what the node
claims. That gave 17 knockout records in 12 entries. Each links to its node
through `modeled_mechanisms`, with readouts quoting IMPC call rows and
limitations naming what the pipeline does not measure.

| Entry | Mouse line(s) | Node | Readout |
|---|---|---|---|
| Hermansky_Pudlak_Syndrome | *Hps5*, *Hps6*, *Dtnbp1*, *Bloc1s6*, *Bloc1s5* | Defective Melanosome Biogenesis | coat, iris and skin pigment |
| Griscelli_Syndrome_Type_2 | *Rab27a* | Failure of Peripheral Melanosome Capture and Transfer to Keratinocytes | coat colour and pattern |
| Chediak-Higashi_Syndrome | *Lyst* | Melanosome Dysfunction and Partial Albinism | coat colour, iris |
| Oculocutaneous_Albinism | *Slc24a5*, *Dct* | Cutaneous and Hair Hypopigmentation; Ocular Hypopigmentation and Foveal Maldevelopment | coat colour, iris transillumination |
| Gray_Platelet_Syndrome | *Nbeal2* | Macrothrombocytopenia and Impaired Platelet Function | platelet count, mean platelet volume |
| Hyper-IgM_Syndrome_Type_2 | *Aicda* | Giant Germinal Center Formation | germinal centre B cells |
| Sitosterolemia | *Abcg8* | Macrothrombocytopenia | mean platelet volume |
| X-Linked_Hypophosphatemia | *Phex* (EuroPhenome) | Reduced Circulating Phosphate; Skeletal Mineralization Failure | serum phosphate, bone mineral density, alkaline phosphatase |
| Autosomal_Recessive_Hypophosphatemic_Rickets_1 | *Dmp1* | Chronic Hypophosphatemia; Skeletal Mineralization Failure | serum phosphate, bone mineral density and content |
| Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency | *Card11* | Loss of Antigen-Receptor-Driven T Cell Activation | regulatory and effector T cells |
| Myeloperoxidase_Deficiency | *Mpo* | Loss of Neutrophil and Monocyte Myeloperoxidase Activity | large unstained cells, neutrophil and monocyte counts |
| Pyrimidine_5_Nucleotidase_Deficiency | *Nt5c3* | Shortened Erythrocyte Survival | red cell distribution width |

The *Mpo* line is the clearest case of a high-throughput readout landing on a
mechanism. A peroxidase-based analyser counts myeloperoxidase-negative
neutrophils and monocytes as "large unstained cells". So the IMPC pattern of
fewer neutrophils and monocytes with more large unstained cells is a direct
readout of absent peroxidase activity. That is the same artefact that flags MPO
deficiency in patients. The pigmentation lines are the commonest kind of contact.
Coat colour is visible, scored in every line, and reports melanosome biogenesis
through its end product. The weakest pilot links (*Abcg8*, *Nt5c3*) are recorded
with `fidelity: LOW` and say why.

## Answer, as far as it goes

- **Mendelian disease: a phenotype check, rarely a mechanism.** An IMPC
  knockout can confirm that loss of the gene disturbs the right system and
  stage. For blood, immune, pigmentation and mineral-metabolism disorders it can
  reach the affected cell or analyte. It cannot place the gene's product in a
  pathophysiology node: that needs the molecular and cellular readouts IMPC does
  not make.
- **Complex disease: weaker still.** Susceptibility and risk genes are knocked
  out completely, whereas the human effect is usually a small change in dosage
  or regulation. Their system concordance is barely above random.
- **Where it is useful for dismech:** an `animal_models` record citing
  `IMPC:MGI:<n>` that `RECAPITULATES` or `PARTIALLY_RECAPITULATES` a node the
  readout measures, as in the pilot. A null mouse that was tested for the
  defining human system and showed nothing is a candidate `FAILS_TO_RECAPITULATE`
  link or `HUMAN_MODEL_MISMATCH` discussion. The coverage table makes that
  checkable, but it still needs a curator to judge whether the IMPC test could
  have detected the human phenotype.

## Caveats

- The system map is coarse by design, and logical-definition matching misses
  phenotypes whose HP and MP definitions name related but different entities.
- Gene mapping uses IMPC's human-symbol field; 1:many orthologs are pooled.
- dismech phenotype lists are curated from human literature and are uneven
  across entries, which affects recall in both directions.
- IMPC is predominantly C57BL/6N, early adult and null alleles; the analysis
  says nothing about knock-in models of patient variants.

## How this relates to existing projects

- [`COMMONFUND/KOMP2.md`](COMMONFUND/KOMP2.md) proposed a ten-gene IMPC
  concordance pass and a `komp2.py` helper. This project runs that comparison
  corpus-wide, and the `IMPC:` source is the citable helper. KOMP2's evidence
  wording still describes IMPC evidence as `PARTIAL`, a `supports` value that has
  been retired. The right encoding is `SUPPORT` with `evidence_source:
  MODEL_ORGANISM`.
- [`MODEL_ORGANISM_ASSAYS.md`](MODEL_ORGANISM_ASSAYS.md) is designing readout
  slots for an IMPReSS parameter and an MP result term. Once they exist, the
  pilot readouts can carry the parameter and MP term structurally instead of
  only inside the quoted row.

## Plan

- [x] Corpus-wide coverage, system concordance and mechanism-contact pass.
- [x] Pin an IMPC release and read it instead of the live API.
- [x] Separate "tested, no call" from "never tested" per system.
- [x] CL-hierarchy mechanism contact and phenotype-level matching.
- [x] Heterozygote-only recall.
- [x] `IMPC:` structured reference source, with tests and documentation.
- [x] Pilot: 17 IMPC-backed animal models in 12 entries.
- [ ] Extend the pilot to the remaining coincidental-looking contacts after
      reading each, and to diseases whose node is measured by a procedure IMPC
      runs (hearing, bone, glucose tolerance) even where no cell or process term
      is shared.
- [ ] Draft `FAILS_TO_RECAPITULATE` links for well-characterised loss-of-function
      diseases whose defining system was tested without a call, each checked by
      hand for whether the IMPC test could see the human phenotype.
- [ ] Complex-disease genes against GWAS effect direction. dismech does not
      record a direction for most susceptibility genes, so this needs that data
      first.

## Reproduce

Raw downloads go to the git-ignored `.cache/impc/` and `data/impc/*.csv.gz`.

```bash
just impc-refresh
uv run python projects/IMPC/fetch_impc.py
curl -sSL -o .cache/impc/mp.owl https://purl.obolibrary.org/obo/mp.owl
curl -sSL -o .cache/impc/hp.owl https://purl.obolibrary.org/obo/hp.owl
curl -sSL -o .cache/impc/hp.obo https://purl.obolibrary.org/obo/hp.obo
curl -sSL -o .cache/impc/go-basic.obo https://purl.obolibrary.org/obo/go/go-basic.obo
curl -sSL -o .cache/impc/cl-basic.obo https://purl.obolibrary.org/obo/cl/cl-basic.obo
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
