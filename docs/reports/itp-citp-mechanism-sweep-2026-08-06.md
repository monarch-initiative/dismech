# ITP / CITP bibliography sweep: which publications carry mechanism?

**Date:** 2026-08-06
**Scope:** All 20 publications listed on the [MPD ITP1 project page](https://phenome.jax.org/projects/ITP1)
and all 24 PubMed-indexed publications listed on the [CITP publications page](https://citpaging.org/publications).
**Question:** The hosted data for both programs is overwhelmingly chemical→lifespan association.
Where does the mechanism actually live, and which papers would a dismech curator cite?

## Why this sweep exists

The NIA **Interventions Testing Program** (ITP; UM-HET3 mice, 3 sites) and the NIA
***Caenorhabditis* Intervention Testing Program** (CITP; 3 *Caenorhabditis* species, 3 sites)
are the two highest-quality replication-controlled geroprotector screens in existence. Their
portals are tempting as an evidence source for treatment claims against dismech's
hallmark-of-aging modules. But an inspection of the hosted data (recorded below) shows that
neither portal supports mechanism directly — the portals are survival statistics. If mechanism
is to be curated, it has to come from the publications.

This document classifies every publication in both bibliographies by how much mechanistic
content it carries, so that a curator can go straight to the ~9 papers that have any.

### What the portals actually contain

Measured from the live data tables, not the portal prose:

**ITP1 (MPD)** — 74 compound × cohort trials, 62 unique compounds, 21 with a significant
lifespan p-value.

- Only **22 of 74 trials carry any secondary phenotype at all**, and **all 22 of those are body weight**.
- Beyond body weight, the entire secondary-phenotype layer is two trials: grip strength/duration
  and rotarod on acarbose C2013 and NDGA C2010.
- **Exactly one trial** (acarbose C2013) has the full panel — body composition, fat pads,
  glucose meter, grip force/duration, rotarod, pathology.
- The histopathology layer is four organ/condition categories with an odds ratio and p-value
  per sex (adrenal medullary vasodilation, liver degeneration, lung tumor, renal glomerulosclerosis).
- **No molecular, biochemical, transcriptomic, or proteomic measure anywhere in the portal.**

**CITP portal** — 468 summary rows across 48 compounds.

- **Dose–response**: median 5 concentrations per compound, up to 9.
- **Genetic background**: 11 strains across 3 species; 9 compounds run across all 9 strain × species combinations.
- Per-row survival statistics: n dead/censored/total, median + 95% CL, mean ± SE, 90th quantile,
  Cox PH p-value, `Quality` flag, lab/site attribution.
- **RNA-seq**: 8 experiments, **2 compounds only** (sulforaphane 5-point age time course;
  retinoic acid in N2 + two mutant backgrounds), GEO-linked (GSE289233, GSE272535).
- The two mutant strains in the RNA-seq arm (PS3551 *hsf-1(sy441)*, RB754 *aak-2(ok524)*)
  carry `has_ls=False` — **they exist in the portal only as RNA-seq entries.** The lifespan
  epistasis is in the paper, not the tables.

## Tier definitions

| Tier | Meaning |
|---|---|
| **0** | Program design, methods, assay platform, software, or resource paper. No biological claim about an intervention. |
| **1** | Lifespan association only. Compound → survival, optionally with body weight. No mechanism. |
| **2** | Lifespan + organ, physiology, or healthspan phenotype (pathology, glucose handling, stress resistance, mobility). Localizes the effect to a tissue or function but identifies no molecular pathway. |
| **3** | **Mechanism-bearing.** Molecular or pathway-level evidence: omics, genetic epistasis, target identification, or pharmacokinetics used to explain a differential response. |

## ITP (mouse) — 20 publications

| PMID | Year | Short title | Tier | Mechanistic content |
|---|---|---|---|---|
| 17578509 | 2007 | Study design and interim report | 0 | Design paper; describes planned T-cell subset and activity assays |
| 19424842 | 2008 | Design of aging intervention studies | 0 | Program design |
| 27923560 | 2017 | NIA ITP: investigating putative agents | 0 | Program overview (no abstract) |
| 18631321 | 2008 | NDGA and aspirin increase male lifespan | 1 | Lifespan only |
| 22451473 | 2013 | Resveratrol, GTE, curcumin, OAA, MCT | 1 | All null; lifespan only |
| 27312235 | 2016 | Protandim, fish oil, UDCA, metformin, 17aE2, NDGA | 1 | Lifespan; Nrf2 framing asserted, not measured |
| 33788371 | 2021 | 17aE2 late-life; NR and 3 others null | 1 | Lifespan + body weight |
| 36179270 | 2022 | Rapamycin + acarbose combination; captopril | 1 | Drug-combination potency, no molecular readout |
| 38041783 | 2024 | Astaxanthin, meclizine; 5 null | 1 | Target class asserted (Nrf2 activator, mTORC1 inhibitor), not assayed |
| 40973907 | 2026 | Epicatechin, halofuginone, mitoglitazone | 1 | Lifespan only |
| 33145977 | 2020 | Rapamycin late-life dosing regimens | 1 | Dosing schedule; confounded by diet-supplier weight variation |
| 19587680 | 2009 | Rapamycin fed late in life (Nature) | 2 | Lifespan + disease patterns at necropsy; mTOR inferred, not measured |
| 20974732 | 2011 | Rapamycin, not resveratrol or simvastatin | 2 | Lifespan + spontaneous activity + causes of death |
| 22587563 | 2012 | **Rapamycin slows aging in mice** | 2 | Multi-tissue aging-rate: heart, liver, adrenal, endometrium, tendon, plus activity; also harms (testicular degeneration, cataracts) |
| 30688027 | 2019 | **Acarbose improves health and lifespan** | 2 | Lung tumors, liver degeneration, glomerulosclerosis, refeeding glucose response, rotarod — the C2013 dataset behind the portal's only pathology page |
| 30916479 | 2019 | Glycine supplementation | 2 | 40 necropsy pathology categories; pulmonary adenocarcinoma reduced; methionine-toxicity framing |
| 32990681 | 2020 | Canagliflozin | 2 | Fasting glucose, glucose tolerance, fat mass; mechanism argued by convergence with acarbose ("blunting of peak glucose levels") |
| 24245565 | 2014 | Acarbose, 17-α-estradiol, NDGA male-preferential | **3** | PK used to *exclude* a mechanism: NDGA at a dose producing female blood levels matching males still gave no female benefit |
| 38753230 | 2024 | Sodium thiosulfate, 16-OH-estriol, late canagliflozin | **3** | "blood levels of Cana were approximately 20-fold higher in aged females than in young males, suggesting a possible mechanism for the sex-specific disparities" |
| 24341993 | 2014 | **Rapamycin dose/sex dependent, metabolically distinct from DR** | **3** | Hepatic xenobiotic-metabolism gene expression profiles differ between rapamycin and dietary restriction; drug blood levels differ by sex |

**ITP totals: 3 Tier-0, 8 Tier-1, 6 Tier-2, 3 Tier-3.**

The single most mechanism-bearing ITP paper is **PMID:24341993** — it is the one that separates
rapamycin from dietary restriction on a molecular readout rather than asserting they differ. The
other two Tier-3 entries are pharmacokinetic, not pathway-level: they explain *why a response
differs by sex*, which is mechanistically real but narrow.

Note the striking pattern: **ITP's most mechanistic work is about sexual dimorphism**, because
that is the phenomenon the lifespan data itself forces the investigators to explain.

## CITP (nematode) — 24 publications

| PMID | Year | Short title | Tier | Mechanistic content |
|---|---|---|---|---|
| 28060275 | 2016 | CeleST swim behavior software | 0 | Methods |
| 28836615 | 2017 | A long journey to reproducible results | 0 | Nature comment |
| 31042764 | 2019 | The Stress-Chip microfluidic platform | 0 | Methods |
| 31820364 | 2019 | Automated Lifespan Machines across strains | 0 | Methods/validation; notes assay-specific intervention effects |
| 33204740 | 2020 | Simplified lifespan machine design | 0 | Methods |
| 35098051 | 2022 | Genetic diversity estimates for the screening panel | 0 | Resource; whole-genome-based diversity of the 22-strain panel |
| 40178707 | 2025 | CITP program overview | 0 | Program design |
| 32010883 | 2019 | Imatinib does not extend lifespan | 1 | Null |
| 31998863 | 2020 | β-guanidinopropionic acid does not extend lifespan | 1 | Null |
| 32550518 | 2020 | Obeticholic acid does not robustly extend lifespan | 1 | Null |
| 34585102 | 2021 | Diuron does not robustly extend lifespan | 1 | Null |
| 41993912 | 2026 | Levetiracetam does not extend lifespan | 1 | Null; notes anticonvulsants differ in effect |
| 28220799 | 2017 | **Impact of genetic background and reproducibility** (Nat Commun) | 1 | Landmark: 22 strains, 3 species, 10 compounds. Establishes strain/species specificity of DR mimetics vs. robustness of ThioflavinT. Association, but across the genetic axis |
| 34837316 | 2022 | Metformin across diverse *Caenorhabditis* | 2 | Lifespan + healthspan; metformin benefit is genetic-background dependent (works in *C. elegans* strains, not *C. briggsae*) |
| 37923874 | 2024 | Green tea extract and NDGA | 2 | Species- and strain-specific lifespan *and* health effects |
| 38613792 | 2024 | Healthspan–lifespan coupling | 2 | Swim performance, thermotolerance, oxidative stress resistance across the panel for NP1, propyl gallate, resveratrol; shows the relationships are not simply coupled |
| 40027526 | 2025 | Tamibarotene and bakuchiol do not extend lifespan | 2 | Structure–activity argument: a *potent RAR agonist* fails where atRA works, constraining atRA's mechanism |
| 41701440 | 2026 | Male lifespan and reproductive healthspan | 2 | Sex differences; lifespan and reproductive healthspan decouple (only sulforaphane and metformin improved late-life mating success) |
| 32831297 | 2020 | Insolublome quantification by DIA proteomics | **3** | Methods paper, but the readout is proteostasis: SDS-insoluble proteome extraction and label-free quantification |
| 32877690 | 2020 | **Alpha-ketoglutarate extends lifespan and compresses morbidity in mice** (Cell Metab) | **3** | IL-10 induction suppressing chronic inflammation; systemic inflammatory cytokines; frailty. *Mouse, not worm* |
| 38753231 | 2024 | **Amyloid β accelerates proteome-wide protein insolubility** | **3** | Unbiased proteomics; Aβ drives proteome-wide insolubility in *C. elegans* even in young animals |
| 40462948 | 2025 | **Sulforaphane slows the transcriptional aging clock** | **3** | RNA-seq-derived gene-specific transcriptional aging clock; ~4-day younger transcriptional age (~20% biological-age reduction); detoxification pathways dominant; dose-response shape indicates hormesis |
| 42320027 | 2026 | **Translation state modulators extend lifespan** | **3** | 4E-BP/eIF4E pathway, 5'-UTR-length-dependent translation; cell-based screen; DR/cold-induced-longevity mimicry; *Drosophila* + *C. elegans* |
| 41432067 | 2025 | **Retinoic acid modulation drives conserved longevity pathways** (eLife) | **3** | **The flagship.** Genetic epistasis + RNA-seq |

**CITP totals: 7 Tier-0, 6 Tier-1, 5 Tier-2, 6 Tier-3.**

### The atRA paper (PMID:41432067) in detail

This is the only paper in either bibliography that does full pathway dissection, and it is the
reason CITP is mechanistically ahead of ITP despite the shorter-lived model.

Epistasis strains and their outcome for atRA lifespan extension:

| Strain | Gene | Human ortholog concept | atRA extension |
|---|---|---|---|
| RB754 | *aak-2(ok524)* | AMPK catalytic subunit | **Required** |
| RB759 / VC204 | *akt-1(ok525)* / *akt-2(ok393)* | AKT | **Required** |
| PS3551 | *hsf-1(sy441)* | HSF1 | **Required** |
| — | *skn-1* | NRF2 | **Required** |
| CF1038 | *daf-16(mu86)* | FOXO | Not absolutely required; partial contribution |
| KU25 | *pmk-1(km25)* | p38 MAPK | Less critical |
| IG10 | *tol-1(nr2033)* | Toll-like receptor | Enhanced response |

Transcriptional findings: 17% (2,169) of detected genes differentially expressed; 83% (20/24) of
the most-upregulated genes previously IIS-regulated and 71% Nrf2-regulated; sphingolipid metabolism
and fatty-acid biosynthesis enriched.

## Summary

| | ITP | CITP |
|---|---|---|
| Publications swept | 20 | 24 |
| Tier 0 (design/methods) | 3 | 7 |
| Tier 1 (lifespan only) | 8 | 6 |
| Tier 2 (organ/physiology) | 6 | 5 |
| **Tier 3 (mechanism)** | **3** | **6** |
| Nature of the Tier-3 work | Pharmacokinetics + one hepatic expression comparison | Genetic epistasis, transcriptomics, proteomics, target pathway |

**Roughly 20% of the combined bibliography (9 of 44) carries mechanism**, and the two programs
carry different kinds. ITP's mechanism is pharmacological (why does this drug act differently in
males?). CITP's is pathway-level (which conserved longevity pathway does this compound require?).

CITP's Tier-3 papers are also disproportionately *recent* — five of six are 2024 or later —
which suggests the program has shifted from screening toward mechanism as its compound set matured.

## Relevance to dismech modules

The Tier-3 set maps onto modules the KB already has. None of this is curatable as a human
treatment claim (`evidence_source: MODEL_ORGANISM` or `IN_VITRO` throughout, per the evidence
policy), but it is legitimate module-level mechanism evidence.

| PMID | Maps to | Note |
|---|---|---|
| 41432067 | `deregulated_nutrient_sensing` (AMPK, AKT/IIS), `loss_of_proteostasis` (HSF-1) | Epistasis establishes *requirement*, not correlation |
| 42320027 | `deregulated_nutrient_sensing`, `loss_of_proteostasis`, `mitochondrial_dysfunction` | 4E-BP/eIF4E translational control |
| 38753231 | `loss_of_proteostasis`, `amyloidogenesis` | Aβ → proteome-wide insolubility; connects two existing modules |
| 32831297 | `loss_of_proteostasis` | Assay method for the insolublome |
| 32877690 | `inflammaging` | AKG → IL-10 → reduced chronic inflammation; **mouse**, so the strongest of the set translationally |
| 40462948 | `epigenetic_alterations` (as a transcriptional-age biomarker) | Also a hormesis/detoxification claim |
| 24341993 | `deregulated_nutrient_sensing` | Separates rapamycin from DR on hepatic gene expression |
| 22587563 | Cross-cutting | Best available "does it slow aging broadly or just suppress tumors?" multi-tissue evidence |
| 32990681 / 30688027 | `diabetic_vascular_complications` (glucose-excursion arm) | Acarbose/canagliflozin converge on postprandial glucose blunting |

## Caveats

1. **Classification is from abstracts, not full text.** A Tier-1 or Tier-2 paper may contain
   mechanistic figures not described in its abstract. The tiers indicate where mechanism is
   *advertised*, which is the right filter for deciding what to read next — not a claim about
   the paper's total content.
2. **Two CITP-listed papers are mouse or fly work** from consortium labs rather than core
   nematode CITP output (PMID:32877690 alpha-ketoglutarate in mice; PMID:42320027 includes
   *Drosophila*). They are listed on the CITP publications page and are included here, but a
   curator should note the organism explicitly.
3. **PMID:40462948 is a bioRxiv preprint** (2025.05.11.653363) at time of sweep. Its RNA-seq is
   in the portal (GSE289233), but the paper is not peer-reviewed. Treat accordingly.
4. **Tier 3 does not mean "human-relevant."** Every mechanism paper here is model-organism or
   in-vitro. Under the dismech evidence policy these cannot be sole support for a human
   phenotype claim.
5. **Null results are not failures.** Both programs publish negatives by policy, and the
   Tier-1 nulls (imatinib, obeticholic acid, diuron, β-GPA, levetiracetam, tamibarotene,
   bakuchiol; resveratrol, curcumin, MCT oil, nicotinamide riboside, fisetin) are among the most
   valuable content in either bibliography, because they are replication-controlled refutations
   of widely promoted compounds. In dismech terms these are candidate
   `supports: REFUTE` evidence items.

## Sources

- [MPD ITP1 project page](https://phenome.jax.org/projects/ITP1) and its measure/pathology tables
- [CITP Data Portal](https://citpaging.org/portal) — `summary.json`, `compound.json`, `strain.json`, `rnaseq.json`
- [CITP publications page](https://citpaging.org/publications)
- PubMed abstracts for all 44 PMIDs, retrieved 2026-08-06 via NCBI E-utilities
- [Banse et al. 2025, eLife 13:RP104375](https://elifesciences.org/articles/104375) ([PMC12258912](https://pmc.ncbi.nlm.nih.gov/articles/PMC12258912/))
