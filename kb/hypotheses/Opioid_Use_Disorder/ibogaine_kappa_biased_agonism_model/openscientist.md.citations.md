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
- **Hypothesis ID:** ibogaine_kappa_biased_agonism_model
- **Hypothesis Label:** Noribogaine G-protein-biased kappa-opioid agonism model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ibogaine_kappa_biased_agonism_model
hypothesis_label: Noribogaine G-protein-biased kappa-opioid agonism model
status: EMERGING
description: 'Proposes that the anti-opioid action of ibogaine is carried principally by noribogaine''s
  G-protein-biased agonism at the kappa-opioid receptor, with weak mu-opioid antagonism as a secondary
  contributor. Bias away from beta-arrestin recruitment is invoked to explain why the compound lacks the
  dysphoria of conventional kappa agonists, and functional inhibition of dynorphin-driven beta-arrestin
  signalling is invoked to explain relief of the hyperkatifeia/anti-reward state. The strongest support
  is structural rather than loss-of-function: iboga analogues engineered as potent kappa agonists retain
  long-lasting suppression of opioid intake and reverse opioid-induced hyperalgesia while shedding the
  cardiac liability. That establishes kappa agonism as sufficient in rodents, not that ibogaine itself
  acts through kappa.'
notes: 'Distinguishing test: a selective kappa antagonist, or a kappa-receptor knockout, should abolish
  ibogaine''s suppression of opioid self-administration if this model holds. Note also that the micromolar
  affinities involved mean the model depends on brain concentrations actually reached at therapeutic doses,
  which is where the CYP2D6-driven exposure variability becomes mechanistically relevant rather than merely
  a safety issue.'
evidence:
- reference: PMID:26302653
  reference_title: Noribogaine is a G-protein biased κ-opioid receptor agonist.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: noribogaine was a G-protein biased kappa agonist 75% as efficacious as dynorphin A at stimulating
    GDP-GTP exchange
  explanation: Characterizes the biased kappa pharmacology the model is built on.
- reference: PMID:26302653
  reference_title: Noribogaine is a G-protein biased κ-opioid receptor agonist.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Noribogaine was a weak mu antagonist with a functional inhibition constants (Ke) of 20 μM at
    the G-protein and β-arrestin signaling pathways
  explanation: Constrains the mu contribution to weak antagonism, which argues against withdrawal relief
    being explained by opioid-agonist substitution.
- reference: PMID:7796150
  reference_title: Radioligand-binding study of noribogaine, a likely metabolite of ibogaine.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Noribogaine showed a higher affinity than ibogaine for all of the opioid receptors
  explanation: Supports assigning the opioid-receptor component of the effect to the long-lived metabolite
    rather than the parent drug.
- reference: PMID:39304653
  reference_title: Oxa-Iboga alkaloids lack cardiac risk and disrupt opioid use in animal models.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: Oxa-noribogaine induces long-lasting suppression of morphine, heroin, and fentanyl intake after
    a single dose or a short treatment regimen, reversal of persistent opioid-induced hyperalgesia, and
    suppression of opioid drug seeking in rodent relapse models
  explanation: Shows kappa-agonist iboga analogues are sufficient to produce the target behavioural effect,
    without establishing that ibogaine acts through kappa.
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
**Generated:** 2026-08-28T04:29:44.838594

1. PMID:26302653
2. PMID:24204784
3. PMID:7796150
4. PMID:38519421
5. PMID:15178360
6. PMID:12801235
7. PMID:30216039
8. PMID:15659598
9. PMID:9685673
10. PMID:26807959
11. PMID:10506904
12. PMID:28402682
13. PMID:19716811
14. PMID:38649428
15. PMID:39019223
16. PMID:32894343
17. PMID:33299186
18. PMID:41424776
19. PMID:39304653
20. PMID:34843875
21. PMID:28656735
22. PMID:23101464
23. PMID:37177778
24. PMID:35513117
25. PMID:39833376