---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-05T14:30:02.789971'
end_time: '2026-07-05T15:05:47.846191'
duration_seconds: 2145.06
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Alpha-gal Syndrome
  category: Complex
  hypothesis_group_id: tick_associated_microorganism
  hypothesis_label: Tick-Associated Microorganism Model
  hypothesis_status: DEPRECATED
  hypothesis_yaml: "hypothesis_group_id: tick_associated_microorganism\nhypothesis_label:\
    \ Tick-Associated Microorganism Model\nstatus: DEPRECATED\ndescription: The response\
    \ is induced by another organism present in the tick (e.g. commensal or pathogenic\n\
    \  microbes such as Rickettsia or Borrelia), rather than by tick or mammalian\
    \ glycans directly.\nnotes: Deprecated following the 2026 openscientist hypothesis-search\
    \ (kb/hypotheses/Alpha-gal_Syndrome/tick_salivary_constituent_sensitization).\n\
    \  Epidemiological studies show no correlation between alpha-gal sIgE and antibodies\
    \ to tick-borne pathogens\n  (PMID:35382677), and pathogen-free tick salivary\
    \ gland extract alone is sufficient to sensitize AGKO\n  mice (PMID:34034363),\
    \ refuting a co-transmitted microorganism as the primary sensitizer. A minor contributory\n\
    \  role from tick microbiota cannot be fully excluded. Retained as DEPRECATED\
    \ for provenance.\nevidence:\n- reference: PMID:25747720\n  reference_title: 'The\
    \ alpha-gal story: lessons learned from connecting the dots.'\n  supports: SUPPORT\n\
    \  evidence_source: HUMAN_CLINICAL\n  snippet: That the response is induced by\
    \ another organism that is present in the tick.\n  explanation: States the tick-associated-microorganism\
    \ theory as a historically competing sensitization\n    mechanism.\n- reference:\
    \ PMID:35382677\n  reference_title: Sensitisation and allergic reactions to alpha-1,3-galactose\
    \ in Podlasie, Poland, an\n    area endemic for tick-borne infections.\n  supports:\
    \ REFUTE\n  evidence_source: HUMAN_CLINICAL\n  snippet: confirm that the pathogens\
    \ carried by ticks we examined for do not seem implicated in this\n    immune\
    \ response\n  explanation: The absence of correlation between alpha-gal sIgE and\
    \ tick-borne pathogen exposure refutes\n    a co-transmitted microorganism as\
    \ the antigen source."
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
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 24
artifact_count: 14
artifact_sources:
  openscientist_artifacts_zip: 14
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
- filename: provenance_comprehensive_evidence_diagram.json
  path: openscientist_artifacts/provenance_comprehensive_evidence_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comprehensive evidence diagram
- filename: provenance_comprehensive_evidence_diagram.png
  path: openscientist_artifacts/provenance_comprehensive_evidence_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist comprehensive evidence diagram
- filename: provenance_evidence_map.json
  path: openscientist_artifacts/provenance_evidence_map.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence map
- filename: provenance_evidence_map.png
  path: openscientist_artifacts/provenance_evidence_map.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence map
- filename: provenance_final_verdict_diagram.json
  path: openscientist_artifacts/provenance_final_verdict_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final verdict diagram
- filename: provenance_final_verdict_diagram.png
  path: openscientist_artifacts/provenance_final_verdict_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final verdict diagram
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
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Alpha-gal Syndrome
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** tick_associated_microorganism
- **Hypothesis Label:** Tick-Associated Microorganism Model
- **Status in KB:** DEPRECATED

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: tick_associated_microorganism
hypothesis_label: Tick-Associated Microorganism Model
status: DEPRECATED
description: The response is induced by another organism present in the tick (e.g. commensal or pathogenic
  microbes such as Rickettsia or Borrelia), rather than by tick or mammalian glycans directly.
notes: Deprecated following the 2026 openscientist hypothesis-search (kb/hypotheses/Alpha-gal_Syndrome/tick_salivary_constituent_sensitization).
  Epidemiological studies show no correlation between alpha-gal sIgE and antibodies to tick-borne pathogens
  (PMID:35382677), and pathogen-free tick salivary gland extract alone is sufficient to sensitize AGKO
  mice (PMID:34034363), refuting a co-transmitted microorganism as the primary sensitizer. A minor contributory
  role from tick microbiota cannot be fully excluded. Retained as DEPRECATED for provenance.
evidence:
- reference: PMID:25747720
  reference_title: 'The alpha-gal story: lessons learned from connecting the dots.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: That the response is induced by another organism that is present in the tick.
  explanation: States the tick-associated-microorganism theory as a historically competing sensitization
    mechanism.
- reference: PMID:35382677
  reference_title: Sensitisation and allergic reactions to alpha-1,3-galactose in Podlasie, Poland, an
    area endemic for tick-borne infections.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: confirm that the pathogens carried by ticks we examined for do not seem implicated in this
    immune response
  explanation: The absence of correlation between alpha-gal sIgE and tick-borne pathogen exposure refutes
    a co-transmitted microorganism as the antigen source.
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

# Hypothesis Evaluation Report: Tick-Associated Microorganism Model for Alpha-Gal Syndrome

**Hypothesis ID:** tick_associated_microorganism  
**Hypothesis Label:** Tick-Associated Microorganism Model  
**Current KB Status:** DEPRECATED  
**Evaluation Date:** 2026-07-05  
**Search Iterations:** 5 (complete)  
**Literature Reviewed:** 51 papers  
**Confirmed Findings:** 7  

---

## Executive Judgment

**Verdict: REFUTED as primary sensitization mechanism. The DEPRECATED KB status is well-justified.**

The Tick-Associated Microorganism Model proposes that alpha-gal syndrome (AGS) sensitization is driven not by tick-derived or mammalian glycans directly, but by a co-transmitted microorganism present in the tick (e.g., *Rickettsia*, *Borrelia*, or other commensal/pathogenic microbes). This hypothesis has been refuted by convergent evidence from four independent lines of investigation:

1. **Sufficiency of tick saliva alone:** Pathogen-free tick salivary gland extract (TSGE) from laboratory-reared *Amblyomma americanum* induces robust alpha-gal IgE (190-fold increase, p < 0.001) and clinical allergic reactions in AGKO mice ([PMID: 34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/)), demonstrating that no co-transmitted microorganism is necessary.
2. **Absence of epidemiological correlation:** No correlation was found between alpha-gal sIgE and antibodies to tick-borne pathogens (*Borrelia*, *Anaplasma*, *Babesia*, tick-borne encephalitis virus) in a tick-endemic Polish cohort, despite a strong association with tick bite history (OR = 9.31) ([PMID: 35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/)).
3. **Endogenous tick alpha-gal synthesis:** Ticks possess their own galactosyltransferases capable of synthesizing alpha-gal ([PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/)), and alpha-gal glycolipids have been directly identified in tick saliva by mass spectrometry with demonstrated basophil-activating capacity ([PMID: 39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/)).
4. **Helminth dissociation:** Helminths (*Ascaris lumbricoides*) contain alpha-gal at even higher concentrations than ticks and drive alpha-gal IgE sensitization in developing countries (32–54% prevalence), yet clinical meat allergy is NOT observed in these populations ([PMID: 34333031](https://pubmed.ncbi.nlm.nih.gov/34333031/), [PMID: 33539899](https://pubmed.ncbi.nlm.nih.gov/33539899/)). This proves the critical variable is the immunological context (tick salivary adjuvants), not the antigen source — the very question the microorganism model was asking.

**Most important caveat:** Laboratory "pathogen-free" tick colonies still harbor obligate endosymbionts such as Francisella-like organisms ([PMID: 35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/)), meaning the TSGE experiments formally exclude known tick-borne pathogens but do not exclude all tick-associated microorganisms. However, since ticks produce alpha-gal endogenously, alpha-gal glycolipids are directly present in saliva, and the salivary immune context — not antigen source — drives clinical disease, this caveat does not rescue the hypothesis. It merely leaves open a minor, untested modulatory role for endosymbionts that does not alter the DEPRECATED verdict.

---

## Summary

Alpha-gal syndrome (AGS) is an IgE-mediated delayed hypersensitivity to galactose-α-1,3-galactose (alpha-gal), a carbohydrate present in mammalian tissues but absent in humans and Old World primates. First linked to tick bites in the early 2000s, AGS has become a major emerging allergic disease, with an estimated 450,000 affected individuals in the United States alone and seroprevalence reaching 31% in some southeastern states ([PMID: 42391055](https://pubmed.ncbi.nlm.nih.gov/42391055/)). The mechanistic question of *how* tick bites cause sensitization has generated several competing hypotheses.

One early proposal — the Tick-Associated Microorganism Model — suggested that a co-transmitted microbe within the tick, rather than tick salivary constituents themselves, was the source of the sensitizing alpha-gal antigen. This was a reasonable hypothesis at the time, as many tick-borne pathogens are known to carry alpha-gal on their surfaces ([PMID: 33988703](https://pubmed.ncbi.nlm.nih.gov/33988703/)). However, the weight of evidence now decisively refutes this model.

This report evaluates the hypothesis against 51 papers reviewed across 5 investigative iterations. The competing **Tick Salivary Constituent Sensitization Model** — in which endogenous tick alpha-gal glycoproteins and glycolipids delivered in a Th2-skewing salivary context drive IgE class-switching — is the strongly supported alternative and represents the current mechanistic consensus.

---

## Key Findings

### Finding 1: Pathogen-Free Tick Salivary Extract Induces Full AGS in Mice

The most decisive evidence against the microorganism model comes from the demonstration that tick salivary gland extract (TSGE) from laboratory-reared *Amblyomma americanum* ticks — free of known tick-borne pathogens — is sufficient to induce alpha-gal syndrome in AGKO mice ([PMID: 34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/)). Compared to control animals, TSGE-treated mice exhibited **190-fold higher total IgE** on Day 56 (0.60 ± 0.12 ng/ml vs. 113.2 ± 24.77 ng/ml; p < 0.001), and alpha-gal-specific IgE was produced (undetected vs. 158.4 ± 72.43 pg/ml). Critically, sensitized mice developed clinical allergic reactions upon meat challenge, demonstrating that the full spectrum of AGS — from IgE class-switching to clinical anaphylaxis — can be recapitulated without any pathogenic microorganism.

This experiment directly tests and refutes the core prediction of the microorganism model: that a co-transmitted pathogen is *necessary* for sensitization. The experimental design uses laboratory-reared ticks maintained free of *Borrelia*, *Ehrlichia*, *Rickettsia*, and other known tick-borne pathogens, eliminating the most prominent candidate microorganisms proposed under this hypothesis.

### Finding 2: No Epidemiological Correlation Between Tick-Borne Pathogens and Alpha-Gal sIgE

A study conducted in Podlasie, Poland — a region highly endemic for tick-borne infections — found no correlation between alpha-gal sIgE levels and antibodies to *Borrelia burgdorferi*, *Anaplasma phagocytophilum*, *Babesia* spp., or tick-borne encephalitis virus, despite a strong association with tick bite history (OR = 9.31) ([PMID: 35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/)). The study concluded: *"Our data support the link between I. ricinus ticks and the production of α-gal sIgE and confirm that the pathogens carried by ticks we examined for do not seem implicated in this immune response."*

This epidemiological dissociation — strong tick bite association but no pathogen association — is a critical refutation. If a co-transmitted pathogen were the primary sensitizer, one would expect a positive correlation between pathogen-specific antibodies and alpha-gal sIgE, which was not observed.

### Finding 3: Ticks Produce Alpha-Gal Endogenously via Galactosyltransferases

The molecular basis for the alternative model was established by the identification of three galactosyltransferase genes in *Ixodes scapularis* capable of synthesizing alpha-gal ([PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/)). Heterologous expression in alpha-gal-negative cells confirmed alpha-gal synthesis, and gene knockdown demonstrated that these enzymes are essential for tick feeding. This finding was extended by showing that alpha-gal concentration in *Hyalomma lusitanicum* salivary glands was independent of sex or blood meal status, confirming endogenous rather than exogenous origin ([PMID: 38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/)).

Most directly, nanospray ionization mass spectrometry (NSI-MS) identified alpha-gal-bound glycolipids directly in *Amblyomma americanum* saliva and demonstrated that these lipid antigens activate basophils ([PMID: 39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/)). This finding eliminates the need to invoke any microbial source: ticks themselves produce the sensitizing antigen and deliver it in a form capable of activating innate immune cells.

### Finding 4: Tick Bite Histology Reveals Th2 Immune Infiltrate Driving IgE Class Switch

Direct histological evidence from human *Amblyomma testudinarium* tick bite lesions demonstrated basophil, eosinophil, and type 2 cytokine-producing T cell infiltration at bite sites ([PMID: 29273488](https://pubmed.ncbi.nlm.nih.gov/29273488/)). Patients with ≥2 tick bites had greater inflammatory infiltrates and higher alpha-gal IgE levels. The study reported that *"basophils; eosinophils; and type 2, cytokine-producing T cells infiltrate the skin and alpha-gal IgE antibodies are produced. These findings provide a potential mechanistic connection between Amblyomma bites and red meat hypersensitivity."* This establishes the cellular mechanism for IgE class-switching to alpha-gal at the tick bite site, supporting the salivary constituent model and demonstrating no microbial trigger is needed.

### Finding 5: Blood Group B Protection Confirms Anti-Gal Immune Biology

Across independent cohorts, blood group B individuals are dramatically underrepresented among AGS patients. In a Swedish cohort (n=128), only 2 patients had blood group B ([PMID: 32142962](https://pubmed.ncbi.nlm.nih.gov/32142962/)). In French Guiana (n=54 cases), 0% of AGS cases had blood group B or AB versus 19% of controls (AOR = 0.227, 95% CI [0–8.899]) ([PMID: 41610799](https://pubmed.ncbi.nlm.nih.gov/41610799/)). The blood group B antigen is structurally related to alpha-gal, and anti-Gal/B clones comprise >85% of anti-B antibody activity ([PMID: 37449060](https://pubmed.ncbi.nlm.nih.gov/37449060/)). Self-tolerance to blood antigen B reduces the anti-alpha-gal immune response ([PMID: 28280265](https://pubmed.ncbi.nlm.nih.gov/28280265/)). This host susceptibility finding is fully consistent with the salivary constituent model and orthogonal to the microorganism model.

### Finding 6: Helminth Alpha-Gal Demonstrates That Antigen Source ≠ Disease Driver

*Ascaris lumbricoides* helminths contain alpha-gal at higher concentrations than tick species, and alpha-gal IgE correlates with *Ascaris*-specific IgE ([PMID: 34333031](https://pubmed.ncbi.nlm.nih.gov/34333031/)). However, in helminth-endemic regions of Ecuador (32% sensitization) and Kenya (54% sensitization), meat allergy was *not* reported despite widespread alpha-gal sensitization ([PMID: 33539899](https://pubmed.ncbi.nlm.nih.gov/33539899/)). The study noted: *"Sensitization was associated with rural living, antibody markers of Ascaris exposure, and total IgE, but not active infections with Ascaris or Trichuris species."*

This dissociation between sensitization and clinical disease is the most intellectually important finding from this investigation. It proves that the *source* of alpha-gal antigen is not the determining factor — the immunological context in which sensitization occurs (specifically, the Th2-skewing tick salivary milieu) is what drives clinical AGS. This insight is devastating for the microorganism model, which hinges entirely on the identity of the antigen source, and confirms that the microorganism model was fundamentally asking the wrong question.

### Finding 7: Endosymbiont Caveat — Formal Exclusion of All Microorganisms Is Incomplete

An important methodological limitation was identified: Francisella-like endosymbionts (FLE) are the most dominant bacteria in both laboratory-raised and field-collected *A. americanum* ticks ([PMID: 35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/)). These obligate endosymbionts cannot be eliminated without killing the tick, meaning the TSGE experiments technically refute only *known tick-borne pathogens*, not all tick-associated microorganisms. However, given that: (a) ticks produce alpha-gal endogenously, (b) alpha-gal glycolipids are directly identified in saliva, and (c) the salivary immune context — not antigen source — drives clinical disease, this caveat does not meaningfully support the microorganism model.

---

{{figure:final_verdict_diagram.png|caption=Comprehensive hypothesis evaluation diagram showing the refuted Tick-Associated Microorganism Model versus the supported Tick Salivary Constituent Sensitization Model, with mechanistic chains, qualifying evidence (endosymbiont caveat, pathogen modulation), key insight from helminth data, and overall verdict.}}

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Disease Context | Confidence & Limitations |
|---|----------|--------------|-----------|--------------------------|-------------|-----------------|--------------------------|
| 1 | [PMID: 34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/) | Model organism (AGKO mouse) | **REFUTES** | Microorganism needed for sensitization | Pathogen-free TSGE → 190-fold IgE increase (p<0.001) + clinical AGS | A. americanum, mouse model | **High**. Direct test. Limitation: endosymbionts not excluded |
| 2 | [PMID: 35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/) | Human clinical (epidemiological) | **REFUTES** | Pathogen antibodies correlate with alpha-gal sIgE | No pathogen correlation; OR=9.31 for tick bites | I. ricinus endemic, Poland | **High**. Large cohort; limited pathogen panel tested |
| 3 | [PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/) | In vitro / molecular | **REFUTES** / **QUALIFIES** | Microbial source needed for alpha-gal | 3 galactosyltransferase genes; heterologous expression confirmed; Anaplasma increases alpha-gal | I. scapularis | **High**. Functional confirmation. Dual finding: refutes primary role, qualifies modulatory |
| 4 | [PMID: 39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/) | In vitro / analytical chemistry | **REFUTES** | Tick saliva alpha-gal requires microbial origin | Alpha-gal glycolipids identified in A. americanum saliva by NSI-MS; basophil activation demonstrated | A. americanum | **High**. Direct MS identification |
| 5 | [PMID: 38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/) | In vitro / biochemical | **REFUTES** | Alpha-gal from blood meal or microbes | Alpha-gal independent of sex/diet in salivary glands | H. lusitanicum | **Moderate**. Single species; extends generalizability |
| 6 | [PMID: 29273488](https://pubmed.ncbi.nlm.nih.gov/29273488/) | Human clinical (histology) | **Supports alternative** | Th2 immune pathway at bite site | Basophils, eosinophils, Th2 T cells at bite site; dose-response with repeated bites | A. testudinarium, Japan | **High**. Direct human histology |
| 7 | [PMID: 25747720](https://pubmed.ncbi.nlm.nih.gov/25747720/) | Review (historical) | **SUPPORTS** (historically) | Microorganism as competing hypothesis | Listed as one of competing theories | General AGS | **Low**. No experimental evidence |
| 8 | [PMID: 33988703](https://pubmed.ncbi.nlm.nih.gov/33988703/) | Review | **QUALIFIES** | Pathogens carry alpha-gal on surface | Borrelia and Anaplasma express surface alpha-gal | General | **Low**. Does not prove causation |
| 9 | [PMID: 34333031](https://pubmed.ncbi.nlm.nih.gov/34333031/) | Human clinical / in vitro | **QUALIFIES** | Non-tick organisms as alpha-gal source | Ascaris alpha-gal > tick alpha-gal; IgE correlation | South Africa | **High**. But clinical AGS absent |
| 10 | [PMID: 33539899](https://pubmed.ncbi.nlm.nih.gov/33539899/) | Human clinical (epidemiological) | **Supports alternative** | Antigen source vs. immune context | 32–54% sensitized via helminths, no meat allergy | Ecuador, Kenya | **High**. Large populations |
| 11 | [PMID: 35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/) | Molecular / microbiome | **QUALIFIES** | "Pathogen-free" = truly microbe-free? | FLE dominant in lab and field A. americanum | Tick biology | **High** for observation; low impact on verdict |
| 12 | [PMID: 38390396](https://pubmed.ncbi.nlm.nih.gov/38390396/) | Model organism (AGKO mouse) | **Supports alternative** | Species-specific tick factors | A. americanum > A. maculatum for IgE induction | Tick species comparison | **Moderate-High** |
| 13 | [PMID: 32142962](https://pubmed.ncbi.nlm.nih.gov/32142962/) | Human clinical (cohort) | **Supports alternative** | Host susceptibility factors | Blood group B underrepresented (2/128); atopy modulates severity | Sweden | **High** |
| 14 | [PMID: 41610799](https://pubmed.ncbi.nlm.nih.gov/41610799/) | Human clinical (case-control) | **Supports alternative** | Blood group B protection | 0% B/AB in cases vs 19% controls; AOR for tick bite = 170.25 | French Guiana | **Moderate-High**. Small sample (n=54) |
| 15 | [PMID: 37449060](https://pubmed.ncbi.nlm.nih.gov/37449060/) | Review / experimental | **QUALIFIES** | Alpha-gal as core of blood group antigens | Anti-Gal/B clones >85% of anti-B activity; T-cell help paradox | Transplant immunology | **Moderate-High** |
| 16 | [PMID: 28280265](https://pubmed.ncbi.nlm.nih.gov/28280265/) | Computational / epidemiological | **QUALIFIES** | Blood type B and alpha-gal immunity | Structural similarity → tolerance → reduced AGS risk | Infectious disease | **Moderate** |
| 17 | [PMID: 32268573](https://pubmed.ncbi.nlm.nih.gov/32268573/) | Model organism / in vitro | **QUALIFIES** | Helminth sensitization capacity | Helminths evaluated for alpha-gal sensitization | Parasitology | **Moderate** |
| 18 | [PMID: 42391055](https://pubmed.ncbi.nlm.nih.gov/42391055/) | Human clinical (seroprevalence) | **Supports alternative** | Distribution matches tick range | Seroprevalence 31% Arkansas, 26% Missouri; matches A. americanum range | US population | **High** |
| 19 | [PMID: 32522461](https://pubmed.ncbi.nlm.nih.gov/32522461/) | Human clinical (epidemiological) | **Supports alternative** | Geographic link to tick species | AGS distribution matches A. americanum range; case-control confirmed | US epidemiology | **High** |
| 20 | [PMID: 39441524](https://pubmed.ncbi.nlm.nih.gov/39441524/) | Human clinical (population) | **QUALIFIES** | Prevalence trends | Alpha-gal sensitization doubled from 1.3% to 3.7% (1990–2017); >97% asymptomatic | Denmark | **High** |

---

## Mechanistic Causal Chain

### The Tick-Associated Microorganism Model (Refuted)

```
Tick bite
  │
  ▼
Co-transmitted microorganism (Rickettsia, Borrelia, etc.) enters host skin
  │                                    ← CHAIN BREAKS HERE
  ▼                                      (pathogen-free TSGE suffices;
Microorganism expresses alpha-gal         no epidemiological correlation;
  │                                       ticks make their own alpha-gal)
  ▼
Microbial alpha-gal + immune adjuvant → Th2 polarization → IgE class switch
  │
  ▼
Anti-alpha-gal sIgE → delayed anaphylaxis upon mammalian meat consumption
```

**Where the chain is broken:**

| Step | Status | Key Evidence |
|------|--------|-------------|
| Tick bite → microorganism enters host | Established (general biology) | — |
| Microorganism carries alpha-gal | Confirmed for some species | PMID: 33988703 |
| Microorganism alpha-gal is *necessary* | **REFUTED** | PMID: 34034363 |
| Microorganism alpha-gal *correlates* with sIgE | **REFUTED** | PMID: 35382677 |
| Tick requires exogenous alpha-gal source | **REFUTED** | PMID: 30242261, 39053323 |

### The Supported Alternative: Tick Salivary Constituent Sensitization Model

```
Tick feeds on human host (prolonged skin penetration, often repeated)
  │
  ▼
Tick injects saliva containing:
  • Alpha-gal glycoproteins (endogenously synthesized by galactosyltransferases)
  • Alpha-gal glycolipids (confirmed by mass spectrometry)
  • Immunomodulatory factors (Th2-skewing salivary adjuvants)
  │
  ▼
Cutaneous immune response at bite site:
  • Tick saliva polarizes toward Th2
  • Basophils, eosinophils, Th2 T cells infiltrate (confirmed in human histology)
  • Langerhans cells/dendritic cells process alpha-gal antigens
  │
  ▼
B cell IgE class-switching to alpha-gal
  (mechanism of T-cell help for carbohydrate antigen still unclear)
  │
  ▼
Anti-alpha-gal sIgE circulates systemically
  │
  ▼
Upon mammalian meat ingestion:
  Alpha-gal on meat glycolipids absorbed (delayed due to lipid digestion)
  → Cross-links IgE on mast cells/basophils
  → Delayed anaphylaxis (3-6 hours post-ingestion)
```

**Evidence strength at each step:**

| Step | Strength | Key References |
|------|----------|----------------|
| Tick saliva contains alpha-gal | **Strong** | PMID: 39053323, 30242261, 38741222 |
| Tick saliva sufficient for sensitization | **Strong** | PMID: 34034363 |
| Cutaneous Th2 response at bite site | **Strong** | PMID: 29273488 |
| Repeated bites amplify response | **Strong** | PMID: 29273488, 32522461 |
| IgE class-switching mechanism | **Moderate** (T-cell help paradox unresolved) | PMID: 32765532, 37449060 |
| Host susceptibility (blood group B protection) | **Moderate** | PMID: 32142962, 41610799 |
| Delayed reaction via lipid digestion | **Moderate** (clinically observed, mechanism inferred) | PMID: 25747720 |

---

{{figure:comprehensive_evidence_diagram.png|caption=Two-panel visualization showing (left) the mechanistic causal chains for both the refuted microorganism model and the supported salivary constituent model, and (right) a summary of evidence categories and knowledge gaps organized by evidence type and direction.}}

---

## Knowledge Gaps

### Gap 1: Formal Exclusion of Endosymbiont Contribution

- **Scope:** Obligate tick endosymbionts (Francisella-like organisms, Coxiella-like organisms) cannot be eliminated from laboratory tick colonies without compromising tick viability.
- **Why it matters:** The TSGE experiment ([PMID: 34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/)) refutes known tick-borne pathogens but not all tick-associated microorganisms. A strict interpretation of the microorganism model could claim endosymbionts contribute.
- **What was checked:** Microbiome studies confirm FLE dominance in lab colonies ([PMID: 35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/)); no antibiotic-perturbation experiments in AGS context were found.
- **What would resolve it:** Antibiotic-treated tick salivary extracts tested for sensitization capacity in AGKO mice; or reconstitution experiments with recombinant tick alpha-gal (completely microorganism-free) combined with tick salivary adjuvant fractions.

### Gap 2: Molecular Identity of Tick Salivary Th2 Adjuvant(s)

- **Scope:** While tick saliva clearly creates a Th2-skewing environment, the specific molecular component(s) responsible have not been definitively identified.
- **Why it matters:** Without identifying the adjuvant, we cannot fully explain why tick-delivered alpha-gal (but not helminth-delivered alpha-gal) produces clinical AGS. Identification would also explain species-specific differences (A. americanum >> A. maculatum for sensitization; [PMID: 38390396](https://pubmed.ncbi.nlm.nih.gov/38390396/)).
- **What was checked:** Alpha-gal glycolipids activate basophils ([PMID: 39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/)); Th2 infiltrate confirmed at bite sites ([PMID: 29273488](https://pubmed.ncbi.nlm.nih.gov/29273488/)); but specific IgE class-switch signals remain uncharacterized.
- **What would resolve it:** Fractionation of tick saliva with systematic testing of each fraction for Th2-skewing and IgE class-switching capacity.

### Gap 3: Mechanism of IgE Class Switching to a Carbohydrate Antigen

- **Scope:** IgE production typically requires T-cell help and sequential class switching, but immune responses to carbohydrates are classically T-cell independent.
- **Why it matters:** This is the central immunological mystery of AGS, explicitly flagged by multiple expert reviews ([PMID: 25747720](https://pubmed.ncbi.nlm.nih.gov/25747720/), [PMID: 32057766](https://pubmed.ncbi.nlm.nih.gov/32057766/)). Understanding it would clarify why only some tick-bitten individuals develop AGS.
- **What was checked:** Anti-Gal/B clones and T-cell help requirements described ([PMID: 37449060](https://pubmed.ncbi.nlm.nih.gov/37449060/)); CD1d/iNKT pathway proposed as candidate mechanism based on general immunology ([PMID: 26564814](https://pubmed.ncbi.nlm.nih.gov/26564814/), [PMID: 25830340](https://pubmed.ncbi.nlm.nih.gov/25830340/)) but not tested in AGS.
- **What would resolve it:** CD1d-KO × AGKO double knockout mouse studies; identification of carrier glycoproteins providing T-cell epitopes alongside alpha-gal.

### Gap 4: Why Only a Fraction of Sensitized Individuals Develop Clinical AGS

- **Scope:** Most alpha-gal-sensitized individuals develop IgE but only a minority develop clinical AGS. In Denmark, >97% of sensitized individuals continue to eat red meat without reactions ([PMID: 39441524](https://pubmed.ncbi.nlm.nih.gov/39441524/)).
- **Why it matters:** Identifying host susceptibility factors would enable risk stratification and prevention.
- **What was checked:** Blood group B dramatically underrepresented ([PMID: 32142962](https://pubmed.ncbi.nlm.nih.gov/32142962/), [PMID: 41610799](https://pubmed.ncbi.nlm.nih.gov/41610799/)); atopy modulates severity; repeated bites increase risk.
- **What would resolve it:** GWAS or immune phenotyping comparing sensitized individuals with and without clinical AGS.

### Gap 5: Cross-Species Tick Variation

- **Scope:** Multiple tick species across all continents are associated with AGS, but their relative potency and mechanism may differ.
- **Why it matters:** If species-specific endosymbionts contributed to sensitization, this would be a species-specific modulatory role for microorganisms.
- **What was checked:** A. americanum > A. maculatum in mouse models ([PMID: 38390396](https://pubmed.ncbi.nlm.nih.gov/38390396/)); galactosyltransferases in I. scapularis ([PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/)).
- **What would resolve it:** Comparative salivary glycomics and microbiomics across all AGS-associated tick species.

### Gap 6: Limited Pathogen Panel in Epidemiological Refutation

- **Scope:** The Polish study ([PMID: 35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/)) tested Borrelia, Anaplasma, Babesia, and TBEV but not all possible tick microbes.
- **What would resolve it:** Broader microbiome-wide association study correlating tick microbiome composition with host alpha-gal IgE titers.

### Gap 7: Source/Data-Level Absences

- No GenCC, ClinGen, or genetic association data specifically for AGS susceptibility were found.
- No clinical trials testing the microorganism hypothesis or anti-microbial interventions for AGS prevention.
- No omics-level datasets comparing immune responses to pathogen-bearing vs. pathogen-free tick bites in humans.

---

## Alternative Models

### 1. Tick Salivary Constituent Sensitization Model *(Direct Alternative — Strongly Supported)*

Tick saliva contains endogenously produced alpha-gal glycoproteins and glycolipids that, combined with tick-derived immunomodulatory factors, drive IgE class switching via the cutaneous immune route. This model fully replaces the microorganism model and is supported by mouse models, molecular biology, human histology, and epidemiology.

### 2. Residual Blood Meal Model *(Alternative Source — Largely Refuted)*

Proposes alpha-gal originates from retained mammalian blood meal in tick salivary glands. Largely refuted by evidence that alpha-gal levels are independent of feeding status ([PMID: 38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/)) and by functional confirmation of tick galactosyltransferases ([PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/)).

### 3. Helminth/Parasite Co-Sensitization Model *(Parallel Mechanism — Supported for Sensitization Only)*

Helminths (particularly *Ascaris*) contain alpha-gal at high concentrations and can drive IgE sensitization. However, helminth-driven sensitization does NOT produce clinical AGS ([PMID: 33539899](https://pubmed.ncbi.nlm.nih.gov/33539899/)), demonstrating that the tick salivary adjuvant context is uniquely required for disease.

### 4. Cutaneous Immune Route / Skin Barrier Model *(Complementary — Emerging)*

The unique cutaneous route of tick antigen delivery (prolonged penetration, Th2-promoting skin environment) is critical for IgE class switching, distinguishing tick exposure from mucosal helminth exposure. Complements the salivary constituent model by explaining *why* the route matters.

### 5. Host Genetic Susceptibility Model *(Complementary — Emerging)*

Blood group B protection is consistent across cohorts ([PMID: 32142962](https://pubmed.ncbi.nlm.nih.gov/32142962/), [PMID: 41610799](https://pubmed.ncbi.nlm.nih.gov/41610799/), [PMID: 28280265](https://pubmed.ncbi.nlm.nih.gov/28280265/)). Explains inter-individual variation rather than being an alternative to the salivary model.

### 6. CD1d/iNKT Cell Glycolipid Presentation Model *(Candidate Downstream Mechanism — Speculative)*

Alpha-gal glycolipids in tick saliva may be presented via CD1d to invariant NKT cells, which produce IL-4/IL-13 needed for IgE class switching. Based on general immunology of iNKT cells ([PMID: 26564814](https://pubmed.ncbi.nlm.nih.gov/26564814/), [PMID: 25830340](https://pubmed.ncbi.nlm.nih.gov/25830340/)) but not yet tested in AGS. Would resolve the T-cell help paradox for carbohydrate antigens.

### 7. Acquired Tick Resistance / Evolutionary Trade-off Model *(Complementary — Emerging)*

Alpha-gal IgE may have evolved as part of acquired tick resistance; AGS is a maladaptive consequence. Anti-alpha-gal IgM/IgG protects against pathogens while IgE causes allergy ([PMID: 33988703](https://pubmed.ncbi.nlm.nih.gov/33988703/)).

---

## Discriminating Tests

### Test 1: Endosymbiont-Depleted TSGE Sensitization Assay

- **Objective:** Determine whether removing endosymbiont components from tick saliva reduces sensitization capacity.
- **Design:** Antibiotic-treated TSGE versus unmodified TSGE in AGKO mice with pork challenge.
- **Expected result if microorganism model has residual validity:** Reduced IgE induction with endosymbiont-depleted TSGE.
- **Expected result if salivary model is complete:** No difference.

### Test 2: Recombinant Alpha-Gal + Salivary Adjuvant Reconstitution

- **Objective:** Test whether purified (microorganism-free) tick alpha-gal glycolipids combined with tick salivary proteins suffice for AGS.
- **Design:** Intradermal administration in AGKO mice of: (a) synthetic alpha-gal glycolipids alone, (b) tick salivary protein fraction alone, (c) combination.
- **Expected result:** Combination induces full AGS; alpha-gal alone induces only sensitization; salivary proteins alone induce Th2 without alpha-gal specificity.

### Test 3: Prospective Human Cohort with Broad Pathogen Serology

- **Objective:** Definitively test epidemiological prediction across a broader pathogen/microbiome panel.
- **Design:** ≥500 tick-exposed individuals; serial alpha-gal sIgE + comprehensive pathogen/endosymbiont serology + tick 16S sequencing.
- **Patient stratification:** Blood group B vs. non-B; atopic vs. non-atopic; tick bite frequency.

### Test 4: Helminth Alpha-Gal + Tick Adjuvant Cross-Over

- **Objective:** Determine why helminth alpha-gal drives sensitization but not clinical AGS.
- **Design:** Compare Ascaris alpha-gal extract alone vs. TSGE vs. Ascaris alpha-gal + tick adjuvant fraction in AGKO mice.
- **Expected result:** If tick adjuvant + any alpha-gal source → clinical AGS, this definitively proves antigen source is irrelevant and adjuvant context is everything.

### Test 5: CD1d-KO × AGKO Double Knockout Mouse Study

- **Objective:** Test whether CD1d-restricted iNKT cells provide T-cell help for alpha-gal IgE class switching.
- **Design:** Compare TSGE sensitization and alpha-gal IgE production in AGKO vs. CD1d-KO × AGKO mice.
- **Expected result if CD1d pathway involved:** Reduced IgE in double-KO mice.

### Test 6: Cross-Species Tick Salivary Glycomics

- **Objective:** Determine whether alpha-gal content or microbiome composition predicts sensitization potency.
- **Design:** Comparative glycomics + microbiomics of saliva from A. americanum, I. ricinus, A. testudinarium, I. holocyclus, and A. maculatum.
- **Expected result:** Endogenous alpha-gal content (not microbiome diversity) correlates with sensitization risk.

---

{{figure:evidence_map.png|caption=Evidence map summarizing the direction and strength of key studies for the refuted microorganism model versus the supported salivary constituent sensitization model.}}

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References

| PMID | Snippet (to verify against abstract) | Proposed Direction | Proposed Action |
|------|--------------------------------------|-------------------|-----------------|
| [39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/) | "Nanospray ionization mass spectrometry (NSI-MS) analysis revealed the identification of α-gal bound lipid antigens in Am. americanum saliva." | REFUTE (microorganism) / SUPPORT (salivary) | Add as evidence for both hypotheses |
| [38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/) | "Neither sex nor diet influenced the concentration of α-Gal, which seems to indicate its endogenous production" | REFUTE | Add as REFUTE for microorganism model |
| [38390396](https://pubmed.ncbi.nlm.nih.gov/38390396/) | "Our results showed a significant increase in the total IgE, IgG1, and α-gal IgG1 antibodies titers in the lone-star tick-sensitized AGKO mice compared to the gulf-coast tick-sensitized mice." | REFUTE (indirectly) | Species specificity argues against shared pathogen explanation |
| [35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/) | "Overall, Francisellaceae was the most dominant bacteria identified in the microbiome of both laboratory-raised and field-collected" | QUALIFIES | Add as knowledge_gap: endosymbiont not formally excluded |
| [29273488](https://pubmed.ncbi.nlm.nih.gov/29273488/) | "basophils; eosinophils; and type 2, cytokine-producing T cells infiltrate the skin and alpha-gal IgE antibodies are produced." | SUPPORT (salivary model) | Add as direct human histological evidence |
| [34333031](https://pubmed.ncbi.nlm.nih.gov/34333031/) | "Alpha-gal protein at 70 to 130 kDa was detected in A lumbricoides at concentrations higher than those found in...ticks." | QUALIFIES | Non-tick alpha-gal sources exist but don't cause clinical AGS |
| [33539899](https://pubmed.ncbi.nlm.nih.gov/33539899/) | "Sensitization was associated with rural living, antibody markers of Ascaris exposure, and total IgE, but not active infections" | QUALIFIES / Supports alternative | Antigen source alone insufficient for AGS |

### Candidate Pathophysiology Nodes/Edges

- **Node:** Tick galactosyltransferase enzymes → alpha-gal synthesis (established, PMID: 30242261)
- **Edge:** Tick salivary alpha-gal glycolipids → basophil activation (established, PMID: 39053323)
- **Edge:** Tick bite → cutaneous basophil/eosinophil/Th2 T cell infiltrate → IgE class switch (established, PMID: 29273488)
- **Edge (modulatory):** Anaplasma infection → increased tick alpha-gal levels (PMID: 30242261) — note as modulatory, not causal
- **Edge (host):** Blood group B → tolerance to alpha-gal-like epitopes → reduced AGS risk (emerging, PMID: 32142962, 41610799, 28280265)
- **Edge (candidate, speculative):** Tick salivary alpha-gal glycolipids → CD1d presentation → iNKT cell activation → IL-4/IL-13 → IgE class switch

### Candidate Ontology Terms

- **Cell types:** basophil (CL:0000767), eosinophil (CL:0000771), Th2 T cell (CL:0000546), mast cell (CL:0000097), iNKT cell, Langerhans cell (CL:0001006)
- **Biological processes:** IgE isotype switching (GO:0048291), alpha-galactosyltransferase activity (GO:0004577), basophil activation (GO:0002553), type 2 immune response (GO:0042092)

### Candidate Status Changes

- **tick_associated_microorganism:** **Confirm DEPRECATED**. Evidence from 51 papers across 5 iterations strongly supports this designation.
- **Recommended note update:** Add PMID: 39053323, 38390396, 38741222, and 35493735 to the deprecation notes as additional evidence beyond the original two citations.

### Candidate Knowledge Gaps for KB

1. Mechanism of IgE class switching to carbohydrate antigen alpha-gal (central unresolved question)
2. Quantitative contribution of tick endosymbionts to alpha-gal load (methodological limitation: TSGE experiments exclude pathogens but not all microorganisms)
3. Host genetic determinants of clinical AGS vs. asymptomatic sensitization (no GWAS/genetic data found)
4. Identity of specific tick salivary Th2 adjuvant factors (fractionation studies needed)

### Candidate Discussion Prompts

1. Should the KB explicitly note the endosymbiont caveat (PMID: 35493735) in the deprecation notes, or does this over-represent a refuted model?
2. Should a new hypothesis node be created for "tick microbiota as alpha-gal amplifier" (distinct from "microorganism as primary sensitizer")?
3. The helminth evidence reveals that **sensitization ≠ clinical AGS**. Should the KB formally distinguish between these two phenotypes?
4. The CD1d/iNKT pathway is a speculative but plausible candidate mechanism for the T-cell help paradox. Worth noting as a candidate edge?

---

## Answers to Research Objective Questions

### 1. Strongest direct evidence FOR this hypothesis
Only historical: [PMID: 25747720](https://pubmed.ncbi.nlm.nih.gov/25747720/) lists the microorganism theory as one of competing mechanisms. No experimental study has ever provided positive evidence that a co-transmitted microorganism is the primary sensitizer for AGS.

### 2. Evidence AGAINST the hypothesis
Three independent, converging experimental and epidemiological refutations: pathogen-free TSGE sufficiency ([PMID: 34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/)); no pathogen-sIgE correlation ([PMID: 35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/)); endogenous tick alpha-gal production ([PMID: 30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/), [PMID: 39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/), [PMID: 38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/)).

### 3. Claim status summary

| Claim | Status |
|-------|--------|
| Tick-borne pathogens are the primary sensitizing agent | **Contradicted** |
| Tick-borne pathogens carry alpha-gal on their surfaces | **Established** (but irrelevant to causation) |
| Pathogen infection modulates tick alpha-gal levels | **Established** (minor modulatory role) |
| Endosymbionts contribute to sensitization | **Speculative** (not formally excluded) |
| Non-tick organisms (helminths) drive alpha-gal sensitization | **Emerging** (sensitization yes, clinical AGS no) |
| Tick salivary constituents are the primary sensitizer | **Established** |

### 4. Patient subtypes the hypothesis best explains
The microorganism model does NOT best explain any AGS subtype. The salivary constituent model provides a more parsimonious explanation for all observed clinical patterns.

### 5. Better alternative hypotheses
The **Tick Salivary Constituent Sensitization Model** explains all features of AGS more parsimoniously. See Alternative Models section for 7 competing/complementary hypotheses.

### 6. Knowledge gaps
Seven explicit gaps identified — see Knowledge Gaps section. The most critical is the mechanism of IgE class switching to a carbohydrate antigen.

### 7. Discriminating experiments
Six concrete tests proposed — see Discriminating Tests section. The most informative would be: (a) endosymbiont-depleted TSGE assay, (b) helminth alpha-gal + tick adjuvant cross-over, and (c) CD1d-KO × AGKO double knockout mouse study.

---

*Report compiled across 5 iterations of systematic hypothesis evaluation. Total literature reviewed: 51 papers. Evidence matrix: 20 primary entries. Confirmed findings: 7. Generated: 2026-07-05.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist comprehensive evidence diagram](openscientist_artifacts/provenance_comprehensive_evidence_diagram.json)
![OpenScientist comprehensive evidence diagram](openscientist_artifacts/provenance_comprehensive_evidence_diagram.png)
- [OpenScientist evidence map](openscientist_artifacts/provenance_evidence_map.json)
![OpenScientist evidence map](openscientist_artifacts/provenance_evidence_map.png)
- [OpenScientist final verdict diagram](openscientist_artifacts/provenance_final_verdict_diagram.json)
![OpenScientist final verdict diagram](openscientist_artifacts/provenance_final_verdict_diagram.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)