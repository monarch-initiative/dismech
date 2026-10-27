# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Opioid Use Disorder
- **Category:** Psychiatric

## Target Hypothesis
- **Hypothesis ID:** ibogaine_alpha3beta4_habenular_model
- **Hypothesis Label:** Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ibogaine_alpha3beta4_habenular_model
hypothesis_label: Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway
status: EMERGING
description: 'Proposes that iboga alkaloids reduce opioid self-administration by noncompetitively blocking
  alpha3beta4 nicotinic acetylcholine receptors, which are concentrated in the medial habenula and interpeduncular
  nucleus rather than in the mesolimbic pathway, and thereby damping the sensitized accumbal dopamine
  response to repeated opioid exposure. The site specificity is the model''s strength: local infusion
  into the medial habenula or interpeduncular nucleus reduces morphine self-administration while the same
  infusion into the ventral tegmental area does not, and the effect spares responding for a non-drug reinforcer.
  Its weakness for ibogaine specifically is that the supporting in vivo work uses the congener 18-MC,
  which does not reproduce ibogaine''s neurotrophic actions, while noribogaine is a comparatively weak
  alpha3beta4 blocker.'
notes: 'Distinguishing test: this model and the GDNF model predict opposite outcomes for a local-infusion
  dissociation - intra-habenular ibogaine should suffice if the nicotinic route carries the effect, intra-VTA
  ibogaine if the neurotrophic route does. The two are not mutually exclusive and may account for different
  time courses, with nicotinic blockade acting during drug exposure and neurotrophic remodelling accounting
  for persistence.'
evidence:
- reference: PMID:16626688
  reference_title: 18-Methoxycoronaridine acts in the medial habenula and/or interpeduncular nucleus to
    decrease morphine self-administration in rats.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Local administration of 18-MC into either the medial habenula or the interpeduncular area decreased
    morphine self-administration while having no effect on responding for a non-drug reinforcer (sucrose)
  explanation: Localizes the anti-opioid effect to the habenulo-interpeduncular pathway and shows it is
    not general response suppression.
- reference: PMID:16626688
  reference_title: 18-Methoxycoronaridine acts in the medial habenula and/or interpeduncular nucleus to
    decrease morphine self-administration in rats.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Local administration of 18-MC into the ventral tegmental area had no effect on morphine self-administration
  explanation: Negative control that separates this model's site of action from the VTA site invoked by
    the GDNF model.
- reference: PMID:17447255
  reference_title: 18-MC acts in the medial habenula and interpeduncular nucleus to attenuate dopamine
    sensitization to morphine in the nucleus accumbens.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: 18-MC had no effect on the dopamine response to acute morphine
  explanation: Restricts the proposed mechanism to sensitized rather than acute mesolimbic dopamine signalling,
    which is the state relevant to established dependence.
- reference: PMID:26022277
  reference_title: Coronaridine congeners inhibit human α3β4 nicotinic acetylcholine receptors by interacting
    with luminal and non-luminal sites.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: coronaridine congeners noncompetitively inhibit hα3β4 AChRs
  explanation: Supplies the receptor-level mechanism, while the reported potency ordering places noribogaine
    well below ibogaine and 18-MC, qualifying the model's applicability to the long-lived metabolite.
- reference: PMID:21040239
  reference_title: Noribogaine, but not 18-MC, exhibits similar actions as ibogaine on GDNF expression
    and ethanol self-administration.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: our results suggest that noribogaine and 18-MC have different mechanisms and sites of action
  explanation: Explicit statement that the congener used for most in vivo alpha3beta4 work does not share
    ibogaine's route, limiting transfer of this model to ibogaine.
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
**Generated:** 2026-08-28T04:27:44.704881

1. PMID:16626688
2. PMID:17447255
3. PMID:26022277
4. PMID:24750073
5. PMID:20485328
6. PMID:9668680
7. PMID:11085336
8. PMID:21040239
9. PMID:15659598
10. PMID:18541917
11. PMID:31005059
12. PMID:42217817
13. PMID:39270652
14. PMID:22278092
15. PMID:26256075
16. PMID:25689019
17. PMID:10556676
18. PMID:42038284
19. PMID:33299186