# MCD New-Approach-Methodology (NAM) paper map

Curator reference for the malformation-of-cortical-development (MCD) curation
cluster seeded from:

> Romero DM, Bahi-Buisson N, Francis F. *Genetics and mechanisms leading to
> human cortical malformations.* Seminars in Cell & Developmental Biology
> 76:33–75 (2018). DOI: [10.1016/j.semcdb.2017.09.031](https://doi.org/10.1016/j.semcdb.2017.09.031)

Tracks issue [#4100](https://github.com/monarch-initiative/dismech/issues/4100)
("capture iPSC/organoid NAM evidence and modeling patterns for cortical
malformation curation"), itself part of the cortical-malformation epic
[#4098](https://github.com/monarch-initiative/dismech/issues/4098).

## Purpose

The review's Section 4 treats stem-cell / organoid systems (NAMs) as the primary
tools for studying *human-specific* cortical-development mechanisms that rodent
models miss (most notably basal/outer radial glia, bRG/oRG). This file maps the
NAM papers behind that section to **verified PubMed identifiers**, so that every
MCD entry and module in the cluster cites the same, identity-checked references
with consistent `evidence_source` handling.

## How this map was built (anti-hallucination methodology)

Per the CLAUDE.md deep-research SOP, review-summary reference numbers and
recalled PMIDs are treated as *leads, not ground truth*. Every PMID below was:

1. fetched with `just fetch-reference PMID:<id>` (never hand-created), and
2. confirmed by reading the **cached title / journal / year** in
   `references_cache/PMID_<id>.md` against the paper the review describes.

Where the issue thread named a specific paper for a Romero reference bracket
(e.g. `[298]` = Bershteyn; `[299]` = Iefremova; `[278]` = KATNB1), the bracket is
reproduced from the issue. For clusters the issue gives only as a *range*
(e.g. ZIKV `[294–297, 309–311]`), papers are assigned to the **cluster**, not to
a single bracket number, because the Romero reference list was not independently
available to pin exact numbers — the paper *identity* is verified from the cache,
the exact bracket index is not. Unverified bracket→PMID guesses are listed under
"Not yet mapped" rather than asserted.

## Core curation rule (from #4100)

NAM data — patient-derived iPSC, hESC-derived neural rosettes, neurospheres,
cerebral/forebrain organoids, organotypic fetal slices, single-cell profiling of
organoids — is **mechanistic evidence, classified `IN_VITRO`**, not
`HUMAN_CLINICAL`. Always name the model system in the evidence `explanation`
(e.g. "patient-derived iPSC forebrain organoid", "human cerebral organoid
single-cell profiling"). Use the `HUMAN_MODEL_MISMATCH` discussion kind (not a
generic `KNOWLEDGE_GAP`) when the point is that human organoid/fetal data reveal
biology absent or weak in rodent models — the canonical example being bRG/oRG
findings.

---

## NAM platform / foundational methods (Romero cluster [282–284, 293] and [288–291])

These establish the platforms themselves; cite them when a node's evidence rests
on the validity of the model system rather than a disease-specific finding.

| PMID | Verified title (from cache) | First author / journal / year | NAM platform | Cited by (MCD cluster) |
|------|------------------------------|-------------------------------|--------------|------------------------|
| [16904174](https://pubmed.ncbi.nlm.nih.gov/16904174/) | Induction of pluripotent stem cells from mouse embryonic and adult fibroblast cultures by defined factors. | Takahashi K et al., *Cell*, 2006 | iPSC reprogramming (foundational) | foundational platform reference (fetch-reference-verified; not yet cited in the cluster) |
| [18035408](https://pubmed.ncbi.nlm.nih.gov/18035408/) | Induction of pluripotent stem cells from adult human fibroblasts by defined factors. | Takahashi K et al., *Cell*, 2007 | human iPSC reprogramming (foundational) | foundational platform reference (fetch-reference-verified; not yet cited in the cluster) |
| [23995685](https://pubmed.ncbi.nlm.nih.gov/23995685/) | Cerebral organoids model human brain development and microcephaly. | Lancaster MA et al., *Nature*, 2013 | cerebral organoid corticogenesis | already in repo cache; cited by `microtubule_dependent_neuronal_migration_failure`, `apical_neuroependyma_integrity_failure`, `pial_basement_membrane_radial_glial_endfoot_failure`, `reelin_terminal_translocation_lamination_failure` |

---

## Lissencephaly / Miller-Dieker (MDS) organoid models (Romero `[298]`, `[299]`)

| PMID | Verified title (from cache) | First author / journal / year | NAM finding | Romero ref | Cited by (MCD cluster) |
|------|------------------------------|-------------------------------|-------------|-----------|------------------------|
| [28111201](https://pubmed.ncbi.nlm.nih.gov/28111201/) | Human iPSC-Derived Cerebral Organoids Model Cellular Features of Lissencephaly and Reveal Prolonged Mitosis of Outer Radial Glia. | Bershteyn M et al., *Cell Stem Cell*, 2017 | MDS patient iPSC organoids: neuroepithelial apoptosis, reduced size, altered cleavage angle, defective radial migration rescued by chromosome-17 compensation; **prolonged oRG mitosis (human-specific, absent in mouse)** | `[298]` | `neural_progenitor_centrosome_spindle_dysfunction`, `microtubule_dependent_neuronal_migration_failure`, `apical_neuroependyma_integrity_failure`, `pial_basement_membrane_radial_glial_endfoot_failure`, `reelin_terminal_translocation_lamination_failure`, `interneuron_specification_tangential_migration_failure`, `KATNB1-related_Cortical_Malformation`, `TUBA1A-related_Tubulinopathy`, `TUBB_TUBB5-related_Microcephaly`, `NDE1-related_Microcephaly_Lissencephaly` |
| [28380362](https://pubmed.ncbi.nlm.nih.gov/28380362/) | An Organoid-Based Model of Cortical Development Identifies Non-Cell-Autonomous Defects in Wnt Signaling Contributing to Miller-Dieker Syndrome. | Iefremova V et al., *Cell Rep*, 2017 | MDS forebrain organoids: premature neurogenesis, symmetric→asymmetric apical RGC division switch, altered N-cadherin/β-catenin/Wnt; **rescue by Wnt activation** | `[299]` | `neural_progenitor_centrosome_spindle_dysfunction` |

> **bRG/oRG note:** 28111201's prolonged-oRG-mitosis finding is the cluster's
> clearest case of a NAM result that *disambiguates an entry boundary* — oRG
> biology is a LIS1/MDS-specific feature not shared by DCX or most other LIS
> genes, and is not reproduced in mouse. Model it with a `HUMAN_MODEL_MISMATCH`
> discussion where it bears on lump/split decisions.

---

## Centrosome / spindle progenitor models (Romero `[278]`)

| PMID | Verified title (from cache) | First author / journal / year | NAM finding | Romero ref | Cited by (MCD cluster) |
|------|------------------------------|-------------------------------|-------------|-----------|------------------------|
| [25521378](https://pubmed.ncbi.nlm.nih.gov/25521378/) | Mutations in KATNB1 cause complex cerebral malformations by disrupting asymmetrically dividing neural progenitors. | Mishra-Gorur K et al., *Neuron*, 2014 | KATNB1 patient-derived cells / progenitor models: disrupted asymmetric progenitor division, defective neuronal production and migration | `[278]` | `neural_progenitor_centrosome_spindle_dysfunction`, `KATNB1-related_Cortical_Malformation`, `Autosomal_Recessive_Primary_Microcephaly` |

---

## ZIKV neural-progenitor / organoid models (Romero cluster [294–297, 309–311])

These are the primary mechanistic evidence for the viral progenitor-cytopathy
pathway (`kb/modules/viral_neural_progenitor_cytopathy.yaml`, #4079) and the
Congenital Zika Syndrome entry (#4088). All are `IN_VITRO` **except where noted**.

| PMID | Verified title (from cache) | First author / journal / year | NAM finding | Cited by (MCD cluster) |
|------|------------------------------|-------------------------------|-------------|------------------------|
| [26952870](https://pubmed.ncbi.nlm.nih.gov/26952870/) | Zika Virus Infects Human Cortical Neural Progenitors and Attenuates Their Growth. | Tang H et al., *Cell Stem Cell*, 2016 | human iPSC-derived NPCs (hNPCs) are direct ZIKV targets; increased cell death, cell-cycle dysregulation, attenuated growth | `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [27064148](https://pubmed.ncbi.nlm.nih.gov/27064148/) | Zika virus impairs growth in human neurospheres and brain organoids. | Garcez PP et al., *Science*, 2016 | reduced viability/growth of human neurospheres and brain organoids → abrogated neurogenesis | `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [27038591](https://pubmed.ncbi.nlm.nih.gov/27038591/) | Expression Analysis Highlights AXL as a Candidate Zika Virus Entry Receptor in Neural Stem Cells. | Nowakowski TJ et al., *Cell Stem Cell*, 2016 | single-cell expression: candidate entry receptor AXL enriched on human radial glia / astrocytes / endothelium / microglia | `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [27162029](https://pubmed.ncbi.nlm.nih.gov/27162029/) | Zika Virus Depletes Neural Progenitors in Human Cerebral Organoids through Activation of the Innate Immune Receptor TLR3. | Dang J et al., *Cell Stem Cell*, 2016 | hESC-derived cerebral organoids: TLR3 upregulation, perturbed cell fate, reduced organoid volume; TLR3 inhibition partially rescues | `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [27568284](https://pubmed.ncbi.nlm.nih.gov/27568284/) | Zika Virus Disrupts Phospho-TBK1 Localization and Mitosis in Human Neuroepithelial Stem Cells and Radial Glia. | Onorati M et al., *Cell Rep*, 2016 | human neuroepithelial stem cells / radial glia: pTBK1 mislocalization, disrupted centrosome/mitosis | `neural_progenitor_centrosome_spindle_dysfunction`, `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [28132835](https://pubmed.ncbi.nlm.nih.gov/28132835/) | Recent Zika Virus Isolates Induce Premature Differentiation of Neural Progenitors in Human Brain Organoids. | Gabriel E et al., *Cell Stem Cell*, 2017 | human brain organoids: centrosome perturbation, premature progenitor differentiation → progenitor depletion / cortical thinning | `neural_progenitor_centrosome_spindle_dysfunction`, `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |
| [27279226](https://pubmed.ncbi.nlm.nih.gov/27279226/) | The Brazilian Zika virus strain causes birth defects in experimental models. | Cugola FR et al., *Nature*, 2016 | **mixed-model**: human organoids **and** mouse / non-human-primate models. Split evidence items so the organoid arm is `IN_VITRO` and the in-vivo arm is `MODEL_ORGANISM`. | `viral_neural_progenitor_cytopathy`, `Congenital_Zika_Syndrome` |

---

## Adjacent ZIKV references that are **not** NAMs (boundary check)

These appear in the same ZIKV evidence base but must **not** be tagged
`IN_VITRO` — they are listed here so curators don't misclassify them when reusing
the cluster's citations.

| PMID | Verified title (from cache) | First author / journal / year | Correct `evidence_source` | Why |
|------|------------------------------|-------------------------------|---------------------------|-----|
| [27179424](https://pubmed.ncbi.nlm.nih.gov/27179424/) | Zika Virus Disrupts Neural Progenitor Development and Leads to Microcephaly in Mice. | Li C et al., *Cell Stem Cell*, 2016 | `MODEL_ORGANISM` | in vivo mouse model (despite the journal), not a stem-cell/organoid system |
| [26862926](https://pubmed.ncbi.nlm.nih.gov/26862926/) | Zika Virus Associated with Microcephaly. | Mlakar J et al., *N Engl J Med*, 2016 | `HUMAN_CLINICAL` | human fetal autopsy case, not an in-vitro model |
| [24388750](https://pubmed.ncbi.nlm.nih.gov/24388750/) | Microcephaly-associated protein WDR62 regulates neurogenesis through JNK1 in the developing neocortex. | Xu D et al., *Cell Rep*, 2014 | `MODEL_ORGANISM` | in vivo developing-neocortex study; cited in MCPH/centrosome context but not a NAM |

---

## Rescue-branch modeling reminder

Where an organoid experiment **reverses** a phenotype, model the rescue as
mechanistic evidence on the perturbed causal branch, **not** as a treatment,
unless separate clinical evidence exists:

- chromosome-17 compensation rescues bRG mitotic delay — Bershteyn 28111201
- Wnt activation rescues premature neurogenesis in MDS organoids — Iefremova 28380362
- TLR3 inhibition reduces ZIKV-induced organoid volume loss — Dang 27162029

---

## Not yet mapped (open follow-ups for this issue)

The following Romero clusters from #4100 are **not** asserted here because no
single PMID could be identity-verified against the cache in this pass. Resolve
each with `just fetch-reference` + cached-title confirmation before citing:

- Neural rosette / neural-precursor model papers `[285–287]`.
- The remaining individual cerebral-organoid corticogenesis / single-cell
  validation papers in `[288–291]` beyond Lancaster 23995685 (e.g. organoid
  single-cell transcriptomic validation of corticogenesis pathways).
- Any additional ZIKV `[309–311]` papers (e.g. further AXL / Sofosbuvir rescue
  reports) beyond the seven verified above.

When these are verified, append them to the relevant table above with the same
columns and the same cached-title-confirmation standard.
