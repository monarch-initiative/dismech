---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-23T23:18:41.310274'
end_time: '2026-05-23T23:35:47.345613'
duration_seconds: 1026.04
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Fabry disease
  category: Mendelian
  hypothesis_group_id: canonical_gla_deficiency_gb3_lysosomal_storage_model
  hypothesis_label: "Canonical \u03B1-Galactosidase A / Gb3 Lysosomal Storage Model"
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_gla_deficiency_gb3_lysosomal_storage_model\n\
    hypothesis_label: Canonical \u03B1-Galactosidase A / Gb3 Lysosomal Storage Model\n\
    status: CANONICAL\ndescription: Fabry disease is an X-linked lysosomal storage\
    \ disorder caused by loss-of-function variants\n  in GLA on Xq22.1 encoding the\
    \ lysosomal enzyme \u03B1-galactosidase A (\u03B1-Gal A). Loss of \u03B1-Gal A\
    \ catalytic\n  activity prevents lysosomal hydrolysis of globotriaosylceramide\
    \ (Gb3) and related glycosphingolipids,\n  leading to progressive accumulation\
    \ in lysosomes of vascular endothelium, podocytes, cardiomyocytes,\n  dorsal root\
    \ ganglion neurons, and other cell types. Substrate accumulation causes endothelial\
    \ dysfunction,\n  microvascular ischemia, cardiomyopathy, progressive renal failure,\
    \ small-fiber neuropathy, and stroke.\n  Enzyme replacement therapy (agalsidase\
    \ alfa/beta), pharmacological chaperone therapy (migalastat for\n  amenable mutations),\
    \ and substrate reduction trials all corroborate the \u03B1-Gal A deficiency /\
    \ Gb3 accumulation\n  axis as the canonical pathogenic mechanism.\nevidence:\n\
    - reference: PMID:28613767\n  reference_title: 'Fabry disease revisited: Management\
    \ and treatment recommendations for adult patients.'\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Fabry disease represents an X-linked, multisystem\
    \ lysosomal storage disorder caused by defective\n    function of the enzyme alpha-galactosidase\
    \ A (\u03B1-Gal A).\n  explanation: |\n    Canonical mechanism reference used\
    \ as the seed for the hypothesis-search deep-research run."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 61
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Fabry disease
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_gla_deficiency_gb3_lysosomal_storage_model
- **Hypothesis Label:** Canonical α-Galactosidase A / Gb3 Lysosomal Storage Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_gla_deficiency_gb3_lysosomal_storage_model
hypothesis_label: Canonical α-Galactosidase A / Gb3 Lysosomal Storage Model
status: CANONICAL
description: Fabry disease is an X-linked lysosomal storage disorder caused by loss-of-function variants
  in GLA on Xq22.1 encoding the lysosomal enzyme α-galactosidase A (α-Gal A). Loss of α-Gal A catalytic
  activity prevents lysosomal hydrolysis of globotriaosylceramide (Gb3) and related glycosphingolipids,
  leading to progressive accumulation in lysosomes of vascular endothelium, podocytes, cardiomyocytes,
  dorsal root ganglion neurons, and other cell types. Substrate accumulation causes endothelial dysfunction,
  microvascular ischemia, cardiomyopathy, progressive renal failure, small-fiber neuropathy, and stroke.
  Enzyme replacement therapy (agalsidase alfa/beta), pharmacological chaperone therapy (migalastat for
  amenable mutations), and substrate reduction trials all corroborate the α-Gal A deficiency / Gb3 accumulation
  axis as the canonical pathogenic mechanism.
evidence:
- reference: PMID:28613767
  reference_title: 'Fabry disease revisited: Management and treatment recommendations for adult patients.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Fabry disease represents an X-linked, multisystem lysosomal storage disorder caused by defective
    function of the enzyme alpha-galactosidase A (α-Gal A).
  explanation: |
    Canonical mechanism reference used as the seed for the hypothesis-search deep-research run.
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Fabry disease
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_gla_deficiency_gb3_lysosomal_storage_model
- **Hypothesis Label:** Canonical α-Galactosidase A / Gb3 Lysosomal Storage Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_gla_deficiency_gb3_lysosomal_storage_model
hypothesis_label: Canonical α-Galactosidase A / Gb3 Lysosomal Storage Model
status: CANONICAL
description: Fabry disease is an X-linked lysosomal storage disorder caused by loss-of-function variants
  in GLA on Xq22.1 encoding the lysosomal enzyme α-galactosidase A (α-Gal A). Loss of α-Gal A catalytic
  activity prevents lysosomal hydrolysis of globotriaosylceramide (Gb3) and related glycosphingolipids,
  leading to progressive accumulation in lysosomes of vascular endothelium, podocytes, cardiomyocytes,
  dorsal root ganglion neurons, and other cell types. Substrate accumulation causes endothelial dysfunction,
  microvascular ischemia, cardiomyopathy, progressive renal failure, small-fiber neuropathy, and stroke.
  Enzyme replacement therapy (agalsidase alfa/beta), pharmacological chaperone therapy (migalastat for
  amenable mutations), and substrate reduction trials all corroborate the α-Gal A deficiency / Gb3 accumulation
  axis as the canonical pathogenic mechanism.
evidence:
- reference: PMID:28613767
  reference_title: 'Fabry disease revisited: Management and treatment recommendations for adult patients.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Fabry disease represents an X-linked, multisystem lysosomal storage disorder caused by defective
    function of the enzyme alpha-galactosidase A (α-Gal A).
  explanation: |
    Canonical mechanism reference used as the seed for the hypothesis-search deep-research run.
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


# Hypothesis-Search Report: canonical_gla_deficiency_gb3_lysosomal_storage_model (Fabry disease)

**Seed hypothesis:** Loss-of-function variants in **GLA** cause **α-galactosidase A (α-Gal A)** deficiency, leading to lysosomal accumulation of **globotriaosylceramide (Gb3/GL-3)** and related lipids (including **globotriaosylsphingosine, lyso-Gb3**), driving multi-organ injury; disease-modifying therapies (ERT, migalastat, emerging gene/SRT) validate the axis.

**Search date:** 2026-05-24 (tools executed against 2023–2025 primary/review literature and ClinicalTrials.gov records).

## Executive Judgment

**Verdict: Supported (canonical) but mechanistically incomplete as a storage-only model.**

Intervention-based evidence strongly supports **α-Gal A restoration → reduced Gb3/lyso-Gb3 burden** in disease-relevant tissues, including electron-microscopy reduction of storage inclusions in preclinical gene therapy models and dose-/cell-type–dependent tissue substrate clearance with enzyme-based therapies. (jeyakumar2023preclinicalevaluationof pages 11-14, jeyakumar2023preclinicalevaluationof pages 10-11, zhang2024fabrynephropathyfocus pages 3-5, germain2024pegunigalsidasealfaa pages 1-2)

However, multiple 2023–2024 sources indicate that **downstream programs (inflammation, oxidative stress/NO dysregulation, ER stress/UPR (“agalopathy”), autophagy-lysosomal dysfunction, fibrosis)** can persist despite biochemical improvement and may become partially **self-sustaining**, limiting reversibility in advanced disease. (feriozzi2024theinflammatorypathogenetic pages 5-7, faro2024inflammationoxidativestress pages 12-13, faro2024inflammationoxidativestress pages 13-15, feriozzi2024theinflammatorypathogenetic pages 1-3)

## 1) Key Concepts and Definitions (current mechanistic understanding)

### Core biochemical entities

* **α-Gal A (GLA product):** lysosomal hydrolase required to catabolize Gb3; deficiency leads to substrate accumulation. (bertoldi2023biochemicalmechanismsbeyond pages 1-3, kugadas2024cardiacmanifestationsof pages 1-2)
* **Gb3 (GL-3):** canonical stored glycosphingolipid; accumulates in multiple cell types and is visible as lamellar/zebra bodies by electron microscopy in Fabry nephropathy. (zhang2024fabrynephropathyfocus pages 3-5)
* **Lyso-Gb3 (globotriaosylsphingosine):** deacylated Gb3 derivative; often correlates with severity and is widely used as a **pharmacodynamic biomarker** of therapy response, but may also be a **bioactive mediator**. (nikolaenko2023elucidatingthetoxic pages 1-1, germain2024pegunigalsidasealfaa pages 5-6)

### Cell types and tissues best explained by the canonical model

The storage model most directly explains disease features in tissues/cell types with clear substrate deposition and/or strong dependence on lysosome/autophagy integrity:

* **Kidney:** podocytes, glomerular endothelial/mesangial cells, tubular epithelium—Gb3 inclusions and podocyte injury are central, and renal decline is a key endpoint in trials. (zhang2024fabrynephropathyfocus pages 3-5, wallace2024headtoheadtrialof pages 2-3)
* **Vasculature:** endothelial and smooth muscle dysfunction linked to substrate-related signaling (NO/ROS imbalance, adhesion molecules). (faro2024inflammationoxidativestress pages 10-12)
* **Heart:** cardiomyocyte and microvascular involvement; substrate accumulation can be linked to measurable functional changes in animal models, but human cardiomyopathy progression often requires secondary mechanisms (fibrosis/inflammation). (kugadas2024cardiacmanifestationsof pages 1-2, bertoldi2023biochemicalmechanismsbeyond pages 1-3)
* **Peripheral nervous system:** small-fiber neuropathy/pain plausibly linked to bioactive lipid effects and cellular stress signaling. (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 2-3)

## 2) Strongest Direct Evidence for the Hypothesis

### A. Direct “perturbation–rescue” evidence (gene therapy preclinical)

**FLT190 liver-directed AAV gene therapy (preclinical) provides the strongest mechanistic rescue evidence**: restoring GLA expression produces secreted α-Gal A that is taken up by Fabry-relevant target cells with lysosomal localization, and reduces Gb3/lyso-Gb3 in multiple tissues with EM evidence of reduced storage inclusions in kidney and heart. (jeyakumar2023preclinicalevaluationof pages 4-6, jeyakumar2023preclinicalevaluationof pages 1-2, jeyakumar2023preclinicalevaluationof pages 11-14, jeyakumar2023preclinicalevaluationof pages 10-11)

This supports the causal chain:

GLA restoration → ↑α-Gal A in plasma/tissues → lysosomal delivery → ↓Gb3/lyso-Gb3 → reduction of storage pathology. (jeyakumar2023preclinicalevaluationof pages 11-14, jeyakumar2023preclinicalevaluationof pages 10-11)

### B. Human therapeutic evidence linking enzyme replacement to organ function and biomarkers (2024)

**BALANCE phase III head-to-head trial (pegunigalsidase alfa vs agalsidase beta; 2 years)**: renal function decline (annualized eGFR slope) improved from steep pre-trial deterioration to ~−2 to −3 mL/min/1.73 m²/year and the primary non-inferiority endpoint was met; importantly, biomarker behavior (lyso-Gb3 increases) tracked with risk features such as higher proteinuria and antidrug antibodies in a treated population. (wallace2024headtoheadtrialof pages 1-1, germain2024pegunigalsidasealfaa pages 5-6)

Key numeric results (mechanistic/clinical anchors):

* ITT difference in median eGFR slope: **−0.36 mL/min/1.73 m²/year** (95% CI −2.44 to 1.73), non-inferior vs margin. (wallace2024headtoheadtrialof pages 1-1, germain2024pegunigalsidasealfaa pages 5-6)
* In males at 24 months, median plasma lyso-Gb3 change differed by arm (directionally rising in the pegunigalsidase group in this analysis and decreasing in the agalsidase beta group), and rises were associated with **proteinuria and anti-drug antibodies**, linking biomarker control to treatment pharmacology/immunogenicity. (germain2024pegunigalsidasealfaa pages 5-6)

Interpretation: this trial supports the enzyme/substrate axis as therapeutic target engagement, but also underscores that **plasma lyso-Gb3 is not a complete surrogate** for organ-level progression in advanced, previously treated disease. (germain2024pegunigalsidasealfaa pages 5-6, faro2024inflammationoxidativestress pages 12-13)

### C. Histology/EM evidence of tissue Gb3 clearance (2024)

Kidney-focused 2024 syntheses report that sustained agalsidase β can effectively clear Gb3 from **glomerular endothelial and mesangial cells**, while **podocyte clearance is dose-dependent and often incomplete**, consistent with a terminally differentiated, slow-turnover compartment. (zhang2024fabrynephropathyfocus pages 3-5, west2024fabrynephropathya pages 18-20)

## 3) Evidence Against, Non-reproduction, or Scope Limits

No evidence in the checked corpus refutes the upstream biochemical claim that α-Gal A deficiency leads to substrate accumulation. The strongest “against/limits” evidence instead challenges the *sufficiency* of storage to explain later-stage disease and treatment resistance:

1) **Persistence after substrate reduction (“point of no return”)**: renal sources describe models where Gb3 can be cleared yet altered signaling/lysosomal defects persist, suggesting secondary programs can become partly autonomous. (feriozzi2024theinflammatorypathogenetic pages 5-7, feriozzi2024theinflammatorypathogenetic pages 9-11)

2) **Disproportionate pathology vs measured storage**: vascular remodeling and endothelial dysfunction are emphasized as involving oxidative stress and inflammation, and vascular wall changes may appear disproportionate to lipid deposits, implying additional mediators. (faro2024inflammationoxidativestress pages 13-15)

3) **Animal model incompleteness**: standard GlaKO mice accumulate substrate but show relatively mild disease; a high-Gb3 model (G3Stg/GlaKO) increases pathology but may introduce non-physiologic artifacts. This limits direct inference that storage alone is sufficient for the full human phenotype. (kugadas2024cardiacmanifestationsof pages 1-2)

4) **Agalopathy (misfolded mutant α-Gal A → ER stress/UPR)**: renal inflammatory syntheses propose that some missense variants induce ER stress and inflammatory signaling independent of bulk storage, potentially explaining heterogeneity and incomplete response. (feriozzi2024theinflammatorypathogenetic pages 1-3, feriozzi2024theinflammatorypathogenetic pages 9-11)

## 4) Recent Developments / Latest Research (prioritizing 2023–2024)

### (i) Lyso-Gb3 as an active mediator (2023 primary)

A key 2023 mechanistic advance is direct demonstration that lyso-Gb3 can drive **proteostasis/ubiquitination/translation-folding perturbations** in a neuronal model at concentrations chosen to mimic patient serum (20 and 200 ng/mL), and can bind chaperone systems (HSP90/HSP60/TRiC). This supports a “bioactive lyso-Gb3” extension to the canonical model, especially relevant to neuropathic features. (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 5-6)

### (ii) Inflammation and immune signaling integrated into Fabry mechanism (2024 syntheses)

2024 reviews consolidate evidence that stored/derived lipids act as **ligands** (e.g., Gb3→TLR4→Notch1/NF-κB) and that lyso-Gb3 may enhance **TGF-β–linked profibrotic programs**, bridging storage to chronic inflammation/fibrosis. (coelhoribeiro2024inflammationandexosomes pages 7-9, kurdi2024inflammationinfabry pages 7-8)

### (iii) Vascular/endothelial dysfunction and oxidative stress emphasized (2024)

A 2024 vascular-focused synthesis links substrate accumulation to **NO dysregulation**, **ROS**, and **smooth muscle proliferation**, and notes persistence of inflammatory/oxidative markers despite long-term therapy—supporting secondary, potentially self-sustaining drivers of vasculopathy. (faro2024inflammationoxidativestress pages 10-12, faro2024inflammationoxidativestress pages 12-13)

### (iv) ERT innovation: pegylated α-Gal A and immunogenicity as a mechanistic modifier (2024)

BALANCE (2024) provides contemporary human RCT evidence where renal outcomes were similar across two ERTs but differences in tolerability and antibody patterns exist. It reinforces that **immunogenicity and proteinuria** can modulate pharmacodynamics (including lyso-Gb3 behavior), affecting mechanistic “target engagement.” (wallace2024headtoheadtrialof pages 6-7, germain2024pegunigalsidasealfaa pages 5-6)

## 5) Current Applications and Real-World Implementations

### A. Enzyme replacement therapy (ERT) in practice

ERT is implemented as repeated IV infusion; mechanistic goals are restoring α-Gal A activity and reducing Gb3/lyso-Gb3. In treated populations with renal deterioration, switching/comparator RCT evidence shows eGFR slope stabilization consistent with “enzyme augmentation slows substrate-driven injury,” while also highlighting limitations in advanced disease and the role of antibodies. (wallace2024headtoheadtrialof pages 1-1, wallace2024headtoheadtrialof pages 6-7)

### B. Migalastat (oral chaperone) for amenable variants

Migalastat is used for patients with **amenable** GLA variants; it stabilizes mutant α-Gal A for lysosomal trafficking and can raise measured α-Gal A activity and reduce/stabilize lyso-Gb3, with cardiac mass benefits in several studies. (perretta2023fabrydiseaseswitch pages 1-2, perretta2023fabrydiseaseswitch pages 2-3)

Real-world/switch evidence summarized in 2023 indicates:

* α-Gal A activity increases (e.g., **0.06–0.2 nmol/min/mg; p=0.001** in a cohort), supporting mechanistic target engagement. (perretta2023fabrydiseaseswitch pages 2-3)
* Lyso-Gb3 decreases in treatment-naïve patients (e.g., **10.9→6.0 ng/mL; p=0.021**) but may be stable after switching from ERT. (perretta2023fabrydiseaseswitch pages 2-3)

Expert consensus (2023) explicitly cautions that **α-Gal A and lyso-Gb3 pharmacodynamic thresholds are not fully reliable**, recommending holistic clinical monitoring and serial lyso-Gb3 measurements as supportive rather than definitive markers. (bichet2023consensusrecommendationsfor pages 11-13, bichet2023consensusrecommendationsfor pages 1-2)

### C. Gene therapy trials as mechanistic tests in humans

ClinicalTrials.gov records show in vivo liver-directed gene therapy is explicitly framed as sustained α-Gal A production; mechanistic validation includes serial measurement of **plasma α-Gal A activity** (STAAR; NCT04046224). (NCT04046224 chunk 1)

*STAAR (ST-920; NCT04046224)* is a dose-ranging AAV2/6 GLA gene therapy study with planned plasma α-Gal A activity measurement at defined timepoints (e.g., change from baseline at Week 24 and Week 52/EOS). (NCT04046224 chunk 1)

*FLT190 first-in-human trial (NCT04040049)* is terminated due to sponsor portfolio reprioritization (pause to focus on FLT201), not due to a stated mechanistic failure in the provided excerpt; the record includes biomarker monitoring such as plasma αGLA activity and extensive safety monitoring including vector shedding. (NCT04040049 chunk 1)

## Evidence Matrix (artifact)

| Citation (PMID if known else DOI) | Publication date | Evidence type | Supports / refutes / qualifies / competing | Mechanistic claim tested | Key finding (1-2 sentences) | Subtype / context / tissue | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| Nikolaenko et al., *Hum Mol Genet* (DOI: 10.1093/hmg/ddad073) | 2023-05 | In vitro proteomics / cell model | Qualifies (supports upstream metabolite toxicity while extending beyond storage-only) | Lyso-Gb3 is not just a biomarker of α-Gal A deficiency but a direct toxic effector that perturbs cellular pathways downstream of GLA loss | In SH-Sy5y neuronal cells, lyso-Gb3 at concentrations modeling mild and classical Fabry serum levels (20 and 200 ng/mL) increased protein ubiquitination and disrupted protein translation/folding; affinity capture identified direct binding to chaperones including HSP90, HSP60, and TRiC. This supports the canonical GLA→lyso-Gb3 axis while showing that disease propagation includes proteostasis/ER-stress signaling, not only lysosomal engorgement. (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 5-6) | Neuronal model; relevance to neuropathic pain and broader cellular stress in Fabry disease | **Moderate-high** for direct lyso-Gb3 cellular toxicity; limited by use of a neuroblastoma cell line and lack of direct human tissue causal confirmation. |
| Jeyakumar et al., *Gene Therapy* (DOI: 10.1038/s41434-022-00381-y) | 2023-01 | Preclinical gene therapy; in vitro + mouse/NHP | Supports | Restoring GLA expression and circulating α-Gal A should enable uptake into affected cells, lysosomal delivery, and substrate clearance if the canonical model is correct | Liver-directed AAV-FLT190 produced dose-dependent plasma α-Gal A, uptake into Fabry-relevant kidney, podocyte, cardiomyocyte, and fibroblast targets, and lysosomal localization; in Fabry mice it reduced plasma/urine/kidney/heart Gb3 and lyso-Gb3 and reduced storage inclusions by EM. This is strong intervention-based support for the causal chain from enzyme deficiency to substrate accumulation. (jeyakumar2023preclinicalevaluationof pages 4-6) | Fabry mouse model, non-human primates, Fabry-relevant target cells; kidney and heart | **High** for mechanistic rescue of storage phenotype; limited by preclinical setting and incomplete proof that all human organ injury is reversible with substrate correction. |
| Kugadas et al., *PLOS ONE* (DOI: 10.1371/journal.pone.0304415) | 2024-05 | Model organism; longitudinal mouse phenotyping | Supports, with qualifications | Progressive Gb3/lyso-Gb3 accumulation is sufficient to drive at least early cardiac abnormalities in vivo | GlaKO mice showed progressive substrate accumulation with mild cardiomegaly, increased LV mass, wider LV cavity, and reduced global longitudinal strain, while G3Stg/GlaKO mice had higher substrate loads and more pathology. However, standard GlaKO mice show only modest disease and some G3Stg/GlaKO features diverge from human cardiomyopathy, limiting simple translation. (kugadas2024cardiacmanifestationsof pages 1-2) | Cardiac disease modeling; early Fabry cardiomyopathy; mouse heart | **Moderate**; useful in vivo support for substrate-linked cardiac effects, but mouse models incompletely recapitulate human multisystem disease. |
| Wallace et al., *J Med Genet* (DOI: 10.1136/jmg-2023-109445) | 2024-11 | Human clinical trial (phase III randomized head-to-head) | Supports, with qualifications | Increasing α-Gal A activity by ERT should stabilize organ function and modify substrate biomarkers if enzyme deficiency/storage is central | In BALANCE, pegunigalsidase alfa was non-inferior to agalsidase beta for annualized eGFR slope over 2 years (difference in median slope −0.36 mL/min/1.73 m²/year; 95% CI −2.44 to 1.73), and both arms showed minimal overall lyso-Gb3 change after prior long-term ERT exposure. Neutralizing antibodies and proteinuria tracked with worse biomarker behavior, indicating that target engagement matters but also that renal decline is not fully explained by plasma substrate alone in advanced disease. (germain2024pegunigalsidasealfaa pages 5-6, wallace2024headtoheadtrialof pages 2-3, wallace2024headtoheadtrialof pages 6-7, wallace2024headtoheadtrialof pages 1-1) | Adults with Fabry disease and deteriorating renal function already treated with agalsidase beta; kidney | **High** for clinical relevance; limited because this is a switch/comparator trial in previously treated, relatively advanced patients rather than an untreated natural-history test of the canonical mechanism. |
| Germain & Linhart, *Front Genet* (DOI: 10.3389/fgene.2024.1395287) | 2024-04 | Review-level clinical synthesis | Supports | Existing ERT clinical data collectively validate the enzyme deficiency/storage model and show that improved enzyme pharmacology can maintain renal outcomes | Review synthesis of phase 1/2 and phase 3 pegunigalsidase data notes prior renal capillary endothelial Gb3 clearance and BALANCE non-inferiority for kidney decline, consistent with the idea that augmenting α-Gal A reduces substrate burden and slows disease. It also notes residual limitations such as hypersensitivity and immune-complex events. (germain2024pegunigalsidasealfaa pages 1-2) | Treated adult Fabry disease; renal/capillary endothelial context | **Moderate** because it is secondary literature; useful corroboration but not primary evidence. |
| Coelho-Ribeiro et al., *Cells* (DOI: 10.3390/cells13080654) | 2024-04 | Review-level mechanistic synthesis | Qualifies | Gb3/lyso-Gb3 accumulation activates immune/inflammatory signaling pathways that help connect storage to tissue injury | Synthesized evidence indicates Gb3 can activate TLR4 and downstream Notch1/NF-κB signaling, while lyso-Gb3 enhances TGF-β1 and other inflammatory/profibrotic mediators; clinical inflammatory markers associate with LVH and renal disease. This supports the canonical storage trigger but argues that pathogenesis is mediated through active signaling and immune crosstalk rather than passive storage alone. (coelhoribeiro2024inflammationandexosomes pages 7-9) | Immune cells, macrophages, cardiovascular and renal involvement | **Moderate**; broad and mechanistically helpful, but mostly review-level and dependent on cited primary studies. |
| Faro et al., *Int J Mol Sci* (DOI: 10.3390/ijms25158273) | 2024-07 | Review-level mechanistic/vascular synthesis | Qualifies | Vascular complications arise from Gb3/lyso-Gb3-driven endothelial dysfunction, oxidative stress, and inflammatory remodeling downstream of enzyme deficiency | The review links substrate accumulation to reduced NO bioavailability, ROS generation, eNOS dysregulation, ROCK activation, smooth-muscle proliferation, and fibrotic vascular remodeling; it also notes persistent inflammatory/oxidative markers despite ERT and disproportionate vascular wall changes relative to stored lipid. Thus, the canonical storage model explains initiation, but secondary vascular mechanisms are needed to explain progression. (faro2024inflammationoxidativestress pages 10-12, faro2024inflammationoxidativestress pages 12-13, faro2024inflammationoxidativestress pages 13-15) | Vascular endothelium, smooth muscle, macro- and microvasculature; cardiac/cerebrovascular risk | **Moderate**; strong biologic plausibility but largely review synthesis rather than new direct perturbation data. |
| Feriozzi & Rozenfeld, *Rare Disease and Orphan Drugs Journal* (DOI: 10.20517/rdodj.2023.37) | 2024-04 | Review-level mechanistic synthesis with cited primary renal data | Qualifies / competing-complementary | Fabry nephropathy is initiated by Gb3/lyso-Gb3 storage but may become self-sustaining via inflammation, oxidative stress, mitochondrial dysfunction, autophagy defects, and ER-stress “agalopathy” | The review summarizes evidence that Gb3 clearance can fail to restore altered cytokine signaling or lysosomal function in podocytes, identifies persistent mitochondrial/autophagic injury in tubular cells, and highlights ER-stress from misfolded mutant α-Gal A as a parallel mechanism. It therefore limits the scope of a storage-only model, especially in advanced renal disease. (feriozzi2024theinflammatorypathogenetic pages 5-7, feriozzi2024theinflammatorypathogenetic pages 1-3, feriozzi2024theinflammatorypathogenetic pages 9-11) | Fabry nephropathy; podocytes, tubular cells, renal interstitium | **Moderate**; highly relevant to disease-stage limits, but several claims are review-mediated and some cited primary studies were not directly inspected here. |
| Kurdi et al., *Front Cardiovasc Med* (DOI: 10.3389/fcvm.2024.1420067) | 2024-06 | Review-level mechanistic synthesis | Qualifies | Inflammation has stage-specific roles in Fabry disease and may persist despite treatment, linking storage to fibrosis and incomplete reversibility | The review synthesizes data showing lyso-Gb3 can induce TGF-β1 and SMAD signaling, proteostasis stress, apoptosis, macrophage recruitment/polarization changes, and autoinflammatory-like features. It is especially useful for explaining why therapy is less effective once fibrosis/inflammatory programs are established, despite correction of the primary enzymatic defect. (kurdi2024inflammationinfabry pages 7-8) | Cardiovascular emphasis; systemic inflammation; fibrosis-prone stages | **Moderate**; important conceptual qualifier, but primarily interpretive synthesis rather than direct causal proof. |


*Table: This evidence matrix summarizes key supporting and qualifying evidence for the canonical α-Gal A deficiency/Gb3 lysosomal storage model in Fabry disease. It highlights where direct intervention and biomarker data strongly support the model and where newer inflammatory, proteostatic, and vascular findings limit a simple storage-only interpretation.*

## Mechanistic Causal Chain (with strength of evidence)

### Canonical chain

1) **GLA loss-of-function → α-Gal A deficiency** (established, canonical; assumed background across sources). (bertoldi2023biochemicalmechanismsbeyond pages 1-3)

2) **α-Gal A deficiency → lysosomal Gb3 accumulation and lyso-Gb3 generation** (strong): animal and clinical pathology literature consistently describe Gb3/lyso-Gb3 as the accumulating substrates and core biomarkers. (kugadas2024cardiacmanifestationsof pages 1-2, zhang2024fabrynephropathyfocus pages 3-5)

3) **Substrate accumulation in specific cells (endothelium, podocytes, cardiomyocytes, neurons) → cellular dysfunction** (strong-to-moderate):

* Direct intervention support: gene therapy restoring α-Gal A reduces tissue Gb3/lyso-Gb3 and reduces EM inclusions in kidney/heart. (jeyakumar2023preclinicalevaluationof pages 11-14, jeyakumar2023preclinicalevaluationof pages 10-11)
* Cell-biologic extension: lyso-Gb3 has direct non-lysosomal effects on proteostasis and chaperone binding, supporting additional cytotoxic mechanisms. (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 5-6)

4) **Cellular dysfunction → organ pathology (renal decline, cardiomyopathy, vasculopathy, neuropathic pain)** (moderate; stage-dependent):

* Renal function stabilization in advanced treated patients supports continued mechanistic relevance. (wallace2024headtoheadtrialof pages 1-1)
* Cardiac changes are detectable in substrate-accumulating mice, but models incompletely recapitulate human phenotypes, indicating missing modifiers. (kugadas2024cardiacmanifestationsof pages 1-2)
* Vascular dysfunction appears to be mediated by oxidative stress/NO imbalance and inflammation, partly downstream and potentially self-amplifying. (faro2024inflammationoxidativestress pages 10-12)

### Where the chain is inferred or incomplete

* The step from **substrate reduction → reversal of established fibrosis/inflammation** is weak/variable: multiple sources emphasize incomplete reversibility and persistence of downstream signaling defects after Gb3 clearance in some models. (feriozzi2024theinflammatorypathogenetic pages 5-7, faro2024inflammationoxidativestress pages 12-13)

## Knowledge Gaps (curation-relevant)

| Gap/unknown | Why it matters for the hypothesis | What evidence was checked here (cite context IDs) | Current best interpretation (supporting/limiting) | Discriminating experiment or dataset needed |
|---|---|---|---|---|
| Whether lysosomal Gb3 accumulation alone is sufficient to explain progressive organ failure once fibrosis/inflammation are established | The seed hypothesis implies a largely storage-driven chain; if disease becomes self-sustaining after secondary pathway activation, the canonical model is true but incomplete for later-stage causality and treatment response | Podocyte/tubular and review-synthesized evidence that Gb3 clearance may not restore cytokine signaling, lysosomal function, or structural damage; persistent inflammatory/oxidative markers despite ERT (feriozzi2024theinflammatorypathogenetic pages 5-7, faro2024inflammationoxidativestress pages 10-12, feriozzi2024theinflammatorypathogenetic pages 1-3, feriozzi2024theinflammatorypathogenetic pages 9-11, kurdi2024inflammationinfabry pages 7-8, faro2024inflammationoxidativestress pages 12-13) | **Limiting**: strong support that storage is upstream, but substantial evidence suggests later disease is partly maintained by downstream inflammatory, fibrotic, oxidative, and autophagy-related programs | Longitudinal paired biopsies/omics before and after potent substrate correction (e.g., gene therapy or highly effective ERT), with matched plasma/tissue Gb3/lyso-Gb3 and fibrosis/inflammation readouts |
| Relative causal role of Gb3 versus lyso-Gb3 in tissue injury | The canonical model centers on Gb3 storage, but newer work suggests lyso-Gb3 may be an active signaling/toxic mediator, changing which node should be modeled as the main effector | Experimental lyso-Gb3 proteomics and binding studies; vascular/inflammatory syntheses citing direct lyso-Gb3 signaling effects (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 1-2, nikolaenko2023elucidatingthetoxic pages 5-6, nikolaenko2023elucidatingthetoxic pages 2-3, nikolaenko2023elucidatingthetoxic pages 3-4, nikolaenko2023elucidatingthetoxic pages 4-5) | **Supporting but qualifying**: data support a GLA-deficiency-driven axis, but lyso-Gb3 appears to be more than a byproduct and may mediate important non-storage toxicity | Cell-type-resolved perturbation comparing selective lowering of Gb3 versus lyso-Gb3, plus rescue experiments in podocytes, DRG neurons, endothelial cells, and cardiomyocytes |
| Which circulating biomarker best tracks pathogenic burden: plasma lyso-Gb3, tissue Gb3, urinary markers, or another marker | The hypothesis uses substrate accumulation as a causal biomarker, but therapy studies show plasma lyso-Gb3 may not mirror tissue injury or progression in all settings | BALANCE biomarker/renal outcome data; reviews noting organ damage despite normal/near-stable lyso-Gb3 and uncertainty of biomarker reliability on migalastat/ERT (germain2024pegunigalsidasealfaa pages 5-6, wallace2024headtoheadtrialof pages 2-3, wallace2024headtoheadtrialof pages 6-7, wallace2024headtoheadtrialof pages 1-1, wallace2024headtoheadtrialof pages 2-2, faro2024inflammationoxidativestress pages 12-13) | **Limiting**: plasma lyso-Gb3 is useful but insufficient as a universal surrogate for organ-level disease activity, especially in treated or advanced patients | Prospective cohort with synchronized plasma, urine, imaging, histology, and single-cell tissue lipidomics across untreated, newly treated, and advanced treated patients |
| Extent to which cardiac disease is caused by storage versus secondary remodeling | Fabry cardiomyopathy is a major phenotype the hypothesis seeks to explain; if cardiac dysfunction is poorly predicted by storage alone, a competing downstream model is needed | Mouse cardiac data showing mild/incomplete phenotypes with storage; reviews citing disproportionally small lipid burden relative to hypertrophy and persistent inflammation/vascular dysfunction (kugadas2024cardiacmanifestationsof pages 1-2, bertoldi2023biochemicalmechanismsbeyond pages 1-3, faro2024inflammationoxidativestress pages 10-12, faro2024inflammationoxidativestress pages 12-13, faro2024inflammationoxidativestress pages 13-15) | **Limiting**: storage likely initiates disease, but oxidative stress, endothelial dysfunction, inflammation, and fibrosis probably dominate progression and treatment resistance in heart tissue | Human cardiac tissue studies linking local Gb3/lyso-Gb3, inflammation, fibrosis, and contractile dysfunction before/after treatment; multimodal CMR + biopsy + spatial transcriptomics |
| Whether mutant α-Gal A misfolding/ER stress (“agalopathy”) is an independent pathogenic mechanism or mainly a modifier | If true, some pathology would arise from toxic mutant protein handling rather than only loss of enzymatic function/substrate storage, creating a parallel mechanism to the seed hypothesis | Renal/inflammatory review syntheses citing UPR, PERK-JAK1-STAT3, CREBH, and missense-variant ER stress evidence (feriozzi2024theinflammatorypathogenetic pages 1-3, feriozzi2024theinflammatorypathogenetic pages 9-11, kurdi2024inflammationinfabry pages 7-8) | **Unresolved but plausible limiter**: evidence in context is mostly review-mediated and supports agalopathy as a complementary mechanism, especially for some missense variants | Variant-stratified isogenic cell systems and patient cohorts comparing null vs missense GLA variants, with controlled equalization of substrate load and measurement of ER stress/UPR outputs |
| Why standard Gla knockout mouse models show substrate accumulation but relatively weak human-like organ pathology | Weak phenotype in canonical models limits direct experimental proof that storage alone is sufficient for full human disease expression | Mouse-model comparisons showing progressive storage with only modest pathology in GlaKO, while engineered high-Gb3 models improve some but not all translatability and may introduce artifacts (kugadas2024cardiacmanifestationsof pages 1-2) | **Limiting**: current models support the storage mechanism but incompletely reproduce human organ damage, making some causal links indirect | Better humanized or tissue-specific models with physiological lipid flux and X-linked mosaicism; cross-species comparison datasets aligning tissue lipid burden with functional outcomes |
| Cell-type specificity of injury from the same upstream defect | The hypothesis lists many affected tissues, but it remains unclear why podocytes, cardiomyocytes, DRG neurons, and endothelial/smooth-muscle cells differ in vulnerability and reversibility | Evidence for cell-specific uptake and lysosomal delivery in gene therapy models; lyso-Gb3-specific effects in neuronal cells; vascular and podocyte-specific signaling reports (jeyakumar2023preclinicalevaluationof pages 4-6, faro2024inflammationoxidativestress pages 10-12, nikolaenko2023elucidatingthetoxic pages 1-1, feriozzi2024theinflammatorypathogenetic pages 5-7, nikolaenko2023elucidatingthetoxic pages 2-3) | **Partially supported**: different cell types clearly respond differently, but the source of differential vulnerability is not fully resolved | Single-cell multi-omics and lipidomics in Fabry tissues, with perturb-seq or CRISPR-based tests of trafficking, autophagy, ER stress, and inflammatory pathways by cell type |
| Impact of sex, mosaicism, and residual enzyme activity on the canonical chain | Fabry disease is X-linked; females and non-classical patients may not fit a simple deficiency→storage→phenotype relationship, affecting scope of the hypothesis | BALANCE sex-specific observations and multiple reviews noting phenotype heterogeneity, male-biased ADA formation, and weaker biomarker-performance consistency across subtypes (germain2024pegunigalsidasealfaa pages 5-6, wallace2024headtoheadtrialof pages 2-3, wallace2024headtoheadtrialof pages 2-2) | **Scope-limiting**: canonical mechanism is strongest for classical males; it explains females/non-classical disease less parsimoniously without modifiers such as X-inactivation and residual activity | Large genotype-phenotype cohorts with enzyme activity, X-inactivation status, tissue biomarkers, and organ outcomes analyzed separately for classical males, non-classical males, and females |
| Clinical significance of anti-drug antibodies in separating primary from secondary treatment failure | If treatment fails because enzyme delivery is neutralized, persistence of disease may still support the canonical model; if failure persists despite adequate target engagement, secondary mechanisms are implicated | BALANCE ADA and infusion-reaction data; notes that proteinuria/ADA positivity tracked with less favorable lyso-Gb3 behavior (germain2024pegunigalsidasealfaa pages 5-6, wallace2024headtoheadtrialof pages 6-7, wallace2024headtoheadtrialof pages 6-6, wallace2024headtoheadtrialof pages 2-2) | **Partially supporting**: ADAs clearly modulate target engagement and biomarker response, but they do not fully explain residual organ progression | Standardized multicenter ADA assays linked to pharmacokinetics, tissue uptake, substrate lowering, and clinical outcomes across ERT platforms |
| Absence in checked context of direct human longitudinal tissue datasets proving full causal sequence from GLA deficiency to substrate accumulation to organ injury reversal | The strongest version of the hypothesis would be directly shown by serial human tissue-level correction and outcome reversal; lack of such datasets leaves some edges inferred | Context included clinical trial, preclinical gene therapy, mouse models, and reviews, but no directly inspected large human serial biopsy/spatial-omics dataset demonstrating complete reversal of causal intermediates was found here (jeyakumar2023preclinicalevaluationof pages 4-6, germain2024pegunigalsidasealfaa pages 5-6, wallace2024headtoheadtrialof pages 1-1, germain2024pegunigalsidasealfaa pages 1-2) | **Evidence gap**: substantial intervention evidence supports the hypothesis, but human tissue-level causal resolution remains incomplete in the checked context | International longitudinal biobank/registry with serial tissue, imaging, omics, and biomarker data before and after next-generation therapies |


*Table: This table summarizes the main unresolved causal steps and scope limits for the canonical GLA deficiency→Gb3/lyso-Gb3 storage model in Fabry disease. It is useful for curation because it distinguishes where the model is strongly supported from where additional experiments are needed to separate storage-driven from secondary mechanisms.*

## Alternative / Competing Mechanistic Models

| Model | Relationship to canonical | Key supporting evidence in context | What it explains better than storage-only | Key predictions / discriminating tests |
|---|---|---|---|---|
| Lyso-Gb3 bioactive signaling/toxicity model (proteostasis/ER stress; TGF-β/Notch) | Downstream effector / complementary mediator | Lyso-Gb3 directly perturbed proteostasis in SH-Sy5y cells at 20 and 200 ng/mL, increasing ubiquitination and binding chaperones including HSP90, HSP60, and TRiC; linked to translation/folding stress and ER/proteasome perturbation. Reviews also cite lyso-Gb3-driven TGF-β1, Notch1/SMAD signaling and podocyte/neuronal effects (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 5-6, kurdi2024inflammationinfabry pages 7-8) | Why plasma lyso-Gb3 tracks severity better than Gb3 in some settings; neuropathic pain, podocyte signaling injury, and fibrosis-promoting signaling despite limited bulk storage | Selective lyso-Gb3 lowering or receptor/pathway blockade should improve cellular stress/fibrotic readouts even when lysosomal Gb3 is incompletely normalized; compare effects of isolated Gb3 vs lyso-Gb3 perturbation in podocytes, neurons, cardiomyocytes |
| Innate immune activation model (Gb3 as TLR4 ligand → NF-κB; NKT cells) | Downstream / parallel amplifier | Gb3 was summarized as activating TLR4 with downstream Notch1/NF-κB signaling, while Gb3/lyso-Gb3 may alter immune-cell composition and activate invariant NKT-related pathways; inflammatory markers associate with LVH and renal disease (coelhoribeiro2024inflammationandexosomes pages 7-9, feriozzi2024theinflammatorypathogenetic pages 1-3, faro2024inflammationoxidativestress pages 12-13) | Persistent inflammatory phenotypes, cytokine elevation, and organ injury that seem disproportionate to measured substrate burden; possible autoinflammatory features | TLR4 or NKT-pathway inhibition should reduce cytokines/fibrotic signaling independent of full substrate clearance; longitudinal immune profiling before/after high-efficacy substrate correction should show whether inflammation normalizes or remains autonomous |
| Oxidative stress / NO dysregulation / endothelial dysfunction model | Downstream consequence that can become semi-autonomous | Reviews link Gb3/lyso-Gb3 accumulation to reduced NO bioavailability, eNOS dysregulation/uncoupling, ROS generation, ROCK activation, nitrotyrosine staining, smooth-muscle proliferation, increased IMT, and reduced flow-mediated dilation; vascular wall changes may be disproportionate to lipid storage (faro2024inflammationoxidativestress pages 10-12, faro2024inflammationoxidativestress pages 12-13, faro2024inflammationoxidativestress pages 13-15) | Vascular remodeling, vasospasm, microvascular dysfunction, and stroke/cardiac risk that exceed what passive lysosomal engorgement alone predicts | Endothelial/vascular biomarkers (NO metabolites, MPO, nitrotyrosine, FMD, CMR perfusion) should improve with antioxidant/RAS/ROCK-targeted interventions even when substrate biomarkers change little; tissue-specific lipidomics vs vascular function studies can test dissociation |
| ER stress / unfolded protein response “agalopathy” from misfolded α-Gal A variants | Parallel mechanism, especially for missense variants | Reviewed evidence proposes that some GLA missense variants produce misfolded α-Gal A causing ER stress/UPR and inflammatory signaling via PERK–JAK1–STAT3 and related pathways, potentially independent of substrate accumulation; presymptomatic/VUS-associated inflammatory findings are also cited (feriozzi2024theinflammatorypathogenetic pages 1-3, gragnaniello2026biochemicalandcellular pages 28-30, feriozzi2024theinflammatorypathogenetic pages 9-11) | Variant-specific disease heterogeneity, pathology in settings with lower storage burden, and differences between null vs missense genotypes not captured by substrate levels alone | Isogenic null-vs-missense GLA systems matched for substrate burden should show higher UPR/inflammatory signaling in missense states; chaperone correction should reduce ER-stress markers even before large substrate changes |
| Self-sustaining fibrosis / autophagy-lysosomal dysfunction model (point-of-no-return; SNCA-mediated) | Downstream chronic-state model | Renal reviews cite podocyte/tubular studies where Gb3 clearance after ERT failed to restore altered cytokine signaling or lysosomal defects; SNCA was implicated in persistent lysosomal dysfunction, and inhibition improved lysosomal structure. Tubular injury, ROS, autophagy defects, and epithelial-myofibroblast transition are also described (feriozzi2024theinflammatorypathogenetic pages 5-7, feriozzi2024theinflammatorypathogenetic pages 9-11, gragnaniello2026biochemicalandcellular pages 30-34) | Why late-treated renal/cardiac disease may progress despite substrate reduction; fibrosis, persistent lysosomal dysfunction, and incomplete reversibility of organ damage | Early vs late intervention studies should show a threshold after which substrate correction no longer normalizes autophagy/fibrosis programs; combine substrate-lowering with SNCA/autophagy/fibrosis-targeted therapies and assess whether organ outcomes improve beyond monotherapy |
| Model-organism limitations / need for modifiers | Qualifies evidentiary strength of canonical and alternative models | GlaKO mice accumulate Gb3/lyso-Gb3 but often show only mild pathology; G3Stg/GlaKO increases substrate and pathology but introduces potentially non-physiologic features. This suggests additional modifiers or species/cell-context factors are needed for full human disease expression (kugadas2024cardiacmanifestationsof pages 1-2) | Why human Fabry phenotypes are more severe, heterogeneous, and organ-specific than standard animal models predict; why storage alone in mice may be insufficient to reproduce human cardiomyopathy/nephropathy | Develop models incorporating human Gb3 synthase levels, X-linked mosaicism, missense-specific ER stress, immune pathways, and cell-type vulnerability; benchmark models by matching tissue lipid burden, fibrosis, and organ-function signatures to human multi-omics datasets |


*Table: This table compares complementary and competing mechanistic models for Fabry disease against the canonical α-Gal A deficiency/Gb3 storage model. It is useful for showing which downstream or parallel pathways are supported by current evidence and what experiments would best distinguish them.*

## Discriminating Tests (studies that best separate canonical vs alternatives)

1) **Variant-stratified “null vs missense” cohorts with matched substrate burden**

*Design:* enroll classic null variants and missense “amenable” variants, match baseline tissue lipid load (kidney biopsy lipid morphometry or tissue lipidomics), then compare ER-stress/UPR markers and inflammatory signaling trajectories under potent substrate correction.

*Rationale:* tests “storage-only” vs “agalopathy” (ER stress) as parallel drivers. (feriozzi2024theinflammatorypathogenetic pages 9-11, bichet2023consensusrecommendationsfor pages 11-13)

2) **Longitudinal multi-omics + lipidomics + imaging before/after high-efficacy substrate correction**

*Design:* prospective study with plasma and tissue Gb3/lyso-Gb3, spatial transcriptomics/single-cell data, fibrosis markers, and CMR/perfusion endpoints.

*Rationale:* determines whether inflammation/oxidative stress normalize when substrate is durably corrected or remain autonomous (supporting self-sustaining models). (faro2024inflammationoxidativestress pages 12-13, faro2024inflammationoxidativestress pages 13-15)

3) **Selective pathway blocking in addition to substrate lowering**

*Design:* in Fabry-relevant human cell systems (podocytes, endothelial cells, DRG neurons), compare (a) α-Gal A restoration/substrate lowering alone vs (b) substrate lowering + blockade of TLR4/Notch/TGF-β signaling or antioxidant/NO pathway modulation.

*Rationale:* tests whether bioactive signaling (TLR4/Notch; TGF-β) is required for injury independently of storage. (coelhoribeiro2024inflammationandexosomes pages 7-9, faro2024inflammationoxidativestress pages 10-12)

4) **Biomarker validity study: plasma lyso-Gb3 vs tissue burden vs clinical trajectory**

*Design:* treated and untreated strata; assess discordance between plasma lyso-Gb3 and kidney/cardiac outcomes; include antibody and proteinuria effects.

*Rationale:* addresses limitations highlighted by BALANCE and inflammatory/vascular literature about “normal/near-stable lyso-Gb3” not equaling absence of active disease. (germain2024pegunigalsidasealfaa pages 5-6, faro2024inflammationoxidativestress pages 12-13)

## Curation Leads (candidate KB updates; curator verification required)

### A. Candidate evidence references + snippets to verify

1) **Lyso-Gb3 proteostasis mechanism**

*Reference:* Nikolaenko et al., *Human Molecular Genetics*, 2023-05, DOI: 10.1093/hmg/ddad073 (URL: https://doi.org/10.1093/hmg/ddad073). (nikolaenko2023elucidatingthetoxic pages 1-1)

*Snippet to verify:* SH-Sy5y exposure to lyso-Gb3 (20/200 ng/mL) → increased ubiquitination; lyso-Gb3 binds chaperones (HSP90/HSP60/TRiC). (nikolaenko2023elucidatingthetoxic pages 1-1)

2) **ERT non-inferiority renal outcome + biomarker/immunogenicity modifier**

*Reference:* Wallace et al., *Journal of Medical Genetics*, 2024-11, DOI: 10.1136/jmg-2023-109445 (URL: https://doi.org/10.1136/jmg-2023-109445). (wallace2024headtoheadtrialof pages 1-1)

*Snippet to verify:* eGFR slope difference −0.36 mL/min/1.73 m²/year; both arms show minimal lyso-Gb3 change after 2 years; antibody patterns and tolerability differ. (wallace2024headtoheadtrialof pages 1-1, wallace2024headtoheadtrialof pages 6-7)

3) **Vascular oxidative stress / endothelial dysfunction beyond storage**

*Reference:* Faro et al., *International Journal of Molecular Sciences*, 2024-07, DOI: 10.3390/ijms25158273 (URL: https://doi.org/10.3390/ijms25158273). (faro2024inflammationoxidativestress pages 10-12)

*Snippet to verify:* Gb3/lyso-Gb3 accumulation → reduced NO and increased ROS; inflammatory/oxidative markers persist despite ERT; vascular changes disproportionate to deposits. (faro2024inflammationoxidativestress pages 10-12, faro2024inflammationoxidativestress pages 13-15)

4) **Renal “point-of-no-return” / self-sustaining dysfunction and ‘agalopathy’ concept**

*Reference:* Feriozzi & Rozenfeld, *Rare Disease and Orphan Drugs Journal*, 2024-04, DOI: 10.20517/rdodj.2023.37 (URL: https://doi.org/10.20517/rdodj.2023.37). (feriozzi2024theinflammatorypathogenetic pages 5-7)

*Snippet to verify:* clearance of Gb3 yet persistent signaling/lysosomal defects; downstream mechanisms may become independent; zebrafish lesions in absence of Gb3; ER-stress UPR from missense variants. (feriozzi2024theinflammatorypathogenetic pages 1-3, feriozzi2024theinflammatorypathogenetic pages 5-7)

### B. Candidate nodes/edges (mechanistic graph leads)

* **Gb3 → TLR4 activation → Notch1/NF-κB signaling → cytokines (TNFα, IL-1β)** (innate immune activation edge; complementary to storage). (coelhoribeiro2024inflammationandexosomes pages 7-9, feriozzi2024theinflammatorypathogenetic pages 1-3)
* **Lyso-Gb3 → chaperone binding (HSP90/TRiC) → increased ubiquitination / proteostasis stress** (proteotoxicity edge). (nikolaenko2023elucidatingthetoxic pages 1-1, nikolaenko2023elucidatingthetoxic pages 5-6)
* **Substrate accumulation → eNOS dysregulation/NO decrease + ROS increase → endothelial dysfunction → vasculopathy**. (faro2024inflammationoxidativestress pages 10-12)
* **Misfolded α-Gal A (missense) → ER stress/UPR (PERK–JAK1–STAT3) → inflammation** (“agalopathy” parallel mechanism). (feriozzi2024theinflammatorypathogenetic pages 9-11)

### C. Candidate ontology terms (examples; curator to map)

* Cell types: podocyte; glomerular endothelial cell; vascular endothelial cell; vascular smooth muscle cell; cardiomyocyte; dorsal root ganglion neuron; macrophage/monocyte.
* Processes: lysosomal storage; autophagy dysfunction; unfolded protein response; oxidative stress; endothelial dysfunction; innate immune activation; fibrosis/TGF-β signaling.

### D. Candidate subtype restrictions

* The canonical storage axis is **strongest for classic males** and for **early-stage** disease where substrate removal more plausibly prevents downstream fibrosis/autoinflammation. Evidence and expert guidance highlight heterogeneity by sex, stage, and immunogenicity, which should be recorded as scope constraints rather than refutation. (germain2024pegunigalsidasealfaa pages 5-6, bichet2023consensusrecommendationsfor pages 11-13)

### E. Candidate knowledge_gaps entries

* “Plasma lyso-Gb3 is an imperfect surrogate for tissue-level injury and progression, especially in advanced treated disease.” (germain2024pegunigalsidasealfaa pages 5-6, faro2024inflammationoxidativestress pages 12-13)
* “Determine whether ER-stress/UPR (‘agalopathy’) is causal vs modifier and which variants are most affected.” (feriozzi2024theinflammatorypathogenetic pages 9-11, bichet2023consensusrecommendationsfor pages 11-13)

---

## URLs and publication dates (for quick curation)

* Nikolaenko et al., 2023-05, *Hum Mol Genet*, https://doi.org/10.1093/hmg/ddad073 (nikolaenko2023elucidatingthetoxic pages 1-1)
* Jeyakumar et al., 2023-01, *Gene Therapy*, https://doi.org/10.1038/s41434-022-00381-y (jeyakumar2023preclinicalevaluationof pages 1-2)
* Kurdi et al., 2024-06, *Front Cardiovasc Med*, https://doi.org/10.3389/fcvm.2024.1420067 (kurdi2024inflammationinfabry pages 7-8)
* Coelho-Ribeiro et al., 2024-04, *Cells*, https://doi.org/10.3390/cells13080654 (coelhoribeiro2024inflammationandexosomes pages 7-9)
* Faro et al., 2024-07, *Int J Mol Sci*, https://doi.org/10.3390/ijms25158273 (faro2024inflammationoxidativestress pages 10-12)
* Wallace et al., 2024-11, *J Med Genet*, https://doi.org/10.1136/jmg-2023-109445 (wallace2024headtoheadtrialof pages 1-1)
* Germain & Linhart, 2024-04, *Front Genet*, https://doi.org/10.3389/fgene.2024.1395287 (germain2024pegunigalsidasealfaa pages 1-2)
* Perretta & Jaurretche, 2023-02, *Healthcare*, https://doi.org/10.3390/healthcare11040449 (perretta2023fabrydiseaseswitch pages 2-3)
* Bichet et al., 2023-09, *Frontiers in Medicine* (Delphi), https://doi.org/10.3389/fmed.2023.1220637 (bichet2023consensusrecommendationsfor pages 11-13)
* STAAR trial (ST-920), ClinicalTrials.gov, NCT04046224: https://clinicaltrials.gov/study/NCT04046224 (NCT04046224 chunk 1)
* FLT190 trial, ClinicalTrials.gov, NCT04040049: https://clinicaltrials.gov/study/NCT04040049 (NCT04040049 chunk 1)


References

1. (jeyakumar2023preclinicalevaluationof pages 11-14): Jey M. Jeyakumar, Azadeh Kia, Lawrence C. S. Tam, Jenny McIntosh, Justyna Spiewak, Kevin Mills, Wendy Heywood, Elisa Chisari, Noemi Castaldo, Daniël Verhoef, Paniz Hosseini, Petya Kalcheva, Clement Cocita, Carlos J. Miranda, Miriam Canavese, Jaminder Khinder, Cecilia Rosales, Derralynn Hughes, Rose Sheridan, Romuald Corbau, and Amit Nathwani. Preclinical evaluation of flt190, a liver-directed aav gene therapy for fabry disease. Gene Therapy, 30:487-502, Jan 2023. URL: https://doi.org/10.1038/s41434-022-00381-y, doi:10.1038/s41434-022-00381-y. This article has 45 citations and is from a peer-reviewed journal.

2. (jeyakumar2023preclinicalevaluationof pages 10-11): Jey M. Jeyakumar, Azadeh Kia, Lawrence C. S. Tam, Jenny McIntosh, Justyna Spiewak, Kevin Mills, Wendy Heywood, Elisa Chisari, Noemi Castaldo, Daniël Verhoef, Paniz Hosseini, Petya Kalcheva, Clement Cocita, Carlos J. Miranda, Miriam Canavese, Jaminder Khinder, Cecilia Rosales, Derralynn Hughes, Rose Sheridan, Romuald Corbau, and Amit Nathwani. Preclinical evaluation of flt190, a liver-directed aav gene therapy for fabry disease. Gene Therapy, 30:487-502, Jan 2023. URL: https://doi.org/10.1038/s41434-022-00381-y, doi:10.1038/s41434-022-00381-y. This article has 45 citations and is from a peer-reviewed journal.

3. (zhang2024fabrynephropathyfocus pages 3-5): Dan Zhang, Kenan Xie, and Jiong Zhang. Fabry nephropathy: focus on podocyte damage and therapeutic target. Journal of Translational Genetics and Genomics, 8:302-11, Sep 2024. URL: https://doi.org/10.20517/jtgg.2024.39, doi:10.20517/jtgg.2024.39. This article has 3 citations.

4. (germain2024pegunigalsidasealfaa pages 1-2): Dominique P. Germain and Ales Linhart. Pegunigalsidase alfa: a novel, pegylated recombinant alpha-galactosidase enzyme for the treatment of fabry disease. Frontiers in Genetics, Apr 2024. URL: https://doi.org/10.3389/fgene.2024.1395287, doi:10.3389/fgene.2024.1395287. This article has 38 citations and is from a peer-reviewed journal.

5. (feriozzi2024theinflammatorypathogenetic pages 5-7): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

6. (faro2024inflammationoxidativestress pages 12-13): Denise Cristiana Faro, Francesco Lorenzo Di Pino, and Ines Paola Monte. Inflammation, oxidative stress, and endothelial dysfunction in the pathogenesis of vascular damage: unraveling novel cardiovascular risk factors in fabry disease. International Journal of Molecular Sciences, 25:8273, Jul 2024. URL: https://doi.org/10.3390/ijms25158273, doi:10.3390/ijms25158273. This article has 41 citations.

7. (faro2024inflammationoxidativestress pages 13-15): Denise Cristiana Faro, Francesco Lorenzo Di Pino, and Ines Paola Monte. Inflammation, oxidative stress, and endothelial dysfunction in the pathogenesis of vascular damage: unraveling novel cardiovascular risk factors in fabry disease. International Journal of Molecular Sciences, 25:8273, Jul 2024. URL: https://doi.org/10.3390/ijms25158273, doi:10.3390/ijms25158273. This article has 41 citations.

8. (feriozzi2024theinflammatorypathogenetic pages 1-3): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

9. (bertoldi2023biochemicalmechanismsbeyond pages 1-3): Giovanni Bertoldi, Ilaria Caputo, Giulia Driussi, Lucia Federica Stefanelli, Valentina Di Vico, Gianni Carraro, Federico Nalesso, and Lorenzo A. Calò. Biochemical mechanisms beyond glycosphingolipid accumulation in fabry disease: might they provide additional therapeutic treatments? Journal of Clinical Medicine, 12:2063, Mar 2023. URL: https://doi.org/10.3390/jcm12052063, doi:10.3390/jcm12052063. This article has 24 citations.

10. (kugadas2024cardiacmanifestationsof pages 1-2): Abirami Kugadas, Pietro Artoni, Wanida Ruangsiriluk, Meng Zhao, Natalia Boukharov, Rizwana Islam, Dmitri Volfson, and Katayoun Derakhchan. Cardiac manifestations of fabry disease in g3stg/glako and glako mouse models–translation to fabry disease patients. PLOS ONE, 19:e0304415, May 2024. URL: https://doi.org/10.1371/journal.pone.0304415, doi:10.1371/journal.pone.0304415. This article has 8 citations and is from a peer-reviewed journal.

11. (nikolaenko2023elucidatingthetoxic pages 1-1): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

12. (germain2024pegunigalsidasealfaa pages 5-6): Dominique P. Germain and Ales Linhart. Pegunigalsidase alfa: a novel, pegylated recombinant alpha-galactosidase enzyme for the treatment of fabry disease. Frontiers in Genetics, Apr 2024. URL: https://doi.org/10.3389/fgene.2024.1395287, doi:10.3389/fgene.2024.1395287. This article has 38 citations and is from a peer-reviewed journal.

13. (wallace2024headtoheadtrialof pages 2-3): Eric L Wallace, Ozlem Goker-Alpan, William R Wilcox, Myrl Holida, John Bernat, Nicola Longo, Aleš Linhart, Derralynn A Hughes, Robert J Hopkin, Camilla Tøndel, Mirjam Langeveld, Pilar Giraldo, Antonio Pisani, Dominique Paul Germain, Ankit Mehta, Patrick B Deegan, Maria Judit Molnar, Damara Ortiz, Ana Jovanovic, Michael Muriello, Bruce A Barshop, Virginia Kimonis, Bojan Vujkovac, Albina Nowak, Tarekegn Geberhiwot, Ilkka Kantola, Jasmine Knoll, Stephen Waldek, Khan Nedd, Amel Karaa, Einat Brill-Almon, Sari Alon, Raul Chertkoff, Rossana Rocco, Anat Sakov, and David G Warnock. Head-to-head trial of pegunigalsidase alfa versus agalsidase beta in patients with fabry disease and deteriorating renal function: results from the 2-year randomised phase iii balance study. Journal of Medical Genetics, 61:520-530, Nov 2024. URL: https://doi.org/10.1136/jmg-2023-109445, doi:10.1136/jmg-2023-109445. This article has 53 citations and is from a domain leading peer-reviewed journal.

14. (faro2024inflammationoxidativestress pages 10-12): Denise Cristiana Faro, Francesco Lorenzo Di Pino, and Ines Paola Monte. Inflammation, oxidative stress, and endothelial dysfunction in the pathogenesis of vascular damage: unraveling novel cardiovascular risk factors in fabry disease. International Journal of Molecular Sciences, 25:8273, Jul 2024. URL: https://doi.org/10.3390/ijms25158273, doi:10.3390/ijms25158273. This article has 41 citations.

15. (nikolaenko2023elucidatingthetoxic pages 2-3): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

16. (jeyakumar2023preclinicalevaluationof pages 4-6): Jey M. Jeyakumar, Azadeh Kia, Lawrence C. S. Tam, Jenny McIntosh, Justyna Spiewak, Kevin Mills, Wendy Heywood, Elisa Chisari, Noemi Castaldo, Daniël Verhoef, Paniz Hosseini, Petya Kalcheva, Clement Cocita, Carlos J. Miranda, Miriam Canavese, Jaminder Khinder, Cecilia Rosales, Derralynn Hughes, Rose Sheridan, Romuald Corbau, and Amit Nathwani. Preclinical evaluation of flt190, a liver-directed aav gene therapy for fabry disease. Gene Therapy, 30:487-502, Jan 2023. URL: https://doi.org/10.1038/s41434-022-00381-y, doi:10.1038/s41434-022-00381-y. This article has 45 citations and is from a peer-reviewed journal.

17. (jeyakumar2023preclinicalevaluationof pages 1-2): Jey M. Jeyakumar, Azadeh Kia, Lawrence C. S. Tam, Jenny McIntosh, Justyna Spiewak, Kevin Mills, Wendy Heywood, Elisa Chisari, Noemi Castaldo, Daniël Verhoef, Paniz Hosseini, Petya Kalcheva, Clement Cocita, Carlos J. Miranda, Miriam Canavese, Jaminder Khinder, Cecilia Rosales, Derralynn Hughes, Rose Sheridan, Romuald Corbau, and Amit Nathwani. Preclinical evaluation of flt190, a liver-directed aav gene therapy for fabry disease. Gene Therapy, 30:487-502, Jan 2023. URL: https://doi.org/10.1038/s41434-022-00381-y, doi:10.1038/s41434-022-00381-y. This article has 45 citations and is from a peer-reviewed journal.

18. (wallace2024headtoheadtrialof pages 1-1): Eric L Wallace, Ozlem Goker-Alpan, William R Wilcox, Myrl Holida, John Bernat, Nicola Longo, Aleš Linhart, Derralynn A Hughes, Robert J Hopkin, Camilla Tøndel, Mirjam Langeveld, Pilar Giraldo, Antonio Pisani, Dominique Paul Germain, Ankit Mehta, Patrick B Deegan, Maria Judit Molnar, Damara Ortiz, Ana Jovanovic, Michael Muriello, Bruce A Barshop, Virginia Kimonis, Bojan Vujkovac, Albina Nowak, Tarekegn Geberhiwot, Ilkka Kantola, Jasmine Knoll, Stephen Waldek, Khan Nedd, Amel Karaa, Einat Brill-Almon, Sari Alon, Raul Chertkoff, Rossana Rocco, Anat Sakov, and David G Warnock. Head-to-head trial of pegunigalsidase alfa versus agalsidase beta in patients with fabry disease and deteriorating renal function: results from the 2-year randomised phase iii balance study. Journal of Medical Genetics, 61:520-530, Nov 2024. URL: https://doi.org/10.1136/jmg-2023-109445, doi:10.1136/jmg-2023-109445. This article has 53 citations and is from a domain leading peer-reviewed journal.

19. (west2024fabrynephropathya pages 18-20): Michael L. West, Laurette Geldenhuys, and Daniel G. Bichet. Fabry nephropathy: a treatable cause of chronic kidney disease. Rare Disease and Orphan Drugs Journal, Jul 2024. URL: https://doi.org/10.20517/rdodj.2023.61, doi:10.20517/rdodj.2023.61. This article has 4 citations.

20. (feriozzi2024theinflammatorypathogenetic pages 9-11): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

21. (nikolaenko2023elucidatingthetoxic pages 5-6): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

22. (coelhoribeiro2024inflammationandexosomes pages 7-9): Bruna Coelho-Ribeiro, Helena G. Silva, Belém Sampaio-Marques, Alexandra G. Fraga, Olga Azevedo, Jorge Pedrosa, and Paula Ludovico. Inflammation and exosomes in fabry disease pathogenesis. Cells, 13:654, Apr 2024. URL: https://doi.org/10.3390/cells13080654, doi:10.3390/cells13080654. This article has 18 citations.

23. (kurdi2024inflammationinfabry pages 7-8): Hibba Kurdi, Lucia Lavalle, James C. C. Moon, and Derralynn Hughes. Inflammation in fabry disease: stages, molecular pathways, and therapeutic implications. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1420067, doi:10.3389/fcvm.2024.1420067. This article has 27 citations and is from a peer-reviewed journal.

24. (wallace2024headtoheadtrialof pages 6-7): Eric L Wallace, Ozlem Goker-Alpan, William R Wilcox, Myrl Holida, John Bernat, Nicola Longo, Aleš Linhart, Derralynn A Hughes, Robert J Hopkin, Camilla Tøndel, Mirjam Langeveld, Pilar Giraldo, Antonio Pisani, Dominique Paul Germain, Ankit Mehta, Patrick B Deegan, Maria Judit Molnar, Damara Ortiz, Ana Jovanovic, Michael Muriello, Bruce A Barshop, Virginia Kimonis, Bojan Vujkovac, Albina Nowak, Tarekegn Geberhiwot, Ilkka Kantola, Jasmine Knoll, Stephen Waldek, Khan Nedd, Amel Karaa, Einat Brill-Almon, Sari Alon, Raul Chertkoff, Rossana Rocco, Anat Sakov, and David G Warnock. Head-to-head trial of pegunigalsidase alfa versus agalsidase beta in patients with fabry disease and deteriorating renal function: results from the 2-year randomised phase iii balance study. Journal of Medical Genetics, 61:520-530, Nov 2024. URL: https://doi.org/10.1136/jmg-2023-109445, doi:10.1136/jmg-2023-109445. This article has 53 citations and is from a domain leading peer-reviewed journal.

25. (perretta2023fabrydiseaseswitch pages 1-2): Fernando Perretta and Sebastián Jaurretche. Fabry disease: switch from enzyme replacement therapy to oral chaperone migalastat: what do we know today? Healthcare, 11:449, Feb 2023. URL: https://doi.org/10.3390/healthcare11040449, doi:10.3390/healthcare11040449. This article has 25 citations.

26. (perretta2023fabrydiseaseswitch pages 2-3): Fernando Perretta and Sebastián Jaurretche. Fabry disease: switch from enzyme replacement therapy to oral chaperone migalastat: what do we know today? Healthcare, 11:449, Feb 2023. URL: https://doi.org/10.3390/healthcare11040449, doi:10.3390/healthcare11040449. This article has 25 citations.

27. (bichet2023consensusrecommendationsfor pages 11-13): Daniel G. Bichet, Robert J. Hopkin, Patrício Aguiar, Sridhar R. Allam, Yin-Hsiu Chien, Roberto Giugliani, Staci Kallish, Sabina Kineen, Olivier Lidove, Dau-Ming Niu, Iacopo Olivotto, Juan Politei, Paul Rakoski, Roser Torra, Camilla Tøndel, and Derralynn A. Hughes. Consensus recommendations for the treatment and management of patients with fabry disease on migalastat: a modified delphi study. Frontiers in Medicine, Sep 2023. URL: https://doi.org/10.3389/fmed.2023.1220637, doi:10.3389/fmed.2023.1220637. This article has 19 citations.

28. (bichet2023consensusrecommendationsfor pages 1-2): Daniel G. Bichet, Robert J. Hopkin, Patrício Aguiar, Sridhar R. Allam, Yin-Hsiu Chien, Roberto Giugliani, Staci Kallish, Sabina Kineen, Olivier Lidove, Dau-Ming Niu, Iacopo Olivotto, Juan Politei, Paul Rakoski, Roser Torra, Camilla Tøndel, and Derralynn A. Hughes. Consensus recommendations for the treatment and management of patients with fabry disease on migalastat: a modified delphi study. Frontiers in Medicine, Sep 2023. URL: https://doi.org/10.3389/fmed.2023.1220637, doi:10.3389/fmed.2023.1220637. This article has 19 citations.

29. (NCT04046224 chunk 1):  Dose-Ranging Study of ST-920, an AAV2/6 Human Alpha Galactosidase A Gene Therapy in Subjects With Fabry Disease (STAAR). Sangamo Therapeutics. 2019. ClinicalTrials.gov Identifier: NCT04046224

30. (NCT04040049 chunk 1):  A Fabry Disease Gene Therapy Study. Spur Therapeutics. 2019. ClinicalTrials.gov Identifier: NCT04040049

31. (nikolaenko2023elucidatingthetoxic pages 1-2): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

32. (nikolaenko2023elucidatingthetoxic pages 3-4): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

33. (nikolaenko2023elucidatingthetoxic pages 4-5): Valeria Nikolaenko, David G Warnock, Kevin Mills, and Wendy E Heywood. Elucidating the toxic effect and disease mechanisms associated with lyso-gb3 in fabry disease. Human Molecular Genetics, 32:2464-2472, May 2023. URL: https://doi.org/10.1093/hmg/ddad073, doi:10.1093/hmg/ddad073. This article has 17 citations and is from a domain leading peer-reviewed journal.

34. (wallace2024headtoheadtrialof pages 2-2): Eric L Wallace, Ozlem Goker-Alpan, William R Wilcox, Myrl Holida, John Bernat, Nicola Longo, Aleš Linhart, Derralynn A Hughes, Robert J Hopkin, Camilla Tøndel, Mirjam Langeveld, Pilar Giraldo, Antonio Pisani, Dominique Paul Germain, Ankit Mehta, Patrick B Deegan, Maria Judit Molnar, Damara Ortiz, Ana Jovanovic, Michael Muriello, Bruce A Barshop, Virginia Kimonis, Bojan Vujkovac, Albina Nowak, Tarekegn Geberhiwot, Ilkka Kantola, Jasmine Knoll, Stephen Waldek, Khan Nedd, Amel Karaa, Einat Brill-Almon, Sari Alon, Raul Chertkoff, Rossana Rocco, Anat Sakov, and David G Warnock. Head-to-head trial of pegunigalsidase alfa versus agalsidase beta in patients with fabry disease and deteriorating renal function: results from the 2-year randomised phase iii balance study. Journal of Medical Genetics, 61:520-530, Nov 2024. URL: https://doi.org/10.1136/jmg-2023-109445, doi:10.1136/jmg-2023-109445. This article has 53 citations and is from a domain leading peer-reviewed journal.

35. (wallace2024headtoheadtrialof pages 6-6): Eric L Wallace, Ozlem Goker-Alpan, William R Wilcox, Myrl Holida, John Bernat, Nicola Longo, Aleš Linhart, Derralynn A Hughes, Robert J Hopkin, Camilla Tøndel, Mirjam Langeveld, Pilar Giraldo, Antonio Pisani, Dominique Paul Germain, Ankit Mehta, Patrick B Deegan, Maria Judit Molnar, Damara Ortiz, Ana Jovanovic, Michael Muriello, Bruce A Barshop, Virginia Kimonis, Bojan Vujkovac, Albina Nowak, Tarekegn Geberhiwot, Ilkka Kantola, Jasmine Knoll, Stephen Waldek, Khan Nedd, Amel Karaa, Einat Brill-Almon, Sari Alon, Raul Chertkoff, Rossana Rocco, Anat Sakov, and David G Warnock. Head-to-head trial of pegunigalsidase alfa versus agalsidase beta in patients with fabry disease and deteriorating renal function: results from the 2-year randomised phase iii balance study. Journal of Medical Genetics, 61:520-530, Nov 2024. URL: https://doi.org/10.1136/jmg-2023-109445, doi:10.1136/jmg-2023-109445. This article has 53 citations and is from a domain leading peer-reviewed journal.

36. (gragnaniello2026biochemicalandcellular pages 28-30): V Gragnaniello. Biochemical and cellular abnormalities in presymptomatic pediatric patients with fabry disease and gaucher disease identified through newborn screening. Unknown journal, 2026.

37. (gragnaniello2026biochemicalandcellular pages 30-34): V Gragnaniello. Biochemical and cellular abnormalities in presymptomatic pediatric patients with fabry disease and gaucher disease identified through newborn screening. Unknown journal, 2026.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](falcon_artifacts/artifact-02.md)
