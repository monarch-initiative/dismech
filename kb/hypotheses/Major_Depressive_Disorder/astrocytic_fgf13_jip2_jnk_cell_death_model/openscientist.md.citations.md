# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Major Depressive Disorder
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** astrocytic_fgf13_jip2_jnk_cell_death_model
- **Hypothesis Label:** Astrocytic FGF13-JIP2-JNK Cell-Death Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: astrocytic_fgf13_jip2_jnk_cell_death_model
hypothesis_label: Astrocytic FGF13-JIP2-JNK Cell-Death Model
status: EMERGING
description: 'In stress-exposed male mouse hippocampus, reduced astrocytic FGF13 is proposed to permit
  MAPK8IP2/JIP2-associated JNK activation, shift BAX/BCL2 signaling toward apoptosis, increase inflammation,
  and reduce synaptic proteins, thereby worsening depression-like behavior. This is a model-supported
  hypothesis rather than an established human MDD mechanism: the human component is a secondary astrocyte
  transcriptomic association in an all-male suicide dorsolateral-prefrontal-cortex cohort, and older FHF-IB2
  biochemistry instead favored p38delta recruitment over JNK.'
evidence:
- reference: PMID:42421017
  reference_title: FGF13 alleviates astrocytic apoptosis via JIP2 inhibition in the hippocampus and mitigates
    depression-like behavior.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Astrocyte-specific knockout of FGF13 induces astrocytic apoptosis, exacerbates inflammatory
    levels, and aggravates depression-like behaviors in mice. In contrast, astrocyte-specific overexpression
    of FGF13 significantly attenuates both astrocyte apoptosis and inflammation, and effectively ameliorates
    depression-like behaviors.
  explanation: Bidirectional astrocyte-specific manipulation in stress-exposed mice supports a causal
    Fgf13-dependent phenotype in the model, but does not by itself establish an endogenous adult human
    MDD mechanism.
- reference: PMID:42421017
  reference_title: FGF13 alleviates astrocytic apoptosis via JIP2 inhibition in the hippocampus and mitigates
    depression-like behavior.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: FGF13 regulates apoptosis in primary astrocytes through the JIP2–JNK signaling pathway.
  explanation: Primary-astrocyte immunoblot experiments (reported at n=4 per group in the supplement)
    support the proposed signaling chain, although the small neonatal culture system does not establish
    its operation in adult human astrocytes.
- reference: PMID:42421017
  reference_title: FGF13 alleviates astrocytic apoptosis via JIP2 inhibition in the hippocampus and mitigates
    depression-like behavior.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: GSE144136 contains nuclei from the postmortem dorsolateral prefrontal cortex (dlPFC) of 17
    healthy controls (HC) and 17 patients with major depressive disorder (MDD) who died by suicide. All
    subjects were male.
  explanation: The secondary human transcriptomic analysis provides limited disease association, but its
    sex, cause-of-death, and cortical-region restrictions do not validate the hippocampal apoptosis mechanism
    or pathway activity.
- reference: PMID:12244047
  reference_title: Fibroblast growth factor homologous factors and the islet brain-2 scaffold protein
    regulate activation of a stress-activated protein kinase.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: FHF binding to IB2 facilitates recruitment of the MAPK p38delta (SAPK4), while failing to stimulate
    binding of JNK, the preferred kinase of the related scaffold IB1 (JIP-1).
  explanation: Earlier biochemical work confirms an FHF-IB2/JIP2 interaction but raises a direct pathway-specificity
    question because it favored p38delta, not JNK; this prevents treating the newer JIP2-JNK direction
    as settled.
notes: Curated as an emerging, model-specific hypothesis only. No new pathophysiology edge or FGF13/JIP2-directed
  treatment is asserted because adult human target engagement, causal mediation, and safety or efficacy
  evidence are absent.
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
**Generated:** 2026-07-26T06:02:04.139259

1. PMID:42421017
2. PMID:40566816
3. PMID:12244047
4. PMID:37217515
5. PMID:39332965
6. PMID:33109036
7. PMID:41611011
8. PMID:42309192
9. PMID:42436150
10. PMID:42320287
11. PMID:42271086
12. PMID:33245860
13. PMID:41545369
14. PMID:37705188
15. PMID:42092624
16. PMID:35195262
17. PMID:15863036
18. PMID:26063919
19. PMID:32150824
20. PMID:38468384
21. PMID:39773461
22. PMID:41014338
23. PMID:41218740
24. PMID:42189975
