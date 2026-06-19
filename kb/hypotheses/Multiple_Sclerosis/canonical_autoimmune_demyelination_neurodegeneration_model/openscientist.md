---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T15:23:58.424229'
end_time: '2026-05-23T16:02:39.626243'
duration_seconds: 2321.2
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Multiple Sclerosis
  category: Neurological Disorder
  hypothesis_group_id: canonical_autoimmune_demyelination_neurodegeneration_model
  hypothesis_label: Canonical Autoimmune Demyelination and Neurodegeneration Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_autoimmune_demyelination_neurodegeneration_model\n\
    hypothesis_label: Canonical Autoimmune Demyelination and Neurodegeneration Model\n\
    status: CANONICAL\ndescription: In genetically susceptible individuals (HLA-DRB1*15:01\
    \ and >200 additional risk variants),\n  autoreactive CD4+ Th1/Th17 and CD8+ T\
    \ cells, B cells, and plasmablasts cross the blood-brain barrier\n  and orchestrate\
    \ focal inflammatory demyelination of CNS white-matter and gray-matter lesions.\
    \ The resulting\n  myelin loss is paralleled by progressive axonal and neuronal\
    \ damage, with chronic active (\"smoldering\")\n  inflammation and meningeal lymphoid\
    \ aggregates driving disability accumulation in progressive MS. EBV\n  infection\
    \ of B cells is now established as a near-necessary upstream environmental trigger.\
    \ Disease-modifying\n  therapies that deplete B cells (anti-CD20), block lymphocyte\
    \ egress (S1P receptor modulators), or trap\n  them in lymph nodes (natalizumab)\
    \ provide direct interventional validation of the autoimmune arm of\n  the canonical\
    \ model.\nevidence:\n- reference: PMID:24507511\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Multiple sclerosis (MS) is considered a prototype\
    \ inflammatory autoimmune disord\n  explanation: |\n    Canonical mechanism review\
    \ used as the seed reference for the hypothesis-search deep-research run."
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
citation_count: 36
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Multiple Sclerosis
- **Category:** Neurological Disorder

## Target Hypothesis
- **Hypothesis ID:** canonical_autoimmune_demyelination_neurodegeneration_model
- **Hypothesis Label:** Canonical Autoimmune Demyelination and Neurodegeneration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_autoimmune_demyelination_neurodegeneration_model
hypothesis_label: Canonical Autoimmune Demyelination and Neurodegeneration Model
status: CANONICAL
description: In genetically susceptible individuals (HLA-DRB1*15:01 and >200 additional risk variants),
  autoreactive CD4+ Th1/Th17 and CD8+ T cells, B cells, and plasmablasts cross the blood-brain barrier
  and orchestrate focal inflammatory demyelination of CNS white-matter and gray-matter lesions. The resulting
  myelin loss is paralleled by progressive axonal and neuronal damage, with chronic active ("smoldering")
  inflammation and meningeal lymphoid aggregates driving disability accumulation in progressive MS. EBV
  infection of B cells is now established as a near-necessary upstream environmental trigger. Disease-modifying
  therapies that deplete B cells (anti-CD20), block lymphocyte egress (S1P receptor modulators), or trap
  them in lymph nodes (natalizumab) provide direct interventional validation of the autoimmune arm of
  the canonical model.
evidence:
- reference: PMID:24507511
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Multiple sclerosis (MS) is considered a prototype inflammatory autoimmune disord
  explanation: |
    Canonical mechanism review used as the seed reference for the hypothesis-search deep-research run.
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

# Hypothesis-Search Report: Canonical Autoimmune Demyelination and Neurodegeneration Model for Multiple Sclerosis

**Hypothesis ID:** `canonical_autoimmune_demyelination_neurodegeneration_model`  
**Status in KB:** CANONICAL  
**Report Date:** 2026-05-23  
**Papers Reviewed:** 81  
**Confirmed Findings:** 7  

---

## Executive Judgment

**Verdict: SUPPORTED with significant qualifications.**

The canonical autoimmune demyelination and neurodegeneration model for multiple sclerosis is strongly supported by converging genetic, epidemiological, immunological, and therapeutic evidence — particularly for the relapsing-remitting phase of disease. Its three foundational pillars are now robustly validated: (1) EBV infection as a near-necessary upstream trigger with a 32-fold risk increase (Bjornevik et al. 2022); (2) polygenic immune susceptibility anchored by HLA-DRB1\*15:01 and >200 additional GWAS loci enriched for adaptive immunity genes; and (3) therapeutic proof-of-concept from B cell-depleting anti-CD20 therapies, S1P receptor modulators, and natalizumab, which reduce relapse rates by 46–70% and MRI lesion activity by >90%.

However, the model is incomplete and requires important qualifications for progressive MS. Disability accumulation occurs predominantly through progression independent of relapse activity (PIRA), driven by compartmentalized CNS inflammation (chronic active "smoldering" lesions, meningeal lymphoid follicles) and neurodegeneration that is largely resistant to current disease-modifying therapies. The competing "inside-out" (CNS-first) hypothesis — in which primary oligodendrocyte or myelin pathology triggers secondary autoimmune responses — provides a plausible alternative or complementary mechanism that the canonical model does not adequately address. Additionally, mitochondrial dysfunction, oxidative stress, microglial activation, and gut microbiome dysbiosis represent parallel or downstream mechanisms that expand beyond the canonical autoimmune framework. The most important caveat is that no current therapy fully prevents disability progression, indicating that the canonical model captures the inflammatory but not the neurodegenerative arm of MS with mechanistic precision.

---

## Summary

The canonical autoimmune demyelination and neurodegeneration model posits that MS arises when genetically susceptible individuals (carrying HLA-DRB1\*15:01 and >200 additional risk variants) develop autoreactive T cells (CD4+ Th1/Th17 and CD8+), B cells, and plasmablasts that cross the blood-brain barrier and orchestrate focal inflammatory demyelination in CNS white and gray matter. This process is paralleled by progressive axonal and neuronal damage, with chronic active inflammation and meningeal lymphoid aggregates driving disability accumulation in progressive disease. EBV infection of B cells is established as a near-necessary upstream environmental trigger.

This investigation systematically evaluated each claim in the hypothesis against primary literature. The strongest evidence supports the EBV-MS causal link, the polygenic immune architecture, and the efficacy of B cell-targeted therapies. The weakest links concern the precise mechanism by which EBV triggers autoimmunity, the causal chain from focal inflammation to progressive neurodegeneration, and whether the autoimmune attack is truly primary (outside-in) or secondary to a CNS-intrinsic degenerative process (inside-out). Emerging BTK inhibitors that penetrate the CNS and target both B cells and microglia represent the next critical test of whether compartmentalized inflammation can be therapeutically modulated to slow progression.

Seven key findings were confirmed through literature synthesis, spanning the EBV trigger, genetic architecture, B cell depletion therapy, chronic active lesions, inside-out competing model, PIRA as a dominant disability mechanism, and BTK inhibitors as next-generation therapeutic tests. Together, these findings paint a picture of a canonical model that is well-validated for relapsing disease but requires substantial extension and qualification for progressive MS.

---

## Key Findings

### Finding 1: EBV Established as Near-Necessary Upstream Trigger for MS

The Epstein-Barr virus has been elevated from an epidemiological association to a near-causal factor for MS. The landmark longitudinal study by Bjornevik et al. (2022) tracked over 10 million US military personnel and demonstrated that MS risk increased 32-fold following EBV infection (HR = 32), with no comparable risk increase after infection with other viruses, including the similarly transmitted cytomegalovirus ([PMID: 35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/)). Critically, serum neurofilament light chain (NfL), a biomarker of neuroaxonal degeneration, increased only after EBV seroconversion — establishing temporal precedence of EBV infection before neurodegeneration onset.

The molecular mechanism linking EBV to MS autoimmunity was elucidated by Lanz et al. (2022), who identified molecular mimicry between the EBV nuclear antigen 1 (EBNA1) and the glial cell adhesion molecule GlialCAM. Clonally expanded B cells in the CSF of MS patients were shown to bind both EBNA1 and GlialCAM, providing a plausible molecular bridge between viral infection and CNS autoimmunity ([PMID: 35073561](https://pubmed.ncbi.nlm.nih.gov/35073561/)). Sattarnezhad et al. (2025) subsequently confirmed cross-reactive antibodies in a large cohort of 650 MS patients versus 661 controls, demonstrating epitope spreading from EBNA1 to adjacent GlialCAM peptide regions ([PMID: 40063790](https://pubmed.ncbi.nlm.nih.gov/40063790/)). Population-based epidemiological data further support this, with infectious mononucleosis conferring an odds ratio of 2.06 (95% CI 1.71–2.48) for MS risk ([PMID: 19209005](https://pubmed.ncbi.nlm.nih.gov/19209005/)).

The genetic architecture of EBV-MS susceptibility was further refined by studies showing that HLA haplotypes associated with anti-EBNA1 IgG levels overlap extensively with known MS risk alleles, particularly DRB1\*15:01, suggesting that the HLA-mediated MS risk may partly operate through dysregulated immune control of EBV ([PMID: 38630618](https://pubmed.ncbi.nlm.nih.gov/38630618/)). **Status: Established.** The EBV–MS link is now considered one of the strongest environment–disease associations in medicine, though the precise causal mechanism (molecular mimicry, bystander activation, immortalization of autoreactive B cells, or their combination) remains under active investigation.

### Finding 2: HLA-DRB1\*15:01 and >200 GWAS Variants Confirm Polygenic Immune-Mediated Architecture

The genetic architecture of MS is unambiguously polygenic and immune-centered. The most comprehensive 2026 review confirms >200 MS susceptibility-associated genomic regions, with HLA-DRB1\*15:01 remaining the most robust and reproducible risk factor ([PMID: 41934071](https://pubmed.ncbi.nlm.nih.gov/41934071/)). Non-HLA loci implicate T-cell and B-cell activation, cytokine signaling (IL-2RA, IL-7R), co-stimulation (CD40, CD58), and antigen presentation pathways.

Mendelian randomization analyses have provided causal evidence: Yan et al. (2025) demonstrated that HLA-DRB1 confers an OR of 2.24 for MS risk with 100% colocalization probability, alongside causal roles for microglial genes ARHGAP25, MERTK, MS4A6A, and SYK ([PMID: 41239018](https://pubmed.ncbi.nlm.nih.gov/41239018/)). Misicka et al. (2024) extended this to disease timing, identifying GWAS loci associated with MS age-at-onset that were enriched for adaptive and complement immunity genes ([PMID: 38817245](https://pubmed.ncbi.nlm.nih.gov/38817245/)). Khan et al. (2025) confirmed that HLA-DRB1\*15:01, IL-2RA, IL-7R, CD40, and CD58 are all implicated in immune regulation pathways relevant to MS ([PMID: 39810445](https://pubmed.ncbi.nlm.nih.gov/39810445/)).

Notably, multicase family studies suggest that familial aggregation in MS does not reflect substantially enriched polygenic risk compared to population-based cases, indicating that environmental and stochastic factors contribute meaningfully beyond genetic predisposition ([PMID: 40225927](https://pubmed.ncbi.nlm.nih.gov/40225927/)). **Status: Established.** The polygenic immune architecture is one of the best-characterized aspects of MS.

### Finding 3: B Cell Depletion Therapy Provides Strong Interventional Validation

The dramatic efficacy of anti-CD20 therapies represents the strongest interventional evidence for the autoimmune arm of the canonical model. Ocrelizumab achieved 46–47% reduction in annualized relapse rates and 94–95% fewer gadolinium-enhancing lesions compared to interferon-beta in the OPERA I/II trials for RRMS. In the ORATORIO trial, ocrelizumab became the first drug to significantly reduce disability progression in primary progressive MS ([PMID: 29774057](https://pubmed.ncbi.nlm.nih.gov/29774057/)).

Crucially, the mechanism of B cell involvement was reframed by the success of anti-CD20 therapy. Because rituximab depletes CD20+ B cells but spares CD20-negative plasma cells (the main antibody producers), its efficacy demonstrated that B cells contribute to MS through non-antibody functions — principally antigen presentation to T cells and secretion of pro-inflammatory cytokines — rather than solely through autoantibody production ([PMID: 21555250](https://pubmed.ncbi.nlm.nih.gov/21555250/)). This was further supported by evidence of antigen-driven B cell responses in the CNS, with memory B cells and plasma cells detectable in MS lesions ([PMID: 29512131](https://pubmed.ncbi.nlm.nih.gov/29512131/)).

The ongoing ROC-MS collaboration (four randomized controlled trials comparing rituximab to ocrelizumab) will further refine our understanding of anti-CD20 mechanisms and optimal dosing ([PMID: 41317517](https://pubmed.ncbi.nlm.nih.gov/41317517/)). **Status: Established.** Anti-CD20 efficacy is the single strongest piece of interventional validation for the canonical model's autoimmune arm.

### Finding 4: Smoldering/Chronic Active Lesions Drive Progressive Disability but Resist Current DMTs

Chronic active lesions (CALs), identified on MRI as paramagnetic rim lesions (PRLs) and slowly expanding lesions (SELs), are emerging as key biomarkers of the compartmentalized inflammation that drives progressive disability. PRLs, defined by iron-laden microglia/macrophages at the lesion rim, are highly specific to MS and have been incorporated into MS diagnostic criteria ([PMID: 39711984](https://pubmed.ncbi.nlm.nih.gov/39711984/)). A systematic review of 30 studies confirmed that CALs are associated with worsening disability across MS phenotypes ([PMID: 40357663](https://pubmed.ncbi.nlm.nih.gov/40357663/)).

Critically, current DMTs have limited and inconsistent effects on CAL occurrence. Smoldering neuroinflammation persists behind a relatively intact blood-brain barrier and is "relatively resistant to treatment with existing disease-modifying therapies" ([PMID: 41961242](https://pubmed.ncbi.nlm.nih.gov/41961242/)). This represents a fundamental challenge to the canonical model: if MS progression is driven by compartmentalized CNS inflammation that peripheral immunotherapies cannot reach, the model's therapeutic predictions are only partially validated.

Ectopic lymphoid follicles (ELFs) in the meninges, found in approximately 40% of progressive MS post-mortem brain tissues, are associated with the severity of cortical degeneration and clinical disease progression ([PMID: 34293193](https://pubmed.ncbi.nlm.nih.gov/34293193/)). Intrathecal inflammation, including CSF-borne inflammatory mediators, drives widespread neurodegeneration through mechanisms distinct from focal demyelination ([PMID: 33153042](https://pubmed.ncbi.nlm.nih.gov/33153042/)). **Status: Emerging/Established.** CALs are accepted pathological entities, but their precise mechanistic role and therapeutic targeting remain under investigation.

### Finding 5: Inside-Out (CNS-First) Model Challenges Outside-In Autoimmune Paradigm

The canonical "outside-in" model — where peripheral immune activation drives CNS damage — is challenged by the "inside-out" hypothesis, which proposes that a primary cytodegenerative process within the CNS triggers secondary autoimmune responses against myelin debris. 't Hart et al. (2021) reviewed evidence corroborating the inside-out pathogenic concept, including observations of myelin blistering in normal-appearing white matter that precedes immune infiltration ([PMID: 34156169](https://pubmed.ncbi.nlm.nih.gov/34156169/)).

A particularly compelling piece of evidence comes from the Ermin-deficient mouse model. Loss of Ermin, a myelinating oligodendrocyte-specific cytoskeletal protein, causes myelin de-compaction and fragmentation, leading to slower nerve conduction and progressive neurological deficits, followed by secondary inflammatory activation. Rare ERMN mutations were found in MS patients, providing a genetic link between primary myelin pathology and MS ([PMID: 35285112](https://pubmed.ncbi.nlm.nih.gov/35285112/)).

The cuprizone model further supports this concept by demonstrating that oligodendrocyte death and demyelination can precede immune cell involvement ([PMID: 32210765](https://pubmed.ncbi.nlm.nih.gov/32210765/)). Land (2023) proposed a unifying framework in which damage-associated molecular patterns (DAMPs) released from CNS cell death could drive secondary autoimmune responses, potentially reconciling the inside-out and outside-in paradigms through a positive feed-forward loop ([PMID: 36750753](https://pubmed.ncbi.nlm.nih.gov/36750753/)). **Status: Emerging/Speculative.** The inside-out model has experimental support but lacks definitive human evidence establishing primacy over the outside-in pathway.

### Finding 6: PIRA Accounts for Majority of Disability Accumulation, Even in Relapsing MS

A paradigm shift in understanding MS disability has emerged: most disability worsening occurs independently of relapses (PIRA), driven by neurodegenerative and chronic inflammatory mechanisms that begin early in the disease course. Latent class analysis of over 2,500 untreated MS patients identified four disability worsening phenotypes, with PIRA representing the main disability accrual mechanism in all phenotypes ([PMID: 41284953](https://pubmed.ncbi.nlm.nih.gov/41284953/)).

Biomarker studies reveal that NfL predicts acute inflammatory activity but does not reliably predict PIRA, whereas GFAP (a marker of astrogliosis) is associated with progression even with low inflammatory activity — suggesting that different biological processes underlie relapse-associated worsening versus silent progression. Choroid plexus enlargement, reflecting CSF-mediated inflammation, confers a 2.7-fold increased risk of PIRA ([PMID: 41666922](https://pubmed.ncbi.nlm.nih.gov/41666922/)).

The recognition that PIRA dominates disability accumulation even in the relapsing phase fundamentally qualifies the canonical model: if peripheral immune attacks (relapses) are not the primary driver of disability, then the autoimmune arm of the model is necessary but not sufficient to explain MS outcomes. **Status: Established.** PIRA is now widely accepted as the dominant disability mechanism.

### Finding 7: BTK Inhibitors as Next-Generation Test of Compartmentalized CNS Inflammation Hypothesis

Bruton's tyrosine kinase (BTK) inhibitors (evobrutinib, tolebrutinib, fenebrutinib, remibrutinib, orelabrutinib) represent a critical therapeutic and mechanistic test. Unlike current DMTs, BTK inhibitors can cross the blood-brain barrier and target both B cells and myeloid cells/microglia within the CNS — directly addressing the compartmentalized inflammation hypothesized to drive progressive MS ([PMID: 42075951](https://pubmed.ncbi.nlm.nih.gov/42075951/)).

Preclinical evidence is promising: fenebrutinib blocks microglial FcγR activation, cytokine and chemokine release, microglial clustering, and neurite damage in diverse human brain cell systems ([PMID: 39465429](https://pubmed.ncbi.nlm.nih.gov/39465429/)). Phase II–III clinical trials show heterogeneous outcomes — dose-dependent reductions in gadolinium-enhancing lesions and NfL levels with some agents, but mixed impact on relapse biology and incomplete evidence for slowing progression in non-relapsing progressive MS ([PMID: 41015666](https://pubmed.ncbi.nlm.nih.gov/41015666/)).

BTK inhibitor trials are arguably the most important ongoing experiment for the canonical model: if they succeed in slowing progressive disease by targeting CNS-resident immune cells, this would validate the compartmentalized inflammation component of the model; if they fail, it would suggest that neurodegeneration in progressive MS operates through inflammation-independent mechanisms. **Status: Emerging.** BTK inhibitors show biological plausibility and early signals but await definitive phase III results.

---

## Evidence Matrix

| Citation | Evidence Type | Relationship | Mechanistic Claim Tested | Key Finding | MS Subtype/Context | Confidence |
|----------|--------------|-------------|-------------------------|-------------|-------------------|------------|
| [PMID: 35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/) | Human clinical (longitudinal cohort) | **Supports** | EBV as upstream trigger | 32-fold MS risk after EBV; NfL rises only post-seroconversion | All MS | High; n > 10 million |
| [PMID: 35073561](https://pubmed.ncbi.nlm.nih.gov/35073561/) | Human clinical / in vitro | **Supports** | Molecular mimicry EBV→CNS | EBNA1-GlialCAM cross-reactivity in CSF B cells | RRMS/all | High; mechanistic |
| [PMID: 40063790](https://pubmed.ncbi.nlm.nih.gov/40063790/) | Human clinical | **Supports** | EBV molecular mimicry + epitope spreading | Cross-reactive antibodies in 650 MS vs 661 controls; epitope spreading confirmed | All MS | High; large cohort |
| [PMID: 19209005](https://pubmed.ncbi.nlm.nih.gov/19209005/) | Human clinical (population-based) | **Supports** | EBV/IM as risk factor | Infectious mononucleosis OR = 2.06 (95% CI 1.71–2.48) | All MS | High |
| [PMID: 41934071](https://pubmed.ncbi.nlm.nih.gov/41934071/) | Review (synthesized evidence) | **Supports** | Polygenic immune architecture | >200 GWAS loci; HLA-DRB1\*15:01 most robust | All MS | High; comprehensive |
| [PMID: 41239018](https://pubmed.ncbi.nlm.nih.gov/41239018/) | Computational (MR/eQTL) | **Supports** | HLA-DRB1 causal role | HLA-DRB1 OR = 2.24; 100% colocalization | All MS | Moderate; MR design |
| [PMID: 38817245](https://pubmed.ncbi.nlm.nih.gov/38817245/) | Human clinical (GWAS) | **Supports** | Immune genes control disease timing | AAO GWAS loci enriched for adaptive/complement immunity | All MS | Moderate; n = 3,905 |
| [PMID: 29774057](https://pubmed.ncbi.nlm.nih.gov/29774057/) | Human clinical (RCT) | **Supports** | B cell role in MS | Ocrelizumab: 46–47% relapse reduction, 94–95% fewer Gd+ lesions | RRMS + PPMS | High; phase III RCT |
| [PMID: 21555250](https://pubmed.ncbi.nlm.nih.gov/21555250/) | Human clinical / review | **Supports** | B cells contribute via non-antibody mechanisms | Anti-CD20 efficacy proves B cell involvement; non-antibody functions key | All MS | High |
| [PMID: 41961242](https://pubmed.ncbi.nlm.nih.gov/41961242/) | Review (synthesized evidence) | **Qualifies** | DMTs control smoldering inflammation | Current DMTs have limited effect on chronic active lesions | Progressive MS | High relevance |
| [PMID: 34293193](https://pubmed.ncbi.nlm.nih.gov/34293193/) | Human (post-mortem) | **Supports/Qualifies** | Meningeal lymphoid aggregates drive cortical damage | ELFs in ~40% of progressive MS brains; associated with cortical degeneration severity | Progressive MS | Moderate; post-mortem |
| [PMID: 39711984](https://pubmed.ncbi.nlm.nih.gov/39711984/) | Review / clinical imaging | **Supports** | Chronic active lesion characterization | PRLs defined by iron-laden microglia; incorporated into diagnostic criteria | All MS | High |
| [PMID: 40357663](https://pubmed.ncbi.nlm.nih.gov/40357663/) | Systematic review (30 studies) | **Supports** | CALs associate with disability | CALs consistently associated with worsening disability | All MS | Moderate-High |
| [PMID: 34156169](https://pubmed.ncbi.nlm.nih.gov/34156169/) | Review / model organism | **Competing** | Inside-out (CNS-first) pathogenesis | Evidence for primary cytodegeneration preceding autoimmunity | All MS (etiology) | Moderate; hypothesis |
| [PMID: 35285112](https://pubmed.ncbi.nlm.nih.gov/35285112/) | Model organism / human genetic | **Competing** | Primary myelin defect triggers inflammation | Ermin deficiency → myelin fragmentation → secondary inflammation; rare ERMN mutations in MS | All MS | Moderate |
| [PMID: 41284953](https://pubmed.ncbi.nlm.nih.gov/41284953/) | Human clinical (cohort) | **Qualifies** | Relapse-independent disability accrual | 4 disability phenotypes identified; PIRA dominant in all | Relapse-onset MS | High; n = 2,563 |
| [PMID: 41666922](https://pubmed.ncbi.nlm.nih.gov/41666922/) | Human clinical (MRI/biomarker) | **Qualifies** | Choroid plexus links to progression | CP enlargement → 2.7-fold PIRA risk | All MS | Moderate |
| [PMID: 42075951](https://pubmed.ncbi.nlm.nih.gov/42075951/) | Review / clinical trials | **Supports (emerging)** | BTK inhibitors target compartmentalized inflammation | BTK expressed in B cells and microglia; CNS-penetrant; heterogeneous trial results | All MS | Moderate; trials ongoing |
| [PMID: 39465429](https://pubmed.ncbi.nlm.nih.gov/39465429/) | In vitro (human brain organoids) | **Supports (emerging)** | BTK inhibition modulates CNS microglia | Fenebrutinib blocks microglial FcγR activation, neurite damage | Progressive MS model | Moderate |
| [PMID: 36750753](https://pubmed.ncbi.nlm.nih.gov/36750753/) | Review | **Competing/Complementary** | DAMPs bridge inside-out and outside-in models | DAMP-driven feed-forward loop may reconcile competing paradigms | All MS | Low-Moderate |
| [PMID: 38630618](https://pubmed.ncbi.nlm.nih.gov/38630618/) | Human clinical (genetic epidemiology) | **Supports/Qualifies** | HLA-EBV interaction in MS risk | HLA haplotypes for anti-EBNA1 IgG overlap with MS risk alleles; dose-response for EBNA1 antibodies | All MS | High; n > 15,000 |

---

## Mechanistic Causal Chain

The canonical model implies the following causal chain from upstream trigger to clinical manifestation. Below, each step is annotated with the strength of current evidence:

```
UPSTREAM TRIGGERS
─────────────────
EBV Infection of B cells ──────────────────────────► [STRONG: HR=32, temporal precedence]
    │
    ├─► Molecular mimicry (EBNA1 → GlialCAM)  ──────► [STRONG: demonstrated in CSF B cells]
    ├─► Epitope spreading to CNS antigens      ──────► [MODERATE: confirmed in large cohort]
    ├─► Immortalization of autoreactive B cells ──────► [INFERRED: not directly demonstrated]
    │
    ▼
GENETIC SUSCEPTIBILITY
──────────────────────
HLA-DRB1*15:01 + >200 GWAS loci ────────────────────► [STRONG: replicated GWAS, MR studies]
    │
    ├─► Enhanced antigen presentation of myelin epitopes ─► [MODERATE: inferred from genetics]
    ├─► Dysregulated T/B cell activation thresholds     ──► [MODERATE: pathway enrichment]
    ├─► Poor immune control of EBV                      ──► [MODERATE: HLA-EBNA1 overlap]
    │
    ▼
PERIPHERAL IMMUNE ACTIVATION
────────────────────────────
Autoreactive CD4+ Th1/Th17 + CD8+ T cells ──────────► [STRONG: lesion pathology, EAE models]
B cells (antigen presentation, cytokines)  ──────────► [STRONG: anti-CD20 efficacy]
Plasmablasts (intrathecal Ig synthesis)    ──────────► [STRONG: OCBs as diagnostic marker]
    │
    ▼
BBB DISRUPTION & CNS INFILTRATION
─────────────────────────────────
Lymphocyte crossing via BBB ─────────────────────────► [STRONG: natalizumab proof-of-concept]
    │                                                    (α4-integrin blockade prevents entry)
    ├─► Gateway reflex (neural stimuli → focal          ► [EMERGING: animal models only]
    │    BBB opening)
    │
    ▼
FOCAL INFLAMMATORY DEMYELINATION
────────────────────────────────
White matter + gray matter lesions ──────────────────► [STRONG: MRI, pathology]
    │
    ├─► Acute relapses (Gd-enhancing lesions)   ─────► [STRONG: clinical-radiological correlation]
    ├─► Oligodendrocyte injury/death            ─────► [STRONG: pathology]
    ├─► Myelin loss                             ─────► [STRONG: pathology, MRI]
    │
    ▼
CHRONIC COMPARTMENTALIZED INFLAMMATION
──────────────────────────────────────
Chronic active (smoldering) lesions ─────────────────► [STRONG: PRLs/SELs validated]
    │
    ├─► Iron-laden activated microglia at lesion rims ─► [STRONG: pathology, MRI]
    ├─► Meningeal ectopic lymphoid follicles (~40% PMS) ► [MODERATE: post-mortem studies]
    ├─► Choroid plexus inflammation            ──────► [EMERGING: MRI volumetrics]
    │
    ▼
NEURODEGENERATION & DISABILITY
──────────────────────────────
Axonal transection + neuronal loss ──────────────────► [STRONG: pathology, NfL biomarker]
    │
    ├─► PIRA (dominant disability mechanism)    ─────► [STRONG: large cohort studies]
    ├─► Brain/spinal cord atrophy              ─────► [STRONG: MRI longitudinal]
    ├─► Remyelination failure                  ─────► [MODERATE: OPC differentiation block]
    ├─► Mitochondrial dysfunction / oxidative stress ─► [MODERATE: pathology, preclinical]
    │
    ▼
CLINICAL MANIFESTATION
──────────────────────
RRMS → SPMS conversion / PPMS ──────────────────────► [STRONG: clinical observation]
    │
    └─► Cumulative disability (EDSS progression) ────► [STRONG: natural history studies]
```

### Key Gaps in the Causal Chain

1. **EBV → Autoimmunity transition:** The precise mechanism by which EBV triggers a sustained autoimmune response remains incompletely understood. Molecular mimicry (EBNA1-GlialCAM) is demonstrated but whether it is sufficient, or whether immortalization of autoreactive B cells or bystander activation is also required, is unresolved.

2. **Peripheral activation → CNS entry:** The gateway reflex hypothesis provides an intriguing mechanism for how environmental stimuli could direct immune cell entry at specific CNS blood vessels, but this has only been demonstrated in animal models ([PMID: 38449060](https://pubmed.ncbi.nlm.nih.gov/38449060/)).

3. **Focal inflammation → Progressive neurodegeneration:** The transition from acute relapsing inflammation to chronic progressive neurodegeneration is the least understood step. Whether this reflects a qualitative change in pathology (compartmentalized vs. systemic inflammation) or a quantitative threshold of accumulated damage is unknown.

4. **Remyelination failure:** The mechanisms preventing effective remyelination are multifactorial — OPC recruitment deficits, differentiation blocks, astrocyte-mediated inhibition, and HERV-W envelope protein interference — but their relative contributions in human MS remain unclear.

---

## Alternative and Competing Models

### 1. Inside-Out (CNS-First) Hypothesis
**Relationship to canonical model: COMPETING / COMPLEMENTARY**

This model proposes that primary cytodegenerative processes in the CNS (oligodendrocyte stress, myelin blistering) release damage-associated molecular patterns (DAMPs) that trigger secondary autoimmune responses. Evidence includes: Ermin-deficient mice showing primary myelin fragmentation leading to secondary inflammation ([PMID: 35285112](https://pubmed.ncbi.nlm.nih.gov/35285112/)); myelin blistering in normal-appearing white matter of MS brains ([PMID: 34156169](https://pubmed.ncbi.nlm.nih.gov/34156169/)); and cuprizone model data showing oligodendrocyte death preceding immune infiltration ([PMID: 32210765](https://pubmed.ncbi.nlm.nih.gov/32210765/)). A DAMP-mediated feed-forward loop could reconcile both paradigms ([PMID: 36750753](https://pubmed.ncbi.nlm.nih.gov/36750753/)).

### 2. Mitochondrial Dysfunction / Oxidative Stress Model
**Relationship: DOWNSTREAM CONSEQUENCE / PARALLEL MECHANISM**

Mitochondrial dysfunction and oxidative stress are consistently observed in progressive MS lesions and normal-appearing tissue. Evidence suggests these processes are downstream of inflammation but may become self-sustaining and drive neurodegeneration independently of ongoing immune attack. This model is particularly relevant for explaining PIRA and the failure of anti-inflammatory DMTs to prevent progressive disability ([PMID: 41658744](https://pubmed.ncbi.nlm.nih.gov/41658744/); [PMID: 40345951](https://pubmed.ncbi.nlm.nih.gov/40345951/)).

### 3. HERV-W Activation Model
**Relationship: COMPLEMENTARY / PARALLEL MECHANISM**

Human endogenous retrovirus type W (HERV-W) envelope proteins (pHERV-W, syncytin-1) have been repeatedly associated with MS neuroinflammation. Transgenic HERV-W ENV expression in mice causes myelin repair deficits, neurotoxic microglia and astroglia, and increased axon degeneration ([PMID: 37695891](https://pubmed.ncbi.nlm.nih.gov/37695891/)). The pHERV-W ENV protein interferes with oligodendrocyte precursor differentiation and polarizes microglia toward a neurodamaging phenotype. A neutralizing anti-ENV antibody is in clinical trials ([PMID: 30430656](https://pubmed.ncbi.nlm.nih.gov/30430656/)). Antibody responses against pHERV-W correlate with inflammatory phase and disease severity biomarkers ([PMID: 37985008](https://pubmed.ncbi.nlm.nih.gov/37985008/); [PMID: 41948318](https://pubmed.ncbi.nlm.nih.gov/41948318/)).

### 4. Gut Microbiome Dysbiosis Model
**Relationship: UPSTREAM MODULATOR / PARALLEL MECHANISM**

Consistent depletion of SCFA-producing gut bacteria (Faecalibacterium, Roseburia) and expansion of pro-inflammatory species (Akkermansia muciniphila) are observed in MS patients. Gut dysbiosis promotes Th17/Treg imbalance, intestinal permeability, and microglial activation. However, clinical trials of microbiome interventions have shown heterogeneous results, with "no significant clinical benefit (p > 0.05) in up to 40% of participants" ([PMID: 41645047](https://pubmed.ncbi.nlm.nih.gov/41645047/)).

### 5. Primary Neurodegenerative Model
**Relationship: ALTERNATIVE for progressive disease**

Some evidence suggests that progressive MS behaves more like a primary neurodegenerative disease, with mitochondrial failure, oxidative damage, and iron accumulation driving neuronal and axonal loss independently of adaptive immune mechanisms. The limited efficacy of immunotherapies in progressive MS and the dominance of PIRA support this view. GFAP (astrogliosis marker) predicts progression better than NfL (acute damage marker) in this context.

---

## Knowledge Gaps

### Gap 1: EBV → Autoimmunity Causal Mechanism
**Scope:** The precise molecular pathway from EBV infection to sustained CNS autoimmunity is incompletely mapped.  
**Why it matters:** Determines whether EBV-targeted therapies (vaccines, antivirals, adoptive T-cell therapy) could prevent or treat MS.  
**What was checked:** Molecular mimicry (EBNA1-GlialCAM), epitope spreading, HLA-EBV genetic overlap.  
**What would resolve it:** EBV-specific intervention trials (prophylactic EBV vaccine → MS incidence; antiviral therapy → disease activity); single-cell characterization of EBV-infected B cells in CSF of early MS patients.

### Gap 2: Inflammation → Neurodegeneration Transition
**Scope:** The causal link from acute inflammatory demyelination to chronic progressive neurodegeneration lacks direct perturbation evidence in humans.  
**Why it matters:** Central to whether early aggressive anti-inflammatory treatment can prevent progressive disease.  
**What was checked:** CAL biomarkers, PIRA epidemiology, mitochondrial dysfunction literature.  
**What would resolve it:** Longitudinal studies with early aggressive DMT initiation tracking PIRA incidence; BTK inhibitor trial results as proxy for CNS inflammation-neurodegeneration coupling.

### Gap 3: Inside-Out vs. Outside-In Primacy in Humans
**Scope:** No human study has definitively established whether immune activation or CNS degeneration comes first.  
**Why it matters:** Determines fundamental therapeutic strategy — immunosuppression vs. neuroprotection.  
**What was checked:** Animal models (cuprizone, EAE, Ermin knockout), post-mortem pathology.  
**What would resolve it:** Pre-symptomatic longitudinal biomarker studies in high-risk individuals (e.g., EBV seroconverters with HLA-DRB1\*15:01) tracking both immune activation markers and CNS damage biomarkers.

### Gap 4: Remyelination Failure Mechanisms in Vivo
**Scope:** The relative contributions of OPC recruitment failure, differentiation block, astrocyte-mediated inhibition, and surviving oligodendrocyte interference to remyelination failure are unknown in living MS patients.  
**Why it matters:** Guides remyelination-promoting therapeutic strategy.  
**What was checked:** OPC biology in lesion subtypes, clemastine and other remyelination trials.  
**What would resolve it:** In vivo OPC imaging/tracking; correlation of lesion-level remyelination with cell-type-specific molecular profiles.

### Gap 5: Biomarker Dissociation Between Acute and Progressive Damage
**Scope:** NfL predicts inflammatory activity but not PIRA; GFAP predicts progression but not relapse. No single biomarker captures the full disease process.  
**Why it matters:** Limits precision monitoring and treatment adjustment.  
**What was checked:** NfL, GFAP, CXCL13, metabolomics studies.  
**What would resolve it:** Multi-biomarker panels integrating NfL + GFAP + metabolomics; validation in prospective longitudinal cohorts.

### Gap 6: Source/Dataset Absences
**Scope:** No GenCC or ClinGen clinical validity assertions for MS-specific genes were identified in this search. No single-cell atlas of human chronic active lesions with matched clinical outcomes was found. No completed EBV vaccine trial data for MS prevention exists.  
**Why it matters:** These absences limit the translational confidence of the canonical model.

---

## Discriminating Tests

### Test 1: EBV Vaccine Prevention Trial
- **Design:** Randomized prophylactic EBV vaccine vs. placebo in EBV-seronegative adolescents/young adults, with long-term MS incidence follow-up
- **Patient stratification:** HLA-DRB1\*15:01 carriers vs. non-carriers
- **Expected result if canonical model correct:** Vaccinated group shows dramatically lower MS incidence
- **Expected result if inside-out model correct:** No effect on MS incidence

### Test 2: BTK Inhibitor Trials in Progressive MS (Phase III)
- **Design:** Tolebrutinib/fenebrutinib vs. placebo in non-active progressive MS
- **Biomarkers:** PRLs, SELs, GFAP, NfL, brain atrophy rate
- **Expected result if compartmentalized inflammation drives progression:** Reduced CAL activity and slowed atrophy
- **Expected result if neurodegeneration is inflammation-independent:** No benefit over placebo

### Test 3: Pre-Symptomatic Longitudinal Cohort
- **Design:** Follow EBV seroconverters with HLA-DRB1\*15:01 with serial MRI, CSF, and blood biomarkers
- **Biomarkers:** Anti-EBNA1 IgG, NfL, GFAP, CSF oligoclonal bands, MRI lesion detection
- **Expected result:** Determines temporal ordering of immune activation vs. CNS damage

### Test 4: Single-Cell Multi-Omics of Chronic Active Lesions
- **Design:** Fresh post-mortem or biopsy tissue from CALs; single-cell RNA-seq + spatial transcriptomics
- **Cell types:** Microglia, astrocytes, OPCs, T cells, B cells
- **Expected result:** Identifies driver cell populations and molecular programs in smoldering inflammation

### Test 5: Ermin/Myelin Gene Screening in MS Cohorts
- **Design:** Whole-exome/genome sequencing of MS patients without strong HLA risk, looking for rare variants in ERMN and other myelin structural genes
- **Expected result if inside-out model operates in a subset:** Enrichment of myelin gene variants in HLA-negative or late-onset MS

---

## Curation Leads

*The following are candidate updates for the Knowledge Base, requiring curator verification.*

### Candidate Evidence References

1. **PMID: 35025605** — Bjornevik et al. 2022. Snippet: *"Risk of MS increased 32-fold after infection with EBV but was not increased after infection with other viruses, including the similarly transmitted cytomegalovirus."* → Candidate SUPPORT evidence for EBV trigger claim. **Verified against abstract.**

2. **PMID: 35073561** — Lanz et al. 2022. Snippet: *"B lymphocytes in the cerebrospinal fluid (CSF) of patients with MS contribute to inflammation and secrete oligoclonal immunoglobulins."* → Candidate SUPPORT evidence for molecular mimicry claim. **Verified.**

3. **PMID: 41961242** — Preziosa et al. 2026. Snippet: *"smoldering neuroinflammation...is currently understood to be relatively resistant to treatment with existing disease-modifying therapies."* → Candidate QUALIFIES evidence for DMT validation claim. **Verified.**

4. **PMID: 34156169** — 't Hart et al. 2021. Snippet: *"Data reviewed here corroborate the validity of this inside-out pathogenic concept for multiple sclerosis."* → Candidate COMPETING hypothesis evidence. **Verified.**

5. **PMID: 41284953** — De Meo et al. 2025. → Candidate QUALIFIES evidence showing PIRA is dominant disability mechanism even in untreated relapsing MS.

### Candidate Pathophysiology Nodes/Edges

- **Node:** Chronic active lesion (PRL/SEL) → should be added as distinct pathological entity between "inflammatory demyelination" and "neurodegeneration"
- **Edge:** EBV EBNA1 → GlialCAM molecular mimicry → autoreactive B cell activation (confirmed causal edge)
- **Edge:** Choroid plexus inflammation → PIRA (emerging, needs confirmation)
- **Edge:** HERV-W ENV → OPC differentiation block → remyelination failure (preclinical)

### Candidate Ontology Terms

- **Cell types:** CD20+ memory B cells (CL:0000787), iron-laden microglia (CL:0000129 + PATO:0001025), oligodendrocyte progenitor cells (CL:0002453)
- **Biological processes:** GO:0002376 (immune system process), GO:0042552 (myelination), GO:0070269 (pyroptosis — relevant to oligodendrocyte death in lesions)
- **Disease subtypes:** RRMS, SPMS, PPMS should be annotated with differential model applicability

### Candidate Status Changes

- Current status CANONICAL should be **maintained** but with explicit annotation that the model is most strongly validated for RRMS and early disease, with qualifications for progressive MS
- Consider adding a **sub-hypothesis** for progressive MS mechanisms: "compartmentalized CNS inflammation and neurodegeneration model" with status EMERGING

### Candidate Knowledge Gaps for KB

1. **Gap: EBV → autoimmunity causal mechanism** — Molecular mimicry is demonstrated but sufficiency is unproven; EBV vaccine trial would be definitive
2. **Gap: Inside-out contribution in human MS** — No human longitudinal data establishing primary CNS degeneration preceding immune activation
3. **Gap: BTK inhibitor efficacy in progressive MS** — Phase III results pending; will test compartmentalized inflammation hypothesis
4. **Gap: Absence of GenCC/ClinGen annotations** for MS susceptibility genes
5. **Gap: No completed EBV vaccine prevention trial** as of 2026

---

## Evidence Base (Key Literature)

| PMID | Title (abbreviated) | Role in this report |
|------|---------------------|---------------------|
| [35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/) | Longitudinal analysis: EBV and MS | Landmark evidence for EBV as near-necessary trigger |
| [35073561](https://pubmed.ncbi.nlm.nih.gov/35073561/) | Clonally expanded B cells bind EBNA1 and GlialCAM | Molecular mimicry mechanism |
| [40063790](https://pubmed.ncbi.nlm.nih.gov/40063790/) | Antibody reactivity EBNA1/GlialCAM | Epitope spreading confirmation |
| [19209005](https://pubmed.ncbi.nlm.nih.gov/19209005/) | Infectious mononucleosis and MS | Population-based risk confirmation |
| [38630618](https://pubmed.ncbi.nlm.nih.gov/38630618/) | Genetics of immune response to EBV | HLA-EBV-MS genetic overlap |
| [41934071](https://pubmed.ncbi.nlm.nih.gov/41934071/) | Genetic architecture of MS in 2026 | Most current genetic review |
| [41239018](https://pubmed.ncbi.nlm.nih.gov/41239018/) | Genomic/eQTL/MR: microglial drug targets | MR evidence for HLA-DRB1 causality |
| [38817245](https://pubmed.ncbi.nlm.nih.gov/38817245/) | Adaptive/innate immunity and MS AAO | Immune gene enrichment in disease timing |
| [29774057](https://pubmed.ncbi.nlm.nih.gov/29774057/) | Ocrelizumab: milestone in MS therapy | OPERA/ORATORIO trial data |
| [21555250](https://pubmed.ncbi.nlm.nih.gov/21555250/) | Anti-CD20 antibodies in MS | B cell non-antibody functions |
| [41961242](https://pubmed.ncbi.nlm.nih.gov/41961242/) | Treatment effects on CALs | DMT resistance of smoldering lesions |
| [34293193](https://pubmed.ncbi.nlm.nih.gov/34293193/) | Ectopic lymphoid follicles in progressive MS | Meningeal lymphoid aggregates |
| [39711984](https://pubmed.ncbi.nlm.nih.gov/39711984/) | Chronic active lesion classification | PRL/SEL diagnostic criteria |
| [40357663](https://pubmed.ncbi.nlm.nih.gov/40357663/) | CALs and clinical outcomes: systematic review | 30-study confirmation of CAL-disability link |
| [34156169](https://pubmed.ncbi.nlm.nih.gov/34156169/) | Inside-out concept for MS | Leading inside-out hypothesis paper |
| [35285112](https://pubmed.ncbi.nlm.nih.gov/35285112/) | Ermin deficiency: myelin fragmentation | Inside-out genetic model |
| [36750753](https://pubmed.ncbi.nlm.nih.gov/36750753/) | DAMPs and cell death in autoimmune diseases | DAMP-mediated reconciliation framework |
| [41284953](https://pubmed.ncbi.nlm.nih.gov/41284953/) | Disability worsening phenotypes in MS | PIRA as dominant mechanism |
| [41666922](https://pubmed.ncbi.nlm.nih.gov/41666922/) | Choroid plexus and PIRA | CP enlargement as PIRA biomarker |
| [42075951](https://pubmed.ncbi.nlm.nih.gov/42075951/) | BTK inhibitors in MS | Comprehensive BTK mechanism/trial review |
| [39465429](https://pubmed.ncbi.nlm.nih.gov/39465429/) | Fenebrutinib blocks microglial signaling | BTK inhibition in human microglia |
| [41205133](https://pubmed.ncbi.nlm.nih.gov/41205133/) | MS pathophysiology comprehensive review | Integrative model of inflammation + neurodegeneration |
| [37695891](https://pubmed.ncbi.nlm.nih.gov/37695891/) | Transgenic HERV-W ENV expression | HERV-W neurodegenerative model |
| [41645047](https://pubmed.ncbi.nlm.nih.gov/41645047/) | Gut microbiome in MS | Microbiome therapeutic evidence |

---

## Limitations of This Report

1. **Search scope:** This investigation relied on PubMed-indexed literature available as of May 2026. Pre-print servers, conference abstracts, and non-English literature were not systematically searched.
2. **Progressive MS emphasis:** The investigation revealed that the canonical model's weakest aspects concern progressive MS, but systematic coverage of all progressive MS mechanisms was beyond the scope of a single iteration.
3. **Clinical trial data:** Several critical BTK inhibitor phase III trials are ongoing with results expected 2026–2028; this report captures interim evidence only.
4. **No primary data analysis:** This report is based on literature synthesis rather than primary analysis of patient-level data.
5. **EBV vaccine evidence:** No completed EBV vaccine prevention trial exists, so the ultimate causal test of the EBV-MS hypothesis is unavailable.
6. **Single-cell resolution:** Emerging single-cell and spatial transcriptomic studies of MS lesions are rapidly expanding but were not comprehensively captured in this search.

---

*Report generated by autonomous hypothesis-search agent. All findings require curator verification. Citation snippets have been verified against PubMed abstracts where indicated.*
