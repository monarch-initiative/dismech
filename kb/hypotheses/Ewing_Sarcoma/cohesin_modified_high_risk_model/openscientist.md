---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-28T13:31:47.446678'
end_time: '2026-05-28T14:12:55.507949'
duration_seconds: 2468.06
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Ewing Sarcoma
  category: ''
  hypothesis_group_id: cohesin_modified_high_risk_model
  hypothesis_label: STAG2/cohesin-modified high-risk enhancer model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: cohesin_modified_high_risk_model\nhypothesis_label:\
    \ STAG2/cohesin-modified high-risk enhancer model\nstatus: EMERGING\ndescription:\
    \ STAG2 loss modifies the canonical EWS-FLI1 pathograph by altering cohesin architecture\
    \ and\n  selectively amplifying multimeric GGAA enhancer output, creating a high-risk,\
    \ more aggressive transcriptional\n  state.\nevidence:\n- reference: PMID:41950086\n\
    \  reference_title: STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer\
    \ activity promoting Ewing\n    sarcoma aggressiveness.\n  supports: SUPPORT\n\
    \  evidence_source: IN_VITRO\n  snippet: oncogenic transcriptional state in Ewing\
    \ sarcoma.\n  explanation: Supports the STAG2-modified high-risk enhancer model."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 32
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Ewing Sarcoma
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** cohesin_modified_high_risk_model
- **Hypothesis Label:** STAG2/cohesin-modified high-risk enhancer model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cohesin_modified_high_risk_model
hypothesis_label: STAG2/cohesin-modified high-risk enhancer model
status: EMERGING
description: STAG2 loss modifies the canonical EWS-FLI1 pathograph by altering cohesin architecture and
  selectively amplifying multimeric GGAA enhancer output, creating a high-risk, more aggressive transcriptional
  state.
evidence:
- reference: PMID:41950086
  reference_title: STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing
    sarcoma aggressiveness.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: oncogenic transcriptional state in Ewing sarcoma.
  explanation: Supports the STAG2-modified high-risk enhancer model.
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

# STAG2/Cohesin-Modified High-Risk Enhancer Model in Ewing Sarcoma: Hypothesis Evaluation Report

**Hypothesis ID:** `cohesin_modified_high_risk_model`
**Status in KB:** EMERGING
**Report Date:** 2026-05-28
**Investigation:** 5 iterations, 28 primary references, 222 genomic samples, 11 confirmed findings

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — Recommend maintaining EMERGING status**

The STAG2/cohesin-modified high-risk enhancer model posits that STAG2 loss modifies the canonical EWS-FLI1 pathograph by altering cohesin architecture and selectively amplifying multimeric GGAA enhancer output, creating a high-risk, more aggressive transcriptional state. After systematic evaluation of 28 primary references, 222 genomic samples across two major datasets, and cross-cancer validation evidence, we find that the core enhancer-redistribution claim is well-supported by two independent multiomics studies, and the clinical prognostic association is confirmed in Western cohorts. However, the model is incomplete in three critical respects: (1) STAG2 loss simultaneously disrupts PRC2-mediated gene silencing and CTCF-dependent chromatin contacts through mechanisms partially independent of EWS-FLI1, meaning the hypothesis captures only one arm of a multi-mechanism phenotype; (2) the prognostic impact varies by population, with a Japanese cohort showing no significant survival difference; and (3) all enhancer-level data derive from cell lines rather than primary tumors, and no STAG2-stratified clinical trials or formal gene-disease database annotations exist.

The most important caveat is that the hypothesis, as stated, focuses narrowly on enhancer amplification while the evidence points to a more complex, multi-layered chromatin reprogramming event. The enhancer model captures the most distinctive and mechanistically novel component, but likely explains only part of the aggressive phenotype. Upgrade to SUPPORTED should require: (1) primary tumor chromatin validation, (2) mechanism dissection separating enhancer from PRC2 contributions, and (3) retrospective or prospective STAG2-stratified therapeutic data.

---

## Summary

The STAG2/cohesin-modified high-risk enhancer model represents one of the most mechanistically detailed hypotheses for a secondary genetic modifier in Ewing sarcoma. Two independent studies — Eyunni et al. (2026, [PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/)) and Giménez-Llorente et al. (2024, [PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/)) — converge on the finding that STAG2 loss selectively redistributes EWS-FLI1 binding from short (1–4) GGAA repeat enhancers to multimeric (≥5 repeat) GGAA microsatellite enhancers, amplifying the oncogenic transcriptional program at these high-output sites. This chromatin reprogramming is accompanied by increased chromatin accessibility and H3K27ac at the amplified sites, consistent with a gain-of-function enhancer phenotype. Clinically, STAG2 protein loss by immunohistochemistry is prognostic in localized Ewing sarcoma in the COG cohort (5-year EFS 54% vs. 75%, P = 0.0034; Shulman et al. 2022, [PMID: 36221002](https://pubmed.ncbi.nlm.nih.gov/36221002/)), and STAG2 mutations are found in 10–17% of cases across multiple genomic studies.

However, several important caveats limit the model's scope. First, STAG2 loss also disrupts PRC2-mediated gene regulation — now validated across Ewing sarcoma, bladder cancer, and Down syndrome–associated leukemia — and alters CTCF-dependent chromatin contacts independent of EWS-FLI1 binding. Second, the prognostic significance of STAG2 loss was not replicated in a Japanese cohort (P = 0.663; Kamio et al. 2026, [PMID: 41206913](https://pubmed.ncbi.nlm.nih.gov/41206913/)), where CDKN2A/CDKN2B deletions were prognostic instead. Third, the mechanism by which STAG2 loss increases EWS-FLI1 protein abundance — a key observation from Eyunni et al. — remains entirely unknown. Fourth, no STAG2-stratified clinical trials exist, and no formal gene-disease database annotations have been curated for somatic STAG2 in any cancer.

These findings support maintaining the hypothesis at EMERGING status while prioritizing primary tumor chromatin validation, STAG2-stratified retrospective analyses of PARP inhibitor trials, and mechanistic dissection of the multi-arm chromatin disruption.

---

## Key Findings

### Finding 1: STAG2 Loss Selectively Amplifies Multimeric GGAA Enhancer Output

The core mechanistic claim of the hypothesis is directly supported by two independent studies using complementary approaches. Eyunni et al. (2026; [PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/)) demonstrated that *"STAG2 loss eliminates over 40% of EWS-FLI1 binding sites, predominantly at enhancers containing short (1-4) GGAA repeats, while concurrently increasing binding at multimeric enhancers with ≥5 GGAA-repeat motifs."* The reprogrammed sites showed increased chromatin accessibility and H3K27ac, consistent with enhanced transcriptional output. Independently, Giménez-Llorente et al. (2024; [PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/)) used Capture Hi-C to show that *"cohesin-STAG2 facilitates communication between EWS::FLI1-bound long GGAA repeats, presumably acting as neoenhancers, and their target promoters."* They further identified a STAG2-dependent gene signature associated with worse prognosis.

The convergence of these two studies — one focused on binding redistribution, the other on 3D chromatin contact changes — provides robust, complementary evidence for the enhancer amplification arm of the hypothesis. The key limitation is that both studies used Ewing sarcoma cell lines; primary tumor validation remains absent.

{{figure:evidence_synthesis.png|caption=Comprehensive evidence synthesis showing the causal chain from STAG2 loss to aggressive phenotype, with evidence strength at each link}}

### Finding 2: STAG2 Protein Loss Is Clinically Prognostic in Localized Ewing Sarcoma

The clinical arm of the hypothesis is supported by the largest prospective immunohistochemistry study to date. Shulman et al. (2022; [PMID: 36221002](https://pubmed.ncbi.nlm.nih.gov/36221002/)) analyzed the COG cohort (N = 135 with definitive IHC) and found *"5-year event-free survival was 54% (95% CI 34-70%) and 75% (95% CI 63-84%) for patients with STAG2 loss vs. expression (P = 0.0034)"* in localized disease. STAG2 was lost in 29/108 (27%) localized cases by IHC — a higher rate than the ~15% mutation frequency, consistent with non-genetic mechanisms of STAG2 inactivation reported by Crompton et al. (2014; [PMID: 25186949](https://pubmed.ncbi.nlm.nih.gov/25186949/)). Tirode et al. (2014; [PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/)) found STAG2 mutated in 17% of 112 WGS cases, with *"STAG2 and TP53 mutations [being] often concurrent and associated with poor outcome."*

Critically, however, Kamio et al. (2026; [PMID: 41206913](https://pubmed.ncbi.nlm.nih.gov/41206913/)) found only 3.7% STAG2 mutations in a Japanese cohort with no significant survival difference (P = 0.663), while CDKN2A and CDKN2B deletions were prognostic (P = 0.024 and P = 0.012). This population-level discrepancy may reflect differences in GGAA microsatellite architecture between ethnic groups — African and Asian populations have shorter GGAA repeats at key loci (Beck et al. 2012, [PMID: 22749036](https://pubmed.ncbi.nlm.nih.gov/22749036/)), which could reduce the substrate for STAG2-loss-mediated enhancer amplification.

### Finding 3: STAG2 Loss Operates Through Dual Mechanisms — EWS-FLI1-Dependent AND -Independent

The hypothesis as stated focuses on the enhancer amplification mechanism, but the evidence reveals a more complex picture. Adane et al. (2021; [PMID: 34129824](https://pubmed.ncbi.nlm.nih.gov/34129824/)) showed that STAG2 loss both perturbs the EWS-FLI1 oncogenic program via altered enhancer-promoter contacts AND disrupts PRC2-mediated regulation of gene expression. They found that *"loss of STAG2 also disrupted PRC2-mediated regulation of gene expression. Combined, these transcriptional changes converged to modulate EWS/FLI1, migratory, and neurodevelopmental programs."* STAG2 loss enhanced metastatic potential in xenografts. Giménez-Llorente et al. (2024; [PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/)) independently identified *"changes in CTCF-dependent chromatin contacts involving signature genes, unrelated to EWS::FLI1 binding."*

This dual-mechanism finding qualifies the seed hypothesis: the enhancer amplification model is real but represents only one arm of STAG2's contribution to aggressiveness. The PRC2 arm and the CTCF-dependent arm likely contribute independently to the clinical phenotype.

### Finding 4: STAG1 Cannot Compensate for STAG2 at Enhancer Regions, Creating Therapeutic Vulnerability

A critical mechanistic underpinning of the hypothesis is the non-interchangeability of cohesin variants. Kojic et al. (2018; [PMID: 29867216](https://pubmed.ncbi.nlm.nih.gov/29867216/)) established that *"a distinct population of the SA2-containing cohesin complexes... localize to enhancers lacking CTCF, are linked to tissue-specific transcription and cannot be replaced by the SA1-containing cohesin complex."* This was confirmed in Ewing sarcoma by Giménez-Llorente et al. (*"STAG1 is unable to compensate for STAG2 loss and chromatin-bound cohesin is severely decreased"*) and Adane et al. (compensatory increase in cohesin-STAG1 at non-enhancer regions but NOT at enhancer-rich regions).

This non-compensation creates a therapeutic vulnerability: STAG1 is synthetic lethal with STAG2 loss, as demonstrated by multiple groups (van der Lelij et al. 2020, [PMID: 32467316](https://pubmed.ncbi.nlm.nih.gov/32467316/); Liu et al. 2018, [PMID: 29649003](https://pubmed.ncbi.nlm.nih.gov/29649003/); Benedetti et al. 2017, [PMID: 28430577](https://pubmed.ncbi.nlm.nih.gov/28430577/)). Additionally, STAG2 loss impairs replication fork progression, creating synthetic lethality with PARP and ATR inhibitors (Bailey et al. 2019, [PMID: 30975996](https://pubmed.ncbi.nlm.nih.gov/30975996/)).

### Finding 5: STAG2 and CDKN2A Define Parallel, Mutually Exclusive High-Risk Pathways

Tirode et al. (2014; [PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/)) discovered that *"STAG2 mutations and CDKN2A deletions were mutually exclusive, as confirmed in Ewing sarcoma cell lines."* Our cBioPortal analysis of 222 samples across two studies independently confirmed this mutual exclusivity (0 co-mutations for STAG2 + CDKN2A point mutations). STAG2 co-occurs with TP53 instead (31% of STAG2-mutant cases). This defines at least two parallel molecular routes to high-risk Ewing sarcoma: the STAG2/TP53 chromatin-disruption pathway and the CDKN2A/cell-cycle-disruption pathway. Notably, Lerman et al. (2015; [PMID: 25464386](https://pubmed.ncbi.nlm.nih.gov/25464386/)) found TP53/CDKN2A NOT prognostic in a COG localized cohort (P = 0.58), suggesting STAG2 loss carries prognostic weight beyond its TP53 co-mutation.

{{figure:mutation_landscape.png|caption=STAG2 mutation landscape in Ewing sarcoma showing LOF spectrum, co-mutation patterns, and mutual exclusivity with CDKN2A}}

### Finding 6: GGAA Microsatellite Length Polymorphism Modulates the Substrate for STAG2 Effects

The enhancer amplification model predicts that STAG2 loss should have greater impact in tumors with more multimeric GGAA microsatellites. Monument et al. (2014; [PMID: 25093581](https://pubmed.ncbi.nlm.nih.gov/25093581/)) showed *"a complex, bimodal pattern of EWS/FLI-mediated gene expression... across a wide range of GGAA motifs, with maximal expression observed in constructs containing 20-26 GGAA motifs."* Beck et al. (2012; [PMID: 22749036](https://pubmed.ncbi.nlm.nih.gov/22749036/)) demonstrated that NR0B1 GGAA microsatellites are significantly longer in European versus African populations. Johnson et al. (2017; [PMID: 29091716](https://pubmed.ncbi.nlm.nih.gov/29091716/)) identified two distinct classes of GGAA microsatellites (promoter-like and enhancer-like) with length-dependent EWS-FLI1 binding. This population-level variation in GGAA architecture may explain both the 10-fold lower ES incidence in Africans and why STAG2 prognostic impact varies across cohorts.

### Finding 7: Cross-Cancer Validation of the STAG2-PRC2 Connection

The PRC2-disruption arm of STAG2 loss has been validated across three cancer types, upgrading this mechanism from moderate to strong evidence. Suzuki et al. (2026; [PMID: 41949996](https://pubmed.ncbi.nlm.nih.gov/41949996/)) showed that in a Down syndrome–myeloid leukemia model, *"Stag2 loss induced a moderate but significant degree of PRC2-insufficient state in Gata1s progenitors."* Park et al. (2025; [PMID: 41091719](https://pubmed.ncbi.nlm.nih.gov/41091719/)) found that *"inactivation of STAG2 in bladder cancer cells and in bladder epithelial precursor cells resulted in concomitant inactivation of the H3K27me3 Polycomb chromatin mark."* Combined with Adane et al.'s findings in Ewing sarcoma, this establishes a conserved STAG2→PRC2 insufficiency axis across cancer types. Pherson et al. (2017; [PMID: 28782042](https://pubmed.ncbi.nlm.nih.gov/28782042/)) provided mechanistic context showing PRC1 is directly recruited to active genes by cohesin complex.

### Finding 8: EWS-FLI1 Protein Abundance Increase — Mechanism Unknown

Eyunni et al. (2026) reported increased EWS-FLI1 protein abundance upon STAG2 loss, but the mechanism is entirely uncharacterized. The EWS-FLI1 protein turnover pathway is known: it is regulated by the ubiquitin-proteasome system with a half-life of 2–4 hours (Gierisch et al. 2016; [PMID: 27875302](https://pubmed.ncbi.nlm.nih.gov/27875302/)), and USP19 deubiquitinase stabilizes EWS-FLI1 — *"Depletion of USP19 resulted in diminished EWS-FLI1 protein levels and, vice versa, upregulation of active USP19 stabilized the fusion protein"* (Gierisch et al. 2019; [PMID: 30700749](https://pubmed.ncbi.nlm.nih.gov/30700749/)). Lys-380 in the ETS domain is the critical ubiquitin acceptor residue. No study has investigated whether STAG2 loss alters USP19 expression, EWS-FLI1 ubiquitination, or proteasomal degradation rates. This represents a critical knowledge gap because increased EWS-FLI1 protein could independently amplify the enhancer phenotype through a feedforward mechanism.

### Finding 9: cBioPortal Confirms STAG2 LOF Mutation Spectrum and Co-Occurrence Patterns

Analysis of 222 Ewing sarcoma samples across two cBioPortal studies (DFCI N=107, Institut Curie N=115) independently validated key genomic features: STAG2 mutated in 10.3% and 15.7% respectively; 93% of STAG2 mutations are loss-of-function (nonsense 41%, frameshift 41%, splice site 10%); R216* is the most recurrent hotspot (5/29 mutations, 17%); STAG2+TP53 co-mutation confirmed in 9/29 STAG2-mutant cases (31%); and perfect mutual exclusivity between STAG2 and CDKN2A point mutations (0 co-mutations).

### Finding 10: SIX1/EWS-FLI1 Anti-Metastatic Network as Candidate Mechanistic Bridge

Hughes et al. (2023; [PMID: 37468459](https://pubmed.ncbi.nlm.nih.gov/37468459/)) identified SIX1 as a homeoprotein that suppresses ES metastasis. They showed that *"EWS/FLI1 promotes SIX1 protein expression, and that the two proteins share genome-wide binding profiles and transcriptional regulatory targets, including many metastasis-associated genes such as integrins, which they co-regulate."* If STAG2-mediated enhancer reprogramming disrupts SIX1 expression or the SIX1-EWS-FLI1 co-regulatory network, this could provide a direct mechanistic bridge between enhancer amplification and the metastatic phenotype observed clinically. This link is speculative but testable.

### Finding 11: Major Translational and Database Annotation Gaps

No STAG2-stratified clinical trials exist in Ewing sarcoma. PARP inhibitor trials (olaparib NCT01583543; talazoparib NCT02116777) have been completed but none stratified by STAG2 status. Crompton et al. (2014; [PMID: 25186949](https://pubmed.ncbi.nlm.nih.gov/25186949/)) confirmed that *"STAG2 loss... is present in more than 15% of Ewing sarcoma tumors; occurs by point mutation, rearrangement, and likely nongenetic mechanisms; and is associated with disease dissemination."* Yet UniProt annotates STAG2 only for developmental cohesinopathies (MIM:301022, 301043), with no cancer annotation. No GenCC, ClinGen, or ClinVar gene-disease curation exists for somatic STAG2 in any cancer. This represents a significant gap between research evidence and curated knowledge infrastructure.

---

## Mechanistic Causal Chain

The hypothesis implies the following causal chain from upstream trigger to clinical manifestation. Evidence strength is annotated at each step.

```
UPSTREAM TRIGGER
    │
    ▼
[1] STAG2 loss-of-function (mutation ~10-17%, or epigenetic silencing ~27% by IHC)
    │   Evidence: STRONG — Tirode 2014, Shulman 2022, Crompton 2014, cBioPortal
    │   93% truncating mutations; R216* hotspot; multiple mechanisms of inactivation
    │
    ├────────────────────────────────────────────┐
    │                                            │
    ▼                                            ▼
[2a] Cohesin-STAG2 lost at                    [2b] PRC2-mediated silencing
     CTCF-free enhancers                            disrupted (H3K27me3 loss)
    │   Evidence: STRONG                        │   Evidence: STRONG (cross-cancer)
    │   Kojic 2018, Adane 2021,                 │   Adane 2021, Suzuki 2026,
    │   Giménez-Llorente 2024                   │   Park 2025
    │                                            │
    ▼                                            ▼
[3a] EWS-FLI1 redistributed:                  [3b] Derepression of PRC2
     lost from short GGAA repeats                   target genes (migratory,
     gained at multimeric GGAA                      neurodevelopmental programs)
    │   Evidence: STRONG                        │   Evidence: MODERATE
    │   Eyunni 2026                             │   Adane 2021
    │                                            │
    ├──── [3c] CTCF-dependent rewiring ──────────┤
    │     Evidence: MODERATE                     │
    │     Giménez-Llorente 2024                  │
    │                                            │
    ▼                                            │
[4] Amplified enhancer output                   │
    at multimeric microsatellites               │
    (↑ H3K27ac, ↑ accessibility)                │
    │   Evidence: STRONG                        │
    │   Eyunni 2026                             │
    │                                            │
    ├──────────────┬─────────────────────────────┤
    │              │                             │
    ▼              ▼                             ▼
[5a] Oncogenic  [5b] ↑ EWS-FLI1            [5c] Migratory/
     gene            protein                     metastatic
     activation      abundance                   program
    │  STRONG       │  WEAK-MODERATE            │  MODERATE
    │               │  mechanism UNKNOWN         │  Adane 2021
    │               │  Eyunni 2026              │
    │               │                            │
    ▼               ▼                            ▼
[6] ═══════════════════════════════════════════════
    AGGRESSIVE TRANSCRIPTIONAL STATE
    ═══════════════════════════════════════════════
    │
    ▼
[7] Worse clinical outcome (↓ EFS, ↑ metastasis)
    STRONG in Western cohorts (Shulman 2022, P=0.003)
    WEAK in Japanese cohort (Kamio 2026, P=0.663)
```

### Evidence Strength by Causal Link

| Causal Link | Evidence Strength | Key Gap |
|------------|------------------|---------|
| STAG2 loss → cohesin reprogramming | **STRONG** (multiple studies, cross-cancer) | None major |
| Cohesin loss → enhancer redistribution | **STRONG** (ChIP-seq, ATAC-seq, Hi-C) | Cell lines only |
| Enhancer redistribution → transcriptional change | **STRONG** (RNA-seq integration) | Relative contribution vs. PRC2/CTCF unknown |
| STAG2 loss → PRC2 disruption | **STRONG** (3 cancer types) | Conserved; relative contribution unknown |
| Transcriptional change → metastatic phenotype | **MODERATE** (xenograft only) | No patient-matched data |
| Metastatic phenotype → poor outcome | **STRONG** (clinical cohorts) | Population variability |
| STAG2 loss → increased EWS-FLI1 protein | **MODERATE** (one study) | Mechanism completely unknown |

{{figure:final_synthesis_dashboard.png|caption=Final synthesis dashboard integrating evidence dimensions, confidence levels, and knowledge gaps across the STAG2 hypothesis}}

---

## Evidence Matrix

| # | Citation | Year | Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence | Limitations |
|---|----------|------|------|-----------|-------------------|-------------|---------|------------|-------------|
| 1 | [PMID: 41950086](https://pubmed.ncbi.nlm.nih.gov/41950086/) | 2026 | In vitro multiomics | **Supports** | STAG2 loss amplifies multimeric enhancer output | >40% EWS-FLI1 sites lost at short GGAA; gained at ≥5-repeat; ↑H3K27ac | ES cell lines | High | Cell lines only |
| 2 | [PMID: 39487368](https://pubmed.ncbi.nlm.nih.gov/39487368/) | 2024 | In vitro + patient RNA | **Supports/Qualifies** | Cohesin-STAG2 mediates enhancer-promoter contacts | Capture Hi-C: STAG2 enables GGAA–promoter communication; also CTCF-dependent changes | ES cell lines | High | Dual mechanism complicates pure enhancer model |
| 3 | [PMID: 36221002](https://pubmed.ncbi.nlm.nih.gov/36221002/) | 2022 | Human clinical (IHC) | **Supports** | STAG2 loss clinically prognostic | 5-yr EFS 54% vs 75%, P=0.0034, localized ES | COG, N=135 | High | Retrospective; Western cohort |
| 4 | [PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/) | 2014 | Human clinical (WGS) | **Supports** | STAG2 defines aggressive subtype | 17% mutated; STAG2+TP53 = poor outcome; STAG2/CDKN2A mutually exclusive | WGS N=112 | High | Pre-dates enhancer mechanism |
| 5 | [PMID: 41206913](https://pubmed.ncbi.nlm.nih.gov/41206913/) | 2026 | Human clinical (CGP) | **Qualifies** | STAG2 prognostic universality | 3.7% frequency; P=0.663 for survival; CDKN2A prognostic instead | Japanese, N=81 | Moderate | Small STAG2 N; different population |
| 6 | [PMID: 34129824](https://pubmed.ncbi.nlm.nih.gov/34129824/) | 2021 | In vitro + xenograft | **Supports/Qualifies** | STAG2 loss rewires oncogenic programs | Dual: enhancer + PRC2 disruption; ↑ metastatic potential | ES models | High | Qualifies single-mechanism model |
| 7 | [PMID: 29867216](https://pubmed.ncbi.nlm.nih.gov/29867216/) | 2018 | In vitro (ChIP-seq) | **Supports** | STAG1 cannot replace STAG2 at enhancers | Cohesin-SA2 at CTCF-free enhancers non-replaceable | Multiple cell types | High | Not ES-specific |
| 8 | [PMID: 25093581](https://pubmed.ncbi.nlm.nih.gov/25093581/) | 2014 | In vitro + clinical | **Supports** | GGAA length modulates enhancer output | Bimodal expression; max at 20-26 GGAA motifs | ES cell lines, COG | Moderate | Reporter assays |
| 9 | [PMID: 22749036](https://pubmed.ncbi.nlm.nih.gov/22749036/) | 2012 | Population genetics | **Qualifies** | Population variation in GGAA | NR0B1 GGAA longer in Europeans vs Africans | Cross-population | Moderate | Limited loci |
| 10 | [PMID: 41949996](https://pubmed.ncbi.nlm.nih.gov/41949996/) | 2026 | Model organism | **Supports** (cross-cancer) | STAG2 → PRC2 insufficiency | PRC2-insufficient state in Gata1s progenitors | DS-ML model | High | Not ES |
| 11 | [PMID: 41091719](https://pubmed.ncbi.nlm.nih.gov/41091719/) | 2025 | In vitro | **Supports** (cross-cancer) | STAG2 → Polycomb disruption | H3K27me3 loss; attenuated differentiation | Bladder cancer | High | Not ES |
| 12 | [PMID: 25186949](https://pubmed.ncbi.nlm.nih.gov/25186949/) | 2014 | Genomic + clinical | **Supports** | STAG2 loss → dissemination | >15% frequency; multiple mechanisms; disease dissemination | ES genomic landscape | Moderate | Retrospective |
| 13 | [PMID: 30700749](https://pubmed.ncbi.nlm.nih.gov/30700749/) | 2019 | In vitro | **Context** | EWS-FLI1 protein stability | USP19 deubiquitinase regulates EWS-FLI1 | ES cell lines | Moderate | Not linked to STAG2 |
| 14 | [PMID: 27875302](https://pubmed.ncbi.nlm.nih.gov/27875302/) | 2016 | In vitro | **Context** | EWS-FLI1 proteasomal degradation | Half-life 2-4h; Lys-380 ubiquitin acceptor | ES cell lines | High | Not linked to STAG2 |
| 15 | [PMID: 37468459](https://pubmed.ncbi.nlm.nih.gov/37468459/) | 2023 | In vitro + xenograft | **Supports** (indirect) | SIX1 anti-metastatic network | SIX1 co-regulates EWS-FLI1 targets; suppresses metastasis | ES models | Moderate | No direct STAG2 link |
| 16 | [PMID: 41252851](https://pubmed.ncbi.nlm.nih.gov/41252851/) | 2025 | Human clinical | **Competing** | 1q gain as independent marker | 1q gain independently predicts poor EFS (N=305) | PROVABES | High | No STAG2 interaction tested |
| 17 | [PMID: 25464386](https://pubmed.ncbi.nlm.nih.gov/25464386/) | 2015 | Human clinical | **Qualifies** | TP53/CDKN2A prognostic value | TP53/CDKN2A NOT prognostic in localized COG (P=0.58) | COG, N=112 | Moderate | May be underpowered |
| 18 | [PMID: 30975996](https://pubmed.ncbi.nlm.nih.gov/30975996/) | 2019 | In vitro | **Supports** (therapeutic) | STAG2 → replication stress | STAG2 loss = fork stalling; SL with PARP/ATR | Multiple cancers | Moderate | Not ES-specific |
| 19 | [PMID: 28430577](https://pubmed.ncbi.nlm.nih.gov/28430577/) | 2017 | In vitro | **Supports** (therapeutic) | STAG1-STAG2 synthetic lethality | STAG1+STAG2 double loss = cell death | Cancer cell lines | High | Not ES-specific |
| 20 | [PMID: 32467316](https://pubmed.ncbi.nlm.nih.gov/32467316/) | 2020 | In vitro | **Supports** (therapeutic) | STAG1 vulnerability | STAG1 depletion selectively kills STAG2-deficient cells | Cancer models | High | No ES in vivo |
| 21 | [PMID: 29649003](https://pubmed.ncbi.nlm.nih.gov/29649003/) | 2018 | In vitro + in vivo | **Supports** (therapeutic) | SA1 essential lethality | SA1 depletion kills SA2-mutant ES/bladder; synergy with PARPi | ES + bladder | High | Clinical validation absent |
| 22 | [PMID: 31898537](https://pubmed.ncbi.nlm.nih.gov/31898537/) | 2020 | Model organism | **Supports** | Stag2 cooperates with EWS-FLI1 | Synergistic sarcoma production from murine MSCs | Mouse MSC model | Moderate | Required irradiation |
| 23 | [PMID: 28782042](https://pubmed.ncbi.nlm.nih.gov/28782042/) | 2017 | In vitro (Drosophila) | **Supports** (context) | PRC1 recruited by cohesin | PRC1 recruited to active genes by cohesin | Drosophila | Moderate | Not ES |
| 24 | [PMID: 29091716](https://pubmed.ncbi.nlm.nih.gov/29091716/) | 2017 | In vitro + computational | **Supports** (context) | Two GGAA microsatellite classes | Promoter-like and enhancer-like; length-dependent binding | ES cell lines | High | Pre-dates STAG2 link |
| 25 | [PMID: 37069029](https://pubmed.ncbi.nlm.nih.gov/37069029/) | 2023 | Review (GU cancers) | **Context** | STAG2-immune connection | STAG2 among genes associated with adaptive immunity | GU cancers | Low (review) | Not ES-specific |
| 26 | [PMID: 41002248](https://pubmed.ncbi.nlm.nih.gov/41002248/) | 2026 | In vitro (cell lines) | **Supports** (context) | STAG2 in ES cell line panel | STAG2 among most frequent mutations; TP53 = biggest drug sensitivity impact | New ES cell lines | Moderate | Descriptive |
| 27 | [PMID: 33080033](https://pubmed.ncbi.nlm.nih.gov/33080033/) | 2020 | In vitro + xenograft | **Context** | CRC trio and super-enhancers | EWS-FLI1 establishes CRC via super-enhancers; CRC co-occupies 77% promoters | ES models | High | CRC-STAG2 intersection untested |
| 28 | [PMID: 41502392](https://pubmed.ncbi.nlm.nih.gov/41502392/) | 2026 | In vitro + in vivo | **Supports** (therapeutic) | STAG2 + PARP inhibition | SA1 depletion + PARP inhibition = synergistic killing | Brain tumor models | Moderate | Not ES |

---

## Alternative and Competing Models

### 1. CDKN2A/Cell-Cycle Disruption Model
**Relationship to seed hypothesis:** ALTERNATIVE (mutually exclusive pathway)

CDKN2A homozygous deletion (12% of cases) represents a parallel route to aggressive Ewing sarcoma operating through cell-cycle deregulation rather than chromatin remodeling. The mutual exclusivity with STAG2 mutations ([PMID: 25223734](https://pubmed.ncbi.nlm.nih.gov/25223734/)) suggests functional redundancy at the phenotypic level — both achieve aggressive transcriptional states through different mechanisms. Kamio et al. (2026; [PMID: 41206913](https://pubmed.ncbi.nlm.nih.gov/41206913/)) found CDKN2A/B deletions prognostic in a Japanese cohort where STAG2 was not, suggesting population-dependent dominance of one pathway over the other.

### 2. PRC2 Derepression / Developmental Program Model
**Relationship:** COMPLEMENTARY (parallel arm of STAG2 loss)

STAG2 loss disrupts PRC2-mediated silencing of developmental and migratory gene programs. This arm is now validated across three cancer types (ES, DS-ML, bladder cancer). It is partially independent of the enhancer amplification model and may contribute more specifically to the metastatic phenotype.

### 3. Replication Stress / DNA Damage Model
**Relationship:** PARALLEL MECHANISM (non-enhancer effect of STAG2 loss)

STAG2 is essential for replication fork progression; loss causes fork stalling and double-strand breaks ([PMID: 30975996](https://pubmed.ncbi.nlm.nih.gov/30975996/)). This creates synthetic lethality with PARP/ATR inhibitors. It operates through an entirely different mechanism than enhancer amplification and has the most direct therapeutic implications.

### 4. Chromosome 1q Gain / Copy-Number Alteration Burden Model
**Relationship:** INDEPENDENT/COMPETING

Chromosome 1q gain is an independent prognostic marker in localized ES (Díaz-Martín et al. 2025; [PMID: 41252851](https://pubmed.ncbi.nlm.nih.gov/41252851/); PROVABES, N = 305). Higher fraction of genome altered is also prognostic. The relationship between STAG2 loss and copy-number alteration burden has not been characterized — notably, STAG2 loss in bladder cancer does NOT cause aneuploidy ([PMID: 24121791](https://pubmed.ncbi.nlm.nih.gov/24121791/)).

### 5. EWS-FLI1 Activity Level / Phase Separation Model
**Relationship:** UPSTREAM MODIFIER (complementary)

EWS-FLI1 activity exists on a spectrum within tumors ([PMID: 32049009](https://pubmed.ncbi.nlm.nih.gov/32049009/)). STAG2 loss increases EWS-FLI1 protein abundance, which could enhance transcriptional condensate formation at multimeric GGAA sites. This would make phase separation an underlying biophysical mechanism for the observed enhancer amplification — complementary, not competing.

### 6. LSD1/NuRD-Mediated Repression Model
**Relationship:** COMPLEMENTARY

EWS-FLI1 represses genes via NuRD/LSD1 complex ([PMID: 23178492](https://pubmed.ncbi.nlm.nih.gov/23178492/)). Catalytic LSD1 inhibition is therapeutically insufficient ([PMID: 31207107](https://pubmed.ncbi.nlm.nih.gov/31207107/)). The interaction between STAG2 loss and the repressive arm of EWS-FLI1 is unexplored.

{{figure:competing_models.png|caption=Competing and complementary mechanistic models for high-risk biology in Ewing sarcoma}}

---

## Knowledge Gaps

### HIGH PRIORITY

**1. No Primary Tumor Chromatin Validation**
- **Scope:** All enhancer-level evidence derives from cell lines (A673, TC71, etc.).
- **Why it matters:** Cell line chromatin may not recapitulate primary tumor biology; culture conditions can alter enhancer landscapes.
- **What was checked:** PubMed searches for "Ewing sarcoma primary tumor ATAC-seq" and "Ewing sarcoma patient chromatin."
- **Resolution:** ATAC-seq + CUT&Tag for H3K27ac on STAG2-positive vs. STAG2-negative primary tumors from COG tissue bank.

**2. Mechanism of EWS-FLI1 Protein Increase Upon STAG2 Loss**
- **Scope:** Eyunni et al. (2026) observed increased EWS-FLI1 protein; no mechanistic explanation exists.
- **Why it matters:** If STAG2 loss stabilizes EWS-FLI1 protein (e.g., via USP19 upregulation), this would constitute an independent oncogenic mechanism and potential feedforward loop.
- **What was checked:** PubMed for "STAG2 EWS-FLI1 protein stability," "STAG2 USP19," "cohesin protein turnover." No results.
- **Resolution:** Cycloheximide chase, IP-MS for ubiquitination, and USP19 epistasis in isogenic STAG2-WT/KO cells.

**3. Relative Contribution of Enhancer vs. PRC2 vs. CTCF Mechanisms**
- **Scope:** Three chromatin mechanisms coexist; their relative contributions to aggressiveness are unknown.
- **Why it matters:** Therapeutic strategies depend on which arm dominates.
- **What was checked:** No rescue experiments dissecting individual arms published.
- **Resolution:** dCas9-based selective rescue at enhancer vs. PRC2 target vs. CTCF sites in STAG2-null cells.

### MODERATE PRIORITY

**4. No STAG2-Stratified Clinical Trials**
- **Scope:** Zero trials on ClinicalTrials.gov mention STAG2 or cohesin in Ewing sarcoma.
- **Why it matters:** PARP/ATR inhibitors have been tested without STAG2 stratification, potentially missing responder subgroups.
- **Resolution:** Retrospective STAG2 IHC on banked specimens from completed trials (olaparib NCT01583543, talazoparib NCT02116777).

**5. Population-Specific Prognostic Discrepancy**
- **Scope:** STAG2 prognostic in Western but not Japanese cohort.
- **Why it matters:** May restrict the hypothesis's geographic applicability.
- **Resolution:** Genotype GGAA microsatellite lengths in the Japanese cohort; correlate with STAG2 status and outcome.

**6. STAG2 Protein Loss Without Mutations**
- **Scope:** Shulman 2022 found IHC-negative cases without detectable STAG2 mutations.
- **Why it matters:** Non-mutational inactivation broadens the affected population and may be reversible.
- **Resolution:** STAG2 promoter methylation analysis in IHC-negative/mutation-negative tumors.

**7. TP53 Cooperation Mechanism**
- **Scope:** STAG2+TP53 co-mutations produce worst outcomes but mechanistic basis unknown.
- **Resolution:** Chromatin profiling in isogenic STAG2-null, TP53-null, and double-null ES cells.

### SOURCE/DATA ABSENCES

**8. No Gene-Disease Database Annotations**
- UniProt, GenCC, ClinGen, ClinVar have no somatic STAG2–cancer annotation as of search date.

**9. No Single-Cell Chromatin Data**
- No scATAC-seq or single-cell Hi-C in STAG2-stratified ES samples.

**10. STAG2-Immune Microenvironment Connection Unexplored in ES**
- STAG2-immune associations noted in GU cancers ([PMID: 37069029](https://pubmed.ncbi.nlm.nih.gov/37069029/)) but no ES data exist.

**11. SIX1-STAG2 Intersection Untested**
- Whether STAG2 loss disrupts the SIX1/EWS-FLI1 anti-metastatic network is unknown.

**12. CRC-Enhancer Intersection Untested**
- Whether core regulatory circuitry super-enhancers (KLF15/TCF4/NKX2-2) overlap with STAG2-affected GGAA sites is unknown.

**13. Clonal Evolution of Enhancer Landscape at Relapse**
- STAG2-negative cells expand at relapse (Tirode 2014); no paired chromatin data exist.

---

## Discriminating Tests

### Test 1: Primary Tumor Chromatin Profiling (Highest Priority)
- **Design:** ATAC-seq + CUT&Tag (H3K27ac, H3K27me3) on FFPE or fresh-frozen STAG2-positive (N ≥ 15) vs. STAG2-negative (N ≥ 15) primary Ewing sarcoma tumors
- **Patient stratification:** STAG2 by IHC; matched for stage, age, site
- **Expected if hypothesis true:** Increased accessibility and H3K27ac at multimeric GGAA sites in STAG2-negative tumors
- **Expected if false:** No systematic enhancer difference between groups
- **Feasibility:** Moderate; requires COG tissue bank access

### Test 2: EWS-FLI1 Protein Stability Mechanism
- **Design:** Cycloheximide chase + IP-MS in isogenic STAG2-WT vs. STAG2-KO A673 and TC71 cells
- **Perturbation:** USP19 knockdown to test dependence
- **Expected if stability mechanism:** Increased half-life in STAG2-KO; reversed by USP19 KD
- **Alternative:** Protein increase is transcriptional (mRNA-level)

### Test 3: PARP Inhibitor Retrospective Stratification
- **Design:** STAG2 IHC on banked specimens from olaparib (NCT01583543) and talazoparib (NCT02116777) ES trials
- **Expected:** Higher response rate in STAG2-negative subgroup based on replication stress vulnerability

### Test 4: STAG2 × GGAA Genotype Interaction
- **Design:** Long-read sequencing of GGAA microsatellites at top 50 EWS-FLI1-bound loci in Japanese + European cohorts
- **Correlation:** Repeat length × STAG2 status × outcome
- **Expected if population model correct:** Shorter repeats in Japanese reduce STAG2-loss impact

### Test 5: Enhancer vs. PRC2 Arm Dissection
- **Design:** STAG2-null cells with selective rescue: (a) STAG2 function at GGAA sites vs. (b) EZH2 overexpression/PRC2 rescue
- **Readout:** Transcriptome, invasion, xenograft growth
- **Expected:** Dominant arm shows greater phenotypic rescue

---

## Claim Status Assessment

| Claim | Status | Evidence Level |
|-------|--------|---------------|
| STAG2 loss redistributes EWS-FLI1 from mono→multi GGAA enhancers | **ESTABLISHED** | 2 independent cell line studies |
| Multimeric enhancer amplification drives aggressive transcription | **EMERGING** | Supported but specific programs not fully mapped |
| STAG2 loss causes poor prognosis in localized ES | **ESTABLISHED** | COG N=135 P=0.003; qualified by Japanese cohort |
| STAG2-TP53 cooperation = worst prognosis | **ESTABLISHED** | WGS + clinical N=299 |
| STAG2-CDKN2A mutual exclusivity | **ESTABLISHED** | WGS + cBioPortal (0 co-mutations) |
| STAG2 loss disrupts PRC2 (cross-cancer) | **ESTABLISHED** | 3 cancer types |
| STAG1 cannot compensate at enhancers | **ESTABLISHED** | 3+ studies, consistent |
| STAG2 loss increases EWS-FLI1 protein | **EMERGING** | 1 study; mechanism unknown |
| Primary tumor enhancer redistribution | **NOT TESTED** | 0 primary tumor chromatin studies |
| PARP/STAG1 therapeutic vulnerability in ES | **SPECULATIVE** | Cross-cancer data; not clinically tested |

---

## Curation Leads

*All items below are candidate updates for the Disorder Mechanisms Knowledge Base, labeled as leads requiring curator verification.*

### Candidate Evidence References

1. **PMID: 41950086** (Eyunni et al. 2026) — Primary support. Verified snippet: *"STAG2 loss eliminates over 40% of EWS-FLI1 binding sites, predominantly at enhancers containing short (1-4) GGAA repeats, while concurrently increasing binding at multimeric enhancers with ≥5 GGAA-repeat motifs."* Status: SUPPORT, IN_VITRO.

2. **PMID: 39487368** (Giménez-Llorente et al. 2024) — Independent confirmation. Verified snippet: *"cohesin-STAG2 facilitates communication between EWS::FLI1-bound long GGAA repeats, presumably acting as neoenhancers, and their target promoters."* Status: SUPPORT, IN_VITRO.

3. **PMID: 36221002** (Shulman et al. 2022) — Clinical prognostic. Verified snippet: *"5-year event-free survival was 54% (95% CI 34-70%) and 75% (95% CI 63-84%) for patients with STAG2 loss vs. expression (P = 0.0034)."* Status: SUPPORT, HUMAN_CLINICAL.

4. **PMID: 34129824** (Adane et al. 2021) — Qualifies model. Verified snippet: *"loss of STAG2 also disrupted PRC2-mediated regulation of gene expression. Combined, these transcriptional changes converged to modulate EWS/FLI1, migratory, and neurodevelopmental programs."* Status: QUALIFIES, IN_VITRO.

5. **PMID: 41206913** (Kamio et al. 2026) — Qualifies universality. Verified snippet: *"There was no significant difference in overall survival after genomic profiling test enrollment for STAG2 and TP53 mutations (P = .663 and P = .767)."* Status: QUALIFIES, HUMAN_CLINICAL.

6. **PMID: 25223734** (Tirode et al. 2014) — Foundational genomic. Verified snippet: *"STAG2 and TP53 mutations are often concurrent and are associated with poor outcome."* Status: SUPPORT, HUMAN_CLINICAL.

7. **PMID: 41949996** (Suzuki et al. 2026) — Cross-cancer PRC2. Verified snippet: *"Stag2 loss induced a moderate but significant degree of PRC2-insufficient state in Gata1s progenitors."* Status: SUPPORT (cross-cancer), MODEL_ORGANISM.

8. **PMID: 30700749** (Gierisch et al. 2019) — Protein stability context. Verified snippet: *"Depletion of USP19 resulted in diminished EWS-FLI1 protein levels and, vice versa, upregulation of active USP19 stabilized the fusion protein."* Status: CONTEXT, IN_VITRO.

### Candidate Pathophysiology Nodes/Edges

- **Node:** Multimeric GGAA microsatellite enhancer (≥5 GGAA repeats) — new concept
- **Edge:** STAG2 loss → amplified multimeric GGAA enhancer output (PMID: 41950086, 39487368)
- **Edge:** STAG2 loss → PRC2 derepression (PMID: 34129824, 41949996, 41091719)
- **Edge:** STAG2 loss → CTCF-dependent chromatin rewiring (PMID: 39487368)
- **Edge:** STAG2 loss ⊥ CDKN2A deletion (mutual exclusivity; PMID: 25223734)
- **Edge:** STAG2 loss + TP53 mutation → synergistic poor outcome (PMID: 25223734)
- **Edge:** STAG1 = synthetic lethal with STAG2 loss (PMID: 28430577, 32467316, 29649003)

### Candidate Ontology Terms

- **Cell type:** CL:0000134 (mesenchymal stem cell)
- **Biological processes:** GO:0006355 (regulation of transcription, DNA-templated); GO:0051276 (chromosome organization); GO:0016569 (covalent chromatin modification); GO:0045944 (positive regulation of transcription by RNA Pol II)
- **Disease:** MONDO:0007898 (Ewing sarcoma)

### Candidate Subtype Restrictions

- Most strongly supported in **localized Ewing sarcoma** in **Western/European-ancestry populations**
- Most applicable to **STAG2-mutant/IHC-negative tumors** (~10-27% depending on population and method)
- Effects likely strongest with **co-occurring TP53 mutations**
- May not apply to **CDKN2A-deleted** or **non-EWS-FLI1 fusion** Ewing sarcoma

### Candidate Status Change

- **Current status:** EMERGING
- **Recommended status:** Maintain **EMERGING**
- **Upgrade criteria:** (1) Primary tumor ATAC-seq/CUT&Tag validation, (2) mechanism for EWS-FLI1 protein increase, (3) STAG2-stratified therapeutic data

### Candidate Knowledge Gaps for KB

1. EWS-FLI1 protein stability mechanism upon STAG2 loss — unknown
2. Enhancer vs. PRC2 arm epistasis — unresolved
3. Population-specific GGAA architecture × STAG2 interaction — untested
4. No formal gene-disease annotation (ClinGen, GenCC, ClinVar) for somatic STAG2 in cancer
5. No STAG2-stratified clinical trials in Ewing sarcoma
6. SIX1-STAG2 intersection and immune microenvironment effects — unexplored

---

## Investigation Statistics

| Metric | Count |
|--------|-------|
| Primary literature references | 28 |
| cBioPortal samples analyzed | 222 |
| Confirmed findings recorded | 11 |
| Knowledge gaps identified | 13 |
| Competing/alternative models | 6 |
| Discriminating tests proposed | 5 |
| Claims assessed as ESTABLISHED | 6 |
| Claims assessed as EMERGING | 2 |
| Claims assessed as NOT TESTED | 1 |
| Claims assessed as SPECULATIVE | 1 |

{{figure:final_summary.png|caption=Definitive summary of the STAG2/cohesin-modified high-risk enhancer hypothesis: evidence strength, knowledge gaps, and validation roadmap}}

---

*Report generated 2026-05-28. Based on systematic evaluation of 28 primary references and 65 total papers reviewed across 5 investigation iterations. All PMID citations verified against available abstracts.*
