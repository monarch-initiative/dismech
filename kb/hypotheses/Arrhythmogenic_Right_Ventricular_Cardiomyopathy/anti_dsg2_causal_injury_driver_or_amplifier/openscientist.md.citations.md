# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** arrhythmogenic right ventricular cardiomyopathy
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** anti_dsg2_causal_injury_driver_or_amplifier
- **Hypothesis Label:** Anti-DSG2 Causal Injury Driver or Amplifier
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: anti_dsg2_causal_injury_driver_or_amplifier
hypothesis_label: Anti-DSG2 Causal Injury Driver or Amplifier
status: EMERGING
description: Anti-DSG2 antibodies may causally worsen genetically vulnerable myocardium either as antecedent
  drivers or as injury-dependent amplifiers. Candidate mechanisms are direct impairment of junctional
  adhesion or electrical coupling and Fc-receptor- or complement-dependent injury. A signal that merely
  follows tissue damage without antigen-specific functional activity is the null, biomarker-only alternative
  and refutes this causal hypothesis. DAMP-mediated innate activation remains a separately tested possible
  upstream or parallel branch rather than a presumed linear cascade. Current evidence does not warrant
  wiring this emerging hypothesis to a causal pathophysiology edge, defining a clinical biomarker, or
  proposing an immune-directed treatment.
evidence:
- reference: PMID:42406223
  reference_title: 'From inflammation to inheritance: rethinking myocarditis as the first signal of desmosomal
    cardiomyopathy.'
  supports: PARTIAL
  evidence_source: OTHER
  snippet: While these observations support a possible role for autoimmunity, the causal contribution
    of these autoantibodies to myocardial injury and disease progression remains incompletely established
    and constitutes a proposed rather than confirmed model.
  explanation: The seed narrative review explicitly identifies the causal autoimmune interpretation as
    a working model while emphasizing that it remains unconfirmed. This supports testing an emerging causal
    hypothesis, not treating an injury-associated antibody signal as part of that hypothesis.
- reference: PMID:30239670
  reference_title: An autoantibody identifies arrhythmogenic right ventricular cardiomyopathy and participates
    in its pathogenesis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: We identified anti-DSG2 antibodies in 12/12 and 25/25 definite ARVC cohorts and 7/8 borderline
    subjects.
  explanation: The original small discovery and validation cohorts support antibody occurrence in clinically
    defined ARVC. The study lacked myocarditis and inflammatory-cardiomyopathy comparators, so these case-control
    results do not establish disease specificity, temporal order, or causality.
- reference: PMID:30239670
  reference_title: An autoantibody identifies arrhythmogenic right ventricular cardiomyopathy and participates
    in its pathogenesis.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: antibodies caused gap junction dysfunction, a common feature of ARVC, in vitro.
  explanation: Purified IgG from two ARVC patients and a commercial anti-DSG2 antibody provide an initial
    functional signal in human iPSC-derived cardiomyocytes. The experiment did not use antigen-specific
    depletion and add-back for patient IgG or establish Fc or complement dependence, necessity, or sufficiency
    in vivo.
- reference: PMID:37450050
  reference_title: Catalytic antibodies in arrhythmogenic cardiomyopathy patients cleave desmoglein 2
    and N-cadherin and impair cardiomyocyte cohesion.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: IgG fractions were purified from 15 AC patients and 4 healthy controls.
  explanation: The donor series was small, comprised only DSP- or PKP2-variant arrhythmogenic cardiomyopathy
    cases, and pooled IgG from four healthy controls. It included no inflammatory cardiac comparator,
    serial samples, or clinical test of whether the activity preceded injury.
- reference: PMID:37450050
  reference_title: Catalytic antibodies in arrhythmogenic cardiomyopathy patients cleave desmoglein 2
    and N-cadherin and impair cardiomyocyte cohesion.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Immunostainings revealed that autoantibodies against ICD proteins are prevalent in AC and most
    autoantibody fractions have catalytic properties and cleave the ICD adhesion molecules DSG2 and N-cadherin,
    thereby reducing cadherin interactions as revealed by AFM.
  explanation: In biochemical and murine atrial cell-line assays, 11 of 15 IgG fractions cleaved recombinant
    DSG2, six reduced cellular cohesion, and p38 inhibition rescued cohesion for selected fractions. The
    fractions also targeted N-cadherin, the study could not detect anti-DSG2 binding by its ELISAs, and
    it used no antigen-specific adsorption, monoclonal reconstruction, or intact-animal transfer.
- reference: PMID:39597880
  reference_title: 'Prevalence and Correlates of Anti-DSG2 Antibodies in Arrhythmogenic Right Ventricular
    Cardiomyopathy and Myocarditis: Immunological Insights from a Multicenter Study.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Anti-DSG2-ab titer was not different between ARVC and myocarditis/DCM patients (48% anti-DSG-ab
    positive).
  explanation: In 77 ARVC cases, 91 myocarditis or DCM cases, 27 systemic immune-mediated disease cases,
    and 50 controls, 56% of ARVC cases were positive, but titers did not distinguish ARVC from myocarditis
    or DCM and anti-DSG2 positivity had no ARVC clinical correlates. This argues against treating the
    antibody as ARVC-specific or as an established mediator.
- reference: PMID:32114801
  reference_title: 'Evidence From Family Studies for Autoimmunity in Arrhythmogenic Right Ventricular
    Cardiomyopathy: Associations of Circulating Anti-Heart and Anti-Intercalated Disk Autoantibodies With
    Disease Severity and Family History.'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Longitudinal studies are needed to clarify whether they may predict ARVC development in healthy
    relatives or if they be a result of manifest ARVC.
  explanation: Anti-heart and anti-intercalated-disc antibodies were enriched in ARVC families and associated
    cross-sectionally with severity features, but the investigators explicitly could not distinguish antecedent
    autoimmunity from a response to manifest disease.
- reference: PMID:35764120
  reference_title: High frequency of anti-DSG 2 antibodies in post COVID-19 serum samples.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Of note, 29.3% of the post COVID-19 infection samples demonstrated a signal higher than the
    90th percentile of the control population and 8.7% were higher than the median found in ARVC patients.
  explanation: Sustained anti-DSG2 signals after COVID-19 show that antibody elevation can follow a non-ARVC
    inflammatory or injury context. The study did not phenotype cardiac injury deeply, so it establishes
    neither a common mechanism nor harmlessness, but materially weakens disease specificity.
- reference: PMID:19635863
  reference_title: Myocyte necrosis underlies progressive myocardial dystrophy in mouse dsg2-related arrhythmogenic
    right ventricular cardiomyopathy.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: We demonstrate for the first time that myocyte necrosis is the key initiator of myocardial
    injury, triggering progressive myocardial damage, including an inflammatory response and massive calcification
    within the myocardium, followed by injury repair with fibrous tissue replacement, and myocardial atrophy.
  explanation: A transgenic Dsg2 model supports primary structural injury followed by inflammation and
    fibrosis. It does not test DAMP necessity or autoantibodies, and therefore supports a plausible injury-first
    branch without establishing the proposed adaptive immune sequence in humans.
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

For this ARVC anti-DSG2 investigation, explicitly:

- reconcile the selected-comparator diagnostic/prognostic findings in
  PMID:42233375 with the myocarditis/DCM comparator findings in PMID:39597880;
- distinguish native anti-DSG2 activity from total polyclonal IgG effects,
  N-cadherin or other intercalated-disc targets, proteolytic activity,
  Fc/complement mechanisms, and assay or cutoff artifacts;
- evaluate PMID:42219531 without treating its three responder IgG samples or
  GSK-3β rescue as anti-DSG2-specific causality or a treatment result;
- keep broader ACM, DSP cardiomyopathy, myocarditis, and post-COVID findings
  separate from evidence in exact ARVC;
- test injury-first and DAMP/cGAS-STING/TLR/IL-1 mechanisms as upstream or
  parallel alternatives, not as a presumed linear DAMP → anti-DSG2 cascade;
- identify whether any study provides antigen-specific depletion and add-back,
  monoclonal reconstruction, epitope rescue, Fc/complement dissection,
  intact-animal transfer, or longitudinal pre-injury antibody evidence.

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

**Provider:** openscientist
**Generated:** 2026-07-26T08:24:52.655852

1. PMID:39597880
2. PMID:42233375
3. PMID:41351822
4. PMID:42160918
5. PMID:30239670
6. PMID:37450050
7. PMID:34345905
8. PMID:39786454
9. PMID:34993452
10. PMID:42219531
11. PMID:32376797
12. PMID:32114801
13. PMID:35764120
14. PMID:19635863
15. PMID:42193878
16. PMID:41448261
17. PMID:42406223
18. PMID:39786662
