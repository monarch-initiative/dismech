# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** HER2-Positive Breast Cancer
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** grb2_conformational_pivot_resistance_model
- **Hypothesis Label:** GRB2 Conformational Pivot Resistance Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: grb2_conformational_pivot_resistance_model
hypothesis_label: GRB2 Conformational Pivot Resistance Model
status: EMERGING
description: GRB2 is a thermodynamic pivot point whose conformational state determines whether HER2-driven
  tumors funnel into cytoplasmic effector dominance, nuclear RAD51-dependent replication-fork protection,
  or PARPi-STING innate-immune activation. Allosteric stabilization or PROTAC degradation of GRB2 would
  select between these interactome states and modulate trastuzumab/TKI resistance. This hypothesis is
  distinguishable from the canonical effector model by predicting that GRB2 perturbation produces different
  phenotypes depending on which conformational state is locked, not simply graded loss of adaptor function.
evidence:
- reference: PMID:38459011
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Growth factor receptor-bound protein 2 (GRB2) is a cytoplasmic adapter for tyrosine kinase
    signaling and a nuclear adapter for homology-directed-DNA repair.
  explanation: Dual cytoplasmic/nuclear GRB2 framing motivates the conformational-pivot hypothesis as
    distinct from the canonical effector model.
- reference: PMID:38459011
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: In GRB2-depleted cells, PARP inhibitor (PARPi) treatment releases DNA fragments from stalled
    forks into the cytoplasm that activate the cGAS-STING pathway to trigger pro-inflammatory cytokine
    production.
  explanation: Experimental demonstration that loss of GRB2 fork-protection function produces a distinct
    PARPi-STING vulnerability supports the pivot framing.
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
**Generated:** 2026-05-26T23:12:53.534041

1. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Gathering Evidence of Mechanisms. https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
2. F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al. (2018). A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection. NPJ Systems Biology and Applications. https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
3. Jack Freeman, R. Millikin, Leo Xu, Ishaan Sharma, Bethany Moore et al. (2025). SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation. BMC Bioinformatics. https://www.semanticscholar.org/paper/ce7a6900a181708dba6ed2bf612d06b0be1d20b1
4. P. N. Lalagkas, R. Melamed (2024). Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates. Human Genomics. https://www.semanticscholar.org/paper/5ed48d880dca9568260615e67fcb2cbd68c1bb3a
5. Eunhye Lee, A. Moon (2016). Identification of Biomarkers for Breast Cancer Using Databases. Journal of Cancer Prevention. https://www.semanticscholar.org/paper/9b33e30afc69380f4e374d30f12b9da9fc4ec013
6. P. N. Lalagkas, R. Melamed (2024). Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates. Research Square. https://www.semanticscholar.org/paper/3f4729126c3c31a61b5f2d6714f1632ac55aa27a
7. Rossella Loria, P. Vici, F. S. Di Lisa, S. Soddu, M. Maugeri-Saccà et al. (2022). Cross-Resistance Among Sequential Cancer Therapeutics: An Emerging Issue. Frontiers in Oncology. https://www.semanticscholar.org/paper/cb43697914b25bbaa34869cbe04ffec4defb8ced
8. T. Honkanen, Milla E. K. Luukkainen, Antti Tikkanen, P. Karihtala, Markus J. Mäkinen et al. (2021). Immune cell profiles of metastatic HER2-positive breast cancer patients according to the sites of metastasis. Breast Cancer Research and Treatment. https://www.semanticscholar.org/paper/f95f5f3008b0b18de39a4025a3d293e414e13fdc
9. Chun-Chi Liu, Y. Tseng, Wenyuan Li, Chia-Yu Wu, I. Mayzus et al. (2014). DiseaseConnect: a comprehensive web server for mechanism-based disease–disease connections. Nucleic Acids Research. https://www.semanticscholar.org/paper/164eec8e3e9af7dd3b1182e46be7577b90d44e1b
10. Reyk Hillert, Anne Gieseler, Andreas Krusche, D. Humme, H.-J. Röwert-Huber et al. (2016). Large molecular systems landscape uncovers T cell trapping in human skin cancer. Scientific Reports. https://www.semanticscholar.org/paper/33de2062cfd1ed11b827368d31223ecb21fac495
11. Christophe Gerard Lambert, L. Black (2012). Learning from our GWAS mistakes: from experimental design to scientific method. Biostatistics (Oxford, England). https://www.semanticscholar.org/paper/7c92a4bffd527e9275e5dbc57e2037bc07fa93f9
12. Whitney P. Kirschbrown, Bei Wang, Ihsan Nijem, A. Ohtsu, P. Hoff et al. (2019). Pharmacokinetic and exposure–response analysis of pertuzumab in patients with HER2-positive metastatic gastric or gastroesophageal junction cancer. Cancer Chemotherapy and Pharmacology. https://www.semanticscholar.org/paper/a492f9caf28f09d00f0c32bddf510e6551559553
13. Liam V. Brown, J. Wagg, R. Darley, Andy van Hateren, Tim Elliott et al. (2022). De-risking clinical trial failure through mechanistic simulation. Immunotherapy Advances. https://www.semanticscholar.org/paper/231e07df51f980fbee090257094d32e95722e73e
14. Vinod Kumar, P. Sanseau, D. Simola, M. Hurle, Pankaj Agarwal (2016). Systematic Analysis of Drug Targets Confirms Expression in Disease-Relevant Tissues. Scientific Reports. https://www.semanticscholar.org/paper/afe28e41430a6602a7e0d0c0c1e94356bd3a534a
15. Marco Fernandes, H. Husi (2019). Integrative Systems Biology Resources and Approaches in Disease Analytics. Systems Biology. https://www.semanticscholar.org/paper/b6360f094840c900e0116b69fe90daebe3161325
16. E. Efstathiou, A. Merseburger, A. Liew, K. Kurtyka, O. Panda et al. (2024). Perception of cure in prostate cancer: human-led and artificial intelligence-assisted landscape review and linguistic analysis of literature, social media and policy documents. ESMO Open. https://www.semanticscholar.org/paper/fb81df75cf8787f5fec559887b77f5ba6d75837f
17. M. Pereda, Ernesto Estrada (2018). Machine Learning Analysis of Complex Networks in Hyperspherical Space. arXiv: Physics and Society. https://www.semanticscholar.org/paper/a21feb31b53b4c5b59520b175884e15949582073
18. Rubén Romero-Córdoba, J. Olivas, F. P. Romero, Francisco Alonso-Gómez, J. Serrano-Guerrero (2017). An Application of Fuzzy Prototypes to the Diagnosis and Treatment of Fuzzy Diseases. International Journal of Intelligent Systems. https://www.semanticscholar.org/paper/36623f163659f9e4d1cf968252e10e36faa19676
