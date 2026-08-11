# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Parkinson's Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** brain_first_central_alpha_synuclein_model
- **Hypothesis Label:** Brain-First Central α-Synuclein Initiation Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: brain_first_central_alpha_synuclein_model
hypothesis_label: Brain-First Central α-Synuclein Initiation Model
status: ALTERNATIVE
description: Alpha-synuclein pathology initiates within central nervous system sites such as the olfactory
  bulb or amygdala and spreads centrifugally to brainstem and peripheral autonomic structures. This model
  best explains Parkinson disease presentations where central dopaminergic or olfactory involvement precedes
  prominent autonomic and enteric manifestations.
notes: The model is supported mainly by subtype-level human imaging, clinical, and neuropathological patterns.
  It competes with, rather than refutes, the body-first model because both origin routes may exist within
  clinically diagnosed Parkinson disease.
evidence:
- reference: PMID:38519273
  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update on recent evidence.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the initial pathology starts either in the olfactory bulb or amygdala leading to a brain-first
    subtype, or in the enteric nervous system leading to a body-first subtype.
  explanation: The ASOC model explicitly defines an olfactory bulb/amygdala origin as the brain-first
    subtype that competes with the enteric body-first route.
- reference: PMID:38519273
  reference_title: 'Brain-first vs. body-first Parkinson''s disease: An update on recent evidence.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: These subtypes should be distinguishable early in the disease course on a range of imaging,
    clinical, and neuropathological markers.
  explanation: Human subtype distinguishability supports representing brain-first and body-first disease
    routes as alternative mechanistic hypothesis groups.
- reference: PMID:32830221
  reference_title: 'Brain-first versus body-first Parkinson''s disease: a multimodal imaging case-control
    study.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: the PDRBD- data were compatible with a brain-first trajectory, characterized by primary loss
    of putaminal FDOPA uptake followed by a secondary loss of cardiac MIBG signal and 11C-donepezil signal.
  explanation: Primary multimodal imaging data support a brain-first trajectory in RBD-negative de novo
    PD, where central dopaminergic dysfunction appears before peripheral autonomic marker loss.
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

**Provider:** openscientist
**Generated:** 2026-07-06T06:14:58.676310

1. PMID:32830221
2. PMID:34334424
3. PMID:40209563
4. PMID:38879548
5. PMID:35989519
6. PMID:33547846
7. PMID:35943058
8. PMID:38519273
9. PMID:41309711
10. PMID:42390607
11. PMID:39665845
12. PMID:40542411
13. PMID:41714532
14. PMID:29084403
15. PMID:37422999
16. PMID:40678221
17. PMID:41316710
18. PMID:35733234
19. PMID:38267190
20. PMID:39973492
21. PMID:40796681
22. PMID:41195692
23. PMID:38607765
24. PMID:35031485
25. PMID:33682732
26. PMID:34910119
27. PMID:39370052
28. PMID:40250815
29. PMID:31797870
30. PMID:33978813
31. PMID:31254094
32. PMID:30166532
33. PMID:40754311
34. PMID:37062013
35. PMID:15480835
36. PMID:40771982