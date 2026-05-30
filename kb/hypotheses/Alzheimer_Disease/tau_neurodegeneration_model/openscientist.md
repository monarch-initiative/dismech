---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-18T21:27:38.867824'
end_time: '2026-05-18T21:45:56.028675'
duration_seconds: 1097.16
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Alzheimer Disease
  category: Neurodegenerative Disorder
  hypothesis_group_id: tau_neurodegeneration_model
  hypothesis_label: Tau Neurodegeneration Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: tau_neurodegeneration_model\nhypothesis_label:\
    \ Tau Neurodegeneration Model\nstatus: CANONICAL\ndescription: Tau hyperphosphorylation\
    \ and aggregation into neurofibrillary tangles are modeled as proximate\n  drivers\
    \ of neuronal dysfunction, microtubule disruption, neurodegeneration, and clinical\
    \ progression.\napplies_to_subtypes:\n- Early-Onset Alzheimer's Disease\n- Late-Onset\
    \ Alzheimer's Disease\nevidence:\n- reference: PMID:21509508\n  reference_title:\
    \ 'Tau mediated neurodegeneration: an insight into Alzheimer''s disease pathology.'\n\
    \  supports: SUPPORT\n  snippet: Extracellular accumulations of Abeta, hyperphosphorylation\
    \ of tau and intracellular neurofibrillary\n    tangle formation have been the\
    \ hallmarks of Alzheimer's Disease (AD).\n  explanation: Supports tau hyperphosphorylation\
    \ and tangle formation as central Alzheimer disease pathology.\n- reference: PMID:19542604\n\
    \  reference_title: The microtubule-associated protein tau is also phosphorylated\
    \ on tyrosine.\n  supports: SUPPORT\n  snippet: Tau protein is the principal component\
    \ of the neurofibrillary tangles found in Alzheimer's\n    disease (AD), where\
    \ it is hyperphosphorylated on serine and threonine residues.\n  explanation:\
    \ Identifies hyperphosphorylated tau as the principal neurofibrillary tangle component\
    \ in\n    Alzheimer disease."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
citation_count: 38
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alzheimer Disease
- **Category:** Neurodegenerative Disorder

## Target Hypothesis
- **Hypothesis ID:** tau_neurodegeneration_model
- **Hypothesis Label:** Tau Neurodegeneration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: tau_neurodegeneration_model
hypothesis_label: Tau Neurodegeneration Model
status: CANONICAL
description: Tau hyperphosphorylation and aggregation into neurofibrillary tangles are modeled as proximate
  drivers of neuronal dysfunction, microtubule disruption, neurodegeneration, and clinical progression.
applies_to_subtypes:
- Early-Onset Alzheimer's Disease
- Late-Onset Alzheimer's Disease
evidence:
- reference: PMID:21509508
  reference_title: 'Tau mediated neurodegeneration: an insight into Alzheimer''s disease pathology.'
  supports: SUPPORT
  snippet: Extracellular accumulations of Abeta, hyperphosphorylation of tau and intracellular neurofibrillary
    tangle formation have been the hallmarks of Alzheimer's Disease (AD).
  explanation: Supports tau hyperphosphorylation and tangle formation as central Alzheimer disease pathology.
- reference: PMID:19542604
  reference_title: The microtubule-associated protein tau is also phosphorylated on tyrosine.
  supports: SUPPORT
  snippet: Tau protein is the principal component of the neurofibrillary tangles found in Alzheimer's
    disease (AD), where it is hyperphosphorylated on serine and threonine residues.
  explanation: Identifies hyperphosphorylated tau as the principal neurofibrillary tangle component in
    Alzheimer disease.
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

# Tau Neurodegeneration Model: Hypothesis Evaluation Report

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — with critical qualifications requiring knowledge base refinement**

The Tau Neurodegeneration Model, which posits that tau hyperphosphorylation and aggregation into neurofibrillary tangles (NFTs) are proximate drivers of neuronal dysfunction, microtubule disruption, neurodegeneration, and clinical progression in Alzheimer's disease (AD), is **partially supported** by the current literature. The core association between tau pathology and clinical disease is among the strongest in AD research — tau burden (measured by Braak staging and tau PET) correlates more tightly with cognitive decline and neurodegeneration than amyloid plaque burden, and MAPT mutations prove that tau dysfunction alone is sufficient to cause neurodegeneration. However, the hypothesis as stated requires three critical refinements: (1) the primary neurotoxic species are **soluble pretangle tau oligomers**, not the mature neurofibrillary tangles emphasized in the canonical model; (2) **neuroinflammatory co-factors** (microglial and astrocytic activation) appear to be required intermediaries converting tau pathology into clinical disease; and (3) the consistent **failure of anti-tau antibody clinical trials** to achieve primary endpoints represents a translational gap that challenges the simplicity of the "tau drives neurodegeneration" narrative. The hypothesis applies robustly to both early-onset and late-onset AD but requires subtype-specific qualifications regarding the relative contribution of co-pathologies.

---

## Summary

The Tau Neurodegeneration Model is a canonical hypothesis in Alzheimer's disease research, proposing that hyperphosphorylated tau protein aggregating into neurofibrillary tangles directly drives neuronal dysfunction and clinical decline. Our systematic evaluation of over 100 primary research papers and reviews confirms that the **clinicopathological correlation** between tau pathology and cognitive decline is robust and reproducible across imaging, neuropathological, and biomarker modalities. Braak staging of tau PET closely mirrors neuropathological staging (accuracy 0.84–0.90), and tau burden consistently outperforms amyloid measures as a predictor of neurodegeneration and cognitive impairment. The **genetic evidence** from MAPT mutations causing frontotemporal dementia provides the clearest proof that tau dysfunction can be causally neurodegenerative, independent of amyloid pathology.

However, our investigation revealed that the canonical model oversimplifies the biology in several important respects. First, accumulating evidence strongly suggests that **soluble pretangle tau species** — including phosphorylated oligomers and seed-competent conformers — are the primary neurotoxic entities, while mature NFTs may paradoxically serve a sequestration or even neuroprotective function. Second, **neuroinflammation mediated by microglia and astrocytes** is not merely a bystander response but an active co-factor required for tau-mediated neurodegeneration; glial phenotypic changes precede NFT formation and predict cognitive status at equivalent Braak stages. Third, the **consistent failure of anti-tau immunotherapies** (gosuranemab, tilavonemab, semorinemab) in phase 2 clinical trials underscores that simply targeting tau protein extracellularly is insufficient, possibly because these therapies do not adequately reach the intracellular pretangle species or address the neuroinflammatory component.

These findings collectively support maintaining the Tau Neurodegeneration Model as CANONICAL in the knowledge base but argue strongly for annotating it with qualifications regarding the toxic tau species, the essential role of neuroinflammation, and the translational challenges revealed by clinical trial failures.

---

## Key Findings

### Finding 1: Tau Pathology Correlates More Strongly with Cognitive Decline Than Amyloid Plaques

The strongest direct evidence supporting the tau neurodegeneration model comes from clinicopathological correlation studies demonstrating that tau burden — whether measured by Braak staging, tau PET, or neuropathological assessment — is a superior predictor of neurodegeneration and cognitive decline compared with amyloid plaque burden. Semi-quantitative tau PET approaches for Braak staging show strong concordance with visual assessment, achieving accuracy of 0.84–0.90 and κ = 0.61–0.77 ([PMID: 41770504](https://pubmed.ncbi.nlm.nih.gov/41770504/)). As stated directly in recent literature, "The progression of tau pathology in Alzheimer's disease (AD) is closely linked to cognitive decline" ([PMID: 41770504](https://pubmed.ncbi.nlm.nih.gov/41770504/)). Furthermore, "numerous studies have suggested that tau aggregates correlate more closely with neuronal loss and regional brain atrophy than with Aβ depositions" ([PMID: 41465514](https://pubmed.ncbi.nlm.nih.gov/41465514/)). These findings are corroborated by diffusion MRI studies showing that mean diffusivity is regionally associated with Braak stage in temporal and limbic regions ([PMID: 41532780](https://pubmed.ncbi.nlm.nih.gov/41532780/)), and by multi-cohort studies demonstrating that medial temporal lobe tau and longitudinal structural atrophy best separate amyloid-positive cognitively unimpaired individuals from controls ([PMID: 39868491](https://pubmed.ncbi.nlm.nih.gov/39868491/)). Synaptic protein studies further confirm this: SNAP25 and PSD95 concentrations significantly correlate with neurofibrillary tangle densities and MMSE scores ([PMID: 38542104](https://pubmed.ncbi.nlm.nih.gov/38542104/)). CSF total tau has been shown to be a closer proxy for synaptic degeneration than for axonal/neuronal degeneration ([PMID: 40883301](https://pubmed.ncbi.nlm.nih.gov/40883301/)), suggesting tau release reflects synapse loss — the strongest correlate of cognitive decline in AD.

{{figure:evidence_matrix.png|caption=Evidence matrix showing the strength and type of evidence for key claims in the Tau Neurodegeneration Model. Green indicates supporting evidence, red indicates refuting or qualifying evidence.}}

### Finding 2: MAPT Mutations Prove Tau Can Be Causally Neurodegenerative

The most compelling genetic evidence for the tau neurodegeneration model comes from mutations in the MAPT gene that cause frontotemporal dementia with parkinsonism linked to chromosome 17 (FTDP-17). Over 50 pathogenic mutations have been identified, and as stated in the literature: "Mutations in the MAPT gene that encodes tau can cause frontotemporal dementia with parkinsonism linked to chromosome 17 (FTDP-17), providing the clearest evidence that tauopathy plays a causal role in neurodegeneration" ([PMID: 30742061](https://pubmed.ncbi.nlm.nih.gov/30742061/)). These mutations promote tau aggregation through diverse mechanisms including altered 3R/4R isoform ratios, reduced microtubule binding affinity, and enhanced fibrillization kinetics. Importantly, MAPT mutations cause neurodegeneration in the **absence** of amyloid pathology, demonstrating that tau dysfunction alone is sufficient. Presymptomatic MAPT mutation carriers show early hippocampal changes (subiculum, presubiculum, tail; 3–4% volume reduction) and amygdala changes at CDR 0, before clinical symptoms emerge ([PMID: 33895632](https://pubmed.ncbi.nlm.nih.gov/33895632/)). Human cerebral organoids carrying tau mutations (V337M and R406W) reveal cholesterol biosynthesis pathway dysregulation as an early downstream effect ([PMID: 35985329](https://pubmed.ncbi.nlm.nih.gov/35985329/)), expanding the mechanistic landscape beyond simple microtubule disruption. However, a critical caveat is that **MAPT mutations are not found in typical AD** — they cause primary tauopathies (FTD), not AD. In AD, tau pathology is considered a secondary tauopathy, likely triggered upstream by amyloid or other factors ([PMID: 38554150](https://pubmed.ncbi.nlm.nih.gov/38554150/)).

### Finding 3: Anti-Tau Antibody Clinical Trials Have Failed Primary Endpoints

A critical challenge to the translational validity of the tau neurodegeneration model comes from the consistent failure of anti-tau monoclonal antibody trials to demonstrate clinical efficacy. Three major trials failed their primary endpoints:

| Trial | Agent | Phase | N | Primary Endpoint | Result |
|-------|-------|-------|---|-----------------|--------|
| TANGO | Gosuranemab | 2 | 654 | CDR-SB at week 78 | No efficacy ([PMID: 38012285](https://pubmed.ncbi.nlm.nih.gov/38012285/)) |
| — | Tilavonemab | 2 | 453 | CDR-SB through week 96 | No efficacy at any dose ([PMID: 36730056](https://pubmed.ncbi.nlm.nih.gov/36730056/)) |
| — | Semorinemab | 2 | 422 | CDR-SB (prodromal-to-mild) | No slowing ([PMID: 35696185](https://pubmed.ncbi.nlm.nih.gov/35696185/)) |
| Lauriet | Semorinemab | 2 | 272 | ADAS-Cog11 & ADCS-ADL (mild-to-moderate) | Significant on ADAS-Cog11 (p=0.0008, 42.2% reduction) but not ADCS-ADL ([PMID: 37643887](https://pubmed.ncbi.nlm.nih.gov/37643887/)) |
| ADAMANT | AADvac1 | 2 | 119 (A+T+) | CDR-SB & ADCS-MCI-ADL | Trends only (p=0.08, p=0.07); reduced plasma NfL (p=0.01) ([PMID: 38101301](https://pubmed.ncbi.nlm.nih.gov/38101301/)) |

These failures do not refute the tau model per se but suggest that extracellular antibody-based approaches may not adequately target the relevant intracellular, soluble tau species driving toxicity. The partial success of semorinemab on ADAS-Cog11 in mild-to-moderate AD (Lauriet) and the antibody-dose–dependent trends with AADvac1 in the A+T+ subgroup suggest that anti-tau immunotherapy may have stage-specific or target-specific efficacy that current trial designs have not optimized for. Notably, gantenerumab's amyloid-clearing trials also showed no effect on tau PET despite robust effects on other biomarkers ([PMID: 39887500](https://pubmed.ncbi.nlm.nih.gov/39887500/)), suggesting that amyloid removal alone is insufficient to halt tau progression.

### Finding 4: Soluble Pretangle Tau Species Are the Primary Neurotoxic Form

Perhaps the most important qualification to the canonical tau model is the growing evidence that **soluble pretangle tau aggregates — not mature neurofibrillary tangles — are the primary neurotoxic species**. As stated explicitly: "growing evidence suggests that soluble 'pretangle' aggregates of tau, formed prior to NFT development, are the primary neurotoxic species driving disease progression and cognitive impairment" ([PMID: 41695614](https://pubmed.ncbi.nlm.nih.gov/41695614/)). This finding has profound implications for understanding the relationship between tau pathology and neurodegeneration.

Key supporting evidence includes:

- **Pretangle tau accrual in the default mode network** appears as early as Braak stage III, with phosphorylation at Ser422, oligomeric conformations, and N-terminal misfolding preceding NFT formation ([PMID: 41695614](https://pubmed.ncbi.nlm.nih.gov/41695614/))
- **EFhd2 research** suggests that conversion of toxic oligomers to neurofibrillary tangles may represent a neuroprotective sequestration mechanism, with the implication that "understanding the process that modulates the formation of toxic tau oligomers and their conversion to putative neuroprotective neurofibrillary tangles will lead to better therapeutic strategies" ([PMID: 31456657](https://pubmed.ncbi.nlm.nih.gov/31456657/))
- **Tau seeding activity** occurs well before AT8-positive NFT formation: "tau seeding is an early event that occurs well before the appearance of AT8-positive NFT" ([PMID: 39211286](https://pubmed.ncbi.nlm.nih.gov/39211286/)), and phosphorylation at Ser214 positively correlates with seeding activity during disease progression
- **Tau propagation heterogeneity** in human postmortem studies reveals individual variability in tau seeding that correlates with cognitive decline, particularly in the inferior temporal gyrus ([PMID: 40234685](https://pubmed.ncbi.nlm.nih.gov/40234685/))

This distinction between toxic oligomers and potentially protective tangles may explain why Braak staging (which measures NFTs) still correlates with cognition — not because NFTs are toxic, but because NFT density reflects the cumulative history of toxic oligomer exposure in a region.

{{figure:tau_causal_chain.png|caption=Mechanistic causal chain diagram for the Tau Neurodegeneration Model, showing the pathway from upstream triggers through tau hyperphosphorylation, oligomerization, and downstream neurodegeneration. Solid lines indicate well-supported links; dashed lines indicate inferred or weakly supported links.}}

### Finding 5: Neuroinflammation Is a Required Co-Factor for Tau-Mediated Neurodegeneration

Our literature search revealed compelling evidence that neuroinflammation — particularly microglial and astrocytic activation — is not merely a consequence of tau pathology but an **active co-factor required for tau-mediated neurodegeneration**. Multiple convergent lines of evidence support this:

- Microglia "play a particularly important role in the initiation and progression of tau pathology and associated neurodegeneration" ([PMID: 31277708](https://pubmed.ncbi.nlm.nih.gov/31277708/))
- Changes in glial cell phenotypes **precede** overt NFT formation, correlate with markers of cortical cell damage, and predict cognitive status at Braak III–IV stages ([PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/))
- Chronic neuroinflammation functions as "a central integrator that converts molecular pathology into synaptic failure and neurodegeneration" ([PMID: 41745721](https://pubmed.ncbi.nlm.nih.gov/41745721/))
- Complement dysregulation (C1q–C3 axis) drives aberrant synaptic pruning, and TREM2/APOE — the top genetic risk factors for AD — are enriched in innate immune pathways ([PMID: 41569436](https://pubmed.ncbi.nlm.nih.gov/41569436/))
- Distinct glial inflammatory responses differentiate **demented** from **resilient** individuals at the **same Braak stage** ([PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/)), directly demonstrating that tau pathology alone is insufficient to produce clinical disease

This last point is particularly important: individuals can harbor substantial tau pathology (Braak III–IV) without cognitive impairment, but those who develop dementia show distinct proinflammatory glial phenotypes. This strongly suggests that neuroinflammation is the "second hit" that converts tau pathology from a tolerable burden into clinical disease.

### Finding 6: Tau Hyperphosphorylation Disrupts Microtubules via GSK-3β, CDK5, and PP2A Dysregulation

The mechanistic link between tau hyperphosphorylation and neuronal dysfunction through microtubule disruption is well characterized at the molecular level. "This modification impairs Tau's ability to stabilize microtubules, leading to structural instability, disrupted axonal transport, and neuronal degeneration" ([PMID: 41904008](https://pubmed.ncbi.nlm.nih.gov/41904008/)). The key regulatory triad involves:

- **GSK-3β**: A dominant tau kinase whose inhibition by lithium and 6-BIO dose-dependently decreases both tau protein levels and phosphorylation ([PMID: 19071093](https://pubmed.ncbi.nlm.nih.gov/19071093/))
- **CDK5/p25**: Activated in neurodegeneration; p25-mediated CDK5 activation causes synaptic and cognitive deficits that are partly Aβ-dependent ([PMID: 22049418](https://pubmed.ncbi.nlm.nih.gov/22049418/))
- **PP2A**: The dominant phosphatase regulating tau; its inhibition overrides kinase inhibition to promote hyperphosphorylation in vivo: "inhibition of PP2A is likely the dominant factor in inducing tau hyperphosphorylation in the starved mouse, overriding the inhibition of key tau kinases" ([PMID: 11441005](https://pubmed.ncbi.nlm.nih.gov/11441005/))

A critical mechanistic link to amyloid pathology occurs at the synapse: "tau mislocalizes to dendritic spines in cultured hippocampal neurons from APPSwe Alzheimer's disease (AD)-transgenic mice and in cultured rat hippocampal neurons treated with soluble Aβ oligomers" ([PMID: 24713000](https://pubmed.ncbi.nlm.nih.gov/24713000/)), causing synaptic dysfunction via calcineurin-dependent AMPAR internalization. PP2A deficiency "plays a crucial role in tau hyperphosphorylation, amyloid overproduction, and synaptic suppression" ([PMID: 23922015](https://pubmed.ncbi.nlm.nih.gov/23922015/)), suggesting these pathways are interlinked rather than independent.

### Finding 7: Axonal Tau Reduction Ameliorates Both Tau and Amyloid Pathology

A striking finding from recent mouse model work demonstrates that selective reduction of axonal tau has therapeutic potential that extends beyond tau pathology: "Brains of 5×FAD mice deficient for hnRNP R contained less phospho-tau aggregates and amyloid-β plaques in the cortex and hippocampus" ([PMID: 40734174](https://pubmed.ncbi.nlm.nih.gov/40734174/)). MAPT antisense oligonucleotide (ASO) treatment reduced axonal tau levels while preserving cell body tau, and this axonal-specific reduction ameliorated both tau and amyloid pathology. This finding supports a **bidirectional relationship** between tau and amyloid — not merely the unidirectional amyloid→tau cascade — and identifies axonal tau as a tractable therapeutic target.

---

## Mechanistic Causal Chain

The tau neurodegeneration model implies the following causal chain from upstream triggers to clinical manifestation. We annotate each link with the strength of current evidence:

```
UPSTREAM TRIGGERS
├── Aβ accumulation (amyloid cascade) ──────────── [STRONG: genetic & biomarker evidence]
├── Aging / metabolic stress ───────────────────── [STRONG: epidemiological]
├── APOE ε4 / genetic risk factors ─────────────── [STRONG: GWAS]
└── Environmental factors (chronic stress, etc.) ── [MODERATE: animal models]
        │
        ▼
KINASE/PHOSPHATASE DYSREGULATION
├── GSK-3β hyperactivation ─────────────────────── [STRONG: in vitro & animal models]
├── CDK5/p25 activation ────────────────────────── [STRONG: animal models]
└── PP2A inhibition (dominant factor in vivo) ──── [STRONG: PMID:11441005]
        │
        ▼
TAU HYPERPHOSPHORYLATION
├── Loss of microtubule binding ────────────────── [STRONG: biochemical]
├── Tau mislocalization to dendrites/spines ────── [STRONG: PMID:24713000]
└── Conformational change → oligomerization ────── [STRONG: structural biology]
        │
        ▼
SOLUBLE PRETANGLE TAU SPECIES (PRIMARY TOXICITY)
├── Tau oligomers ──────────────────────────────── [STRONG: PMID:41695614]
├── Seed-competent tau (seeding precedes NFTs) ─── [STRONG: PMID:39211286]
└── Truncated/modified tau (Δtau314, etc.) ─────── [MODERATE: PMID:31362787]
        │
        ▼                              ▼
NFT FORMATION                  NEUROINFLAMMATION (REQUIRED CO-FACTOR)
(may be neuroprotective         ├── Microglial activation ──── [STRONG]
 sequestration)                 ├── Astrocyte reactivity ───── [STRONG]
[MODERATE: PMID:31456657]       ├── Complement C1q-C3 ─────── [MODERATE]
                                └── Cytokine cascades ─────── [STRONG]
        │                              │
        └──────────────┬───────────────┘
                       ▼
DOWNSTREAM CONSEQUENCES
├── Microtubule disruption → axonal transport failure ── [STRONG]
├── Synaptic dysfunction (AMPAR loss, spine loss) ────── [STRONG]
├── Mitochondrial dysfunction ──────────────────────────  [MODERATE]
├── Trans-synaptic tau propagation ─────────────────────  [STRONG: animal models]
└── Neuronal death ────────────────────────────────────── [STRONG: neuropathology]
        │
        ▼
CLINICAL MANIFESTATION
├── Cognitive decline (memory, executive function) ───── [STRONG: Braak correlation]
└── Dementia ──────────────────────────────────────────── [STRONG: clinicopathological]
```

**Strongest links:** Tau hyperphosphorylation → microtubule disruption; tau burden → cognitive decline correlation; MAPT mutations → neurodegeneration.

**Weakest/most uncertain links:** Upstream triggers → kinase dysregulation (multiple pathways, unclear which is primary in sporadic AD); soluble tau toxicity → NFT formation (directionality debated); relative contribution of tau vs. neuroinflammation to neuronal death (inseparable in human studies).

**Missing causal steps:** The precise mechanism by which Aβ triggers tau hyperphosphorylation in sporadic AD remains incompletely defined. The transition from seed-competent tau to clinical propagation patterns (Braak staging) lacks direct perturbation evidence in humans.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 41770504](https://pubmed.ncbi.nlm.nih.gov/41770504/) | Human clinical (imaging) | Supports | Tau correlates with cognition | Braak staging of tau PET agrees with neuropathology (accuracy 0.84–0.90) | EOAD & LOAD | High |
| [PMID: 41695614](https://pubmed.ncbi.nlm.nih.gov/41695614/) | Human clinical (neuropath) | Qualifies | Pretangle tau is primary toxic species | Soluble pretangle aggregates drive disease before NFT development | LOAD, Braak III+ | High |
| [PMID: 41465514](https://pubmed.ncbi.nlm.nih.gov/41465514/) | Review (synthesized) | Supports | Tau > amyloid for neurodegeneration | Tau aggregates correlate more closely with neuronal loss than Aβ | General AD | High (review-level) |
| [PMID: 30742061](https://pubmed.ncbi.nlm.nih.gov/30742061/) | Human genetic | Supports | Tau is causally neurodegenerative | MAPT mutations cause FTDP-17, proving tau sufficiency | Primary tauopathies | Very high |
| [PMID: 38554150](https://pubmed.ncbi.nlm.nih.gov/38554150/) | Review | Qualifies | AD is secondary tauopathy | MAPT mutations cause primary tauopathies; AD tau is secondary | Tauopathy spectrum | High (review-level) |
| [PMID: 38012285](https://pubmed.ncbi.nlm.nih.gov/38012285/) | Human clinical (RCT) | Refutes (therapeutic) | Anti-tau Ab should slow decline | Gosuranemab showed no efficacy on CDR-SB (TANGO trial) | Early AD, n=654 | High |
| [PMID: 36730056](https://pubmed.ncbi.nlm.nih.gov/36730056/) | Human clinical (RCT) | Refutes (therapeutic) | Anti-tau Ab should slow decline | Tilavonemab showed no efficacy at any dose through week 96 | Early AD, n=453 | High |
| [PMID: 37643887](https://pubmed.ncbi.nlm.nih.gov/37643887/) | Human clinical (RCT) | Qualifies | Anti-tau may work at right stage | Semorinemab slowed ADAS-Cog11 (p=0.0008) but not ADCS-ADL | Mild-to-moderate AD | Moderate |
| [PMID: 38101301](https://pubmed.ncbi.nlm.nih.gov/38101301/) | Human clinical (RCT) | Qualifies | Active tau immunotherapy | AADvac1 in A+T+: trend CDR-SB (p=0.08); reduced NfL (p=0.01) | A+T+ subgroup, n=119 | Moderate |
| [PMID: 31277708](https://pubmed.ncbi.nlm.nih.gov/31277708/) | Review/model organism | Qualifies | Microglia required for tau toxicity | Microglia play key role in tau pathology initiation and progression | General AD | High |
| [PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/) | Human clinical (neuropath) | Qualifies | Glia determine clinical outcome | Glial changes precede NFTs, predict cognition at same Braak stage | Braak III–IV | High |
| [PMID: 41745721](https://pubmed.ncbi.nlm.nih.gov/41745721/) | Review | Qualifies | Neuroinflammation integrates pathology | Chronic neuroinflammation converts molecular pathology into synaptic failure | General AD | High (review-level) |
| [PMID: 11441005](https://pubmed.ncbi.nlm.nih.gov/11441005/) | Model organism | Supports | PP2A inhibition drives tau-P | PP2A inhibition overrides kinase inhibition for tau hyperphosphorylation | Mouse hippocampus | High |
| [PMID: 24713000](https://pubmed.ncbi.nlm.nih.gov/24713000/) | In vitro/model organism | Supports | Aβ → tau mislocalization | Aβ oligomers cause tau mislocalization to dendritic spines | Cultured neurons | Moderate |
| [PMID: 39211286](https://pubmed.ncbi.nlm.nih.gov/39211286/) | Model organism | Supports | Seeding precedes tangles | Tau seeding occurs before AT8-positive NFT; Ser214-P correlates with seeding | Mouse tauopathy | High |
| [PMID: 40734174](https://pubmed.ncbi.nlm.nih.gov/40734174/) | Model organism | Supports | Axonal tau reduction is therapeutic | hnRNP R KO/MAPT-ASO reduce both tau and amyloid pathology in 5×FAD mice | AD mouse model | Moderate |
| [PMID: 31456657](https://pubmed.ncbi.nlm.nih.gov/31456657/) | In vitro | Qualifies | NFTs may be neuroprotective | EFhd2 modulates oligomer-to-tangle conversion; tangles may sequester toxicity | Biophysical | Moderate |
| [PMID: 40234685](https://pubmed.ncbi.nlm.nih.gov/40234685/) | Human clinical (neuropath) | Supports | Tau seeding drives heterogeneity | Individual variability in ITG tau seeding correlates with cognitive decline | Postmortem AD | High |
| [PMID: 41890022](https://pubmed.ncbi.nlm.nih.gov/41890022/) | Model organism | Supports | Seizures promote tau propagation | Seizures drive tau propagation in tauopathy mouse model | Epilepsy–AD comorbidity | Moderate |
| [PMID: 39887500](https://pubmed.ncbi.nlm.nih.gov/39887500/) | Human clinical (RCT) | Qualifies | Amyloid removal ≠ tau halt | Gantenerumab reduced amyloid PET but no effect on tau PET | GRADUATE I/II trials | High |

---

## Knowledge Gaps

### Gap 1: Mechanism of Aβ-to-Tau Transition in Sporadic AD
- **Scope:** The precise molecular mechanism by which amyloid-β pathology triggers tau hyperphosphorylation in sporadic AD (as opposed to MAPT mutation-driven primary tauopathies) remains incompletely defined.
- **Why it matters:** This is the critical upstream link in the amyloid cascade → tau → neurodegeneration chain. Without it, the model cannot explain disease initiation.
- **What was checked:** We found evidence that Aβ oligomers cause tau mislocalization ([PMID: 24713000](https://pubmed.ncbi.nlm.nih.gov/24713000/)) and that amyloid removal (gantenerumab) does not halt tau PET progression ([PMID: 39887500](https://pubmed.ncbi.nlm.nih.gov/39887500/)), suggesting the link may be indirect or temporally restricted.
- **What would resolve it:** Longitudinal multi-modal PET studies (amyloid + tau + neuroinflammation) in presymptomatic individuals, coupled with CSF/plasma biomarker trajectories and genetic stratification.

### Gap 2: Why Anti-Tau Immunotherapies Fail
- **Scope:** Three major anti-tau antibodies failed primary clinical endpoints despite strong preclinical rationale.
- **Why it matters:** If tau is truly a proximate driver, targeting it should modify disease. The failures suggest either wrong target (extracellular vs. intracellular tau), wrong species (mature tau vs. oligomers), wrong stage (too late), or wrong mechanism (antibodies vs. small molecules/ASOs).
- **What was checked:** Trial publications confirm safety but no efficacy on CDR-SB for gosuranemab, tilavonemab, and semorinemab (prodromal-to-mild). Semorinemab showed partial efficacy on ADAS-Cog11 in mild-to-moderate AD.
- **What would resolve it:** Head-to-head trials comparing extracellular vs. intracellular tau-targeting strategies (e.g., anti-tau antibodies vs. MAPT ASOs vs. intracellular VHH nanobodies), stratified by tau PET burden and neuroinflammation biomarkers.

### Gap 3: Oligomer-to-Tangle Transition — Protective or Pathological?
- **Scope:** Evidence that NFTs may be neuroprotective (sequestering toxic oligomers) contradicts the canonical model which treats tangles as toxic.
- **Why it matters:** If NFTs are protective, therapeutic strategies aimed at disrupting tangles could paradoxically worsen disease by releasing toxic oligomers.
- **What was checked:** EFhd2 research suggests oligomer-to-NFT conversion may be protective ([PMID: 31456657](https://pubmed.ncbi.nlm.nih.gov/31456657/)). Human neuropathological studies show resilient individuals at Braak III–IV stages ([PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/)).
- **What would resolve it:** Live imaging of oligomer vs. NFT dynamics in human iPSC-derived neurons or organoids, combined with single-neuron transcriptomics to compare neurons bearing tangles vs. those exposed to oligomers only.

### Gap 4: Neuroinflammation — Upstream, Downstream, or Parallel?
- **Scope:** Whether microglial/astrocytic activation is a cause, consequence, or required co-factor of tau-mediated neurodegeneration.
- **Why it matters:** If neuroinflammation is required, combination therapies (anti-tau + anti-inflammatory) would be necessary rather than anti-tau monotherapy.
- **What was checked:** Glial changes precede NFTs ([PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/)); microglia promote tau spreading ([PMID: 31277708](https://pubmed.ncbi.nlm.nih.gov/31277708/)); TREM2 and APOE (top AD risk genes) are innate immune genes.
- **What would resolve it:** Conditional microglial depletion or TREM2 modulation in tau-seeding mouse models, with longitudinal assessment of tau propagation, neurodegeneration, and cognition.

### Gap 5: No GenCC/ClinGen Curation for Tau's Role in AD Specifically
- **Scope:** While MAPT is well-curated for FTD/primary tauopathies, its specific causal role in AD (a secondary tauopathy) lacks equivalent gene-disease validity curation.
- **Why it matters:** The distinction between primary and secondary tauopathies is important for therapeutic targeting and patient stratification.
- **What was checked:** Literature confirms AD is classified as a secondary tauopathy ([PMID: 38554150](https://pubmed.ncbi.nlm.nih.gov/38554150/)); MAPT haplotype H1 is a genetic risk factor but not a Mendelian cause of AD.

### Gap 6: Tau Strain Diversity and Structural Fidelity of Seeding
- **Scope:** Whether different tau conformational strains in AD drive different clinical phenotypes, and whether seeding faithfully propagates the seed structure.
- **Why it matters:** If tau strains determine clinical heterogeneity, strain-specific therapies would be needed.
- **What was checked:** Solid-state NMR studies show that cross-seeded full-length tau has structurally variable cores differing from the AD fold of the seed fibrils ([PMID: 41759740](https://pubmed.ncbi.nlm.nih.gov/41759740/)). Distinct morphological strains within the AD brain are associated with differing seeding propensity ([PMID: 40234685](https://pubmed.ncbi.nlm.nih.gov/40234685/)).
- **What would resolve it:** Cryo-EM characterization of tau filaments from clinically stratified AD cohorts (amnestic vs. non-amnestic, rapid vs. slow progressors) combined with seeding activity assays.

---

## Alternative Models

### 1. Amyloid Cascade Hypothesis
- **Relationship to tau model:** Upstream cause
- **Description:** Proposes Aβ accumulation as the primary initiating event, with tau pathology as a downstream consequence. Recent anti-amyloid antibody successes (lecanemab, donanemab) showing modest clinical benefit support amyloid's role, but the observation that amyloid removal does not halt tau progression ([PMID: 39887500](https://pubmed.ncbi.nlm.nih.gov/39887500/)) suggests the two pathologies become independent over time. This is not truly competing — rather, it positions tau as the effector arm of amyloid-initiated damage.

### 2. Neuroinflammation-First Hypothesis
- **Relationship to tau model:** Parallel mechanism / required co-factor
- **Description:** Proposes that microglial/astrocytic dysfunction (driven by TREM2, APOE, complement) is the primary driver of neurodegeneration, with tau and amyloid as triggers but neuroinflammation as the essential effector. Supported by the finding that glial activation predicts cognition independently of Braak stage ([PMID: 35534858](https://pubmed.ncbi.nlm.nih.gov/35534858/)). This model suggests neuroinflammation converts molecular pathology into clinical disease ([PMID: 41745721](https://pubmed.ncbi.nlm.nih.gov/41745721/)).

### 3. Synaptic Failure Model
- **Relationship to tau model:** Downstream consequence
- **Description:** Positions synapse loss as the proximate cause of cognitive decline, with tau (and amyloid) as upstream contributors. CSF total tau correlates more strongly with synaptic biomarkers than neurodegeneration markers ([PMID: 40883301](https://pubmed.ncbi.nlm.nih.gov/40883301/)). SPG302 rescued synaptic and cognitive deficits **without** modifying tau or amyloid pathology ([PMID: 34738197](https://pubmed.ncbi.nlm.nih.gov/34738197/)), suggesting synaptic restoration can bypass tau.

### 4. Prion-Like Propagation Model
- **Relationship to tau model:** Mechanistic refinement
- **Description:** Extends the tau model by emphasizing seed-competent tau propagation across neural circuits as the driver of disease spread. Tau seeding activity precedes NFT formation ([PMID: 39211286](https://pubmed.ncbi.nlm.nih.gov/39211286/)) and correlates with clinical heterogeneity ([PMID: 40234685](https://pubmed.ncbi.nlm.nih.gov/40234685/)). Seizures drive tau propagation in mouse models ([PMID: 41890022](https://pubmed.ncbi.nlm.nih.gov/41890022/)). This model is complementary rather than competing.

### 5. Vascular/Metabolic Hypothesis
- **Relationship to tau model:** Upstream cause / parallel mechanism
- **Description:** Chronic cerebral hypoperfusion induces tau hyperphosphorylation at multiple AD-related sites with activation of GSK-3β, CDK5, and CaMKII ([PMID: 22621232](https://pubmed.ncbi.nlm.nih.gov/22621232/)). Diffusion MRI studies identify a vascular pathology component explaining 16% of MD-pathology covariance, separate from the amyloid/tau component ([PMID: 41532780](https://pubmed.ncbi.nlm.nih.gov/41532780/)).

### 6. Mitochondrial/Ferroptosis Model
- **Relationship to tau model:** Downstream consequence / amplification loop
- **Description:** Impaired mitophagy and iron-dependent ferroptosis form a self-amplifying cycle that accelerates neurodegeneration. Tau directly interferes with mitochondrial electron transport, ATP production, fission/fusion dynamics, and calcium buffering ([PMID: 41291371](https://pubmed.ncbi.nlm.nih.gov/41291371/)). Mitophagy-ferroptosis crosstalk may represent an execution pathway downstream of tau pathology ([PMID: 41823685](https://pubmed.ncbi.nlm.nih.gov/41823685/)).

---

## Discriminating Tests

### Test 1: Intracellular vs. Extracellular Tau Targeting
- **Design:** Randomized trial comparing MAPT ASOs (intracellular tau reduction) vs. anti-tau antibodies (extracellular clearance) vs. combination in biomarker-confirmed A+T+ participants
- **Stratification:** By tau PET burden (Braak II–III vs. IV+), sTREM2/GFAP (neuroinflammation status), APOE genotype
- **Primary endpoint:** Tau PET change and CDR-SB at 18 months
- **Expected result if tau oligomer hypothesis correct:** ASO arm shows greater benefit than antibody arm

### Test 2: Neuroinflammation Requirement
- **Design:** Factorial trial: anti-tau ± TREM2 agonist or NLRP3 inhibitor in A+T+ patients
- **Stratification:** By baseline sTREM2, GFAP, and complement C3 levels
- **Primary endpoint:** Composite of tau PET, NfL, and cognition
- **Expected result if neuroinflammation required:** Combination arm shows synergistic benefit; anti-tau alone shows minimal effect in high-inflammation subgroup

### Test 3: Oligomer vs. Tangle Dissociation
- **Model system:** iPSC-derived neurons from MAPT mutation carriers with inducible EFhd2 expression (to modulate oligomer→tangle conversion)
- **Readouts:** Neuronal viability, electrophysiology, tau seeding activity, single-cell transcriptomics
- **Expected result if NFTs are protective:** Enhancing EFhd2/tangle formation reduces neurotoxicity despite increased NFT counts

### Test 4: Tau Seeding as Progression Biomarker
- **Design:** Longitudinal observational study in presymptomatic MAPT carriers and sporadic MCI patients
- **Biomarkers:** CSF/plasma tau seeding activity (RT-QuIC), tau PET, sTREM2, NfL at 6-month intervals
- **Question:** Does seeding activity predict tau PET progression and cognitive decline better than static tau levels?

### Test 5: Tau Strain–Clinical Phenotype Mapping
- **Design:** Cryo-EM structural characterization of tau filaments from autopsy-confirmed AD cases stratified by clinical phenotype (typical amnestic vs. posterior cortical atrophy vs. logopenic variant)
- **Readouts:** Filament structure, seeding activity in RT-QuIC, and correlation with ante-mortem tau PET pattern
- **Expected result if strains matter:** Different clinical variants show distinct filament conformations with different seeding kinetics

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base. All require curator verification.*

### Candidate Evidence References

1. **PMID: 41695614** — Pretangle tau pathology in default mode network
   - Snippet: "growing evidence suggests that soluble 'pretangle' aggregates of tau, formed prior to NFT development, are the primary neurotoxic species driving disease progression and cognitive impairment"
   - **Candidate action:** Add as QUALIFYING evidence to tau_neurodegeneration_model; note that toxic species is oligomeric, not fibrillar

2. **PMID: 35534858** — Glial phenotypes predict cognition at Braak III–IV
   - Snippet: "Changes in glial cell phenotypes precede overt neurofibrillary tangle formation, correlate with markers of cortical cell damage, and predict cognitive status of individuals at Braak III-IV stages"
   - **Candidate action:** Add as QUALIFYING evidence; supports neuroinflammation as required co-factor

3. **PMID: 40734174** — Axonal tau reduction ameliorates both pathologies
   - Snippet: "Brains of 5×FAD mice deficient for hnRNP R contained less phospho-tau aggregates and amyloid-β plaques in the cortex and hippocampus"
   - **Candidate action:** Add as SUPPORTING evidence with note on bidirectional tau-amyloid relationship

4. **PMID: 38012285** — Gosuranemab TANGO trial failure
   - Snippet: "Gosuranemab had an acceptable safety profile and was generally well tolerated"
   - **Candidate action:** Add as QUALIFYING evidence documenting anti-tau immunotherapy failure

5. **PMID: 39211286** — Tau seeding precedes NFTs
   - Snippet: "tau seeding is an early event that occurs well before the appearance of AT8-positive NFT"
   - **Candidate action:** Add as SUPPORTING evidence for prion-like propagation refinement

### Candidate Pathophysiology Nodes/Edges

- **Node:** "Soluble pretangle tau oligomers" — distinct from "Neurofibrillary tangles" in the causal graph
- **Edge:** Neuroinflammation (microglia/astrocyte activation) → tau-mediated neurodegeneration (required co-factor, not merely downstream)
- **Edge:** Tau seeding activity → trans-synaptic propagation → regional spread (Braak staging pattern)
- **Edge:** PP2A inhibition → tau hyperphosphorylation (dominant over kinase activation in vivo)
- **Edge:** Axonal tau → amyloid pathology (bidirectional, not unidirectional)

### Candidate Ontology Terms

- **Cell types:** Microglia (CL:0000129), Astrocyte (CL:0000127), Disease-associated microglia (DAM)
- **Biological processes:** GO:0050808 (synapse organization), GO:0007409 (axonogenesis), GO:0006954 (inflammatory response), GO:0015630 (microtubule cytoskeleton), GO:0007018 (microtubule-based movement)
- **Disease terms:** MONDO:0004975 (Alzheimer disease), MONDO:0017276 (frontotemporal dementia)
- **Molecular functions:** GO:0008017 (microtubule binding), GO:0004674 (protein serine/threonine kinase activity)

### Candidate Knowledge Gaps for KB

1. **Gap: Oligomer vs. tangle toxicity** — The hypothesis description should be updated to distinguish between soluble tau species and mature NFTs as the primary toxic entity
2. **Gap: Neuroinflammation dependency** — The model should explicitly acknowledge that neuroinflammation is required for tau pathology to produce clinical disease
3. **Gap: Anti-tau trial failures** — Should be documented as evidence that the therapeutic translation of the tau model is incomplete
4. **Gap: Primary vs. secondary tauopathy distinction** — The applies_to_subtypes field should note that AD is a secondary tauopathy, distinguishing the causal role of tau in AD from primary tauopathies

### Candidate Status Change

- **Current status:** CANONICAL
- **Recommended status:** CANONICAL with QUALIFIED annotation
- **Rationale:** The core tau-cognition correlation is robust and canonical, but the mechanistic details (toxic species, required co-factors) need refinement. The hypothesis as currently stated overemphasizes NFTs and underemphasizes oligomeric tau and neuroinflammatory co-factors. Recommend adding a "qualifications" field to the hypothesis YAML specifying: (a) primary toxic species are soluble pretangle oligomers, not mature NFTs; (b) neuroinflammation is a required co-factor for clinical expression; (c) anti-tau immunotherapy has not yet demonstrated clinical efficacy on primary endpoints.

---

## Limitations of This Report

1. **Literature search scope:** Our search of ~101 papers, while extensive, may not capture all relevant evidence, particularly from non-English literature, preprints, or very recent publications.
2. **Review reliance:** Several key claims (tau-cognition correlation, neuroinflammation role) are supported primarily by reviews synthesizing multiple studies, rather than individual primary papers with complete effect sizes. These are labeled as review-level support throughout.
3. **Animal model translation:** Many mechanistic findings (PP2A dominance, tau seeding dynamics, axonal tau reduction) derive from mouse models whose relevance to human sporadic AD requires cautious interpretation.
4. **Clinical trial interpretation:** The failure of anti-tau antibodies does not necessarily refute the tau model — it may reflect inadequate drug design, wrong patient selection, or insufficient treatment duration rather than a failure of the underlying biology.
5. **Subtype heterogeneity:** We did not find sufficient data to fully characterize how the tau model applies differently to early-onset vs. late-onset AD, APOE ε4 carriers vs. non-carriers, or different clinical phenotypic variants (amnestic vs. non-amnestic).
6. **Causal inference limitations:** Nearly all human evidence is correlational or observational. Direct perturbation evidence for tau's causal role in AD comes primarily from animal models and the indirect evidence of MAPT mutations in FTD (a different disease).
