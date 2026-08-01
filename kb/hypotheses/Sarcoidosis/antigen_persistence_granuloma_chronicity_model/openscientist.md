---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T02:57:30.725962'
end_time: '2026-07-26T03:11:42.451542'
duration_seconds: 851.73
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Sarcoidosis
  category: Immune
  hypothesis_group_id: antigen_persistence_granuloma_chronicity_model
  hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: antigen_persistence_granuloma_chronicity_model\n\
    hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model\n\
    status: EMERGING\napplies_to_subtypes:\n- Pulmonary Sarcoidosis\ndescription:\
    \ Sarcoidosis is modeled as a genetically conditioned, antigen-driven granulomatous\
    \ immune\n  response in which poorly degradable or repeatedly encountered antigens\
    \ are presented by macrophage-lineage\n  antigen-presenting cells to CD4+ T cells.\
    \ The activated T-cell compartment polarizes toward IFN-gamma-producing\n  Th17.1/Th1-like\
    \ effector states while regulatory T-cell restraint is insufficient. This cytokine\
    \ circuit\n  recruits and activates macrophages, promotes epithelioid and multinucleated\
    \ giant-cell granuloma architecture,\n  and intersects with macrophage-intrinsic\
    \ metabolic programs such as mTORC1 activation. Resolution is\n  hypothesized\
    \ to require antigen clearance or sequestration plus restoration of regulatory\
    \ and apoptotic\n  checkpoints; chronic disease and fibrosis occur when antigen\
    \ persistence, Th17.1 feedback, macrophage\n  survival/proliferation, and tissue-repair\
    \ programs remain engaged.\nnotes: 'Retained as EMERGING after the 2026 OpenScientist\
    \ hypothesis-search report (kb/hypotheses/Sarcoidosis/antigen_persistence_granuloma_chronicity_model/openscientist.md).\n\
    \  The report judged the model partially supported: antigen-driven CD4 T-cell\
    \ responses, Th17.1/Treg imbalance,\n  and macrophage mTORC1 granuloma biology\
    \ are individually well supported, but the integrated Th17.1-to-macrophage\n \
    \ mTORC1 link remains unproven and fibrosis may diverge through distinct profibrotic/EMT-like\
    \ tissue-remodeling\n  programs. Best current fit is non-Lofgren, chronic/progressive\
    \ pulmonary sarcoidosis rather than all\n  sarcoidosis phenotypes.'\nevidence:\n\
    - reference: PMID:38165044\n  reference_title: Immune mechanisms of granuloma\
    \ formation in sarcoidosis and tuberculosis.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Sarcoidosis is a complex immune-mediated disease\
    \ characterized by clusters of immune cells\n    called granulomas.\n  explanation:\
    \ |\n    Recent mechanistic review used as the seed reference for the hypothesis-search\
    \ deep-research run and for the antigen/T-cell/macrophage granuloma-chronicity\
    \ framing.\n- reference: PMID:31273209\n  reference_title: Sarcoidosis.\n  supports:\
    \ SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: The disease develops\
    \ in genetically predisposed individuals with exposure to an as-yet unknown\n\
    \    antigen.\n  explanation: |\n    Nature Reviews Disease Primers review supports\
    \ the central upstream premise of this hypothesis: genetically predisposed patients\
    \ encounter an unknown antigenic trigger."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Sarcoidosis
- **Category:** Immune

## Target Hypothesis
- **Hypothesis ID:** antigen_persistence_granuloma_chronicity_model
- **Hypothesis Label:** Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: antigen_persistence_granuloma_chronicity_model
hypothesis_label: Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model
status: EMERGING
applies_to_subtypes:
- Pulmonary Sarcoidosis
description: Sarcoidosis is modeled as a genetically conditioned, antigen-driven granulomatous immune
  response in which poorly degradable or repeatedly encountered antigens are presented by macrophage-lineage
  antigen-presenting cells to CD4+ T cells. The activated T-cell compartment polarizes toward IFN-gamma-producing
  Th17.1/Th1-like effector states while regulatory T-cell restraint is insufficient. This cytokine circuit
  recruits and activates macrophages, promotes epithelioid and multinucleated giant-cell granuloma architecture,
  and intersects with macrophage-intrinsic metabolic programs such as mTORC1 activation. Resolution is
  hypothesized to require antigen clearance or sequestration plus restoration of regulatory and apoptotic
  checkpoints; chronic disease and fibrosis occur when antigen persistence, Th17.1 feedback, macrophage
  survival/proliferation, and tissue-repair programs remain engaged.
notes: 'Retained as EMERGING after the 2026 OpenScientist hypothesis-search report (kb/hypotheses/Sarcoidosis/antigen_persistence_granuloma_chronicity_model/openscientist.md).
  The report judged the model partially supported: antigen-driven CD4 T-cell responses, Th17.1/Treg imbalance,
  and macrophage mTORC1 granuloma biology are individually well supported, but the integrated Th17.1-to-macrophage
  mTORC1 link remains unproven and fibrosis may diverge through distinct profibrotic/EMT-like tissue-remodeling
  programs. Best current fit is non-Lofgren, chronic/progressive pulmonary sarcoidosis rather than all
  sarcoidosis phenotypes.'
evidence:
- reference: PMID:38165044
  reference_title: Immune mechanisms of granuloma formation in sarcoidosis and tuberculosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Sarcoidosis is a complex immune-mediated disease characterized by clusters of immune cells
    called granulomas.
  explanation: |
    Recent mechanistic review used as the seed reference for the hypothesis-search deep-research run and for the antigen/T-cell/macrophage granuloma-chronicity framing.
- reference: PMID:31273209
  reference_title: Sarcoidosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The disease develops in genetically predisposed individuals with exposure to an as-yet unknown
    antigen.
  explanation: |
    Nature Reviews Disease Primers review supports the central upstream premise of this hypothesis: genetically predisposed patients encounter an unknown antigenic trigger.
```

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

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Mechanistic Hypothesis Search — Sarcoidosis

## Antigen Persistence / Th17.1 / mTORC1 Granuloma Chronicity Model

**Hypothesis ID:** `antigen_persistence_granuloma_chronicity_model`
**KB Status entering search:** EMERGING
**Verdict after search:** **PARTIALLY SUPPORTED — retain EMERGING with explicit subtype restriction and a flagged integrative-edge knowledge gap**

---

## Summary

The Antigen-Persistence / Th17.1 / mTORC1 granuloma-chronicity model is **partially supported** by the current literature. Its individual mechanistic modules are each well-evidenced, but the model's *signature integrative claim* — that Th17.1-derived IFN-γ/cytokines drive macrophage-intrinsic **mTORC1** activation to build and maintain granulomas — is **unproven**. The strongest mTORC1 evidence is genetic and cell-intrinsic and does not invoke Th17.1; the strongest Th17.1-to-macrophage evidence operates through a **CD47/SIRPα antigen-processing** axis, not mTORC1. The two arms of the hypothesis therefore rest on separate experimental foundations that have not been causally connected in a single system.

Where the model is strong: (1) sarcoidosis is a genetically conditioned, antigen-driven CD4⁺ T-cell disease in which **HLA-DRB1** genotype sets an upstream fork between resolving (Löfgren) and chronic disease; (2) **activated Th17.1 cells** are enriched in blood and BALF, track disease activity/progression, and coexist with **insufficient regulatory T-cell restraint** in the lung; (3) macrophage/stromal **mTORC1 hyperactivation is sufficient** to generate sarcoid-like granulomas in mice; and (4) blocking the **IFN-γ/JAK-STAT effector circuit** (tofacitinib) clinically resolves granulomas, causally validating the cytokine-circuit arm.

Where the model is weak or bounded: the causal antigen remains **unidentified** (infectious, autoimmune, and host-innate-amplifier models all compete); the Th17.1→mTORC1 edge is **inferred, not demonstrated**; and **fibrosis** appears only *partially* coupled to the Th17.1/mTORC1 axis, engaging a parallel **myeloid HIF-1α** program in progressive disease. The best-fit scope is **non-Löfgren, chronic/progressive pulmonary (and cardiac) sarcoidosis**, not all sarcoidosis phenotypes. Recommendation: **retain EMERGING**, add a subtype restriction, and record the Th17.1→mTORC1 link as an explicit knowledge gap.

---

## Executive Judgment

**Verdict: partially supported.** Across 26 papers reviewed over 5 investigation iterations, the search confirmed 7 findings and supported 8 hypotheses (0 refuted). Every *module* of the seed hypothesis is supported by at least one strong evidence class — genetic (HLA-DRB1), human immunophenotyping (Th17.1/Treg), murine causal genetics (mTORC1 sufficiency), and human therapeutic reversal (JAK inhibition). However, the integrative edge that gives the hypothesis its distinctive identity — Th17.1→macrophage mTORC1 — is nowhere directly demonstrated. The only measured Th17.1→macrophage mechanism runs through CD47/SIRPα antigen-processing suppression; the antigen is unidentified; and fibrosis recruits a parallel HIF-1α program. This is precisely the profile of an **EMERGING** hypothesis: real, well-motivated, and partly validated at the module level, but not yet unified by direct causal linkage. The most important caveats are (a) the missing Th17.1→mTORC1 causal step, (b) unidentified antigen, and (c) subtype scope limited to non-Löfgren chronic/progressive disease.

---

## Key Findings

### F001 — Macrophage/stromal mTORC1 hyperactivation causally drives sarcoid-like granuloma formation (model-organism, causal)

Genetic mouse models provide the most direct causal evidence for the macrophage-metabolic arm of the hypothesis. Deletion of *Tsc1* or *Tsc2* using an *Fsp1*-Cre driver produces **spontaneous sarcoid-like granulomas** driven by **mTORC1 hyperactivation in fibroblasts and interstitial macrophages**, operating through a dysregulated **CCL24–CCR3** chemokine axis; both **rapamycin** (mTORC1 inhibitor) and **azithromycin** attenuate granuloma burden ([PMID: 40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/)). Independently, **chronic mTORC1 activation restricted to myeloid cells** is sufficient to produce spontaneous pulmonary *and* cardiac sarcoid-like granulomas ([PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)). This is knockout-plus-pharmacologic-rescue evidence — the gold standard for demonstrating sufficiency — but it is in mouse rather than human, and, critically, **it does not require or invoke Th17.1 cells**. mTORC1 activation here is cell-intrinsic and upstream-agnostic, which supports the mTORC1 *node* of the hypothesis while leaving the Th17.1→mTORC1 *edge* untouched.

### F002 — Activated Th17.1 cells are enriched and track disease activity, alongside reduced lung Tregs (human clinical)

In human cohorts (blood n=34, BALF n=22 vs CTD-ILD controls), the proportion of **activated Th17.1 cells was higher** in both peripheral blood and bronchoalveolar lavage fluid of pulmonary sarcoidosis patients than in connective-tissue-disease-associated ILD; these cells **decline with corticosteroid treatment** and reflect disease activity/progression, while **lung Treg proportions were significantly lower** than in CTD-ILD ([PMID: 42286635](https://pubmed.ncbi.nlm.nih.gov/42286635/)). Mass cytometry (CyTOF) of lymph nodes and blood confirms Th17.1 overactivation and identifies a **type III granuloma** endotype (M2-macrophage + Th17.1-high) predicting poor glucocorticoid response; importantly, Th17.1 cells **impaired macrophage antigen phagocytosis and processing via CD47/SIRPα** ([PMID: 41316274](https://pubmed.ncbi.nlm.nih.gov/41316274/)). Integrative scRNA-seq of BALF and cardiac tissue independently confirms Th17.1 upregulation across pulmonary and cardiac sarcoidosis ([PMID: 37576111](https://pubmed.ncbi.nlm.nih.gov/37576111/)). This robustly supports the effector-polarization and insufficient-Treg-restraint claims — but notably the one *direct* Th17.1→macrophage mechanism found operates through antigen-processing suppression, **not mTORC1**.

### F003 — KEY GAP: the integrated Th17.1→macrophage-mTORC1 causal edge is unproven

This is the pivotal finding for hypothesis status. The strongest mTORC1 evidence is genetic and cell-intrinsic (*Tsc1/2* knockout, myeloid mTOR activation) and never invokes Th17.1 ([PMID: 40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/), [PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)). The strongest Th17.1-to-macrophage evidence links the two cell types via **CD47/SIRPα antigen-processing suppression**, not mTORC1 activation ([PMID: 41316274](https://pubmed.ncbi.nlm.nih.gov/41316274/), [PMID: 42286635](https://pubmed.ncbi.nlm.nih.gov/42286635/)). **No located study demonstrates that Th17.1-derived IFN-γ or other cytokines activate macrophage mTORC1 to build granulomas.** The two modules come from separate model systems and have never been experimentally bridged. This is the central missing causal step that keeps the integrated model at EMERGING rather than SUPPORTED.

### F004 — HLA-DRB1*03 antigen-presentation genotype governs the resolution-vs-chronicity fork (human genetic)

The upstream, genetically conditioned premise of the hypothesis is strongly supported and, importantly, **defines the model's subtype boundary**. **HLA-DRB1*03** is significantly associated with **Löfgren syndrome and disease resolution** (Portuguese case-control, n=151/150), while **BTNL2 rs2076530** independently marks non-Löfgren/isolated thoracic disease ([PMID: 23017494](https://pubmed.ncbi.nlm.nih.gov/23017494/)). An in-silico HLA-DR immunome analysis (149 patients/447 controls, high-resolution typing) showed Löfgren patients express alleles recognizing **significantly more bacterial antigen epitopes** than chronic patients (18,496 vs 17,954; p<0.00001) and were far more likely to achieve top-affinity *M. avium* epitope recognition (45% vs 17%; p=0.0037) ([PMID: 19382529](https://pubmed.ncbi.nlm.nih.gov/19382529/)). **Vimentin** is implicated as an HLA-restricted T-cell autoantigen ([PMID: 30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/)), and sarcoid CD4 T cells show **PD-1 upregulation with reduced proliferative capacity** ([PMID: 29234685](https://pubmed.ncbi.nlm.nih.gov/29234685/)). Genotype thus sits upstream of the Th17.1/mTORC1 effector axis and determines whether antigen is efficiently recognized/cleared (resolution) or persists (chronicity).

### F005 — JAK-STAT/IFN-γ effector-circuit blockade clinically resolves granulomas (human clinical, causal perturbation) — but does not isolate mTORC1

The effector-cytokine arm has direct human causal validation. In **refractory cardiac sarcoidosis, tofacitinib achieved inactive/remitting disease in 7/8 patients (87.5%)** by repeat ¹⁸F-FDG-PET/CT, with reduced myocardial SUVmax, stabilized/improved LVEF, corticosteroid tapering, and falling **neopterin** (a macrophage-activation marker) ([PMID: 41916671](https://pubmed.ncbi.nlm.nih.gov/41916671/)). A 49-patient systematic review reported **45% complete and 49% partial responses** to JAK inhibitors ([PMID: 41396108](https://pubmed.ncbi.nlm.nih.gov/41396108/)). Mechanistic model work shows tofacitinib suppresses JAK3/STAT5, **restores Treg-driven M2 polarization, induces pyroptosis, and reduces granuloma burden** ([PMID: 42251788](https://pubmed.ncbi.nlm.nih.gov/42251788/)), and JAK-STAT transduces the IFN-γ/IL-6/IL-12/IL-23 cytokines central to granuloma initiation/maintenance ([PMID: 41459541](https://pubmed.ncbi.nlm.nih.gov/41459541/)). This proves the effector cytokine circuit is causally required to sustain granulomas — but JAK inhibition acts broadly on the cytokine network and **does not isolate a Th17.1→mTORC1 link**.

### F006 — Fibrosis is only partially coupled to the Th17.1/mTORC1 axis; a parallel myeloid HIF-1α program sustains progression

Evidence is mixed and points to partial divergence. *Supporting coupling:* **CXCR6 blockade suppresses both granuloma formation AND pulmonary fibrosis** by inhibiting Th17 responses ([PMID: 42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/)), and mTORC1 mouse models progress to fibrosis ([PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)). *Supporting divergence:* **myeloid HIF-1α** sustains hypoxic fibrotic "advancing fronts" via macrophage–fibroblast crosstalk, and circulating monocytes from **progressive (vs resolving)** sarcoidosis patients show increased HIF-1α ([PMID: 41959437](https://pubmed.ncbi.nlm.nih.gov/41959437/)); cardiac sarcoid granuloma transcriptomics reveal distinct fibrosis/progression programs ([PMID: 40521183](https://pubmed.ncbi.nlm.nih.gov/40521183/)). Fibrosis therefore is neither fully explained by nor fully independent of the seed axis — a parallel innate metabolic program contributes, so the hypothesis best applies to the *granulomatous-inflammation* phase rather than the entire fibrotic trajectory.

### F007 — Antigen persistence is biologically plausible but the driving antigen is unidentified; competing etiologic models

Microbial antigens (mycobacterial + *Cutibacterium acnes*) are detected within sarcoid granulomas by immunohistochemistry ([PMID: 33801218](https://pubmed.ncbi.nlm.nih.gov/33801218/)), and latent *C. acnes* reactivation is proposed as an "endogenous hypersensitivity infection" etiology ([PMID: 41597666](https://pubmed.ncbi.nlm.nih.gov/41597666/), [PMID: 40837573](https://pubmed.ncbi.nlm.nih.gov/40837573/)). In parallel, **serum amyloid A** is abundant in sarcoid tissue and acts as an innate ligand promoting persistent antigen localization and granuloma maintenance ([PMID: 27387100](https://pubmed.ncbi.nlm.nih.gov/27387100/)), and vimentin is implicated as an HLA-restricted autoantigen ([PMID: 30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/)). **No single antigen has been shown causally necessary for chronicity** — the antigen-persistence premise is supported in principle but not resolved in identity, and infectious, autoimmune, and host-amplifier models remain in competition.

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain. Each edge is graded by the evidence strength surfaced in this search.

```
 [Genetic susceptibility]        HLA-DRB1 genotype, BTNL2
        │  (STRONG: F004; PMID 23017494, 19382529)
        ▼
 [Antigen encounter/persistence] microbial (mycobacteria, C. acnes) /
        │                         autoantigen (vimentin) / host SAA amplifier
        │  (PLAUSIBLE but antigen UNIDENTIFIED: F007)
        ▼
 [APC presentation to CD4+ T]    macrophage-lineage APCs
        │  (STRONG, classical)
        ▼
 [Th17.1/Th1 polarization]  +  [insufficient Treg restraint]
        │  (STRONG human: F002; PMID 42286635, 41316274, 37576111)
        ▼
 [IFN-γ / JAK-STAT effector cytokine circuit]
        │  (CAUSALLY VALIDATED by reversal: F005; PMID 41916671, 41396108)
        ▼
 [Macrophage recruitment/activation] ───► [macrophage mTORC1 activation]
        │       (Th17.1→mTORC1 edge = UNPROVEN / MISSING: F003)
        │        ▲ mTORC1 sufficiency proven separately, cell-intrinsic
        │        │ (STRONG but Th17.1-agnostic: F001; PMID 40791394, 37750561)
        ▼
 [Epithelioid / giant-cell granuloma architecture]
        │  (STRONG)
        ├─────────────► [Resolution] if antigen cleared + Treg/apoptotic checkpoints restored
        ▼
 [Chronicity → fibrosis]
        │  Th17.1/CXCR6-coupled (PMID 42143504) + parallel myeloid HIF-1α (PMID 41959437)
        │  (PARTIALLY COUPLED / PARTIALLY DIVERGENT: F006)
        ▼
 [Progressive pulmonary/cardiac disease, organ damage]
```

**Where the literature is strong:** the upstream genetic fork, the antigen→APC→CD4→Th17.1 polarization cascade, insufficient Treg restraint, and the causal necessity of the IFN-γ/JAK-STAT effector circuit (proven by clinical reversal). Macrophage/stromal mTORC1 **sufficiency** for granuloma formation is also strong — but as a *parallel, cell-intrinsic* mechanism rather than a downstream consequence of Th17.1.

**Where the links are inferred:** the specific edge from Th17.1 effector cytokines to macrophage mTORC1 activation. Both nodes exist and are individually validated, but the arrow between them is assumed, not measured.

**Missing causal steps:** (1) demonstration that Th17.1/IFN-γ signaling activates macrophage mTORC1 in sarcoid tissue; (2) identity of the persistent antigen and proof it is causally necessary for chronicity; (3) the mechanism partitioning fibrosis between Th17.1/mTORC1-coupled and HIF-1α-independent routes.

---

## Evidence Base — Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/) | Model organism | Supports (mTORC1 arm) | mTORC1 in macrophage/stromal cells is sufficient for granuloma | *Tsc1/2* deletion → spontaneous granulomas via CCL24-CCR3; rapamycin/azithromycin rescue | Sarcoid-like, mouse | High for sufficiency; mouse; Th17.1-agnostic |
| [PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/) | Model organism | Supports (mTORC1 arm) | Myeloid mTORC1 activation sufficient for granuloma | Chronic myeloid mTORC1 → spontaneous pulmonary + cardiac granulomas | Cardiac/pulmonary, mouse | High; mouse; no adaptive-immune trigger required |
| [PMID: 42286635](https://pubmed.ncbi.nlm.nih.gov/42286635/) | Human clinical | Supports (Th17.1/Treg arm) | Th17.1 enrichment + Treg deficiency | ↑ activated Th17.1 in blood/BALF, ↓ lung Tregs vs CTD-ILD; tracks activity | Pulmonary | High; observational; no mTORC1 readout |
| [PMID: 41316274](https://pubmed.ncbi.nlm.nih.gov/41316274/) | Human/in vitro | Qualifies | Th17.1→macrophage mechanistic link | Th17.1 impair macrophage antigen processing via CD47/SIRPα; type III granuloma predicts poor steroid response | Early-stage | High; link is CD47/SIRPα, **not** mTORC1 |
| [PMID: 37576111](https://pubmed.ncbi.nlm.nih.gov/37576111/) | Computational (scRNA-seq) | Supports | Th17.1 transcriptional upregulation | Th17.1 upregulated in BALF + cardiac tissue | Pulmonary + cardiac | Moderate; public-dataset reanalysis |
| [PMID: 23017494](https://pubmed.ncbi.nlm.nih.gov/23017494/) | Human genetic | Supports (upstream) | HLA/BTNL2 set resolution vs chronic fork | HLA-DRB1*03 → Löfgren + resolution; BTNL2 → non-Löfgren | Löfgren vs chronic | High; case-control; population-specific |
| [PMID: 19382529](https://pubmed.ncbi.nlm.nih.gov/19382529/) | Computational | Supports (upstream) | HLA epitope-recognition breadth vs phenotype | Löfgren alleles recognize more bacterial epitopes (p<0.00001); *M. avium* top-affinity 45% vs 17% | Löfgren vs chronic | Moderate; in silico |
| [PMID: 41916671](https://pubmed.ncbi.nlm.nih.gov/41916671/) | Human clinical | Supports (effector arm) | JAK-STAT/IFN-γ blockade resolves granuloma | Tofacitinib → inactive/remitting in 7/8 (87.5%) by PET | Refractory cardiac | High for effector necessity; small n; not mTORC1-specific |
| [PMID: 41396108](https://pubmed.ncbi.nlm.nih.gov/41396108/) | Human clinical (review) | Supports (effector arm) | JAK inhibition efficacy | 45% complete, 49% partial response (n=49) | Pulmonary + extrapulmonary | Moderate; heterogeneous case series |
| [PMID: 42251788](https://pubmed.ncbi.nlm.nih.gov/42251788/) | Model/in vitro | Supports (effector/Treg) | Tofacitinib restores Treg→M2, induces pyroptosis | ↓ granuloma via JAK3/STAT5; Treg function restored | SodA-induced model | Moderate; induced model |
| [PMID: 42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/) | Model organism | Supports (coupling) | Th17/CXCR6 drives fibrosis | CXCR6 blockade suppresses granuloma AND fibrosis | Pulmonary | Moderate; couples fibrosis to Th17 |
| [PMID: 41959437](https://pubmed.ncbi.nlm.nih.gov/41959437/) | Human + model | Competing (parallel) | Myeloid HIF-1α drives fibrosis | Progressive-disease monocytes ↑ HIF-1α vs resolving | Progressive pulmonary | Moderate; parallel to seed axis |
| [PMID: 40521183](https://pubmed.ncbi.nlm.nih.gov/40521183/) | Computational | Qualifies | Distinct fibrosis/progression programs | Granuloma transcriptomics reveal separate fibrosis programs | Cardiac | Moderate; descriptive |
| [PMID: 33801218](https://pubmed.ncbi.nlm.nih.gov/33801218/) | Human clinical | Supports (antigen) | Microbial antigen persistence | Mycobacterial + *C. acnes* antigens in granulomas by IHC | Diagnostic tissue | Moderate; detection ≠ causation |
| [PMID: 27387100](https://pubmed.ncbi.nlm.nih.gov/27387100/) | Review/in vitro | Competing (host amplifier) | SAA innate-ligand persistence | SAA abundant in tissue, regulates granulomatous inflammation | Innate pathobiology | Moderate; host-protein route |
| [PMID: 30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/) | Human clinical | Supports/competing (autoantigen) | Vimentin as HLA-restricted autoantigen | Vimentin drives HLA-restricted T-cell response | Pulmonary | Moderate; autoimmune framing |
| [PMID: 29234685](https://pubmed.ncbi.nlm.nih.gov/29234685/) | Human clinical | Qualifies | T-cell exhaustion | Sarcoid CD4 T cells ↑ PD-1, ↓ proliferation | Pulmonary | Moderate; exhaustion vs effector tension |
| [PMID: 41197661](https://pubmed.ncbi.nlm.nih.gov/41197661/) | Review | Supports (orientation) | Integrated immunopathogenesis | Innate-adaptive crosstalk, perpetuating loop, fibrotic progression | General | Review-level orientation |
| [PMID: 41884121](https://pubmed.ncbi.nlm.nih.gov/41884121/) | Review | Competing (orientation) | NLRP3/IL-1/IL-18 innate targets | Th17.1 + M2 central; NLRP3 promising target | Cardiac | Review-level; highlights innate alternative |

---

## Limitations and Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | Resolving evidence/experiment |
|---|---|---|---|---|
| **Th17.1→macrophage mTORC1 edge unproven** | Chronic pulmonary/cardiac | This is the model's defining integrative claim; without it the model is two parallel modules, not one circuit | PubMed searches for mTORC1 evidence (genetic, cell-intrinsic) and Th17.1→macrophage links (CD47/SIRPα) — no bridging study found | Co-culture of Th17.1 with macrophages measuring phospho-S6/4E-BP1; IFN-γ/anti-IFN-γ perturbation of macrophage mTORC1 in sarcoid tissue |
| **Causal antigen unidentified** | All subtypes | Antigen persistence is the upstream driver; without identity, "persistence" cannot be tested or cleared therapeutically | Reviewed microbial (mycobacteria, *C. acnes*), autoantigen (vimentin), host-amplifier (SAA) evidence — all correlative | Antigen-specific TCR-seq + tetramer tracking; antimicrobial or antigen-depletion trials with clinical endpoints |
| **Fibrosis partitioning** | Progressive disease | Determines whether anti-Th17.1/mTORC1 therapy prevents fibrosis or only inflammation | Found both coupling (CXCR6/Th17) and divergence (myeloid HIF-1α) evidence | Longitudinal single-cell + spatial transcriptomics of fibrotic fronts; HIF-1α vs mTORC1 conditional knockouts |
| **Subtype restriction** | Löfgren vs non-Löfgren | Model does not fit resolving/Löfgren disease governed by HLA-DRB1*03 | HLA genetics reviewed (F004) | Prospective HLA-stratified cohorts comparing Th17.1/mTORC1 markers across phenotypes |
| **Human mTORC1 causality** | Human | All strong mTORC1 causal data are murine | Only murine knockout/rescue found | Rapamycin/sirolimus trial in chronic sarcoidosis with mTORC1 pathway pharmacodynamic readout |
| **Mechanism of JAK-inhibitor action** | Effector arm | Clinical reversal proves effector necessity but not which cytokine/node | Tofacitinib clinical + mechanistic papers reviewed | Cytokine-selective blockade (anti-IFN-γ vs anti-IL-23) head-to-head |
| **Source/data absence** | Curation | No GenCC/ClinGen gene-disease or omics-cohort evidence for the *integrated* edge was located | PubMed only; genetic databases not directly queried during this run | Query GenCC/ClinGen for HLA-DRB1, BTNL2, TSC1/2; mine GEO/BALF omics for co-expression of Th17.1 and mTORC1 signatures |

---

## Alternative Models

| Alternative model | Relationship to seed | Basis |
|---|---|---|
| **Cell-intrinsic macrophage mTORC1 model** | *Parallel / competing mechanism* — mTORC1 sufficient without Th17.1 | *Tsc1/2* and myeloid-mTOR mouse granulomas form without adaptive trigger ([PMID: 40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/), [PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)) |
| **HLA/antigen-specificity genetic model** | *Upstream cause* — genotype sets resolution vs chronicity before effector polarization | [PMID: 23017494](https://pubmed.ncbi.nlm.nih.gov/23017494/), [PMID: 19382529](https://pubmed.ncbi.nlm.nih.gov/19382529/) |
| **NLRP3 inflammasome / IL-1/IL-18 innate model** | *Parallel/complementary* — innate signaling as primary driver | Cardiac sarcoid reviews highlight NLRP3 + IL-1/IL-18 blockade as targets ([PMID: 41884121](https://pubmed.ncbi.nlm.nih.gov/41884121/)) |
| **Myeloid HIF-1α fibrosis model** | *Downstream/parallel* for fibrosis specifically | Progressive-monocyte HIF-1α ([PMID: 41959437](https://pubmed.ncbi.nlm.nih.gov/41959437/)) |
| **Endogenous hypersensitivity / latent microbial reactivation** | *Upstream cause* — specifies the antigen source | [PMID: 41597666](https://pubmed.ncbi.nlm.nih.gov/41597666/), [PMID: 40837573](https://pubmed.ncbi.nlm.nih.gov/40837573/) |
| **Autoimmune (vimentin) model** | *Upstream cause / competing etiology* | [PMID: 30038611](https://pubmed.ncbi.nlm.nih.gov/30038611/) |
| **Host SAA innate-amplifier model** | *Competing* — persistence via host protein, not exogenous antigen | [PMID: 27387100](https://pubmed.ncbi.nlm.nih.gov/27387100/) |
| **T-cell exhaustion model** | *Qualifying* — tension with an "active effector" framing | PD-1↑, ↓proliferation ([PMID: 29234685](https://pubmed.ncbi.nlm.nih.gov/29234685/)) |

---

## Discriminating Tests / Proposed Follow-up Experiments

1. **Th17.1→mTORC1 bridging assay (highest priority).** Co-culture patient-derived Th17.1 cells (or apply IFN-γ ± neutralizing antibody) with sarcoid alveolar macrophages; read out **phospho-S6, phospho-4E-BP1, mTORC1 target genes**. *Expected if hypothesis true:* Th17.1/IFN-γ increases macrophage mTORC1 activity, blocked by anti-IFN-γ and rapamycin. *If false:* macrophage mTORC1 is independent of Th17.1 signaling. This is the single most decisive experiment for moving the hypothesis from EMERGING toward SUPPORTED or REFUTED.

2. **HLA-stratified longitudinal phenotyping.** Prospective cohort stratified by HLA-DRB1*03 status (Löfgren vs non-Löfgren), serial BALF Th17.1 fraction, Treg fraction, macrophage mTORC1 and HIF-1α signatures. *Expected:* Th17.1/mTORC1 markers persist in HLA-DRB1*03-negative chronic disease and resolve in Löfgren.

3. **mTORC1-pathway trial in humans.** Sirolimus/rapamycin (or continued azithromycin) in chronic pulmonary sarcoidosis with ¹⁸F-FDG-PET and pathway pharmacodynamics. *Expected:* granuloma metabolic activity falls with mTORC1 target engagement — closing the human-causality gap.

4. **Fibrosis-partitioning spatial multi-omics.** Spatial transcriptomics of fibrotic advancing fronts to test whether HIF-1α⁺ regions are mTORC1/Th17.1-low. *Expected:* two spatially distinct programs, supporting F006 divergence.

5. **Antigen-necessity test.** Antimicrobial (targeting *C. acnes*/mycobacteria) or antigen-directed intervention with granuloma-activity endpoint. *Expected if antigen-persistence true:* clearance reduces chronicity.

6. **Cytokine-selective blockade head-to-head.** Anti-IFN-γ vs anti-IL-23/IL-17 to dissect which effector node the JAK-inhibitor benefit depends on.

---

## Curation Leads (require curator verification)

**Candidate status change:** Retain **EMERGING**. Add explicit `applies_to_subtypes` restriction to **non-Löfgren, chronic/progressive pulmonary and cardiac sarcoidosis**; explicitly exclude Löfgren/resolving disease (governed upstream by HLA-DRB1*03).

**Candidate evidence references + snippets to verify:**
- [PMID: 40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/) — "deletion of TSC1 or TSC2 in mice using a Fsp1-Cre leads to spontaneous formation of sarcoid-like granulomas, driven by hyperactivation of the mTORC1 pathway in fibroblasts and interstitial macrophages" (SUPPORT, mTORC1 sufficiency)
- [PMID: 37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/) — "chronic activation of mammalian target of rapamycin (mTOR) complex 1 signaling in myeloid cells known to cause spontaneous pulmonary sarcoid-like granulomas" (SUPPORT)
- [PMID: 42286635](https://pubmed.ncbi.nlm.nih.gov/42286635/) — "The proportion of activated Th17.1 cells was higher in peripheral blood and bronchoalveolar lavage fluid from patients with pulmonary sarcoidosis than from patients with connective tissue disease-associated interstitial lung disease." (SUPPORT)
- [PMID: 41316274](https://pubmed.ncbi.nlm.nih.gov/41316274/) — "Th17.1 cells impaired the antigen phagocytic and processing ability of macrophages through CD47/SIRPα interaction" (QUALIFIES — alternative Th17.1→macrophage link)
- [PMID: 23017494](https://pubmed.ncbi.nlm.nih.gov/23017494/) — "HLA-DRB1*03, besides the association with Löfgren syndrome was significantly related with disease resolution." (SUPPORT, upstream subtype fork)
- [PMID: 41916671](https://pubmed.ncbi.nlm.nih.gov/41916671/) — "Seven out of eight patients (87.5%) who received tofacitinib achieved inactive or remitting disease as assessed by repeat myocardial 18F-FDG PET/CT" (SUPPORT, effector-circuit necessity)
- [PMID: 41959437](https://pubmed.ncbi.nlm.nih.gov/41959437/) — "In sarcoidosis, circulating monocytes from patients with progressive disease exhibited increased HIF-1α compared with those with resolving disease." (COMPETING/parallel fibrosis program)

**Candidate pathophysiology nodes/edges:**
- Node: macrophage mTORC1 activation → CCL24–CCR3 axis → granuloma maintenance (add; murine causal)
- Edge (flag as UNCONFIRMED): Th17.1/IFN-γ → macrophage mTORC1 activation
- Edge (add): Th17.1 → CD47/SIRPα → impaired macrophage antigen processing
- Edge (add, parallel): progressive-monocyte HIF-1α → fibrotic front maintenance
- Node: HLA-DRB1*03 → efficient antigen recognition/clearance → resolution (Löfgren)

**Candidate ontology terms:** Th17.1 cell; regulatory T cell; interstitial macrophage / M2 macrophage; epithelioid cell; multinucleated giant cell; mTORC1 signaling (TORC1 signaling, GO:0038202); granuloma formation; response to hypoxia / HIF-1α signaling; antigen processing and presentation.

**Candidate `knowledge_gaps` prompts:** (1) unproven Th17.1→macrophage-mTORC1 causal edge; (2) unidentified persistent antigen and its causal necessity; (3) fibrosis partitioning between Th17.1/mTORC1-coupled and HIF-1α-independent routes; (4) absence of human mTORC1 causal/interventional data; (5) no located GenCC/ClinGen/omics-cohort evidence for the integrated edge as of the search date (2026-07-26).

---

*Report generated from a 5-iteration autonomous hypothesis-search investigation (26 papers reviewed, 7 confirmed findings, 8 supported hypotheses). Verdict: partially supported; retain EMERGING with subtype restriction to non-Löfgren chronic/progressive pulmonary and cardiac sarcoidosis, and an explicit flagged knowledge gap on the Th17.1→macrophage-mTORC1 causal edge.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
