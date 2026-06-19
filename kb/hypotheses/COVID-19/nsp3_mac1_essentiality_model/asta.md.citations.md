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
- **Hypothesis ID:** nsp3_mac1_essentiality_model
- **Hypothesis Label:** Nsp3 Mac1 Macrodomain Essentiality Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: nsp3_mac1_essentiality_model
hypothesis_label: Nsp3 Mac1 Macrodomain Essentiality Model
status: CANONICAL
description: The SARS-CoV-2 Nsp3 macrodomain (Mac1) is a conserved coronavirus mono-ADP-ribosylhydrolase
  that is essential for pathogenesis. By hydrolyzing PARP9/DTX3L-deposited mono-ADP-ribose marks on host
  proteins, Mac1 neutralizes the effector branch of the host interferon antiviral program and is required
  for productive replication in vivo. This is the disease-level instantiation of the parp_parg_macrodomain_viral_evasion
  module's canonical countermeasure hypothesis.
evidence:
- reference: PMID:33158944
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Mac1 is essential for pathogenesis in multiple animal models of CoV infection
  explanation: In vivo essentiality across multiple coronavirus models directly supports the canonical
    Mac1 essentiality hypothesis.
- reference: PMID:34358560
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: the cellular function of the SARS-CoV-2 Nsp3 macrodomain is to hydrolyze this end product of
    IFN signaling, rather than to suppress the IFN response itself
  explanation: Russo et al. position Mac1 at the effector end of the IFN antiviral cascade, consistent
    with the canonical countermeasure model.
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
**Generated:** 2026-05-26T23:12:23.189814

1. S. Brock, David B Jackson, Theodoros G. Soldatos, K. Hornischer, Anne Schäfer et al. (2023). Whole patient knowledge modeling of COVID-19 symptomatology reveals common molecular mechanisms. Frontiers in Molecular Medicine. https://www.semanticscholar.org/paper/c4cb8ce50e078b71d83a74b18eef01fac0748cbe
2. Bingbo Wang, Xianan Dong, Jie Hu, Xiujuan Ma, Chao Han et al. (2021). The peripheral and core regions of virus-host network of COVID-19. Briefings in Bioinformatics. https://www.semanticscholar.org/paper/eab5ec5446a62abe1461e15c8ae2e15e7a267c8c
3. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Gathering Evidence of Mechanisms. https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
4. F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al. (2018). A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection. NPJ Systems Biology and Applications. https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
5. R. Leak, James B. Schreiber (2020). Mechanistic Research for the Student or Educator (Part I of II). Frontiers in Pharmacology. https://www.semanticscholar.org/paper/310d1cb284042ff6ce384dcc47b7f50a124237e7
6. Fuqiang Ban, Rahul Ravichandran, G. Correy, Oleksandra Herasymenko, Madhushika Silva et al. (2025). Structure-based discovery of inhibitors of Mac1 domain of nonstructural protein-3 of SARS-CoV-2 by machine learning-augmented screening of chemical space. bioRxiv. https://www.semanticscholar.org/paper/5cb90b48c50644b10a7e31328ed3e4647f47a71c
7. Francis E. Agamah, Thomas H. A. Ederveen, Michelle Skelton, Darren P. Martin, Emile R. Chimusa et al. (2023). Network-based integrative multi-omics approach reveals biosignatures specific to COVID-19 disease phases. Frontiers in Molecular Biosciences. https://www.semanticscholar.org/paper/17f9e0e3ecb026cc63a5d13c4917c27ea0253318
8. F. D. de Abajo, S. Rodríguez‐Martín, V. Lerma, G. Mejía-Abril, M. Aguilar et al. (2020). Use of renin–angiotensin–aldosterone system inhibitors and risk of COVID-19 requiring admission to hospital: a case-population study. Lancet (London, England). https://www.semanticscholar.org/paper/5ea714f2f9622f9030f104a7eb50b0b79b2f106b
9. Ernesto Estrada (2021). Cascading from SARS-CoV-2 to Parkinson’s Disease through Protein-Protein Interactions. Viruses. https://www.semanticscholar.org/paper/b012d46aba9b8899e9981dbebae70fc4c846474a
10. P. Thagard (2021). The cognitive science of COVID-19: Acceptance, denial, and belief change. Methods (San Diego, Calif.). https://www.semanticscholar.org/paper/76beb1dd87692e36d49120c0e07dfe80b6f8b8d9
11. A. De, M. Dash, A. Tiwari, A. Sinha (2021). Malaria, COVID-19 and angiotensin-converting enzyme 2: what does the available population data say?. Open Biology. https://www.semanticscholar.org/paper/5f3bcc1a04189b2360efd02fd025fed381d55eb9
12. Chun-Chi Liu, Y. Tseng, Wenyuan Li, Chia-Yu Wu, I. Mayzus et al. (2014). DiseaseConnect: a comprehensive web server for mechanism-based disease–disease connections. Nucleic Acids Research. https://www.semanticscholar.org/paper/164eec8e3e9af7dd3b1182e46be7577b90d44e1b
13. Anna Onisiforou, G. Spyrou (2022). Systems Bioinformatics Reveals Possible Relationship between COVID-19 and the Development of Neurological Diseases and Neuropsychiatric Disorders. Viruses. https://www.semanticscholar.org/paper/6db0f7d994622b5e960d5b8ae7cb402b584d9816
14. Barsha Saha, Majid Bani-Yaghoub, C. Podder (2026). Utility of compartmental models to test the competing hypotheses of pathogen evolution and human intervention. Frontiers in Public Health. https://www.semanticscholar.org/paper/749f3bc337708c7462f520ae5f06ceb914a49149
15. Yousef M. O. Alhammad, Srivatsan Parthasarathy, Roshan Ghimire, Catherine M. Kerr, J. O'Connor et al. (2023). SARS-CoV-2 Mac1 is required for IFN antagonism and efficient virus replication in cell culture and in mice. Proceedings of the National Academy of Sciences of the United States of America. https://www.semanticscholar.org/paper/4b95ed83758a296de204a9e74691af9fcbc4b92c
16. A. Imami, Robert E. Mccullumsmith, S. O’Donovan (2021). Strategies to identify candidate repurposable drugs: COVID-19 treatment as a case example. Translational Psychiatry. https://www.semanticscholar.org/paper/b4ae909dde0722a51145d2f7ff696e60cc99b17d
17. Aida Amini, Tom Hope, David Wadden, Madeleine van Zuylen, E. Horvitz et al. (2020). Extracting a Knowledge Base of Mechanisms from COVID-19 Papers. ArXiv. https://www.semanticscholar.org/paper/c4ce6aca9aed41d57d588674484932e0c2cd3547
