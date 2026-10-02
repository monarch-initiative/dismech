---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T04:29:58.004990'
end_time: '2026-05-23T05:23:55.672740'
duration_seconds: 3237.67
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Huntington's Disease
  category: Genetic
  hypothesis_group_id: canonical_toxic_gain_of_function
  hypothesis_label: Toxic Gain-of-Function (Polyglutamine Aggregation)
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_toxic_gain_of_function\nhypothesis_label:\
    \ Toxic Gain-of-Function (Polyglutamine Aggregation)\nstatus: CANONICAL\ndescription:\
    \ |\n  The expanded polyglutamine tract in mutant huntingtin confers a toxic gain-of-function\
    \ through protein misfolding, oligomerization, and aggregation into inclusion\
    \ bodies. This is the widely accepted primary disease mechanism, with polyQ expansion\
    \ beyond the pathogenic threshold (~36 repeats) driving neurodegeneration predominantly\
    \ in the striatum.\nevidence:\n- reference: PMID:22180703\n  supports: SUPPORT\n\
    \  evidence_source: OTHER\n  snippet: It is caused by expansion of a polyglutamine\
    \ tract within the N-terminal domain of the Huntingtin\n    protein. The mutation\
    \ confers a toxic gain-of-function phenotype, resulting in neurodegeneration that\n\
    \    is most severe in the striatum.\n  explanation: Explicitly names the toxic\
    \ gain-of-function phenotype as the consequence of polyQ expansion\n    and links\
    \ it to striatal neurodegeneration.\n- reference: PMID:25336039\n  supports: SUPPORT\n\
    \  evidence_source: OTHER\n  snippet: The mutational expansion of polyglutamine\
    \ beyond a critical length produces a toxic gain of\n    function in huntingtin\
    \ and results in neuronal death. In the course of the disease, expanded huntingtin\n\
    \    is proteolyzed, becomes abnormally folded, and accumulates in oligomers,\
    \ fibrils, and microscopic\n    inclusions.\n  explanation: Directly states the\
    \ toxic gain-of-function framing and details the aggregation cascade\n    from\
    \ proteolysis through misfolding to inclusion body formation."
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
citation_count: 44
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Huntington's Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_toxic_gain_of_function
- **Hypothesis Label:** Toxic Gain-of-Function (Polyglutamine Aggregation)
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_toxic_gain_of_function
hypothesis_label: Toxic Gain-of-Function (Polyglutamine Aggregation)
status: CANONICAL
description: |
  The expanded polyglutamine tract in mutant huntingtin confers a toxic gain-of-function through protein misfolding, oligomerization, and aggregation into inclusion bodies. This is the widely accepted primary disease mechanism, with polyQ expansion beyond the pathogenic threshold (~36 repeats) driving neurodegeneration predominantly in the striatum.
evidence:
- reference: PMID:22180703
  supports: SUPPORT
  evidence_source: OTHER
  snippet: It is caused by expansion of a polyglutamine tract within the N-terminal domain of the Huntingtin
    protein. The mutation confers a toxic gain-of-function phenotype, resulting in neurodegeneration that
    is most severe in the striatum.
  explanation: Explicitly names the toxic gain-of-function phenotype as the consequence of polyQ expansion
    and links it to striatal neurodegeneration.
- reference: PMID:25336039
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The mutational expansion of polyglutamine beyond a critical length produces a toxic gain of
    function in huntingtin and results in neuronal death. In the course of the disease, expanded huntingtin
    is proteolyzed, becomes abnormally folded, and accumulates in oligomers, fibrils, and microscopic
    inclusions.
  explanation: Directly states the toxic gain-of-function framing and details the aggregation cascade
    from proteolysis through misfolding to inclusion body formation.
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

# Mechanistic Hypothesis Evaluation: Toxic Gain-of-Function (Polyglutamine Aggregation) in Huntington's Disease

**Hypothesis ID:** canonical_toxic_gain_of_function
**Status in KB:** CANONICAL
**Date:** 2026-05-23

---

## Executive Judgment

**Verdict: SUPPORTED — with significant qualifications requiring model refinement**

The toxic gain-of-function hypothesis for Huntington's disease (HD), positing that expanded polyglutamine (polyQ) tracts in mutant huntingtin (mHTT) confer toxicity through protein misfolding, oligomerization, and aggregation, is the most extensively validated mechanistic model in HD research and should retain its **CANONICAL** status. Convergent evidence from human genetics, neuropathology, transgenic animal models, cell biology, and therapeutic studies robustly supports the core claim that polyQ expansion beyond the pathogenic threshold (~36 repeats) drives neurodegeneration through a gain of toxic function.

However, the hypothesis as traditionally framed is incomplete and requires three critical qualifications. First, **somatic CAG repeat instability**—driven by mismatch repair (MMR) genes MSH3, PMS1, and others—has emerged as a major upstream amplifier that expands repeats far beyond the inherited length in vulnerable striatal neurons, meaning that the inherited repeat length is a necessary but not sufficient determinant of toxicity. Second, **loss of normal huntingtin function** operates as a parallel contributor, not merely a bystander, with mHTT aggregates sequestering wild-type HTT and other essential proteins. Third, **RNA-level toxicity** from expanded CAG repeats represents an additional pathogenic layer that is independent of protein aggregation. The identity of the primary toxic species (soluble oligomers vs. insoluble inclusions), the precise molecular basis of selective striatal vulnerability, and the disappointing results of first-generation HTT-lowering clinical trials all represent unresolved gaps that challenge a simplistic gain-of-function narrative.

---

## Summary

Huntington's disease is caused by an expanded CAG trinucleotide repeat in exon 1 of the *HTT* gene, encoding an elongated polyglutamine tract in the huntingtin protein. The toxic gain-of-function hypothesis—the dominant explanatory framework for HD pathogenesis—proposes that this expanded polyQ tract causes mHTT to misfold, form toxic oligomeric intermediates, and aggregate into inclusion bodies, triggering neuronal dysfunction and death predominantly in striatal medium spiny neurons (MSNs). This report evaluates the hypothesis against 81 primary research articles and reviews, cataloguing supporting evidence, qualifying findings, competing mechanistic models, and explicit knowledge gaps.

The evidence supporting the core hypothesis is extensive: the inverse correlation between CAG repeat length and age of onset; faithful disease recapitulation in transgenic models expressing mutant N-terminal HTT fragments; the universal presence of mHTT aggregates in patient brains and model systems; and the therapeutic benefit of enhancing mHTT clearance through autophagy. However, recent genome-wide association studies (GWAS) have shifted the field's attention toward somatic CAG repeat instability as a critical disease modifier, with MMR gene variants (particularly *MSH3*) explaining a substantial portion of onset variability beyond inherited repeat length. Additionally, the dual contribution of gain-of-toxic-function and loss-of-normal-function, transcriptional dysregulation as a major downstream effector, post-translational modifications as critical modulators of mHTT toxicity, and RNA-mediated toxicity from expanded CAG transcripts all demand a more nuanced, multi-layered mechanistic model than the original hypothesis provides.

---

## Key Findings

### Finding 1: Toxic Gain-of-Function Is the Canonical and Well-Supported Primary HD Mechanism

Multiple independent lines of evidence confirm that the expanded polyQ tract in mHTT confers a toxic gain-of-function. Genetically, the inverse correlation between CAG repeat length and age of motor onset is among the most robust genotype-phenotype relationships in neurogenetics. Transgenic models expressing only the mutant N-terminal fragment (e.g., R6/2, BAC226Q) faithfully recapitulate progressive motor deficits, striatal atrophy, neuronal loss, and widespread huntingtin inclusions ([PMID: 35023827](https://pubmed.ncbi.nlm.nih.gov/35023827/)). The BAC226Q model, expressing full-length human HTT with ~226 CAG-CAA repeats, shows age-dependent and progressive HD-like phenotypes including psychiatric and cognitive changes at 2 months, motor deficits from 3–4 months, and significant brain atrophy specific to striatum and cortex with widespread inclusions by 11 months.

At the molecular level, mHTT is proteolyzed into N-terminal fragments that misfold, form oligomers, and accumulate into fibrils and microscopic inclusions ([PMID: 25336039](https://pubmed.ncbi.nlm.nih.gov/25336039/)). These aggregates perturb nuclear gene transcription, RNA splicing and transport, and cellular membrane dynamics ([PMID: 29904030](https://pubmed.ncbi.nlm.nih.gov/29904030/)). Therapeutically, autophagy-enhancing agents that promote mHTT clearance—including rapamycin ([PMID: 37823007](https://pubmed.ncbi.nlm.nih.gov/37823007/)) and rilmenidine ([PMID: 20190273](https://pubmed.ncbi.nlm.nih.gov/20190273/))—reduce aggregate burden and attenuate disease phenotypes in HD models, providing functional validation that the mutant protein is the proximal cause of toxicity.

The hypothesis is further supported by the observation that the mutation's primary consequence is a toxic gain-of-function, although this may be modified by certain normal activities that are impaired by the mutation ([PMID: 18466116](https://pubmed.ncbi.nlm.nih.gov/18466116/)). This framing—gain-of-function as primary, with loss-of-function as modifier—represents the current consensus, though the relative balance remains debated.

### Finding 2: Somatic CAG Repeat Instability Is an Emerging Critical Modifier of HD Pathogenesis

Perhaps the most transformative recent development in HD research is the recognition that somatic CAG repeat instability is not merely a curiosity but a key driver of disease onset and progression. GWAS modifier studies have identified DNA mismatch repair genes—*MSH3*, *PMS1*, *MLH1*, *MSH2*, and *FAN1*—as top modifiers of HD age of onset ([PMID: 39801710](https://pubmed.ncbi.nlm.nih.gov/39801710/); [PMID: 32898862](https://pubmed.ncbi.nlm.nih.gov/32898862/)). These findings demonstrate that it is not simply the inherited CAG length but its progressive somatic expansion in vulnerable neurons that determines disease timing.

In HD knock-in mice, *Msh3* knockout eliminates striatal CAG expansions and rescues neuronal phenotypes, with somatic expansions in striatal MSNs proceeding at approximately 8.8 repeats per month ([PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)). Critically, *Msh3* deficiency prevents mHTT aggregation by keeping somatic MSN CAG length below a pathogenic threshold of ~150 repeats, demonstrating a direct causal link between somatic expansion, aggregation threshold, and neuronal pathology. MSN-specific deletion of *Msh2* was sufficient to eliminate the vast majority of striatal HTT CAG expansions and dramatically inhibited the development of intranuclear huntingtin inclusions ([PMID: 22970194](https://pubmed.ncbi.nlm.nih.gov/22970194/)).

The dynamics of somatic instability differ by tissue: striatal expansions produce broadly distributed unstable repeats, while liver expansions maintain a distinct population of unstable repeats with more uniform size gains ([PMID: 21897851](https://pubmed.ncbi.nlm.nih.gov/21897851/)). Mouse strain background also significantly influences instability, with *MSH3* polymorphisms and protein levels directly affecting CAG repeat dynamics ([PMID: 23468640](https://pubmed.ncbi.nlm.nih.gov/23468640/)). Therapeutic silencing of *MSH3* using di-valent siRNA effectively blocks somatic CAG expansion in the striatum of HD mouse models without affecting other MMR functions ([PMID: 37177784](https://pubmed.ncbi.nlm.nih.gov/37177784/)).

This body of evidence reframes the toxic gain-of-function hypothesis: the inherited polyQ expansion sets the stage, but somatic instability amplifies the mutation in the cells most vulnerable to its effects, creating a feedforward loop that accelerates pathogenesis.

### Finding 3: Gain-of-Function and Loss-of-Function Are Not Mutually Exclusive

HD pathogenesis involves both gain of toxic function and loss of normal huntingtin function, and these mechanisms are intertwined rather than independent. mHTT aggregates sequester wild-type HTT and other essential cellular proteins, compounding the loss-of-function component ([PMID: 31203656](https://pubmed.ncbi.nlm.nih.gov/31203656/)). Normal huntingtin plays critical roles in vesicular transport, transcriptional regulation, BDNF trafficking, and anti-apoptotic signaling; all of these are impaired when HTT is mutated or sequestered.

The debate over the relative contributions of gain- versus loss-of-function remains active ([PMID: 22932724](https://pubmed.ncbi.nlm.nih.gov/22932724/)). Mutant huntingtin results in both the loss of all the functions of normal huntingtin and the genesis of abnormal interactions due to the polyQ expansion ([PMID: 31223078](https://pubmed.ncbi.nlm.nih.gov/31223078/)). The involvement of both gain of new toxic functions and the loss of beneficial properties has been independently confirmed ([PMID: 17041811](https://pubmed.ncbi.nlm.nih.gov/17041811/)). This dual mechanism has important therapeutic implications: HTT-lowering strategies that reduce both mutant and wild-type HTT (such as non-allele-selective ASOs) may inadvertently exacerbate loss-of-function pathology.

### Finding 4: Transcriptional Dysregulation Is a Major Downstream Pathogenic Mechanism

N-terminal mHTT fragments accumulate in the nucleus and directly inhibit transcription by binding to Sp1, TFIID, TFIIF, and other components of the core transcription apparatus in a polyQ-dependent manner ([PMID: 16377565](https://pubmed.ncbi.nlm.nih.gov/16377565/)). Shorter N-terminal fragments are more prone to misfolding and more potent at transcriptional inhibition, with effects reversible by the molecular chaperone Hsp40 ([PMID: 17012230](https://pubmed.ncbi.nlm.nih.gov/17012230/)).

Cell-type-specific transcriptomics has revealed that in striatal spiny projection neurons—the most vulnerable cell type in HD—mHTT leads to mitochondrial RNA release and concomitant upregulation of innate immune signaling ([PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/)). This finding connects mHTT toxicity to neuroinflammation through a novel mechanism involving mitochondrial-derived innate immunogens. Additionally, the striatal-enriched transcription factor Bcl11b (CTIP2) is significantly decreased in HD cells, mouse models, and human subjects, and its overexpression attenuates mHTT toxicity in cultured striatal neurons ([PMID: 18595722](https://pubmed.ncbi.nlm.nih.gov/18595722/)). The enrichment of certain transcription factors and proteins (NR2D, PSD-95, HAP1) in nNOS-positive interneurons—which are selectively spared in HD—suggests that transcriptional profiles contribute to the differential vulnerability of neuronal subtypes ([PMID: 15548548](https://pubmed.ncbi.nlm.nih.gov/15548548/)).

The transcriptional dysregulation extends beyond coding genes to non-coding RNAs, including the long non-coding RNA NEAT1, which is elevated in HD brains in an mHTT-dependent manner and appears to play a protective role ([PMID: 30239724](https://pubmed.ncbi.nlm.nih.gov/30239724/)). REST/NRSF-mediated dysregulation of neuronal gene expression, including BDNF, adds another layer to the transcriptional cascade ([PMID: 19909260](https://pubmed.ncbi.nlm.nih.gov/19909260/)).

### Finding 5: RNA Toxicity from Expanded CAG Repeats Is an Emerging Parallel Mechanism

Independent of protein-level effects, expanded CAG repeats in HTT mRNA can directly cause toxicity. Mechanisms include aberrant subcellular localization of expanded CAG transcripts, sequestration of RNA-binding proteins disrupting alternative splicing, and aberrant biogenesis of small CAG repeated RNAs (sCAGs) causing gene silencing perturbations ([PMID: 27529325](https://pubmed.ncbi.nlm.nih.gov/27529325/)). Repeat-associated non-AUG (RAN) translation from expanded repeats can also produce additional toxic peptides beyond the canonical polyQ-containing protein. This RNA-level toxic gain-of-function represents a pathogenic pathway that is mechanistically distinct from, but potentially synergistic with, the protein aggregation hypothesis. The broader context of repeat expansion disorders affecting both coding and non-coding regions of the transcriptome suggests shared RNA-mediated mechanisms across diseases ([PMID: 33172304](https://pubmed.ncbi.nlm.nih.gov/33172304/)).

### Finding 6: Post-Translational Modifications Critically Modulate mHTT Aggregation and Toxicity

Post-translational modifications (PTMs) including phosphorylation, ubiquitination, acetylation, and SUMOylation play pivotal roles in modulating mHTT's conformation, aggregation propensity, subcellular localization, and degradation pathways ([PMID: 41303392](https://pubmed.ncbi.nlm.nih.gov/41303392/)). IKK-mediated phosphorylation of HTT enhances its clearance by the proteasome and lysosome, with phosphorylation regulating additional modifications including ubiquitination, SUMOylation, and acetylation ([PMID: 20026656](https://pubmed.ncbi.nlm.nih.gov/20026656/)). Threonine 3 in the N17 domain has been identified as a major phosphorylation site regulated by IKKβ ([PMID: 26106822](https://pubmed.ncbi.nlm.nih.gov/26106822/)).

SUMOylation has particularly interesting effects: it inhibits fibril formation while promoting larger, amorphous aggregate species, and prevents HTT binding and aggregation on lipid membranes ([PMID: 31880908](https://pubmed.ncbi.nlm.nih.gov/31880908/)). This demonstrates that the aggregation pathway is not a simple linear process but is dynamically regulated by PTMs, with different modification states potentially producing different toxic species. The age-related decline in PTM-mediated clearance mechanisms may explain the progressive nature of HD and is consistent with the gain-of-function model's prediction that accumulation of mHTT over time drives pathology.

---

## Mechanistic Causal Chain

The following chain describes the sequence from upstream trigger to clinical manifestation, with annotations on evidence strength:

```
UPSTREAM TRIGGER
┌─────────────────────────────────────────────────────────────────┐
│  Inherited CAG expansion in HTT exon 1 (>36 repeats)           │
│  [STRONG: definitive human genetic evidence]                    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  Somatic CAG repeat expansion in vulnerable neurons (MSNs)      │
│  Driven by MMR machinery (MSH3, MSH2, PMS1, MLH1)              │
│  Amplifies repeats to ~150+ in striatum over decades            │
│  [STRONG: GWAS + mouse genetics + interventional evidence]      │
└─────────────────────┬───────────────────────────────────────────┘
                      │
            ┌─────────┴──────────┐
            ▼                    ▼
┌────────────────────┐  ┌────────────────────────────────────────┐
│  RNA-LEVEL TOXICITY│  │  PROTEIN-LEVEL TOXICITY                │
│  - sCAG biogenesis │  │  Proteolytic cleavage → N-terminal     │
│  - RBP sequestrat. │  │  fragments with expanded polyQ          │
│  - RAN translation │  │  [STRONG: biochemistry + cell biology]  │
│  [EMERGING]        │  └─────────────────┬──────────────────────┘
└────────────────────┘                    │
                                          ▼
                              ┌───────────────────────┐
                              │  Misfolding &          │
                              │  Oligomerization       │
                              │  [STRONG: biophysics]  │
                              └─────────┬─────────────┘
                                        │
                    ┌───────────────────┬┴───────────────────┐
                    ▼                   ▼                     ▼
          ┌─────────────────┐ ┌──────────────────┐ ┌───────────────┐
          │ Nuclear accum.  │ │ Cytoplasmic      │ │ Sequestration │
          │ → Transcription │ │ aggregation      │ │ of WT HTT &   │
          │   dysregulation │ │ → Proteostasis   │ │ other proteins│
          │   (Sp1, TFIID,  │ │   impairment     │ │ → Loss of     │
          │    REST, Bcl11b)│ │ → Axonal         │ │   function    │
          │ [STRONG]        │ │   transport block│ │ [MODERATE]    │
          └────────┬────────┘ │ → Mitochondrial  │ └───────┬───────┘
                   │          │   dysfunction    │         │
                   │          │ [STRONG]         │         │
                   │          └────────┬─────────┘         │
                   │                   │                   │
                   └───────────┬───────┴───────────────────┘
                               ▼
                   ┌───────────────────────┐
                   │  DOWNSTREAM EFFECTS    │
                   │  - Excitotoxicity      │
                   │  - Neuroinflammation   │
                   │  - Mitochondrial RNA   │
                   │    release → innate    │
                   │    immune activation   │
                   │  - Synaptic dysfunction│
                   │  - Apoptosis/necrosis  │
                   │  [MODERATE-STRONG]     │
                   └──────────┬────────────┘
                              ▼
                   ┌───────────────────────┐
                   │  CLINICAL MANIFESTATION│
                   │  - Striatal atrophy    │
                   │  - MSN loss            │
                   │  - Chorea, cognitive   │
                   │    decline, psychiatric│
                   │    symptoms            │
                   │  [STRONG: clinical]    │
                   └───────────────────────┘
```

**Strong links:** Inherited CAG expansion → somatic amplification → protein misfolding → aggregation → transcriptional dysregulation → neuronal dysfunction → clinical phenotype.

**Moderate links:** Relative contributions of different aggregate species (oligomers vs. fibrils vs. inclusions); precise mechanism of selective MSN vulnerability; contribution of RNA toxicity relative to protein toxicity.

**Inferred/weak links:** Why striatal MSNs are more susceptible to somatic expansion than other neuronal populations; how PTM regulation fails with age; the precise mechanism by which inclusions may be either toxic or protective.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 22180703](https://pubmed.ncbi.nlm.nih.gov/22180703/) | Review | Supports | PolyQ confers toxic gain-of-function | Explicitly names toxic GoF as consequence of polyQ expansion | General HD | High (review-level) |
| [PMID: 25336039](https://pubmed.ncbi.nlm.nih.gov/25336039/) | Review | Supports | Aggregation cascade | Details proteolysis → misfolding → oligomers → fibrils → inclusions | General HD | High (review-level) |
| [PMID: 29904030](https://pubmed.ncbi.nlm.nih.gov/29904030/) | In vitro / review | Supports | mHTT disrupts multiple cellular processes | Aggregates perturb transcription, splicing, membrane dynamics | General HD | High |
| [PMID: 18466116](https://pubmed.ncbi.nlm.nih.gov/18466116/) | Review | Qualifies | GoF is primary, LoF modifies | Primary consequence is toxic GoF, modified by impaired normal activities | General HD | High (review-level) |
| [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/) | Model organism | Qualifies | Somatic expansion drives pathogenesis | MSH3/PMS1 drive fast somatic expansion; deficiency rescues phenotypes | HD mouse model | Very High |
| [PMID: 22970194](https://pubmed.ncbi.nlm.nih.gov/22970194/) | Model organism | Qualifies | Somatic expansion required for mHTT phenotypes | MSN-specific Msh2 deletion eliminates CAG expansions and inhibits inclusions | HdhQ111 mice | Very High |
| [PMID: 38393920](https://pubmed.ncbi.nlm.nih.gov/38393920/) | Model organism | Qualifies | Somatic instability modifies onset | Somatic instability of HTT CAG modifies age-at-onset | Transgenic sheep | High |
| [PMID: 23468640](https://pubmed.ncbi.nlm.nih.gov/23468640/) | Model organism | Qualifies | MSH3 determines CAG stability | MSH3 polymorphisms and protein levels affect CAG instability | R6/1 mice | High |
| [PMID: 37177784](https://pubmed.ncbi.nlm.nih.gov/37177784/) | Model organism | Qualifies | MSH3 silencing blocks expansion | Di-valent siRNA silencing of Msh3 blocks striatal CAG expansion | HD mice | Very High |
| [PMID: 31203656](https://pubmed.ncbi.nlm.nih.gov/31203656/) | In vitro | Qualifies | Both GoF and LoF contribute | Misfolded aggregates cause GoF; sequestration causes LoF | Structural studies | High |
| [PMID: 22932724](https://pubmed.ncbi.nlm.nih.gov/22932724/) | Review | Qualifies | GoF vs. LoF debate unresolved | Whether mutation leads to GoF or LoF is still highly controversial | General HD | Moderate |
| [PMID: 16377565](https://pubmed.ncbi.nlm.nih.gov/16377565/) | In vitro | Supports | Transcriptional inhibition by mHTT | Sp1, TFIID, TFIIF are direct targets inhibited in polyQ-dependent manner | In vitro transcription | Very High |
| [PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/) | Model organism | Supports | mHTT causes cell-type-specific transcriptomic changes | mtRNA release and innate immune activation in spiny projection neurons | HD mouse striatum | High |
| [PMID: 18595722](https://pubmed.ncbi.nlm.nih.gov/18595722/) | Model organism + human | Supports | Striatal transcription factors depleted | Bcl11b decreased in HD; overexpression attenuates mHTT toxicity | HD cells, mice, humans | High |
| [PMID: 27529325](https://pubmed.ncbi.nlm.nih.gov/27529325/) | Review + in vitro | Competing | RNA-level toxic GoF | Expanded CAG in HTT mRNA induces toxicity through gene expression perturbations | General HD | Moderate |
| [PMID: 41303392](https://pubmed.ncbi.nlm.nih.gov/41303392/) | Review | Qualifies | PTMs modulate mHTT toxicity | Phosphorylation, ubiquitination, acetylation, SUMOylation regulate aggregation | General HD | High (review-level) |
| [PMID: 20026656](https://pubmed.ncbi.nlm.nih.gov/20026656/) | In vitro + model organism | Supports | Phosphorylation regulates mHTT clearance | IKK phosphorylation enhances HTT clearance by proteasome and lysosome | Cell models | High |
| [PMID: 31880908](https://pubmed.ncbi.nlm.nih.gov/31880908/) | In vitro | Qualifies | SUMOylation redirects aggregation | SUMOylation inhibits fibrils, promotes amorphous aggregates, prevents membrane binding | Biophysical studies | High |
| [PMID: 35023827](https://pubmed.ncbi.nlm.nih.gov/35023827/) | Model organism | Supports | Full-length mHTT recapitulates HD | BAC226Q mice show progressive striatal atrophy, neuronal death, inclusions | BAC mouse model | Very High |
| [PMID: 20190273](https://pubmed.ncbi.nlm.nih.gov/20190273/) | Model organism | Supports | Autophagy-enhanced mHTT clearance is therapeutic | Rilmenidine induces autophagy, reduces mHTT levels, attenuates disease signs | HD mouse model | High |
| [PMID: 24022020](https://pubmed.ncbi.nlm.nih.gov/24022020/) | Model organism (Drosophila) | Supports | Aggregates form rapidly and block transport | Pathogenic HTT forms insoluble aggregates within hours; blocks axonal transport | HD fly model | High |
| [PMID: 40330856](https://pubmed.ncbi.nlm.nih.gov/40330856/) | Model organism | Supports | Reducing somatic expansion is therapeutic | Interventionally diminishing somatic expansions modifies disease course | HD mouse models | Very High |
| [PMID: 32463364](https://pubmed.ncbi.nlm.nih.gov/32463364/) | Model organism (Drosophila) | Supports | Prion-like spreading of mHTT | mHTT aggregates transfer across neuronal synapses via phagocytic glia | HD fly model | Moderate |

---

## Alternative and Competing Mechanistic Models

### 1. Somatic CAG Repeat Instability Model
**Relationship to seed hypothesis: Upstream cause / critical modifier**

This model posits that the inherited CAG repeat is necessary but not sufficient for disease, and that progressive somatic expansion in vulnerable neurons—driven by MMR machinery—is the rate-limiting step that determines disease onset. Evidence from GWAS modifier studies, MSH3 knockout experiments, and interventional siRNA studies strongly supports this model. It does not replace the toxic gain-of-function hypothesis but reframes it: the polyQ toxicity occurs, but the effective repeat length in neurons is determined by somatic dynamics, not inheritance alone. This model has the strongest support of any qualifier and is rapidly becoming integrated into the canonical framework.

### 2. Loss-of-Function / Haploinsufficiency Model
**Relationship to seed hypothesis: Parallel mechanism**

Normal huntingtin plays essential roles in vesicular transport, BDNF trafficking, transcriptional regulation, and anti-apoptotic signaling. The loss-of-function model proposes that mHTT impairs these functions through dominant-negative effects and through sequestration of wild-type HTT into aggregates. While pure loss-of-function is unlikely to be the primary mechanism (heterozygous HTT knockout does not cause HD-like disease), it operates as an important parallel pathway that compounds the gain-of-function toxicity. This has critical implications for non-allele-selective HTT-lowering therapies.

### 3. RNA Toxicity Model
**Relationship to seed hypothesis: Parallel mechanism**

Expanded CAG repeats in HTT mRNA can cause toxicity independent of protein translation, through mechanisms including RNA foci formation, sequestration of RNA-binding proteins, aberrant generation of small CAG RNAs, and RAN translation producing additional toxic peptides. This model is still emerging and the relative contribution of RNA-level versus protein-level toxicity in HD patients is unknown, but it represents a mechanistically distinct pathway that could contribute to pathogenesis.

### 4. Excitotoxicity Model
**Relationship to seed hypothesis: Downstream consequence**

Enhanced sensitivity of striatal MSNs to glutamate-mediated excitotoxicity, particularly through extrasynaptic GluN2B-containing NMDA receptors, has been extensively documented in HD models ([PMID: 33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/); [PMID: 40778304](https://pubmed.ncbi.nlm.nih.gov/40778304/)). This is best understood as a downstream consequence of mHTT-induced synaptic dysfunction rather than an independent cause, though it may contribute to the selective vulnerability of MSNs given their glutamatergic inputs from cortex.

### 5. Mitochondrial Dysfunction Model
**Relationship to seed hypothesis: Downstream consequence**

mHTT disrupts mitochondrial dynamics, membrane potential, and respiratory chain function, leading to energy deficits and oxidative stress ([PMID: 27514446](https://pubmed.ncbi.nlm.nih.gov/27514446/)). Mitochondrial RNA release into the cytoplasm triggers innate immune activation in MSNs ([PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/)). These are likely downstream effects of mHTT aggregation rather than independent initiating mechanisms.

### 6. Non-Cell-Autonomous / Glial Dysfunction Model
**Relationship to seed hypothesis: Parallel mechanism**

mHTT expression in astrocytes, microglia, and oligodendrocytes contributes to neuroinflammation and MSN dysfunction through non-cell-autonomous mechanisms ([PMID: 31529216](https://pubmed.ncbi.nlm.nih.gov/31529216/); [PMID: 41495356](https://pubmed.ncbi.nlm.nih.gov/41495356/)). Oligodendroglial mHTT expression alone can drive neuroinflammatory changes, and phagocytic glia may facilitate prion-like spreading of mHTT aggregates across synapses ([PMID: 32463364](https://pubmed.ncbi.nlm.nih.gov/32463364/)). This represents a parallel mechanism that amplifies cell-autonomous toxicity.

---

## Knowledge Gaps

### Gap 1: Identity of the Primary Toxic Species
**Scope:** Whether soluble oligomers, protofibrils, mature fibrils, or inclusion bodies are the primary drivers of toxicity.
**Why it matters:** Therapeutic strategies targeting aggregation depend on knowing which species to reduce. Inclusion bodies may actually be protective by sequestering toxic oligomers.
**What was checked:** Multiple in vitro and model organism studies; SUMOylation studies showing different aggregation pathways ([PMID: 31880908](https://pubmed.ncbi.nlm.nih.gov/31880908/)).
**Resolution needed:** Longitudinal imaging of aggregate species in living neurons correlated with functional outcomes; structure-specific antibodies in patient tissue.

### Gap 2: Molecular Basis of Selective Striatal MSN Vulnerability
**Scope:** Why MSNs in the caudate-putamen are preferentially affected despite ubiquitous mHTT expression.
**Why it matters:** Understanding selective vulnerability could reveal cell-type-specific therapeutic targets.
**What was checked:** Transcriptional profiling showing MSN-specific gene expression changes; excitotoxicity studies; somatic expansion rates in different cell types; Bcl11b depletion; DARPP-32 loss.
**Resolution needed:** Comprehensive single-cell multi-omic profiling of human HD striatum at multiple disease stages; causal perturbation studies testing specific vulnerability factors.

### Gap 3: Relative Contribution of RNA Toxicity vs. Protein Toxicity In Vivo
**Scope:** The proportion of HD pathology attributable to RNA-mediated versus protein-mediated mechanisms.
**Why it matters:** If RNA toxicity is substantial, HTT-lowering strategies targeting only the protein would miss a significant pathogenic pathway.
**What was checked:** In vitro studies of CAG RNA toxicity ([PMID: 27529325](https://pubmed.ncbi.nlm.nih.gov/27529325/)); no direct in vivo quantification of relative contributions found.
**Resolution needed:** Engineered models separating RNA and protein effects (e.g., codon-modified repeats that encode polyQ without CAG RNA structure).

### Gap 4: Why First-Generation HTT-Lowering Trials Failed
**Scope:** Clinical trials of ASOs Tominersen (non-allele-selective) and WVE-120101/WVE-120102 (allele-selective) failed to show efficacy.
**Why it matters:** If the toxic gain-of-function is the primary mechanism, reducing mHTT should be therapeutic.
**What was checked:** Clinical trial landscape reviewed ([PMID: 38861215](https://pubmed.ncbi.nlm.nih.gov/38861215/)).
**Resolution needed:** Determine whether failure was due to insufficient CNS exposure, wrong target population, concurrent loss-of-function from lowering WT HTT, wrong disease stage, or a fundamental limitation of the gain-of-function model.

### Gap 5: Mechanism Linking Somatic Expansion to Aggregation Threshold
**Scope:** The precise CAG length threshold at which somatic expansion triggers aggregation in human neurons, and whether this varies by cell type.
**Why it matters:** Defining the therapeutic window for somatic expansion-blocking treatments.
**What was checked:** Mouse data suggesting ~150 repeats as threshold in MSNs ([PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)); no human data on cell-type-specific thresholds found.
**Resolution needed:** Long-read sequencing of individual neurons from HD patient brains correlated with pathological markers; human iPSC-derived neuron studies.

### Gap 6: Absence of Large-Scale Longitudinal Biomarker Studies Linking Somatic Instability to Clinical Progression
**Scope:** No large prospective cohort studies directly measuring somatic instability in peripheral tissues and correlating with CNS disease progression.
**Why it matters:** Somatic instability in blood may serve as a pharmacodynamic biomarker for interventions targeting MMR-mediated expansion.
**What was checked:** TRACE tool development for measuring somatic instability ([PMID: 42101426](https://pubmed.ncbi.nlm.nih.gov/42101426/)); modifier GWAS using age-of-onset as proxy.
**Resolution needed:** Longitudinal studies using standardized somatic instability metrics (e.g., expansion index from TRACE) in blood correlated with MRI and clinical outcomes.

### Gap 7: Role of Cis-Acting Sequence Modifiers
**Scope:** CAA interruptions within the CAG repeat tract significantly modulate somatic instability and HD pathology.
**Why it matters:** Current genetic diagnostics may underestimate or overestimate pathogenic potential depending on sequence composition.
**What was checked:** Evidence that loss/duplication of the penultimate CAA significantly modulates instability; four internal CAA interruptions completely abolish CAG instability and reverse HD phenotypes ([PMID: 41389205](https://pubmed.ncbi.nlm.nih.gov/41389205/)); diagnostic challenges reviewed ([PMID: 41841481](https://pubmed.ncbi.nlm.nih.gov/41841481/)).
**Resolution needed:** Long-read sequencing-based diagnostic standards that capture repeat composition, not just total length.

---

## Discriminating Tests

### Test 1: Codon-Modified Repeat Models to Dissect RNA vs. Protein Toxicity
**Design:** Generate knock-in mice with CAG repeats replaced by CAA-encoding (polyQ-producing but non-CAG RNA structure) repeats at the same length.
**Expected result:** If protein toxicity is dominant, CAA-encoded polyQ should produce equivalent disease. If RNA toxicity contributes significantly, disease should be attenuated.
**Biomarkers:** Motor phenotype, striatal atrophy, aggregate burden, transcriptomic changes.

### Test 2: Allele-Selective HTT Lowering with Somatic Instability Monitoring
**Design:** Combine allele-selective ASO treatment (targeting only mutant HTT to avoid LoF) with concurrent somatic instability measurements in accessible tissues.
**Expected result:** If toxic GoF is the primary driver, allele-selective lowering should show clinical benefit. If somatic instability is the rate-limiting step, instability-blocking treatments may be more effective.
**Patient stratification:** Stratify by inherited CAG length, SNP-defined MMR modifier haplotypes, and baseline somatic instability metrics.

### Test 3: MSH3 Inhibition Clinical Trial
**Design:** Phase I/II trial of MSH3-targeting therapies (ASO or siRNA) in premanifest HD carriers.
**Expected result:** Reduction in peripheral somatic instability metrics; delayed onset of motor symptoms by NfL and mHTT CSF biomarkers.
**Model system:** Already validated preclinically ([PMID: 37177784](https://pubmed.ncbi.nlm.nih.gov/37177784/); [PMID: 40330856](https://pubmed.ncbi.nlm.nih.gov/40330856/)).

### Test 4: Single-Cell Multi-Omic Profiling of Human HD Striatum
**Design:** Single-nucleus RNA-seq + ATAC-seq + long-read DNA sequencing of individual neurons from HD patient brains across Vonsattel grades.
**Expected result:** Direct correlation between somatic repeat length, transcriptomic dysregulation, and cell death markers at single-cell resolution.
**Key readout:** Whether neurons with the longest somatic expansions show the most severe transcriptomic disruption, and whether this exceeds a sharp threshold.

### Test 5: Longitudinal Imaging of Aggregate Species In Vivo
**Design:** Use aggregate species-specific PET ligands or CSF biomarkers in HD patients across disease stages.
**Expected result:** Determine whether oligomeric species, fibrillar aggregates, or total mHTT burden best predicts clinical progression.
**Patient stratification:** Premanifest carriers, early manifest HD, advanced HD.

---

## Curation Leads

*The following are candidate updates for the Knowledge Base, requiring curator verification:*

### Candidate Evidence References

1. **[PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)** — Key evidence for somatic instability as disease driver. Snippet: *"Msh3 deficiency prevents mHtt aggregation by keeping somatic MSN CAG length below 150. Importantly, Msh3 deficiency corrects synaptic, astrocytic, and locomotor defects in HD mice."* → Candidate SUPPORT evidence for a new "somatic instability" hypothesis node; also QUALIFIES the canonical GoF hypothesis by demonstrating that aggregation depends on somatic expansion exceeding a threshold.

2. **[PMID: 40330856](https://pubmed.ncbi.nlm.nih.gov/40330856/)** — Interventional evidence that reducing somatic expansion modifies disease. → Candidate SUPPORT for somatic instability hypothesis; strengthens causal inference.

3. **[PMID: 41389205](https://pubmed.ncbi.nlm.nih.gov/41389205/)** — CAA interruptions abolish instability and reverse phenotypes. → Candidate evidence for cis-modifier subnode; important for diagnostic implications.

4. **[PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/)** — Mitochondrial RNA release triggers innate immune activation in MSNs. Snippet: *"In striatal spiny projection neurons, the most vulnerable cell type in HD, we observe a release of mitochondrial RNA (mtRNA)...and a concomitant upregulation of innate immune signaling."* → Candidate novel downstream mechanism node linking mHTT to neuroinflammation.

5. **[PMID: 27529325](https://pubmed.ncbi.nlm.nih.gov/27529325/)** — RNA toxic gain-of-function. Snippet: *"the most recent advances have revealed novel pathogenic pathways directly dependent on an RNA toxic gain-of-function."* → Candidate for new parallel mechanism hypothesis node.

### Candidate Pathophysiology Nodes/Edges

- **New node:** "Somatic CAG repeat instability" (upstream modifier of polyQ aggregation)
  - Edge: MMR genes (MSH3, PMS1, MSH2, MLH1, FAN1) → somatic CAG expansion → threshold-dependent mHTT aggregation
- **New node:** "RNA toxicity from expanded CAG repeats" (parallel mechanism)
  - Edge: Expanded CAG mRNA → sCAG biogenesis + RBP sequestration + RAN translation → gene expression perturbation + toxic peptide production
- **Refinement of existing node:** "Transcriptional dysregulation" should include mtRNA release → innate immune signaling as a distinct sub-mechanism

### Candidate Ontology Terms

- **Cell types:** Medium spiny neurons (CL:1001474), striatal interneurons (nNOS+), cortical pyramidal neurons (layer V/VI), oligodendrocytes, astrocytes, microglia
- **Biological processes:** GO:0006298 (mismatch repair), GO:0006986 (response to unfolded protein), GO:0006954 (inflammatory response), GO:0016236 (macroautophagy)
- **Disease ontology:** DOID:12858 (Huntington's disease)

### Candidate Status Assessment

- **Toxic GoF hypothesis status:** Maintain **CANONICAL**, but add mandatory qualifier noting somatic instability as critical upstream modifier
- **Candidate new hypothesis:** "Somatic CAG Repeat Instability" — status: **EMERGING-TO-CANONICAL** (backed by GWAS, mouse interventional studies, and human iPSC data)
- **Candidate new hypothesis:** "RNA Toxicity" — status: **EMERGING** (in vitro evidence, limited in vivo data)

### Candidate Knowledge Gaps for KB

1. Identity of primary toxic mHTT species (oligomers vs. inclusions) — **unresolved**
2. Molecular basis of selective MSN vulnerability — **partially explained** (somatic expansion, excitotoxicity, transcription factor profile) but **incomplete**
3. Why HTT-lowering clinical trials failed — **unresolved**, critical for therapeutic strategy
4. Human somatic expansion threshold in neurons — **unknown**, only mouse data available
5. Relative contribution of RNA vs. protein toxicity in vivo — **unknown**

---

## Evidence Base (Key Literature)

The following papers represent the most critical evidence evaluated in this report:

- **[PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)** — *Distinct mismatch-repair complex genes set neuronal CAG-repeat expansion rate to drive selective pathogenesis in HD mice.* Demonstrates that MSH3 and PMS1 drive somatic expansion to a threshold of ~150 repeats required for aggregation and pathology. Foundational for the somatic instability model.

- **[PMID: 22970194](https://pubmed.ncbi.nlm.nih.gov/22970194/)** — *Msh2 acts in medium-spiny striatal neurons as an enhancer of CAG instability and mutant huntingtin phenotypes.* Cell-type-specific deletion demonstrates that somatic expansion in MSNs is necessary for mHTT pathological phenotypes.

- **[PMID: 37177784](https://pubmed.ncbi.nlm.nih.gov/37177784/)** — *Di-valent siRNA-mediated silencing of MSH3 blocks somatic repeat expansion.* Therapeutic proof-of-concept for somatic instability intervention.

- **[PMID: 16377565](https://pubmed.ncbi.nlm.nih.gov/16377565/)** — *In vitro analysis of huntingtin-mediated transcriptional repression.* Demonstrates direct polyQ-dependent inhibition of Sp1, TFIID, and TFIIF by mHTT.

- **[PMID: 32681824](https://pubmed.ncbi.nlm.nih.gov/32681824/)** — *Cell-type-specific transcriptomics reveals mutant huntingtin leads to mitochondrial RNA release and neuronal innate immune activation.* Novel downstream mechanism in the most vulnerable cell type.

- **[PMID: 35023827](https://pubmed.ncbi.nlm.nih.gov/35023827/)** — *A novel and accurate full-length HTT mouse model for Huntington's disease.* BAC226Q model demonstrates progressive, age-dependent recapitulation of full HD spectrum with full-length human mHTT.

- **[PMID: 31203656](https://pubmed.ncbi.nlm.nih.gov/31203656/)** — *Conformational studies of pathogenic expanded polyglutamine protein deposits.* Supports dual GoF/LoF mechanism through misfolding and sequestration.

- **[PMID: 20026656](https://pubmed.ncbi.nlm.nih.gov/20026656/)** — *IKK phosphorylates huntingtin and targets it for degradation.* Demonstrates PTM-mediated clearance of mHTT and its age-related decline.

- **[PMID: 27529325](https://pubmed.ncbi.nlm.nih.gov/27529325/)** — *RNA toxicity induced by expanded CAG repeats in Huntington's disease.* Establishes RNA-level toxic gain-of-function as a distinct pathogenic pathway.

- **[PMID: 38861215](https://pubmed.ncbi.nlm.nih.gov/38861215/)** — *Huntington's disease: latest frontiers in therapeutics.* Reviews clinical trial landscape including ASO failures and emerging MSH3-targeting approaches.

---

## Limitations of This Report

1. **Literature search scope:** This evaluation is based on 81 papers identified through PubMed searches. Preprint servers, unpublished clinical trial data, and non-English literature were not systematically searched.

2. **Temporal bias:** The search overrepresents recent literature (2020–2026), particularly on somatic instability. Earlier foundational work on excitotoxicity and mitochondrial dysfunction may be underrepresented.

3. **Clinical trial detail:** The report does not include detailed analysis of specific clinical trial results (e.g., GENERATION HD1 for Tominersen), as full trial publications were not captured in the search.

4. **Human tissue data:** Much of the mechanistic evidence comes from transgenic mouse models and cell culture. Direct human neuronal data, particularly at single-cell resolution across disease stages, remains limited.

5. **Quantitative synthesis:** This is a narrative review rather than a systematic review or meta-analysis. Effect sizes across studies were not formally compared.

---

*Report compiled from evaluation of 81 primary research articles and reviews. Search date: May 2026.*
