---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T03:13:11.801298'
end_time: '2026-07-26T03:30:55.985074'
duration_seconds: 1064.18
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Sarcoidosis
  category: Immune
  hypothesis_group_id: environmental_exposure_host_susceptibility_trigger_model
  hypothesis_label: "Environmental Exposure \xD7 Host Susceptibility Trigger Model"
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: environmental_exposure_host_susceptibility_trigger_model\n\
    hypothesis_label: Environmental Exposure \xD7 Host Susceptibility Trigger Model\n\
    status: EMERGING\napplies_to_subtypes:\n- Pulmonary Sarcoidosis\ndescription:\
    \ Specific inhaled bioaerosols or inorganic particles may, in some susceptible\
    \ hosts, initiate\n  pulmonary sarcoidosis by engaging exposure-specific innate\
    \ sensing or antigen-presentation programs\n  that alter CD4+ T-cell polarization.\
    \ HLA and other immune-risk alleles may modify these early responses\n  and the\
    \ resulting disease phenotype. This upstream trigger model complements the existing\
    \ antigen-persistence/granuloma-chronicity\n  model; it does not assert that distinct\
    \ exposure classes share one receptor or causal pathway. The exposure-specific\n\
    \  sensors, intermediates, and exposure-by-genotype combinations remain unresolved.\n\
    notes: Seed hypothesis for GitHub issue 6971. It requires disease-level OpenScientist\
    \ research followed\n  by a focused hypothesis investigation before any exposure-specific\
    \ trigger edge or status change is\n  curated.\nevidence:\n- reference: PMID:42471775\n\
    \  reference_title: Current understanding of environmental exposures and sarcoidosis.\n\
    \  supports: PARTIAL\n  evidence_source: OTHER\n  snippet: The identification\
    \ of multiple exposures across different sarcoidosis manifestations suggests\n\
    \    a possible gene-environment-phenotype relationship, which may explain some\
    \ of the difficulty with\n    identifying specific causes to date.\n  explanation:\
    \ This review motivates an exposure-by-host-susceptibility model while explicitly\
    \ presenting\n    the relationship as possible rather than causal.\n- reference:\
    \ PMID:19382531\n  reference_title: HLA and environmental interactions in sarcoidosis.\n\
    \  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet: Significant\
    \ interaction was observed between HLA DRB1*1101 and insecticide exposure at work\n\
    \    (p < 0.10) and suggestive interaction was observed between HLA DRB1*1101\
    \ and exposure to mold and\n    musty odors and DRB1*1501 and insecticide exposure\
    \ at work (P < 0.15).\n  explanation: The ACCESS case-control analysis provides\
    \ exposure-by-HLA leads, but its exploratory significance\n    thresholds and\
    \ phenotype stratification require independent replication before these pairs\
    \ are modeled\n    as causal.\n- reference: PMID:31126090\n  reference_title:\
    \ Genetic Variants Associated with FDNY WTC-Related Sarcoidosis.\n  supports:\
    \ PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet: Seventeen allele variants\
    \ of human leukocyte antigen (HLA) and non-HLA genes were found to\n    be associated\
    \ with sarcoidosis, and all were within chromosomes 1 and 6.\n  explanation: The\
    \ uniformly WTC-exposed case-control cohort supplies candidate susceptibility\
    \ variants,\n    but it cannot by itself establish a genotype-by-exposure interaction.\n\
    - reference: PMID:31126090\n  reference_title: Genetic Variants Associated with\
    \ FDNY WTC-Related Sarcoidosis.\n  supports: REFUTE\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: In our secondary analysis, we did not find statistical evidence of\
    \ an interaction between common\n    variants and the degree of WTC exposure.\n\
    \  explanation: This small candidate-gene study did not detect effect modification\
    \ by its WTC exposure-severity\n    measure, directly constraining a dose-dependent\
    \ gene-exposure claim.\n- reference: PMID:30134122\n  reference_title: IL-13-regulated\
    \ Macrophage Polarization during Granuloma Formation in an In Vitro Human\n  \
    \  Sarcoidosis Model.\n  supports: PARTIAL\n  evidence_source: IN_VITRO\n  snippet:\
    \ Compared with identically treated PBMCs of control subjects (n\u2009=\u2009\
    5), purified protein derivative-treated\n    sarcoidosis PBMCs (n\u2009=\u2009\
    6) were distinguished by the formation of cellular aggregates resembling granulomas.\n\
    \  explanation: Patient-cell responses to a putative mycobacterial antigen provide\
    \ an experimental antigen-to-granuloma\n    bridge, but the small in-vitro model\
    \ does not identify an environmental trigger in vivo.\n- reference: PMID:20813038\n\
    \  reference_title: No evidence of altered alveolar macrophage polarization, but\
    \ reduced expression of\n    TLR2, in bronchoalveolar lavage cells in sarcoidosis.\n\
    \  supports: PARTIAL\n  evidence_source: HUMAN_CLINICAL\n  snippet: Overall, there\
    \ was no evidence for alveolar macrophage polarization in sarcoidosis. However,\n\
    \    there was a reduced TLR2 mRNA expression in patients with L\xF6fgren's syndrome,\
    \ which may be of relevance\n    for macrophage interactions with a postulated\
    \ sarcoidosis pathogen, and for the characteristics of\n    the ensuing T cell\
    \ response.\n  explanation: Human bronchoalveolar data make TLR2 a phenotype-specific\
    \ lead while directly cautioning\n    against a uniform macrophage-polarization\
    \ or PRR mechanism across sarcoidosis subtypes."
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
artifact_count: 5
artifact_sources:
  openscientist_artifacts_zip: 5
artifacts:
- filename: evidence_matrix.csv
  path: openscientist_artifacts/evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
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
- filename: knowledge_gaps.csv
  path: openscientist_artifacts/knowledge_gaps.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
- filename: mechanistic_diagram.md
  path: openscientist_artifacts/mechanistic_diagram.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic diagram
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
- **Hypothesis ID:** environmental_exposure_host_susceptibility_trigger_model
- **Hypothesis Label:** Environmental Exposure × Host Susceptibility Trigger Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: environmental_exposure_host_susceptibility_trigger_model
hypothesis_label: Environmental Exposure × Host Susceptibility Trigger Model
status: EMERGING
applies_to_subtypes:
- Pulmonary Sarcoidosis
description: Specific inhaled bioaerosols or inorganic particles may, in some susceptible hosts, initiate
  pulmonary sarcoidosis by engaging exposure-specific innate sensing or antigen-presentation programs
  that alter CD4+ T-cell polarization. HLA and other immune-risk alleles may modify these early responses
  and the resulting disease phenotype. This upstream trigger model complements the existing antigen-persistence/granuloma-chronicity
  model; it does not assert that distinct exposure classes share one receptor or causal pathway. The exposure-specific
  sensors, intermediates, and exposure-by-genotype combinations remain unresolved.
notes: Seed hypothesis for GitHub issue 6971. It requires disease-level OpenScientist research followed
  by a focused hypothesis investigation before any exposure-specific trigger edge or status change is
  curated.
evidence:
- reference: PMID:42471775
  reference_title: Current understanding of environmental exposures and sarcoidosis.
  supports: PARTIAL
  evidence_source: OTHER
  snippet: The identification of multiple exposures across different sarcoidosis manifestations suggests
    a possible gene-environment-phenotype relationship, which may explain some of the difficulty with
    identifying specific causes to date.
  explanation: This review motivates an exposure-by-host-susceptibility model while explicitly presenting
    the relationship as possible rather than causal.
- reference: PMID:19382531
  reference_title: HLA and environmental interactions in sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Significant interaction was observed between HLA DRB1*1101 and insecticide exposure at work
    (p < 0.10) and suggestive interaction was observed between HLA DRB1*1101 and exposure to mold and
    musty odors and DRB1*1501 and insecticide exposure at work (P < 0.15).
  explanation: The ACCESS case-control analysis provides exposure-by-HLA leads, but its exploratory significance
    thresholds and phenotype stratification require independent replication before these pairs are modeled
    as causal.
- reference: PMID:31126090
  reference_title: Genetic Variants Associated with FDNY WTC-Related Sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Seventeen allele variants of human leukocyte antigen (HLA) and non-HLA genes were found to
    be associated with sarcoidosis, and all were within chromosomes 1 and 6.
  explanation: The uniformly WTC-exposed case-control cohort supplies candidate susceptibility variants,
    but it cannot by itself establish a genotype-by-exposure interaction.
- reference: PMID:31126090
  reference_title: Genetic Variants Associated with FDNY WTC-Related Sarcoidosis.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: In our secondary analysis, we did not find statistical evidence of an interaction between common
    variants and the degree of WTC exposure.
  explanation: This small candidate-gene study did not detect effect modification by its WTC exposure-severity
    measure, directly constraining a dose-dependent gene-exposure claim.
- reference: PMID:30134122
  reference_title: IL-13-regulated Macrophage Polarization during Granuloma Formation in an In Vitro Human
    Sarcoidosis Model.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Compared with identically treated PBMCs of control subjects (n = 5), purified protein derivative-treated
    sarcoidosis PBMCs (n = 6) were distinguished by the formation of cellular aggregates resembling granulomas.
  explanation: Patient-cell responses to a putative mycobacterial antigen provide an experimental antigen-to-granuloma
    bridge, but the small in-vitro model does not identify an environmental trigger in vivo.
- reference: PMID:20813038
  reference_title: No evidence of altered alveolar macrophage polarization, but reduced expression of
    TLR2, in bronchoalveolar lavage cells in sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Overall, there was no evidence for alveolar macrophage polarization in sarcoidosis. However,
    there was a reduced TLR2 mRNA expression in patients with Löfgren's syndrome, which may be of relevance
    for macrophage interactions with a postulated sarcoidosis pathogen, and for the characteristics of
    the ensuing T cell response.
  explanation: Human bronchoalveolar data make TLR2 a phenotype-specific lead while directly cautioning
    against a uniform macrophage-polarization or PRR mechanism across sarcoidosis subtypes.
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

# Focused Hypothesis-Search Report
## Sarcoidosis — "Environmental Exposure × Host Susceptibility Trigger Model"

**Hypothesis ID:** `environmental_exposure_host_susceptibility_trigger_model`
**KB status entering review:** EMERGING
**Applies to subtype:** Pulmonary Sarcoidosis
**Search date:** 2026-07-26
**Databases:** PubMed (primary literature + labelled reviews). No omics/cohort data files were provided; this is a literature-grounded hypothesis evaluation.

---

## 1. Executive Judgment

**Verdict: PARTIALLY SUPPORTED (EMERGING) — retain EMERGING status; do NOT upgrade to established.**

The hypothesis decomposes into four causal claims that are supported to very different degrees:

| Sub-claim | Status | Basis |
|---|---|---|
| (a) Host genetic susceptibility (HLA class II + immune alleles) predisposes to sarcoidosis and shapes phenotype | **ESTABLISHED** | Cross-ethnic GWAS replication of HLA-DRB1/BTNL2/ANXA11/NOTCH4; strong familial aggregation |
| (b) Specific inhaled bioaerosols / inorganic particles are associated with pulmonary sarcoidosis risk | **SUPPORTED (modest effect)** | ACCESS case-control + 2026 meta-analysis (WTC dust, mould, pesticides robust; silica attenuates in high-quality studies) |
| (c) Exposure × genotype INTERACTION shapes disease onset and phenotype | **EMERGING / WEAK** | Single exploratory ACCESS analysis (p 0.10–0.15) with phenotype-specific leads; not replicated; one candidate-gene study found no dose-interaction |
| (d) A defined **exposure-specific innate sensor / antigen-presentation program** alters CD4⁺ polarization in idiopathic sarcoidosis | **SPECULATIVE / UNPROVEN** | Fully proven only for the *beryllium* paradigm (HLA-DP2); no such sensor mapped for bioaerosols/silica in idiopathic disease |

**Reasoning.** The strongest support for the *architecture* of the model is not idiopathic sarcoidosis at all but **chronic beryllium disease (CBD)** — a clinically and pathologically indistinguishable granulomatosis in which a specific inhaled inorganic particle (Be), acting only in hosts carrying HLA-DP βGlu69 alleles, engages innate chemokine production (CCL3/CCL4) and HLA-DP2-restricted presentation of Be-modified self-peptides to drive Be-specific CD4⁺ Th1 cells and granulomas (PMID 33630763, 20427584, 24912188, 20356827). This is a complete, experimentally validated exposure×genotype→innate→CD4→granuloma chain and is proof-of-principle that the model *class* is biologically real.

The **most important caveats** are: (1) CBD has a *known* antigen and a *specific* HLA restriction, so it validates the template but not its generalisation to idiopathic sarcoidosis; (2) the one direct human gene-environment interaction analysis (ACCESS, PMID 19382531) is exploratory, single-cohort, and unreplicated; (3) main-effect studies show neither the beryllium-susceptibility genotype (Glu69) nor beryllium exposure alone raises community sarcoidosis risk (PMID 25305207), so the model only survives as a genuine *interaction*; (4) no exposure-specific innate sensor has been identified in idiopathic disease, and human BAL data argue against a *uniform* macrophage-polarization/PRR mechanism (PMID 20813038); (5) exposure effect sizes are modest (OR ~1.5) and confoundable. The seed model's own hedges ("may," "remain unresolved," "does not assert one shared receptor") are appropriate and match the evidence.

---

## 2. Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 33630763 (Falta 2021) | Human + mouse mechanistic | **Supports (paradigm)** | Exposure→innate chemokine→HLA-restricted CD4 activation | Be induces CCL3/CCL4; presented as Be-modified self-peptides via HLA-DP2 to Be-specific CD4⁺ T cells; "cycle of innate and adaptive immune activation" | CBD (sarcoidosis surrogate) | High for CBD; generalisation to idiopathic disease inferential |
| 2 | 20427584 (Falta 2010) | Human/structural | **Supports (paradigm)** | Susceptibility allele acts by antigen presentation | HLA-DP alleles that present Be match those conferring genetic risk (βGlu69) | CBD | High; single antigen |
| 3 | 24912188 (Mack 2014) | Model organism (HLA-DP2 Tg mouse) | **Supports (paradigm)** | Genotype×exposure required for granuloma | BeO-exposed HLA-DP2 Tg mice develop Be-specific CD4⁺ granulomatous inflammation; WT do not; Tregs modulate | CBD model | High internal validity; models CBD not idiopathic sarcoidosis |
| 4 | 15347561 (Newman/ACCESS 2004) | Human clinical (case-control, 706 pairs) | **Supports (exposure arm)** | Bioaerosol/chemical exposures raise risk | Mould/mildew OR 1.61 (1.13–2.31); insecticides OR 1.52; agriculture OR 1.46; smoking protective OR 0.62; no single cause | Sarcoidosis (mixed) | Moderate; recall bias, modest OR, no mechanism |
| 5 | 19382531 (Rossman/ACCESS 2008) | Human clinical (G×E, 476 pairs) | **Supports (interaction arm)** | Exposure×HLA shapes onset & phenotype | DRB1*1101×insecticide → cardiac/extrapulmonary; DRB1*1101×mould → pulmonary-only (p<0.05); interactions p 0.10–0.15 | Pulmonary vs extrapulmonary | Low–moderate; exploratory thresholds, single cohort, unreplicated |
| 6 | 41963075 (Kotti 2026) | Review/meta-analysis (13 studies) | **Supports (exposure arm)** | Occupational particles raise risk | Silica, pesticides, mould, WTC dust ↑ odds; robust for WTC dust & mould; silica attenuates in high-quality studies; gold protective | Pulmonary sarcoidosis | Moderate (meta-analytic) but heterogeneity, publication/recall bias |
| 7 | 41691440 (Leite 2026) | Human clinical (case series, n=12) | **Qualifies (host modifies phenotype)** | Same exposure → divergent phenotype | Comparable silica exposure → silicosis vs sarcoidosis vs silicosarcoidosis with distinct course | Silica-exposed workers | Low (tiny n); supports host effect but not mechanism |
| 8 | 22952805 (Adrianto 2012) | Human genetic (GWAS) | **Supports (host arm)** | Host susceptibility is genetic | Replicated HLA-DRA/DRB5/DRB1, BTNL2, ANXA11 across AA & EA; novel NOTCH4 (P=6.5×10⁻¹⁰) | Cross-ethnic | High; genetics, not interaction |
| 9 | 26649486 (Ramstein 2016) | Human clinical (BAL immunology) | **Supports (downstream CD4 arm)** | Altered CD4 polarization | Th17.1 (IFN-γ⁺) cells markedly expanded in lung lavage vs controls, 2 cohorts | Pulmonary sarcoidosis | Moderate–high; effector arm, upstream trigger not identified |
| 10 | 34431542 (Lepzien 2022) | Human clinical (BAL/blood APC) | **Supports (presentation→polarization)** | APCs drive Th1/Th17.1 skewing | Patient DCs induce Tbet⁺/IFN-γ T cells more than monocytes | Pulmonary sarcoidosis | Moderate; ex vivo, antigen-nonspecific |
| 11 | 30134122 (seed; in-vitro model) | In vitro | **Qualifies** | Antigen→granuloma bridge | PPD-treated sarcoidosis PBMCs form granuloma-like aggregates vs controls (n=6 vs 5) | Sarcoidosis | Low; tiny n; PPD is a mycobacterial antigen, not an environmental trigger |
| 12 | 20813038 (Wikén 2010) | Human clinical (BAL) | **Qualifies / limits** | Uniform macrophage/PRR mechanism | No AM M1/M2 polarization difference; TLR2 reduced specifically in Löfgren; IL-17A lower in Löfgren CD4 | Löfgren vs non-Löfgren | Moderate; argues against a single shared PRR mechanism |
| 13 | 25305207 (Cherry 2015) | Human clinical (case-referent, 655/1382) | **Refutes (as main effect)** | Occult Be / Glu69 explains sarcoidosis | No ↑ sarcoidosis with Glu69 OR Be exposure as main effects; Be jobs → COPD | Community sarcoidosis | High; constrains model to interaction effects |
| 14 | 31126090 (Cleven 2019) | Human clinical (candidate-gene) | **Qualifies + partial refute** | Dose-dependent G×E | 17 HLA/non-HLA variants associate with WTC sarcoidosis; BUT no interaction between variants and WTC exposure degree | WTC-exposed | Low–moderate; small; null for dose-interaction |
| 15 | 17975675 (Wahlström 2007) | Human clinical (immunopeptidomics) | **Competing (autoimmune)** | HLA presents self-antigens | HLA-DRB1*0301 lung cells present self-peptides (vimentin, ATP synthase) to AV2S3⁺ CD4 | Löfgren/DRB1*0301 | Moderate; supports self-antigen, not environmental trigger |
| 16 | 22552860 (Oswald-Richter 2012) | Human clinical (BAL) | **Competing (antigen-persistence)** | Persistent microbial antigen drives CD4 | ESAT-6-specific CD4 IFN-γ in 17/27 sarcoidosis vs 2/14 controls (p=0.008); ESAT-6 localizes to granulomas | Sarcoidosis | Moderate; cultures negative, no live organism |
| 17 | 32941653 (Beijer 2021) | Human clinical (ELISPOT, n=201) | **Supports + competing** | Antigen class → phenotype | Metal/silica sensitization 27.6% vs 4.2% (p=0.014), tracks 5-yr fibrosis (69.2% vs 30.3%); mycobacterial→cardiac, P. acnes→skin | Fibrotic phenotype | Moderate; sensitization ≠ causation |
| 18 | 32701676 (Cinetto 2020) | Review | **Competing (amplifier)** | SAA amplifies Th17 | Locally released serum amyloid A induces pro-inflammatory Th17 program; Th17.1 hybrid → chronicity | Chronic sarcoidosis | Review-level orientation |
| 19 | 41479893 (Ucciferri 2025) | Review/framework | **Competing (microbiome)** | Dysbiosis shapes CD4 polarization | Respiratory/gut dysbiosis proposed to modify T-cell polarization & granuloma; antibiotics as modifier | Sarcoidosis | Review; correlational underlying data |
| 20 | 41257857 (Knudsen 2025) | Human clinical (WGS microbiome) | **Competing (microbiome)** | Lung dysbiosis in disease | ↑ alpha diversity & distinct beta diversity/dysbiosis index in sarcoidosis vs controls | Pulmonary sarcoidosis/ILD | Moderate; cross-sectional, causality unknown |

---

## 3. Mechanistic Causal Chain

```
[Inhaled exposure]        [Host susceptibility]
 bioaerosol / mould /      HLA class II (DRB1*11, *15, *03;
 pesticide / silica /      DP βGlu69), BTNL2, ANXA11, NOTCH4
 WTC dust / (Be)                     │
        │                           │
        ▼                           ▼
 (A) Innate sensing / particle uptake by alveolar macrophages & DCs
        │  [LINK STRONG for Be (CCL3/4 induction); INFERRED for bioaerosol/silica]
        ▼
 (B) Antigen processing & HLA-restricted presentation of exogenous
     and/or modified-self peptides (vimentin, ATP synthase; Be-CCL neoantigens)
        │  [LINK STRONG for Be/HLA-DP2 and for self-peptide identification (17975675);
        │   the specific idiopathic-sarcoidosis antigen(s) are UNKNOWN]
        ▼
 (C) CD4⁺ T-cell polarization → Th1 / Th17.1 (IFN-γ⁺), oligoclonal AV2S3⁺ expansion
        │  [LINK STRONG as a described state (26649486, 34431542); the trigger that
        │   drives it is NOT established]
        ▼
 (D) Non-caseating granuloma formation (macrophage/epithelioid/giant cells)
        │  [amplified by SAA → Th17 (32701676); Treg dysfunction]
        ▼
 (E) Clinical phenotype: pulmonary-only vs extrapulmonary/cardiac; resolving
     (Löfgren, DRB1*03) vs chronic/fibrotic (DRB1*15; inorganic sensitization)
        │  [Genotype→phenotype STRONG; exposure→phenotype EMERGING (19382531, 32941653)]
```

**Where the literature is strong:** the host-genetic node, the CD4 Th1/Th17.1 effector state, and the *entire chain for beryllium*.
**Where links are inferred:** exposure → innate sensing → HLA presentation → CD4 polarization for **non-beryllium** exposures.
**Missing causal steps:** (i) the identity of the inhaled antigen/adjuvant for idiopathic disease; (ii) an *exposure-specific* sensor/receptor (no equivalent of HLA-DP2-Be for bioaerosol/silica); (iii) a demonstrated, replicated genotype×exposure interaction with a defined effect size; (iv) longitudinal/temporal proof that exposure precedes the immune shift.

---

## 4. Knowledge Gaps (curation-relevant)

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| G1 — No exposure-specific innate sensor for idiopathic sarcoidosis | Core mechanistic edge (A→B) | The model's defining claim; without it the trigger arm is phenomenological | PubMed innate/TLR/inflammasome + silica searches; only TLR2 data found, and it is *reduced* and Löfgren-specific (20813038) | Exposure-controlled ex vivo BAL/organoid stimulation with candidate sensors knocked out; identify receptor for each exposure class |
| G2 — Gene×exposure interaction not replicated | Edge (b)+(c) | Only one exploratory analysis (19382531, p 0.10–0.15) supports it; one study found no dose-interaction (31126090) | ACCESS G×E and WTC candidate-gene studies | Large multi-ethnic biobank with genotyping + validated exposure metrics; formal interaction test with effect size |
| G3 — Antigen identity unknown | Edge (B) | Distinguishes trigger model from antigen-persistence & autoimmune models | Antigen literature (ESAT-6, P. acnes, vimentin) — candidates only, no consensus | HLA-restricted immunopeptidomics of granuloma tissue + antigen-specific tetramer tracking |
| G4 — Main-effect nulls constrain scope | Whole model | Neither Glu69 nor Be exposure alone raises community risk (25305207) | Large case-referent study | Interaction-powered designs; avoid main-effect framing |
| G5 — Directionality of dysbiosis unknown | Competing microbiome edge | Cannot tell if microbiome change is cause or consequence | Microbiome studies (41257857, 41320317) cross-sectional | Longitudinal pre/post-diagnosis sampling; gnotobiotic transfer |
| G6 — Treatment/biomarker MOA not tied to trigger | Intervention layer | No therapy targets a specific trigger; antibiotics/immunosuppression MOA microbiota-vs-immune unresolved (41479893) | Antibiotic/microbiota review | RCT with mechanistic readouts (antigen-specific T cells, microbiome) |
| G7 — Source/data absence | Curation provenance | As of search date, **no GenCC/ClinGen gene-disease curation, no interventional trial, and no public omics dataset establishing an exposure→sensor→CD4 edge** was surfaced for this specific hypothesis | Targeted PubMed only (no GenCC/ClinGen/trials DB queried directly) | Curator should query GenCC, ClinGen, ClinicalTrials.gov, GEO for direct source evidence |

---

## 5. Alternative / Competing Models

| Model | Relationship to seed | Summary & key evidence | Verdict |
|---|---|---|---|
| **Antigen-persistence / granuloma-chronicity** (mycobacterial mKatG/ESAT-6, Cutibacterium/P. acnes) | **Complementary (supplies the antigen the trigger model needs)** | ESAT-6-specific CD4 in 17/27 vs 2/14 (p=0.008, PMID 22552860); antigens localize to granulomas; P. acnes DNA enriched. Not mutually exclusive — a persistent poorly-degraded exposure product could be both trigger and chronicity driver | Partially supported; no live organism/consensus antigen |
| **Autoimmune / modified-self-antigen** (vimentin, ATP synthase) | **Parallel / downstream of presentation** | HLA-DRB1*0301 lung cells present self-peptides to AV2S3⁺ CD4 (PMID 17975675). Converges with Be model, where the antigen is *Be-modified self* (CCL3/4) | Emerging; plausible unifying "modified-self" mechanism |
| **SAA-amyloid amplification** | **Downstream amplifier, not a trigger** | Locally deposited serum amyloid A drives Th17 and self-perpetuating granuloma (PMID 32701676) | Complementary; explains chronicity not initiation |
| **Microbiome/dysbiosis** (H004) | **Parallel / upstream** | Distinct lung microbiome/mycobiome & dysbiosis index in sarcoidosis (PMID 41257857, 41320317); proposed to steer CD4 polarization (PMID 41479893) | Emerging; correlational, directionality unknown |
| **Immune-paresis / ubiquitous-antigen** (Reich) | **Alternative (denies specific trigger)** | Argues modest ORs reflect confounding; patients respond to many ubiquitous antigens due to inefficient clearance (PMID 22767391) | Sceptical null; cannot be excluded given small effect sizes |

---

## 6. Discriminating Tests

1. **HLA-stratified controlled human exposure / ex vivo challenge.** Stratify newly diagnosed pulmonary sarcoidosis by HLA-DRB1 (*03 vs *11 vs *15) and exposure history (mould vs pesticide vs silica). Challenge BAL cells / lung organoids with the matched vs mismatched exposure antigen; readout antigen-specific CD4 Th1/Th17.1 by tetramer + cytokine. *Seed-model prediction:* polarization is strongest for the matched exposure×genotype pair; *antigen-persistence prediction:* mycobacterial/P. acnes antigens dominate regardless of exposure.
2. **Granuloma immunopeptidomics + TCR tracking.** Elute HLA-DR/DP peptides from granuloma tissue across exposure-defined subgroups; test whether exposure-derived (or exposure-modified-self) peptides are presented and recognized by expanded clonotypes. Distinguishes environmental-neoantigen vs microbial-persistence vs autoimmune.
3. **Prospective at-risk cohort (occupational/WTC-type) with pre-exposure genotyping.** Longitudinal innate + adaptive immunophenotyping to establish temporal order exposure→innate activation→CD4 shift→granuloma, and to estimate a *replicated* genotype×exposure interaction effect size (resolves G2, G4).
4. **Sensor perturbation in HLA-humanized models.** In HLA-DR/DP-transgenic mice, expose to bioaerosol/silica ± candidate innate-sensor (NLRP3, TLR, C-type lectin) knockouts; test whether granuloma requires a specific sensor per exposure class (resolves G1). *Prediction:* exposure-specific, not shared, sensor dependence.
5. **Microbiome causality.** Longitudinal pre/post-diagnosis microbiome + gnotobiotic transfer of patient microbiota into HLA-humanized mice; test whether dysbiosis is sufficient to skew CD4 polarization (discriminates H004 from inhaled-trigger model).

---

## 7. Curation Leads (require curator verification)

**Status recommendation:** **Keep `EMERGING`.** Evidence supports the *host-susceptibility* node (established) and a *modest environmental-exposure* association (supported), but the defining *exposure-specific-sensor × genotype → CD4 polarization* edge is unproven for idiopathic disease. Do **not** curate any exposure-specific trigger edge as causal yet.

**Candidate evidence references + verbatim snippets to verify:**
- PMID 33630763 — "we demonstrate a direct link between Be-induced innate production of chemokines and the development of a robust adaptive immune response to those same chemokines presented as Be-modified self-peptides, creating a cycle of innate and adaptive immune activation." → *proof-of-principle for the model class (label: paradigm/surrogate = CBD).*
- PMID 20427584 — "The HLA-DP alleles that present Be to T cells match those implicated in the genetic susceptibility…" → *host-susceptibility-acts-by-presentation edge.*
- PMID 19382531 — "HLA DRB1*1101 and insecticide exposure at work was associated with extrapulmonary sarcoidosis…and…molds and musty odors was associated with pulmonary only sarcoidosis (P < 0.05)." → *exposure×genotype→phenotype lead (label EMERGING, exploratory p).*
- PMID 41963075 — "occupational silica, pesticides, mould/mildew and World Trade Center…dust exposures were associated with increased odds…robustness…for WTC dust and mould, whereas…silica appeared attenuated in high-quality studies." → *meta-analytic exposure-arm support with class specificity.*
- PMID 25305207 — "No increase in sarcoidosis was seen with either Glu69 or beryllium exposure…as main effects." → *constraint: model is interaction-only (add as knowledge_gap/conflict).*
- PMID 31126090 — "we did not find statistical evidence of an interaction between common variants and the degree of WTC exposure." → *failed dose-interaction (conflict note).*
- PMID 20813038 — "there was no evidence for alveolar macrophage polarization…reduced TLR2 mRNA expression in patients with Löfgren's syndrome." → *limits uniform-PRR mechanism; subtype restriction.*

**Candidate pathophysiology nodes/edges (leads):**
- Node: *inhaled bioaerosol/inorganic particle (exposure)* → Node: *alveolar macrophage/DC innate sensing* → Node: *HLA class II-restricted (modified-self) antigen presentation* → Node: *CD4⁺ Th1/Th17.1 polarization* → Node: *non-caseating granuloma* → Node: *pulmonary vs extrapulmonary phenotype*. Mark edges A→B and B→C as **INFERRED/UNCONFIRMED** for non-beryllium exposures.
- Modifier edges: *HLA-DRB1\*03 → resolving/Löfgren*; *HLA-DRB1\*15 → chronic/fibrotic*; *inorganic sensitization → fibrotic phenotype* (PMID 32941653); *SAA → Th17 amplification* (PMID 32701676).

**Candidate ontology terms:**
- Cell types: CD4-positive Th1 cell; T-helper 17 cell (Th17.1/IFN-γ⁺ subset); alveolar macrophage; conventional dendritic cell; epithelioid/multinucleated giant cell; regulatory T cell.
- Biological processes: antigen processing and presentation via MHC class II; innate immune response / pattern-recognition receptor signaling; CD4⁺ T-cell differentiation; granuloma formation; type II hypersensitivity to metals.
- Genes/molecules: HLA-DRB1, HLA-DPB1, BTNL2, ANXA11, NOTCH4, TLR2, CCL3/CCL4, SAA, IFNG, IL17A.

**Candidate subtype restrictions:** interaction/phenotype leads are strongest for **pulmonary vs cardiac/extrapulmonary** split and **Löfgren (acute/resolving) vs chronic-fibrotic**; inorganic-antigen sensitization is a lead specifically for the **fibrotic** phenotype.

**Candidate knowledge_gaps / discussion prompts:** G1 (missing exposure-specific sensor), G2 (unreplicated G×E), G3 (unknown antigen), G4 (main-effect nulls → interaction-only), G7 (no GenCC/ClinGen/trial/omics source directly establishing the trigger edge as of search date — curator should confirm by querying those sources).

---

## 8. Limitations of this search

- Literature-only; no primary omics/cohort data were analysed.
- PubMed was the sole database queried; GenCC, ClinGen, ClinicalTrials.gov, and GEO/omics repositories were **not** directly queried (see G7) — their absence is a *lead to check*, not a confirmed absence.
- Several supporting studies are small (n≤27) or exploratory; effect sizes are modest and vulnerable to recall/selection bias.
- Beryllium evidence, while mechanistically decisive, describes a *surrogate* disease with a known antigen and cannot be assumed to generalise.

---

*Prepared for the Disorder Mechanisms Knowledge Base — hypothesis-level review. All curation leads require human verification.*


## Artifacts

- [OpenScientist evidence matrix](openscientist_artifacts/evidence_matrix.csv)
- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist knowledge gaps](openscientist_artifacts/knowledge_gaps.csv)
- [OpenScientist mechanistic diagram](openscientist_artifacts/mechanistic_diagram.md)
