---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T16:45:22.725212'
end_time: '2026-07-31T17:06:24.678289'
duration_seconds: 1261.95
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Multiple Sclerosis
  category: Neurological Disorder
  hypothesis_group_id: chronic_active_lesion_smouldering_inflammation_pira
  hypothesis_label: Compartmentalized Smouldering Chronic-Active-Lesion Inflammation
    Driving PIRA
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: chronic_active_lesion_smouldering_inflammation_pira\n\
    hypothesis_label: Compartmentalized Smouldering Chronic-Active-Lesion Inflammation\
    \ Driving PIRA\nstatus: EMERGING\ndescription: A CNS-compartmentalized, innate-immune-driven\
    \ mechanism proposes that disability accumulation\n  in progressive MS is driven\
    \ predominantly by progression independent of relapse activity (PIRA) rather\n\
    \  than by acute peripheral-lymphocyte-mediated relapses. At the rim of chronic\
    \ active (\"smouldering\")\n  white-matter lesions \u2014 identifiable in vivo\
    \ as iron-laden paramagnetic-rim lesions on MRI \u2014 a self-sustaining\n  glial\
    \ circuit maintains slow demyelination and axonal loss behind a relatively intact\
    \ blood-brain barrier.\n  Single-nucleus RNA-seq of the lesion edge (Absinta et\
    \ al. 2021) defines disease-specific \"microglia\n  inflamed in MS\" (MIMS) and\
    \ \"astrocytes inflamed in MS\" states with neurodegenerative transcriptional\n\
    \  programming, and implicates complement component 1q (C1q) as a critical upstream\
    \ mediator of MIMS activation.\n  Because this compartment sits behind the BBB,\
    \ it is predicted to be refractory to peripheral B-cell\n  depletion (consistent\
    \ with the modest anti-CD20 effect in primary progressive MS) and to require CNS-penetrant,\n\
    \  microglia/complement-directed strategies. The MIMS profile overlaps microglial\
    \ states in other neurodegenerative\n  diseases, suggesting a shared secondary-neurodegeneration\
    \ mechanism.\nnotes: Elevated from a qualification embedded in the CANONICAL model\
    \ to its own EMERGING hypothesis because\n  it makes distinct, testable predictions\
    \ (BBB-compartmentalized innate/complement drive of PIRA; paramagnetic-rim\n \
    \ lesions as a monitorable biomarker; CNS-penetrant complement/microglia targets)\
    \ and is directly motivated\n  by the single-nucleus dataset added to this entry\
    \ (scea:E-GEOD-180759). Seeded for an OpenScientist\n  hypothesis-search deep-research\
    \ run; findings to be verified and folded back after assessment.\nevidence:\n\
    - reference: PMID:34497421\n  reference_title: A lymphocyte-microglia-astrocyte\
    \ axis in chronic active multiple sclerosis.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: MRI-informed single-nucleus RNA sequencing to profile\
    \ the edge of demyelinated white matter\n    lesions at various stages of inflammation\n\
    \  explanation: Human single-nucleus RNA-seq of the chronic active lesion edge\
    \ is the seed observation\n    for this hypothesis \u2014 it defines the MIMS/inflamed-astrocyte\
    \ states and the C1q-driven smouldering-inflammation\n    circuit predicted to\
    \ drive PIRA."
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
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
- **Hypothesis ID:** chronic_active_lesion_smouldering_inflammation_pira
- **Hypothesis Label:** Compartmentalized Smouldering Chronic-Active-Lesion Inflammation Driving PIRA
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: chronic_active_lesion_smouldering_inflammation_pira
hypothesis_label: Compartmentalized Smouldering Chronic-Active-Lesion Inflammation Driving PIRA
status: EMERGING
description: A CNS-compartmentalized, innate-immune-driven mechanism proposes that disability accumulation
  in progressive MS is driven predominantly by progression independent of relapse activity (PIRA) rather
  than by acute peripheral-lymphocyte-mediated relapses. At the rim of chronic active ("smouldering")
  white-matter lesions — identifiable in vivo as iron-laden paramagnetic-rim lesions on MRI — a self-sustaining
  glial circuit maintains slow demyelination and axonal loss behind a relatively intact blood-brain barrier.
  Single-nucleus RNA-seq of the lesion edge (Absinta et al. 2021) defines disease-specific "microglia
  inflamed in MS" (MIMS) and "astrocytes inflamed in MS" states with neurodegenerative transcriptional
  programming, and implicates complement component 1q (C1q) as a critical upstream mediator of MIMS activation.
  Because this compartment sits behind the BBB, it is predicted to be refractory to peripheral B-cell
  depletion (consistent with the modest anti-CD20 effect in primary progressive MS) and to require CNS-penetrant,
  microglia/complement-directed strategies. The MIMS profile overlaps microglial states in other neurodegenerative
  diseases, suggesting a shared secondary-neurodegeneration mechanism.
notes: Elevated from a qualification embedded in the CANONICAL model to its own EMERGING hypothesis because
  it makes distinct, testable predictions (BBB-compartmentalized innate/complement drive of PIRA; paramagnetic-rim
  lesions as a monitorable biomarker; CNS-penetrant complement/microglia targets) and is directly motivated
  by the single-nucleus dataset added to this entry (scea:E-GEOD-180759). Seeded for an OpenScientist
  hypothesis-search deep-research run; findings to be verified and folded back after assessment.
evidence:
- reference: PMID:34497421
  reference_title: A lymphocyte-microglia-astrocyte axis in chronic active multiple sclerosis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: MRI-informed single-nucleus RNA sequencing to profile the edge of demyelinated white matter
    lesions at various stages of inflammation
  explanation: Human single-nucleus RNA-seq of the chronic active lesion edge is the seed observation
    for this hypothesis — it defines the MIMS/inflamed-astrocyte states and the C1q-driven smouldering-inflammation
    circuit predicted to drive PIRA.
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

# Compartmentalized Smouldering Chronic-Active-Lesion Inflammation Driving PIRA — Hypothesis-Search Report

**Disease:** Multiple Sclerosis (Neurological Disorder)
**Hypothesis ID:** `chronic_active_lesion_smouldering_inflammation_pira`
**KB Status:** EMERGING
**Search date:** 2026-07-31 · 61 papers reviewed · 8 findings confirmed

---

## Summary

The seed hypothesis proposes that disability accumulation in progressive multiple sclerosis (MS) is driven predominantly by **progression independent of relapse activity (PIRA)**, generated by a **CNS-compartmentalized, innate-immune / glial circuit** at the rim of chronic active ("smouldering") white-matter lesions — visible in vivo as iron-laden **paramagnetic-rim lesions (PRLs)**. It further specifies a molecular engine: a **C1q-driven "microglia inflamed in MS" (MIMS)** and "astrocytes inflamed in MS" state, sitting behind a relatively intact blood–brain barrier (BBB) and therefore refractory to peripheral B-cell depletion but responsive to CNS-penetrant, microglia/complement-directed therapy.

**Verdict: PARTIALLY SUPPORTED.** The hypothesis is strongest where it is most testable. Its **clinical/biomarker arm** is well supported: PRLs predict PIRA and confirmed disability progression in a meta-analysis (OR 2.24 and 2.87; [PMID: 41205558](https://pubmed.ncbi.nlm.nih.gov/41205558/)), and a second, independent chronic-active-lesion (CAL) imaging marker — slowly expanding lesions (SELs) — independently predicts PIRA ([PMID: 40897401](https://pubmed.ncbi.nlm.nih.gov/40897401/)). Its **compartmentalization/therapeutic arm** is also well supported by two randomized trials working in opposite directions: peripheral anti-CD20 (rituximab) fails to lower the astrocytic biomarker sGFAP or prevent PIRMA even as it lowers the acute axonal marker sNfL ([PMID: 41968564](https://pubmed.ncbi.nlm.nih.gov/41968564/)), whereas the brain-penetrant BTK inhibitor tolebrutinib produced the first positive phase 3 result in non-relapsing secondary progressive MS (HR 0.69; [PMID: 40202696](https://pubmed.ncbi.nlm.nih.gov/40202696/)).

What remains **unresolved and partly contested** is the specific molecular-causal core. The claim that **C1q is an upstream driver** of the MIMS state rests principally on a single correlational single-nucleus RNA-seq dataset ([PMID: 34497421](https://pubmed.ncbi.nlm.nih.gov/34497421/)) and is directly complicated by a longitudinal primary-progressive MS (PPMS) study in which **elevated CSF C1q was protective**, not harmful ([PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/)). Meanwhile, **grey-matter and spinal-cord atrophy — not white-matter rims alone — are the single strongest predictors of PIRA** ([PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/)), forming a partly competing anatomical substrate. The framework is therefore right about *what kind* of process drives progression (compartmentalized, innate/glial, BBB-shielded) and about *how to monitor and treat it*, but the *precise molecular trigger* (C1q → MIMS) should not be curated as established. Recommendation: retain **EMERGING**, upgrade the biomarker and therapeutic sub-claims toward well-supported, and explicitly flag the C1q-driver mechanism as speculative/contested while adding grey-matter/cord degeneration as a competing substrate.

---

## Key Findings

### F001 — Paramagnetic rim lesions (in vivo chronic active lesions) predict PIRA and confirmed disability progression

The strongest direct support for the biomarker arm comes from a systematic review and meta-analysis of 5 studies and 744 patients ([PMID: 41205558](https://pubmed.ncbi.nlm.nih.gov/41205558/)), which found that *"The presence of PRLs was associated with a higher risk of PIRA (odds ratio [OR] 2.24; 95% confidence interval [CI]: 1.17-4.29; p = 0.01) and CDP (OR 2.87; 95% CI: 1.01-8.1; p = 0.05). In studies with ≤4 years of follow-up, the association with PIRA was stronger (OR 2.84; 95% CI: 1.72-4.68; p < 0.0001)."* This is corroborated by an independent 10-year cohort ([PMID: 38366920](https://pubmed.ncbi.nlm.nih.gov/38366920/)) reporting that *"PRLs are a marker of aggressive ongoing disease inflammatory activity, including more frequent future clinical relapses and greater long-term, relapse-independent disability progression,"* and by an optical-coherence-tomography cohort ([PMID: 39529542](https://pubmed.ncbi.nlm.nih.gov/39529542/)) in which the number of PRLs predicted PIRA (HR 1.24 per PRL) and linked to retinal neurodegeneration. The imaging-to-histology mapping underlying PRLs is itself validated: quantitative susceptibility mapping (QSM) identifies iron-positive rims with 100% positive predictive value against Perls' stain ([PMID: 39916751](https://pubmed.ncbi.nlm.nih.gov/39916751/)). Together these establish PRLs as a specific, prognostic, in vivo readout of chronic active lesions that track relapse-independent progression — exactly as the hypothesis predicts.

### F002 — Brain-penetrant BTK inhibitor tolebrutinib slows disability in non-relapsing SPMS

The phase 3 HERCULES trial ([PMID: 40202696](https://pubmed.ncbi.nlm.nih.gov/40202696/)) randomized 1,131 non-relapsing secondary-progressive MS participants 2:1 and found that *"A smaller percentage of participants in the tolebrutinib group than in the placebo group had confirmed disability progression sustained for at least 6 months (22.6% vs. 30.7%; hazard ratio, 0.69; 95% confidence interval, 0.55 to 0.88; P = 0.003)."* Crucially, the drug's mechanism matches the hypothesis: *"Tolebrutinib is an oral, brain-penetrant Bruton's tyrosine kinase inhibitor that targets myeloid cells (including microglia) and B cells in both the periphery and central nervous system."* This is the first positive trial in a population for which no approved therapies previously existed, and it provides the strongest therapeutic evidence that a CNS-penetrant, microglia-directed strategy can slow PIRA — a direct prediction of the compartmentalization model.

### F003 — Complement activation tracks progression, but the specific C1q-as-driver claim is only partially supported and possibly context-dependent

Complement pathway involvement in MS progression is supported broadly: intrathecal complement activation associates with structural brain damage, with a doubling of CSF C4a linked to −0.24% additional brain volume loss ([PMID: 39752618](https://pubmed.ncbi.nlm.nih.gov/39752618/), n=239), which concludes *"Intrathecal complement activation is consistently associated with MRI metrics and liquid biomarkers indicative for MS disease activity and progression."* However, the **specific claim that C1q is an upstream driver is contradicted in PPMS**. A longitudinal study (mean 9.6-year follow-up, n=68; [PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/)) found that *"Proteins involved in the activation of early complement cascades play a role in disability progression as risk (elevated serum C3a/C3 ratio) or protective (elevated CSF C1q) factors after 6 or more years of follow-up in patients with PPMS."* Elevated CSF C1q being **protective** directly complicates the C1q-as-driver edge. Additional CSF complement dysregulation is documented (sCR2 elevated and correlated with C1q, C3, and severity; [PMID: 27085202](https://pubmed.ncbi.nlm.nih.gov/27085202/)), but this establishes involvement, not directionality. The molecular core of the hypothesis is thus the weakest link.

### F004 — Slowly expanding lesions, a second CAL imaging marker, independently predict PIRA

A prospective diffusion-MRI cohort (n=130, median 9.2-year clinical follow-up; 29 [22%] developed PIRA; [PMID: 40897401](https://pubmed.ncbi.nlm.nih.gov/40897401/)) found that definite SELs showed progressive fractional-anisotropy (FA) decline in lesion core and perilesional tissue, and that *"Longitudinal core FA reductions within definite SELs were associated with worse MSFC z-score evolution (β=0.03, 95% CI 0.01 to 0.05, p=0.003), higher odds for PIRA"* (p=0.001). Because SELs are a mechanistically distinct imaging measure from PRLs, this convergence strengthens the general claim that chronic active lesions — however visualized — drive PIRA. It also connects to congress-level synthesis reporting memory astrocytes (CLEC16A) in chronic active lesions and grey-matter atrophy associated with PIRA ([PMID: 41609134](https://pubmed.ncbi.nlm.nih.gov/41609134/)).

### F005 — CALs are largely refractory to current DMTs; EBV is an upstream initiator, not the PIRA driver

A review of DMT effects on CALs ([PMID: 41961242](https://pubmed.ncbi.nlm.nih.gov/41961242/)) concludes that *"current evidence suggests that available DMTs have a limited and inconsistent effect on CAL occurrence and evolution over short- to medium-term follow-up,"* consistent with a BBB-shielded compartment. A QSM cohort found no significant change in PRL number after anti-CD20 treatment ([PMID: 40131429](https://pubmed.ncbi.nlm.nih.gov/40131429/)). Separately, the search clarified the causal geography of the disease: EBV is an upstream *initiator*, not the compartmentalized progression driver. In a cohort of >10 million adults ([PMID: 35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/)), *"Risk of MS increased 32-fold after infection with EBV but was not increased after infection with other viruses... Serum levels of neurofilament light chain, a biomarker of neuroaxonal degeneration, increased only after EBV seroconversion."* This positions EBV before disease onset, distinct from the smouldering-progression mechanism the hypothesis addresses.

### F006 — Anti-CD20 fails to reduce astrocytic sGFAP or PIRMA, while lowering acute sNfL — a therapeutic dissociation supporting compartmentalization

The RIFUND-MS randomized controlled trial (n=197 RRMS; [PMID: 41968564](https://pubmed.ncbi.nlm.nih.gov/41968564/)) provides the cleanest test of the BBB-shielding prediction. Both rituximab and dimethyl fumarate lowered sNfL (~47–51%), but the astrocytic/chronic-process marker sGFAP diverged: *"sGFAP remained stable in RTX (3.6% decrease; CI -7.8%-13.8%, p = 0.81) but decreased with DMF (18.4%; CI 8.5%-27.2%; p < 0.001)."* Furthermore, *"The risk of progression independent of relapse and MRI activity (PIRMA) was higher with RTX (HR 3.3, CI 1.1-10, p = 0.04)."* Peripheral B-cell depletion thus reduced the acute axonal-injury marker but neither the astrocytic marker nor relapse-independent progression — precisely the dissociation expected if the driving pathology sits behind the BBB. sGFAP independently predicts PIRA and progressive phenotype ([PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/), [PMID: 42127333](https://pubmed.ncbi.nlm.nih.gov/42127333/)).

### F007 — Spinal-cord and grey-matter degeneration are the strongest PIRA predictors — a partly competing substrate

Machine-learning feature selection across two independent cohorts (n=120 and n=279; [PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/)) found that *"Spinal cord atrophy consistently emerged as the strongest predictor of disability severity and predicted PIRA, along with cortical thinning and subcortical atrophy - particularly in deep gray matter."* sNfL, sGFAP, and quantitative-MRI metrics added independent value. Congress synthesis concurs: grey-matter atrophy is associated with PIRA and cervical cord atrophy predicts progressive-form prognosis ([PMID: 41609134](https://pubmed.ncbi.nlm.nih.gov/41609134/)). This is the most important qualification to the hypothesis: white-matter rim lesions are *a* driver, but grey-matter and cord degeneration may drive PIRA at least as strongly and partly independently.

### F008 — A CSF disease-associated macrophage signature defines progressive MS and shares degenerative features with Alzheimer's

Independent (non-lesion) support for the innate-myeloid and shared-neurodegeneration arms comes from a CSF study ([PMID: 42129775](https://pubmed.ncbi.nlm.nih.gov/42129775/)) combining flow cytometry (RRMS n=169, progressive MS n=56, non-inflammatory controls n=74) with prospective CSF single-cell transcriptomics (35 individuals) and age-matched Alzheimer's CSF single-cell data. The authors report: *"We thus identified MS stage-specific CSF signatures and shared cellular features of degeneration detectable in CSF of PMS patients."* This corroborates a disease-associated myeloid/degenerative signature in progressive MS and its overlap with neurodegenerative features seen in other diseases — supporting the hypothesis's "shared secondary-neurodegeneration" prediction — though it is measured in CSF rather than at the lesion rim, so it does not independently replicate the MIMS lesion-edge state.

---

## Mechanistic Model / Interpretation

The findings assemble into the following causal chain. Annotations mark where the literature is strong, inferred, or contested.

```
[EBV infection]  ──(upstream initiator; NOT the progression driver)──►  [MS onset]
      │  STRONG: 32-fold risk; NfL rises only post-seroconversion (PMID 35025605)
      ▼
[Focal WM lesion forms] ──► [Subset fails to resolve → CHRONIC ACTIVE LESION]
                                    │
             iron-laden microglia/macrophages accumulate at the RIM
                                    │  STRONG imaging↔histology: QSM PPV 100% (PMID 39916751)
                                    ▼
        ┌───────────────  in vivo readouts (STRONG)  ───────────────┐
        │  PRLs (paramagnetic-rim)        SELs (slowly expanding)    │
        │  PMID 41205558, 38366920        PMID 40897401              │
        └──────────────────────┬─────────────────────────────────────┘
                               │
      ??? SPECULATIVE / CONTESTED MOLECULAR CORE ???
  [C1q]──►[MIMS microglia]──►[inflamed astrocytes]──►[slow demyelination + axonal loss]
    │          │                        │
 CONTESTED   correlational only       supported broadly by innate-myeloid
 (CSF C1q     (single snRNA-seq,       CSF signature (PMID 42129775)
 PROTECTIVE   PMID 34497421)
 in PPMS,
 PMID 38912898)
                               │
                               ▼
   Behind relatively intact BBB → refractory to peripheral anti-CD20
   (sGFAP/PIRMA unchanged by RTX, PMID 41968564; CALs resist DMTs, PMID 41961242)
   but responsive to CNS-penetrant BTKi (tolebrutinib HR 0.69, PMID 40202696)
                               │
                               ▼
                     [PIRA / disability accumulation]
   COMPETING SUBSTRATE (STRONG): grey-matter + spinal-cord atrophy (PMID 41527428)
   are the single strongest independent PIRA predictors
```

**Where the literature is strong.** The upstream initiator (EBV), the imaging↔histology mapping (iron rim = chronic active lesion), the PRL/SEL→PIRA association, the refractoriness of CALs to peripheral therapy, and the responsiveness of progression to a CNS-penetrant microglia-targeting drug are each backed by convergent human data, including two randomized trials.

**Where the links are inferred.** The step `C1q → MIMS activation → demyelination/axonal loss` is inferred from a single correlational snRNA-seq experiment. No surfaced study shows that perturbing C1q at the lesion rim changes the MIMS state or slows progression. The "shared secondary-neurodegeneration" claim is plausible at the transcriptional/CSF level but is not proven mechanistic identity.

**Missing causal steps.** (i) A quantified link from rim microglial iron/MIMS activation to a *rate* of axonal loss; (ii) proof that C1q is upstream rather than a bystander or protective; (iii) demonstration that the tolebrutinib benefit is *mediated by* rim/microglial modulation rather than meningeal-B-cell or peripheral effects (no PRL-mediation analysis available).

---

## Evidence Base (Evidence Matrix)

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 41205558](https://pubmed.ncbi.nlm.nih.gov/41205558/) | Human clinical (meta-analysis, 5 studies, 744 pts) | **Supports** | PRLs predict PIRA/CDP | PIRA OR 2.24 (1.17–4.29); CDP OR 2.87 (1.01–8.1); stronger ≤4y | Mixed MS | High for association; heterogeneous, observational |
| [PMID: 38366920](https://pubmed.ncbi.nlm.nih.gov/38366920/) | Human clinical (10-y cohort) | **Supports** | PRLs mark relapse-independent progression | PRL+ → more relapses & greater long-term relapse-independent EDSS progression | Mixed MS | Moderate-high; single cohort |
| [PMID: 39529542](https://pubmed.ncbi.nlm.nih.gov/39529542/) | Human clinical (OCT, n=97) | **Supports** | PRLs → retinal degeneration + PIRA | PRL number → PIRA HR 1.24/PRL | Early RRMS | Moderate; small, single-center |
| [PMID: 39916751](https://pubmed.ncbi.nlm.nih.gov/39916751/) | Human (post-mortem imaging↔histology) | **Supports** | QSM rim = iron-positive rim | QSM PPV 100% vs Perls' stain | Post-mortem MS | High; validates imaging biomarker |
| [PMID: 40897401](https://pubmed.ncbi.nlm.nih.gov/40897401/) | Human clinical (diffusion-MRI, n=130, 9.2y) | **Supports** | SELs (2nd CAL marker) predict PIRA | Core FA decline → worse MSFC (β=0.03), higher PIRA odds | Mixed MS | Moderate-high; independent CAL marker |
| [PMID: 40202696](https://pubmed.ncbi.nlm.nih.gov/40202696/) | Human clinical (phase 3 RCT, n=1131) | **Supports** | CNS-penetrant microglia/myeloid targeting slows PIRA | 6-mo CDP 22.6% vs 30.7%; HR 0.69 (0.55–0.88) | Non-relapsing SPMS | High; first positive trial in population |
| [PMID: 41968564](https://pubmed.ncbi.nlm.nih.gov/41968564/) | Human clinical (RCT, n=197) | **Supports** | Peripheral anti-CD20 spares glial process | sGFAP unchanged by RTX (p=0.81) vs DMF; PIRMA higher with RTX (HR 3.3) | RRMS | High; key compartmentalization dissociation |
| [PMID: 41961242](https://pubmed.ncbi.nlm.nih.gov/41961242/) | Review (DMT effects on CALs) | **Supports (review)** | CALs resist current DMTs | "Limited and inconsistent effect" of DMTs on CALs | Mixed MS | Review-level orientation |
| [PMID: 40131429](https://pubmed.ncbi.nlm.nih.gov/40131429/) | Human clinical (QSM, n=39) | **Qualifies/Supports** | Anti-CD20 doesn't resolve PRLs | No significant PRL number change after anti-CD20 | RRMS/PPMS | Small; supports refractoriness |
| [PMID: 42129775](https://pubmed.ncbi.nlm.nih.gov/42129775/) | Human clinical (CSF flow + scRNA-seq) | **Supports** | Innate-myeloid/degenerative signature defines PMS; AD overlap | CSF disease-associated macrophage signature; shared degeneration with AD | RRMS vs PMS | Moderate-high; CSF not lesion |
| [PMID: 34497421](https://pubmed.ncbi.nlm.nih.gov/34497421/) | Human snRNA-seq (lesion edge) — **seed** | **Supports (seed)** | C1q → MIMS/inflamed-astrocyte circuit | Defines MIMS and inflamed-astrocyte states; implicates C1q upstream | Chronic active lesions | Foundational but correlational; single dataset |
| [PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/) | Human clinical (PPMS, n=68, 9.6y) | **Refutes/Qualifies** | CSF C1q drives progression | Serum C3a/C3 → risk (OR 2.30); **CSF C1q PROTECTIVE** | PPMS | Moderate; contradicts C1q-driver in PPMS |
| [PMID: 39752618](https://pubmed.ncbi.nlm.nih.gov/39752618/) | Human clinical (CSF, n=239) | **Supports (pathway)** | Intrathecal complement tracks progression | C4a doubling → −0.24% extra brain-volume loss | Mixed MS | Moderate; not C1q-specific |
| [PMID: 27085202](https://pubmed.ncbi.nlm.nih.gov/27085202/) | Human clinical (CSF) | **Qualifies** | Complement dysregulation in MS CSF | sCR2 elevated; correlates with C1q, C3, severity | RRMS/SPMS | Moderate; mechanism ambiguous |
| [PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/) | Human clinical (ML, n=120/279) | **Competing** | Anatomical substrate of PIRA | Spinal cord atrophy strongest PIRA predictor; cortical/deep-GM add | Mixed MS | High; competing substrate |
| [PMID: 41609134](https://pubmed.ncbi.nlm.nih.gov/41609134/) | Review/congress synthesis | **Competing/Qualifies** | GM/cord atrophy; memory astrocytes | GM atrophy → PIRA; cord atrophy predicts progressive prognosis; CLEC16A memory astrocytes in CALs | Mixed MS | Review-level |
| [PMID: 35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/) | Human clinical (>10M cohort) | **Qualifies (upstream)** | EBV as MS cause | 32-fold MS risk post-EBV; NfL rises only post-seroconversion | MS onset | High; EBV is initiator, not progression driver |

---

## Limitations and Knowledge Gaps

**Gap 1 — C1q causal directionality is unconfirmed and possibly reversed.** *Scope:* the molecular core. *Why it matters:* C1q is the named mechanistic/therapeutic target; if it is protective in some compartments the drug-development rationale changes. *What was checked:* complement literature — the seed snRNA-seq ([PMID: 34497421](https://pubmed.ncbi.nlm.nih.gov/34497421/)) implicates C1q upstream, but longitudinal PPMS data found CSF C1q **protective** ([PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/)), while intrathecal complement broadly tracks damage ([PMID: 39752618](https://pubmed.ncbi.nlm.nih.gov/39752618/)). *Resolution:* compartment-resolved (rim vs CSF vs serum) C1q measurement with functional C1q perturbation in a MIMS-reproducing model.

**Gap 2 — No independent replication of the MIMS lesion-edge state with perturbation.** *Scope:* reproducibility of the seed observation. *Why it matters:* curation should not elevate a mechanism resting on one dataset. *What was checked:* snRNA-seq / CSF single-cell MS literature; closest independent support is a CSF (not lesion) disease-associated macrophage signature ([PMID: 42129775](https://pubmed.ncbi.nlm.nih.gov/42129775/)) and cortical snRNA-seq showing glial activation at plaque rims ([PMID: 31316211](https://pubmed.ncbi.nlm.nih.gov/31316211/)); neither independently defines MIMS with a C1q edge. *Resolution:* multi-center lesion-edge snRNA-seq with harmonized annotation and spatial validation.

**Gap 3 — Competing anatomical substrate not reconciled.** *Scope:* what structure actually drives PIRA. *Why it matters:* if cord/GM atrophy dominates, WM rims may be a correlated marker rather than the principal driver. *What was checked:* ML predictor studies — cord atrophy is the strongest PIRA predictor across two cohorts ([PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/)); congress synthesis concurs ([PMID: 41609134](https://pubmed.ncbi.nlm.nih.gov/41609134/)). *Resolution:* joint longitudinal modeling with formal variance partitioning of PRL burden vs cord vs GM atrophy.

**Gap 4 — Mechanism of the tolebrutinib benefit is not proven to be rim/microglial.** *Scope:* whether the therapeutic arm actually validates the hypothesized target. *Why it matters:* a positive trial supports "CNS-penetrant works" but not specifically "rim-microglial modulation works." *What was checked:* HERCULES report ([PMID: 40202696](https://pubmed.ncbi.nlm.nih.gov/40202696/)) and BTKi reviews ([PMID: 42352643](https://pubmed.ncbi.nlm.nih.gov/42352643/)) — no PRL-mediation analysis surfaced. *Resolution:* PRL/SEL burden as a pre-specified mediator endpoint in BTKi trials.

**Gap 5 — Source/data absences.** No GenCC/ClinGen gene–disease evidence bears on this *mechanistic-progression* hypothesis (expected — MS is a complex trait). Critically, **no dedicated randomized trial of a complement/C1q-directed agent in progressive MS was found as of the search date** — the direct test of the hypothesis's named target does not yet exist. The seed omics dataset (scea:E-GEOD-180759 / [PMID: 34497421](https://pubmed.ncbi.nlm.nih.gov/34497421/)) remains the sole lesion-edge single-nucleus source for this edge.

**Search-level limitations.** The MIMS/C1q core was assessed from abstract-level reading; full-text spatial and functional data were not re-analyzed. Several supporting items are single-cohort or small (QSM n=39, OCT n=97). Review/congress syntheses are used for orientation and clearly labeled as review-level.

---

## Alternative / Competing Models

| Model | Relationship to seed | Summary & support |
|---|---|---|
| **Grey-matter + spinal-cord neurodegeneration** | **Competing / parallel substrate** | Cord and deep-GM atrophy are the strongest PIRA predictors ([PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/), [PMID: 41609134](https://pubmed.ncbi.nlm.nih.gov/41609134/)); may drive PIRA partly independently of WM rims. |
| **Meningeal inflammation / ectopic lymphoid follicles → cortical degeneration** | **Parallel / partly upstream** | ELFs in ~40% of progressive MS meninges correlate with cortical degeneration and clinical progression ([PMID: 34293193](https://pubmed.ncbi.nlm.nih.gov/34293193/)); surface-in cortical neuron loss under meningeal inflammation ([PMID: 31316211](https://pubmed.ncbi.nlm.nih.gov/31316211/)). |
| **Hypoxia–inflammation ("virtual hypoxia") cycle** | **Upstream/parallel engine** | HIF-driven bioenergetic failure sustains and compartmentalizes smouldering inflammation ([PMID: 42047854](https://pubmed.ncbi.nlm.nih.gov/42047854/)); could feed rim glia metabolically. |
| **EBV-initiated autoimmunity** | **Upstream cause, distinct from progression** | Near-necessary initiator ([PMID: 35025605](https://pubmed.ncbi.nlm.nih.gov/35025605/)); not the compartmentalized progression driver. |
| **Inflammaging / immunosenescence** | **Parallel age-dependent amplifier** | Aging shifts MS toward compartmentalized neuroinflammation and PIRA ([PMID: 42367807](https://pubmed.ncbi.nlm.nih.gov/42367807/)); explains post-midlife progression despite relapse suppression. |
| **Residual peripheral B-cell/adaptive drive** | **Alternative to strict BBB-shielding** | Ocrelizumab reduced 12-week composite CDP in a broad PPMS population (HR 0.70; ORATORIO-HAND, [PMID: 42208561](https://pubmed.ncbi.nlm.nih.gov/42208561/)); higher exposure → less progression ([PMID: 36792367](https://pubmed.ncbi.nlm.nih.gov/36792367/)) — arguing some progression remains peripherally accessible. |

The seed hypothesis is best viewed as **one node in an interacting "asynchronous neuroinflammatory system"** ([PMID: 42445199](https://pubmed.ncbi.nlm.nih.gov/42445199/), [PMID: 41934147](https://pubmed.ncbi.nlm.nih.gov/41934147/)) rather than the sole explanation for PIRA.

---

## Proposed Follow-up Experiments / Discriminating Tests

1. **PRL-mediation analysis inside a BTKi trial (seed vs therapeutic-nonspecificity).** *Stratify:* non-relapsing SPMS/PPMS by baseline PRL/SEL burden. *Biomarkers:* longitudinal PRL count / rim QSM intensity, sGFAP, sNfL. *Perturbation:* tolebrutinib vs placebo. *Expected if hypothesis true:* disability benefit statistically mediated by reduced PRL expansion and sGFAP, not sNfL alone.

2. **Complement/C1q-directed CNS-penetrant agent trial (direct test of the molecular core).** *Stratify:* PRL-high progressive MS. *Perturbation:* C1q or classical-pathway inhibitor with CNS exposure. *Expected if hypothesis true:* slowed rim expansion + PIRA. *Expected if C1q protective (per [PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/)):* no benefit or harm — cleanly resolves Gap 1.

3. **Competing-substrate variance partitioning.** *Sample:* single longitudinal cohort with brain + cord MRI, PRL/SEL quantification, sGFAP/sNfL. *Analysis:* joint model of PIRA on cord atrophy vs GM atrophy vs PRL burden. *Expected:* if seed is dominant, PRL burden retains a large independent effect after adjustment.

4. **Independent multi-center lesion-edge snRNA-seq + spatial transcriptomics with C1q perturbation** in an ex vivo / organoid / humanized-microglia model — resolves Gaps 1 & 2 by testing whether C1q is *necessary* for the MIMS state.

5. **Anti-CD20 vs BTKi head-to-head on astrocytic/microglial biomarkers and PRLs** — extends the RIFUND-MS dissociation ([PMID: 41968564](https://pubmed.ncbi.nlm.nih.gov/41968564/)) to directly contrast peripheral vs CNS-penetrant mechanisms on compartmentalized readouts.

---

## Curation Leads (require curator verification)

**Candidate evidence references & exact snippets to verify:**

- **Upgrade biomarker arm.** [PMID: 41205558](https://pubmed.ncbi.nlm.nih.gov/41205558/) — *"The presence of PRLs was associated with a higher risk of PIRA (odds ratio [OR] 2.24; 95 % confidence interval [CI]: 1.17-4.29; p = 0.01) and CDP (OR 2.87; 95 % CI: 1.01-8.1; p = 0.05)."* Stance: SUPPORT (HUMAN_CLINICAL, meta-analysis).
- **Add SEL corroboration.** [PMID: 40897401](https://pubmed.ncbi.nlm.nih.gov/40897401/) — *"Longitudinal core FA reductions within definite SELs were associated with worse MSFC z-score evolution (β=0.03, 95% CI 0.01 to 0.05, p=0.003), higher odds for PIRA."* Stance: SUPPORT.
- **Add therapeutic arm.** [PMID: 40202696](https://pubmed.ncbi.nlm.nih.gov/40202696/) — *"...22.6% vs. 30.7%; hazard ratio, 0.69; 95% confidence interval, 0.55 to 0.88; P = 0.003."* Stance: SUPPORT (phase 3).
- **Add compartmentalization dissociation.** [PMID: 41968564](https://pubmed.ncbi.nlm.nih.gov/41968564/) — *"sGFAP remained stable in RTX (3.6% decrease... p = 0.81)..."* and *"The risk of progression independent of relapse and MRI activity (PIRMA) was higher with RTX (HR 3.3..."* Stance: SUPPORT.
- **Flag C1q-driver as contested — add refuting evidence.** [PMID: 38912898](https://pubmed.ncbi.nlm.nih.gov/38912898/) — *"...as risk (elevated serum C3a/C3 ratio) or protective (elevated CSF C1q) factors after 6 or more years of follow-up in patients with PPMS."* Stance: REFUTE/QUALIFY for the C1q-as-driver edge.
- **Add competing substrate.** [PMID: 41527428](https://pubmed.ncbi.nlm.nih.gov/41527428/) — *"Spinal cord atrophy consistently emerged as the strongest predictor of disability severity and predicted PIRA..."* Stance: COMPETING.
- **Add independent innate-myeloid support.** [PMID: 42129775](https://pubmed.ncbi.nlm.nih.gov/42129775/) — *"We thus identified MS stage-specific CSF signatures and shared cellular features of degeneration detectable in CSF of PMS patients."* Stance: SUPPORT (non-lesion).

**Candidate pathophysiology nodes/edges:**
- Node *chronic active lesion (PRL/SEL)* → edge → *PIRA*: **upgrade toward well-supported.**
- Edge *C1q → MIMS activation*: **mark speculative/contested; add `knowledge_gap`.**
- Node *spinal-cord / deep-grey-matter atrophy* → edge → *PIRA*: **add as competing substrate.**
- Node *CNS-penetrant BTK inhibition (tolebrutinib)* → edge → *slows PIRA*: **add therapeutic edge.**

**Candidate ontology terms:** microglia (CL:0000129); disease-associated microglia / "MIMS" (candidate cell-state term, no stable CL ID); astrocyte (CL:0000127); complement component C1q; classical complement activation (GO:0006958); microglial cell activation (GO:0001774); demyelination. Tissue: white-matter lesion rim; cerebrospinal fluid macrophage.

**Candidate subtype restrictions / status changes:** Keep group status **EMERGING.** Biomarker/therapeutic sub-claims apply most strongly to **non-relapsing SPMS and PPMS with high PRL/SEL burden**; the C1q-driver sub-claim should carry a **PPMS caveat** (protective CSF C1q signal).

**Candidate `knowledge_gaps` / discussion prompts:** (a) "Is C1q an upstream driver or a protective bystander at the lesion rim vs in CSF?"; (b) "No direct C1q/complement-directed trial in progressive MS as of 2026-07-31"; (c) "Is the tolebrutinib benefit mediated by rim/microglial modulation (PRL-mediation analysis absent)?"; (d) "Does PRL burden retain independent PIRA prediction after adjustment for cord/grey-matter atrophy?"

---

## Conclusion

The seed hypothesis correctly identifies **compartmentalized, innate/glial, BBB-shielded chronic-active-lesion biology as a genuine driver of PIRA**, and its two most actionable predictions — PRLs/SELs as monitorable biomarkers and CNS-penetrant microglia-directed therapy as effective — are now backed by meta-analytic and randomized-trial evidence. What remains speculative is the **specific molecular engine**: the C1q → MIMS causal edge is correlational, unreplicated with perturbation, and directly contradicted by protective CSF-C1q data in PPMS. Grey-matter and spinal-cord degeneration stand as a co-equal or competing anatomical substrate for PIRA. The hypothesis should therefore remain **EMERGING**, with its biomarker/therapeutic arms elevated toward well-supported and its molecular-causal core explicitly flagged as contested pending direct complement-perturbation and independent lesion-edge replication.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)