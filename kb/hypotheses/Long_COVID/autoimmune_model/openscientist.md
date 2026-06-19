---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T05:57:45.558532'
end_time: '2026-05-23T06:18:35.752371'
duration_seconds: 1250.19
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Long COVID
  category: Complex
  hypothesis_group_id: autoimmune_model
  hypothesis_label: Autoimmunity and B-cell Dysregulation Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: autoimmune_model\nhypothesis_label: Autoimmunity\
    \ and B-cell Dysregulation Model\nstatus: EMERGING\ndescription: |\n  SARS-CoV-2\
    \ triggers de novo autoantibody production through B-cell dysregulation, molecular\
    \ mimicry, and bystander activation, contributing to multisystem symptoms and\
    \ immune-mediated tissue damage in Long COVID.\napplies_to_subtypes:\n- Pain-dominant\
    \ long COVID phenotype\n- Cardiopulmonary-dominant long COVID phenotype\nevidence:\n\
    - reference: PMID:39956285\n  reference_title: Autoimmunity in long COVID.\n \
    \ supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Several studies\
    \ show preexisting and/or de novo production of autoantibodies after infection\n\
    \    with SARS-CoV-2, but the persistence of these antibodies and their role in\
    \ causing long COVID is debated.\n  explanation: Supports autoimmunity as an emerging\
    \ mechanistic hypothesis for Long COVID."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 33
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Long COVID
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** autoimmune_model
- **Hypothesis Label:** Autoimmunity and B-cell Dysregulation Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: autoimmune_model
hypothesis_label: Autoimmunity and B-cell Dysregulation Model
status: EMERGING
description: |
  SARS-CoV-2 triggers de novo autoantibody production through B-cell dysregulation, molecular mimicry, and bystander activation, contributing to multisystem symptoms and immune-mediated tissue damage in Long COVID.
applies_to_subtypes:
- Pain-dominant long COVID phenotype
- Cardiopulmonary-dominant long COVID phenotype
evidence:
- reference: PMID:39956285
  reference_title: Autoimmunity in long COVID.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Several studies show preexisting and/or de novo production of autoantibodies after infection
    with SARS-CoV-2, but the persistence of these antibodies and their role in causing long COVID is debated.
  explanation: Supports autoimmunity as an emerging mechanistic hypothesis for Long COVID.
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

# Hypothesis Evaluation Report: Autoimmunity and B-cell Dysregulation Model for Long COVID

**Hypothesis ID:** `autoimmune_model`  
**Hypothesis Label:** Autoimmunity and B-cell Dysregulation Model  
**Status in KB:** EMERGING  
**Date of Evaluation:** 2026-05-23  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED**

The autoimmunity and B-cell dysregulation model for Long COVID is **partially supported** by the current literature. Strong, convergent evidence establishes that SARS-CoV-2 infection triggers de novo autoantibody production through well-characterized immunological pathways — extrafollicular B-cell activation, molecular mimicry between viral and human proteins, and bystander activation of autoreactive clones. A landmark 2026 passive transfer study ([PMID: 42053865](https://pubmed.ncbi.nlm.nih.gov/42053865/)) provides the first direct experimental evidence that IgG from Long COVID patients is pathogenic, inducing pain and sensory symptoms in mice. Meta-analytic data from 68 studies confirm elevated GPCR and renin-angiotensin system autoantibodies across the COVID-19 severity spectrum ([PMID: 37490975](https://pubmed.ncbi.nlm.nih.gov/37490975/)), and longitudinal evidence demonstrates that early anti-apolipoprotein A-1 levels independently predict respiratory symptom persistence at 12 months ([PMID: 35598178](https://pubmed.ncbi.nlm.nih.gov/35598178/)).

However, **three critical caveats** prevent elevation from EMERGING to ESTABLISHED status:

1. **Persistence is debated.** The most rigorous longitudinal B-cell study found that all subpopulation changes normalized within 200 days of symptom onset ([PMID: 40915391](https://pubmed.ncbi.nlm.nih.gov/40915391/)). Anti-apolipoprotein A-1 seropositivity declined from 93% at 1 month to 15% at 12 months. Many autoantibodies appear transient, challenging the model's ability to explain symptoms persisting for years.
2. **Causal evidence is narrow.** The passive transfer experiment reproduced pain and sensory hypersensitivity but explicitly failed to induce cognitive, mood, or memory deficits — excluding the most prevalent and debilitating Long COVID symptoms from the autoantibody hypothesis.
3. **No therapeutic proof-of-concept.** No completed randomized controlled trial has demonstrated that removing autoantibodies (via immunoadsorption, B-cell depletion, or IVIG) improves Long COVID outcomes.

**Most important caveat:** The autoimmune model most plausibly applies to a subset of Long COVID manifestations — particularly pain-dominant and cardiopulmonary phenotypes — and likely operates as one component of multifactorial pathogenesis alongside viral persistence, microvascular dysfunction, and latent virus reactivation, rather than as a standalone universal mechanism.

---

## Summary

SARS-CoV-2 infection disrupts normal B-cell maturation through extrafollicular pathways, producing de novo autoantibodies targeting diverse self-antigens including G protein-coupled receptors (GPCRs), phospholipids, neuronal proteins, and apolipoproteins. Computational and experimental studies confirm molecular mimicry between viral proteins (spike, nucleocapsid) and human proteins as a mechanistic basis for cross-reactive autoantibody generation. The strongest direct evidence comes from a 2026 passive IgG transfer study demonstrating that antibodies from neurological Long COVID patients induce transient mechanical allodynia and thermal hypersensitivity in mice — the first proof that Long COVID autoantibodies are pathogenic in vivo.

Despite these advances, the hypothesis faces significant challenges. A large-scale flow cytometry study found that all B-cell subpopulation changes normalize within 200 days of symptom onset, and most autoantibodies decline to baseline within months. A comprehensive population-based study of persistent post-COVID syndrome found no elevation in complement activity, inflammatory markers, or EBV reactivation markers in patients with symptoms lasting beyond one year ([PMID: 39847575](https://pubmed.ncbi.nlm.nih.gov/39847575/)), complicating autoimmune explanations for chronic disease. The field lacks a completed interventional trial directly testing whether autoantibody removal or B-cell depletion improves Long COVID outcomes.

The evidence supports maintaining autoimmunity as an **EMERGING** mechanism for Long COVID, most relevant to pain-dominant and cardiopulmonary phenotypes, but insufficient to upgrade to ESTABLISHED status without longitudinal autoantibody-outcome correlation studies and positive interventional trial data.

---

## Key Findings

### Finding 1: Autoantibodies Are Consistently Detected After SARS-CoV-2 Infection, but Persistence Is Debated

Multiple independent studies confirm that SARS-CoV-2 infection triggers the production of diverse autoantibodies, including antinuclear antibodies (ANA), anti-phospholipid antibodies, anti-GPCR antibodies, and anti-neuronal antibodies. Talwar et al. ([PMID: 39956285](https://pubmed.ncbi.nlm.nih.gov/39956285/)) provide a comprehensive review stating that *"several studies show preexisting and/or de novo production of autoantibodies after infection with SARS-CoV-2, but the persistence of these antibodies and their role in causing long COVID is debated."* Hi et al. ([PMID: 41259457](https://pubmed.ncbi.nlm.nih.gov/41259457/)) found that among severe COVID-19 patients assessed two years post-discharge, 26 of 55 showed ANA reactivity compared to 0 of 21 controls — among the strongest evidence for long-term autoantibody persistence. However, this must be weighed against Jokiranta et al. ([PMID: 40915391](https://pubmed.ncbi.nlm.nih.gov/40915391/)), who demonstrated that *"all changes in B cell subpopulation proportions normalized within 200 dsso"* (days since symptom onset), suggesting that the cellular basis for ongoing autoantibody production is transient. The discrepancy between persistent autoantibody detection in severe cases and transient B-cell dysregulation in broader cohorts represents a key unresolved tension in the hypothesis.

### Finding 2: Extrafollicular B-cell Pathway Drives De Novo Autoreactivity in Severe COVID-19

The immunological mechanism generating autoantibodies in COVID-19 is increasingly well-characterized. Woodruff et al. ([PMID: 36044993](https://pubmed.ncbi.nlm.nih.gov/36044993/)) identified dysregulated naive B cells and de novo autoreactivity via extrafollicular pathways in severe COVID-19. Haslbauer et al. ([PMID: 33950285](https://pubmed.ncbi.nlm.nih.gov/33950285/)) provided tissue-level autopsy evidence from 20 lethal COVID-19 cases showing *"the absence/hypoplasia of germinal centers and increased presence of plasmablasts,"* implying impaired germinal center responses that favor extrafollicular B-cell maturation. Taghadosi et al. ([PMID: 36471421](https://pubmed.ncbi.nlm.nih.gov/36471421/)) synthesized the role of *"extrafollicular B cell response, Toll-like receptor-7 (TLR-7) activation, and neutrophil extracellular traps (NETs) formation in the development of AABs following SARS-CoV-2 infection."*

This pathway has been independently corroborated in HIV/SARS-CoV-2 co-infection ([PMID: 36300787](https://pubmed.ncbi.nlm.nih.gov/36300787/)), where HIV-positive patients show increased extrafollicular B-cell responses with reduced germinal center activity. Multi-omic profiling by Klein et al. ([PMID: 38318183](https://pubmed.ncbi.nlm.nih.gov/38318183/)) from a prospective cohort of 494 COVID-19 patients found that *"significant differences in autoantibodies and in epigenetic and transcriptional signatures in double-negative 1 B cells"* were among the earliest immune signatures associated with future PASC development, providing prospective evidence linking extrafollicular B-cell phenotypes to Long COVID risk.

### Finding 3: Molecular Mimicry Between SARS-CoV-2 and Human Proteins Is Computationally and Experimentally Validated

Molecular mimicry — structural similarity between viral and host proteins leading to cross-reactive immune responses — is a central pillar of the autoimmune model. Mohkhedkar et al. ([PMID: 34242919](https://pubmed.ncbi.nlm.nih.gov/34242919/)) computationally *"identified 28 human proteins harbouring regions homologous to SARS-CoV-2 peptides that could possibly be acting as autoantigens in COVID-19 patients displaying autoimmune conditions."* This computational prediction has been experimentally validated: Wu et al. ([PMID: 40343769](https://pubmed.ncbi.nlm.nih.gov/40343769/)) demonstrated that anti-mGluR2 (metabotropic glutamate receptor 2) autoantibodies from COVID-19 patients *"cross-react with both the nucleocapsid (N) and spike (S) proteins of SARS-CoV-2,"* confirmed by western blot analysis. Additionally, HSP60 molecular mimicry with SARS-CoV-2 proteins ([PMID: 41007425](https://pubmed.ncbi.nlm.nih.gov/41007425/)) has been implicated in endothelial dysfunction and thromboembolic complications. Vahabi et al. ([PMID: 36182877](https://pubmed.ncbi.nlm.nih.gov/36182877/)) described molecular mimicry as one of three prerequisites for the "autoimmune disease triangle" following COVID-19 infection.

### Finding 4: Passive Transfer of Long COVID IgG Induces Pain but Not Cognitive Symptoms in Mice

The most compelling direct evidence for autoantibody pathogenicity comes from Mignolet et al. ([PMID: 42053865](https://pubmed.ncbi.nlm.nih.gov/42053865/)), who performed the first passive transfer study using IgG from neurological Long COVID patients. They demonstrated that *"mice injected with IgG from long COVID patients showed no difference with the control group in terms of anxiety or depression behaviors, short- or long-term spatial memories. However, they displayed a transient decrease of paw withdrawal threshold and thermal hypersensitivity."* Passive transfer is the gold standard for demonstrating antibody pathogenicity. The result robustly supports the hypothesis for pain-dominant Long COVID phenotypes but simultaneously argues against autoantibodies as a sufficient explanation for cognitive dysfunction ("brain fog") — one of the most prevalent and debilitating Long COVID symptoms. The transient nature of the observed effect further raises questions about whether autoantibodies alone can sustain chronic symptomatology.

### Finding 5: GPCR and RAS Autoantibodies Are Systematically Elevated in COVID-19

Akbari et al. ([PMID: 37490975](https://pubmed.ncbi.nlm.nih.gov/37490975/)) conducted the most comprehensive meta-analysis of autoantibodies in COVID-19, analyzing 68 studies and identifying 18 distinct GPCR autoantibodies in studies of acute COVID-19 severity and 19 autoantibodies in post-/long-COVID studies. Their meta-analysis revealed *"a significantly higher number of seropositive ACE2 AAbs in COVID-19 patients (odds ratio = 7.766 [2.056, 29.208], p = 0.002) and particularly in severe disease (odds ratio = 11.49 [1.04, 126.86], p = 0.046)."* The breadth of GPCR targets — including adrenergic, muscarinic, and angiotensin receptors — provides a plausible molecular basis for the multi-organ autonomic dysfunction and cardiovascular manifestations seen in Long COVID. The IA-PACS-CFS trial protocol ([PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/)) documented that *"in patients with ME/CFS, autoantibodies against thyreoperoxidase (TPO), beta-adrenergic receptors (ß2AR), and muscarinic acetylcholine receptors (MAR) are frequently found,"* linking GPCR autoantibodies to the ME/CFS-like subtype of Long COVID and providing the rationale for ongoing immunoadsorption trials.

### Finding 6: Anti-Apolipoprotein A-1 Autoantibodies Predict Long COVID Symptom Persistence

L'Huillier et al. ([PMID: 35598178](https://pubmed.ncbi.nlm.nih.gov/35598178/)) provided uniquely strong longitudinal evidence. In a cohort of 193 hospital employees with COVID-19, anti-apolipoprotein A-1 (AAA1) seropositivity peaked at 93% at 1 month, declining to 15% at 12 months. Persistent symptoms at 12 months affected 45.1% of participants (neurological 28.5%, general 15%, respiratory 9.3%). Critically, *"COVID-19 induces a marked though transient AAA1 response, independently predicting one-year persistence of respiratory symptoms. By increasing IFN-alpha response, AAA1 may contribute to persistent symptoms."* This study uniquely bridges the gap between autoantibody detection and clinical outcomes, providing both a predictive biomarker and a mechanistic effector pathway (IFN-α-mediated macrophage activation).

---

## Mechanistic Causal Chain

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain of autoimmunity in Long COVID, showing evidence strength at each node from upstream viral trigger to clinical manifestation}}

The autoimmune model posits a multi-step causal chain from SARS-CoV-2 infection to chronic symptoms. Below, each step is annotated with its evidence strength and the critical gaps that remain:

```
UPSTREAM TRIGGER (STRONG evidence)
┌─────────────────────────────────────────────────────┐
│ SARS-CoV-2 infection                                │
│ → Tissue damage, viral antigen release              │
│ → Innate immune hyperactivation (cytokine storm)    │
│ → NETs formation exposes nuclear/cytoplasmic antigens│
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
B-CELL DYSREGULATION (STRONG evidence for acute phase)
┌─────────────────────────────────────────────────────┐
│ Germinal center disruption/hypoplasia (autopsy data)│
│ → Extrafollicular B-cell activation (DN2, ABCs)     │
│ → TLR-7 activation, NET formation                   │
│ → Loss of B-cell tolerance checkpoints              │
│ PMID: 36044993, 33950285, 36471421, 38318183       │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
AUTOANTIBODY GENERATION (STRONG evidence)
┌─────────────────────────────────────────────────────┐
│ Molecular mimicry (S/N → mGluR2, HSP60, etc.)      │
│ Bystander activation of autoreactive B cells        │
│ → Anti-GPCR, anti-phospholipid, anti-neuronal,     │
│   anti-ApoA1, anti-ACE2, anti-nuclear antibodies    │
│ PMID: 34242919, 40343769, 37490975                 │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
AUTOANTIBODY PERSISTENCE (DEBATED — KEY WEAKNESS)
┌─────────────────────────────────────────────────────┐
│ Some persist ≥2 years in severe cases (PMID:41259457)│
│ Most normalize within 200 days (PMID:40915391)      │
│ AAA1: 93% → 15% over 12 months (PMID:35598178)     │
│ ⚠ CRITICAL GAP: What maintains production in the   │
│   subset with Long COVID?                           │
│ Possible: viral persistence provides continuous     │
│   antigenic stimulation                             │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
TISSUE DAMAGE (MODERATE evidence — CRITICAL GAP)
┌─────────────────────────────────────────────────────┐
│ IgG-mediated sensory neuron activation (pain)   ✅  │
│ GPCR signaling disruption (dysautonomia)        ⚠️  │
│ Complement activation / immune complexes        ⚠️  │
│ Endothelial damage / microthrombosis            ⚠️  │
│ IFN-α upregulation via AAA1-macrophage axis     ⚠️  │
│ PMID: 42053865, 35598178                           │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
CLINICAL MANIFESTATION (VARIABLE by subtype)
┌─────────────────────────────────────────────────────┐
│ ✅ Pain, allodynia, sensory hypersensitivity        │
│ ✅ Cardiopulmonary symptoms (respiratory persist.)  │
│ ⚠️  Dysautonomia / POTS (plausible, unproven)      │
│ ❌ Cognitive dysfunction / brain fog                │
│ ❌ Fatigue / post-exertional malaise                │
└─────────────────────────────────────────────────────┘

Key: ✅ = supported by direct evidence  ⚠️ = plausible but unconfirmed
     ❌ = not supported by current autoantibody evidence
```

### Evidence Strength by Causal Link

| Causal Link | Evidence Strength | Key Gap |
|-------------|-------------------|---------|
| Infection → Immune activation | **STRONG** | None |
| Immune activation → B-cell dysregulation | **STRONG** (acute) | Does dysregulation persist beyond 200 days? |
| B-cell dysregulation → Autoantibody generation | **STRONG** | Which specific antibodies are pathogenic? |
| Autoantibody generation → Persistence | **WEAK/DEBATED** | What sustains production in Long COVID? |
| Persistent AAbs → Tissue damage | **MODERATE** (partial) | Only pain phenotype transferred in vivo |
| Tissue damage → Clinical symptoms | **VARIABLE** by subtype | Cognitive symptoms unexplained |

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Subtype/Context | Confidence | Limitations |
|---|----------|---------------|-----------|--------------------------|-------------|-----------------|------------|-------------|
| 1 | [PMID: 39956285](https://pubmed.ncbi.nlm.nih.gov/39956285/) | Review | Supports (with caveats) | De novo autoantibody production via B-cell dysregulation | Reviews evidence for B-cell dysregulation and autoantibodies; notes persistence and causal role debated | General Long COVID | Moderate | Review-level evidence |
| 2 | [PMID: 42053865](https://pubmed.ncbi.nlm.nih.gov/42053865/) | Human clinical + Animal model | Supports (partially) | IgG autoantibodies are pathogenic | Passive transfer induced allodynia and thermal hypersensitivity; NOT cognitive/mood deficits | Pain-dominant neurological LC | **High** | Only sensory symptoms transferred; transient |
| 3 | [PMID: 41259457](https://pubmed.ncbi.nlm.nih.gov/41259457/) | Human clinical | Supports | Autoantibodies persist ≥2 years post-severe COVID | 26/55 severe COVID patients ANA-reactive at 2 years vs 0/21 controls | Severe COVID survivors | Moderate | No Long COVID symptom correlation; severe cases only |
| 4 | [PMID: 40915391](https://pubmed.ncbi.nlm.nih.gov/40915391/) | Human clinical (longitudinal) | Qualifies / Partially refutes | B-cell dysregulation is transient | All B-cell subpopulation changes normalized within 200 days | General COVID-19 | **High** (n=120, 460d) | Anosmia as PASC proxy |
| 5 | [PMID: 36044993](https://pubmed.ncbi.nlm.nih.gov/36044993/) | Human clinical | Supports | Extrafollicular B cells generate de novo autoreactivity | Dysregulated naive B cells with de novo autoreactivity via extrafollicular pathway | Severe acute COVID | **High** | Acute phase; persistence unclear |
| 6 | [PMID: 38318183](https://pubmed.ncbi.nlm.nih.gov/38318183/) | Human clinical (multi-omic) | Supports | Early B-cell signatures predict PASC | DN1 B-cell epigenetic/transcriptional signatures and autoantibodies associated with incident PASC (n=494) | General PASC | **High** | PASC differences more limited than hospitalization effects |
| 7 | [PMID: 33950285](https://pubmed.ncbi.nlm.nih.gov/33950285/) | Human pathology (autopsy) | Supports | GC disruption favors extrafollicular response | Absence/hypoplasia of germinal centers, increased extrafollicular plasmablasts (n=20 autopsies) | Lethal COVID-19 | **High** | Lethal cases only |
| 8 | [PMID: 37490975](https://pubmed.ncbi.nlm.nih.gov/37490975/) | Systematic review + meta-analysis | Supports | GPCR/RAS autoantibodies elevated in COVID/post-COVID | 68 studies; 18 distinct GPCR AAbs; ACE2 AAbs OR=7.77 (p=0.002) | General COVID/LC | **High** (meta-analytic) | Heterogeneous study designs |
| 9 | [PMID: 40343769](https://pubmed.ncbi.nlm.nih.gov/40343769/) | Human clinical + In vitro | Supports | Molecular mimicry generates cross-reactive neuronal AAbs | Anti-mGluR2 cross-reacts with SARS-CoV-2 N and S proteins; western blot validated | Neurological COVID | Moderate-High | Small cohort |
| 10 | [PMID: 34242919](https://pubmed.ncbi.nlm.nih.gov/34242919/) | Computational | Supports | Molecular mimicry between SARS-CoV-2 and human proteins | 28 human proteins with homologous regions to validated SARS-CoV-2 B-cell epitopes | Multi-organ autoimmunity | Moderate | Computational; not all validated |
| 11 | [PMID: 35598178](https://pubmed.ncbi.nlm.nih.gov/35598178/) | Human clinical (longitudinal) | Supports | Anti-ApoA1 AAbs predict LC persistence | AAA1 from 3 months predicts respiratory symptoms at 12 months; IFN-α mechanism | Respiratory LC | Moderate-High | Single AAb type; moderate sample |
| 12 | [PMID: 36471421](https://pubmed.ncbi.nlm.nih.gov/36471421/) | Review | Supports | EF pathway, TLR-7, NETs | Identifies pathways generating autoantibodies post-COVID | General COVID | Moderate | Review-level evidence |
| 13 | [PMID: 34082475](https://pubmed.ncbi.nlm.nih.gov/34082475/) | Human clinical | Supports (with caveats) | Tissue-specific AAbs persist post-COVID | Higher AAb frequency in COVID ITU vs non-COVID ITU; restricted panel (skin, muscle, cardiac) | Severe COVID | Moderate | Small sample (n=84) |
| 14 | [PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/) | Clinical trial protocol | Supports (indirect) | Immunoadsorption of AAbs may treat PACS-CFS | RCT protocol based on anti-ß2AR and anti-MAR evidence | ME/CFS-type LC | Low (protocol only) | Results not yet available |
| 15 | [PMID: 36715690](https://pubmed.ncbi.nlm.nih.gov/36715690/) | Human clinical (longitudinal) | Qualifies | COVID thyroid autoimmunity resolves | Thyroid dysfunction normalized over 12 months; no increased autoantibody prevalence | Thyroid-specific | Moderate-High | Suggests autoimmunity is self-limiting |
| 16 | [PMID: 39847575](https://pubmed.ncbi.nlm.nih.gov/39847575/) | Human clinical (population-based) | Qualifies | Persistent PCS lacks autoimmune markers | No elevated complement, inflammatory markers, or EBV markers in persistent PCS at >1 year | Persistent PCS (>1 year) | **High** | Large cohort, comprehensive testing |
| 17 | [PMID: 35911726](https://pubmed.ncbi.nlm.nih.gov/35911726/) | Human clinical | Refutes (for vaccines) | Vaccination-induced autoimmunity | COVID-19 vaccination did NOT trigger significant aPL or autoantibody production | Vaccinated healthcare workers | **High** | Applies to vaccination, not infection |

---

## Alternative and Competing Mechanistic Models

The autoimmune model exists within a broader landscape of Long COVID pathogenic hypotheses. Understanding their relationships is essential for accurate curation and for designing discriminating experiments.

### 1. Viral Persistence / Reservoir Model
- **Relationship:** UPSTREAM CAUSE or PARALLEL MECHANISM
- **Evidence:** Multiple studies detect persistent SARS-CoV-2 RNA/protein in gut-associated lymphoid tissue ([PMID: 41794369](https://pubmed.ncbi.nlm.nih.gov/41794369/)), adipose tissue ([PMID: 41287121](https://pubmed.ncbi.nlm.nih.gov/41287121/)), and other sanctuary sites months after acute infection. Wang et al. ([PMID: 41494535](https://pubmed.ncbi.nlm.nih.gov/41494535/)) identified intestinal viral reservoirs that disrupt VLCFA-peroxisome signaling as an autoimmunity-independent mechanism for GI symptoms.
- **Relationship to autoimmunity:** Viral persistence could provide continuous antigenic stimulation sustaining autoantibody production, potentially resolving the persistence gap. If viral reservoirs are the root cause, autoimmunity may be a downstream amplifier.
- **Competing strength:** Comparable or stronger. Viral persistence can independently explain multiple Long COVID features and potentially unifies autoimmune, inflammatory, and metabolic mechanisms. However, Bahmer et al. ([PMID: 39847575](https://pubmed.ncbi.nlm.nih.gov/39847575/)) found negative viral persistence screening (stool PCR and plasma spike antigen) in persistent PCS patients, challenging the universality of this model as well.

### 2. Latent Virus Reactivation (EBV/CMV) Model
- **Relationship:** PARALLEL MECHANISM, possibly SYNERGISTIC
- **Evidence:** Stervbo et al. ([PMID: 42002663](https://pubmed.ncbi.nlm.nih.gov/42002663/)) found EBV reactivated in 68–73% of hospitalized COVID-19 patients, with altered CD8 T-cell phenotypes. Lorenz et al. ([PMID: 41518079](https://pubmed.ncbi.nlm.nih.gov/41518079/)) showed enhanced antibody reactivity to specific EBV EBNA1 epitopes in post-COVID syndrome patients. Schneiderova et al. ([PMID: 40540397](https://pubmed.ncbi.nlm.nih.gov/40540397/)) linked host IL-1 genetics to EBV reactivation risk and pulmonary dysfunction in Long COVID.
- **Relationship to autoimmunity:** EBV is a well-established driver of autoimmune diseases (MS, SLE). EBV reactivation could independently trigger autoimmunity via its own molecular mimicry, making the two mechanisms synergistic. However, the population-based PCS study ([PMID: 39847575](https://pubmed.ncbi.nlm.nih.gov/39847575/)) found no evidence of EBV reactivation markers in persistent PCS at >1 year.

### 3. Thromboinflammation / Microclot / Endotheliopathy Model
- **Relationship:** DOWNSTREAM CONSEQUENCE or PARALLEL MECHANISM
- **Evidence:** Nicolai et al. ([PMID: 37178769](https://pubmed.ncbi.nlm.nih.gov/37178769/)) reviewed persistent vascular damage, microclots, elevated D-dimer, and perfusion abnormalities in Long COVID. Pretorius et al. ([PMID: 36015078](https://pubmed.ncbi.nlm.nih.gov/36015078/)) found similar coagulopathy (hyperactivated platelets, fibrinaloid microclots) in ME/CFS.
- **Relationship to autoimmunity:** Anti-phospholipid autoantibodies ([PMID: 32602200](https://pubmed.ncbi.nlm.nih.gov/32602200/)) may directly drive coagulopathy, making thromboinflammation partially downstream of the autoimmune model. However, direct endothelial infection and complement activation can independently cause persistent thromboinflammation. This model provides a more parsimonious explanation for fatigue and cognitive symptoms via tissue hypoxia.

### 4. Chronic Inflammatory / Metabolic Dysregulation Model
- **Relationship:** PARALLEL MECHANISM
- **Evidence:** Gabernet et al. ([PMID: 40924481](https://pubmed.ncbi.nlm.nih.gov/40924481/)) identified a multiomics "recovery factor" from >500 IMPACC patients: persistent inflammation, heme metabolism signatures, decreased androgenic steroids, and increased myeloid cell frequencies predicted Long COVID independently of acute severity.
- **Relationship to autoimmunity:** This broader immune dysregulation signature encompasses but extends beyond autoantibody mechanisms. The emphasis on myeloid-driven inflammation and metabolic disruption suggests Long COVID biology is broader than B-cell-mediated autoimmunity alone.

### 5. Autonomic Nervous System Dysfunction / Serotonin Depletion
- **Relationship:** DOWNSTREAM CONSEQUENCE (partially)
- **Evidence:** Tavee ([PMID: 39154907](https://pubmed.ncbi.nlm.nih.gov/39154907/)) reviewed dysautonomia in Long COVID, noting autoantibodies as one contributing factor alongside reduced serotonin levels and microglial activation.
- **Relationship to autoimmunity:** GPCR autoantibodies (anti-ß2AR, anti-MAR) could directly cause autonomic dysfunction, making this partially downstream. However, serotonin depletion and brainstem signaling disruption may operate independently.

---

## Knowledge Gaps

### Gap 1: Autoantibody Persistence Mechanism (CRITICAL)
- **Scope:** The mechanism sustaining autoantibody production beyond the acute phase is unknown.
- **Why it matters:** If autoantibodies are transient (as suggested by [PMID: 40915391](https://pubmed.ncbi.nlm.nih.gov/40915391/)), they cannot independently explain symptoms lasting months to years. The hypothesis requires either long-lived autoreactive plasma cells, continuous restimulation by viral reservoirs, or self-perpetuating autoimmune feedback loops.
- **What was checked:** Longitudinal B-cell phenotyping, longitudinal autoantibody kinetics (anti-ApoA1, ANA, thyroid autoantibodies).
- **Resolving evidence:** Bone marrow biopsy assessment for long-lived autoreactive plasma cells in Long COVID patients; paired measurements of autoantibody titers and tissue viral antigen levels at multiple time points.

### Gap 2: Causal vs. Epiphenomenal Autoantibodies (CRITICAL)
- **Scope:** Whether detected autoantibodies are pathogenic drivers or bystander markers of immune activation.
- **Why it matters:** The therapeutic premise (immunoadsorption, IVIG, B-cell depletion) depends entirely on autoantibodies being causal.
- **What was checked:** One passive transfer study showing partial pathogenicity; no controlled depletion trial results available.
- **Resolving evidence:** Results from the IA-PACS-CFS trial ([PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/)); additional passive transfer experiments with purified autoantibody fractions targeting specific symptom domains.

### Gap 3: Cognitive Symptom Mechanism (SIGNIFICANT)
- **Scope:** Brain fog and cognitive dysfunction — among the most debilitating Long COVID symptoms — are NOT explained by autoantibody passive transfer.
- **Why it matters:** The hypothesis claims to explain "multisystem symptoms" but the most prevalent complaint lacks experimental autoimmune support.
- **What was checked:** Passive transfer of total IgG to mice ([PMID: 42053865](https://pubmed.ncbi.nlm.nih.gov/42053865/)) showed no cognitive, memory, or mood effects.
- **Resolving evidence:** Intrathecal IgG transfer experiments; CSF-specific autoantibody profiling; investigation of blood-brain barrier permeability as a permissive factor for autoantibody CNS access.

### Gap 4: Subtype-Specific Autoantibody Profiles (MODERATE)
- **Scope:** Whether specific autoantibody profiles map to specific Long COVID phenotypic clusters.
- **Why it matters:** If autoimmunity drives Long COVID, different autoantibody specificities should predict different symptom clusters, enabling precision immunotherapy.
- **What was checked:** Most studies measure autoantibodies without systematic phenotyping by Long COVID subtype.
- **Resolving evidence:** Large cohort (n>500) with comprehensive autoantibody panels linked to validated Long COVID symptom clusters (pain, cognitive, fatigue, cardiopulmonary, autonomic).

### Gap 5: Specificity to SARS-CoV-2 vs. Generic Post-Viral Response (MODERATE)
- **Scope:** Whether autoantibodies are specific to SARS-CoV-2 or a generic consequence of severe viral infection.
- **Why it matters:** If any severe respiratory virus triggers similar autoantibodies, the mechanism is not SARS-CoV-2-specific. Haw et al. ([PMID: 34082475](https://pubmed.ncbi.nlm.nih.gov/34082475/)) showed COVID patients had a more restricted autoantibody panel than non-COVID ICU controls, but no direct comparison with influenza or RSV was identified.
- **Resolving evidence:** Head-to-head autoantibody profiling in matched cohorts of post-COVID, post-influenza, and post-RSV patients.

### Gap 6: Absence of Completed Interventional Trials (CRITICAL)
- **Scope:** No completed RCT of B-cell depletion, immunoadsorption, or IVIG in Long COVID.
- **Why it matters:** Therapeutic proof-of-concept is the most convincing test of a disease mechanism hypothesis.
- **What was checked:** Searched for rituximab, immunoadsorption, IVIG, and plasmapheresis trials in Long COVID. Found one ongoing protocol ([PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/)) and uncontrolled IVIG case series ([PMID: 39389388](https://pubmed.ncbi.nlm.nih.gov/39389388/)).
- **Resolving evidence:** Completion of IA-PACS-CFS trial and additional RCTs of B-cell-targeted therapies.

### Gap 7: Source/Dataset Absences
- No **GenCC or ClinGen** entries for genetic associations with autoimmune Long COVID identified.
- No **GWAS or HLA association** data for autoantibody-positive Long COVID found.
- No completed **ClinicalTrials.gov-registered RCT** of anti-B-cell therapy for Long COVID found.
- No large-scale **PhIP-Seq or protein array** autoantibody discovery study in well-phenotyped Long COVID identified.

---

## Discriminating Tests

### Test 1: Immunoadsorption RCT in Autoantibody-Positive Long COVID (HIGHEST PRIORITY)
- **Design:** Double-blind, sham-controlled trial of immunoadsorption (5 cycles)
- **Patient stratification:** Long COVID patients with elevated GPCR autoantibodies (anti-ß2AR, anti-M3R, anti-M4R) vs. autoantibody-negative Long COVID
- **Biomarkers:** Pre/post autoantibody titers (GPCR panel, ANA, anti-PL), inflammatory markers, heart rate variability
- **Expected result if hypothesis correct:** Symptom improvement correlating with autoantibody depletion
- **Expected result if hypothesis wrong:** No improvement despite autoantibody reduction
- **Status:** Protocol registered ([PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/)); results pending

### Test 2: Longitudinal Autoantibody-Symptom Correlation Study
- **Design:** Prospective cohort, n≥500, serial blood draws at 1, 3, 6, 12, 24 months post-COVID
- **Biomarkers:** Broad autoantibody panel (GPCR, aPL, ANA, anti-neuronal, AAA1), B-cell subset flow cytometry (DN2, ABCs, plasmablasts)
- **Stratification:** By symptom cluster (pain, cognitive, cardiopulmonary, fatigue, autonomic)
- **Expected result if hypothesis correct:** Persistent autoantibodies in patients with ongoing symptoms; declining autoantibodies in those who recover; specific autoantibody-symptom associations

### Test 3: Expanded Passive Transfer with CNS Endpoints
- **Design:** Passive transfer of IgG from symptom-stratified Long COVID patients into mice, with optional blood-brain barrier disruption (low-dose LPS) to model neuroinflammatory conditions
- **Patient groups:** (a) Pain-dominant, (b) Cognitive-dominant, (c) Cardiopulmonary-dominant, (d) Fatigue-dominant
- **Endpoints:** Pain (von Frey, hot plate), cognition (novel object recognition, Barnes maze), cardiac function (echocardiography), autonomic measures
- **Expected result if hypothesis correct:** Subtype-specific symptom transfer; cognitive deficits emerge with BBB disruption

### Test 4: Unbiased Autoantibody Discovery (PhIP-Seq/Protein Array)
- **Design:** High-throughput autoantibody target identification in serum and CSF
- **Sample:** n>200 Long COVID, n>100 recovered controls, n>100 uninfected controls
- **Outcome:** Identification of novel pathogenic autoantibody targets; validation by functional assays
- **Expected result:** Discovery of autoantibody signatures specific to Long COVID subtypes

### Test 5: Antiviral Therapy to Test Viral Persistence-Autoimmunity Link
- **Design:** RCT of prolonged antiviral therapy (Paxlovid) in Long COVID patients
- **Biomarkers:** Pre/post autoantibody titers alongside viral antigen levels
- **Expected result if viral persistence drives autoimmunity:** Antiviral reduces both viral load and autoantibodies; if autoimmunity is self-sustaining, antivirals reduce viral load but not autoantibodies

---

## Curation Leads

*All items below are candidate updates for the Disorder Mechanisms Knowledge Base requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 42053865](https://pubmed.ncbi.nlm.nih.gov/42053865/)** (Mignolet et al., 2026) — *Priority: HIGH*
   - **Snippet:** *"Mice injected with IgG from long COVID patients showed no difference with the control group in terms of anxiety or depression behaviors, short- or long-term spatial memories. However, they displayed a transient decrease of paw withdrawal threshold and thermal hypersensitivity"*
   - **Proposed KB entry:** SUPPORT with qualifier — supports pathogenicity for pain-dominant subtype only

2. **[PMID: 40915391](https://pubmed.ncbi.nlm.nih.gov/40915391/)** (Jokiranta et al., 2025) — *Priority: HIGH*
   - **Snippet:** *"All changes in B cell subpopulation proportions normalized within 200 dsso."*
   - **Proposed KB entry:** QUALIFY — B-cell dysregulation is transient, challenging the persistence component

3. **[PMID: 38318183](https://pubmed.ncbi.nlm.nih.gov/38318183/)** (Klein et al., 2024) — *Priority: HIGH*
   - **Snippet:** *"significant differences in autoantibodies and in epigenetic and transcriptional signatures in double-negative 1 B cells, in particular"*
   - **Proposed KB entry:** SUPPORT — early DN1 B-cell signatures prospectively predict PASC

4. **[PMID: 37490975](https://pubmed.ncbi.nlm.nih.gov/37490975/)** (Akbari et al., 2023) — *Priority: HIGH*
   - **Snippet:** *"Meta-analysis revealed a significantly higher number of seropositive ACE2 AAbs in COVID-19 patients (odds ratio = 7.766 [2.056, 29.208], p = 0.002)"*
   - **Proposed KB entry:** SUPPORT — meta-analytic confirmation of GPCR/RAS autoantibodies

5. **[PMID: 40343769](https://pubmed.ncbi.nlm.nih.gov/40343769/)** (Wu et al., 2025) — *Priority: MODERATE*
   - **Snippet:** *"Western blot analysis showed these antibodies cross-react with both the nucleocapsid (N) and spike (S) proteins of SARS-CoV-2."*
   - **Proposed KB entry:** SUPPORT — experimental validation of molecular mimicry (mGluR2-specific)

6. **[PMID: 35598178](https://pubmed.ncbi.nlm.nih.gov/35598178/)** (L'Huillier et al., 2022) — *Priority: HIGH*
   - **Snippet:** *"COVID-19 induces a marked though transient AAA1 response, independently predicting one-year persistence of respiratory symptoms. By increasing IFN-alpha response, AAA1 may contribute to persistent symptoms."*
   - **Proposed KB entry:** SUPPORT — longitudinal prediction of Long COVID persistence via autoantibody

7. **[PMID: 39847575](https://pubmed.ncbi.nlm.nih.gov/39847575/)** (Bahmer et al., 2025) — *Priority: MODERATE*
   - **Proposed KB entry:** QUALIFY — no elevated complement, inflammatory, or autoimmune markers in persistent PCS at >1 year, challenging late-stage autoimmune hypothesis

### Candidate Pathophysiology Nodes and Edges

- **Node:** Extrafollicular B-cell activation (DN2 cells, activated naive B cells)
- **Node:** Double-negative 1 B cells as early PASC biomarker
- **Edge:** SARS-CoV-2 infection → Germinal center hypoplasia → Extrafollicular B-cell pathway → Autoantibody generation (STRONG)
- **Edge:** Molecular mimicry (SARS-CoV-2 S/N proteins) → Cross-reactive autoantibodies → Tissue damage (MODERATE)
- **Edge:** Anti-GPCR autoantibodies → Autonomic dysfunction (CANDIDATE — needs functional confirmation)
- **Edge:** Anti-mGluR2 ↔ SARS-CoV-2 N/S (molecular mimicry, experimentally confirmed)

### Candidate Ontology Terms

- **Cell types:** Double-negative 1 B cell (DN1), Double-negative 2 B cell (DN2), Activated naive B cell (ABN), Extrafollicular plasmablast
- **Biological processes:** Extrafollicular antibody response, Molecular mimicry, Bystander activation, Germinal center reaction
- **Molecular targets:** Anti-ß2AR, anti-M3R, anti-M4R, anti-AT1R, anti-ACE2, anti-mGluR2, anti-apolipoprotein A-1

### Candidate Subtype Restrictions

| Subtype | Support Level | Key Evidence |
|---------|---------------|--------------|
| Pain-dominant Long COVID | **Strong** | Passive transfer evidence (PMID: 42053865) |
| Cardiopulmonary-dominant | **Moderate** | AAA1 prediction, anti-PL (PMID: 35598178) |
| ME/CFS-type / Autonomic | **Moderate** | GPCR AAbs (PMID: 37490975, 38454468) |
| Cognitive-dominant | **Weak/None** | Passive transfer negative for cognition |
| **Recommendation:** Consider splitting hypothesis applicability by subtype rather than treating as universal |

### Candidate Status Change

- **Current:** EMERGING
- **Recommended:** **Maintain EMERGING**. Upgrade to SUPPORTED contingent on: (a) positive interventional trial data demonstrating symptom improvement with autoantibody depletion, (b) large longitudinal study demonstrating persistent pathogenic autoantibodies correlating with Long COVID symptom persistence, or (c) replication of passive transfer findings with broader symptom coverage.

### Candidate Knowledge Gaps for KB

1. `autoantibody_persistence_mechanism` — What sustains autoantibody production beyond the acute phase?
2. `causal_vs_epiphenomenal` — Are autoantibodies causal drivers or bystander markers?
3. `cognitive_symptom_mechanism` — Why does IgG transfer not reproduce cognitive symptoms?
4. `therapeutic_proof_of_concept` — No completed RCT of autoimmunity-targeted therapy in Long COVID
5. `viral_persistence_autoimmunity_interaction` — Does viral persistence sustain autoantibody production?
6. `genetic_susceptibility` — No GWAS/HLA data for autoimmune Long COVID subtypes

---

## Limitations of This Report

1. **Search scope:** Literature search was conducted via PubMed only; preprints (medRxiv, bioRxiv) and conference abstracts were not systematically screened, potentially missing very recent findings.
2. **Publication bias:** Positive autoantibody findings are more likely published than negative results, potentially inflating apparent support for the hypothesis.
3. **Heterogeneous definitions:** "Long COVID" definitions vary across studies (WHO, NICE, CDC criteria), and many studies report on post-acute COVID or post-COVID syndrome without distinguishing specific phenotypic subtypes.
4. **Pre-Omicron bias:** Much foundational evidence (extrafollicular B cells, germinal center pathology) derives from severe, pre-vaccination, pre-Omicron cohorts. Applicability to post-Omicron, post-vaccination Long COVID is uncertain. Teo et al. ([PMID: 41639746](https://pubmed.ncbi.nlm.nih.gov/41639746/)) showed that PASC risks were attenuated in later Omicron waves with high vaccination rates.
5. **Animal model limitations:** The passive transfer study used a single mouse strain (C57BL/6J) and total IgG rather than purified autoantibody fractions, limiting mechanistic resolution.
6. **Single-iteration constraint:** This report synthesizes evidence from a focused investigation. Additional iterations might identify emerging clinical trial results, newer longitudinal cohort data, or mechanistic studies not captured in this search.

---

## Proposed Follow-up Experiments and Actions

1. **Priority 1 — Track IA-PACS-CFS trial results:** The double-blinded immunoadsorption trial ([PMID: 38454468](https://pubmed.ncbi.nlm.nih.gov/38454468/)) is the most direct test of the autoimmune hypothesis. Monitor for publication and update KB accordingly.

2. **Priority 2 — Serial autoantibody profiling in phenotyped Long COVID cohorts:** Partner with existing cohorts (IMPACC, RECOVER) to add comprehensive autoantibody panels with symptom-cluster stratification at multiple longitudinal time points.

3. **Priority 3 — Replicate and extend passive transfer model:** Test purified autoantibody fractions (anti-GPCR, anti-neuronal) rather than total IgG; include BBB disruption conditions; test in additional mouse strains; expand endpoint panels to cardiac, pulmonary, and fatigue measures.

4. **Priority 4 — HLA and GWAS analysis:** Perform HLA genotyping in autoantibody-positive vs. autoantibody-negative Long COVID patients to identify genetic predisposition to the autoimmune subtype.

5. **Priority 5 — Cross-viral comparison:** Design head-to-head autoantibody profiling studies comparing post-COVID, post-influenza, and post-RSV patients to establish SARS-CoV-2 specificity of the autoimmune response.

6. **Priority 6 — KB literature monitoring:** Set automated alerts for: (a) Long COVID + rituximab/anti-CD20 trial results, (b) Long COVID + immunoadsorption outcomes, (c) PhIP-Seq autoantibody discovery studies, (d) longitudinal autoantibody-clinical outcome correlation publications.
