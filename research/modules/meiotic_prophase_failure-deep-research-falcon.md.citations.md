# Citations for Research Query

**Query:** # Mechanism Module Research Template

## Target Module
- **Module Name:** Meiotic Prophase Failure Module
- **Module Slug:** meiotic_prophase_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module for inherited gametogenic failure caused by disruption of meiotic prophase I chromosome synapsis and recombination. In affected germ cells, programmed meiotic chromosome events fail at homolog pairing, synaptonemal complex assembly, homologous-recombination repair of DNA double-strand breaks, or pachytene checkpoint resolution. The shared path is meiotic arrest with germ-cell apoptosis, producing sex-dimorphic clinical outcomes: ovarian follicle depletion and primary ovarian insufficiency in 46,XX individuals, and spermatogenic arrest with non-obstructive azoospermia or Sertoli-cell-only syndrome in 46,XY individuals. This module is intended for meiotic genes such as SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, and SYCP3. It intentionally excludes upstream gonadal organogenesis and steroidogenic transcription-factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Current Provisional Nodes

- Meiotic Prophase I Entry and Homolog Pairing: Germ cells enter the meiotic cell cycle and initiate prophase I chromosome pairing. This node captures the shared upstream context for module genes: the gonad is present, germ cells enter meiosis, and homologous chromosomes must pair before synapsis and recombination can be completed.
- Synaptonemal Complex Assembly: Synaptonemal complex components assemble between paired homologous chromosomes during meiotic prophase I. Disruption of central or lateral element proteins such as SYCE1 or SYCP3 produces asynapsis or unstable synapsis, preventing normal progression through pachytene.
- Homologous Recombination Repair of Meiotic DNA Breaks: Programmed and repair-associated DNA breaks in meiotic prophase require homologous-recombination machinery to complete chromosome pairing, crossover formation, and genome integrity surveillance. Disruption of repair factors such as MCM8, MCM9, DMC1, HFM1, MSH4, or MSH5 leaves meiotic DNA damage unresolved and blocks normal pachytene progression.
- Pachytene Checkpoint Arrest and Germ Cell Apoptosis: Failed synapsis or unresolved meiotic recombination activates pachytene checkpoint signaling. Instead of completing meiotic prophase and producing functional gametes, affected germ cells arrest and are eliminated by apoptosis.
- Ovarian Follicle Depletion and Primary Ovarian Insufficiency: In 46,XX individuals, loss of oocytes during fetal or early postnatal meiotic progression depletes the ovarian follicle pool. The clinical manifestation is primary ovarian insufficiency, ovarian dysgenesis, primary amenorrhea, or hypergonadotropic hypogonadism depending on ascertainment and residual ovarian reserve.
- Spermatogenic Arrest and Non-Obstructive Azoospermia: In 46,XY individuals, meiotic prophase failure in spermatocytes produces spermatogenic arrest, often observed clinically as non-obstructive azoospermia, maturation arrest, or Sertoli-cell-only syndrome after germ cell depletion.
- Somatic DNA Repair Deficiency and Cancer Predisposition: A gene-specific branch for module genes that also function in mitotic or somatic DNA repair. MCM8 and MCM9 are the main current examples: biallelic variants may combine meiotic prophase failure with germ-cell tumors or gastrointestinal polyposis and early-onset malignancy. This branch should be used only when gene-specific evidence supports a somatic cancer phenotype.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology of meiotic prophase I failure leading to
gametogenic failure. Prioritize evidence for:

- The conserved causal chain: meiotic prophase entry, homolog pairing,
  synaptonemal complex assembly, meiotic homologous-recombination repair,
  pachytene checkpoint arrest, germ-cell apoptosis, and sex-dimorphic outcomes.
- The boundary between synaptonemal complex structural genes and homologous
  recombination / DNA-repair genes.
- Gene-specific branches for MCM8 and MCM9 somatic DNA repair and cancer
  predisposition, while distinguishing these from the core meiotic module.
- Explicit exclusions: gonadal organogenesis and steroidogenesis transcription
  factor disorders such as NR5A1, WT1, SOX9, SRY, FOXL2, and DHH.

## Key Genes In Scope

SYCE1, MCM8, MCM9, STAG3, HFM1, MSH4, MSH5, DMC1, SYCP3.

## Questions To Answer

1. What is the best-supported shared mechanism across these genes?
2. Should the module be named `meiotic_prophase_failure`,
   `meiotic_recombination_failure`, or something else?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes support the synaptonemal-complex branch, the homologous
   recombination branch, and the somatic DNA-repair/cancer branch?
5. What evidence supports pachytene checkpoint arrest and apoptosis as the
   shared terminal mechanism in both 46,XX and 46,XY presentations?
6. What direct human evidence links the same gene or variant class to both
   primary ovarian insufficiency and non-obstructive azoospermia?
7. What model organism evidence clarifies the causal path from meiotic defect
   to germ-cell loss?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.

**Provider:** falcon
**Generated:** 2026-05-28T08:37:29.278503

1. llano2023synaptonemalcomplexin pages 7-8
2. huang2024geneticcontrolof pages 11-12
3. acharya2024mechanismofdna pages 1-2
4. bijl2019mutationsinthe pages 1-2
5. ding2023dnadoublestrandbreak pages 14-16
6. verrilli2021sharedgeneticsbetween pages 5-6
7. verrilli2021sharedgeneticsbetween pages 3-5
8. ozturk2023geneticvariantsunderlying pages 34-35
9. acharya2024mechanismofdna pages 16-16
10. llano2023synaptonemalcomplexin pages 8-10
11. ding2023dnadoublestrandbreak pages 21-22
12. cioppi2021geneticsofazoospermia pages 20-21
13. ozturk2023geneticvariantsunderlying pages 20-22
14. and
15. https://doi.org/10.3390/cells12131718
16. https://doi.org/10.1186/s13048-023-01221-2
17. https://doi.org/10.1016/j.xfnr.2021.04.001
18. https://doi.org/10.1093/molehr/gaaa050
19. https://doi.org/10.1093/humrep/dez204
20. https://doi.org/10.3389/fcell.2023.1127440
21. https://doi.org/10.1038/s44318-024-00134-0
22. https://doi.org/10.1038/s41467-024-47936-8
23. https://doi.org/10.3390/cells12131718,
24. https://doi.org/10.1186/s13048-023-01221-2,
25. https://doi.org/10.3389/fcell.2023.1127440,
26. https://doi.org/10.1038/s44318-024-00134-0,
27. https://doi.org/10.1038/s41467-024-47936-8,
28. https://doi.org/10.1093/humrep/dez204,
29. https://doi.org/10.1093/molehr/gaaa050,
30. https://doi.org/10.1016/j.xfnr.2021.04.001,
31. https://doi.org/10.1080/15384101.2023.2171544,
32. https://doi.org/10.3390/ijms22063264,
