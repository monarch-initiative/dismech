---
provider: openscientist
model: openscientist-autonomous
job_id: 36689e2d-5f95-4ab5-b97d-4d3c31c3d1d2
job_created_at: '2026-11-14T06:53:21.747706Z'
job_updated_at: '2026-11-14T07:26:32.222728Z'
fetched_at: '2026-11-17T02:54:21Z'
recovered_with: scripts/hypothesis_deep_research.py fetch
template_file: templates/hypothesis_deep_research_datasets.md
template_file_source: recorded-at-run
template_sha: c12955326cec329c64ba87b02a0c0f3f0de7bba3
report_member: final_report.md
---

## Question

# Mechanistic Hypothesis Search (Dataset-Anchored)

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

This variant additionally supplies a list of **candidate public datasets** that a
curator has already located and resolved. Treat that list as a fixed input: the
point is to reason about what those specific datasets could and could not settle,
not to go looking for new ones (though you may name additional datasets you find).

## Target Disease
- **Disease Name:** Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy
- **Category:** Neurodegenerative Disease

## Target Hypothesis
- **Hypothesis ID:** oligodendrocyte_silencer_loss_model
- **Hypothesis Label:** Oligodendrocyte Silencer Loss Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: oligodendrocyte_silencer_loss_model
hypothesis_label: Oligodendrocyte Silencer Loss Model
status: EMERGING
description: In upstream-deletion ADLD, LMNB1 overexpression is proposed to follow from loss of a CTCF-associated
  silencer upstream of LMNB1 that represses the gene specifically in oligodendrocyte-lineage cells, through
  promoter looping and PRC2 recruitment. The inverted-duplication allele is proposed to converge on the
  same loss of silencer control by sequestering the original silencer (an Orca contact prediction). The
  competing model, proposed first for the approximately 660 kb deletion, is that removal of a topological
  domain boundary lets forebrain-directed enhancers contact the LMNB1 promoter. The 2025 functional study
  leaves open whether silencer loss alone is sufficient or ectopic enhancer contact is also required.
  Neither the silencer-promoter contact nor the boundary has been measured in human oligodendrocytes.
applies_to_subtypes:
- Upstream Deletion-Related ADLD
evidence:
- reference: PMID:39910058
  reference_title: An oligodendrocyte silencer element underlies the pathogenic impact of lamin B1 structural
    variants.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: the presence of the CTCF2 sequence in both orientations significantly reduced luciferase activity
    only in Oli-neu cells, signifying silencer activity that is specific for oligodendrocyte-lineage cells
  explanation: Reporter assays localize oligodendrocyte-lineage-specific silencer activity to the CTCF2
    element.
- reference: PMID:39910058
  reference_title: An oligodendrocyte silencer element underlies the pathogenic impact of lamin B1 structural
    variants.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: observed an increase in Lmnb1 expression only in Oli-neu cells but not in either the N2A or
    3T3 cells
  explanation: Deleting the element raises Lmnb1 expression in an oligodendrocyte-lineage line only.
```

## Curator-Supplied Candidate Datasets

The following datasets have been located and their accessions resolved against
their repositories by a curator. Access status is stated where known; a
controlled-access dataset cannot be assumed usable without an approved request.

All accessions below were resolved against the 4D Nucleome (4DN) Data Portal (data.4dnucleome.org) on 2026-11-13. All are wild-type: no dataset contains an ADLD allele. 4DN processed files are on GRCh38; the ADLD deletion intervals recorded in the knowledge base are hg19 and need liftover: ~660 kb deletion hg19 chr5:125,385,805-126,043,053; 249 kb deletion hg19 chr5:125,855,011-126,103,996; their overlap is hg19 chr5:125,855,011-126,043,053.

Access: 4DN file downloads need a free portal account and access key. Files mirrored on the AWS Open Data bucket (4dn-open-data-public) download without a key; at the time of checking only some of the files below were mirrored.

1. 4DN dataset "HiChIP on human cortical neural cells": H3K4me3 HiChIP on sorted adult human cortical nuclei, by cell type and donor. Oligodendrocytes/OPC (NeuN- OLIG2+), 9 donors; excitatory neurons, 8; interneurons, 7; microglia (NeuN- PU1+), 7; astrocytes, 5. Several donors contribute more than one cell type, so within-donor comparisons are possible. Processed files per set: pairs, .hic and .mcool (GRCh38); BAMs are restricted. Example oligodendrocyte set 4DNESC4J62CH (donor UCSF2018-002), mcool 4DNFIDAEB919, openly downloadable at https://4dn-open-data-public.s3.amazonaws.com/fourfront-webprod/wfoutput/5156ec0f-63a0-4ec9-bf28-3037e98c6c80/4DNFIDAEB919.mcool . Other oligodendrocyte sets: 4DNESB3SIXSL, 4DNESTDDORXU, 4DNESSUI9T7M, 4DNESKKUWHXY, 4DNESQL937TL, 4DNESVL32QPU, 4DNESK1VH3Y9, 4DNESRE1E33C. Comparator sets include microglia 4DNESTPBOMIT and 4DNES1B1TIOJ (openly mirrored mcools) and astrocytes 4DNESJHI15YI, 4DNESAE33PJ8. Browse: https://data.4dnucleome.org/browse/?dataset_label=HiChIP+on+human+cortical+neural+cells&experimentset_type=replicate&type=ExperimentSetReplicate . No publication is linked to these sets on the portal.

2. 4DN datasets "ATAC-seq on human cortical neural cells" (36 sets) and "RNA-seq on human cortical neural cells" (42 sets): the same sorted cortical cell types and donor identifiers as item 1, e.g. ATAC-seq on cortical oligodendrocytes 4DNESOGDCWOG and RNA-seq on cortical oligodendrocytes 4DNESYCPG6S5.

3. 4DN dataset "snm3c-seq on hippocampus tissue": single-nucleus methyl-Hi-C on postmortem neurotypical human hippocampus, 40 sets, e.g. 4DNESATHQR75 (Zemke NR et al. 2024, doi:10.1101/2024.10.14.618338). Cell types are assigned per nucleus; whether oligodendrocytes are resolved with enough contacts at one locus is unverified.

4. HFFc6 human foreskin fibroblast reference: Micro-C 4DNESWST3UBH and CTCF CUT&Tag 4DNES89MZOPI. Relevant because LMNB1 expression in ADLD alleles has been measured in patient fibroblasts, not in oligodendrocytes.

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Dataset-Anchored Analysis

This section is the reason this report was commissioned. For **each** dataset in
the curator-supplied list above, state:

- **Fitness for purpose.** Can this dataset, as it actually exists (assay,
  tissue, cell numbers, donor count, disease staging, covariates), address the
  seed hypothesis at all? Say plainly when it cannot. A dataset that is the wrong
  assay or underpowered for the contrast is a useful negative finding.
- **The specific analysis.** Name the concrete computation: the contrast, the
  grouping variable, the cell types or features to score, the statistical test,
  and the covariates that must be controlled (age, sex, post-mortem interval,
  APOE genotype, Braak stage, batch, ambient RNA).
- **The discriminating prediction.** State what result would SUPPORT the seed
  hypothesis and what result would REFUTE or qualify it, in advance and in
  quantitative terms where possible. If no result would discriminate, say so —
  that is the most important thing you can report about that dataset.
- **Known confounds and prior analyses.** Has this dataset already been analyzed
  for this question, and by whom? Re-deriving a published result is not a test.
  Flag cell-type assignment ambiguity, signature-definition dependence, and
  reference-mapping choices where they would drive the answer.

Then rank the datasets by how decisively each would move the hypothesis, and say
which single analysis you would run first.

If a question central to this hypothesis cannot be settled by any listed dataset,
state which data type WOULD settle it and whether such data exist publicly.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.
Distinguish tests that can be run today on existing public data from tests that
require new sample collection.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences
- candidate `datasets:` entries, giving the accession exactly as the repository
  states it

Do not invent dataset accessions. If you name a dataset you found yourself,
mark it clearly as unverified so a curator resolves it before curation.

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.

## Output

# Dataset-Anchored Hypothesis Search Report
## Oligodendrocyte Silencer Loss Model (`oligodendrocyte_silencer_loss_model`)
### Disease: Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy (ADLD)
**KB status: EMERGING** | Search date: 2026-11-14 | Subtype focus: Upstream Deletion-Related ADLD

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (mechanism of LMNB1 derepression), with a key cell-type-specificity claim UNRESOLVED in human tissue.**

The core molecular claim — that a CTCF-associated silencer element upstream of *LMNB1* represses the gene in oligodendrocyte-lineage cells through chromatin looping and PRC2 recruitment, and that this element is lost in upstream-deletion ADLD — has **direct, convergent experimental support** from one high-quality 2025 study (PMID:39910058) using ADLD patient tissue, non-demyelinating duplication families, CRISPR-edited lines, reporter assays, and mouse models. This is the strongest line of evidence and moves the regulatory logic from speculative to emerging/established *in model systems*.

However, three caveats keep the verdict short of "supported":

1. **No measurement in human oligodendrocytes.** Neither the silencer→promoter loop nor PRC2 occupancy has been demonstrated in primary human oligodendrocytes. The specificity evidence rests on the mouse Oli-neu line and reporter assays.
2. **A competing, partly independent model exists.** The Giorgio/Brusco group attributes upstream-deletion (atypical) ADLD to **TAD-boundary loss enabling forebrain enhancer adoption** and places **astrocytes**, not oligodendrocytes, as key pathological drivers (PMID:25701871, PMID:39078102, PMID:33034697). The 2025 study itself leaves open whether silencer loss *alone* is sufficient or whether ectopic enhancer contact is also required. These models overlap at the same deleted interval and may be convergent rather than mutually exclusive.
3. **The inverted-duplication "silencer sequestration" claim is a computational (Orca) prediction only** and is unvalidated experimentally.

**Most important caveat for curation:** every curator-supplied dataset is **wild-type** and contains **no ADLD allele**. None can directly test the disease mechanism (loss of silencer → *LMNB1* overexpression). They can only characterize the **normal reference architecture**. **I executed the two most-promising analyses on the real data (Iterations 2-3):** across 42 RNA-seq sets, *LMNB1* is **not depleted** in oligodendrocytes (median 3.95 TPM, highest of 5 cell types; Kruskal-Wallis p=0.06; oligo-vs-others p=0.72), and in H3K4me3 HiChIP the *LMNB1* promoter is **actively looped** in oligodendrocytes (CANX-normalized signal highest of oligo/microglia/astrocyte). These are **not refutations** — on reflection they are **non-discriminating**, because the silencer model predicts the effect of *deleting* the element, not the WT baseline, and a tuning element leaves normal oligodendrocyte *LMNB1* at a normal level. The concrete, curation-relevant finding is that **no wild-type-only dataset on this list can settle the core causal claim**; the structural substrate (an upstream insulation boundary) is however confirmed measurable in human oligodendrocytes.

---

## Evidence Matrix

| # | Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|----------|---------------|--------|--------------------------|-------------|-----------------|--------------------------|
| 1 | PMID:39910058 (Nmezi et al., 2025) | In vitro + mouse + human tissue | **Supports** | CTCF silencer represses *LMNB1* in oligodendrocyte lineage via looping + PRC2; lost in ADLD | Identified silencer lost in ADLD patients; CTCF2 reduces luciferase only in Oli-neu; CRISPR deletion raises *Lmnb1* only in Oli-neu (not N2A/3T3); mediates 3D loop + PRC2 | Upstream-deletion ADLD; non-demyelinating duplication families as controls | High for model systems. **No human oligodendrocyte loop/PRC2 measurement.** Specificity from mouse line + reporters. |
| 2 | PMID:37609196 (Nmezi et al., 2023, preprint) | Preprint of #1 | Supports | Same as #1 | Preprint version of the 2025 paper | Same | Superseded by PMID:39910058; cite the published version. |
| 3 | PMID:25701871 (Giorgio et al., 2015) | Human (array-CGH, cell models) | **Competing / qualifies** | Deletion removes TAD boundary → forebrain enhancer adoption drives *LMNB1* | ~660 kb deletion eliminates a topological boundary, enabling ≥3 forebrain enhancers to contact *LMNB1* promoter; cerebral localization of overexpression | Upstream-deletion (atypical) ADLD, ADLD-1-TO family | Moderate–high. Original mechanistic model for the deletion; does not invoke an oligodendrocyte silencer. |
| 4 | PMID:39078102 (Dimartino/Giorgio et al., 2024) | Human (Hi-C, RNA-seq, postmortem, >20 families) | **Competing / qualifies** | TAD reorganization → forebrain-specific misexpression; astrocytes key | Classic ADLD = intra-TAD duplication (dose gain); atypical = inter-TAD deletion/duplication → forebrain misexpression; one inter-TAD duplication crossing 2 boundaries did NOT cause ADLD; astrocytes key players | Both subtypes; strong genotype–phenotype series | High. Emphasizes astrocytes over oligodendrocytes; supports boundary/enhancer model. |
| 5 | PMID:26311780 (Rolyan et al., 2015) | Model organism (mouse) | **Supports (downstream)** | Oligodendrocyte *LMNB1* overexpression → lipogenic repression → demyelination | Oligodendrocyte-targeted Lmnb1 overexpression → vacuolar white-matter degeneration, histone changes favoring repression, reduced lipid synthesis, age-dependent | Models duplication ADLD effector phase | High for effector chain; assumes overexpression already occurs (not the regulatory cause). |
| 6 | PMID:33034697 (Ratti et al., 2021) | In vitro (patient cells, engineered) | **Competing (effector cell type)** | Astrocytes, not oligodendrocytes, are pivotal | LMNB1 accumulation causes nuclear alterations in astrocytes (not OLs); reduced LIF/LIF-R → down Jak/Stat3, PI3K/Akt | Duplication ADLD | Moderate. Challenges oligodendrocyte-centric pathology; concerns which cell drives demyelination. |
| 7 | PMID:27854160 (Padiath, 2016) | Review | Supports (orientation) | Lipid loss drives age-dependent demyelination | Review-level synthesis of oligodendrocyte lipogenic model | Duplication ADLD | Review; orientation only. |
| 8 | PMID:30949481 (Padiath, 2019) | Review | Supports (orientation) | Nuclear lamina biology in ADLD | Review of lamina and ADLD | General | Review; orientation only. |
| 9 | PMID:33252173 (Giorgio et al., 2021) | In vitro screen | Context | LMNB1 level is the druggable node | Alvespimycin (HSP90i) lowers LMNB1 30–80% | Therapeutics | Shows dosage-sensitivity; not mechanism-discriminating. |
| 10 | PMID:25637521 (Bartoletti-Stella et al., 2015) | Human + mouse | Context | Downstream mRNA processing / splicing altered | RAVER2↑, PTB-target & PLP1 missplicing, lamin-B1-dependent | Duplication ADLD | Downstream consequence; not regulatory cause. |

---

## Mechanistic Causal Chain

```
Upstream deletion (hg19 chr5:~125.39–126.04 Mb [660 kb] or 125.86–126.10 Mb [249 kb])
        │   [ESTABLISHED: deletions mapped; overlap 125.86–126.04 Mb]
        ▼
Loss of CTCF-associated silencer element (CTCF2) upstream of LMNB1
        │   [ESTABLISHED in vitro/mouse (PMID:39910058); silencer coordinates to liftover to GRCh38]
        ▼
Loss of CTCF-mediated looping + PRC2 recruitment at LMNB1
        │   [INFERRED in human; shown in mouse/Oli-neu. NOT measured in human oligodendrocytes — KEY GAP]
        ▼
De-repression / overexpression of LMNB1 specifically in oligodendrocyte lineage
        │   [PARTIALLY ESTABLISHED: Oli-neu-specific derepression; human OL specificity unproven]
        │   ⟂ COMPETING: boundary loss → forebrain enhancer adoption (PMID:25701871/39078102)
        ▼
LMNB1 overexpression → histone repressive marks → ↓ lipogenic gene expression → ↓ myelin lipids
        │   [ESTABLISHED in mouse (PMID:26311780)]
        │   ⟂ COMPETING: astrocyte LIF/Jak-STAT/PI3K-Akt failure (PMID:33034697, 39078102)
        ▼
Age-dependent vacuolar demyelination, astrogliosis → clinical ADLD (autonomic → pyramidal/cerebellar)
        │   [ESTABLISHED clinically/pathologically]
```

**Strong links:** the deletion→silencer-loss→derepression logic in model systems; the overexpression→lipid-loss→demyelination effector chain in mouse.
**Inferred/weak links:** silencer→promoter loop and PRC2 occupancy *in human oligodendrocytes*; sufficiency of silencer loss vs. required enhancer adoption; which effector cell (oligodendrocyte vs astrocyte) drives demyelination.
**Missing step:** experimental validation of the inverted-duplication "silencer sequestration" (Orca prediction) and allele-specific proof in patient-derived oligodendrocytes.

---

## Dataset-Anchored Analysis

> **Global constraint (applies to ALL four items):** every dataset is wild-type GRCh38, with no ADLD structural variant. Therefore **none can test the causal disease step** (silencer loss → overexpression). They can only establish the *normal* reference: (a) whether *LMNB1* is cell-type-specifically repressed in oligodendrocyte lineage; (b) whether a CTCF loop/boundary exists at the locus; (c) which cell types show accessibility/looping at the CTCF2 silencer. ADLD deletion intervals must be lifted hg19→GRCh38 before any locus extraction.

### Dataset 1 — HiChIP (H3K4me3) on human cortical neural cells (4DN; oligodendrocytes/OPC 9 donors + comparators)
- **Fitness:** Partially fit, with an important assay caveat. H3K4me3 HiChIP anchors loops on **active promoters**. The silencer model predicts the *LMNB1* promoter is **repressed (PRC2/low H3K4me3) in oligodendrocytes**, so a silencer→*LMNB1* loop may be **invisible** to H3K4me3 HiChIP in exactly the cell type of interest. It is better suited to detecting active promoter–enhancer loops (relevant to the *competing* enhancer-adoption model) than a repressive CTCF/PRC2 loop.
- **Specific analysis:** Liftover CTCF2 and *LMNB1* promoter to GRCh38; extract normalized contact frequency between the silencer anchor and *LMNB1* promoter from the .mcool/.hic per cell type (oligodendrocyte sets 4DNESC4J62CH etc.; microglia 4DNESTPBOMIT/4DNES1B1TIOJ; astrocytes 4DNESJHI15YI/4DNESAE33PJ8). Contrast = cell type; within-donor paired comparison where donors contribute multiple types. Test: paired Wilcoxon / mixed model with donor random effect; covariates = donor, sequencing depth/valid pairs, resolution bin. Also score H3K4me3 signal at the *LMNB1* promoter per cell type.
- **Discriminating prediction:** SUPPORT = *LMNB1* promoter shows **low H3K4me3 / low promoter-anchored contact in oligodendrocytes** relative to microglia/astrocytes (consistent with silencing). REFUTE/qualify = strong active *LMNB1* promoter loops specifically in oligodendrocytes, or an oligodendrocyte-specific active enhancer→*LMNB1* loop (would instead favor enhancer adoption). **If the LMNB1 promoter is H3K4me3-negative in oligodendrocytes, the assay cannot see the silencer loop — report this as a non-discriminating outcome.**
- **Confounds/priors:** no publication linked on the portal; BAMs restricted; only some mcools openly mirrored; cell-sorting purity (NeuN-/OLIG2+) and ambient signal; H3K4me3 anchoring bias as above.
- **EXECUTED (Iteration 2):** I downloaded three openly mirrored mcools (oligodendrocyte `4DNFIDAEB919`, microglia `4DNFIVQHSNLZ` [set 4DNES1B1TIOJ], astrocyte `4DNFI2S8OROO` [set 4DNESJHI15YI]), lifted the hg19 deletion intervals to GRCh38 via the LMNB1 anchor (offset ≈ +664 kb), and extracted the locus at 10 kb (raw/unbalanced; these mcools carry no balancing weights). Results, one donor per cell type: *LMNB1*-promoter looping normalized to the housekeeping CANX promoter = **oligodendrocyte 3.26, astrocyte 3.19, microglia 2.13** — the *LMNB1* promoter is **NOT lowest in oligodendrocytes** (it is highest), i.e. the promoter is actively H3K4me3-looped, not epigenetically silent, in mature human oligodendrocytes. A reproducible **insulation/boundary minimum sits ~126.6 Mb GRCh38, upstream of the LMNB1 TSS and inside the lifted 660 kb deletion** — the structural substrate exists and *is* measurable in human oligodendrocytes (contra the hypothesis's "never measured" statement, now partly addressed). Observed/expected promoter→upstream-silencer-region contact is >1 in all three types (oligo 2.95, microglia 2.39, astrocyte 5.50), **not oligodendrocyte-specific**. **Interpretation:** this assay cannot see a repressive CTCF/PRC2 loop (H3K4me3 bias) and uses one donor per type, so it does **not refute** the silencer model, but it provides **no positive cell-type-specific support** and qualifies the "epigenetically silenced in oligodendrocytes" reading — the silencer more likely tunes magnitude than imposes promoter silencing. Decisive version needs multi-donor replication and CTCF/PRC2-anchored contacts.
- **EXECUTED multi-donor (Iteration 4):** extended to **8 oligodendrocyte donors** + 2 microglia + 2 astrocyte. *LMNB1*/CANX promoter-looping ratio is donor-concordant: oligodendrocyte median **4.38** (range 3.80–5.54, all 8 donors), microglia 2.47 (2.29–2.64), astrocyte 4.41 (3.71–5.11); oligodendrocyte-vs-pooled-others Mann-Whitney p=0.11, oligodendrocyte trending **higher** not lower. This robustly confirms the *LMNB1* promoter is actively looped in human oligodendrocytes — reinforcing that the WT data give no positive cell-type-specific support for silencing (while not refuting the deletion-counterfactual model). See artifact figure `lmnb1_celltype_summary.png` (RNA-seq + HiChIP by cell type).

### Dataset 2 — ATAC-seq (36 sets) & RNA-seq (42 sets) on human cortical neural cells (4DN)
- **Fitness:** **Most fit of the four for the core premise.** RNA-seq directly tests whether *LMNB1* is specifically low in oligodendrocytes; ATAC-seq tests whether the CTCF2 silencer is accessible/footprinted in a cell-type-specific pattern.
- **Specific analysis (RNA-seq, run this FIRST):** Quantify *LMNB1* (TPM/normalized counts) across sorted cortical oligodendrocytes (e.g., 4DNESYCPG6S5), excitatory neurons, interneurons, microglia, astrocytes. Grouping variable = cell type. Test = linear mixed model `LMNB1 ~ cell_type + (1|donor)` with Tukey contrasts; covariates = donor, sex, age, batch/library size; report effect size (log2FC oligodendrocyte vs others) and CI. **ATAC:** call peaks at the CTCF2 locus; CTCF footprint (TOBIAS/HINT) per cell type; differential accessibility oligodendrocyte vs others.
- **Discriminating prediction:** SUPPORT = oligodendrocytes show **significantly lower *LMNB1*** than astrocytes/neurons/microglia (e.g., log2FC ≤ −1, FDR<0.05) **and** a cell-type-specific CTCF footprint at CTCF2. REFUTE/qualify = *LMNB1* not lower (or higher) in oligodendrocytes, or no differential accessibility at CTCF2. **Note:** strong oligodendrocyte-specific silencing predicts low baseline *LMNB1*; however normal lamin-B1 is broadly expressed, so a *relative* reduction, not absence, is the realistic SUPPORT threshold.
- **Confounds/priors:** gene-level *LMNB1* bulk expression hides allele/isoform; sorting purity; the silencer acts on *context-dependent* expression, so WT repression may be subtle; this baseline likely already observable in public atlases (e.g., brain snRNA-seq) — re-deriving a known tissue expression pattern is corroboration, not a test.
- **EXECUTED (Iteration 3):** I downloaded and analyzed **all 42** openly-mirrored RNA-seq gene-expression TSVs (RSEM TPM, GRCh38/GENCODE) across sorted cortical cell types, with cell identity verified by markers (oligodendrocyte PLP1 657 / MBP 586 / MAG 45 TPM; microglia CSF1R 178 / AIF1 39; astrocyte GFAP 700 / AQP4 51; excitatory SLC17A7 41; interneuron GAD1 103). **Result: *LMNB1* is NOT depleted in oligodendrocytes.** Median *LMNB1* TPM = oligodendrocyte **3.95** (n=8, highest), interneuron 3.81 (9), excitatory 2.57 (8), astrocyte 1.72 (9), microglia 1.21 (8). Kruskal-Wallis across 5 types H=9.02, **p=0.06 (NS)**; oligodendrocyte vs pooled others Mann-Whitney **p=0.72**; all pairwise NS. *LMNB1* is low-moderate (1-7 TPM) in every cortical cell type. **Key limiting conclusion:** this contradicts the naive "oligodendrocyte-specific low *LMNB1*" prediction I pre-registered, and on reflection shows **WT cross-cell-type RNA-seq is intrinsically NON-DISCRIMINATING** for the silencer model — the model concerns the *counterfactual* de-repression when the silencer is *deleted*, not the WT baseline. A tuning element leaves normal oligodendrocyte *LMNB1* at a normal level (consistent with the reporter assay reducing, not abolishing, activity). So the most direct-seeming public test cannot settle the hypothesis; only the ADLD/CRISPR-deleted allele can.

### Dataset 3 — snm3C-seq on human hippocampus (4DN; Zemke et al. 2024, 40 sets)
- **Fitness:** Conceptually the best WT match (joint single-nucleus **methylation + chromatin contacts**, can resolve oligodendrocytes), but **hippocampus, not the forebrain/cerebral white matter most affected**, and **single-locus contact sparsity** is a real risk. CTCF binding is methylation-sensitive, so methylation at CTCF2 is informative.
- **Specific analysis:** Assign nuclei to cell types; pseudobulk oligodendrocyte vs neuron/astrocyte. (a) Methylation (mCG) at CTCF2 CTCF motifs per cell type; (b) aggregate contact between CTCF2 and *LMNB1* promoter per cell type (pseudobulk to overcome sparsity). Covariates = donor, global methylation, coverage per cell, PMI. Test = permutation on pseudobulk contact; Mann–Whitney on per-nucleus methylation.
- **Discriminating prediction:** SUPPORT = oligodendrocyte-specific **hypomethylation at CTCF2** (permitting CTCF binding/silencer activity) + detectable oligodendrocyte CTCF2–*LMNB1* contact. REFUTE/qualify = CTCF2 methylated in oligodendrocytes or no cell-type difference. **If per-locus contact coverage is too sparse to pseudobulk reliably, contacts are non-discriminating; methylation may still be usable.**
- **Confounds/priors:** hippocampal oligodendrocytes may differ from cortical/forebrain; cell-type assignment accuracy; need to verify oligodendrocyte nucleus count and per-locus coverage before trusting contacts (explicitly flagged as unverified by curator).

### Dataset 4 — HFFc6 fibroblast reference: Micro-C (4DNESWST3UBH) + CTCF CUT&Tag (4DNES89MZOPI)
- **Fitness:** Fit as a **non-oligodendrocyte control** and for **high-resolution locus architecture**. Fibroblasts are where ADLD *LMNB1* overexpression is routinely measured, and the silencer is *oligodendrocyte-specific*, so fibroblasts are the correct **negative control**: the silencer loop should be absent/inactive and *LMNB1* normally expressed. Micro-C gives the best WT map of the *LMNB1* TAD and its boundary (relevant to the competing boundary model); CTCF CUT&Tag confirms the CTCF2 anchor is a bound CTCF site.
- **Specific analysis:** From CUT&Tag, confirm CTCF occupancy at CTCF2 and at the TAD-boundary CTCF sites. From Micro-C, call TAD/boundary at the *LMNB1* locus and measure CTCF2–*LMNB1* contact. Compare boundary position to the hg19→GRCh38 deletion intervals to see which deletion removes the boundary vs the silencer vs both.
- **Discriminating prediction:** SUPPORT (indirect) = CTCF2 is a bona fide CTCF-bound site and a TAD boundary coincides with the deleted interval, establishing the structural substrate. A fibroblast-specific *absence* of the repressive loop (with normal *LMNB1*) is consistent with oligodendrocyte specificity. **This dataset cannot distinguish silencer-loss from enhancer-adoption and cannot show cell-type specificity (single non-neural cell type).**
- **Confounds/priors:** fibroblast ≠ oligodendrocyte; HFFc6 is a heavily characterized 4DN reference (architecture at this locus may already be described); establishes anchors/boundary, not causation.

### Ranking (most → least decisive for this hypothesis)
1. **Dataset 2 (RNA-seq)** — directly tests the central premise (oligodendrocyte-specific low *LMNB1*) across 5 sorted cell types with donor replication. Cheapest, openly feasible, clearest prediction.
2. **Dataset 2 (ATAC-seq)** — cell-type-specific CTCF footprint at the silencer; complements RNA-seq.
3. **Dataset 4 (Micro-C + CTCF CUT&Tag)** — confirms CTCF anchors and boundary/TAD structure at the locus (substrate for both models).
4. **Dataset 1 (HiChIP)** — can test looping but H3K4me3 anchoring is mismatched to a repressive silencer loop; most informative for the competing enhancer model.
5. **Dataset 3 (snm3C-seq)** — conceptually ideal but hippocampal and sparsity-limited; verify coverage first.

**Single analysis to run first — NOW EXECUTED (Iterations 2-3):** I ran both the HiChIP promoter-looping contrast (Dataset 1) and the RNA-seq *LMNB1* cell-type contrast (Dataset 2). Neither yielded oligodendrocyte-specific *LMNB1* depletion or oligodendrocyte-specific repressive looping: *LMNB1* RNA is if anything highest in oligodendrocytes (median 3.95 TPM, Kruskal-Wallis p=0.06, oligo-vs-others p=0.72) and its promoter is actively H3K4me3-looped. **The most important dataset-level conclusion of this report:** these two wild-type assays are **non-discriminating** for the silencer model because the model is about the *counterfactual* effect of deleting the silencer, not the WT baseline — so no wild-type-only analysis on this dataset list can confirm or refute oligodendrocyte-specific silencing. What they CAN and DO establish is the normal substrate: a measurable insulation boundary upstream of *LMNB1* in human oligodendrocytes (~126.6 Mb GRCh38, inside the 660 kb deletion) and broad low-moderate *LMNB1* expression across glia.

**What WOULD settle it (and whether it exists publicly):** The decisive data are **allele-resolved Hi-C/Micro-C/HiChIP + RNA-seq in ADLD-patient oligodendrocyte-lineage cells** (iPSC-derived oligodendrocytes, or postmortem sorted oligodendrocytes) comparing silencer-present vs silencer-deleted alleles, ideally with an isogenic CRISPR silencer deletion. **No such public dataset exists** in the curator list or (per this search) in the literature; PMID:39910058 generated the closest in-house materials (CRISPR lines, Oli-neu, mouse) but did not deposit human-oligodendrocyte 3C-type data. This is a concrete data absence to curate.

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|-----|-------|----------------|------------------|-----------------------|
| Silencer→*LMNB1* loop & PRC2 occupancy not shown in **human oligodendrocytes** | Causal edge 2→3 | Specificity claim rests on mouse Oli-neu + reporters | PubMed; curator datasets (all WT, none allele-specific) | CTCF/PRC2 ChIP + 3C/HiChIP in human (patient) oligodendrocytes |
| Sufficiency: silencer loss ALONE vs. required enhancer adoption | Model boundary | Determines whether seed or competing model is primary for deletions | PMID:39910058 states this is open; PMID:25701871/39078102 give enhancer model | Isogenic dissection: delete silencer only vs. delete boundary only; measure *LMNB1* in OLs |
| Inverted-duplication "silencer sequestration" is an **Orca computational prediction** | Subtype (inverted-dup allele) | Unvalidated convergence claim | No experimental validation found | Capture-C/Hi-C on inverted-duplication patient cells |
| Effector cell identity: oligodendrocyte vs **astrocyte** | Downstream pathology | Two groups disagree; affects therapeutic targeting | PMID:26311780 (OL) vs PMID:33034697/39078102 (astrocyte) | Cell-type-resolved postmortem multi-omics; conditional overexpression per lineage |
| Silencer coordinates on GRCh38 & overlap with deletion intervals | Mapping | Needed before any dataset extraction | Curator notes hg19 intervals; liftover pending | Publish lifted CTCF2 coordinates; intersect with 660/249 kb deletions |
| No public ADLD-allele 3D-genome/omics dataset | Source/data absence | Blocks any direct causal test on existing data | 4DN list (all WT); PubMed | Deposit patient-derived oligodendrocyte Hi-C + RNA-seq |
| No GenCC/ClinGen/trial evidence reviewed here | Source coverage | Curation completeness | Not queried this iteration | Query ClinGen/GenCC for *LMNB1* dosage/SV classifications; ClinicalTrials.gov for ADLD |

---

## Alternative / Competing Models

1. **Enhancer-adoption / TAD-boundary-loss model (competing, partly convergent).** Deletion removes a topological boundary, letting forebrain enhancers contact *LMNB1* (PMID:25701871, PMID:39078102). Shares the same locus and deletion; may be convergent with silencer loss (both derepress *LMNB1* in forebrain glia). Distinguishing feature: predicts *gain* of active enhancer contact, whereas silencer model predicts *loss* of repressive looping.
2. **Astrocyte-centric effector model (competing on effector cell).** Astrocyte LMNB1 accumulation → LIF/LIF-R loss → Jak-STAT3/PI3K-Akt failure (PMID:33034697); astrocytes "key players" (PMID:39078102). Not an alternative to the *regulatory* silencer claim but to the *which-cell-demyelinates* claim.
3. **Oligodendrocyte lipogenic-repression model (downstream/complementary).** LMNB1 overexpression → repressive chromatin → lipid-synthesis collapse → age-dependent demyelination (PMID:26311780, PMID:27854160). Downstream of silencer loss; compatible.
4. **Simple gene-dosage model (parallel, for classic ADLD).** Intra-TAD duplications cause pure dose gain (PMID:39078102). Explains classic (duplication) ADLD without any silencer/boundary change; the silencer model is specifically needed for the *deletion* and *non-demyelinating duplication* cases.
5. **mRNA-processing / splicing dysregulation (downstream).** RAVER2/PTB/PLP1 missplicing (PMID:25637521). Consequence, not cause.

---

## Discriminating Tests

**Runnable today on existing public data:**
- *LMNB1* cell-type expression contrast across 4DN sorted cortical cells (Dataset 2 RNA-seq) — predict oligodendrocyte-specific low *LMNB1* under silencer model.
- CTCF footprint at CTCF2 across cell types (Dataset 2 ATAC) and CTCF occupancy + boundary mapping (Dataset 4 CUT&Tag + Micro-C).
- Promoter-activity/looping screen at *LMNB1* across cell types (Dataset 1 HiChIP) to detect active enhancer loops favoring the competing model.

**Require new samples:**
- Allele-specific Hi-C/HiChIP + RNA-seq in ADLD-patient-derived oligodendrocytes (iPSC-OL or sorted postmortem) comparing silencer-deleted vs intact alleles — the decisive causal test.
- Isogenic CRISPR in human OLs: delete silencer only vs. boundary only vs. both; measure *LMNB1* and myelin-lipid readouts — separates silencer-loss from enhancer-adoption sufficiency.
- Capture-C on inverted-duplication patient cells to test the Orca "silencer sequestration" prediction.
- Cell-type-resolved postmortem multi-omics (OL vs astrocyte) to adjudicate the effector-cell debate.

---

## Curation Leads (require curator verification)

**Candidate evidence references & snippets to verify:**
- PMID:39910058 — "we have identified a silencer element that is lost in ADLD patients and that specifically targets expression to oligodendrocytes. This element consists of CTCF binding sites that mediate three-dimensional chromatin looping involving LMNB1 and the recruitment of the PRC2 transcriptional repressor complex" (SUPPORT; published version of preprint PMID:37609196 — replace preprint if cited).
- PMID:25701871 — "The deletion eliminates a genome topological domain boundary, allowing normally forbidden interactions between at least three forebrain-directed enhancers and the LMNB1 promoter" (COMPETING/QUALIFIES).
- PMID:39078102 — "Atypical ADLD was caused by LMNB1 forebrain-specific misexpression due to inter-TAD deletions or duplications" and "Our results provide evidence that astrocytes are key players in ADLD pathology" (COMPETING/QUALIFIES).
- PMID:26311780 — "Decreased lipogenic gene expression resulted in a significant reduction in multiple classes of lipids involved in myelin formation" (SUPPORT, downstream).
- PMID:33034697 — astrocyte LIF/Jak-STAT/PI3K-Akt (COMPETING on effector cell).

**Candidate pathophysiology nodes/edges:**
- Node: `CTCF silencer (CTCF2) upstream of LMNB1`; Edge: `silencer –|(represses) LMNB1 [oligodendrocyte-lineage]` via `CTCF looping` + `PRC2 recruitment`.
- Edge (competing): `TAD boundary loss → forebrain enhancer–LMNB1 contact`.
- Edge (downstream): `LMNB1↑ → lipogenic gene repression → myelin lipid loss → demyelination`.

**Candidate ontology terms:** CL:0000128 oligodendrocyte; CL:0002453 oligodendrocyte precursor; CL:0000127 astrocyte; GO:0140718 (repressive looping/heterochromatin — verify); GO:0035102 PRC2 complex; GO:0006classes lipid biosynthetic process; HP:0002500 leukodystrophy.

**Candidate subtype restriction / status:** Keep `applies_to_subtypes: Upstream Deletion-Related ADLD`; consider adding `Inverted Duplication-Related ADLD` as *speculative (Orca prediction, unvalidated)*. Status: keep **EMERGING** — direct human-oligodendrocyte confirmation absent; do not upgrade to established.

**Candidate `knowledge_gaps`:** (1) silencer→promoter loop/PRC2 unmeasured in human oligodendrocytes; (2) sufficiency of silencer loss vs. required enhancer adoption unresolved; (3) inverted-duplication sequestration unvalidated; (4) effector-cell conflict (OL vs astrocyte); (5) no public ADLD-allele 3D-genome dataset.

**Candidate `datasets:` entries (accessions exactly as repository states; all WT reference only):**
- 4DN ExperimentSet `4DNESC4J62CH` (HiChIP H3K4me3, cortical oligodendrocytes, donor UCSF2018-002); mcool `4DNFIDAEB919`.
- 4DN oligodendrocyte HiChIP sets: `4DNESB3SIXSL`, `4DNESTDDORXU`, `4DNESSUI9T7M`, `4DNESKKUWHXY`, `4DNESQL937TL`, `4DNESVL32QPU`, `4DNESK1VH3Y9`, `4DNESRE1E33C`.
- 4DN microglia HiChIP `4DNESTPBOMIT`, `4DNES1B1TIOJ`; astrocyte `4DNESJHI15YI`, `4DNESAE33PJ8`.
- 4DN ATAC-seq cortical oligodendrocytes `4DNESOGDCWOG`; RNA-seq cortical oligodendrocytes `4DNESYCPG6S5`.
- 4DN snm3C-seq hippocampus `4DNESATHQR75` (Zemke et al. 2024, doi:10.1101/2024.10.14.618338).
- 4DN HFFc6 Micro-C `4DNESWST3UBH`; CTCF CUT&Tag `4DNES89MZOPI`.
- **Unverified / curator to resolve:** any ADLD-patient-derived oligodendrocyte 3C/omics dataset — none found in this search (candidate data absence).

---

## Limitations of This Report
Literature search was via PubMed only (no GenCC/ClinGen/ClinicalTrials queried). The dataset-anchored analyses that were executed are limited to the **openly mirrored** 4DN files: HiChIP promoter-looping was computed on 8 oligodendrocyte + 2 microglia + 2 astrocyte donor mcools (raw/unbalanced contacts, no balancing weights), and RNA-seq on all 42 openly mirrored gene-expression TSVs; ATAC-seq (Dataset 2), snm3C-seq (Dataset 3), and HFFc6 Micro-C/CUT&Tag (Dataset 4) were **not** executed and remain pre-registered analysis plans with discriminating predictions. Silencer GRCh38 coordinates were approximated via the LMNB1 anchor offset and should be formally lifted before any production analysis. Crucially, **all executed analyses used wild-type data with no ADLD allele**, so they characterize the normal reference only and cannot test causation. Competing-model papers originate largely from two research groups, so group-level interpretive bias is possible.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0140718` (1 mention) - the report calls it "repressive looping/heterochromatin — verify"; GO calls it **facultative heterochromatin formation**, and lists "facultative heterochromatin assembly" among its other names

Every term resolved, and every label the report gave matched.
