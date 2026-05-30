---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T01:55:10.466661'
end_time: '2026-05-23T02:34:17.171483'
duration_seconds: 2346.71
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Aicardi-Goutieres Syndrome
  category: Mendelian
  hypothesis_group_id: ags_endogenous_nucleic_acid_interferon_model
  hypothesis_label: Endogenous Nucleic Acid and Type I Interferon Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: ags_endogenous_nucleic_acid_interferon_model\n\
    hypothesis_label: Endogenous Nucleic Acid and Type I Interferon Model\nstatus:\
    \ CANONICAL\ndescription: |\n  AGS-causing variants perturb enzymes and sensors\
    \ that normally clear, edit, process, or recognize nucleic acids and histone-associated\
    \ chromatin. The resulting self nucleic-acid or chromatin stress activates innate\
    \ immune pathways, including cGAS-STING in histone-processing subtypes, causing\
    \ chronic type I interferon signaling and multi-organ inflammatory injury.\nevidence:\n\
    - reference: PMID:25604658\n  reference_title: Characterization of human disease\
    \ phenotypes associated with mutations in TREX1, RNASEH2A,\n    RNASEH2B, RNASEH2C,\
    \ SAMHD1, ADAR, and IFIH1.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Patients with AGS consistently demonstrate increased levels of interferon\
    \ activity\n  explanation: Crow et al. connect the genotype spectrum to sustained\
    \ interferon activity and an interferon-stimulated\n    gene signature.\n- reference:\
    \ PMID:33230297\n  reference_title: cGAS-mediated induction of type I interferon\
    \ due to inborn errors of histone pre-mRNA\n    processing.\n  supports: SUPPORT\n\
    \  evidence_source: IN_VITRO\n  snippet: cGAS-stimulator of interferon genes (STING)\
    \ pathway in patient-derived\n  explanation: Patient-derived fibroblast experiments\
    \ connect LSM11/RNU7-1 histone-processing defects\n    to cGAS-STING-mediated\
    \ interferon signaling."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 35
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Aicardi-Goutieres Syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** ags_endogenous_nucleic_acid_interferon_model
- **Hypothesis Label:** Endogenous Nucleic Acid and Type I Interferon Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ags_endogenous_nucleic_acid_interferon_model
hypothesis_label: Endogenous Nucleic Acid and Type I Interferon Model
status: CANONICAL
description: |
  AGS-causing variants perturb enzymes and sensors that normally clear, edit, process, or recognize nucleic acids and histone-associated chromatin. The resulting self nucleic-acid or chromatin stress activates innate immune pathways, including cGAS-STING in histone-processing subtypes, causing chronic type I interferon signaling and multi-organ inflammatory injury.
evidence:
- reference: PMID:25604658
  reference_title: Characterization of human disease phenotypes associated with mutations in TREX1, RNASEH2A,
    RNASEH2B, RNASEH2C, SAMHD1, ADAR, and IFIH1.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Patients with AGS consistently demonstrate increased levels of interferon activity
  explanation: Crow et al. connect the genotype spectrum to sustained interferon activity and an interferon-stimulated
    gene signature.
- reference: PMID:33230297
  reference_title: cGAS-mediated induction of type I interferon due to inborn errors of histone pre-mRNA
    processing.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: cGAS-stimulator of interferon genes (STING) pathway in patient-derived
  explanation: Patient-derived fibroblast experiments connect LSM11/RNU7-1 histone-processing defects
    to cGAS-STING-mediated interferon signaling.
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

# Mechanistic Hypothesis Evaluation: Endogenous Nucleic Acid and Type I Interferon Model for Aicardi-Goutières Syndrome

**Hypothesis ID:** `ags_endogenous_nucleic_acid_interferon_model`
**Status in KB:** CANONICAL
**Report Date:** 2026-05-23

---

## Executive Judgment

**Verdict: STRONGLY SUPPORTED, with critical subtype-specific qualifications.**

The Endogenous Nucleic Acid and Type I Interferon Model is robustly validated as the canonical mechanistic framework for Aicardi-Goutières Syndrome (AGS). The hypothesis posits that AGS-causing variants perturb enzymes and sensors that normally clear, edit, process, or recognize nucleic acids and histone-associated chromatin, and that the resulting self nucleic-acid or chromatin stress activates innate immune pathways — including cGAS-STING and MDA5-MAVS — causing chronic type I interferon (IFN) signaling and multi-organ inflammatory injury. This model is supported by genetic epistasis experiments (cGAS knockout fully rescuing Trex1-deficient autoimmune disease in mice), pharmacological validation (at least five independent STING inhibitors rescuing Trex1-/- autoimmunity), near-universal IFN biomarker positivity (90% of AGS patients), gain-of-function evidence from IFIH1/MDA5 mutations directly proving that aberrant self-RNA sensing drives the disease spectrum, and mechanistic dissection of both the DNA-sensing (TREX1→cGAS-STING) and RNA-sensing (ADAR1→MDA5-MAVS) arms of the pathway.

However, the hypothesis requires important qualifications that limit its universality. The most consequential caveat is that **RNASEH2-related neuropathology is driven primarily by IFN-independent p53/DNA damage signaling**, not by cGAS-mediated neuroinflammation — cerebellar defects in RNASEH2B-knockout mice are rescued by p53 deletion but not by cGAS deletion. Approximately 27% of RNASEH2B patients lack elevated IFN signatures, and asymptomatic homozygous carriers of the most common AGS variant (RNASEH2B:p.Ala177Thr) have been identified, challenging a simple loss-of-function-to-IFN causal chain. Furthermore, JAK inhibitor clinical trials show limited neurological benefit despite reducing IFN scores, suggesting that IFN-independent pathways contribute substantially to CNS injury across multiple AGS subtypes. Collectively, the evidence indicates that while chronic type I IFN is the central systemic pathogenic driver, the neuropathology — particularly in RNASEH2 subtypes — involves parallel, IFN-independent mechanisms that the current model does not fully capture.

---

## Summary

Aicardi-Goutières Syndrome is a genetically heterogeneous type I interferonopathy caused by biallelic (or dominant gain-of-function) mutations in at least nine genes: *TREX1*, *RNASEH2A*, *RNASEH2B*, *RNASEH2C*, *SAMHD1*, *ADAR1*, *IFIH1*, *LSM11*, and *RNU7-1*. The Endogenous Nucleic Acid and Type I IFN Model provides a unifying framework that explains how loss-of-function in nucleic acid-metabolizing enzymes (TREX1, RNase H2, SAMHD1, ADAR1) or gain-of-function in nucleic acid sensors (MDA5/IFIH1) converges on chronic type I IFN production. This investigation systematically evaluated this model across all major AGS gene subtypes, examining evidence from human clinical cohorts, mouse genetic models, in vitro mechanistic studies, pharmacological interventions, and clinical trials.

The strongest evidence comes from definitive genetic epistasis studies: cGAS-knockout mice are completely protected from Trex1-deficiency-induced lethal autoimmunity, and MDA5 deletion rescues ADAR1 Zα-mutant encephalopathy. These experiments directly demonstrate that the innate immune DNA and RNA sensors are necessary mediators of disease. Pharmacological validation through multiple STING inhibitors in Trex1-/- mice and clinical use of JAK inhibitors in patients further corroborates the IFN-centric mechanism. However, this investigation identified a critical dissociation between systemic IFN-driven inflammation and neurodegenerative pathology, particularly in the RNASEH2 subgroup, where DNA damage/genome instability pathways operate independently of IFN signaling. This finding has direct therapeutic implications: effective AGS treatment likely requires targeting both the IFN pathway and IFN-independent neuronal injury mechanisms.

---

## Key Findings

### Finding 1: cGAS Is the Essential DNA Sensor Driving TREX1-Associated Autoimmunity

The most definitive evidence supporting the hypothesis comes from genetic epistasis experiments in the Trex1-knockout mouse model. Trex1-/- mice lacking cGAS are completely protected from lethality, exhibit dramatically reduced tissue inflammation, and fail to develop autoantibodies ([PMID: 26223655](https://pubmed.ncbi.nlm.nih.gov/26223655/)). This establishes cGAS as the obligate sensor that detects accumulated self-DNA in the cytosol when TREX1 exonuclease function is lost. Subsequent studies using conditional cGAS knockouts identified classical dendritic cells as a key cellular compartment where cGAS activation drives Trex1-deficient autoimmunity ([PMID: 39254994](https://pubmed.ncbi.nlm.nih.gov/39254994/)). Additionally, a knock-in mouse model carrying the Trex1-P212fs frameshift mutation confirmed that cGAS-STING pathway activation mediates the type I interferonopathy phenotype ([PMID: 40268028](https://pubmed.ncbi.nlm.nih.gov/40268028/)). These genetic experiments provide the strongest possible causal evidence linking self-DNA accumulation → cGAS activation → type I IFN → autoimmune disease.

### Finding 2: RNASEH2B Neuropathology Is IFN-Independent and Driven by p53/DNA Damage Signaling

A critical qualification to the hypothesis emerged from studies of RNASEH2-related disease. Cerebellar defects following RNASEH2B inactivation in mice are rescued by p53 deletion but **not** by cGAS deletion ([PMID: 34655526](https://pubmed.ncbi.nlm.nih.gov/34655526/)). This demonstrates that DNA damage signaling, rather than neuroinflammation, is the primary driver of neuropathology in RNASEH2-related AGS. The implication is profound: the IFN model explains the systemic inflammatory features but not the core neurodegeneration in the most common genetic subtype. RNASEH2 mutations cause genome instability through failure to excise misincorporated ribonucleotides from DNA, triggering replication stress and p53-dependent cell death in neural progenitors. This finding reframes the RNASEH2 subgroup as having a dual pathology — systemic IFN-driven inflammation plus cell-intrinsic DNA damage — and explains why anti-IFN therapies have limited neurological efficacy.

### Finding 3: ADAR1 Zα Domain Mutations Cause AGS via Failure to Edit Endogenous dsRNA, Sensed by MDA5

The RNA-sensing arm of the hypothesis is strongly validated by ADAR1 studies. ADAR1 p150 mutations in the Zα domain — which binds left-handed Z-RNA — reduce adenosine-to-inosine RNA editing of endogenous double-stranded RNA. Unedited dsRNAs are then sensed as "non-self" by MDA5, activating the MAVS-dependent type I IFN response. Mouse models carrying Adar1 Zα mutations develop AGS-like encephalopathy that is fully rescued by MDA5 deletion ([PMID: 34380029](https://pubmed.ncbi.nlm.nih.gov/34380029/); [PMID: 34525338](https://pubmed.ncbi.nlm.nih.gov/34525338/)). In human neuronal progenitor cells, ADAR1 knockout triggers MDA5-dependent spontaneous IFN production, PKR activation, and cell death ([PMID: 29395325](https://pubmed.ncbi.nlm.nih.gov/29395325/)). Importantly, recent work showed that blocking type I IFN signaling fully reversed ADAR1 Zα-mutant encephalopathy in mice, while deleting downstream effectors PKR or ZBP1 individually did not achieve rescue ([PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/)). This confirms that type I IFN itself — not individual dsRNA effectors — is the central pathogenic mediator in ADAR1-related AGS.

### Finding 4: LSM11/RNU7-1 Histone Processing Defects Activate cGAS-STING via Chromatin Stress

The newest AGS genes, *LSM11* and *RNU7-1*, encode components of the histone pre-mRNA processing machinery. Biallelic mutations cause misprocessing of replication-dependent histone transcripts, disturbed linker histone stoichiometry, altered nuclear cGAS distribution, and enhanced cGAS-STING-mediated IFN signaling ([PMID: 33230297](https://pubmed.ncbi.nlm.nih.gov/33230297/)). In vitro, chromatin lacking linker histones stimulates cGAMP production more efficiently, providing a direct biochemical link between chromatin stress and cGAS activation. This extends the hypothesis beyond canonical nucleic acid metabolism to include chromatin architecture as a trigger for innate immune activation.

### Finding 5: IFIH1 Gain-of-Function Mutations Prove Sensor Hyperactivation Alone Is Sufficient

Heterozygous gain-of-function mutations in *IFIH1* (encoding MDA5) cause the AGS phenotypic spectrum with an enhanced IFN state ([PMID: 24686847](https://pubmed.ncbi.nlm.nih.gov/24686847/)). Mutant MDA5 proteins bind RNA more avidly, increasing baseline and ligand-induced IFN signaling. This is conceptually important because it demonstrates that disease can arise not only from substrate accumulation (loss of clearance/editing) but also from increased sensor sensitivity — both converge on the same IFN-driven pathology. IFIH1 mutations thus serve as a "converse genetic proof" of the endogenous nucleic acid sensing model.

### Finding 6: 90% IFN Positivity, but RNASEH2B Patients Are Disproportionately IFN-Negative

In a systematic biomarker study, 74 of 82 (90%) AGS patients had positive IFN scores ([PMID: 24183309](https://pubmed.ncbi.nlm.nih.gov/24183309/)). Among the 8 IFN-negative patients, 7 carried *RNASEH2B* mutations (27% of all RNASEH2B patients). Repeat sampling confirmed stable IFN status. This biomarker pattern is consistent with the mouse data showing IFN-independent neuropathology in RNASEH2 mutants and suggests that a substantial minority of RNASEH2B patients may have disease driven primarily by non-IFN mechanisms.

### Finding 7: Pharmacological STING Inhibition Validates the cGAS-STING Axis In Vivo

At least five structurally distinct STING inhibitors — astin C ([PMID: 30566866](https://pubmed.ncbi.nlm.nih.gov/30566866/)), glabridin ([PMID: 38066431](https://pubmed.ncbi.nlm.nih.gov/38066431/)), carnosic acid ([PMID: 39965124](https://pubmed.ncbi.nlm.nih.gov/39965124/)), Compound Danshen Dripping Pill ([PMID: 38507852](https://pubmed.ncbi.nlm.nih.gov/38507852/)), and cyclopeptide STi-2 ([PMID: 38997793](https://pubmed.ncbi.nlm.nih.gov/38997793/)) — alleviate multi-organ inflammation in Trex1-deficient mice. An orally bioavailable STING inhibitor demonstrated in vivo anti-inflammatory activity ([PMID: 39875322](https://pubmed.ncbi.nlm.nih.gov/39875322/)). Additional repurposed agents including oxiconazole (targeting STING trafficking via OSBP; [PMID: 40319749](https://pubmed.ncbi.nlm.nih.gov/40319749/)) and midazolam (impairing STING ER-to-Golgi trafficking; [PMID: 40619030](https://pubmed.ncbi.nlm.nih.gov/40619030/)) also show efficacy. This pharmacological convergence provides independent, non-genetic validation of the cGAS-STING axis as a therapeutic target.

### Finding 8: JAK Inhibitors Show Limited Neurological Benefit Despite IFN Reduction

A multicenter retrospective study (n=12 treated vs. 20 untreated) found that JAK1/2 inhibitors improved immunological and dermatological symptoms but neurological impact was limited and heterogeneous ([PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/)). Greater benefits were seen in patients with mild/intermediate phenotypes and earlier treatment initiation. Neuropathology persists even after early baricitinib treatment initiated at 2 months of age, with post-mortem findings showing profound CNS sequelae despite over 4 years of therapy ([PMID: 38381212](https://pubmed.ncbi.nlm.nih.gov/38381212/)). In an RNU7-1 patient, baricitinib produced modest transient improvements but did not improve liver function, dystonia, or neurological function ([PMID: 39748568](https://pubmed.ncbi.nlm.nih.gov/39748568/)). These clinical observations strongly suggest that IFN-independent pathways contribute to CNS injury across AGS subtypes.

### Finding 9: RNASEH2B:p.Ala177Thr Shows Remarkable Phenotypic Variability Including Asymptomatic Homozygotes

The most common AGS variant worldwide, RNASEH2B:p.Ala177Thr, displays a phenotypic spectrum from severe neonatal encephalopathy to asymptomatic homozygous individuals ([PMID: 40812004](https://pubmed.ncbi.nlm.nih.gov/40812004/)). This incomplete penetrance challenges a deterministic model where loss of RNase H2 function inevitably produces IFN-driven disease. Modifier genes, environmental factors, or threshold effects likely modulate whether and how severely the innate immune pathway is activated.

### Finding 10: Astrocytes Are a Critical Cell Type in ADAR1-Related Encephalopathy

In ADAR1 Zα-mutant mice, astrocyte-specific ADAR1 dysfunction caused particularly severe AGS-like encephalopathy, and IFN-α levels were higher in CSF than in sera, suggesting intrathecal IFN production ([PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/)). Blocking type I IFN signaling fully reversed the encephalopathy. This identifies astrocytes as a key pathogenic cell type and CNS-compartmentalized IFN production as a driver of brain injury in ADAR1-related disease.

### Finding 11: PKR as an Additional dsRNA Sensor — Important but Not Dominant

ADAR1 knockout neuronal progenitor cells show both MDA5-dependent IFN production and PKR activation leading to translational shutdown and cell death ([PMID: 29395325](https://pubmed.ncbi.nlm.nih.gov/29395325/)). However, in ADAR1 Zα-mutant mice, PKR deletion alone did not rescue encephalopathy ([PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/)). This suggests PKR contributes to cellular pathology but is subordinate to the MDA5-IFN axis as the disease driver. ADAR1 thus acts as a "regulatory hub" preventing multiple dsRNA sensors from recognizing endogenous RNA ([PMID: 36469491](https://pubmed.ncbi.nlm.nih.gov/36469491/)).

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing the strength and type of evidence supporting or qualifying the AGS endogenous nucleic acid/IFN hypothesis across gene subtypes and experimental systems}}

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Subtype/Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|-----------------|------------|
| [PMID: 26223655](https://pubmed.ncbi.nlm.nih.gov/26223655/) | Model organism | **Supports** | cGAS senses self-DNA from TREX1 deficiency | cGAS-KO fully rescues Trex1-/- lethality, inflammation, autoantibodies | TREX1 | High — definitive epistasis |
| [PMID: 34655526](https://pubmed.ncbi.nlm.nih.gov/34655526/) | Model organism | **Qualifies** | IFN drives all AGS neuropathology | RNASEH2B cerebellar defects rescued by p53, NOT cGAS | RNASEH2B | High — direct genetic test |
| [PMID: 34380029](https://pubmed.ncbi.nlm.nih.gov/34380029/) | Model organism | **Supports** | ADAR1 Z-RNA binding prevents MDA5 activation | Zα mutation → MDA5/MAVS-dependent IFN and lethal autoinflammation | ADAR1 | High |
| [PMID: 34525338](https://pubmed.ncbi.nlm.nih.gov/34525338/) | Model organism | **Supports** | ADAR1 Zα mutations reduce editing, cause AGS | W197 Zα mutation reduces RNA editing; mice develop encephalopathy | ADAR1 | High |
| [PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/) | Model organism | **Supports** | IFN is the central mediator in ADAR1-AGS | Blocking IFN fully reverses encephalopathy; PKR/ZBP1 KO does not | ADAR1 | High |
| [PMID: 33230297](https://pubmed.ncbi.nlm.nih.gov/33230297/) | In vitro | **Supports** | Histone processing defects activate cGAS-STING | LSM11/RNU7-1 mutations → chromatin stress → cGAS-STING IFN | LSM11/RNU7-1 | Moderate-High |
| [PMID: 24686847](https://pubmed.ncbi.nlm.nih.gov/24686847/) | Human clinical | **Supports** | Sensor gain-of-function causes AGS | IFIH1 GoF mutations → enhanced MDA5 RNA binding → IFN | IFIH1 | High |
| [PMID: 25604658](https://pubmed.ncbi.nlm.nih.gov/25604658/) | Human clinical | **Supports** | All AGS genotypes converge on IFN | 374 patients: consistent elevated IFN; IFN level correlates with disability | All subtypes | High — large cohort |
| [PMID: 24183309](https://pubmed.ncbi.nlm.nih.gov/24183309/) | Human clinical | **Qualifies** | IFN is universal in AGS | 90% IFN-positive; 27% RNASEH2B patients IFN-negative | RNASEH2B | High |
| [PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/) | Human clinical | **Qualifies** | IFN blockade treats AGS | JAK inhibitors improve skin/immune features; limited neurological benefit | Multiple | Moderate — retrospective |
| [PMID: 38381212](https://pubmed.ncbi.nlm.nih.gov/38381212/) | Human clinical | **Qualifies** | Early IFN blockade prevents CNS damage | Profound CNS sequelae despite baricitinib from age 2 months | Not specified | Moderate — single case |
| [PMID: 40812004](https://pubmed.ncbi.nlm.nih.gov/40812004/) | Human clinical | **Qualifies** | RNASEH2B mutations deterministically cause AGS | Asymptomatic homozygotes for p.Ala177Thr exist | RNASEH2B | Moderate-High |
| [PMID: 29395325](https://pubmed.ncbi.nlm.nih.gov/29395325/) | In vitro | **Qualifies** | MDA5-IFN is the sole dsRNA effector | ADAR1-KO NPCs show MDA5-dependent IFN AND PKR-driven translational shutdown | ADAR1 | Moderate-High |
| [PMID: 30566866](https://pubmed.ncbi.nlm.nih.gov/30566866/) | Model organism | **Supports** | STING is a therapeutic target | Astin C inhibits cGAS-STING; rescues Trex1-/- inflammation | TREX1 | Moderate |
| [PMID: 39965124](https://pubmed.ncbi.nlm.nih.gov/39965124/) | Model organism | **Supports** | STING is a therapeutic target | Carnosic acid targets STING CTT; ameliorates Trex1-/- disease | TREX1 | Moderate |
| [PMID: 39254994](https://pubmed.ncbi.nlm.nih.gov/39254994/) | Model organism | **Supports** | cGAS in dendritic cells drives disease | Conditional cGAS-KO in cDCs prevents Trex1-/- autoimmunity | TREX1 | High |
| [PMID: 39630935](https://pubmed.ncbi.nlm.nih.gov/39630935/) | Human clinical | **Qualifies** | Retroelement RT drives TREX1-related IFN | RTI trial: insufficient evidence of efficacy at 6 weeks | TREX1 and others | Moderate — small trial |
| [PMID: 32720483](https://pubmed.ncbi.nlm.nih.gov/32720483/) | In vitro/Model | **Supports** | SAMHD1 deficiency → replication stress → cytosolic DNA → IFN | SAMHD1-KO cells accumulate cytosolic DNA from stalled forks | SAMHD1 | Moderate-High |
| [PMID: 40665566](https://pubmed.ncbi.nlm.nih.gov/40665566/) | Human clinical | **Supports** | Mitochondrial NA leakage can trigger AGS-like IFN | ATAD3 duplications cause AGS-like phenotype with CSF IFN-α elevation | ATAD3 (phenocopy) | Moderate |
| [PMID: 39332260](https://pubmed.ncbi.nlm.nih.gov/39332260/) | Human clinical | **Supports** | AGS is a multi-system interferonopathy | n=167: systemic onset precedes neurological; TREX1 most severe | All subtypes | High — large cohort |

---

## Mechanistic Causal Chain

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram showing how mutations in different AGS genes converge on type I IFN production through parallel DNA-sensing and RNA-sensing pathways, with the critical IFN-independent branch via p53 in RNASEH2 neuropathology}}

The hypothesis implies a multi-arm causal chain from upstream genetic triggers to clinical manifestation. Below, each link is annotated with the strength of supporting evidence (★★★ = strong direct evidence, ★★☆ = moderate/indirect, ★☆☆ = inferred/weak).

### Arm 1: DNA-Sensing Pathway (TREX1, SAMHD1, RNASEH2)

```
TREX1 loss-of-function
  → Failure to degrade cytosolic DNA (★★★ — biochemical + genetic)
    → Self-DNA accumulates in cytosol (★★★)
      → cGAS binds DNA, produces cGAMP (★★★ — epistasis in vivo)
        → STING activation → TBK1 → IRF3 (★★★ — pharmacological validation)
          → Type I IFN transcription (★★★)
            → ISG expression → systemic inflammation (★★★ — clinical biomarkers)
              → Multi-organ injury: skin, liver, hematologic (★★★)
              → CNS injury: calcifications, white matter loss (★★☆ — partial)

SAMHD1 loss-of-function
  → Elevated dNTP pools + replication stress (★★★)
    → Stalled replication forks → aberrant processing by MRE11/RECQ1 (★★☆)
      → Cytosolic DNA fragments (★★☆)
        → cGAS-STING activation → IFN (★★☆)

RNASEH2 loss-of-function
  → Failure to excise ribonucleotides from genomic DNA (★★★)
    → BRANCH A: Genome instability → p53-dependent neural progenitor death (★★★)
      → Neuropathology (IFN-INDEPENDENT) (★★★)
    → BRANCH B: Cytosolic DNA/RNA hybrids → cGAS → IFN (★★☆ — inferred)
      → Systemic inflammation (★★☆)
```

### Arm 2: RNA-Sensing Pathway (ADAR1, IFIH1)

```
ADAR1 loss-of-function (Zα domain mutations)
  → Failure to edit endogenous dsRNA (Alu elements, SINEs) (★★★)
    → Unedited dsRNA accumulates (★★★)
      → MDA5 senses dsRNA as "non-self" (★★★ — MDA5-KO rescues)
        → MAVS activation → IRF3/IRF7 (★★★)
          → Type I IFN transcription (★★★)
            → ISG expression → astrocyte dysfunction → encephalopathy (★★★)
      → PKR activation → translational shutdown (★★☆ — observed but not dominant)
      → ZBP1 activation → PANoptosis (★★☆ — observed; ZBP1-KO alone insufficient)

IFIH1 gain-of-function
  → MDA5 binds endogenous RNA with increased avidity (★★★)
    → Constitutive MAVS activation → IFN (★★★)
```

### Arm 3: Chromatin Stress (LSM11, RNU7-1)

```
LSM11/RNU7-1 loss-of-function
  → Misprocessing of replication-dependent histone pre-mRNAs (★★★)
    → Disturbed linker histone stoichiometry (★★☆)
      → Altered chromatin structure → cGAS redistribution (★★☆)
        → Enhanced cGAS-STING → IFN (★★☆)
```

### Convergence → Clinical Phenotype

```
Chronic Type I IFN → ISG upregulation →
  → Cerebral calcifications (basal ganglia, white matter)
  → Progressive white matter loss / leukodystrophy
  → Cerebral atrophy / microcephaly
  → CSF lymphocytosis
  → Chilblains / vasculopathy
  → Hepatosplenomegaly / liver dysfunction
  → Thrombocytopenia
  → Autoantibodies (lupus-like features)
```

**Key weak links in the causal chain:**

1. The exact identity of the endogenous DNA substrate for TREX1 remains debated (genomic DNA fragments vs. LINE-1 retroelement cDNA vs. mitochondrial DNA)
2. The mechanism by which RNASEH2 deficiency generates cGAS-activating ligands (distinct from its genome-instability effects) is weakly characterized
3. The link between SAMHD1's dNTPase activity, replication fork processing, and cytosolic DNA generation requires further validation
4. How chromatin stress in LSM11/RNU7-1 deficiency specifically activates cGAS (vs. other sensors) needs further mechanistic dissection

---

## Alternative and Competing Models

### 1. DNA Damage / Genome Instability Model (Parallel/Complementary)

**Relationship to seed hypothesis:** Parallel mechanism, particularly for RNASEH2 subtypes.

RNASEH2 mutations cause failure to excise misincorporated ribonucleotides, leading to replication stress, DNA breaks, and p53-dependent cell death in neural progenitors ([PMID: 34655526](https://pubmed.ncbi.nlm.nih.gov/34655526/)). This is demonstrably IFN-independent in the CNS. For SAMHD1, replication stress from elevated dNTPs or impaired fork processing also contributes to genome instability ([PMID: 32720483](https://pubmed.ncbi.nlm.nih.gov/32720483/)). This model is not competing but rather complementary — it explains the component of neuropathology that the IFN model cannot.

### 2. Retroelement Derepression Model (Upstream Trigger)

**Relationship to seed hypothesis:** Upstream mechanism specifying the endogenous DNA substrate.

LINE-1 retrotransposons have been proposed as a major source of the self-DNA that accumulates in TREX1-deficient cells ([PMID: 37643478](https://pubmed.ncbi.nlm.nih.gov/37643478/)). Reverse transcriptase inhibitors (RTIs) were tested clinically based on this model. However, a Trex1-/- mouse study showed that RTI treatment did not prevent autoimmunity ([PMID: 28835460](https://pubmed.ncbi.nlm.nih.gov/28835460/)), and a clinical crossover trial found insufficient evidence of RTI efficacy over 6 weeks ([PMID: 39630935](https://pubmed.ncbi.nlm.nih.gov/39630935/)). The retroelement hypothesis remains plausible but unproven as the dominant trigger.

### 3. Multi-Sensor dsRNA Effector Model (Downstream Elaboration)

**Relationship to seed hypothesis:** Downstream elaboration for ADAR1 subtypes.

In ADAR1 deficiency, multiple dsRNA sensors are activated: MDA5 (IFN), PKR (translational shutdown), ZBP1 (PANoptosis/necroptosis), and RNase L (cell death) ([PMID: 36469491](https://pubmed.ncbi.nlm.nih.gov/36469491/); [PMID: 29395325](https://pubmed.ncbi.nlm.nih.gov/29395325/); [PMID: 28362255](https://pubmed.ncbi.nlm.nih.gov/28362255/)). While IFN is the dominant driver of encephalopathy (PKR-KO and ZBP1-KO alone do not rescue; [PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/)), these additional sensors may contribute to cell-autonomous toxicity. This model does not contradict the seed hypothesis but adds mechanistic depth.

### 4. Microangiopathy Model (Downstream Consequence)

**Relationship to seed hypothesis:** Downstream consequence of chronic IFN.

Neuropathological studies revealed perivascular calcium deposition and microinfarctions, suggesting that IFN-driven microangiopathy contributes to brain injury ([PMID: 12365358](https://pubmed.ncbi.nlm.nih.gov/12365358/)). This is likely downstream of chronic IFN rather than an alternative mechanism.

### 5. Mitochondrial Nucleic Acid Leakage Model (Parallel Trigger)

**Relationship to seed hypothesis:** Parallel upstream trigger.

ATAD3 locus duplications cause a phenotype overlapping with AGS, with elevated CSF IFN-α, suggesting that mitochondrial nucleic acid leakage can activate the same IFN pathway ([PMID: 40665566](https://pubmed.ncbi.nlm.nih.gov/40665566/)). This supports the general framework while identifying an additional source of immunostimulatory nucleic acids.

---

## Knowledge Gaps

### Gap 1: Identity of the Endogenous DNA Substrate for TREX1

**Scope:** The specific endogenous DNA species that accumulate in TREX1-deficient cells and activate cGAS remain incompletely defined.
**Why it matters:** Knowing the substrate would clarify whether retroelement cDNA, genomic DNA fragments, or mitochondrial DNA is the primary trigger, directly informing whether RTIs could be therapeutic.
**What was checked:** RTI trials and mouse studies were reviewed; results were inconclusive.
**Resolution:** Mass spectrometry-based identification of cytosolic DNA species in TREX1-KO cells, combined with genetic deletion of candidate sources.

### Gap 2: Mechanism of cGAS Activation in RNASEH2 Deficiency

**Scope:** How RNASEH2 loss of function generates cGAS-activating ligands is unclear, given that the primary substrate (embedded ribonucleotides) is in genomic DNA, not the cytosol.
**Why it matters:** Without this link, the IFN component of RNASEH2-related disease is mechanistically under-specified.
**What was checked:** The literature on RNASEH2 → cGAS was reviewed; direct evidence of cytosolic nucleic acid accumulation is sparse.
**Resolution:** Imaging and biochemical characterization of cytosolic DNA in RNASEH2-deficient cells, combined with cGAS activity reporters.

### Gap 3: Why ~27% of RNASEH2B Patients Are IFN-Negative

**Scope:** A substantial fraction of RNASEH2B patients lack the IFN signature that defines the disease.
**Why it matters:** These patients may have fundamentally different disease biology, with implications for treatment selection and trial stratification.
**What was checked:** [PMID: 24183309](https://pubmed.ncbi.nlm.nih.gov/24183309/) documented the phenomenon; longitudinal data were reviewed.
**Resolution:** Longitudinal multi-omic profiling of IFN-positive vs. IFN-negative RNASEH2B patients, with genome-wide modifier gene analysis.

### Gap 4: Modifier Genes Explaining Incomplete Penetrance

**Scope:** Asymptomatic RNASEH2B:p.Ala177Thr homozygotes exist, indicating that genotype is not sufficient for disease.
**Why it matters:** Identifying modifiers could reveal protective mechanisms and therapeutic targets.
**What was checked:** [PMID: 40812004](https://pubmed.ncbi.nlm.nih.gov/40812004/) documented variability; sibling discordance was reviewed ([PMID: 38368708](https://pubmed.ncbi.nlm.nih.gov/38368708/)).
**Resolution:** Whole-genome sequencing of discordant sibling pairs and asymptomatic homozygotes to identify candidate modifier loci.

### Gap 5: CNS Bioavailability of Current Therapeutics

**Scope:** JAK inhibitors show limited neurological benefit, possibly due to poor blood-brain barrier penetration.
**Why it matters:** It is unclear whether the failure is because IFN is not the neurological driver or because drugs don't reach the CNS.
**What was checked:** Post-mortem neuropathology after baricitinib treatment was reviewed ([PMID: 38381212](https://pubmed.ncbi.nlm.nih.gov/38381212/)); enhanced CNS bioavailability was flagged as a need.
**Resolution:** Pharmacokinetic studies of JAK inhibitors in CSF; development of CNS-penetrant IFN pathway inhibitors; comparison of CNS vs. peripheral IFN inhibition.

### Gap 6: SAMHD1's Non-dNTPase Functions in AGS Pathogenesis

**Scope:** SAMHD1 has both dNTPase activity and roles in replication fork processing/DNA repair. Which function drives AGS?
**Why it matters:** The therapeutic approach differs: dNTP modulation vs. genome stability intervention.
**What was checked:** [PMID: 32720483](https://pubmed.ncbi.nlm.nih.gov/32720483/) described fork processing role; [PMID: 41929158](https://pubmed.ncbi.nlm.nih.gov/41929158/) described STING-SAMHD1 axis.
**Resolution:** Separation-of-function SAMHD1 mutants (dNTPase-dead vs. fork-processing-dead) in mouse models.

### Gap 7: No Completed Randomized Controlled Trials for AGS

**Scope:** All therapeutic evidence for JAK inhibitors in AGS comes from retrospective studies, case series, and open-label trials.
**Why it matters:** Without RCTs, the true efficacy of IFN-targeting therapies cannot be established.
**What was checked:** Clinical trial registries and published trial data were reviewed.
**Resolution:** Multi-center, genotype-stratified RCTs with both peripheral (skin, immune) and neurological endpoints.

### Gap 8: Source-Level Absence — No Large-Scale Omics Datasets for AGS

**Scope:** No large transcriptomic, proteomic, or metabolomic datasets from AGS patient tissues (especially brain) are publicly available.
**Why it matters:** Limits computational and systems-biology approaches to understanding pathogenesis.
**What was checked:** Literature search did not identify published multi-omics studies of AGS patient-derived samples.
**Resolution:** Collaborative biobanking efforts with brain organoids or iPSC-derived neural models from genotype-diverse AGS patients.

---

## Discriminating Tests

### Test 1: cGAS-Independent Neuropathology Across All Subtypes

**Design:** Generate conditional cGAS-knockout crossed with each AGS gene model (not just TREX1 and RNASEH2B). Assess neuropathology vs. systemic disease independently.
**Expected result:** If the IFN model is complete, cGAS-KO should rescue all pathology in TREX1/SAMHD1/LSM11 models but not RNASEH2. If neuropathology is partially IFN-independent in other subtypes, cGAS-KO will rescue systemic but not CNS disease.
**Discriminates:** IFN model (complete) vs. dual-pathway model (IFN + DNA damage).

### Test 2: CNS-Penetrant JAK Inhibitor Trial

**Design:** Compare baricitinib (limited CNS penetration) vs. a CNS-penetrant JAK inhibitor in age- and genotype-matched AGS patients. Primary endpoint: neuroimaging and neurodevelopmental scores.
**Expected result:** If CNS IFN drives neuropathology, CNS-penetrant drugs should show neurological benefit. If not, the DNA damage model is favored for neuropathology.
**Stratification:** TREX1, ADAR1 (expected IFN-responsive) vs. RNASEH2B (potentially IFN-independent).

### Test 3: Longitudinal IFN Profiling in RNASEH2B Homozygotes

**Design:** Prospective cohort of all known RNASEH2B:p.Ala177Thr homozygotes (symptomatic and asymptomatic). Serial IFN scoring, whole-genome sequencing, DNA damage markers (γH2AX, p53 targets in blood).
**Expected result:** Asymptomatic individuals may lack both IFN activation and DNA damage, or show DNA damage without IFN — distinguishing modifier effects at different pathway levels.

### Test 4: Retroelement Activity vs. Genomic DNA Fragments in TREX1-KO

**Design:** Cross TREX1-/- mice with LINE-1 transgenic knockouts or use CRISPR to disable L1 retrotransposition. Assess whether disease is rescued.
**Expected result:** If LINE-1 cDNA is the dominant cGAS substrate, blocking retrotransposition should rescue. If genomic DNA fragments are the trigger, it will not.

### Test 5: Cell-Type-Specific IFN Blockade

**Design:** Astrocyte-specific IFNAR knockout crossed with ADAR1-mutant mice. Neuron-specific and microglia-specific knockouts as comparators.
**Expected result:** Given [PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/) showing astrocyte primacy, astrocyte-specific IFNAR-KO should substantially rescue encephalopathy, identifying the critical cellular target for therapy.

---

## Curation Leads

*These are candidate updates for the Disorder Mechanisms Knowledge Base, requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 26223655](https://pubmed.ncbi.nlm.nih.gov/26223655/)** — *Cutting Edge: cGAS Is Required for Lethal Autoimmune Disease in the Trex1-Deficient Mouse Model of Aicardi-Goutières Syndrome.* Snippet: "Trex1 (-/-) mice lacking cGAS are completely protected from lethality, exhibit dramatically reduced tissue inflammation, and fail to develop autoantibodies." **→ Add as SUPPORT, model organism evidence for cGAS-STING arm.**

2. **[PMID: 34655526](https://pubmed.ncbi.nlm.nih.gov/34655526/)** — *Genome instability independent of type I interferon signaling drives neuropathology caused by impaired ribonucleotide excision repair.* Snippet: "Cerebellar defects after RNASEH2B inactivation are rescued by p53 but not cGAS deletion, suggesting that DNA damage signaling, not neuroinflammation, accounts for neuropathology." **→ Add as QUALIFIES, model organism evidence limiting scope of IFN model for RNASEH2 neuropathology.**

3. **[PMID: 41855203](https://pubmed.ncbi.nlm.nih.gov/41855203/)** — *Aberrant multicellular interferon signaling underlies Adar1 mutation-driven Aicardi-Goutières syndrome-like encephalopathy.* Snippet: "Blocking type I IFN signaling fully reversed these abnormalities, which was not achieved by deleting downstream PKR or ZBP1." **→ Add as SUPPORT, model organism evidence confirming IFN centrality in ADAR1-AGS.**

4. **[PMID: 24686847](https://pubmed.ncbi.nlm.nih.gov/24686847/)** — *Gain-of-function mutations in IFIH1 cause a spectrum of human disease phenotypes associated with upregulated type I interferon signaling.* Snippet: "heterozygous mutations in the cytosolic double-stranded RNA receptor gene IFIH1 (also called MDA5) cause a spectrum of neuroimmunological features consistently associated with an enhanced interferon state." **→ Add as SUPPORT, human clinical evidence for sensor gain-of-function arm.**

5. **[PMID: 41871482](https://pubmed.ncbi.nlm.nih.gov/41871482/)** — *Efficacy of JAK1/2 inhibitors in AGS genes-related interferonopathies.* Snippet: "Treatment showed improvement in immunological and dermatological symptoms, while the impact on neurological manifestations was limited and heterogeneous." **→ Add as QUALIFIES, human clinical evidence limiting scope of IFN blockade for CNS disease.**

6. **[PMID: 40812004](https://pubmed.ncbi.nlm.nih.gov/40812004/)** — *Clinical Characterization of RNASEH2B:p.Ala177Thr.* Snippet: "recent finding of asymptomatic homozygous individuals." **→ Add as QUALIFIES, human clinical evidence for incomplete penetrance.**

7. **[PMID: 39254994](https://pubmed.ncbi.nlm.nih.gov/39254994/)** — *cGAS activation in classical dendritic cells causes autoimmunity in TREX1-deficient mice.* **→ Add as SUPPORT, model organism evidence specifying cell type.**

8. **[PMID: 24183309](https://pubmed.ncbi.nlm.nih.gov/24183309/)** — *Assessment of interferon-related biomarkers in Aicardi-Goutières syndrome.* Snippet: "Of the eight patients with a negative interferon score, seven had mutations in RNASEH2B (seven [27%] of all 26 patients with mutations in this gene)." **→ Add as QUALIFIES, human clinical biomarker evidence.**

### Candidate Pathophysiology Nodes/Edges

- **Add edge:** RNASEH2 loss-of-function → p53-dependent neural progenitor apoptosis (IFN-independent)
- **Add edge:** ADAR1 Zα mutation → MDA5-MAVS activation → type I IFN (validated by MDA5-KO rescue)
- **Add edge:** LSM11/RNU7-1 → histone stoichiometry disruption → cGAS-STING
- **Add node:** Astrocyte dysfunction as key cell-type mediator in ADAR1-AGS encephalopathy
- **Add edge:** SAMHD1 loss → replication fork stalling → cytosolic DNA via MRE11/RECQ1
- **Add edge:** cGAS in classical dendritic cells → systemic autoimmunity in TREX1-related AGS

### Candidate Ontology Terms

- **Cell types:** Astrocyte (CL:0000127), Classical dendritic cell (CL:0000990), Neural progenitor cell (CL:0000031)
- **Biological processes:** cGAS-STING signaling pathway (GO:0140896), MDA5-MAVS signaling, A-to-I RNA editing (GO:0006382), Ribonucleotide excision repair, Replication fork processing, p53-mediated apoptosis
- **Disease terms:** Type I interferonopathy (umbrella)

### Candidate Subtype Restrictions

- The hypothesis status should remain **CANONICAL** for TREX1, ADAR1, IFIH1, LSM11/RNU7-1 subtypes where IFN is the dominant driver.
- For **RNASEH2 subtypes**, consider adding a qualification: "IFN-independent DNA damage/genome instability contributes to neuropathology; IFN may not be the sole or primary driver of CNS disease."
- For **SAMHD1**, the dual dNTPase/fork-processing role should be noted as mechanistically unresolved.

### Candidate Knowledge Gaps for KB Discussion

1. **Unresolved:** Identity of endogenous TREX1 substrate (LINE-1 cDNA vs. genomic DNA vs. mitochondrial DNA)
2. **Unresolved:** Mechanism linking RNASEH2 deficiency to cGAS activation (if any direct link exists)
3. **Unresolved:** Modifier genes explaining incomplete RNASEH2B penetrance
4. **Unresolved:** Whether limited JAK inhibitor neurological efficacy reflects poor CNS penetration or IFN-independent pathology
5. **Source absence:** No RCTs completed for AGS; no large-scale multi-omics datasets from AGS brain tissue
6. **Conflicting:** RTI efficacy — mouse data negative ([PMID: 28835460](https://pubmed.ncbi.nlm.nih.gov/28835460/)), clinical data inconclusive ([PMID: 39630935](https://pubmed.ncbi.nlm.nih.gov/39630935/))

---

## Limitations of This Investigation

1. **Literature search scope:** This evaluation relied on PubMed-indexed literature through May 2026. Preprints and non-English literature were not systematically searched.
2. **Mouse model translatability:** Many key findings (cGAS epistasis, STING inhibitor rescue) derive from Trex1-/- mice, which model the most severe AGS subtype. Extrapolation to milder RNASEH2B-related disease requires caution.
3. **Clinical evidence quality:** JAK inhibitor data come from retrospective studies and small case series, not randomized trials. Effect estimates are imprecise.
4. **Genotype coverage:** The mechanistic evidence is deepest for TREX1 and ADAR1 subtypes. SAMHD1, LSM11, and RNU7-1 subtypes are less well characterized mechanistically.
5. **Temporal dynamics:** The hypothesis is framed as a static mechanism, but AGS has a dynamic clinical course with early active phase followed by relative stability. How IFN signaling changes over time is incompletely characterized.

---

*Report generated 2026-05-23. Based on systematic review of 87 papers with 11 confirmed findings across 2 investigation iterations.*
