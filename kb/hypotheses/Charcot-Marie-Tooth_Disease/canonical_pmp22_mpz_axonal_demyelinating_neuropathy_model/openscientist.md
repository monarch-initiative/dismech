---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-25T14:03:32.066810'
end_time: '2026-05-25T14:47:10.689285'
duration_seconds: 2618.62
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease
  category: Mendelian
  hypothesis_group_id: canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model
  hypothesis_label: Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy
    Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model\n\
    hypothesis_label: Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy\
    \ Model\nstatus: CANONICAL\ndescription: Charcot-Marie-Tooth (CMT) disease is\
    \ a clinically and genetically heterogeneous group of\n  inherited peripheral\
    \ neuropathies caused by variants in >100 genes encoding myelin components (PMP22,\n\
    \  MPZ, GJB1), axonal cytoskeleton and transport proteins (MFN2, NEFL, KIF1B),\
    \ and other Schwann-cell-axon\n  interface factors. CMT1A (most common, PMP22\
    \ duplication on 17p11.2) produces demyelinating neuropathy\n  through PMP22 overexpression-driven\
    \ Schwann cell dysfunction and secondary axonal loss. Axonal CMT2\n  forms (MFN2,\
    \ MPZ, others) primarily impair axonal function. The uniform clinical phenotype\
    \ \u2014 distal\n  motor and sensory loss in a length-dependent pattern, with\
    \ foot deformity, distal weakness, and absent\n  reflexes \u2014 reflects convergent\
    \ length-dependent axonal degeneration regardless of upstream gene defect.\n \
    \ The PMP22 duplication CMT1A mouse and rat models recapitulate the human phenotype,\
    \ and PMP22-lowering\n  ASO and PXT3003 (low-dose drug combination) corroborate\
    \ the PMP22-dosage axis as a canonical mechanism\n  in the most common subtype.\n\
    evidence:\n- reference: DOI:10.1093/brain/awae064\n  reference_title: Whole genome\
    \ sequencing increases the diagnostic rate in Charcot-Marie-Tooth disease\n  supports:\
    \ SUPPORT\n  evidence_source: OTHER\n  snippet: The most common genetic diagnosis\
    \ was PMP22 duplication (CMT1A; 505/1165, 43.3%)\n  explanation: |\n    Existing\
    \ canonical mechanism citation in the dismech knowledge base, used as the seed\
    \ for the hypothesis-search deep-research run."
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
citation_count: 42
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model
- **Hypothesis Label:** Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model
hypothesis_label: Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy Model
status: CANONICAL
description: Charcot-Marie-Tooth (CMT) disease is a clinically and genetically heterogeneous group of
  inherited peripheral neuropathies caused by variants in >100 genes encoding myelin components (PMP22,
  MPZ, GJB1), axonal cytoskeleton and transport proteins (MFN2, NEFL, KIF1B), and other Schwann-cell-axon
  interface factors. CMT1A (most common, PMP22 duplication on 17p11.2) produces demyelinating neuropathy
  through PMP22 overexpression-driven Schwann cell dysfunction and secondary axonal loss. Axonal CMT2
  forms (MFN2, MPZ, others) primarily impair axonal function. The uniform clinical phenotype — distal
  motor and sensory loss in a length-dependent pattern, with foot deformity, distal weakness, and absent
  reflexes — reflects convergent length-dependent axonal degeneration regardless of upstream gene defect.
  The PMP22 duplication CMT1A mouse and rat models recapitulate the human phenotype, and PMP22-lowering
  ASO and PXT3003 (low-dose drug combination) corroborate the PMP22-dosage axis as a canonical mechanism
  in the most common subtype.
evidence:
- reference: DOI:10.1093/brain/awae064
  reference_title: Whole genome sequencing increases the diagnostic rate in Charcot-Marie-Tooth disease
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The most common genetic diagnosis was PMP22 duplication (CMT1A; 505/1165, 43.3%)
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

# Hypothesis Evaluation Report: Canonical PMP22 / MPZ / Axonal & Demyelinating Peripheral Neuropathy Model for Charcot-Marie-Tooth Disease

**Hypothesis ID:** `canonical_pmp22_mpz_axonal_demyelinating_neuropathy_model`
**Status in KB:** CANONICAL
**Report Date:** 2026-05-25
**Evidence Items Evaluated:** 36 primary findings across 128 papers reviewed over 5 investigation iterations

---

## Executive Judgment

**Verdict: SUPPORTED with seven major qualifications**

The Canonical PMP22/MPZ/Axonal & Demyelinating Peripheral Neuropathy Model for Charcot-Marie-Tooth disease is robustly supported by converging lines of evidence from human genetics, animal models, clinical trials, and emerging biomarker studies. Its core architecture -- PMP22 duplication as the most common cause (43-60% of diagnosed cases), genetic heterogeneity across >130 genes, and convergent length-dependent axonal degeneration as the final common pathway -- is firmly established by large cohort studies, transgenic models that recapitulate the human phenotype, and therapeutic proof-of-concept experiments targeting PMP22 dosage.

However, the hypothesis as currently stated requires seven substantive refinements to align with the literature as of 2026: (1) CMT1A is fundamentally a *dysmyelinating* disorder with uniformly shortened internodes, not a segmental *demyelinating* neuropathy; (2) PMP22 functions as a structural organizer of myelin architecture at nodes and incisures, not merely a compact myelin component; (3) UPR/ER stress represents a convergent pathomechanism across CMT1A and CMT1B subtypes; (4) SARM1 has been identified as the central executioner of axonal degeneration in CMT2A, mediating a feedback loop with mitochondrial dysfunction; (5) secondary neuroinflammation via macrophage-CSF1 signaling amplifies demyelination across CMT subtypes; (6) lipid metabolism dysregulation (sphingolipid and glycerophospholipid pathways) and cholesterol trafficking defects are mechanistically linked to PMP22 dosage; and (7) human proof-of-concept for PMP22-lowering therapies remains the critical unresolved translational gap, though ASO and AAV9-miRNA gene therapy approaches are advancing toward clinical translation.

The most important caveat is that while rodent models strongly validate the PMP22-dosage axis, every pharmacological intervention tested in human CMT1A trials to date (ascorbic acid across five trials, complement inhibition) has failed to demonstrate clinical efficacy except for PXT3003, which showed a modest but statistically significant effect in a single phase III trial complicated by formulation issues. This translational gap between compelling preclinical biology and human clinical outcomes is the defining challenge for the field.

---

## Summary

The canonical model for CMT disease posits that mutations in >100 genes -- principally PMP22 (duplication), MPZ, GJB1, MFN2, and NEFL -- converge on a final common pathway of length-dependent axonal degeneration, producing the characteristic clinical phenotype of distal motor and sensory loss, foot deformities, absent reflexes, and progressive disability. Our systematic evaluation across 128 papers confirms that the genetic architecture, phenotypic convergence, and animal model recapitulation described in this hypothesis are well-substantiated. PMP22 duplication accounts for 43-60% of genetically diagnosed CMT cases across multiple international cohorts, and the C3-PMP22 mouse model faithfully recapitulates human CMT1A neurophysiology with stable, low nerve conduction velocities.

The investigation uncovered several mechanistic layers not captured in the seed hypothesis. PMP22 is now understood to be a structural organizer of myelin architecture -- coordinating adherens junction patterning, nodal subdomain integrity, and cholesterol trafficking via its CRAC domain -- rather than simply a compact myelin component whose overexpression overwhelms Schwann cells. The discovery that SARM1 deletion rescues axonal, synaptic, and mitochondrial phenotypes in CMT2A rat models identifies a druggable node in the axonal degeneration cascade. Furthermore, the identification of UPR/ER stress as a shared mechanism across CMT1A and CMT1B, with therapeutic validation via IFB-088/Sephin1, provides a convergent therapeutic target for demyelinating subtypes.

The therapeutic landscape has evolved substantially. While ascorbic acid trials uniformly failed due to pharmacokinetic limitations, PMP22-targeting ASOs have demonstrated post-onset reversal of CMT1A features in rodent models, and AAV9-miRNA gene therapy has shown efficacy in humanized CMT1A mice with safety confirmed in non-human primates. PXT3003 (baclofen/naltrexone/D-sorbitol) showed a statistically significant improvement in the phase III ONLS primary endpoint, and a second phase III trial is ongoing. MRI calf muscle fat fraction has emerged as the most responsive biomarker, with 12-month changes predicting 4-year clinical outcomes (rho=0.65, p=0.01), while plasma NfL and GFAP provide fluid biomarkers of axonal and glial pathology respectively.

---

## Key Findings

### Finding 1: PMP22 Duplication Dominance in CMT Genetics

PMP22 duplication on 17p11.2 is unequivocally the most common genetic cause of CMT disease. In a landmark whole-genome sequencing study of 1,515 CMT patients from a UK specialist center, PMP22 duplication accounted for 505 of 1,165 genetically diagnosed cases (43.3%), with an overall diagnostic rate of 76.9% ([PMID: 38481354](https://pubmed.ncbi.nlm.nih.gov/38481354/)). When considered as a proportion of all pathogenic variations including copy number variants, PMP22 duplication accounts for approximately 60% ([PMID: 31852984](https://pubmed.ncbi.nlm.nih.gov/31852984/)). More than 130 disease-causing genes have now been identified, confirming the extreme genetic heterogeneity posited by the canonical model. The reciprocal deletion of the same 1.5Mb region causes HNPP (hereditary neuropathy with liability to pressure palsies), confirming strict PMP22 dosage sensitivity ([PMID: 30258273](https://pubmed.ncbi.nlm.nih.gov/30258273/)).

UniProt SPARQL queries confirmed disease annotations for all five seed hypothesis genes (PMP22, MPZ, GJB1, MFN2, NEFL) across 20 disease associations. Notably, MPZ bridges CMT1B (demyelinating), CMT2I/CMT2J (axonal), and CMTDID (intermediate), while NEFL bridges CMT1F (demyelinating) and CMT2E (axonal), directly supporting the hypothesis that the demyelinating/axonal boundary is porous.

### Finding 2: CMT1A Is Dysmyelinating, Not Demyelinating

A critical correction to the canonical model terminology emerged from skin biopsy studies. Analysis of 32 CMT1A patients versus 12 controls revealed uniformly shortened internodal length (p<0.0001), with segmental demyelination entirely absent in the CMT1A group but present in CIDP ([PMID: 19923170](https://pubmed.ncbi.nlm.nih.gov/19923170/)). This establishes that CMT1A is fundamentally a *dysmyelinating* (developmental) rather than *demyelinating* (destructive) disorder. Long-term studies in PMP22-overexpressing mice confirmed that myelination is delayed during development and normal myelination is never reached, but once established, myelin is stable in adult animals ([PMID: 21487305](https://pubmed.ncbi.nlm.nih.gov/21487305/)). This distinction has significant implications for therapeutic timing -- interventions may need to target the developmental myelination window rather than preventing ongoing myelin destruction.

### Finding 3: PMP22 as a Structural Organizer of Myelin Architecture

High-resolution confocal imaging of CMT1A model mice (2026) revealed that PMP22 dosage changes profoundly disrupt molecular architecture at Schmidt-Lanterman incisures and Nodes of Ranvier: disorganized adherens junctions, mislocalized Connexin29, aberrant nodal ion channel distribution, nodal widening, and abnormal Kv1.2/Caspr spreading ([PMID: 41400104](https://pubmed.ncbi.nlm.nih.gov/41400104/)). This study also demonstrated "pronounced neuromuscular impairment in CMT1A model mice in the absence of overt axonal loss," challenging the assumption that motor deficits in CMT1A are entirely secondary to axonal loss. PMP22 is now proposed to function as a structural organizer coordinating adherens junction patterning and nodal subdomain integrity, with dysregulation predicted to compromise Schwann cell architecture, metabolic support, and axonal excitability.

### Finding 4: PMP22 Cholesterol Trafficking via CRAC Domain

PMP22 contains a cholesterol recognition amino acid consensus (CRAC) domain that is essential for cholesterol trafficking. PMP22 overexpression (modeling CMT1A) triggers cholesterol sequestration to lysosomes and reduces ABC transporter-dependent cholesterol efflux, while PMP22 point mutations (TrJ, Leu16Pro) retain cholesterol in the Golgi ([PMID: 32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/)). Critically, myelination deficits in dorsal root ganglia explants from heterozygous PMP22-deficient mice were improved by cholesterol supplementation, demonstrating that cholesterol trafficking defects are functionally relevant to myelination failure and potentially targetable.

### Finding 5: SARM1-Mitochondrial Feedback Loop in CMT2A

In a CMT2A rat model (Mfn2^H361Y), genetic deletion of SARM1 rescued axonal, synaptic, muscle, and functional phenotypes, demonstrating that SARM1 is the central executioner of axon degeneration in this model ([PMID: 36287202](https://pubmed.ncbi.nlm.nih.gov/36287202/)). Unexpectedly, loss of SARM1 also dramatically suppressed mitochondrial defects including number, size, and cristae density defects of synaptic mitochondria, revealing a previously unknown SARM1-mitochondrial feedback loop. This positions SARM1 as a druggable node that could protect axons in CMT2A independent of the primary MFN2 mutation.

### Finding 6: UPR/ER Stress as a Convergent Pathomechanism

IFB-088/Sephin1, a UPR modulator, improved motor function, neurophysiology, and myelination in both C3-PMP22 (CMT1A) and MpzR98C (CMT1B) mouse models ([PMID: 35501630](https://pubmed.ncbi.nlm.nih.gov/35501630/)). MPZ mutations (S63del, R98C) cause ER retention and UPR activation, while PMP22 mutations also trigger altered proteostasis and UPR. Treatment returned UPR markers toward wild-type levels. This identifies UPR/ER stress as a convergent mechanism across genetically distinct demyelinating CMT subtypes and validates it as a therapeutic target.

### Finding 7: Secondary Neuroinflammation Amplifies Demyelination

In CMT1X, CMT1A, and CMT1B mouse models, CD8+ T-lymphocytes and macrophages substantially increase in demyelinating nerves. Cross-breeding P0+/- and Cx32-/- mice with immunodeficient RAG-1-deficient mutants substantially alleviated the demyelinating phenotype ([PMID: 16775375](https://pubmed.ncbi.nlm.nih.gov/16775375/)). CSF-1/CSF-1R signaling regulates macrophage-related disease, and its blockade alleviates pathological alterations ([PMID: 26865613](https://pubmed.ncbi.nlm.nih.gov/26865613/)). Physical exercise in CMT1X mice reduced macrophage number and improved clinical outcome ([PMID: 34153322](https://pubmed.ncbi.nlm.nih.gov/34153322/)). However, systemic inhibition of the terminal complement system in CMT1A mice reduced neuroinflammation but did *not* improve motor function ([PMID: 36926597](https://pubmed.ncbi.nlm.nih.gov/36926597/)), indicating that not all immune pathways are equivalent therapeutic targets and that upstream macrophage-CSF1 signaling may be more relevant than downstream complement.

### Finding 8: Translational Gap -- Ascorbic Acid Failure

Five clinical trials of ascorbic acid in CMT1A patients uniformly failed despite robust preclinical data in PMP22 transgenic mice ([PMID: 26450076](https://pubmed.ncbi.nlm.nih.gov/26450076/)). A 2-year multicenter RCT (CMT-TRIAAL/CMT-TRAUK) of 277 patients showed no difference in CMTNS between ascorbic acid and placebo groups (mean difference 0.0, 95% CI -0.6 to 0.7; p=0.93) ([PMID: 21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/)). Pharmacokinetic limitations -- tight control of ascorbic acid absorption -- likely explain the translational failure ([PMID: 23525455](https://pubmed.ncbi.nlm.nih.gov/23525455/)). This episode underscores the gap between rodent PMP22-lowering and human efficacy.

### Finding 9: Advancing PMP22-Targeting Therapies

PMP22-targeting ASOs reversed CMT1A features in rodent models even when treatment was initiated *after* disease onset, restoring myelination, motor nerve conduction velocity, and compound muscle action potentials to near-wild-type levels ([PMID: 29202483](https://pubmed.ncbi.nlm.nih.gov/29202483/)). PMP22 mRNA reduction in skin biopsies was validated as a target engagement biomarker. AAV9-miRNA gene therapy (miR871) produced long-term expression in Schwann cells, selective RNAi against PMP22 mRNA, and improved disease manifestations in a humanized CMT1A model, with safety and biodistribution confirmed in non-human primates ([PMID: 41948127](https://pubmed.ncbi.nlm.nih.gov/41948127/)). PXT3003 demonstrated statistically significant improvement in the ONLS primary endpoint in phase III (mean difference -0.37 points; 97.5% CI [-0.68 to -0.06]; p=0.008), though the trial was complicated by early discontinuation of the high-dose arm due to formulation issues ([PMID: 34656144](https://pubmed.ncbi.nlm.nih.gov/34656144/)).

### Finding 10: Phenotypic Variability and Genetic Modifiers

Despite uniform PMP22 duplication genotype, CMT1A shows considerable phenotypic variability. A case-only GWAS of 644 CMT1A patients identified suggestive association signals at four loci ([PMID: 30958311](https://pubmed.ncbi.nlm.nih.gov/30958311/)). The CMT rat transcriptome revealed dysregulation of lipid metabolism-associated genes (e.g., PPARgamma) as potential modifiers ([PMID: 22189569](https://pubmed.ncbi.nlm.nih.gov/22189569/)). iPSC-derived neural crest cells from CMT patients identified a glutathione-mediated detoxification pathway as a shared molecular signature across genetically heterogeneous CMT ([PMID: 28704293](https://pubmed.ncbi.nlm.nih.gov/28704293/)).

### Finding 11: Biomarker Landscape

MRI calf muscle fat fraction has emerged as the most responsive biomarker for CMT1A clinical trials. In 20 CMT1A patients followed for a mean of 4 years, 12-month calf fat progression correlated significantly with annualized CMTES progression at final visit (rho=0.65, p=0.01) ([PMID: 39957630](https://pubmed.ncbi.nlm.nih.gov/39957630/)). Plasma NfL and GFAP are significantly elevated in CMT patients versus controls and correlate with clinical severity (CMTNSv2) ([PMID: 39882365](https://pubmed.ncbi.nlm.nih.gov/39882365/)). Sphingolipid and glycerophospholipid changes in plasma of CMT1A patients represent potential lipid biomarkers ([PMID: 32982928](https://pubmed.ncbi.nlm.nih.gov/32982928/)). Automated AI segmentation of MRI has been validated with SRM of 0.65-0.69, enabling scalable analysis for multicenter trials ([PMID: 37979968](https://pubmed.ncbi.nlm.nih.gov/37979968/)).

{{figure:evidence_strength_heatmap.png|caption=Evidence strength heatmap showing support for each core claim of the canonical CMT model across different evidence dimensions (human genetics, animal models, clinical trials, biomarkers, structural/molecular biology). Green indicates strong support; yellow indicates moderate; red indicates weak or contradicted.}}

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Subtype/Context | Confidence |
|---|----------|--------------|-----------|--------------------------|-------------|-----------------|------------|
| 1 | [PMID: 38481354](https://pubmed.ncbi.nlm.nih.gov/38481354/) | Human clinical (n=1515) | Supports | PMP22 duplication is most common CMT cause | 43.3% of diagnosed cases; 76.9% overall diagnostic rate | All CMT | High |
| 2 | [PMID: 31852984](https://pubmed.ncbi.nlm.nih.gov/31852984/) | Human clinical (n=200) | Supports | PMP22 CNV dominance | ~60% of pathogenic variations; other CNVs rare | CMT1A | High |
| 3 | [PMID: 19923170](https://pubmed.ncbi.nlm.nih.gov/19923170/) | Human clinical (n=32) | Qualifies | CMT1A is demyelinating | Uniformly shortened internodes; NO segmental demyelination (p<0.0001) | CMT1A | High -- corrects terminology |
| 4 | [PMID: 41400104](https://pubmed.ncbi.nlm.nih.gov/41400104/) | Model organism | Qualifies | PMP22 as compact myelin component | PMP22 organizes adherens junctions and nodal subdomains; motor deficit without axon loss | CMT1A/HNPP | High -- recent 2026 data |
| 5 | [PMID: 32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/) | In vitro + model | Supports/Extends | PMP22 role in myelin | PMP22 CRAC domain controls cholesterol trafficking; overexpression sequesters cholesterol | CMT1A | Moderate-High |
| 6 | [PMID: 36287202](https://pubmed.ncbi.nlm.nih.gov/36287202/) | Model organism | Supports/Extends | Axonal degeneration mechanism | SARM1 deletion rescues axons, synapses, muscle, mitochondria in CMT2A rat | CMT2A | High |
| 7 | [PMID: 35501630](https://pubmed.ncbi.nlm.nih.gov/35501630/) | Model organism | Supports/Extends | UPR as convergent mechanism | IFB-088/Sephin1 improves both CMT1A and CMT1B mouse models | CMT1A, CMT1B | Moderate-High |
| 8 | [PMID: 16775375](https://pubmed.ncbi.nlm.nih.gov/16775375/) | Model organism | Supports/Extends | Immune amplification | RAG-1 deficiency alleviates demyelination in CMT1X and CMT1B models | CMT1X, CMT1B | High |
| 9 | [PMID: 36926597](https://pubmed.ncbi.nlm.nih.gov/36926597/) | Model organism | Qualifies | Immune-targeted therapy | Complement inhibition reduces inflammation but NOT motor function in CMT1A | CMT1A | Moderate -- limits immune approach |
| 10 | [PMID: 26450076](https://pubmed.ncbi.nlm.nih.gov/26450076/) | Review of 5 RCTs | Qualifies | PMP22-lowering translates to humans | All 5 ascorbic acid trials failed despite preclinical success | CMT1A | High -- robust negative evidence |
| 11 | [PMID: 21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/) | Human RCT (n=277) | Qualifies | Ascorbic acid efficacy | No difference in CMTNS at 24 months (p=0.93) | CMT1A adults | High |
| 12 | [PMID: 29202483](https://pubmed.ncbi.nlm.nih.gov/29202483/) | Model organism | Supports | PMP22-dosage axis is targetable | ASOs reverse CMT1A features post-onset in rodents | CMT1A | High preclinical |
| 13 | [PMID: 41948127](https://pubmed.ncbi.nlm.nih.gov/41948127/) | Model + NHP safety | Supports | PMP22 gene therapy | AAV9-miR871 effective in humanized CMT1A model; NHP safety confirmed | CMT1A | Moderate-High |
| 14 | [PMID: 34656144](https://pubmed.ncbi.nlm.nih.gov/34656144/) | Human RCT (n=323) | Supports | Polypharmacology | PXT3003 high-dose: ONLS improvement p=0.008 vs placebo | CMT1A | Moderate -- formulation issues |
| 15 | [PMID: 25216747](https://pubmed.ncbi.nlm.nih.gov/25216747/) | Model organism | Supports/Extends | Schwann cell repair program | c-Jun inactivation exacerbates axon loss in CMT1A; c-Jun is protective | CMT1A | High |
| 16 | [PMID: 32686211](https://pubmed.ncbi.nlm.nih.gov/32686211/) | Model organism | Supports/Extends | Metabolic support | SC-specific MCT1 KO disrupts NMJ innervation; lactate supports myelination | General PNS | Moderate |
| 17 | [PMID: 38581130](https://pubmed.ncbi.nlm.nih.gov/38581130/) | Human clinical (n=1564) | Supports | Phenotypic variability | Considerable severity variability despite shared PMP22 duplication | CMT1A | High |
| 18 | [PMID: 30958311](https://pubmed.ncbi.nlm.nih.gov/30958311/) | Human GWAS (n=644) | Supports | Genetic modifiers | Suggestive signals at 4 loci for clinical outcomes | CMT1A | Moderate -- suggestive only |
| 19 | [PMID: 28796392](https://pubmed.ncbi.nlm.nih.gov/28796392/) | Human longitudinal (n=206) | Supports | Disease progression | CMTPedS progressed 14% over 2 years; CMT2A faster than CMT1A | Pediatric CMT | High |
| 20 | [PMID: 39957630](https://pubmed.ncbi.nlm.nih.gov/39957630/) | Human longitudinal (n=20) | Supports | Imaging biomarker | 12-month calf FF predicts 4-year CMTES (rho=0.65, p=0.01) | CMT1A | Moderate-High |
| 21 | [PMID: 39882365](https://pubmed.ncbi.nlm.nih.gov/39882365/) | Human biomarker (n=88) | Supports | Fluid biomarkers | NfL, GFAP, GDF15, FGF21 elevated in CMT; NfL/GFAP correlate with severity | All CMT | Moderate |
| 22 | [PMID: 32982928](https://pubmed.ncbi.nlm.nih.gov/32982928/) | Model + human | Supports/Extends | Lipid metabolism | SP/GP changes in CMT1A rat and human plasma; therapeutic potential | CMT1A | Moderate |
| 23 | [PMID: 29350067](https://pubmed.ncbi.nlm.nih.gov/29350067/) | Model organism | Extends | NRG1 pathway | Soluble NRG1 strongly upregulated in CMT1A rat; injury-like pattern | CMT1A | Moderate |
| 24 | [PMID: 28704293](https://pubmed.ncbi.nlm.nih.gov/28704293/) | iPSC in vitro | Extends | Shared molecular signature | Glutathione pathway identified across PMP22/MPZ/EGR2 iPSC models | Multiple CMT1 | Moderate |
| 25 | [PMID: 34153322](https://pubmed.ncbi.nlm.nih.gov/34153322/) | Model organism | Supports | Exercise intervention | Voluntary running reduces macrophages and improves clinical outcome in CMT1X | CMT1X | Moderate |
| 26 | [PMID: 11389829](https://pubmed.ncbi.nlm.nih.gov/11389829/) | Human + model | Competing | KIF1B in CMT2A | Original KIF1B-CMT2A report; now contested as MFN2 is primary CMT2A gene | CMT2A | Low -- contested |
| 27 | [PMID: 30126838](https://pubmed.ncbi.nlm.nih.gov/30126838/) | In vitro + model | Qualifies | KIF1B mechanism | KIF1Bbeta impairs IGF1R transport but limited pedigrees; controversial | CMT2A | Low-Moderate |
| 28 | [PMID: 41108054](https://pubmed.ncbi.nlm.nih.gov/41108054/) | Review/systematic | Qualifies | CRISPR for CMT | Field at early discovery stage; no near-term clinical applicability | CMT1A | Review-level |
| 29 | [PMID: 37455204](https://pubmed.ncbi.nlm.nih.gov/37455204/) | Review | Supports | Therapeutic pipeline | PXT3003 in most advanced phase; HDAC6i, NRG1, Nav1.8 emerging | CMT1A | Review-level |

{{figure:final_summary_visualization.png|caption=Four-panel summary: (A) Distribution of evidence types across the 36 findings, (B) Knowledge gaps ranked by priority, (C) Therapeutic pipeline from preclinical to clinical, and (D) Mechanistic model overview showing upstream triggers converging on axonal degeneration.}}

---

## Mechanistic Causal Chain

The canonical model implies a causal chain from upstream genetic trigger to clinical phenotype. Below, we annotate each step with the strength of evidence and identify gaps.

### CMT1A (Demyelinating) Causal Chain

```
PMP22 DUPLICATION (17p11.2)                    [ESTABLISHED - human genetics]
        |
        v
PMP22 mRNA/protein overexpression              [ESTABLISHED - rodent models, skin biopsy]
        |
        +---> Cholesterol trafficking defect    [EMERGING - CRAC domain, in vitro]
        |     (lysosomal sequestration)
        |
        +---> Disrupted adherens junctions      [EMERGING - 2026 confocal data]
        |     at SLI and Nodes of Ranvier
        |
        +---> ER stress / UPR activation        [ESTABLISHED - shared with CMT1B]
        |
        +---> Altered lipid metabolism           [EMERGING - SP/GP changes in plasma]
        |     (sphingolipid, glycerophospholipid)
        |
        v
SCHWANN CELL DYSFUNCTION                       [ESTABLISHED]
(dysmyelination, NOT demyelination)
        |
        +---> Uniformly shortened internodes    [ESTABLISHED - skin biopsy, p<0.0001]
        |
        +---> NRG1 pathway upregulation         [EMERGING - injury-like state]
        |
        +---> c-Jun activation (PROTECTIVE)     [ESTABLISHED - genetic evidence]
        |
        v
SECONDARY NEUROINFLAMMATION                    [ESTABLISHED - genetic cross experiments]
(macrophages, CD8+ T cells, CSF-1 axis)
        |
        +---> Complement activation             [INSUFFICIENT alone for motor rescue]
        |
        v
IMPAIRED METABOLIC SUPPORT                     [EMERGING - MCT1, lactate shuttling]
        |
        v
LENGTH-DEPENDENT AXONAL DEGENERATION          [ESTABLISHED - clinical, NfL correlation]
        |
        v
DISTAL MOTOR/SENSORY LOSS                     [ESTABLISHED - clinical phenotype]
(foot deformity, weakness, absent reflexes)
```

### CMT2A (Axonal) Causal Chain

```
MFN2 MUTATION                                  [ESTABLISHED - human genetics]
        |
        v
MITOCHONDRIAL FUSION DEFECT                    [ESTABLISHED - in vitro, animal models]
        |
        +---> Impaired mitochondrial transport  [ESTABLISHED but debated mechanism]
        |
        +---> ER-mitochondria contact disruption [EMERGING]
        |
        v
SARM1 ACTIVATION                               [ESTABLISHED - rat rescue experiments]
        |
        +---> NAD+ depletion in axons           [INFERRED from SARM1 biology]
        |
        +---> FEEDBACK to mitochondria          [ESTABLISHED - unexpected finding]
        |
        v
AXONAL DEGENERATION (length-dependent)         [ESTABLISHED]
        |
        v
DISTAL MOTOR/SENSORY LOSS                     [ESTABLISHED - faster progression than CMT1A]
```

**Key missing causal steps:**
1. The precise mechanism by which PMP22 overexpression (vs. point mutations) triggers Schwann cell dysfunction at the molecular level remains incompletely characterized
2. How cholesterol trafficking defects, ER stress, and lipid metabolism changes interact to produce dysmyelination is unclear
3. The signal from dysmyelinating Schwann cells to axons that triggers degeneration (beyond metabolic support withdrawal) is unresolved
4. Why phenotypic severity varies enormously among patients with identical PMP22 duplication remains unexplained at the molecular level

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain diagram showing the cascade from genetic mutations through Schwann cell dysfunction and axonal degeneration to clinical phenotype, with evidence strength annotations for each step.}}

---

## Alternative and Competing Models

### 1. Oxidative Stress / Glutathione Pathway Model
**Relationship:** Parallel mechanism / downstream consequence
iPSC-derived neural crest cells from CMT patients with PMP22 duplication, MPZ, and EGR2 mutations show increased GSTT2 expression and reactive oxygen species production ([PMID: 28704293](https://pubmed.ncbi.nlm.nih.gov/28704293/)). This may represent a shared downstream consequence rather than an independent mechanism, but positions ROS as a potential convergent therapeutic target across genetically heterogeneous CMT.

### 2. NRG1/ErbB Signaling Dysregulation Model
**Relationship:** Parallel mechanism with therapeutic implications
Soluble NRG1 isoforms and ErbB2/ErbB3 co-receptors are strongly upregulated in CMT1A rat nerves, mimicking an injured-nerve transcriptional pattern ([PMID: 29350067](https://pubmed.ncbi.nlm.nih.gov/29350067/)). NRG1-ERBB2/3 imbalance also underlies CMT4H pathology, with niacin treatment reducing myelin outfoldings ([PMID: 36314052](https://pubmed.ncbi.nlm.nih.gov/36314052/)). This positions NRG1 pathway modulation as both a mechanistic layer and an alternative therapeutic axis for multiple CMT subtypes.

### 3. SARM1-Mediated Axon Death Pathway
**Relationship:** Downstream executioner / druggable convergence node
SARM1 deletion rescues essentially all neuropathological features in CMT2A rats, including unexpected suppression of mitochondrial defects ([PMID: 36287202](https://pubmed.ncbi.nlm.nih.gov/36287202/)). This does not compete with the canonical model but identifies a convergence node that could be therapeutically targeted across axonal CMT subtypes regardless of the upstream gene.

### 4. Immune-Mediated Amplification Model
**Relationship:** Modifier / amplifier of primary mechanism
Genetic evidence from RAG-1-deficient crosses demonstrates that adaptive immunity substantially amplifies demyelination in CMT models ([PMID: 16775375](https://pubmed.ncbi.nlm.nih.gov/16775375/)). However, complement inhibition alone was insufficient to improve motor function ([PMID: 36926597](https://pubmed.ncbi.nlm.nih.gov/36926597/)), suggesting that immune modulation may be a useful adjunct but cannot replace correction of the primary genetic defect.

### 5. Metabolic Support Failure Model
**Relationship:** Downstream consequence / parallel mechanism
Schwann cell MCT1-mediated lactate shuttling is required for long-term axonal maintenance ([PMID: 32686211](https://pubmed.ncbi.nlm.nih.gov/32686211/)). Lactate increases Krox20/Egr2 and P0 expression in Schwann cells ([PMID: 25762662](https://pubmed.ncbi.nlm.nih.gov/25762662/)). This suggests that metabolic support failure may be an intermediate mechanism linking Schwann cell dysfunction to axonal degeneration, providing a mechanistic explanation for the "secondary axonal loss" described in the canonical model.

### 6. Non-Mendelian / Oligogenic Inheritance Model
**Relationship:** Extension / complication
Rare variant burden analysis in CMT cases (n=343) and HSP cases (n=515) supports complex inheritance mechanisms in historically Mendelian disorders, with a preliminary risk allele in EXOC4 (p=6.9x10^-6, OR=2.1) ([PMID: 32741968](https://pubmed.ncbi.nlm.nih.gov/32741968/)). Concomitant variants in multiple CMT genes were found in 2.1% of a Chinese cohort ([PMID: 35153971](https://pubmed.ncbi.nlm.nih.gov/35153971/)). This does not refute the canonical model but challenges its purely Mendelian framing for some patients.

---

## Knowledge Gaps

### Gap 1: Human Proof-of-Concept for PMP22-Lowering Therapy
**Scope:** Critical translational gap
**Why it matters:** The entire PMP22-dosage axis, validated extensively in rodent models, lacks definitive human validation. Five ascorbic acid trials failed. PXT3003 showed modest efficacy but through a polypharmacological mechanism, not direct PMP22 lowering.
**What was checked:** All published CMT1A clinical trials; ASO and gene therapy preclinical literature
**Resolution:** First-in-human PMP22 ASO or AAV9-miRNA gene therapy trial results (expected within 2-5 years based on pipeline stage)

### Gap 2: Complete Absence of Human Peripheral Nerve Single-Cell/Spatial Omics
**Scope:** Foundational data absence
**Why it matters:** No published single-cell RNA-seq or spatial transcriptomics study of human CMT peripheral nerve tissue exists. All Schwann cell subtype and state characterization comes from mouse models or non-CMT human tissue.
**What was checked:** PubMed searches for "CMT single-cell RNA-seq," "Schwann cell scRNA-seq CMT," "CMT spatial transcriptomics"
**Resolution:** scRNA-seq or spatial transcriptomics of sural nerve biopsies from CMT1A patients vs. controls

### Gap 3: Mechanism of PMP22 Overexpression-Induced Schwann Cell Dysfunction
**Scope:** Core mechanistic gap
**Why it matters:** The precise molecular cascade from 1.5x PMP22 protein levels to dysmyelination is incompletely characterized. How cholesterol trafficking, ER stress, lipid metabolism, and adherens junction disruption interact and which is primary vs. secondary remains unknown.
**What was checked:** All PMP22 functional studies identified in search
**Resolution:** Time-course proteomics and lipidomics in inducible PMP22-overexpression Schwann cell systems

### Gap 4: Genetic Modifier Architecture of CMT1A
**Scope:** Explains phenotypic variability
**Why it matters:** Despite identical PMP22 duplication, CMT1A severity varies enormously, and the GWAS signals (4 loci at suggestive level) have not been replicated or functionally validated.
**What was checked:** [PMID: 30958311](https://pubmed.ncbi.nlm.nih.gov/30958311/), [PMID: 38581130](https://pubmed.ncbi.nlm.nih.gov/38581130/)
**Resolution:** Larger GWAS (n>5000 CMT1A); whole-genome sequencing modifier studies; functional validation of candidate loci

### Gap 5: Biomarker Responsiveness to Effective Therapy
**Scope:** Clinical trial design gap
**Why it matters:** While MRI fat fraction, NfL, GFAP, and plasma lipids distinguish CMT from controls and correlate with severity, none has been shown to change in response to an effective therapy. Their utility as surrogate endpoints is therefore unvalidated.
**What was checked:** All biomarker studies in CMT; no treatment-response biomarker data found
**Resolution:** Biomarker substudies within upcoming ASO/gene therapy trials

### Gap 6: KIF1B Attribution in CMT2A
**Scope:** Gene-disease attribution controversy
**Why it matters:** The original KIF1B-CMT2A association ([PMID: 11389829](https://pubmed.ncbi.nlm.nih.gov/11389829/)) is contested; most CMT2A cases are attributed to MFN2. The canonical model lists KIF1B as a CMT gene, but evidence is limited to a few pedigrees.
**What was checked:** [PMID: 30126838](https://pubmed.ncbi.nlm.nih.gov/30126838/); CMT2A gene attribution literature
**Resolution:** Large-scale segregation studies; functional validation in human iPSC-derived motor neurons

### Gap 7: Long-Term Safety of Gene Therapy for CMT
**Scope:** Translational safety
**Why it matters:** AAV9-miRNA and lentiviral GJB1 gene therapies show preclinical efficacy, but long-term effects of sustained PMP22 suppression (risk of inducing HNPP-like phenotype) and immune responses to viral vectors in the PNS are unknown.
**What was checked:** [PMID: 41948127](https://pubmed.ncbi.nlm.nih.gov/41948127/), [PMID: 40055046](https://pubmed.ncbi.nlm.nih.gov/40055046/), [PMID: 26010264](https://pubmed.ncbi.nlm.nih.gov/26010264/)
**Resolution:** Long-term (>2 year) NHP safety studies; careful titration studies to achieve partial (not complete) PMP22 suppression

{{figure:biomarker_landscape_and_gaps.png|caption=Left panel: CMT biomarker landscape mapping validation level against responsiveness. MRI fat fraction leads in responsiveness; NfL and GFAP lead in biological validation. Right panel: Knowledge gap resolution status showing current evidence strength and projected closure timeline.}}

---

## Discriminating Tests

### Test 1: First-in-Human PMP22 ASO Trial
**Design:** Phase 1/2 dose-escalation in CMT1A patients (mild-moderate severity, baseline calf FF 5-70%)
**Biomarkers:** Skin biopsy PMP22 mRNA (target engagement), MRI calf FF (12-month), plasma NfL/GFAP (axonal/glial response)
**Expected result if hypothesis correct:** PMP22 mRNA reduction in skin correlates with MRI fat fraction stabilization and NfL reduction
**Discriminates from:** Non-PMP22-dependent mechanisms; tests whether rodent ASO efficacy translates to humans

### Test 2: Human Peripheral Nerve Spatial Transcriptomics
**Design:** Spatial transcriptomics of sural nerve biopsies from CMT1A patients (n>=10) vs. age-matched controls
**Expected result if hypothesis correct:** PMP22-overexpressing Schwann cells show UPR activation, cholesterol pathway disruption, NRG1 upregulation, and c-Jun activation, with gradient from paranodal to compact myelin regions
**Discriminates from:** Whether mouse model transcriptional changes are recapitulated in human tissue

### Test 3: SARM1 Inhibitor Trial in CMT2A
**Design:** Phase 1/2 in genetically confirmed CMT2A (MFN2 mutation) patients
**Biomarkers:** Plasma NfL (axonal protection), CMAP amplitude, MRI muscle fat fraction
**Expected result if hypothesis correct:** NfL stabilization or reduction, CMAP amplitude preservation
**Discriminates from:** Whether SARM1 is the rate-limiting executioner in human CMT2A as in rodent models

### Test 4: CMT1A Modifier GWAS Replication
**Design:** GWAS in >5,000 CMT1A patients with PMP22 duplication, stratified by disease severity (CMTNSv2)
**Expected result:** Replication of suggestive signals from [PMID: 30958311](https://pubmed.ncbi.nlm.nih.gov/30958311/); identification of genome-wide significant modifiers
**Discriminates from:** Whether phenotypic variability is genetic vs. environmental/stochastic

### Test 5: Cholesterol Supplementation in CMT1A
**Design:** Pilot trial of targeted cholesterol supplementation (or LXR agonist) in CMT1A patients
**Biomarkers:** Plasma lipid profiles (SP/GP), MRI fat fraction, nerve conduction studies
**Expected result if lipid hypothesis correct:** Improvement in myelin-related parameters
**Discriminates from:** Whether cholesterol trafficking is a treatable mechanism vs. epiphenomenon

---

## Curation Leads

The following are candidate updates for the Disorder Mechanisms Knowledge Base, labeled as leads requiring curator verification.

### Candidate Evidence References

1. **[PMID: 41400104](https://pubmed.ncbi.nlm.nih.gov/41400104/)** -- Snippet: *"PMP22 functions as a structural organizer of myelin, coordinating adherens junction patterning and nodal subdomain integrity."* Candidate addition to PMP22 functional annotation; qualifies the "compact myelin component" description.

2. **[PMID: 36287202](https://pubmed.ncbi.nlm.nih.gov/36287202/)** -- Snippet: *"deletion of Sarm1 rescued axonal, synaptic, muscle, and functional phenotypes, demonstrating that SARM1 was responsible for much of the neuropathology in this model."* Candidate addition as mechanism for CMT2A axonal degeneration.

3. **[PMID: 19923170](https://pubmed.ncbi.nlm.nih.gov/19923170/)** -- Snippet: *"Internodal length was uniformly shortened in patients with Charcot-Marie-Tooth disease type 1A... Segmental demyelination was absent."* Candidate correction of "demyelinating" to "dysmyelinating" in CMT1A description.

4. **[PMID: 39957630](https://pubmed.ncbi.nlm.nih.gov/39957630/)** -- Snippet: *"Calf muscle fat progression at 12 months correlated significantly with annualised CMT Examination Score progression at final visit."* Candidate biomarker node for CMT1A.

5. **[PMID: 39882365](https://pubmed.ncbi.nlm.nih.gov/39882365/)** -- Snippet: *"plasma concentrations of NfL, GFAP, GDF15, and FGF21 are significantly elevated in patients with CMT compared to controls."* Candidate biomarker evidence supporting dual axonal-glial pathology.

### Candidate Pathophysiology Nodes/Edges

- **Add edge:** PMP22 overexpression --> cholesterol trafficking defect (via CRAC domain)
- **Add edge:** PMP22 overexpression --> adherens junction disorganization at SLI/nodes
- **Add edge:** MFN2 mutation --> SARM1 activation --> axonal NAD+ depletion --> degeneration
- **Add edge:** SARM1 --> mitochondrial feedback (bidirectional)
- **Add node:** c-Jun-dependent Schwann cell repair program (protective modifier)
- **Add node:** Macrophage-CSF1 neuroinflammation (disease amplifier across CMT1/1X/1B)

### Candidate Ontology Terms

- **Cell types:** Myelinating Schwann cell (CL:0000218), Non-myelinating Schwann cell, Neural crest cell (CL:0000333), Endoneurial macrophage
- **Biological processes:** Myelination (GO:0042552), Cholesterol transport (GO:0030301), Unfolded protein response (GO:0006986), Axon degeneration (GO:0031175), Schwann cell differentiation (GO:0014037), Wallerian degeneration

### Candidate Status Changes

- **Terminology correction:** Replace "demyelinating neuropathy" with "dysmyelinating neuropathy" for CMT1A specifically (retain "demyelinating" for acquired forms like CIDP). Evidence: [PMID: 19923170](https://pubmed.ncbi.nlm.nih.gov/19923170/), [PMID: 21487305](https://pubmed.ncbi.nlm.nih.gov/21487305/).
- **KIF1B reclassification:** Downgrade KIF1B from established CMT2A gene to "limited/contested evidence." Evidence: [PMID: 30126838](https://pubmed.ncbi.nlm.nih.gov/30126838/).
- **Overall status:** Maintain CANONICAL with notation that the model requires the seven qualifications described in this report.

### Candidate Knowledge Gaps for KB

1. **No human proof-of-concept for direct PMP22-lowering therapy** -- Critical gap; ASO and gene therapy trials are the rate-limiting step for validating the PMP22-dosage axis in humans.
2. **No human nerve single-cell/spatial omics data for any CMT subtype** -- Foundational data absence that limits mechanistic understanding.
3. **Biomarker responsiveness to therapy is unvalidated** -- No biomarker has been tested against an effective treatment.
4. **Genetic modifier architecture of CMT1A is undefined** -- Only suggestive GWAS signals; no validated modifiers.

---

## Limitations of This Report

1. **Literature search scope:** While 128 papers were systematically reviewed, the search was conducted through PubMed and may miss preprints, conference abstracts, or non-English-language publications.
2. **Ascertainment bias:** Large CMT cohort studies are predominantly from Europe and North America; genetic spectrum and modifier effects may differ in understudied populations (e.g., sub-Saharan Africa, where novel variants are being discovered; [PMID: 40320863](https://pubmed.ncbi.nlm.nih.gov/40320863/)).
3. **Preclinical-to-clinical translation uncertainty:** Many mechanistic findings are from rodent models with supraphysiological PMP22 copy numbers (C22 mice: 7 copies) that may not reflect the 3-copy human situation. The C3-PMP mouse (3-4 copies) is more relevant but less widely used.
4. **Temporal limitation:** The CMT therapeutic field is rapidly evolving; ASO and gene therapy clinical trial results expected within 2-3 years could substantially alter the evidence landscape.
5. **Review-level evidence:** Several findings (CRISPR status, therapeutic pipeline overview) are derived from review articles rather than primary data.

{{figure:evidence_strength_assessment.png|caption=Evidence strength assessment across the major claims of the canonical CMT model, showing established, emerging, and speculative claims with their supporting evidence types.}}

---

## Conclusion

The Canonical PMP22/MPZ/Axonal & Demyelinating Peripheral Neuropathy Model for CMT is robustly supported as a framework but requires substantive updates to reflect the current state of knowledge. The model's core genetic architecture, phenotypic convergence, and therapeutic target (PMP22 dosage) are well-validated. The most consequential gaps are the absence of human proof-of-concept for direct PMP22-lowering therapy, the lack of human nerve omics data, and the incompletely characterized molecular cascade from PMP22 overexpression to Schwann cell dysfunction. The field is at a critical juncture: if the first PMP22 ASO or gene therapy trials demonstrate human efficacy, the canonical model will be definitively validated; if they fail, the field will need to reassess whether the rodent PMP22-dosage axis faithfully models human disease or whether additional mechanisms (NRG1, cholesterol, immune, metabolic) must be co-targeted for clinical benefit.
