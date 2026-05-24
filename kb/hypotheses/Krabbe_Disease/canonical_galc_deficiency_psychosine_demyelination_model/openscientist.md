---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-24T15:57:07.426630'
end_time: '2026-05-24T16:48:56.316286'
duration_seconds: 3108.89
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Krabbe Disease
  category: Genetic
  hypothesis_group_id: canonical_galc_deficiency_psychosine_demyelination_model
  hypothesis_label: Canonical GALC Deficiency / Psychosine-Mediated Demyelination
    Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_galc_deficiency_psychosine_demyelination_model\n\
    hypothesis_label: Canonical GALC Deficiency / Psychosine-Mediated Demyelination\
    \ Model\nstatus: CANONICAL\ndescription: Krabbe disease (globoid cell leukodystrophy)\
    \ is an autosomal recessive lysosomal storage\n  disorder caused by loss-of-function\
    \ variants in GALC encoding galactocerebrosidase. Loss of GALC activity\n  prevents\
    \ lysosomal hydrolysis of galactosylceramide but, critically, also fails to clear\
    \ its toxic deacylated\n  lyso-derivative galactosylsphingosine (psychosine).\
    \ Psychosine accumulation in oligodendrocytes and\n  Schwann cells triggers apoptosis\
    \ of myelin-forming cells, secondary lipid-laden multinucleated macrophages\n\
    \  (globoid cells), and progressive CNS and peripheral demyelination. The infantile\
    \ form (~85% of cases)\n  presents in the first 6 months with irritability, hypertonia,\
    \ opisthotonus, seizures, blindness, and\n  death by age 2-3 in untreated patients.\
    \ Pre-symptomatic hematopoietic stem cell transplantation (the\n  only available\
    \ disease-modifying therapy), the twitcher mouse model (Galc^trs/trs) faithfully\
    \ recapitulating\n  the human phenotype, and AAV-GALC gene therapy corroborate\
    \ the GALC-deficiency / psychosine-toxicity\n  / demyelination axis as the canonical\
    \ pathogenic mechanism.\nevidence:\n- reference: PMID:31527255\n  reference_title:\
    \ 'Globoid cell leukodystrophy: Insights from CRISPR/Cas9 modeling.'\n  supports:\
    \ SUPPORT\n  evidence_source: OTHER\n  snippet: Infantile globoid cell leukodystrophy\
    \ (GLD, Krabbe disease) is a fatal\n  explanation: |\n    Existing canonical mechanism\
    \ citation in the dismech knowledge base, used as the seed for the hypothesis-search\
    \ deep-research run."
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
citation_count: 33
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Krabbe Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_galc_deficiency_psychosine_demyelination_model
- **Hypothesis Label:** Canonical GALC Deficiency / Psychosine-Mediated Demyelination Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_galc_deficiency_psychosine_demyelination_model
hypothesis_label: Canonical GALC Deficiency / Psychosine-Mediated Demyelination Model
status: CANONICAL
description: Krabbe disease (globoid cell leukodystrophy) is an autosomal recessive lysosomal storage
  disorder caused by loss-of-function variants in GALC encoding galactocerebrosidase. Loss of GALC activity
  prevents lysosomal hydrolysis of galactosylceramide but, critically, also fails to clear its toxic deacylated
  lyso-derivative galactosylsphingosine (psychosine). Psychosine accumulation in oligodendrocytes and
  Schwann cells triggers apoptosis of myelin-forming cells, secondary lipid-laden multinucleated macrophages
  (globoid cells), and progressive CNS and peripheral demyelination. The infantile form (~85% of cases)
  presents in the first 6 months with irritability, hypertonia, opisthotonus, seizures, blindness, and
  death by age 2-3 in untreated patients. Pre-symptomatic hematopoietic stem cell transplantation (the
  only available disease-modifying therapy), the twitcher mouse model (Galc^trs/trs) faithfully recapitulating
  the human phenotype, and AAV-GALC gene therapy corroborate the GALC-deficiency / psychosine-toxicity
  / demyelination axis as the canonical pathogenic mechanism.
evidence:
- reference: PMID:31527255
  reference_title: 'Globoid cell leukodystrophy: Insights from CRISPR/Cas9 modeling.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Infantile globoid cell leukodystrophy (GLD, Krabbe disease) is a fatal
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

# Hypothesis Evaluation Report: Canonical GALC Deficiency / Psychosine-Mediated Demyelination Model for Krabbe Disease

**Hypothesis ID:** `canonical_galc_deficiency_psychosine_demyelination_model`  
**Disease:** Krabbe Disease (Globoid Cell Leukodystrophy)  
**Category:** Genetic  
**Status in KB:** CANONICAL  
**Evaluation Date:** 2026-05-24  
**Papers Reviewed:** 90  
**Confirmed Findings:** 20  

---

## Executive Judgment

**Verdict: SUPPORTED with significant qualifications — expansion to a multi-mechanism framework is required.**

The canonical model positing that GALC deficiency leads to psychosine accumulation, which in turn kills myelinating cells and causes progressive demyelination, is quantitatively validated by the strongest available evidence. Across 31 GALC missense variants expressed in human oligodendrocytic cells, residual GALC enzyme activity correlates with age of disease onset with a Pearson's r > 0.94 (p < 0.0001), and an inverse correlation exists between residual GALC activity and endogenous psychosine levels ([PMID: 40449593](https://pubmed.ncbi.nlm.nih.gov/40449593/)). Genetic ablation of acid ceramidase (ACDase) in twitcher mice eliminates psychosine and reportedly cures GLD ([PMID: 31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/)). Gene therapy restoring GALC corrects metabolic deficiencies and extends survival in mouse and canine models ([PMID: 29433937](https://pubmed.ncbi.nlm.nih.gov/29433937/); [PMID: 35333110](https://pubmed.ncbi.nlm.nih.gov/35333110/)). Psychosine is clinically validated as a disease-specific biomarker for newborn screening ([PMID: 32089546](https://pubmed.ncbi.nlm.nih.gov/32089546/)).

However, a critical unresolved discrepancy undermines the sufficiency of psychosine as the sole pathogenic mediator. Saposin-D genetic ablation in twitcher mice eliminates psychosine accumulation yet fails to prevent late-stage demyelination — with lifespans even shorter than standard twitcher mice ([PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/)). Similarly, a UGT8 inhibitor reduces psychosine by 72–86% without extending lifespan ([PMID: 35290889](https://pubmed.ncbi.nlm.nih.gov/35290889/)). These results demonstrate that psychosine is necessary but not sufficient, and that GALC has critical functions beyond psychosine degradation. The canonical model must be expanded to incorporate galactosylceramide-driven macrophage pathology, neuroinflammation (including adaptive immunity), cell-autonomous neuronal dysfunction, autophagy dysregulation, UPR/ER stress, and emerging mechanisms such as α-synuclein aggregation and sphingolipid fibril formation.

---

## Summary

Krabbe disease (globoid cell leukodystrophy, GLD) is an autosomal recessive lysosomal storage disorder caused by loss-of-function variants in *GALC*, encoding galactocerebrosidase. The canonical pathogenic model — that GALC deficiency prevents clearance of the toxic lysosphingolipid psychosine (galactosylsphingosine), which accumulates in and kills oligodendrocytes and Schwann cells, causing progressive demyelination — has been the dominant framework since Miyatake and Suzuki's "psychosine hypothesis" in 1972.

This evaluation synthesized evidence from 90 publications spanning human clinical data, model organism studies (twitcher mouse, canine, rhesus macaque, zebrafish), iPSC-derived neural models, and in vitro biochemical studies. The core GALC → psychosine → demyelination axis is robustly supported by genetic, pharmacological, and biomarker evidence. However, three independent experimental approaches that eliminate or substantially reduce psychosine yield contradictory outcomes: ACDase knockout cures GLD, Saposin-D knockout does not prevent late-stage disease, and UGT8 inhibition fails to extend lifespan. This "psychosine paradox" is the single most important unresolved question in Krabbe disease biology and necessitates expanding the canonical model to a multi-mechanism framework where psychosine toxicity operates alongside galactosylceramide-driven macrophage pathology, neuroinflammation, neuronal dysfunction, and proteostatic stress.

Two active Phase 1/2 gene therapy clinical trials (FBX-101/AAVrh10, NCT04693598 and NCT05739643) and a global patient registry (NCT02993796) are underway, reflecting the field's continued commitment to GALC restoration as the primary therapeutic strategy while acknowledging the need for combinatorial approaches targeting multiple pathogenic mechanisms.

---

## Key Findings

### Finding 1: The "Psychosine Paradox" — Contradictory Outcomes from Psychosine Elimination

The most consequential finding of this evaluation is a critical discrepancy among three independent approaches to eliminate or reduce psychosine in the twitcher mouse model:

**ACDase knockout** in twitcher mice eliminates psychosine accumulation by blocking the catabolic generation of psychosine from galactosylceramide, reportedly curing GLD. Li et al. (2019) demonstrated that "genetic loss of ACDase activity (Farber disease) in the GALC-deficient mouse model of human GLD (twitcher) eliminates psychosine accumulation and cures GLD" and established that psychosine is generated catabolically through deacylation of galactosylceramide by acid ceramidase, not via an anabolic pathway ([PMID: 31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/)).

**Saposin-D knockout** in twitcher mice also results in near-zero psychosine in both CNS and PNS. Watanabe et al. (2023) reported that "very little psychosine accumulated in the CNS or PNS of the mouse. As expected, demyelination with the infiltration of multinucleated macrophages (globoid cells) characteristic of Krabbe disease was milder in Twi/Sap-D KO mice than in Twi mice both in the CNS and PNS during the early disease stage. However, at the later disease stage, qualitatively and quantitatively comparable demyelination occurred in Twi/Sap-D KO mice, particularly in the PNS, and the lifespans of Twi/Sap-D KO mice were even shorter than that of Twi mice" ([PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/)).

**UGT8 inhibitor (RA 5557)** reduced pathologically elevated psychosine 72–86% in midbrain and cerebral cortex. Zaccariotto et al. (2022) reported that despite this reduction, "given the unchanged lifespan, it appears that GALC has critical functions in the nervous system beyond its traditional role in the degradation of galactosylceramide and psychosine" ([PMID: 35290889](https://pubmed.ncbi.nlm.nih.gov/35290889/)).

In contrast, CGT inhibitor S202 reduced both GalCer and psychosine dose-dependently and "significantly increased lifespan" in twitcher mice ([PMID: 34262084](https://pubmed.ncbi.nlm.nih.gov/34262084/)), suggesting that targeting both substrates simultaneously is more effective.

| Approach | Psychosine Reduced? | GLD Cured? | Lifespan | Reference |
|----------|-------------------|-----------|----------|-----------|
| ACDase KO (Farber × twitcher) | Eliminated | **Yes** | Extended | [PMID: 31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/) |
| Sap-D KO (× twitcher) | Eliminated | **No** | **Shorter** | [PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/) |
| UGT8 inhibitor RA 5557 | 72–86% reduction | **No** | Unchanged | [PMID: 35290889](https://pubmed.ncbi.nlm.nih.gov/35290889/) |
| CGT inhibitor S202 | Dose-dependent | **Partial** | Extended | [PMID: 34262084](https://pubmed.ncbi.nlm.nih.gov/34262084/) |

The reconciliation of these discordant results is the field's central unsolved problem. The ACDase KO may cure GLD not solely by eliminating psychosine but by simultaneously preventing acid ceramidase-mediated generation of other toxic lipid intermediates or by ceramide pathway modulation.

### Finding 2: Quantitative Genotype-Phenotype Validation of the GALC-Psychosine Axis

Peng et al. (2025) expressed a panel of 31 GALC missense variants in a GALC-KO human oligodendrocytic cell line and found that 26 of 31 clinically relevant variants reduced enzyme activity by 92–100%. "Residual GALC activity strongly correlated with the age of disease-onset in reported cases (Pearson's r > 0.94, p < 0.0001), suggesting that enzyme activity resulting from MMV expression in this model may serve as a readout for clinical prognostication." Additionally, "an inverse correlation between residual GALC activity and endogenous psychosine levels in the MMV panel" was observed ([PMID: 40449593](https://pubmed.ncbi.nlm.nih.gov/40449593/)). This is the strongest quantitative evidence linking the canonical dose-response relationship between GALC activity and disease severity, and directly validates the canonical causal chain in a human cellular system.

### Finding 3: Dual-Mechanism Model — Psychosine Plus GalCer-Driven Macrophage Pathology

Weinstock et al. (2020) provided direct evidence that GLD involves multiple mechanisms. They demonstrated that "cross-correction does not occur efficiently in vivo and that Galc-deficient Schwann cells autonomously produce psychosine. Furthermore, macrophages require GALC to degrade myelin, as Galc-deficient macrophages are transformed into globoid cells by exposure to galactosylceramide and produce a more severe GLD phenotype. Finally, hematopoietic stem cell transplantation in patients reduces globoid cells in nerves, suggesting that the phagocytic response of healthy macrophages, rather than cross-correction, contributes to the therapeutic effect. Thus, GLD may be caused by at least two mechanisms: psychosine-induced demyelination and secondary neuroinflammation from galactosylceramide storage in macrophages" ([PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/)). This finding reframes HSCT efficacy as macrophage replacement therapy rather than enzyme cross-correction.

### Finding 4: Neuroinflammation Precedes Demyelination and Involves Adaptive Immunity

Multiple studies indicate that immune activation is not merely a secondary response to demyelination. Potter & Petryniak (2016) showed that "inflammation in Krabbe's disease has been considered a secondary effect... However, recent studies have shown immune activation preceding clinical symptoms and white matter pathology" ([PMID: 27638616](https://pubmed.ncbi.nlm.nih.gov/27638616/)). CD4 and CD8 T cells infiltrate the twitcher CNS starting around postnatal day 30, with MCP-1 mRNA correlating with infiltration timing ([PMID: 10901235](https://pubmed.ncbi.nlm.nih.gov/10901235/)). Anti-inflammatory drugs (indomethacin, ibuprofen, minocycline) "significantly extended the life-span of the treated mice and reduced the levels of several of the immuno-related factors" ([PMID: 19748497](https://pubmed.ncbi.nlm.nih.gov/19748497/)). Recent reviews highlight "a previously understudied role for the adaptive immune system as a contributing factor to GLD pathophysiology" ([PMID: 40058166](https://pubmed.ncbi.nlm.nih.gov/40058166/)). KD patient peripheral blood mononuclear cells show a basal proinflammatory pattern with elevated TNF-alpha ([PMID: 17458901](https://pubmed.ncbi.nlm.nih.gov/17458901/)).

### Finding 5: Cell-Autonomous Neuronal Pathology Independent of Demyelination

Krabbe disease is not solely a white matter disorder. Patient-derived iNeurons showed "not only diminished GALC activity and increased psychosine levels, as expected, but also neurite fragmentation and abnormal neuritic branching" ([PMID: 27780934](https://pubmed.ncbi.nlm.nih.gov/27780934/)). Psychosine alone was sufficient to induce these defects in healthy neurons. Twitcher mouse hippocampal neurons demonstrated that "psychosine, the pathological sphingolipid in KD, accumulated preferentially in presynaptic membranes and synaptic vesicles. Moreover, its higher biosynthetic rate in synaptosome fractions suggests local synthesis within the synaptic compartment" ([PMID: 41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/)). These neuronal defects are cell-autonomous and include impaired paired-pulse facilitation, decreased EPSP amplitude, reduced dendritic spine density, and SNARE protein deregulation.

### Finding 6: Psychosine Disrupts Membrane Architecture

Psychosine accumulates specifically in lipid rafts in twitcher mouse and human Krabbe brain, "accompanied by an increase in cholesterol in these domains and changes in the distribution of the LR markers flotillin-2 and caveolin-1" ([PMID: 19439584](https://pubmed.ncbi.nlm.nih.gov/19439584/)). At the biophysical level, psychosine "is sufficient to disrupt sphingomyelin-enriched domains, increases the rigidity of localized areas in the plasma membrane, and promotes the shedding of membranous microvesicles" ([PMID: 28531236](https://pubmed.ncbi.nlm.nih.gov/28531236/)). Regional psychosine accumulation patterns match clinical dysfunction: "the presence of the psychosine was increased in specific anatomical regions of the brain responsible for the bodily functions that are impaired by GLD (cerebellum and brain stem)" ([PMID: 41578040](https://pubmed.ncbi.nlm.nih.gov/41578040/)).

### Finding 7: Prion-Like α-Synuclein Pathology

Post-mortem study of 4 Krabbe infant brains "identified widespread accumulations of α-synuclein" with "aggregation into fibrils similar to those observed in Lewy body disease, confirming the prion-like capacity of Krabbe disease-derived α-synuclein" ([PMID: 34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/)). The molecular mechanism involves psychosine binding: "psychosine forms hydrophilic clusters and binds the C-terminus of α-synuclein through its amino group and sugar moiety, suggesting that psychosine promotes an open/aggregation-prone conformation" ([PMID: 30127535](https://pubmed.ncbi.nlm.nih.gov/30127535/)). Genetic correction of GALC completely prevents α-synuclein aggregation, while α-synuclein knockout reduces but does not prevent neurological signs in twitcher mice.

### Finding 8: Sphingolipid Fibril Formation — A Novel Cytotoxic Mechanism

Kumar et al. (2025) demonstrated that "both GalCer and GalSph can self-assemble in vitro into highly organized fibrils reminiscent of fibrils of amyloidogenic proteins. These fibrils exhibit significant cytotoxicity to both neuronal and oligodendroglial cells" ([PMID: 40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/)). Fibril formation was detected in GALC-inhibited cells mimicking GLD. Small molecule amyloid inhibitors mitigated fibril formation in vitro, suggesting a novel therapeutic avenue.

### Finding 9: Autophagy Dysregulation — Partially Psychosine-Independent

"Large p62 cytoplasmic aggregates are present in the brain of both early and late symptomatic TWI mice. p62 expression is also upregulated in TWI sciatic nerves... In vitro data suggest that this effect might not be fully PSY-driven" ([PMID: 31108173](https://pubmed.ncbi.nlm.nih.gov/31108173/)). Chronic rapamycin treatment "significantly enhances motor functions at specific treatment time points and reduces astrogliosis in TWI brain, spinal cord, and sciatic nerves" ([PMID: 38422660](https://pubmed.ncbi.nlm.nih.gov/38422660/)), providing GALC-independent therapeutic benefit through autophagy induction.

### Finding 10: iPSC Organoids Reveal Early Myelination Defects Without Lysosomal Dysfunction

Krabbe disease organoids showed shorter but similar number of myelin internodes. Critically, "myelin is affected in the absence of autophagy and mTOR pathway dysregulation, suggesting lack of lysosomal dysfunction which makes this organoid model a very valuable tool to study the early events that drive demyelination in Kd" ([PMID: 39636943](https://pubmed.ncbi.nlm.nih.gov/39636943/)). Moreover, "the partial rescue of the neural differentiation program upon GALC reconstitution and psychosine clearance suggests multiple mechanisms contributing to neural pathology in GLD. Also, the pathological phenotype associated to supraphysiological GALC levels highlights the need of regulated GALC expression for proper human neural commitment/differentiation" ([PMID: 33989519](https://pubmed.ncbi.nlm.nih.gov/33989519/)).

### Finding 11: Gene Therapy Validates GALC Restoration Strategy

Marshall et al. (2018) demonstrated that "these results demonstrate that achieving nearly complete correction of GALC's metabolic deficiencies across the entire nervous system via gene therapy can have a significant improvement to behavioral deficits, pathophysiological changes, and survival" ([PMID: 29433937](https://pubmed.ncbi.nlm.nih.gov/29433937/)). Hordeaux et al. (2022) showed remarkable efficacy of AAVhu68-GALC in both twitcher mice and canine models ([PMID: 35333110](https://pubmed.ncbi.nlm.nih.gov/35333110/)). Two active Phase 1/2 trials (NCT04693598, NCT05739643) are testing FBX-101 (AAVrh10-GALC) in humans.

### Finding 12: GALC Heterozygosity as a Neurodegenerative Risk Factor

Feo et al. (2025) screened 110 adults with neurodegenerative symptoms and found "GALC heterozygosity in this group to be notably enriched, approximately 1 in 28, compared to 1 in 150 in the general population" ([PMID: 40391866](https://pubmed.ncbi.nlm.nih.gov/40391866/)). All 11 selected patients showed symptoms similar to atypical Parkinson's disease. This extends the relevance of the GALC-sphingolipid axis beyond classical Krabbe disease.

---

## Mechanistic Causal Chain

{{figure:mechanistic_framework.png|caption=Comprehensive mechanistic framework diagram showing the canonical GALC-psychosine-demyelination axis alongside parallel pathogenic mechanisms identified through this investigation. Evidence strength annotations are included for each causal link.}}

### Core Chain (Strong Evidence)

```
GALC Gene Variants (biallelic, >260 pathogenic variants identified)
    │ [STRONG: human genetics, enzyme assays, >40 years of evidence]
    ▼
GALC Enzyme Deficiency (complete in infantile; partial in late-onset)
    │ [STRONG: r > 0.94 activity-onset correlation, PMID:40449593]
    ├───────────────────────────────────────────┐
    │                                           │
    ▼                                           ▼
Psychosine Accumulation                    GalCer Accumulation
(catabolically via ACDase)                 (in macrophages/microglia)
    │ [STRONG: PMID:31527255]                  │ [STRONG: PMID:32375064]
    │                                           │
    ├► Lipid raft disruption                   ├► Globoid cell formation
    ├► Membrane microvesiculation               ├► MMP-3 induction
    ├► Caspase-mediated OL apoptosis           ├► Failed myelin clearance
    ├► Neuronal synaptic dysfunction            ├► Secondary neuroinflammation
    ├► α-Synuclein aggregation                  │
    ├► Sphingolipid fibril formation            │
    │                                           │
    ▼                                           ▼
    ╔═══════════════════════════════════════════╗
    ║  CONVERGING PATHOLOGY                     ║
    ║  • Oligodendrocyte/Schwann cell death     ║
    ║  • Progressive CNS + PNS demyelination    ║
    ║  • Neuroinflammation (innate + adaptive)  ║
    ║  • Neurodegeneration                      ║
    ╚═══════════════════════════════════════════╝
                        │
                        ▼
             CLINICAL PHENOTYPE
    Infantile: irritability, hypertonia, seizures,
    blindness, death by age 2-3
    Late-onset: peripheral neuropathy, ataxia,
    cognitive decline
```

### Parallel/Contributing Mechanisms

| Mechanism | Evidence Level | Key References | Relationship to Core Model |
|-----------|---------------|----------------|--------------------------|
| GalCer macrophage pathology | **Strong** | [PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/) | Parallel, co-equal arm |
| Neuroinflammation (innate + adaptive) | **Moderate** | [PMID: 27638616](https://pubmed.ncbi.nlm.nih.gov/27638616/), [PMID: 19748497](https://pubmed.ncbi.nlm.nih.gov/19748497/) | Amplifying, may precede demyelination |
| Cell-autonomous neuronal dysfunction | **Moderate** | [PMID: 41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/), [PMID: 27780934](https://pubmed.ncbi.nlm.nih.gov/27780934/) | Parallel, extends beyond white matter |
| α-Synuclein aggregation | **Moderate** | [PMID: 34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/), [PMID: 30127535](https://pubmed.ncbi.nlm.nih.gov/30127535/) | Downstream of psychosine |
| Autophagy dysregulation | **Moderate** | [PMID: 31108173](https://pubmed.ncbi.nlm.nih.gov/31108173/), [PMID: 38422660](https://pubmed.ncbi.nlm.nih.gov/38422660/) | Partially independent of psychosine |
| UPR/ER stress | **Moderate** | [PMID: 29615819](https://pubmed.ncbi.nlm.nih.gov/29615819/) | Mutation-dependent, parallel |
| Sphingolipid fibril formation | **Emerging** | [PMID: 40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/) | Novel supramolecular toxicity |
| LacCer accumulation | **Emerging** | [PMID: 40305757](https://pubmed.ncbi.nlm.nih.gov/40305757/) | Alternative substrate (zebrafish) |
| Peroxisomal dysfunction | **Weak** | [PMID: 16530726](https://pubmed.ncbi.nlm.nih.gov/16530726/) | Downstream of psychosine |

---

## Evidence Matrix

{{figure:final_evidence_summary.png|caption=Final evidence summary visualization showing the classification breakdown of evidence types, investigation metrics, and the balance between supporting, qualifying, and competing evidence across all 20 confirmed findings.}}

| # | Citation | Evidence Type | Verdict | Claim Tested | Key Finding | Context | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | [PMID: 40449593](https://pubmed.ncbi.nlm.nih.gov/40449593/) | In vitro (human OL) | **Supports** | GALC activity → disease severity | r > 0.94 correlation across 31 variants; inverse PSY correlation | All subtypes | High |
| 2 | [PMID: 31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/) | Model organism (mouse) | **Supports** | Psychosine hypothesis | ACDase KO eliminates PSY, cures GLD | Twitcher | High (but see #3) |
| 3 | [PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/) | Model organism (mouse) | **Qualifies** | Psychosine is sole mediator | Sap-D KO eliminates PSY but disease persists | Twitcher | High |
| 4 | [PMID: 35290889](https://pubmed.ncbi.nlm.nih.gov/35290889/) | Model organism (mouse) | **Qualifies** | PSY reduction extends lifespan | 72–86% PSY reduction, no lifespan change | Twitcher | High |
| 5 | [PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/) | Model + human | **Qualifies** | PSY-only pathogenesis | Dual mechanism: PSY + GalCer macrophage pathology | PNS focus | High |
| 6 | [PMID: 34262084](https://pubmed.ncbi.nlm.nih.gov/34262084/) | Model organism (mouse) | **Supports** | Substrate reduction | CGT inhibitor reduces GalCer + PSY, extends lifespan | Twitcher | Moderate |
| 7 | [PMID: 29433937](https://pubmed.ncbi.nlm.nih.gov/29433937/) | Model organism (mouse) | **Supports** | GALC restoration cures disease | AAV9-GALC corrects metabolic deficits | Twitcher | High |
| 8 | [PMID: 35333110](https://pubmed.ncbi.nlm.nih.gov/35333110/) | Multi-species | **Supports** | Gene therapy efficacy | AAVhu68-GALC via CSF effective in mice + dogs | Pre-clinical | High |
| 9 | [PMID: 19439584](https://pubmed.ncbi.nlm.nih.gov/19439584/) | Human + mouse | **Supports** | PSY disrupts membranes | PSY in lipid rafts in mouse + human Krabbe brain | CNS + PNS | High |
| 10 | [PMID: 28531236](https://pubmed.ncbi.nlm.nih.gov/28531236/) | In vitro | **Supports** | PSY demyelination mechanism | Membrane microvesiculation, SM disruption | In vitro | Moderate |
| 11 | [PMID: 27780934](https://pubmed.ncbi.nlm.nih.gov/27780934/) | Human iPSC | **Qualifies** | Disease is purely demyelinating | Neuron-autonomous PSY toxicity (neurite fragmentation) | Adult-onset | Moderate |
| 12 | [PMID: 41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/) | Model organism (mouse) | **Qualifies** | Disease is purely demyelinating | PSY in presynaptic vesicles, synaptic dysfunction | Twitcher hippocampus | Moderate |
| 13 | [PMID: 27638616](https://pubmed.ncbi.nlm.nih.gov/27638616/) | Review | **Qualifies** | Inflammation is secondary | Immune activation precedes demyelination | Twitcher + human | Moderate |
| 14 | [PMID: 19748497](https://pubmed.ncbi.nlm.nih.gov/19748497/) | Model organism (mouse) | **Supports** | Inflammation contributes | Anti-inflammatory drugs extend lifespan | Twitcher CNS | Moderate |
| 15 | [PMID: 34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/) | Human post-mortem | **Qualifies** | PSY is sole toxin | Prion-like α-synuclein in infant Krabbe brains | Infantile | Moderate |
| 16 | [PMID: 30127535](https://pubmed.ncbi.nlm.nih.gov/30127535/) | In vitro + mouse | **Qualifies** | PSY toxicity mechanism | PSY binds α-syn C-terminus, promotes aggregation | Twitcher | Moderate |
| 17 | [PMID: 40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/) | In vitro | **Competing** | PSY acts as soluble toxin | GalCer/PSY form cytotoxic amyloid-like fibrils | In vitro | Emerging |
| 18 | [PMID: 31108173](https://pubmed.ncbi.nlm.nih.gov/31108173/) | Model organism (mouse) | **Qualifies** | PSY explains all pathology | Autophagy dysfunction not fully PSY-driven | Twitcher brain | Moderate |
| 19 | [PMID: 38422660](https://pubmed.ncbi.nlm.nih.gov/38422660/) | Model organism (mouse) | **Qualifies** | Only GALC therapy works | Rapamycin improves motor function, reduces astrogliosis | Twitcher | Moderate |
| 20 | [PMID: 39636943](https://pubmed.ncbi.nlm.nih.gov/39636943/) | Human iPSC organoid | **Qualifies** | Lysosomal dysfunction drives early disease | Myelination defects without autophagy/mTOR dysregulation | Early stage | Moderate |
| 21 | [PMID: 33989519](https://pubmed.ncbi.nlm.nih.gov/33989519/) | Human iPSC | **Qualifies** | GALC restoration fully rescues | Partial rescue; supraphysiological GALC is harmful | iPSC neural | High |
| 22 | [PMID: 32089546](https://pubmed.ncbi.nlm.nih.gov/32089546/) | Human clinical | **Supports** | PSY as biomarker | DBS PSY differentiates subtypes, monitors treatment | NBS context | High |
| 23 | [PMID: 34071213](https://pubmed.ncbi.nlm.nih.gov/34071213/) | Human clinical | **Qualifies** | PSY predicts all KD | Low PSY at NBS in patient who developed late-infantile KD | Late-infantile | Moderate |
| 24 | [PMID: 41578040](https://pubmed.ncbi.nlm.nih.gov/41578040/) | Model organism (MSI) | **Supports** | PSY regional distribution | PSY elevated in cerebellum/brainstem matching clinical dysfunction | Twitcher | Moderate |
| 25 | [PMID: 40391866](https://pubmed.ncbi.nlm.nih.gov/40391866/) | Human clinical | **Qualifies** | KD is biallelic only | GALC heterozygosity enriched ~1:28 in neurodegeneration patients | Adult carriers | Moderate |
| 26 | [PMID: 29615819](https://pubmed.ncbi.nlm.nih.gov/29615819/) | In vitro | **Qualifies** | Single mechanism for all variants | UPR activation is mutation-dependent, multiple pathways | All subtypes | Moderate |
| 27 | [PMID: 17458901](https://pubmed.ncbi.nlm.nih.gov/17458901/) | Human ex vivo | **Supports** | PSY activates inflammation | KD patient PBMCs basal proinflammatory pattern | Peripheral | Moderate |
| 28 | [PMID: 10901235](https://pubmed.ncbi.nlm.nih.gov/10901235/) | Model organism (mouse) | **Supports** | Adaptive immunity involved | CD4/CD8 T cells infiltrate twitcher CNS | Twitcher | Moderate |

---

## Evidence Base — Key Literature Synthesis

### Papers Providing Strongest Support

The **Peng et al. 2025** ([PMID: 40449593](https://pubmed.ncbi.nlm.nih.gov/40449593/)) systematic variant study is the gold standard for the canonical dose-response model, showing r > 0.94 correlation between GALC activity and onset age across 31 variants. **Li et al. 2019** ([PMID: 31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/)) provides the strongest genetic proof-of-concept via ACDase KO curing GLD in mice. **Marshall et al. 2018** ([PMID: 29433937](https://pubmed.ncbi.nlm.nih.gov/29433937/)) and **Hordeaux et al. 2022** ([PMID: 35333110](https://pubmed.ncbi.nlm.nih.gov/35333110/)) demonstrate that global GALC restoration via gene therapy corrects disease across species. **Guenzel et al. 2020** ([PMID: 32089546](https://pubmed.ncbi.nlm.nih.gov/32089546/)) validates psychosine as a clinical biomarker.

### Papers Providing Strongest Challenges

**Watanabe et al. 2023** ([PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/)) is the single most challenging paper, showing psychosine elimination does not prevent late-stage disease. **Zaccariotto et al. 2022** ([PMID: 35290889](https://pubmed.ncbi.nlm.nih.gov/35290889/)) corroborates this with pharmacological evidence. **Weinstock et al. 2020** ([PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/)) directly demonstrates dual pathogenic mechanisms.

### Papers Extending the Model

**Zelada et al. 2025** ([PMID: 41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/)) and **Lim et al. 2016** ([PMID: 27780934](https://pubmed.ncbi.nlm.nih.gov/27780934/)) extend pathology to neurons. **Hatton et al. 2022** ([PMID: 34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/)) links Krabbe to proteinopathy. **Kumar et al. 2025** ([PMID: 40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/)) identifies a novel fibrillar cytotoxic species. **Feo et al. 2025** ([PMID: 40391866](https://pubmed.ncbi.nlm.nih.gov/40391866/)) extends relevance to heterozygous carriers with neurodegenerative disease.

---

## Limitations and Knowledge Gaps

### Gap 1: The "Psychosine Paradox" (Critical Priority)

**Scope:** Three approaches to eliminate psychosine in twitcher mice yield contradictory outcomes — ACDase KO cures, Sap-D KO does not, UGT8 inhibitor does not.
**Why it matters:** This directly determines whether psychosine-targeting therapies are sufficient and has profound implications for drug development.
**What was checked:** All three primary studies and their methods (PMID: 31527255, 37337846, 35290889). No head-to-head comparison or reconciliation study exists.
**Resolution needed:** Side-by-side comprehensive lipidomic profiling of ACDase KO/Twi vs. Sap-D KO/Twi brains; conditional inducible psychosine-specific tools that do not perturb other sphingolipid pathways.

### Gap 2: Relative Contribution of Parallel Mechanisms (High Priority)

**Scope:** Neuroinflammation, autophagy, UPR, α-synuclein, and neuronal dysfunction are documented but their quantitative contributions to disease progression at each stage are unknown.
**Why it matters:** Combinatorial therapy design requires understanding which mechanisms matter most at which stages.
**What was checked:** Individual mechanism studies; no integrated multi-mechanism quantitative analysis exists.
**Resolution needed:** Multi-omic temporal profiling of twitcher mice at multiple disease stages; computational modeling of mechanism interactions.

### Gap 3: Human Neuronal Pathology Data (High Priority)

**Scope:** Neuronal involvement documented in iPSC and mouse models but human neuropathological data are sparse.
**Why it matters:** Cell-autonomous neuronal defects may explain why HSCT does not fully prevent progression.
**Resolution needed:** Systematic neuropathological analysis of neurons in post-mortem Krabbe brains; single-nucleus RNA-seq of human KD tissue.

### Gap 4: Late-Onset KD Mechanisms (Moderate Priority)

**Scope:** Most research focuses on infantile KD; late-onset mechanisms are poorly understood. Low-psychosine cases exist ([PMID: 34071213](https://pubmed.ncbi.nlm.nih.gov/34071213/)).
**Why it matters:** Late-onset patients may benefit from different therapeutic approaches targeting different pathogenic arms.
**Resolution needed:** Natural history studies with longitudinal biomarkers; characterization of CRISPR knock-in models (PMID: 35620447).

### Gap 5: GALC Dosage Effects and Gene Therapy Safety (Moderate Priority)

**Scope:** Supraphysiological GALC expression causes pathology in iPSC models ([PMID: 33989519](https://pubmed.ncbi.nlm.nih.gov/33989519/)).
**Why it matters:** Two active gene therapy trials must determine safe expression levels.
**Resolution needed:** Dose-escalation studies; regulatable AAV-GALC constructs.

### Gap 6: PNS-Specific Pathogenic Mechanisms (Moderate Priority)

**Scope:** PNS continues to deteriorate after HSCT; Sap-D KO showed severe PNS demyelination despite no psychosine.
**Why it matters:** Peripheral neuropathy is a major source of morbidity even in transplanted patients.
**Resolution needed:** PNS-specific lipidomics; Schwann cell-specific GALC rescue experiments.

### Gap 7: HSCT Mechanism of Action (Moderate Priority)

**Scope:** Evidence suggests macrophage replacement rather than cross-correction ([PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/)), but relative contributions are unquantified.
**Resolution needed:** Conditional GALC restoration (macrophage-specific vs. global) in animal models.

### Gap 8: Source-Level and Data Absences

- **ClinGen/GenCC:** No published formal gene-disease validity classification found for GALC-Krabbe (though well-established in OMIM).
- **Clinical trials:** No published human gene therapy results as of search date. Two active Phase 1/2 trials (NCT04693598, NCT05739643).
- **Omics data:** No large-scale single-cell or proteomic study of human Krabbe CNS tissue identified.
- **Longitudinal biomarkers:** Limited longitudinal psychosine + clinical outcome data beyond small series.

{{figure:knowledge_gaps.png|caption=Knowledge gap analysis showing scope, importance, and recommended resolution strategies for each identified gap in the Krabbe disease mechanistic model.}}

---

## Alternative Models

### 1. GalCer-Driven Macrophage Pathology Model
**Relationship:** Parallel / complementary mechanism  
**Evidence:** GalCer transforms Galc-deficient macrophages into globoid cells ([PMID: 32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/)). Demyelination persists without psychosine ([PMID: 37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/)). GalCer uniquely elicits macrophage infiltration ([PMID: 6152811](https://pubmed.ncbi.nlm.nih.gov/6152811/)).  
**Status:** Strongly supported; should be incorporated as a co-equal arm of the canonical model.

### 2. Neuroinflammation-Primary Model
**Relationship:** Competing for temporal primacy / amplifying  
**Evidence:** Immune activation precedes demyelination ([PMID: 27638616](https://pubmed.ncbi.nlm.nih.gov/27638616/)). T cell role emerging ([PMID: 40058166](https://pubmed.ncbi.nlm.nih.gov/40058166/)). Anti-inflammatory drugs extend lifespan ([PMID: 19748497](https://pubmed.ncbi.nlm.nih.gov/19748497/)).  
**Status:** Partially supported; likely amplifying rather than fully independent.

### 3. Neuron-Autonomous Toxicity Model
**Relationship:** Parallel mechanism  
**Evidence:** iPSC neurons ([PMID: 27780934](https://pubmed.ncbi.nlm.nih.gov/27780934/)), synaptic dysfunction ([PMID: 41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/)), α-synuclein ([PMID: 34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/)).  
**Status:** Supported by multiple studies; clinical significance unclear.

### 4. Autophagy/Lysosomal Stress Model
**Relationship:** Parallel mechanism  
**Evidence:** p62 aggregation not fully psychosine-driven ([PMID: 31108173](https://pubmed.ncbi.nlm.nih.gov/31108173/)). Rapamycin provides benefit ([PMID: 38422660](https://pubmed.ncbi.nlm.nih.gov/38422660/)).  
**Status:** Emerging; needs independent replication.

### 5. Sphingolipid Fibril / Lipid Amyloid Model
**Relationship:** Mechanistic extension  
**Evidence:** GalCer/psychosine self-assemble into cytotoxic fibrils ([PMID: 40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/)).  
**Status:** Speculative; in vitro only.

### 6. UPR/ER Stress Model
**Relationship:** Parallel (mutation-dependent)  
**Evidence:** Mutation-specific UPR activation ([PMID: 29615819](https://pubmed.ncbi.nlm.nih.gov/29615819/)).  
**Status:** Emerging; relevant only for misfolding mutations.

### 7. Lactosylceramide Model
**Relationship:** Alternative toxic metabolite  
**Evidence:** Dramatic LacCer accumulation in zebrafish KD with modest psychosine elevation ([PMID: 40305757](https://pubmed.ncbi.nlm.nih.gov/40305757/)).  
**Status:** Emerging; may be species-specific.

### 8. GALC Heterozygosity as Neurodegenerative Risk Factor
**Relationship:** Extension beyond classical Krabbe  
**Evidence:** ~1/28 carrier frequency in neurodegeneration patients vs. ~1/150 general population ([PMID: 40391866](https://pubmed.ncbi.nlm.nih.gov/40391866/)).  
**Status:** Emerging; requires replication.

---

## Discriminating Tests

### Test 1: Resolve the Psychosine Paradox (Highest Priority)
- **Design:** Generate ACDase KO/Twi and Sap-D KO/Twi mice on identical C57BL/6 background. Comprehensive lipidomic profiling of brain, spinal cord, and sciatic nerve at postnatal days 15, 25, and 35.
- **Assay:** Mass spectrometry for all sphingolipid species (psychosine, GalCer, ceramides, sphingosine, S1P, LacCer, sulfatides).
- **Expected result:** If ACDase KO cures by eliminating non-psychosine lipids, profiles will differ from Sap-D KO despite similar psychosine levels.
- **Discriminates:** Psychosine-only vs. multi-lipid toxicity model.

### Test 2: T Cell Depletion in Twitcher Mice
- **Design:** Anti-CD4/CD8 antibody treatment or Rag1-KO cross with twitcher mice.
- **Biomarkers:** Demyelination score, lifespan, psychosine levels, globoid cell counts.
- **Expected result:** If adaptive immunity is a major driver, T-cell depletion should extend lifespan.
- **Discriminates:** Inflammation-primary vs. inflammation-secondary model.

### Test 3: Cell-Type-Specific GALC Restoration
- **Design:** Conditional GALC expression in (a) oligodendrocytes only, (b) macrophages only, (c) neurons only in twitcher mice using cell-type-specific Cre drivers.
- **Expected result:** Reveals relative therapeutic contribution of each cell type.
- **Discriminates:** Single vs. dual/multi-mechanism; identifies therapeutic targets.

### Test 4: Human Single-Cell Transcriptomics
- **Design:** Single-nucleus RNA-seq of post-mortem Krabbe brain (infantile + late-onset).
- **Expected result:** Cell-type-specific transcriptomic signatures of pathology.
- **Discriminates:** Relative contribution of each mechanism in human disease.

### Test 5: Longitudinal Multi-Biomarker Monitoring in Clinical Trials
- **Design:** Measure psychosine, GalCer, LacCer, NfL, cytokines in CSF/DBS longitudinally in FBX-101 gene therapy trial patients.
- **Expected result:** Defines temporal ordering and treatment response of each pathogenic axis.
- **Discriminates:** Psychosine-only vs. multi-substrate toxicity in humans.

### Test 6: Anti-Amyloid Compounds in Twitcher Mice
- **Design:** Small molecule amyloid inhibitors (identified in PMID: 40603002) administered to twitcher mice.
- **Expected result:** If sphingolipid fibrils contribute to pathology in vivo, inhibitors should provide benefit.
- **Discriminates:** Fibril toxicity model vs. soluble toxin model.

---

## Curation Leads

*All candidate updates below require curator verification.*

### Candidate Evidence References

| Priority | PMID | Author/Year | Verdict | Verified Snippet |
|----------|------|-------------|---------|------------------|
| HIGH | [31527255](https://pubmed.ncbi.nlm.nih.gov/31527255/) | Li 2019 | Supports | "genetic loss of ACDase activity...eliminates psychosine accumulation and cures GLD" |
| HIGH | [37337846](https://pubmed.ncbi.nlm.nih.gov/37337846/) | Watanabe 2023 | Qualifies | "at the later disease stage, qualitatively and quantitatively comparable demyelination occurred" |
| HIGH | [32375064](https://pubmed.ncbi.nlm.nih.gov/32375064/) | Weinstock 2020 | Qualifies | "GLD may be caused by at least two mechanisms" |
| HIGH | [40449593](https://pubmed.ncbi.nlm.nih.gov/40449593/) | Peng 2025 | Supports | "residual GALC activity strongly correlated with the age of disease-onset (r > 0.94, p < 0.0001)" |
| MEDIUM | [34999780](https://pubmed.ncbi.nlm.nih.gov/34999780/) | Hatton 2022 | Extends | "confirming the prion-like capacity of Krabbe disease-derived α-synuclein" |
| MEDIUM | [41430252](https://pubmed.ncbi.nlm.nih.gov/41430252/) | Zelada 2025 | Extends | "psychosine accumulated preferentially in presynaptic membranes and synaptic vesicles" |
| MEDIUM | [40603002](https://pubmed.ncbi.nlm.nih.gov/40603002/) | Kumar 2025 | Competing | "both GalCer and GalSph can self-assemble into highly organized fibrils" |
| MEDIUM | [40391866](https://pubmed.ncbi.nlm.nih.gov/40391866/) | Feo 2025 | Extends | "GALC heterozygosity...approximately 1 in 28, compared to 1 in 150" |

### Candidate Pathophysiology Nodes/Edges

- **New node:** Galactosylceramide-mediated macrophage pathology (parallel to psychosine)
- **New node:** Neuronal synaptic dysfunction (cell-autonomous, psychosine-mediated)
- **New node:** α-Synuclein aggregation (downstream of psychosine)
- **New node:** Sphingolipid fibril formation (novel cytotoxic species)
- **New edge:** GalCer → ACDase → psychosine (catabolic pathway confirmed)
- **New edge:** GALC deficiency → GalCer accumulation in macrophages → globoid cells
- **New edge:** Psychosine → α-synuclein aggregation → neurodegeneration
- **Qualify edge:** "Psychosine → demyelination" should note "necessary for early-stage but not sufficient for late-stage"
- **Strengthen edge:** GALC activity → onset age (r > 0.94 across 31 variants)

### Candidate Ontology Terms

- **Cell types:** CL:0000128 (oligodendrocyte), CL:0002573 (Schwann cell), CL:0000235 (macrophage), CL:0000129 (microglia), CL:0000540 (neuron)
- **Biological processes:** GO:0042552 (myelination), GO:0006915 (apoptotic process), GO:0031579 (lipid raft organization), GO:0099504 (synaptic vesicle cycle), GO:0006914 (autophagy), GO:0006954 (inflammatory response)

### Candidate Status Change

- **Current:** CANONICAL
- **Recommended:** CANONICAL with mandatory qualifications
- **Qualifier text:** "Multi-mechanism expansion required — psychosine toxicity is a major but not sole driver. Parallel GalCer macrophage pathology, neuroinflammation, and neuronal dysfunction contribute independently. Critical discrepancy between ACDase KO and Sap-D KO outcomes remains unresolved."

### Candidate Knowledge Gaps for KB

1. ACDase KO vs. Sap-D KO discrepancy (no reconciliation study exists)
2. Relative psychosine vs. GalCer contributions by disease stage and tissue compartment
3. Causal role of adaptive immunity (T cells) — perturbation data missing
4. Clinical significance of neuronal pathology — in vivo rescue data missing
5. GALC dosage safety window for gene therapy
6. PNS-specific mechanisms post-HSCT
7. No published human gene therapy trial results
8. No human single-cell/proteomic data for Krabbe CNS tissue

---

*Report generated 2026-05-24. Based on systematic evaluation of 90 publications and 20 confirmed findings across 5 investigation iterations.*
