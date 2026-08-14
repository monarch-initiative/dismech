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
| [26644564](https://pubmed.ncbi.nlm.nih.gov/26644564/) | Human cerebral organoids recapitulate gene expression programs of fetal neocortex development. | Camp JG et al., *Proc Natl Acad Sci U S A*, 2015 | cerebral organoid single-cell corticogenesis validation | already in repo cache (`IN_VITRO`); cited by `microtubule_dependent_neuronal_migration_failure` |
| [24277810](https://pubmed.ncbi.nlm.nih.gov/24277810/) | Self-organization of axial polarity, inside-out layer pattern, and species-specific progenitor dynamics in human ES cell-derived neocortex. | Kadoshima T et al., *Proc Natl Acad Sci U S A*, 2013 | hESC-derived 3D neocortex: self-organized axial polarity, inside-out layering, **species-specific (human) progenitor-zone dynamics** | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [26005811](https://pubmed.ncbi.nlm.nih.gov/26005811/) | Functional cortical neurons and astrocytes from human pluripotent stem cells in 3D culture. | Paşca AM et al., *Nat Methods*, 2015 | 3D cortical spheroid platform yielding functional cortical neurons **and astrocytes** (glial arm the 2013–2015 organoid protocols under-represent) | fetch-reference-verified 2026-07-29; not yet cited in the cluster |

> **Which platform paper to cite:** Lancaster 23995685 and Kadoshima 24277810 are
> the two independent 3D-corticogenesis platform anchors; Kadoshima is the better
> citation when the claim is specifically about **human-vs-rodent progenitor-zone
> dynamics** (it reports species-specific progenitor behaviour directly), and is
> therefore the natural platform reference behind a `HUMAN_MODEL_MISMATCH`
> discussion. Camp 26644564 anchors *molecular* fidelity to fetal neocortex;
> Paşca 26005811 anchors the astrocyte/glial readout.

---

## Neural rosette / neural-precursor models (Romero cluster `[285–287]`)

The review uses these for the claim that neural rosettes recapitulate
apical-basal polarity resembling neural-tube organization, and that neurospheres
model self-renewal but lack spatial organization. Cite them for **2D / early
neural-precursor** claims; they are weaker support than organoids for cortical
layering or radial-migration mechanisms (see the NAM hierarchy in #4100).

| PMID | Verified title (from cache) | First author / journal / year | NAM platform | Cited by (MCD cluster) |
|------|------------------------------|-------------------------------|--------------|------------------------|
| [11731781](https://pubmed.ncbi.nlm.nih.gov/11731781/) | In vitro differentiation of transplantable neural precursors from human embryonic stem cells. | Zhang SC et al., *Nat Biotechnol*, 2001 | foundational hESC → neural-precursor / rosette derivation | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [18198334](https://pubmed.ncbi.nlm.nih.gov/18198334/) | Human ES cell-derived neural rosettes reveal a functionally distinct early neural stem cell stage. | Elkabetz Y et al., *Genes Dev*, 2008 | neural rosettes as a discrete early neural-stem-cell stage (apical-basal polarity) | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [19252484](https://pubmed.ncbi.nlm.nih.gov/19252484/) | Highly efficient neural conversion of human ES and iPS cells by dual inhibition of SMAD signaling. | Chambers SM et al., *Nat Biotechnol*, 2009 | dual-SMAD-inhibition neural induction — the standard route to rosettes/NPCs used by most downstream MCD NAM studies | fetch-reference-verified 2026-07-29; not yet cited in the cluster |

> **Scope caveat:** a rosette or neurosphere result showing altered self-renewal
> or polarity supports a **progenitor-level** node only. Do not use it as
> evidence for a migration-primary or lamination-primary mechanism — that is
> exactly the progenitor-vs-migration ambiguity #4101 flags as an open knowledge
> gap.

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
| [27118425](https://pubmed.ncbi.nlm.nih.gov/27118425/) | Brain-Region-Specific Organoids Using Mini-bioreactors for Modeling ZIKV Exposure. | Qian X et al., *Cell*, 2016 | forebrain-specific organoids in mini-bioreactors: ZIKV preferentially infects NPCs, reduces proliferation, increases death, and thins the neuronal layer | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [27911847](https://pubmed.ncbi.nlm.nih.gov/27911847/) | Zika virus cell tropism in the developing human brain and inhibition by azithromycin. | Retallack H et al., *Proc Natl Acad Sci U S A*, 2016 | human astrocyte/NPC and organotypic fetal-brain tropism mapping; **azithromycin reduces ZIKV proliferation and cytopathic effect** | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [29020636](https://pubmed.ncbi.nlm.nih.gov/29020636/) | Self-Organized Cerebral Organoids with Human-Specific Features Predict Effective Drugs to Combat Zika Virus Infection. | Watanabe M et al., *Cell Rep*, 2017 | cerebral organoid screen identified **duramycin and ivermectin** as active hits; azithromycin was ineffective in this platform despite prior protection in cultured glial cells | fetch-reference-verified 2026-07-29; not yet cited in the cluster |
| [28098253](https://pubmed.ncbi.nlm.nih.gov/28098253/) | The clinically approved antiviral drug sofosbuvir inhibits Zika virus replication. | Sacramento CQ et al., *Sci Rep*, 2017 | **sofosbuvir rescue**: inhibits ZIKV replication in hepatoma (Huh-7) cells, neural stem cells, and brain organoids. All-in-vitro (no in-vivo arm) → `IN_VITRO`. | fetch-reference-verified 2026-07-29; not yet cited in the cluster |

> **Drug-rescue caveat (azithromycin, sofosbuvir):** these are *mechanistic*
> rescue results in NAM systems, not clinical evidence. Per #4100 they belong on
> the perturbed causal branch as `IN_VITRO` support, **not** in a `treatments:`
> block, unless separate clinical evidence for congenital Zika syndrome exists.
> Azithromycin's effect is platform-dependent: pair Retallack's supportive
> glial-cell result with Watanabe's refuting cerebral-organoid result rather than
> recording unqualified support.

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
- azithromycin reduces ZIKV proliferation/cytopathic effect in glial cell lines
  and human astrocytes — Retallack 27911847
- sofosbuvir inhibits ZIKV replication in neural stem cells and brain organoids —
  Sacramento 28098253
- duramycin and ivermectin reduce ZIKV infection in cerebral organoids, while
  azithromycin shows little activity — Watanabe 29020636

---

## Not yet mapped (open follow-ups for this issue)

The following Romero clusters from #4100 are **not** asserted here because no
single PMID could be identity-verified against the cache in this pass. Resolve
each with `just fetch-reference` + cached-title confirmation before citing:

- ~~Neural rosette / neural-precursor model papers `[285–287]`.~~
  **Resolved (2026-07-29):** three cache-verified anchors now recorded in the
  new "Neural rosette / neural-precursor models" table — Zhang 11731781,
  Elkabetz 18198334, Chambers 19252484.
- ~~The remaining individual cerebral-organoid corticogenesis / single-cell
  validation papers in `[288–291]` beyond Lancaster 23995685 (e.g. organoid
  single-cell transcriptomic validation of corticogenesis pathways).~~
  **Partially resolved (2026-06-30):** the canonical single-cell organoid
  corticogenesis-validation paper — Camp JG et al. 2015 (`PMID:26644564`,
  *Human cerebral organoids recapitulate gene expression programs of fetal
  neocortex development*) — was already cache-verified and already cited
  (`IN_VITRO`) in `microtubule_dependent_neuronal_migration_failure`; it is now
  recorded in the platform table above.
  **Extended (2026-07-29):** Kadoshima 24277810 (species-specific progenitor
  dynamics) and Paşca 26005811 (3D cortical neurons + astrocytes) added to the
  platform table. Any further `[288–291]` papers remain open.
- ~~Any additional ZIKV `[309–311]` papers (e.g. further AXL / Sofosbuvir rescue
  reports) beyond the seven verified above.~~
  **Resolved (2026-07-29):** four more cache-verified ZIKV NAM papers added —
  Qian 27118425, Retallack 27911847, Watanabe 29020636, Sacramento 28098253
  (the sofosbuvir rescue report the issue asked for). Exact Romero bracket
  indices are still not pinned (the reference list was not independently
  available); papers are assigned to the **cluster**, per the methodology note
  above.

Still open:

- Exact Romero bracket→PMID indices for the ZIKV and `[288–291]` clusters
  (paper *identity* is verified; bracket *number* is not).
- Neurosphere-specific `[285–287]` primary papers, as distinct from the
  rosette/NPC-induction anchors recorded above.

When these are verified, append them to the relevant table above with the same
columns and the same cached-title-confirmation standard.

---

## Verification log — recalled PMIDs that were **wrong**

Recorded because it is direct evidence for the CLAUDE.md rule that recalled or
review-summary PMIDs are leads, not ground truth. In the 2026-07-29 pass, two
confidently-recalled identifiers turned out to cite unrelated papers, and were
caught only by reading the cached title after `just fetch-reference`:

| Recalled as | Actual cached title | Correct PMID |
|---|---|---|
| `PMID:24145430` — Kadoshima 2013 hESC neocortex self-organization | *Plus-end tracking proteins, CLASPs, and a viral Akt mimic regulate herpesvirus-induced stable microtubule formation and virus spread.* | [24277810](https://pubmed.ncbi.nlm.nih.gov/24277810/) |
| `PMID:28445721` — Watanabe 2017 ZIKV organoid drug screen | *NACHO Mediates Nicotinic Acetylcholine Receptor Function throughout the Brain.* | [29020636](https://pubmed.ncbi.nlm.nih.gov/29020636/) |

Neither wrong PMID was ever written into a table; both were rejected at the
cached-title check. **Always read the cache before asserting a mapping.**
