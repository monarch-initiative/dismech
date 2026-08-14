---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T03:21:18.479112'
end_time: '2026-07-06T04:13:56.531418'
duration_seconds: 3158.05
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Schizophrenia
  category: Psychiatric
  hypothesis_group_id: complement_synaptic_pruning_hypothesis
  hypothesis_label: Complement-Mediated Synaptic Pruning Hypothesis
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: complement_synaptic_pruning_hypothesis\n\
    hypothesis_label: Complement-Mediated Synaptic Pruning Hypothesis\nstatus: EMERGING\n\
    description: Schizophrenia risk alleles that increase complement C4A activity\
    \ may increase complement\n  tagging of vulnerable synapses during adolescent\
    \ and young-adult cortical maturation. Microglia then\n  remove more synaptic\
    \ material than is developmentally appropriate, especially in prefrontal and hippocampal\n\
    \  circuits, creating synaptic-density loss and circuit dysconnectivity that can\
    \ feed into downstream dopamine\n  dysregulation and clinical symptom domains.\n\
    notes: Modeled separately from the canonical dopamine/glutamate framework because\
    \ the complement-C4A link\n  has strong genetic, patient-derived cellular, and\
    \ mouse-model support, but the full human causal chain\n  from C4A dosage to synapse\
    \ loss, dopamine changes, developmental timing, and symptom-domain specificity\n\
    \  remains partially inferred."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 27
artifact_count: 30
artifact_sources:
  openscientist_artifacts_zip: 30
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
- filename: provenance_alternative_models.json
  path: openscientist_artifacts/provenance_alternative_models.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist alternative models
- filename: provenance_alternative_models.png
  path: openscientist_artifacts/provenance_alternative_models.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist alternative models
- filename: provenance_causal_chain.json
  path: openscientist_artifacts/provenance_causal_chain.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain
- filename: provenance_causal_chain.png
  path: openscientist_artifacts/provenance_causal_chain.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain
- filename: provenance_claim_status.json
  path: openscientist_artifacts/provenance_claim_status.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim status
- filename: provenance_claim_status.png
  path: openscientist_artifacts/provenance_claim_status.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim status
- filename: provenance_evidence_matrix.json
  path: openscientist_artifacts/provenance_evidence_matrix.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_evidence_matrix.png
  path: openscientist_artifacts/provenance_evidence_matrix.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_evidence_summary_iter2.json
  path: openscientist_artifacts/provenance_evidence_summary_iter2.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence summary iter2
- filename: provenance_evidence_summary_iter2.png
  path: openscientist_artifacts/provenance_evidence_summary_iter2.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence summary iter2
- filename: provenance_final_dashboard.json
  path: openscientist_artifacts/provenance_final_dashboard.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final dashboard
- filename: provenance_final_dashboard.png
  path: openscientist_artifacts/provenance_final_dashboard.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final dashboard
- filename: provenance_knowledge_gaps.json
  path: openscientist_artifacts/provenance_knowledge_gaps.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
- filename: provenance_knowledge_gaps.png
  path: openscientist_artifacts/provenance_knowledge_gaps.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
- filename: provenance_plot_1.json
  path: openscientist_artifacts/provenance_plot_1.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_1.png
  path: openscientist_artifacts/provenance_plot_1.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_2.json
  path: openscientist_artifacts/provenance_plot_2.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_2.png
  path: openscientist_artifacts/provenance_plot_2.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_3.json
  path: openscientist_artifacts/provenance_plot_3.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_3.png
  path: openscientist_artifacts/provenance_plot_3.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_4.json
  path: openscientist_artifacts/provenance_plot_4.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_4.png
  path: openscientist_artifacts/provenance_plot_4.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_5.json
  path: openscientist_artifacts/provenance_plot_5.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_plot_5.png
  path: openscientist_artifacts/provenance_plot_5.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_plot_6.json
  path: openscientist_artifacts/provenance_plot_6.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 6
- filename: provenance_plot_6.png
  path: openscientist_artifacts/provenance_plot_6.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 6
- filename: provenance_plot_7.json
  path: openscientist_artifacts/provenance_plot_7.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 7
- filename: provenance_plot_7.png
  path: openscientist_artifacts/provenance_plot_7.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 7
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Schizophrenia
- **Category:** Psychiatric

## Target Hypothesis
- **Hypothesis ID:** complement_synaptic_pruning_hypothesis
- **Hypothesis Label:** Complement-Mediated Synaptic Pruning Hypothesis
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: complement_synaptic_pruning_hypothesis
hypothesis_label: Complement-Mediated Synaptic Pruning Hypothesis
status: EMERGING
description: Schizophrenia risk alleles that increase complement C4A activity may increase complement
  tagging of vulnerable synapses during adolescent and young-adult cortical maturation. Microglia then
  remove more synaptic material than is developmentally appropriate, especially in prefrontal and hippocampal
  circuits, creating synaptic-density loss and circuit dysconnectivity that can feed into downstream dopamine
  dysregulation and clinical symptom domains.
notes: Modeled separately from the canonical dopamine/glutamate framework because the complement-C4A link
  has strong genetic, patient-derived cellular, and mouse-model support, but the full human causal chain
  from C4A dosage to synapse loss, dopamine changes, developmental timing, and symptom-domain specificity
  remains partially inferred.
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

# Complement C4A-Mediated Synaptic Pruning Hypothesis in Schizophrenia: A Mechanistic Evidence Review

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — with significant mechanistic revision required.**

The Complement C4A-Mediated Synaptic Pruning Hypothesis posits that schizophrenia risk alleles increasing complement C4A expression lead to excessive complement tagging of synapses during adolescent cortical maturation, with microglia removing more synaptic material than developmentally appropriate, particularly in prefrontal and hippocampal circuits, ultimately creating synaptic-density loss and circuit dysconnectivity that feeds into downstream dopamine dysregulation and clinical symptoms.

After systematic evaluation of 93 primary research papers, reviews, and meta-analyses, the hypothesis is **partially supported** at its genetic and cellular core but requires substantial revision of its effector mechanism, developmental timing, and downstream causal chain. Four foundational claims are well-established: (1) the dose-response relationship between C4A expression and schizophrenia risk, (2) C4 protein localization at synapses, (3) C4A overexpression causing synaptic loss in mouse models, and (4) inverse C4A-mediated vulnerability for schizophrenia vs. autoimmune diseases. However, two central claims of the hypothesis are directly challenged by recent evidence: the microglia-phagocytosis effector mechanism is contested by two contradictory 2025–2026 studies proposing CR3-dependent vs. CR3-independent pathways, and the adolescent developmental timing window is undermined by human postmortem data showing complement expression peaks in toddlers, not teenagers. Furthermore, no direct evidence links C4A to dopamine dysregulation, no clinical trials target the complement pathway for schizophrenia, and peripheral complement biomarker studies show inconsistent directionality across cohorts. C4A contributes a moderate genetic effect (OR ~1.27) but explains well under 1% of total heritability within a highly polygenic architecture of 287+ GWAS loci.

---

## Summary

The complement C4A hypothesis represents one of the most genetically tractable immune-mediated pathways in schizophrenia, anchored by the landmark 2016 Sekar et al. discovery that structurally diverse C4 alleles associate with schizophrenia risk in proportion to their tendency to generate greater C4A expression. This genetic finding has been substantiated by mouse models showing that C4A overexpression reduces cortical synapse density and increases microglial engulfment of synapses, by patient-derived iPSC models demonstrating increased synapse elimination in schizophrenia neural cultures, and by postmortem meta-analyses confirming C4 overexpression alongside downregulation of neuroimmune regulatory brakes (CD46, CX3CL1) in schizophrenia brain tissue.

However, this five-iteration investigation reveals that the hypothesis as originally formulated requires significant mechanistic revision. The proposed effector pathway — microglia phagocytosing complement-tagged synapses via CR3 — is now contested by two recent studies with contradictory findings: one shows CR3-dependent effects operating through reduced microglia-synapse surveillance (not increased engulfment), while another demonstrates CR3-independent synaptic loss driven by impaired AMPAR/GluR1 trafficking through an intracellular SNX27 endosomal mechanism. The claimed adolescent timing window is challenged by human postmortem evidence that complement activators (C1QB, C3, C4 protein) peak in toddlers and decline in teenagers. The downstream link to dopamine dysregulation remains entirely speculative, with no published study connecting C4A variants to dopamine system changes, and recent PET studies showing that striatal dopamine synthesis elevation is not even universal in schizophrenia. After a decade since the foundational genetic discovery, no complement-targeted clinical trials exist for schizophrenia, no symptom-domain specificity data have been generated, and peripheral complement biomarker studies yield inconsistent results across cohorts.

The hypothesis identifies a genuine but modest genetic risk pathway (one of 287+ loci) that likely contributes to synaptic vulnerability through mechanisms more complex than simple microglial over-eating of tagged synapses, operating in a developmental window that may be earlier than adolescence, and interacting with environmental factors such as maternal immune activation.

---

## Key Findings

### Finding 1: C4A Genetic Association Is Proportional to Expression Levels (ESTABLISHED)

The foundational genetic evidence comes from Sekar et al. (2016), who demonstrated that structurally diverse alleles of C4 genes associate with schizophrenia in proportion to their tendency to generate greater C4A expression ([PMID: 26814963](https://pubmed.ncbi.nlm.nih.gov/26814963/)). The study further showed that C4 protein localizes to neuronal synapses, dendrites, axons, and cell bodies, and that in mice, C4 mediates synapse elimination during postnatal development. This represents the strongest genetic association at the MHC locus for schizophrenia. The effect size is moderate for a GWAS locus (OR ~1.27 per unit increase in expression), placing it among the largest common-variant effects for schizophrenia, where typical loci have OR 1.03–1.15. However, C4A is one of ~287+ GWAS loci identified by Trubetskoy et al. (2022; [PMID: 35396580](https://pubmed.ncbi.nlm.nih.gov/35396580/)), with the MHC region accounting for only ~0.5–1% of total SNP-heritability (~24%). No published study has directly quantified what proportion of total schizophrenia variance C4A explains, but it is clearly well under 1%.

### Finding 2: C4A Overexpression Causes Synaptic Loss and Behavioral Changes in Mice (ESTABLISHED)

Yilmaz et al. (2021) provided critical mouse model evidence ([PMID: 33353966](https://pubmed.ncbi.nlm.nih.gov/33353966/)). Human C4A bound synapses more efficiently than C4B. C4A (but not C4B) rescued visual system synaptic refinement deficits in C4 knockout mice. Crucially, C4A overexpression reduced cortical synapse density, increased microglial engulfment of synapses, and altered behavior. An important nuance emerged: **mice without C4 had normal numbers of cortical synapses**, suggesting complement is not required for normal developmental pruning but drives pathological over-pruning when overexpressed. This distinction between normal pruning and pathological excess is fundamental — it means C4A acts as a gain-of-function risk factor, not a disruption of a required developmental process.

### Finding 3: The Effector Mechanism Is Contested — CR3-Dependent vs. CR3-Independent Pathways (CONTRADICTED)

Two 2025–2026 studies report directly contradictory findings on how C4 overexpression leads to synaptic loss, representing a critical unresolved mechanistic debate:

**CR3-dependent model** — Gockel et al. (2026; [PMID: 41903141](https://pubmed.ncbi.nlm.nih.gov/41903141/)): C4-OE effects on synapse density and function were rescued in CR3-deficient mice. However, the mechanism was not increased phagocytosis but rather *decreased* microglial surveilled volume, motility, and frequency of microglial contacts with pre- and postsynaptic structures. This fundamentally revises the "microglia eat too many synapses" narrative to "microglia withdraw surveillance support from synapses."

**CR3-independent model** — Phadke et al. (2025; [PMID: 39227431](https://pubmed.ncbi.nlm.nih.gov/39227431/)): C4-mediated cortical hypoconnectivity was CR3-independent. Instead, C4-OE triggered impaired GluR1/AMPAR trafficking through an intracellular mechanism involving the endosomal protein SNX27. SNX27 overexpression rescued C4 circuit alterations. This proposes a completely non-immune mechanism: C4 acting intracellularly on receptor trafficking rather than extracellularly on microglial phagocytosis.

These contradictory findings fundamentally challenge the hypothesis's core mechanistic claim and suggest the true effector pathway may be more complex — possibly involving both immune and non-immune mechanisms operating in parallel or in different cellular compartments.

{{figure:evidence_matrix.png|caption=Evidence matrix showing the strength and type of evidence for each major claim of the C4A hypothesis}}

### Finding 4: Patient-Derived iPSC Models Show Increased Synapse Elimination (EMERGING)

Sellgren et al. (2019; [PMID: 30718903](https://pubmed.ncbi.nlm.nih.gov/30718903/)) used reprogrammed in vitro models of microglia-mediated synapse engulfment, demonstrating increased synapse elimination in patient-derived neural cultures and isolated synaptosomes. Importantly, excessive pruning reflected abnormalities in *both* microglia-like cells and synaptic structures. C4 risk variants were associated with increased neuronal complement deposition and synapse uptake, **but did not fully explain the observed increase**. This suggests C4A is one contributor among multiple factors driving excessive synapse elimination. Minocycline reduced microglia-mediated synapse uptake in vitro, providing a proof-of-concept for therapeutic intervention, though its use was associated with only a modest decrease in incident schizophrenia risk in electronic health records.

### Finding 5: Developmental Timing Challenge — Complement Peaks in Toddlers, Not Adolescents (CONTRADICTS HYPOTHESIS)

Sager et al. (2021; [PMID: 33190236](https://pubmed.ncbi.nlm.nih.gov/33190236/)) examined human postmortem prefrontal cortex across neonatal to young adult development and found that complement activator transcripts (C1QB and C3) peaked in early neurodevelopment and were highest in toddlers, *declining* in teenagers (ANCOVAs F = 2.41–3.325, p = 0.01–0.05). C4 protein was higher at 1–5 years (H = 16.378, p = 0.012). Microglial complement receptor CD11b peaked in toddler brain (ANCOVA: F = 4.186, p = 0.003). Complement inhibitors (CD46, CD55) increased at school age but did not decrease like complement activators.

This directly challenges the hypothesis's claim that complement-mediated pruning occurs specifically during the adolescent period coinciding with schizophrenia onset. The complement system's peak activity in toddlers suggests either: (a) pathological complement effects begin much earlier than symptom onset, with a long prodromal period; (b) C4A overexpression creates vulnerability during early development that manifests clinically only during later adolescent circuit maturation; or (c) a second, later wave of complement activity not captured in existing developmental studies is responsible.

{{figure:evidence_summary_iter2.png|caption=Summary visualization of causal chain evidence strength highlighting the developmental timing challenge}}

### Finding 6: C4A Shows Selective Inflammatory Network Disruption in First-Episode Psychosis CSF (EMERGING)

Arjmand et al. (2026; [PMID: 42000733](https://pubmed.ncbi.nlm.nih.gov/42000733/)) studied 90 healthy controls and 113 first-episode psychosis patients and found that the CSF C1Q–C4A association was abolished in FEP (z = 0.09, p = 0.40 vs. z = 0.41, p < 0.001 in controls). C4A showed a robust positive directional shift in inflammatory correlations in FEP (z = 3.81, p < 0.0001), while C4B showed a non-significant negative shift. This demonstrates C4A-specific (not C4B) disruption of complement cascade associations in first-episode psychosis, supporting the isoform-specificity predicted by the hypothesis.

### Finding 7: TSPO PET Does Not Support Widespread Microglial Activation (QUALIFIES HYPOTHESIS)

Multiple TSPO PET studies show a *decrease or lack of increase* in TSPO binding in schizophrenia, contradicting expectations of increased microglial activation. Sneeboer et al. (2020; [PMID: 31699629](https://pubmed.ncbi.nlm.nih.gov/31699629/)) demonstrated that TSPO expression is not increased in postmortem brain tissue, not correlated with microglial activation markers, not restricted to microglia, and not upregulated in ex vivo activated human primary microglia. Iliopoulou et al. (2021; [PMID: 34819729](https://pubmed.ncbi.nlm.nih.gov/34819729/)) reviewed that TSPO PET studies in schizophrenia show a decrease or lack of increase in TSPO binding. This challenges any model requiring widespread, detectable microglial activation in the schizophrenic brain, though it does not rule out subtle, regionally restricted, or phenotypically specific microglial changes.

### Finding 8: Sex-Biased C4 Vulnerability — Inverse SZ-SLE Relationship (ESTABLISHED)

Kamitaki et al. (2020; [PMID: 32499649](https://pubmed.ncbi.nlm.nih.gov/32499649/)) demonstrated that higher C4A expression increases schizophrenia risk (more common in men), while lower C4A expression increases SLE/Sjögren's risk (more common in women). This inverse genetic relationship mediated by C4 copy number variation links the complement hypothesis to sex differences in disease prevalence and provides one of the strongest biological validations of the C4A pathway's clinical relevance.

### Finding 9: Genetic Risk Predominantly Affects Glial Cells (SUPPORTS HYPOTHESIS)

Gerstner et al. (2025; [PMID: 40053590](https://pubmed.ncbi.nlm.nih.gov/40053590/)) performed single-nucleus multi-omics on 92 postmortem human OFC samples and found that while diagnosis-associated dysregulation was pronounced in excitatory neurons, genetic risk predominantly affected glial and endothelial cells. This dissociation between genetic risk (glial) and clinical phenotype (neuronal) is consistent with the complement hypothesis — C4A being expressed by glial cells and causing downstream neuronal damage.

### Finding 10: Meta-Analysis Confirms C4 Overexpression and Neuroimmune Brake Failure (EMERGING)

Boughanmi et al. (2026; [PMID: 42276261](https://pubmed.ncbi.nlm.nih.gov/42276261/)) conducted a meta-analysis of 532 schizophrenia and 623 healthy control postmortem brain tissue samples. Schizophrenia was associated with C4 overexpression AND underexpression of neuroimmune regulators CD46 and CX3CL1. Sex-specific transcriptional differences emerged: CD200 (female-specific) and CD59, CX3CR1 (male-specific). The CX3CL1-CX3CR1 axis disruption was observed in both brain and blood. This suggests complement excess co-occurs with a broader failure of neuroimmune homeostasis.

### Finding 11: Peripheral Complement Biomarkers Are Inconsistent Across Cohorts (LIMITS HYPOTHESIS)

Three 2026 studies show contradictory peripheral complement findings: elevated C3 correlating with symptom severity in one cohort ([PMID: 41983246](https://pubmed.ncbi.nlm.nih.gov/41983246/)), elevated C3/C4 in FEP at baseline and follow-up in another ([PMID: 41978241](https://pubmed.ncbi.nlm.nih.gov/41978241/)), but *decreased* C3 in drug-naive FEP in a third ([PMID: 41274180](https://pubmed.ncbi.nlm.nih.gov/41274180/)). Cao et al. (2024; [PMID: 39741241](https://pubmed.ncbi.nlm.nih.gov/39741241/)) found elevated C1–C4 and CH50 in first-episode schizophrenia. The inconsistent directionality undermines the use of peripheral complement as a reliable biomarker and suggests complex compartment-specific regulation.

### Finding 12: Maternal Immune Activation Amplifies Complement Pathway (EMERGING)

Han et al. (2017; [PMID: 28138113](https://pubmed.ncbi.nlm.nih.gov/28138113/)) showed increased C1q in offspring PFC after maternal immune activation (MIA) in mice, preventable by early TrkB agonist treatment. Severance et al. (2014; [PMID: 25195065](https://pubmed.ncbi.nlm.nih.gov/25195065/)) found that maternal C1q was significantly elevated in mothers whose offspring developed psychosis (OR 2.66–6.31, p ≤ 0.008–0.05), linking prenatal immune activation to offspring risk. This gene-environment interaction may amplify the genetic C4A risk.

### Finding 13: Disease-Specific C4A Genotype-Phenotype Correlation in Peripheral Immune Cells (EMERGING)

Kalinowski et al. (2026; [PMID: 42113976](https://pubmed.ncbi.nlm.nih.gov/42113976/)) found that C4A gene copies correlated with C4 protein only in neutrophils and only in schizophrenia (Spearman's rho = 0.63, 95% CI: 0.12 to 0.89). No such correlation existed in controls. C4 protein activation did not coincide with expected changes to other complement cascade proteins, suggesting a non-canonical source of C4 activation. Though the sample was small (15 patients, 21 controls), this disease-state-specific finding suggests that immune activation in schizophrenia unmasks the C4A genotype-phenotype relationship.

### Finding 14: No Clinical Translation After 10 Years (ABSENCE OF EVIDENCE)

Systematic search found: (1) No registered clinical trials targeting complement components (C4, C3, CR3 inhibitors) for schizophrenia prevention or treatment. Minocycline trials target broad anti-inflammatory mechanisms (effect size = 0.38 for total symptoms; [PMID: 30864461](https://pubmed.ncbi.nlm.nih.gov/30864461/)), not complement specifically. (2) No study correlates C4A genotype with specific symptom domains. (3) No study stratifies treatment response by C4A genotype. (4) CNS penetrance of complement inhibitors remains a major pharmacological barrier.

{{figure:claim_status.png|caption=Claim status assessment heatmap showing established, emerging, contradicted, and speculative claims within the C4A hypothesis}}

---

## Mechanistic Causal Chain

The hypothesis proposes the following causal chain from upstream trigger to clinical manifestation. Below, each step is annotated with the strength of current evidence:

```
UPSTREAM TRIGGER
┌─────────────────────────────────────────────────────────────────┐
│ C4A Risk Alleles (CNV/expression variants)                      │
│ → Increased C4A mRNA/protein expression in brain                │
│ EVIDENCE: ██████████ ESTABLISHED (Sekar 2016, OR~1.27)          │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
ENVIRONMENTAL MODIFIERS (parallel input)
┌─────────────────────────────────────────────────────────────────┐
│ Maternal immune activation → ↑C1q in offspring PFC              │
│ EVIDENCE: ██████░░░░ EMERGING (Han 2017, Severance 2014)        │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
SYNAPTIC TAGGING
┌─────────────────────────────────────────────────────────────────┐
│ C4A protein deposits on vulnerable synapses                     │
│ → C4A binds synapses more efficiently than C4B                  │
│ EVIDENCE: ████████░░ ESTABLISHED (Yilmaz 2021)                  │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
EFFECTOR MECHANISM ← ← ← CONTESTED
┌─────────────────────────────────────────────────────────────────┐
│ MODEL A: CR3-dependent reduced microglia surveillance           │
│   (Gockel 2026) — ↓surveilled volume, motility, contacts       │
│ MODEL B: CR3-independent impaired AMPAR/GluR1 trafficking       │
│   (Phadke 2025) — intracellular SNX27 endosomal pathway        │
│ ORIGINAL MODEL: CR3-dependent microglial phagocytosis           │
│   (Yilmaz 2021) — ↑engulfment of tagged synapses               │
│ EVIDENCE: ██░░░░░░░░ CONTRADICTED/UNRESOLVED                   │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
DEVELOPMENTAL TIMING ← ← ← CHALLENGED
┌─────────────────────────────────────────────────────────────────┐
│ Hypothesized: Adolescent cortical maturation window             │
│ Observed: Complement peaks in toddlers (1-5y), declines in     │
│           teenagers (Sager 2021)                                │
│ EVIDENCE: ██░░░░░░░░ CONTRADICTED                               │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
SYNAPTIC LOSS
┌─────────────────────────────────────────────────────────────────┐
│ Reduced synaptic density in PFC and hippocampus                 │
│ → Confirmed by SV2A PET, postmortem electron microscopy         │
│ EVIDENCE: ████████░░ ESTABLISHED (multiple PET studies)         │
│ NOTE: Synaptic loss is multiply determined; C4A is one path     │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
CIRCUIT DYSCONNECTIVITY
┌─────────────────────────────────────────────────────────────────┐
│ Disrupted PFC-hippocampal connectivity                          │
│ EVIDENCE: ██████░░░░ EMERGING (neuroimaging studies)             │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
DOPAMINE DYSREGULATION ← ← ← NO DIRECT EVIDENCE
┌─────────────────────────────────────────────────────────────────┐
│ Hypothesized: Synapse loss → altered DA signaling               │
│ No study links C4A to dopamine changes                          │
│ DA synthesis elevation is not universal (Eisenberg 2022)        │
│ EVIDENCE: ░░░░░░░░░░ SPECULATIVE                                │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
CLINICAL SYMPTOMS ← ← ← NO SPECIFICITY DATA
┌─────────────────────────────────────────────────────────────────┐
│ Positive, negative, cognitive symptom domains                   │
│ No study links C4A genotype to specific symptom domains         │
│ EVIDENCE: ░░░░░░░░░░ SPECULATIVE                                │
└──────────────────────────┘
```

The causal chain is strong at the top (genetics → synaptic tagging) and at the level of synaptic density reduction (independently confirmed). However, the connecting mechanism between tagging and loss is contested, the developmental timing is challenged, and the downstream links to dopamine and symptom specificity are entirely inferred with no direct evidence.

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|-------------------|-------------|---------|------------|
| 1 | [PMID: 26814963](https://pubmed.ncbi.nlm.nih.gov/26814963/) (Sekar 2016) | Human genetic | **Supports** | C4A expression → SZ risk | Dose-response: C4 alleles associate with SZ proportional to C4A expression | General SZ (PGC GWAS) | HIGH — large GWAS, replicated |
| 2 | [PMID: 33353966](https://pubmed.ncbi.nlm.nih.gov/33353966/) (Yilmaz 2021) | Model organism | **Supports** | C4A-OE → synaptic loss | C4A-OE ↓synapse density, ↑microglial engulfment; C4 KO = normal synapses | Mouse cortex | HIGH — causal manipulation |
| 3 | [PMID: 41903141](https://pubmed.ncbi.nlm.nih.gov/41903141/) (Gockel 2026) | Model organism | **Qualifies** | CR3 dependence of C4 effects | C4-OE effects rescued by CR3 KO; mechanism is ↓microglia surveillance, not ↑engulfment | Mouse PFC | MODERATE — contradicts Phadke |
| 4 | [PMID: 39227431](https://pubmed.ncbi.nlm.nih.gov/39227431/) (Phadke 2025) | Model organism | **Qualifies** | Effector mechanism | C4-mediated hypoconnectivity is CR3-independent; acts via SNX27/AMPAR trafficking | Mouse cortex | MODERATE — contradicts Gockel |
| 5 | [PMID: 30718903](https://pubmed.ncbi.nlm.nih.gov/30718903/) (Sellgren 2019) | In vitro (iPSC) | **Supports** | Patient cells show ↑pruning | ↑Synapse elimination in SZ patient cells; C4 risk variants contribute but don't fully explain | Patient-derived iPSC | MODERATE — in vitro artifact risk |
| 6 | [PMID: 33190236](https://pubmed.ncbi.nlm.nih.gov/33190236/) (Sager 2021) | Human postmortem | **Refutes** | Adolescent timing window | Complement activators peak in toddlers, decline in teenagers | Human PFC development | HIGH — direct developmental measurement |
| 7 | [PMID: 42000733](https://pubmed.ncbi.nlm.nih.gov/42000733/) (Arjmand 2026) | Human clinical | **Supports** | C4A-specific dysregulation in psychosis | C1Q-C4A association abolished in FEP CSF; C4A inflammatory shift (z=3.81) | First-episode psychosis | MODERATE — cross-sectional |
| 8 | [PMID: 42276261](https://pubmed.ncbi.nlm.nih.gov/42276261/) (Boughanmi 2026) | Meta-analysis | **Supports** | C4 overexpression + neuroimmune brake failure | C4 overexpressed, CD46/CX3CL1 underexpressed in SZ brain; sex-specific patterns | 532 SZ, 623 HC postmortem | MODERATE — meta-analysis of heterogeneous data |
| 9 | [PMID: 31699629](https://pubmed.ncbi.nlm.nih.gov/31699629/) (Sneeboer 2020) | Human postmortem | **Refutes** | Microglial activation in SZ | TSPO not increased, not correlated with activation markers, not microglia-specific | SZ postmortem brain | HIGH — challenges microglial activation premise |
| 10 | [PMID: 32499649](https://pubmed.ncbi.nlm.nih.gov/32499649/) (Kamitaki 2020) | Human genetic | **Supports** | C4 sex-biased vulnerability | High C4A → SZ risk (male-biased); Low C4A → SLE risk (female-biased) | Population genetics | HIGH — large datasets, replicated |
| 11 | [PMID: 40053590](https://pubmed.ncbi.nlm.nih.gov/40053590/) (Gerstner 2025) | Human multi-omics | **Supports** | Genetic risk in glia, phenotype in neurons | Genetic risk → glial cells; clinical dysregulation → excitatory neurons | 92 postmortem OFC samples | HIGH — large multi-omics dataset |
| 12 | [PMID: 42113976](https://pubmed.ncbi.nlm.nih.gov/42113976/) (Kalinowski 2026) | Human clinical | **Supports** | C4A genotype-phenotype link | C4A gene copies correlate with C4 protein only in neutrophils, only in SZ (rho=0.63) | 15 SZ, 21 HC peripheral blood | LOW — small sample size |
| 13 | [PMID: 28138113](https://pubmed.ncbi.nlm.nih.gov/28138113/) (Han 2017) | Model organism | **Supports** | MIA → ↑complement in offspring | MIA ↑C1q in PFC of adult offspring; prevented by TrkB agonist | Mouse MIA model | MODERATE — animal model |
| 14 | [PMID: 25195065](https://pubmed.ncbi.nlm.nih.gov/25195065/) (Severance 2014) | Human clinical | **Supports** | Maternal complement → offspring psychosis | Maternal C1q elevated (OR 2.66–6.31) in mothers of offspring who developed psychosis | 55 matched maternal serum pairs | MODERATE — small sample, prospective |
| 15 | [PMID: 34789848](https://pubmed.ncbi.nlm.nih.gov/34789848/) (Eisenberg 2022) | Human PET | **Refutes** | DA synthesis elevation is universal | No elevation of striatal DA synthesis capacity in two medication-free SZ cohorts | Med-free SZ patients | HIGH — challenges downstream dopamine link |
| 16 | [PMID: 38906225](https://pubmed.ncbi.nlm.nih.gov/38906225/) (Coyle 2024) | Review | **Competing** | Glutamatergic synapse pathology | ≥30 GWAS risk genes encode proteins at glutamatergic synapses; inhibit NMDAR function | Review-level evidence | MODERATE — review synthesis |
| 17 | [PMID: 41274180](https://pubmed.ncbi.nlm.nih.gov/41274180/) (Zhang 2026) | Human clinical | **Qualifies** | Peripheral complement as biomarker | *Decreased* C3 in drug-naive FEP vs. controls (contradicts other studies showing elevation) | 71 FEP, 92 HC | MODERATE — contradicts other cohorts |
| 18 | [PMID: 40752823](https://pubmed.ncbi.nlm.nih.gov/40752823/) | In vitro | **Qualifies** | C4 acts on astrocytes too | Exogenous C4 induces astrocyte maturation/reactivity via MAPK/ERK and mTORC1 suppression | hiPSC-derived astrocytes | MODERATE — in vitro, new mechanism |

{{figure:final_dashboard.png|caption=Comprehensive hypothesis assessment dashboard showing evidence strength, claim status, and knowledge gaps}}

---

## Alternative and Competing Models

### 1. Glutamate/NMDA Receptor Hypofunction Hypothesis
**Relationship: Parallel mechanism with synaptic convergence**

At least 30 GWAS risk genes encode proteins localized to the glutamatergic synapse ([PMID: 38906225](https://pubmed.ncbi.nlm.nih.gov/38906225/)). NMDAR hypofunction leads to GABAergic interneuron dysfunction, E/I imbalance, and cortical disinhibition. This pathway explains more genetic variance than C4A alone, directly addresses glutamatergic synaptic spine loss found in postmortem studies, and has more direct connections to all three symptom domains. The glutamate and complement pathways may converge at the synapse but operate through independent genetic architectures.

### 2. GABAergic Parvalbumin Interneuron Deficit Hypothesis
**Relationship: Potential downstream consequence or parallel mechanism**

PV interneuron deficits are consistently found in postmortem studies and animal models ([PMID: 37041206](https://pubmed.ncbi.nlm.nih.gov/37041206/)). Pharmacogenetic activation of PV interneurons in PFC rescues cognitive deficits in schizophrenia models. Complement-mediated synaptic loss could preferentially target PV interneuron inputs, but this has not been directly demonstrated. Alternatively, PV interneuron deficits may arise independently through NMDAR hypofunction or other developmental insults.

### 3. Dopamine Synthesis Dysregulation
**Relationship: Hypothesized downstream consequence, but evidence is weak**

Elevated striatal dopamine synthesis capacity is a hallmark finding, but Eisenberg et al. (2022; [PMID: 34789848](https://pubmed.ncbi.nlm.nih.gov/34789848/)) found no elevation in two medication-free cohorts, suggesting it is not universal. TAAR1 agonists can reduce DA synthesis ([PMID: 41130556](https://pubmed.ncbi.nlm.nih.gov/41130556/)). No study has linked C4A variants to dopamine changes, making the complement → dopamine link entirely speculative.

### 4. Maternal Immune Activation / Gene-Environment Interaction
**Relationship: Upstream cause and effect modifier**

MIA may amplify complement pathway activation in genetically susceptible individuals. This model helps explain why not all individuals with high C4A expression develop schizophrenia and is supported by mouse ([PMID: 28138113](https://pubmed.ncbi.nlm.nih.gov/28138113/)) and human maternal serum ([PMID: 25195065](https://pubmed.ncbi.nlm.nih.gov/25195065/)) data.

### 5. Broader Neuroimmune Dysregulation
**Relationship: Superordinate framework**

The meta-analysis by Boughanmi et al. (2026; [PMID: 42276261](https://pubmed.ncbi.nlm.nih.gov/42276261/)) shows that C4 overexpression co-occurs with downregulation of neuroimmune regulators (CD46, CX3CL1) in schizophrenia brain, with sex-specific patterns. This suggests complement excess may be part of a broader failure of neuroimmune homeostasis, not an isolated pathway.

{{figure:alternative_models.png|caption=Comparison of alternative and competing mechanistic hypotheses for schizophrenia with relationship to C4A hypothesis}}

---

## Limitations and Knowledge Gaps

### Critical Unknown: Effector Mechanism
**Scope:** The downstream pathway from C4A synaptic tagging to synaptic loss is unresolved. Two contradictory models (CR3-dependent microglia surveillance changes vs. CR3-independent intracellular AMPAR trafficking) cannot both be correct as primary mechanisms in the same cellular context. **What was checked:** Two primary research papers from 2025–2026 (PMIDs 41903141, 39227431). **Resolution needed:** Direct comparison of CR3 KO effects in the same experimental paradigm, with cell-type-specific and circuit-specific readouts.

### Critical Unknown: Developmental Timing
**Scope:** The hypothesis claims adolescent pruning as the critical window, but complement expression peaks in toddlers. **What was checked:** Sager et al. 2021 postmortem developmental trajectory (PMID 33190236). **Resolution needed:** Longitudinal complement measurements in the same individuals from childhood through young adulthood, ideally with CSF sampling; determination of whether there is a "second wave" of complement activity in adolescence not captured by mRNA/protein snapshots.

### Missing Link: C4A → Dopamine
**Scope:** No published study connects C4A genetic variants, complement activation, or synaptic pruning to any dopamine system parameter. **What was checked:** PubMed searches for C4A + dopamine, complement + dopamine + schizophrenia. **Resolution needed:** C4A genotype-stratified dopamine PET studies; C4 manipulation in dopamine-sensitive behavioral paradigms with dopamine release measurements.

### Missing Data: Symptom Domain Specificity
**Scope:** No study has correlated C4A genotype with positive, negative, or cognitive symptom severity. **What was checked:** PubMed searches for C4A + symptoms + schizophrenia. **Resolution needed:** Genotype-phenotype studies in large clinical cohorts with dimensional symptom assessments.

### Inconsistent Biomarkers: Peripheral Complement
**Scope:** Peripheral C3 and C4 measurements show contradictory directions across cohorts (elevated in some, decreased in others). **What was checked:** Four 2024–2026 clinical studies (PMIDs 39741241, 41983246, 41978241, 41274180). **Resolution needed:** Standardized multi-center complement biomarker study with harmonized assays, matched for medication status, illness stage, and demographics.

### Source-Level Absence: Clinical Trials
**Scope:** No clinical trials target complement components for schizophrenia. Minocycline trials target broad anti-inflammatory mechanisms, not complement specifically. CNS penetrance of complement inhibitors remains a major pharmacological barrier. **What was checked:** ClinicalTrials.gov, systematic reviews of anti-inflammatory trials in schizophrenia. **Resolution needed:** Development of CNS-penetrant complement modulators; phase I safety studies in high-risk populations.

### Source-Level Absence: Genotype-Treatment Interaction
**Scope:** No study stratifies antipsychotic treatment response by C4A genotype. **Resolution needed:** Retrospective pharmacogenomic analysis in existing biobank cohorts.

### Incomplete: C4 Effects Beyond Microglia
**Scope:** Recent evidence shows C4 directly affects astrocyte maturation and reactivity ([PMID: 40752823](https://pubmed.ncbi.nlm.nih.gov/40752823/)), and sparse neuronal C4-OE triggers widespread transcriptional changes across neural circuits ([PMID: 40502190](https://pubmed.ncbi.nlm.nih.gov/40502190/)). These non-microglial effects are poorly characterized. **Resolution needed:** Cell-type-specific C4 manipulation studies with comprehensive readouts across neurons, astrocytes, oligodendrocytes, and microglia.

{{figure:knowledge_gaps.png|caption=Knowledge gaps table showing unresolved causal steps, missing evidence, and experimental priorities}}

---

## Proposed Follow-Up Experiments and Discriminating Tests

### Priority 1: Resolve the CR3-Dependent vs. CR3-Independent Debate
- **Design:** Compare C4A-OE effects in CR3 KO vs. WT mice using identical experimental protocols, measuring both microglial surveillance metrics (Gockel paradigm) AND intracellular AMPAR trafficking (Phadke paradigm) simultaneously
- **Expected result:** If both mechanisms contribute, rescue should be partial with either CR3 KO or SNX27-OE alone, complete with both
- **Model system:** Mouse with C4A-OE via in utero electroporation
- **Discriminates:** Whether the hypothesis requires immune (microglial) or non-immune (intracellular trafficking) mechanism, or both

### Priority 2: Longitudinal Complement Measurement Across Human Development
- **Design:** Prospective cohort study of at-risk youth (e.g., 22q11.2 deletion carriers or offspring of affected parents) with serial CSF complement measurements from childhood through young adulthood
- **Biomarkers:** CSF C4A, C4B, C3, C1q; plasma complement panel; SV2A PET for synaptic density at key developmental milestones
- **Expected result if hypothesis is correct:** C4A levels should correlate with synaptic density decline and precede symptom onset
- **Discriminates:** Whether the adolescent timing claim can be rescued or must be abandoned

### Priority 3: C4A Genotype-Stratified Dopamine PET
- **Design:** F-DOPA PET in first-episode patients and high-risk individuals stratified by C4A copy number/predicted expression
- **Expected result if hypothesis is correct:** Higher C4A expression should predict lower SV2A binding AND higher dopamine synthesis capacity
- **Expected result if competing models are correct:** No correlation between C4A and dopamine metrics
- **Discriminates:** Whether the complement → dopamine link exists or should be removed from the causal chain

### Priority 4: Symptom Domain Mapping
- **Design:** Large biobank analysis (e.g., UK Biobank, PGC) correlating C4 structural variants with dimensional symptom profiles
- **Stratification:** By sex (given Kamitaki 2020 findings), age of onset, illness stage
- **Expected result:** C4A should preferentially associate with negative/cognitive symptoms if complement-mediated synaptic loss drives deficit phenotype
- **Discriminates:** Whether C4A defines a clinical subtype or contributes non-specifically to risk

### Priority 5: CNS-Penetrant Complement Modulator Trial
- **Design:** Proof-of-concept trial of ANX005 (anti-C1q antibody) or other complement inhibitor in clinical high-risk individuals with elevated C4A expression
- **Primary outcome:** SV2A PET synaptic density change over 12 months
- **Secondary outcomes:** Conversion to psychosis, cognitive function, negative symptoms
- **Stratification:** By C4A genotype to test precision medicine approach
- **Discriminates:** Whether complement inhibition can prevent synaptic loss and psychosis conversion

### Priority 6: Multi-Center Harmonized Peripheral Complement Biomarker Study
- **Design:** Standardized complement panel (C1–C5, C4A/C4B separately, CH50, C3a, C5a) across ≥5 sites, ≥500 FEP patients, medication-naive, with longitudinal follow-up
- **Goal:** Resolve directional inconsistency and determine whether peripheral complement reliably reflects CNS complement status
- **Discriminates:** Whether peripheral complement can serve as a clinically useful biomarker

---

## Curation Leads (Requiring Curator Verification)

### Candidate Status Change
- **Current status:** EMERGING
- **Recommended status:** Maintain EMERGING, but add qualifier: "mechanistic revision required for effector pathway and developmental timing"
- **Rationale:** The genetic core is strong, but two central mechanistic claims are contradicted by recent primary evidence

### Candidate Evidence References
1. Gockel 2026 ([PMID: 41903141](https://pubmed.ncbi.nlm.nih.gov/41903141/)): *"C4-OE decreases microglial surveilled volume, motility, and the frequency of microglial contacts with pre- and postsynaptic structures. These changes are abolished by CR3 deficiency."* — Revises phagocytosis model to surveillance withdrawal model
2. Phadke 2025 ([PMID: 39227431](https://pubmed.ncbi.nlm.nih.gov/39227431/)): *"C4-mediated cortical hypoconnectivity is CR3-independent. Instead, C4-OE triggers impaired GluR1 trafficking through an intracellular mechanism involving the endosomal protein SNX27"* — Proposes non-immune effector mechanism
3. Sager 2021 ([PMID: 33190236](https://pubmed.ncbi.nlm.nih.gov/33190236/)): *"complement activator (C1QB and C3) transcripts peaked in early neurodevelopment, and were highest in toddlers, declining in teenagers"* — Challenges adolescent timing
4. Kalinowski 2026 ([PMID: 42113976](https://pubmed.ncbi.nlm.nih.gov/42113976/)): *"We found a large positive correlation between the number of C4A gene copies and the amount of C4 protein only in neutrophils and only in the schizophrenia group (Spearman's rho = 0.63)"* — Novel disease-state-specific genotype-phenotype finding
5. Boughanmi 2026 ([PMID: 42276261](https://pubmed.ncbi.nlm.nih.gov/42276261/)): *"In brain tissue, SZ was associated with C4 overexpression and underexpression of CD46 and CX3CL1. Sex-specific transcriptional differences emerged for CD200 (female-specific) and CD59, CX3CR1 (male-specific)"* — Coordinated complement/neuroimmune brake dysregulation
6. Arjmand 2026 ([PMID: 42000733](https://pubmed.ncbi.nlm.nih.gov/42000733/)): *"In controls, C4A and C4B were positively associated with C1Q... whereas in FEP, the CSF C1Q-C4A association was abolished"* — C4A-specific CSF network disruption

### Candidate Pathophysiology Nodes/Edges
- **New node:** SNX27 endosomal pathway (Phadke 2025) as alternative effector mechanism
- **New node:** Astrocyte maturation/reactivity induced by C4 ([PMID: 40752823](https://pubmed.ncbi.nlm.nih.gov/40752823/))
- **Contested edge:** C4A → CR3-mediated microglial phagocytosis (contested; may need bifurcation into CR3-dependent surveillance and CR3-independent AMPAR trafficking)
- **Missing edge:** C4A → dopamine dysregulation (no evidence; should be flagged as speculative)
- **New edge:** Maternal immune activation → C1q in offspring PFC → amplified complement vulnerability

### Candidate Ontology Terms
- **Cell types:** CL:0000129 (microglial cell), CL:0000127 (astrocyte), CL:0000540 (neuron), CL:0000775 (neutrophil — for peripheral biomarker findings)
- **Biological processes:** GO:0006958 (complement activation, classical pathway), GO:0098883 (synapse pruning), GO:0007268 (chemical synaptic transmission), GO:0016079 (synaptic vesicle exocytosis)
- **Pathways:** Complement cascade (KEGG:hsa04610), AMPAR trafficking/recycling

### Candidate Knowledge Gaps for KB
1. **Effector mechanism bifurcation:** CR3-dependent surveillance vs. CR3-independent AMPAR trafficking — requires direct experimental comparison
2. **Developmental timing mismatch:** Complement peaks in toddlers vs. hypothesized adolescent window — unresolved
3. **Dopamine link absent:** No direct evidence for complement → dopamine causal step
4. **Clinical translation gap:** 10 years post-discovery, no complement-targeted trials for schizophrenia
5. **Peripheral biomarker inconsistency:** Complement levels elevated in some FEP cohorts, decreased in others

### Candidate Discussion Prompts for Curators
- Should the hypothesis be reformulated as "early developmental complement vulnerability" rather than "adolescent pruning excess"?
- Is the effector mechanism better described as "complement-modulated synaptic maintenance failure" rather than "complement-mediated synaptic pruning"?
- Should the C4A pathway be modeled as one contributor to a multi-pathway synaptic convergence model rather than as a standalone hypothesis?

---

## Evidence Base: Key Literature

| Paper | PMID | Role in Analysis |
|-------|------|-----------------|
| Sekar et al. 2016, *Nature* | [26814963](https://pubmed.ncbi.nlm.nih.gov/26814963/) | Foundational genetic evidence for C4A–SZ association |
| Yilmaz et al. 2021 | [33353966](https://pubmed.ncbi.nlm.nih.gov/33353966/) | Mouse model: C4A-OE → synaptic loss |
| Gockel et al. 2026 | [41903141](https://pubmed.ncbi.nlm.nih.gov/41903141/) | CR3-dependent surveillance mechanism |
| Phadke et al. 2025 | [39227431](https://pubmed.ncbi.nlm.nih.gov/39227431/) | CR3-independent AMPAR trafficking mechanism |
| Sellgren et al. 2019 | [30718903](https://pubmed.ncbi.nlm.nih.gov/30718903/) | Patient iPSC model of synapse elimination |
| Sager et al. 2021 | [33190236](https://pubmed.ncbi.nlm.nih.gov/33190236/) | Developmental timing of complement expression |
| Arjmand et al. 2026 | [42000733](https://pubmed.ncbi.nlm.nih.gov/42000733/) | CSF C4A network disruption in FEP |
| Boughanmi et al. 2026 | [42276261](https://pubmed.ncbi.nlm.nih.gov/42276261/) | Meta-analysis: C4 overexpression + neuroimmune brake failure |
| Kamitaki et al. 2020 | [32499649](https://pubmed.ncbi.nlm.nih.gov/32499649/) | Sex-biased C4 vulnerability (SZ vs. SLE) |
| Sneeboer et al. 2020 | [31699629](https://pubmed.ncbi.nlm.nih.gov/31699629/) | TSPO not valid for microglial activation in SZ |
| Iliopoulou et al. 2021 | [34819729](https://pubmed.ncbi.nlm.nih.gov/34819729/) | TSPO PET findings in schizophrenia |
| Gerstner et al. 2025 | [40053590](https://pubmed.ncbi.nlm.nih.gov/40053590/) | Genetic risk in glia, phenotype in neurons |
| Kalinowski et al. 2026 | [42113976](https://pubmed.ncbi.nlm.nih.gov/42113976/) | C4A gene-protein correlation in SZ neutrophils |
| Eisenberg et al. 2022 | [34789848](https://pubmed.ncbi.nlm.nih.gov/34789848/) | No DA synthesis elevation in med-free SZ |
| Coyle 2024 | [38906225](https://pubmed.ncbi.nlm.nih.gov/38906225/) | Glutamatergic synapse as alternative pathway |
| Trubetskoy et al. 2022 | [35396580](https://pubmed.ncbi.nlm.nih.gov/35396580/) | 287 GWAS loci for schizophrenia |
| Akingbuwa et al. 2022 | [35665764](https://pubmed.ncbi.nlm.nih.gov/35665764/) | Common and rare variants converge on synaptic processes |
| Han et al. 2017 | [28138113](https://pubmed.ncbi.nlm.nih.gov/28138113/) | MIA → ↑C1q in offspring PFC |
| Severance et al. 2014 | [25195065](https://pubmed.ncbi.nlm.nih.gov/25195065/) | Maternal C1q predicts offspring psychosis |
| Cao et al. 2024 | [39741241](https://pubmed.ncbi.nlm.nih.gov/39741241/) | Elevated serum complement in FEP |
| Szwajca et al. 2026 | [41983246](https://pubmed.ncbi.nlm.nih.gov/41983246/) | C3 correlates with clinical severity |
| Sarikavak et al. 2026 | [41978241](https://pubmed.ncbi.nlm.nih.gov/41978241/) | Elevated C3/C4 in FEP at baseline and follow-up |
| Zhang et al. 2026 | [41274180](https://pubmed.ncbi.nlm.nih.gov/41274180/) | Decreased C3 in FEP — contradicts elevation studies |
| Chamberlin et al. 2023 | [37041206](https://pubmed.ncbi.nlm.nih.gov/37041206/) | PV interneuron deficits and cognitive rescue |
| Howes et al. 2026 | [41130556](https://pubmed.ncbi.nlm.nih.gov/41130556/) | TAAR1 agonist reduces DA synthesis in SZ |
| Cho et al. 2019 | [30864461](https://pubmed.ncbi.nlm.nih.gov/30864461/) | Anti-inflammatory agents meta-analysis in SZ |

---

*Report generated: July 6, 2026. Based on systematic review of 93 papers across 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist alternative models](openscientist_artifacts/provenance_alternative_models.json)
![OpenScientist alternative models](openscientist_artifacts/provenance_alternative_models.png)
- [OpenScientist causal chain](openscientist_artifacts/provenance_causal_chain.json)
![OpenScientist causal chain](openscientist_artifacts/provenance_causal_chain.png)
- [OpenScientist claim status](openscientist_artifacts/provenance_claim_status.json)
![OpenScientist claim status](openscientist_artifacts/provenance_claim_status.png)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist evidence summary iter2](openscientist_artifacts/provenance_evidence_summary_iter2.json)
![OpenScientist evidence summary iter2](openscientist_artifacts/provenance_evidence_summary_iter2.png)
- [OpenScientist final dashboard](openscientist_artifacts/provenance_final_dashboard.json)
![OpenScientist final dashboard](openscientist_artifacts/provenance_final_dashboard.png)
- [OpenScientist knowledge gaps](openscientist_artifacts/provenance_knowledge_gaps.json)
![OpenScientist knowledge gaps](openscientist_artifacts/provenance_knowledge_gaps.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)
- [OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.json)
![OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.png)
- [OpenScientist plot 6](openscientist_artifacts/provenance_plot_6.json)
![OpenScientist plot 6](openscientist_artifacts/provenance_plot_6.png)
- [OpenScientist plot 7](openscientist_artifacts/provenance_plot_7.json)
![OpenScientist plot 7](openscientist_artifacts/provenance_plot_7.png)