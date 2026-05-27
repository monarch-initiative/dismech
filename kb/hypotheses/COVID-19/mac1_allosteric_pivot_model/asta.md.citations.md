# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** COVID-19
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** mac1_allosteric_pivot_model
- **Hypothesis Label:** Mac1 Allosteric Conformational Pivot Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: mac1_allosteric_pivot_model
hypothesis_label: Mac1 Allosteric Conformational Pivot Model
status: EMERGING
description: The conserved Mac1 fold across coronaviruses (SARS-CoV-2, SARS-CoV, MERS-CoV) supports treating
  Mac1 as a thermodynamic pivot point rather than only an active-site target. Allosteric stabilization
  of distinct Mac1 conformational states or PROTAC-based physical degradation would rebalance the host
  interactome toward antiviral ADP-ribosylation, with potential broad anti-coronavirus activity that active-site
  inhibition alone may not achieve.
evidence:
- reference: PMID:33158944
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: SARS-CoV-2, SARS-CoV, and Middle East respiratory syndrome coronavirus (MERS-CoV) Mac1 domains
    exhibit similar structural folds, and all 3 proteins bound to ADP-ribose with affinities in the low
    micromolar range
  explanation: Structural conservation of Mac1 across coronaviruses supports the feasibility of a pan-CoV
    pivot-control strategy beyond active-site inhibition.
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

**Provider:** asta
**Generated:** 2026-05-26T23:12:53.056892

1. S. Brock, David B Jackson, Theodoros G. Soldatos, K. Hornischer, Anne Schäfer et al. (2023). Whole patient knowledge modeling of COVID-19 symptomatology reveals common molecular mechanisms. Frontiers in Molecular Medicine. https://www.semanticscholar.org/paper/c4cb8ce50e078b71d83a74b18eef01fac0748cbe
2. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Gathering Evidence of Mechanisms. https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
3. F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al. (2018). A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection. NPJ Systems Biology and Applications. https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
4. F. D. de Abajo, S. Rodríguez‐Martín, V. Lerma, G. Mejía-Abril, M. Aguilar et al. (2020). Use of renin–angiotensin–aldosterone system inhibitors and risk of COVID-19 requiring admission to hospital: a case-population study. Lancet (London, England). https://www.semanticscholar.org/paper/5ea714f2f9622f9030f104a7eb50b0b79b2f106b
5. Bingbo Wang, Xianan Dong, Jie Hu, Xiujuan Ma, Chao Han et al. (2021). The peripheral and core regions of virus-host network of COVID-19. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/eab5ec5446a62abe1461e15c8ae2e15e7a267c8c
6. P. Thagard (2021). The cognitive science of COVID-19: Acceptance, denial, and belief change. Methods (San Diego, Calif.). https://www.semanticscholar.org/paper/76beb1dd87692e36d49120c0e07dfe80b6f8b8d9
7. Francis E. Agamah, Thomas H. A. Ederveen, Michelle Skelton, Darren P. Martin, Emile R. Chimusa et al. (2023). Network-based integrative multi-omics approach reveals biosignatures specific to COVID-19 disease phases. Frontiers in Molecular Biosciences. https://www.semanticscholar.org/paper/17f9e0e3ecb026cc63a5d13c4917c27ea0253318
8. G. Vavougios, G. A. de Erausquin, H. Snyder (2022). Type I interferon signaling in SARS-CoV-2 associated neurocognitive disorder (SAND): Mapping host-virus interactions to an etiopathogenesis. Frontiers in Neurology. https://www.semanticscholar.org/paper/b12780ce3683c282a128917b0bdbc13fd2798ab6
9. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Evaluating Evidence of Mechanisms. https://www.semanticscholar.org/paper/3329d810339c68716085aed1bc85c5b56838b361
10. Barsha Saha, Majid Bani-Yaghoub, C. Podder (2026). Utility of compartmental models to test the competing hypotheses of pathogen evolution and human intervention. Frontiers in Public Health. https://www.semanticscholar.org/paper/749f3bc337708c7462f520ae5f06ceb914a49149
11. Ernesto Estrada (2021). Cascading from SARS-CoV-2 to Parkinson’s Disease through Protein-Protein Interactions. Viruses. https://www.semanticscholar.org/paper/b012d46aba9b8899e9981dbebae70fc4c846474a
12. A. De, M. Dash, A. Tiwari, A. Sinha (2021). Malaria, COVID-19 and angiotensin-converting enzyme 2: what does the available population data say?. Open Biology. https://www.semanticscholar.org/paper/5f3bcc1a04189b2360efd02fd025fed381d55eb9
13. Anna Onisiforou, G. Spyrou (2022). Systems Bioinformatics Reveals Possible Relationship between COVID-19 and the Development of Neurological Diseases and Neuropsychiatric Disorders. Viruses. https://www.semanticscholar.org/paper/6db0f7d994622b5e960d5b8ae7cb402b584d9816
14. J. Li, Xin Tong (2020). Statistical Hypothesis Testing versus Machine Learning Binary Classification: Distinctions and Guidelines. Patterns. https://www.semanticscholar.org/paper/60ef10665e62aafb9c0990148c79aa619b55eede
15. Christophe Gerard Lambert, L. Black (2012). Learning from our GWAS mistakes: from experimental design to scientific method. Biostatistics (Oxford, England). https://www.semanticscholar.org/paper/7c92a4bffd527e9275e5dbc57e2037bc07fa93f9
16. A. Ruttenberg, Tim Clark, W. Bug, M. Samwald, O. Bodenreider et al. (2007). Advancing translational research with the Semantic Web. BMC Bioinformatics. https://www.semanticscholar.org/paper/a363cd9efbc0b28d0c04241ad998b90207cbcb11
17. A. Imami, Robert E. Mccullumsmith, S. O’Donovan (2021). Strategies to identify candidate repurposable drugs: COVID-19 treatment as a case example. Translational Psychiatry. https://www.semanticscholar.org/paper/b4ae909dde0722a51145d2f7ff696e60cc99b17d
