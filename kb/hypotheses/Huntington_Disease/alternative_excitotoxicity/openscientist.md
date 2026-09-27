---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T04:29:58.004987'
end_time: '2026-05-23T05:06:10.340393'
duration_seconds: 2172.34
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Huntington's Disease
  category: Genetic
  hypothesis_group_id: alternative_excitotoxicity
  hypothesis_label: NMDA Receptor-Mediated Excitotoxicity
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: alternative_excitotoxicity\nhypothesis_label:\
    \ NMDA Receptor-Mediated Excitotoxicity\nstatus: ALTERNATIVE\ndescription: |\n\
    \  Historical but still supported superimposed model proposing that mutant huntingtin\
    \ and corticostriatal circuit dysfunction enhance NMDA receptor-mediated excitotoxicity\
    \ in striatal medium spiny neurons. This hypothesis is best viewed as a selective-vulnerability\
    \ amplifier rather than the sole initiating lesion.\nevidence:\n- reference: PMID:17188796\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Many lines of evidence\
    \ support a role for neuronal damage arising as a result of excessive\n    activation\
    \ of glutamate receptors by excitatory amino acids in the pathogenesis of Huntington\
    \ disease.\n    The N-methyl-d-aspartate subclass of ionotropic glutamate receptors\
    \ (NMDARs) is more selective and\n    effective than the other subclasses in mediating\
    \ this damage.\n  explanation: Comprehensive review establishing NMDAR-mediated\
    \ excitotoxicity as a key pathogenic mechanism\n    in HD with evidence from human\
    \ tissue, animal models, and cell-based systems.\n- reference: PMID:19279257\n\
    \  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet: This is the\
    \ first direct in vivo evidence of NR2B-NMDAR-mediated excitotoxicity in the context\n\
    \    of HD. Our results are consistent with previous suggestions that direct and/or\
    \ indirect interactions\n    of mutant huntingtin with NMDARs are a proximate\
    \ cause of neurodegeneration in HD.\n  explanation: Provides the first direct\
    \ in vivo genetic evidence for the excitotoxicity hypothesis by\n    showing exacerbated\
    \ striatal neurodegeneration when NR2B-NMDAR subunits are overexpressed in an\
    \ HD\n    mouse model."
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
citation_count: 34
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
- **Hypothesis ID:** alternative_excitotoxicity
- **Hypothesis Label:** NMDA Receptor-Mediated Excitotoxicity
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: alternative_excitotoxicity
hypothesis_label: NMDA Receptor-Mediated Excitotoxicity
status: ALTERNATIVE
description: |
  Historical but still supported superimposed model proposing that mutant huntingtin and corticostriatal circuit dysfunction enhance NMDA receptor-mediated excitotoxicity in striatal medium spiny neurons. This hypothesis is best viewed as a selective-vulnerability amplifier rather than the sole initiating lesion.
evidence:
- reference: PMID:17188796
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Many lines of evidence support a role for neuronal damage arising as a result of excessive
    activation of glutamate receptors by excitatory amino acids in the pathogenesis of Huntington disease.
    The N-methyl-d-aspartate subclass of ionotropic glutamate receptors (NMDARs) is more selective and
    effective than the other subclasses in mediating this damage.
  explanation: Comprehensive review establishing NMDAR-mediated excitotoxicity as a key pathogenic mechanism
    in HD with evidence from human tissue, animal models, and cell-based systems.
- reference: PMID:19279257
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: This is the first direct in vivo evidence of NR2B-NMDAR-mediated excitotoxicity in the context
    of HD. Our results are consistent with previous suggestions that direct and/or indirect interactions
    of mutant huntingtin with NMDARs are a proximate cause of neurodegeneration in HD.
  explanation: Provides the first direct in vivo genetic evidence for the excitotoxicity hypothesis by
    showing exacerbated striatal neurodegeneration when NR2B-NMDAR subunits are overexpressed in an HD
    mouse model.
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

# NMDA Receptor-Mediated Excitotoxicity in Huntington's Disease: A Hypothesis Evaluation Report

**Hypothesis ID:** `alternative_excitotoxicity`  
**Status in KB:** ALTERNATIVE  
**Date:** 2026-05-23  
**Papers reviewed:** 71  
**Findings confirmed:** 9

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — as a selective-vulnerability amplifier, not the sole initiating lesion.**

The NMDA receptor (NMDAR)-mediated excitotoxicity hypothesis in Huntington's disease (HD) is partially supported by a substantial body of evidence spanning more than three decades of research. Strong experimental data from genetic mouse models, electrophysiology, single-cell transcriptomics, and pharmacological studies demonstrate that mutant huntingtin (mHTT) drives a cell-autonomous redistribution of GluN2B-containing NMDARs to extrasynaptic (pro-death) sites in striatal medium spiny neurons (MSNs), amplified by downstream kinases such as DAPK1 and p38 MAPK. The quinolinic acid (QA) lesion model — an NMDAR agonist — uniquely reproduces the neurochemical and interneuron-sparing pattern of human HD striatum, lending classical pharmacological support. However, major caveats limit the hypothesis to an amplifier role rather than a primary driver: (1) somatic CAG repeat expansion driven by DNA mismatch repair (MMR) genes, particularly MSH3, has emerged as the most upstream modifiable pathogenic event, operating above excitotoxicity in the causal chain; (2) clinical trials of NMDAR antagonists (remacemide, memantine) have failed to modify HD progression; (3) biphasic corticostriatal dynamics — early glutamate excess followed by late disconnection — mean that excitotoxicity cannot explain neurodegeneration across all disease stages; and (4) multiple parallel mechanisms (proteostasis collapse, transcriptional dysregulation, mitochondrial dysfunction, neuroinflammation) converge on MSN vulnerability independently of NMDAR signaling. The hypothesis is best classified as **ALTERNATIVE** in the knowledge base: a real and important pathogenic contributor, particularly in presymptomatic and early disease stages, but subordinate to the somatic expansion model as the primary upstream cause.

---

## Summary

The excitotoxicity hypothesis for Huntington's disease posits that mutant huntingtin enhances NMDA receptor-mediated glutamatergic toxicity in striatal medium spiny neurons, driving their selective degeneration. This report evaluates that claim against 71 papers spanning human postmortem studies, genetic mouse models, single-cell transcriptomics, electrophysiology, and clinical trial data. Nine key findings were confirmed during the investigation. The strongest evidence supports excitotoxicity as an early, cell-autonomous vulnerability amplifier: mHTT drives GluN2B-NMDAR redistribution to extrasynaptic sites, where DAPK1 phosphorylation and p38 MAPK signaling amplify pro-death cascades. The ovine HD model provides single-cell transcriptomic evidence of glutamate receptor upregulation in MSNs before any detectable cell death, and QA lesions uniquely replicate human HD neurochemistry including the characteristic sparing of somatostatin/neuropeptide Y interneurons.

However, the hypothesis faces significant challenges. The discovery that somatic CAG repeat expansion — driven by MMR pathway genes (MSH3, MLH1, MLH3) — is the critical upstream determinant of disease onset and progression has repositioned excitotoxicity as a downstream amplifier rather than a root cause. Biphasic corticostriatal dynamics complicate the narrative: early excessive glutamate release gives way to progressive disconnection, with optogenetically-induced glutamate release becoming undetectable in late-stage HD mice. The failure of NMDAR antagonist clinical trials further limits the therapeutic actionability of this hypothesis. The evidence converges on a model where excitotoxicity is one node in a multi-mechanism pathogenic network — interacting with proteostasis failure, mitochondrial dysfunction, BDNF loss, and neuroinflammation — rather than a sufficient standalone explanation for HD neurodegeneration.

---

## Key Findings

### Finding 1: Extrasynaptic GluN2B-NMDAR Redistribution Is an Early, Cell-Autonomous Event in HD MSNs

One of the most mechanistically precise findings supporting the excitotoxicity hypothesis is the demonstration that mHTT drives a cell-autonomous increase in extrasynaptic NMDAR localization in MSNs. In YAC128 mice, extrasynaptic NMDAR current is elevated while synaptic NMDAR currents remain unchanged. GluN2B surface expression is markedly increased at extrasynaptic sites, driven by intrinsic MSN mechanisms involving calpain-mediated GluN2B cleavage and elevated STEP (striatal-enriched protein tyrosine phosphatase) activity. PSD-95 interactions with GluN2B are increased specifically at extrasynaptic sites. Critically, this occurs presymptomatically, placing it early in the pathogenic cascade.

The cell-autonomous nature of this redistribution was demonstrated in cortico-striatal co-culture systems, where "MSN cell-autonomous increases in extrasynaptic NMDARs are driven by the HD mutation" ([PMID: 22668780](https://pubmed.ncbi.nlm.nih.gov/22668780/)). This was confirmed independently: "Deleterious extrasynaptic NMDAR localization and signalling are increased early in yeast artificial chromosome mice expressing full-length mhtt with 128 polyglutamine repeats (YAC128 mice)" ([PMID: 22523092](https://pubmed.ncbi.nlm.nih.gov/22523092/)). This synaptic-to-extrasynaptic shift is significant because extrasynaptic NMDARs are coupled to pro-death signaling (CREB shut-off, mitochondrial dysfunction), while synaptic NMDARs promote survival.

Additional mechanistic detail was provided by studies of PSD-95, a key scaffolding protein. The association of PSD-95 with the NR2B subunit in striatal tissue was enhanced by increased huntingtin polyQ length, and treatment with Tat-NR2B9c peptide — which disrupts the GluN2B–PSD-95 interaction — reduced NMDAR surface expression by 20% and "restored susceptibility to NMDAR excitoxicity in YAC HD MSNs to levels observed in wild-type MSNs" ([PMID: 19726651](https://pubmed.ncbi.nlm.nih.gov/19726651/)).

### Finding 2: First Direct In Vivo Genetic Evidence for NR2B-NMDAR Excitotoxicity in HD

The most direct genetic test of the excitotoxicity hypothesis was performed by crossing Hdh(CAG)150 knock-in HD mice with NR2B-overexpressing transgenic mice. The resulting double-mutant line showed exacerbated selective striatal neurodegeneration, providing "the first direct in vivo evidence of NR2B-NMDAR-mediated excitotoxicity in the context of HD" ([PMID: 19279257](https://pubmed.ncbi.nlm.nih.gov/19279257/)). This genetic epistasis experiment is important because it demonstrates that NR2B-NMDAR activation is sufficient to worsen HD-like striatal pathology in vivo, moving beyond correlative evidence from pharmacological models.

### Finding 3: Transcriptomic Upregulation of Glutamate Receptors in MSNs Precedes Cell Death

Single-nuclei RNA-seq of striatum from 5-year-old OVT73 transgenic HD sheep (73Q, somatically stable, prodromal phase, no detectable cell loss) revealed transcriptional upregulation of genes encoding NMDA, AMPA, and kainate receptors specifically in MSNs. Compensatory upregulation of astrocytic glutamate transporters and GABAA receptors was also observed. The study identified "transcriptional upregulation of genes encoding N-methyl-D-aspartate (NMDA), α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) and kainate receptors in medium spiny neurons, the cell type preferentially lost early in HD" ([PMID: 38776957](https://pubmed.ncbi.nlm.nih.gov/38776957/)). This is significant because it provides single-cell resolution evidence from a large-animal model at a presymptomatic stage, linking glutamate receptor upregulation to MSN-specific vulnerability before any neuronal death occurs.

### Finding 4: DAPK1 Amplifies Extrasynaptic GluN2B Toxicity Through S1303 Phosphorylation

Death-associated protein kinase 1 (DAPK1), a pro-apoptotic kinase normally silenced in adult brain, "becomes re-activated and recruited to extrasynaptic NMDAR complexes during neuronal death, where it phosphorylates GluN2B at S1303, amplifying toxic receptor function" ([PMID: 33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/)). In YAC128 mice, DAPK1 reactivation is associated with increased cell death pathways, inhibition of survival signaling, and greater susceptibility to excitotoxicity. This finding identifies a specific molecular amplifier of the extrasynaptic NMDAR toxicity cascade in HD, providing a potential therapeutic target within the excitotoxicity pathway.

Further downstream, the p38 MAPK pathway was shown to mediate the enhanced excitotoxicity. Basal levels of both activated p38 and JNK MAPKs were elevated in the YAC128 striatum, and "p38 MAPK inhibition reduced YAC128 NMDAR-mediated cell death to WT levels" ([PMID: 22198502](https://pubmed.ncbi.nlm.nih.gov/22198502/)). Importantly, the p38 activation was PSD-95-dependent and was selectively reduced by Tat-NR2B9c, while JNK activation was PSD-95-independent, establishing pathway specificity.

### Finding 5: Somatic CAG Repeat Expansion — The Upstream Driver Superseding Excitotoxicity

The most transformative finding for the excitotoxicity hypothesis is the emergence of somatic CAG repeat expansion as the primary upstream driver of HD pathogenesis. GWAS modifiers of HD onset converge on DNA mismatch repair genes (MSH3, PMS1, MLH1). Msh3 knockout in Q140 HD mice abolishes somatic CAG expansion, prevents mHTT aggregation, and corrects synaptic, astrocytic, and locomotor defects. "The fast linear rate of mHtt modal-CAG-repeat expansion in MSNs (8.8 repeats/month) is drastically reduced or stopped by MMR mutants" ([PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)). This was validated in human iPSC models: "Reduced MSH2, MSH3, and MLH1 slowed repeat expansion to the largest degree" ([PMID: 38749429](https://pubmed.ncbi.nlm.nih.gov/38749429/)).

This finding repositions excitotoxicity as a downstream consequence of somatic expansion rather than an independent initiating lesion. As somatic repeats expand beyond pathogenic thresholds in striatal neurons, the resulting higher-polyQ mHTT increasingly disrupts NMDAR trafficking. However, an important caveat emerged from studies using very long repeats: Msh3 knockout in zQ175 mice (~185 CAG) "had no effect on the deposition of huntingtin aggregation in the nuclei of striatal neurons, nor on the dysregulated striatal transcriptional profile" ([PMID: 38387080](https://pubmed.ncbi.nlm.nih.gov/38387080/)), suggesting that once the repeat length exceeds a critical threshold, further somatic expansion becomes dispensable for certain pathogenic readouts.

### Finding 6: TNF-Dependent Synaptic Changes Potentiate Excitotoxicity in Direct Pathway MSNs

In presymptomatic YAC128 mice, "an increase in excitatory synaptic strength, as measured by AMPA/NMDA ratios, specifically on direct pathway D1 receptor expressing medium spiny neurons, with no changes on indirect pathway neurons" was observed ([PMID: 36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/)). TNF-α elevation in the striatum drives this pathway-specific enhancement, and genetic or pharmacological TNF blockade normalized synaptic strength. This finding adds neuroinflammation as a contributor to excitotoxic vulnerability and reveals unexpected pathway specificity — direct pathway MSNs, not just indirect pathway neurons, are affected early, creating a paradox given that D2 (indirect pathway) MSNs are traditionally considered the first to degenerate in HD.

### Finding 7: Biphasic Corticostriatal Disconnection Complicates the Excitotoxicity Model

The excitotoxicity hypothesis implicitly requires sustained glutamatergic input to drive ongoing neuronal death. However, HD mouse models show biphasic corticostriatal dynamics: "a progressive disconnection in the corticostriatal pathway leads to abnormal function engaging extrasynaptic N-methyl-D-aspartate glutamate receptors that contribute to eventual cell degeneration" ([PMID: 33198566](https://pubmed.ncbi.nlm.nih.gov/33198566/)). In late-stage mice, "optogenetically-induced glutamate release from M2 cortex terminals in the dorsolateral striatum (DLS) was undetectable in HD mice and striatal neurons show blunted electrophysiological responses" ([PMID: 33016873](https://pubmed.ncbi.nlm.nih.gov/33016873/)). This biphasic pattern — early dysregulated excess followed by late progressive loss — means excitotoxicity may contribute to early/prodromal pathology but cannot explain continued neurodegeneration in advanced disease. Importantly, repeated optogenetic corticostriatal stimulation rescued some motor behavior in late-stage mice, suggesting that the disconnection itself contributes to late symptoms.

### Finding 8: Quinolinic Acid Striatal Lesions Closely Reproduce HD Neuropathology

The classical pharmacological evidence for NMDAR-mediated excitotoxicity in HD comes from the QA lesion model. Chronic striatal QA lesions in rats produce increases in somatostatin and neuropeptide Y concentrations, reductions in GABA and substance P, striking sparing of NADPH-diaphorase neurons (not seen with kainate or AMPA lesions), and changes that "closely resemble Huntington's disease" ([PMID: 1710657](https://pubmed.ncbi.nlm.nih.gov/1710657/)). The specificity of this pattern to NMDAR agonists was confirmed in detailed dose-response studies: "N-methyl-D,L-aspartate and quinolinic acid had no significant effect on concentrations of SLI and NPYLI," while kainic acid and AMPA reduced all markers equally ([PMID: 2563916](https://pubmed.ncbi.nlm.nih.gov/2563916/)). This remains the strongest pharmacological argument that NMDAR activation specifically — rather than general excitotoxicity — underlies the characteristic neuropathological pattern of HD.

Human postmortem in situ hybridization data further supports this finding. NR1 and NR2B mRNA decreased in HD neostriatum in correlation with disease severity, but notably "Early in the disease, cellular NR1/NR2BmRNA levels were higher in these zones than in controls" ([PMID: 9100675](https://pubmed.ncbi.nlm.nih.gov/9100675/)). Additionally, astrocytic GLT1 (glutamate transporter) mRNA showed reduced per-cell expression despite astrogliosis, suggesting impaired glutamate clearance capacity.

### Finding 9: PKD1 Downregulation Links Excitotoxicity to MSN-Specific Vulnerability

A recent study found "an unexpected reduction in PKD1 protein levels in striatal neurons from HD patients. Similarly, the R6/1 mouse model of HD exhibited progressive PKD1 protein loss, commencing at early disease stages, accompanied by decreased Prkd1 transcript levels" ([PMID: 40461488](https://pubmed.ncbi.nlm.nih.gov/40461488/)). PKD1 normally potentiates neuronal survival in excitotoxic environments; pharmacological PKD inhibition in primary striatal neurons exacerbated excitotoxic damage and apoptosis induced by NMDA receptors. PKD1 loss occurs early in striatum but only late in cortex, potentially helping explain the selective striatal vulnerability characteristic of HD. This is notable as one of the few findings validated in human postmortem tissue.

---

## Mechanistic Causal Chain

The excitotoxicity hypothesis implies the following causal chain from upstream trigger to clinical manifestation. The evidence strength at each link is annotated:

{{figure:mechanistic_chain.png|caption=Mechanistic causal chain from HTT CAG expansion through NMDAR-mediated excitotoxicity to MSN degeneration, showing evidence strength at each link}}

```
UPSTREAM TRIGGER (Strong evidence)
┌─────────────────────────────────────────────────────┐
│ HTT CAG repeat expansion (germline mutation)        │
│ → Somatic CAG expansion in striatal MSNs            │
│   (MMR-driven: MSH3, MLH1, MLH3)                   │
│   [PMID: 39938516, 38749429, 31216018, 18930147]    │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
MOLECULAR EVENTS (Strong evidence)
┌─────────────────────────────────────────────────────┐
│ Mutant huntingtin (expanded polyQ)                  │
│ → Altered PSD-95/GluN2B interactions                │
│ → Calpain activation & STEP dysregulation           │
│ → GluN2B-NMDAR redistribution to                   │
│   EXTRASYNAPTIC sites (cell-autonomous)             │
│   [PMID: 22668780, 22523092, 19726651]              │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
AMPLIFICATION CASCADE (Moderate-Strong evidence)
┌─────────────────────────────────────────────────────┐
│ DAPK1 reactivation → GluN2B S1303 phosphorylation  │
│ p38 MAPK activation (PSD-95-dependent)              │
│ PKD1 loss → reduced survival signaling              │
│ TNF-α elevation → pathway-specific E/I imbalance    │
│ Astrocytic GLT-1/GLAST downregulation               │
│ Glutamate receptor transcriptional upregulation     │
│   [PMID: 33250715, 22198502, 40461488,              │
│    36517241, 19168136, 38776957]                     │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
CELLULAR CONSEQUENCES (Moderate evidence)
┌─────────────────────────────────────────────────────┐
│ Excessive Ca²⁺ influx via extrasynaptic NMDARs      │
│ → CREB shut-off (survival gene suppression)         │
│ → Mitochondrial Ca²⁺ overload / dysfunction         │
│ → Caspase activation / apoptosis                    │
│ → Selective MSN degeneration                        │
│   (interneurons spared: fewer NMDARs on SS/NPY)    │
│   [PMID: 1710657, 2563916, 11086188]                │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
COMPLICATING FACTOR (Strong evidence)
┌─────────────────────────────────────────────────────┐
│ BIPHASIC CORTICOSTRIATAL DYNAMICS                   │
│ Early: ↑ glutamate release → excitotoxic            │
│ Late: progressive disconnection                     │
│   (glutamate release undetectable)                  │
│ → Excitotoxicity mainly relevant early-stage        │
│   [PMID: 33198566, 33016873, 21907762]              │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
CLINICAL MANIFESTATION
┌─────────────────────────────────────────────────────┐
│ Striatal atrophy → chorea, cognitive decline,       │
│ psychiatric symptoms                                │
│ (HD onset age modified by MMR variants, not         │
│  glutamate receptor variants)                       │
└─────────────────────────────────────────────────────┘
```

### Evidence Strength at Each Causal Link

| Causal Link | Evidence Strength | Key References |
|-------------|-------------------|----------------|
| CAG expansion → mHTT toxicity | **ESTABLISHED** | Fundamental HD genetics |
| Somatic CAG expansion → threshold toxicity | **STRONG** (emerging) | [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/), [PMID: 38749429](https://pubmed.ncbi.nlm.nih.gov/38749429/), [PMID: 38387080](https://pubmed.ncbi.nlm.nih.gov/38387080/) |
| mHTT → extrasynaptic NMDAR redistribution | **STRONG** | [PMID: 22668780](https://pubmed.ncbi.nlm.nih.gov/22668780/), [PMID: 22523092](https://pubmed.ncbi.nlm.nih.gov/22523092/) |
| Extrasynaptic NMDAR → p38/CREB death signaling | **STRONG** | [PMID: 22198502](https://pubmed.ncbi.nlm.nih.gov/22198502/), [PMID: 22668780](https://pubmed.ncbi.nlm.nih.gov/22668780/) |
| DAPK1 → GluN2B-S1303 amplification | **MODERATE** | [PMID: 33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/) |
| PKD1 loss → increased vulnerability | **MODERATE-STRONG** | [PMID: 40461488](https://pubmed.ncbi.nlm.nih.gov/40461488/) (human + mouse) |
| GLT-1 loss → impaired glutamate clearance | **MODERATE** | [PMID: 19168136](https://pubmed.ncbi.nlm.nih.gov/19168136/), [PMID: 9100675](https://pubmed.ncbi.nlm.nih.gov/9100675/) |
| TNF → pathway-specific E/I imbalance | **MODERATE** | [PMID: 36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/) |
| Excitotoxicity → selective MSN death pattern | **STRONG** (lesion models) | [PMID: 1710657](https://pubmed.ncbi.nlm.nih.gov/1710657/), [PMID: 2563916](https://pubmed.ncbi.nlm.nih.gov/2563916/) |
| Excitotoxicity → HD clinical progression | **INFERRED** (no clinical trial success) | [PMID: 15717010](https://pubmed.ncbi.nlm.nih.gov/15717010/), [PMID: 11554551](https://pubmed.ncbi.nlm.nih.gov/11554551/) |
| Somatic expansion → excitotoxicity | **INFERRED** (not directly tested) | Gap identified |

**Key missing causal links:**

1. **Somatic expansion → NMDAR redistribution**: It is inferred but not directly demonstrated that progressive somatic CAG expansion is the trigger for extrasynaptic NMDAR redistribution. No study has shown that blocking somatic expansion prevents the synaptic-to-extrasynaptic NMDAR shift.
2. **Extrasynaptic Ca²⁺ → MSN death in vivo (human)**: While extrasynaptic NMDAR signaling is well-characterized in mouse models, the quantitative contribution of this pathway to MSN death in human HD brain remains unconfirmed.
3. **Late-stage neurodegeneration mechanism**: If corticostriatal disconnection abolishes glutamate input in late disease, what drives continued MSN death? Cell-autonomous mechanisms (proteostasis failure, transcriptional dysregulation) likely dominate.

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing key studies supporting, qualifying, or competing with the NMDAR excitotoxicity hypothesis in HD}}

| # | PMID | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|---|------|---------------|-----------|-------------------|-------------|---------|------------|
| 1 | [19279257](https://pubmed.ncbi.nlm.nih.gov/19279257/) | Model organism (genetic in vivo) | **SUPPORTS** | NR2B-NMDAR excitotoxicity is a proximate cause of striatal degeneration in HD | NR2B overexpression in Hdh(CAG)150 mice exacerbates selective striatal neurodegeneration | Knock-in HD × NR2B-Tg double mutant | **HIGH** — first direct in vivo genetic evidence |
| 2 | [22668780](https://pubmed.ncbi.nlm.nih.gov/22668780/) | Model organism (co-culture) | **SUPPORTS** | Extrasynaptic NMDAR redistribution is cell-autonomous in HD MSNs | Extrasynaptic NMDAR current elevated in YAC128 MSNs; GluN2B surface expression markedly increased; synaptic NMDARs unchanged | YAC128 corticostriatal co-cultures, presymptomatic | **HIGH** |
| 3 | [38776957](https://pubmed.ncbi.nlm.nih.gov/38776957/) | Model organism (snRNA-seq) | **SUPPORTS** | Glutamate receptor upregulation precedes cell death | NMDA, AMPA, and kainate receptor genes upregulated in MSNs before any detectable neuronal loss; compensatory astrocytic glutamate transporter upregulation | OVT73 HD sheep, 5yr, prodromal | **HIGH** — large animal, single-cell resolution |
| 4 | [33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/) | Model organism | **SUPPORTS** | DAPK1 amplifies extrasynaptic GluN2B toxicity | DAPK1 recruited to extrasynaptic NMDARs, phosphorylates GluN2B-S1303, amplifies toxic receptor function and cell death pathways | YAC128, early stages | **MODERATE-HIGH** |
| 5 | [22198502](https://pubmed.ncbi.nlm.nih.gov/22198502/) | Model organism | **SUPPORTS** | p38 MAPK death pathway via PSD-95-GluN2B | p38 and JNK basally elevated in YAC128 striatum; p38 inhibition reduces NMDAR cell death to WT levels | YAC128, presymptomatic | **MODERATE-HIGH** |
| 6 | [19726651](https://pubmed.ncbi.nlm.nih.gov/19726651/) | Model organism | **SUPPORTS** | PSD-95–NR2B interaction drives excitotoxicity | PSD-95-NR2B association enhanced by increased polyQ length; Tat-NR2B9c reduces NMDAR surface expression by 20% and normalizes excitotoxicity | YAC128 and YAC72 vs WT | **HIGH** |
| 7 | [40461488](https://pubmed.ncbi.nlm.nih.gov/40461488/) | Human + model organism | **SUPPORTS** | PKD1 loss increases excitotoxic vulnerability | PKD1 protein reduced in HD patient striatum (postmortem) and R6/1 mice from early stages; PKD inhibition exacerbates NMDA-mediated damage | Human HD tissue + R6/1 mice | **HIGH** — human tissue confirmation |
| 8 | [22523092](https://pubmed.ncbi.nlm.nih.gov/22523092/) | Model organism | **SUPPORTS** | Calpain/STEP drive extrasynaptic NMDAR localization | Increased calpain cleavage of GluN2B and elevated STEP activity at extrasynaptic sites in YAC128 | YAC128, early | **MODERATE-HIGH** |
| 9 | [1710657](https://pubmed.ncbi.nlm.nih.gov/1710657/) | Model organism (lesion) | **SUPPORTS** | QA (NMDA agonist) uniquely reproduces HD neurochemistry | Chronic QA lesions produce HD-like interneuron sparing, neurochemical changes; KA and AMPA lesions do not | Rat, 6mo–1yr post-lesion | **HIGH** (foundational) |
| 10 | [2563916](https://pubmed.ncbi.nlm.nih.gov/2563916/) | Model organism (lesion) | **SUPPORTS** | NMDAR-specific interneuron sparing | Only NMDAR agonists (not KA/AMPA) spare SS/NPY neurons as in HD; dose-response evidence | Rat, dose-response | **HIGH** |
| 11 | [17188796](https://pubmed.ncbi.nlm.nih.gov/17188796/) | Review | **SUPPORTS** | Comprehensive evidence for NMDAR excitotoxicity in HD | "Many lines of evidence support a role for neuronal damage arising as a result of excessive activation of glutamate receptors... NMDARs is more selective and effective" | Comprehensive review | **HIGH** (review-level) |
| 12 | [36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/) | Model organism | **QUALIFIES** | TNF-mediated E/I imbalance in pathway-specific MSNs | Increased AMPA/NMDA ratio specific to D1-MSNs (not D2); TNF-dependent | YAC128, presymptomatic | **MODERATE-HIGH** |
| 13 | [33198566](https://pubmed.ncbi.nlm.nih.gov/33198566/) | Review (synthesis) | **QUALIFIES** | Biphasic corticostriatal dysfunction | Early excess glutamate release, then progressive disconnection; changes are time-dependent | Multiple HD mouse models | **HIGH** (review-level) |
| 14 | [33016873](https://pubmed.ncbi.nlm.nih.gov/33016873/) | Model organism | **QUALIFIES** | Late corticostriatal disconnection | Optogenetically-induced glutamate release from M2 cortex undetectable in HD mice | R6/2 and Q175 mice | **HIGH** |
| 15 | [9100675](https://pubmed.ncbi.nlm.nih.gov/9100675/) | Human (postmortem ISH) | **QUALIFIES** | NMDAR changes in human HD brain | NR1/NR2B mRNA decreases with severity; early zones show higher expression than controls; GLT1 reduced per cell | HD patients, various grades | **HIGH** |
| 16 | [19168136](https://pubmed.ncbi.nlm.nih.gov/19168136/) | Model organism | **QUALIFIES** | Age-dependent glutamate vulnerability | Striatal vulnerability increases only at 14wk (not 10wk) in R6/2; correlates with GLT-1/GLAST decrease | R6/2 mice | **MODERATE** |
| 17 | [39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/) | Model + human genetics | **COMPETING** | Somatic CAG expansion via MSH3/MMR is upstream driver | MSH3-KO blocks somatic expansion, prevents aggregation, corrects synaptic/astrocytic/locomotor defects | Q140 mice + GWAS | **VERY HIGH** |
| 18 | [38749429](https://pubmed.ncbi.nlm.nih.gov/38749429/) | Human (iPSC) | **COMPETING** | MMR gene modulation as therapeutic approach | CRISPRi lowering of MSH2, MSH3, MLH1 slows CAG repeat expansion in HD iPSCs | HD iPSCs, >125 CAG | **HIGH** |
| 19 | [26282324](https://pubmed.ncbi.nlm.nih.gov/26282324/) | Model organism | **COMPETING** | BDNF loss as parallel mechanism | Selective mBDNF reduction in striatum; decreased TrkB activation; no proBDNF increase | zQ175 mice, aged | **MODERATE-HIGH** |
| 20 | [28099414](https://pubmed.ncbi.nlm.nih.gov/28099414/) | Human + model organism | **COMPETING** | Neuroinflammatory astrocyte toxicity | A1 reactive astrocytes abundant in HD brain; kill neurons independently of excitotoxicity | Multiple NDs including HD | **HIGH** |
| 21 | [23994717](https://pubmed.ncbi.nlm.nih.gov/23994717/) | Model organism | **SUPPORTS** | Kynurenine pathway–excitotoxicity link | IDO1 knockout mice less sensitive to QA-induced striatal neurotoxicity; decreased 3-HK levels | IDO-/- mice | **MODERATE** |
| 22 | [15717010](https://pubmed.ncbi.nlm.nih.gov/15717010/) | Clinical/review | **QUALIFIES** | NMDA antagonist clinical feasibility | High-affinity NMDA antagonists failed; memantine shows modest benefit via preferential extrasynaptic blockade | Clinical trial data | **HIGH** (clinical reality) |

---

## Alternative and Competing Models

{{figure:knowledge_gaps.png|caption=Knowledge gaps and competing mechanistic models compared to the NMDAR excitotoxicity hypothesis in HD}}

### 1. Somatic CAG Repeat Expansion (MSH3/MMR-Driven) — Upstream Cause

The strongest competing model posits that somatic instability of the CAG repeat, driven by mismatch repair pathway genes (MSH3, MLH1, MLH3, PMS1), is the primary upstream determinant of disease onset and progression. GWAS modifier studies in humans and genetic experiments in mice provide convergent evidence. Msh3 knockout prevents somatic expansion, mHTT aggregation, and multiple downstream phenotypes ([PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/)). Human iPSC validation confirmed the role of MMR genes ([PMID: 38749429](https://pubmed.ncbi.nlm.nih.gov/38749429/)). Additional studies established that Mlh1 and Mlh3 are essential for somatic CAG expansions, with the MutLγ complex (MLH1-MLH3) being as critical as MutSβ (MSH2-MSH3) ([PMID: 24204323](https://pubmed.ncbi.nlm.nih.gov/24204323/)). **Relationship to excitotoxicity: upstream cause — somatic expansion increases the effective polyQ length, which then triggers downstream mechanisms including NMDAR redistribution. Not a competing explanation but rather reframes excitotoxicity as a downstream effector.**

### 2. Proteostasis Network Collapse — Parallel Mechanism

The expanded polyQ tract in mHTT leads to misfolding, aggregation, and progressive overloading of the ubiquitin-proteasome system and autophagy-lysosomal pathways. This proteostasis collapse is well-documented ([PMID: 30502498](https://pubmed.ncbi.nlm.nih.gov/30502498/)). Multiple therapeutic strategies targeting protein clearance — including TFEB activation, UCHL3 inhibition ([PMID: 41578740](https://pubmed.ncbi.nlm.nih.gov/41578740/)), IGF2 signaling ([PMID: 32642868](https://pubmed.ncbi.nlm.nih.gov/32642868/)), and autophagy enhancement — show efficacy in HD models. **Relationship: parallel mechanism that can independently drive cell death even in the absence of excitotoxic input. Potentially more parsimonious for explaining late-stage neurodegeneration after corticostriatal disconnection.**

### 3. BDNF/Neurotrophin Signaling Deficit — Parallel Mechanism

Selective reduction of mature BDNF without induction of proBDNF was demonstrated in the zQ175 model, with decreased TrkB activation ([PMID: 26282324](https://pubmed.ncbi.nlm.nih.gov/26282324/)). Since MSNs depend on cortically-derived BDNF for survival, this deficit provides an alternative explanation for selective MSN vulnerability. Disrupted neurotrophin receptor signaling has been proposed as a comprehensive therapeutic target ([PMID: 29254102](https://pubmed.ncbi.nlm.nih.gov/29254102/)). **Relationship: parallel mechanism that converges on MSN death and interacts with excitotoxicity through shared downstream signaling (CREB pathway).**

### 4. Transcriptional Dysregulation — Parallel/Downstream

mHTT disrupts multiple transcription factors and epigenetic regulators, leading to widespread gene expression changes. The genome-wide CNS screening study identified that "CNS neurons are particularly sensitive not only to perturbations to synaptic processes but also autophagy, proteostasis, mRNA processing, and mitochondrial function" ([PMID: 32004439](https://pubmed.ncbi.nlm.nih.gov/32004439/)). miR-132/212 dysregulation has also been implicated in HD-related BDNF and CREB signaling ([PMID: 39170678](https://pubmed.ncbi.nlm.nih.gov/39170678/)). **Relationship: some transcriptional changes feed into excitotoxicity (e.g., ↓PKD1, ↓BDNF) while others cause independent damage.**

### 5. Neuroinflammation / A1 Astrocyte Toxicity — Parallel Mechanism with Bidirectional Interactions

Activated microglia secrete IL-1α, TNF and C1q to induce neurotoxic A1 astrocytes, which are "abundant in various human neurodegenerative diseases including Alzheimer's, Huntington's and Parkinson's disease" ([PMID: 28099414](https://pubmed.ncbi.nlm.nih.gov/28099414/)). A1 astrocytes kill neurons independently of excitotoxicity while also losing the ability to clear glutamate efficiently. TNF elevation potentiates excitotoxicity specifically in D1-MSNs ([PMID: 36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/)). **Relationship: parallel mechanism with strong bidirectional interactions — inflammation amplifies excitotoxicity, and excitotoxic damage may promote inflammation.**

### 6. Mitochondrial Dysfunction and Energy Deficit — Bidirectional Interaction

mHTT directly impairs mitochondrial function, causing respiratory chain deficits, oxidative stress, and energy failure ([PMID: 21539755](https://pubmed.ncbi.nlm.nih.gov/21539755/)). Mitochondrial dysfunction can both result from (Ca²⁺ overload via NMDARs) and amplify excitotoxic damage (impaired Ca²⁺ buffering, reduced ATP for glutamate clearance). **Relationship: bidirectional positive feedback loop with excitotoxicity.**

### 7. Kynurenine Pathway Dysregulation — Upstream Amplifier

IDO1 is chronically elevated in YAC128 striatum, producing neurotoxic 3-hydroxykynurenine and quinolinic acid (an endogenous NMDAR agonist). IDO knockout mice show reduced QA-induced striatal toxicity ([PMID: 23994717](https://pubmed.ncbi.nlm.nih.gov/23994717/)). Kynurenine 3-monooxygenase (KMO) activity in human neurons generates both 3-HK and QUIN with neurotoxic effects ([PMID: 30666558](https://pubmed.ncbi.nlm.nih.gov/30666558/)). **Relationship: upstream amplifier that may increase endogenous NMDAR agonist levels, feeding into the excitotoxicity cascade.**

---

## Knowledge Gaps

### Gap 1: No Direct Evidence Connecting Somatic CAG Expansion to NMDAR Redistribution
- **Scope**: The causal link between somatic expansion (the upstream driver) and extrasynaptic NMDAR redistribution (the core excitotoxicity mechanism) has not been directly tested
- **Why it matters**: This is the critical junction between the two leading hypotheses; establishing or refuting this link determines whether they are sequential or independent
- **What was checked**: Literature on Msh3-KO effects in HD models; PMID:39938516 showed that MSH3-KO corrects synaptic defects but did not specifically measure extrasynaptic NMDAR localization
- **Resolution**: Electrophysiological characterization of synaptic vs. extrasynaptic NMDAR currents in Msh3-KO × HD knock-in mice at presymptomatic ages

### Gap 2: No Human In Vivo Extrasynaptic NMDAR Measurement
- **Scope**: All extrasynaptic NMDAR redistribution data come from mouse models; no direct measurement in living human HD brain
- **Why it matters**: The core mechanistic claim requires validation in the human disease context for therapeutic translation
- **What was checked**: PET ligand studies (mGluR5 PET in [PMID: 29794227](https://pubmed.ncbi.nlm.nih.gov/29794227/)); no extrasynaptic-specific NMDAR PET ligand exists. Human postmortem ISH ([PMID: 9100675](https://pubmed.ncbi.nlm.nih.gov/9100675/)) provides partial evidence but cannot distinguish synaptic vs. extrasynaptic
- **Resolution**: Development of subunit-selective or location-selective NMDAR PET tracers; or advanced postmortem spatial proteomics

### Gap 3: Mechanism of Continued Neurodegeneration After Corticostriatal Disconnection
- **Scope**: If glutamate input is lost in late-stage HD, what sustains excitotoxic damage?
- **Why it matters**: The biphasic dynamic limits excitotoxicity to early disease stages; late-stage mechanism is unclear
- **What was checked**: Optogenetic and electrophysiological studies showing disconnection ([PMID: 33016873](https://pubmed.ncbi.nlm.nih.gov/33016873/)); no studies of endogenous NMDAR agonist (QA) production or cell-autonomous glutamate release in late HD
- **Resolution**: Longitudinal calcium imaging in MSNs across disease stages; assessment of endogenous QA production via kynurenine pathway in late-stage brain

### Gap 4: Failure of NMDAR Antagonist Trials — Mechanistic Explanation
- **Scope**: Remacemide and memantine clinical trials showed no disease modification in HD
- **Why it matters**: If excitotoxicity were a major driver, blocking it should slow progression; trial failure undermines the hypothesis
- **What was checked**: Clinical trial reports and reviews ([PMID: 11554551](https://pubmed.ncbi.nlm.nih.gov/11554551/), [PMID: 15717010](https://pubmed.ncbi.nlm.nih.gov/15717010/))
- **Possible explanations**: (a) wrong timing (too late in disease), (b) insufficient target engagement, (c) need for extrasynaptic-selective agents, (d) excitotoxicity is truly subsidiary
- **Resolution**: Stage-stratified trial with extrasynaptic-selective or GluN2B-selective agents in presymptomatic carriers

### Gap 5: D1 vs. D2 MSN Pathway Specificity Paradox
- **Scope**: TNF-mediated excitotoxic enhancement is specific to D1-MSNs ([PMID: 36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/)), but D2-MSNs are traditionally considered the first to degenerate in HD
- **Why it matters**: Creates a paradox where the excitotoxicity mechanism targets the "wrong" MSN subtype first
- **What was checked**: CB1R pathway-specific neuroprotection study ([PMID: 29121220](https://pubmed.ncbi.nlm.nih.gov/29121220/)) showing differential vulnerability; limited data on D2-specific NMDAR changes
- **Resolution**: Cell-type-specific NMDAR subunit profiling and excitotoxicity assays in Drd1-Cre and Drd2-Cre HD mice

### Gap 6: Human Genetic Evidence Linking NMDAR Pathway to HD Modification
- **Scope**: GWAS modifiers converge on MMR genes, not glutamate receptor genes
- **Why it matters**: If excitotoxicity were a major determinant of onset, GRIN2B or DLG4 (PSD-95) variants might modify HD onset; their absence from GWAS is notable
- **What was checked**: HD GWAS modifier studies (GeM-HD consortium); no significant glutamate receptor pathway associations reported
- **Resolution**: Targeted sequencing of glutamate receptor pathway genes in large HD cohorts; gene-based burden tests

### Gap 7: No Systematic Gene-Disease Curation for Excitotoxicity Pathway in HD
- **Scope**: No GenCC, ClinGen, or systematic curation database specifically maps excitotoxicity pathway genes in HD
- **Why it matters**: Limits ability to computationally integrate excitotoxicity evidence with other pathogenic pathways
- **What was checked**: Genome-wide screen ([PMID: 32004439](https://pubmed.ncbi.nlm.nih.gov/32004439/)) identified synaptic processes but did not isolate excitotoxicity pathway specifically
- **Resolution**: Systematic Gene Ontology enrichment analysis of HD modifier genes for NMDAR signaling terms

---

## Discriminating Tests

### Test 1: MSH3-KO × Extrasynaptic NMDAR Measurement
- **Question**: Does blocking somatic CAG expansion normalize extrasynaptic NMDAR redistribution?
- **Design**: Cross Msh3-KO mice with Q140 or YAC128 HD mice. At presymptomatic ages (4-6 months), measure extrasynaptic/synaptic NMDAR current ratio via whole-cell patch clamp and GluN2B surface distribution via immunocytochemistry in acute brain slices.
- **Stratification**: Multiple ages (2, 4, 6, 8 months) to capture temporal dynamics
- **Expected result if excitotoxicity is downstream**: Msh3-KO normalizes NMDAR redistribution proportionally to somatic expansion block
- **Expected result if excitotoxicity is independent**: NMDAR shift occurs even without somatic expansion
- **Impact**: Would formally order the causal chain and determine therapeutic priority

### Test 2: Presymptomatic GluN2B-Selective Antagonist Trial
- **Question**: Does early, targeted NMDAR intervention modify HD progression?
- **Population**: Premanifest HD gene carriers (CAG 40-45), stratified by estimated years to onset (5-15 years), n ≈ 200
- **Intervention**: GluN2B-selective antagonist (e.g., ifenprodil derivative) or Tat-NR2B9c-like peptide; vs. placebo
- **Biomarkers**: Primary: neurofilament light chain (NfL) in CSF/blood, caudate volume (MRI). Secondary: HD-CAB cognitive composite, mHTT in CSF
- **Duration**: 2-3 years
- **Stratification**: By CAG length, MSH3 genotype (to control for somatic expansion rate)
- **Expected result if excitotoxicity is a major early driver**: Slowed NfL rise and caudate atrophy in treatment group

### Test 3: Cell-Type-Specific GluN2B Knockout in HD Models
- **Question**: Does excitotoxicity explain differential D1 vs. D2 MSN vulnerability?
- **Design**: Drd1-Cre and Drd2-Cre × conditional GluN2B-flox × Q140 knock-in mice. Selectively delete GluN2B from each MSN subtype and measure differential rescue of degeneration, motor behavior, and transcriptional profiles.
- **Expected result**: If excitotoxicity drives D2 vulnerability, GluN2B-KO in D2-MSNs should be more protective. If TNF-mediated D1 changes are excitotoxic, GluN2B-KO in D1-MSNs should rescue early synaptic changes.
- **Timeline**: 12-18 months for mouse generation and phenotyping

### Test 4: Single-Cell Multi-Omics Across Human HD Vonsattel Grades
- **Question**: What is the spatiotemporal profile of NMDAR pathway activation in human HD?
- **Sample**: Postmortem striatum from HD patients (Grades 0-4, n ≥ 5 per grade) and age-matched controls
- **Method**: Spatial transcriptomics (Visium/MERFISH) + single-nucleus phosphoproteomics (DAPK1-pS308, p38-pT180/Y182, CREB-pS133)
- **Expected result**: If excitotoxicity is primarily early-stage, NMDAR pathway activation should peak at Grade 0-1 and decline by Grade 3-4

### Test 5: Longitudinal Glutamate Imaging and CSF Metabolomics
- **Question**: Are biphasic glutamate dynamics replicated in human HD?
- **Design**: Serial MRS (glutamate/glutamine ratio in striatum) + mGluR5 PET + CSF kynurenine pathway metabolites (QA, 3-HK, kynurenic acid) in premanifest → early manifest HD cohorts (ENROLL-HD, n ≈ 100)
- **Expected result if biphasic model is correct**: Early elevation followed by decline in striatal glutamate markers; QA/kynurenic acid ratio elevated early

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base, labeled as leads requiring curator verification.*

### Candidate Evidence References

| PMID | Exact Abstract Snippet | Relevance to Hypothesis |
|------|------------------------|------------------------|
| [40461488](https://pubmed.ncbi.nlm.nih.gov/40461488/) | "We found an unexpected reduction in PKD1 protein levels in striatal neurons from HD patients. Similarly, the R6/1 mouse model of HD exhibited progressive PKD1 protein loss, commencing at early disease stages" | Novel vulnerability factor: PKD1 loss amplifies excitotoxic damage in HD MSNs. Human tissue + mouse model evidence. |
| [38776957](https://pubmed.ncbi.nlm.nih.gov/38776957/) | "We have identified transcriptional upregulation of genes encoding N-methyl-D-aspartate (NMDA), α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) and kainate receptors in medium spiny neurons, the cell type preferentially lost early in HD" | Single-cell transcriptomic evidence of glutamate receptor upregulation in prodromal HD. Large animal model (sheep). |
| [33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/) | "Death-associated protein kinase 1 (DAPK1) is a pro-apoptotic kinase highly expressed in neurons during development. In the adult brain, DAPK1 becomes re-activated and recruited to extrasynaptic NMDAR complexes during neuronal death, where it phosphorylates GluN2B at S1303, amplifying toxic receptor function." | Molecular amplifier of extrasynaptic NMDAR toxicity identified. Potential drug target. |
| [36517241](https://pubmed.ncbi.nlm.nih.gov/36517241/) | "We observed an increase in excitatory synaptic strength, as measured by AMPA/NMDA ratios, specifically on direct pathway D1 receptor expressing medium spiny neurons, with no changes on indirect pathway neurons." | Pathway-specific (D1) excitotoxic enhancement; TNF-dependent. Qualifies the hypothesis with cell-type specificity. |
| [39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/) | "Msh3 deficiency ameliorates open-chromatin dysregulation in Q140 neurons. Mechanistically, the fast linear rate of mHtt modal-CAG-repeat expansion in MSNs (8.8 repeats/month) is drastically reduced or stopped by MMR mutants." | Somatic expansion as upstream mechanism; MSH3-KO corrects synaptic defects, repositioning excitotoxicity as downstream. |

### Candidate Pathophysiology Nodes and Edges

1. **Node**: Extrasynaptic GluN2B-NMDAR signaling complex (including PSD-95, DAPK1, p38 MAPK)
   - **Edge**: mHTT → calpain/STEP activation → GluN2B extrasynaptic redistribution → p38 MAPK → MSN death
   - **Evidence**: [PMID: 22668780](https://pubmed.ncbi.nlm.nih.gov/22668780/), [PMID: 22523092](https://pubmed.ncbi.nlm.nih.gov/22523092/), [PMID: 22198502](https://pubmed.ncbi.nlm.nih.gov/22198502/), [PMID: 33250715](https://pubmed.ncbi.nlm.nih.gov/33250715/)

2. **Node**: PKD1 / PRKD1 (neuroprotective kinase)
   - **Edge**: mHTT → ↓PKD1 → ↓neuroprotection → ↑excitotoxic vulnerability
   - **Evidence**: [PMID: 40461488](https://pubmed.ncbi.nlm.nih.gov/40461488/)

3. **Edge (temporal qualifier)**: Biphasic corticostriatal dynamics
   - Excitotoxicity most relevant: presymptomatic → early symptomatic
   - Late stages dominated by: corticostriatal disconnection, cell-autonomous mechanisms
   - **Evidence**: [PMID: 33198566](https://pubmed.ncbi.nlm.nih.gov/33198566/), [PMID: 33016873](https://pubmed.ncbi.nlm.nih.gov/33016873/)

4. **Edge (upstream link)**: Somatic CAG expansion → excitotoxicity pathway
   - MSH3/MMR-driven expansion → longer polyQ → enhanced mHTT-NMDAR interaction
   - **Status**: Inferred, not directly demonstrated — candidate knowledge gap
   - **Evidence**: [PMID: 39938516](https://pubmed.ncbi.nlm.nih.gov/39938516/), [PMID: 38749429](https://pubmed.ncbi.nlm.nih.gov/38749429/))

### Candidate Ontology Terms

- **Cell types**: CL:0000540 (neuron), CL:1001474 (medium spiny neuron — D1 and D2 subtypes), CL:0000127 (astrocyte), CL:0000129 (microglial cell)
- **Biological processes**: GO:0007215 (glutamate receptor signaling pathway), GO:0051402 (neuron apoptotic process), GO:0006298 (mismatch repair), GO:0070997 (neuron death), GO:0006816 (calcium ion transport)
- **Molecular functions**: GO:0004972 (NMDA glutamate receptor activity), GO:0005516 (calmodulin binding)

### Candidate Subtype Restrictions

The excitotoxicity hypothesis most strongly applies to:
- **Disease stage**: Presymptomatic to early symptomatic (Vonsattel Grade 0-2)
- **Cell type**: Striatal MSNs (both D1 and D2, with early D1-specific TNF-mediated effects)
- **Brain region**: Striatum > cortex
- **Molecular target**: GluN2B-containing extrasynaptic NMDARs specifically (not pan-NMDAR)

### Candidate Status Change

- **Current status**: ALTERNATIVE
- **Recommended status**: ALTERNATIVE (retain) — with enhanced annotation
- **Suggested annotation**: "Validated selective-vulnerability amplifier; operates downstream of somatic CAG expansion; most relevant in presymptomatic/early disease stages; clinical actionability limited by trial failures and stage-dependent dynamics. Best framed as one node in a converging multi-mechanism pathogenic network."

### Candidate Knowledge Gaps for KB

1. No direct evidence connecting somatic CAG expansion to NMDAR redistribution (untested causal link)
2. No human in vivo measurement of extrasynaptic NMDAR activation in HD
3. No clinical trial of extrasynaptic-selective or GluN2B-selective NMDAR antagonists in HD
4. No GWAS signal for glutamate receptor pathway genes as HD onset modifiers
5. D1/D2 MSN pathway specificity paradox unresolved
6. Mechanism of continued neurodegeneration after corticostriatal disconnection unknown
7. Quantitative contribution of excitotoxicity vs. other mechanisms not determined

### Candidate Discussion Prompts for Curators

- Should the excitotoxicity hypothesis be reclassified from ALTERNATIVE to CONTRIBUTING_FACTOR with explicit temporal and cell-type qualifiers?
- Is the biphasic model (early excitotoxicity → late disconnection) sufficiently evidenced to add as a temporal restriction edge?
- Should the somatic CAG expansion hypothesis be explicitly annotated as upstream of excitotoxicity in the causal graph?
- Given the absence of GRIN2B/DLG4 signals in HD GWAS, should this be flagged as evidence against excitotoxicity being a rate-limiting step?

---

## Limitations of This Report

1. **Literature search scope**: The 71 papers reviewed were identified through PubMed searches; preprints, conference abstracts, and non-indexed literature were not systematically searched.
2. **Model organism bias**: Most mechanistic evidence comes from YAC128 and R6/2 mouse models, which may not fully recapitulate human HD, particularly regarding the pace of somatic expansion and the degree of corticostriatal disconnection.
3. **Clinical trial coverage**: A systematic review of all NMDAR antagonist trials in HD was not performed; the assessment is based on available review-level evidence.
4. **Temporal limitation**: Literature spans from 1979 to 2025; some early clinical pharmacology studies may have been missed.
5. **No formal quantitative evidence synthesis**: The evidence matrix reflects qualitative judgment of study strength and relevance; no formal meta-analysis was performed.
6. **Single-iteration investigation**: Additional iterations could have explored kynurenine pathway metabolomics, calcium imaging datasets, and HD clinical trial registries in greater depth.
