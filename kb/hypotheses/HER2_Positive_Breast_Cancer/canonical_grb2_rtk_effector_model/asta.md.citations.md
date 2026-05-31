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
- **Hypothesis ID:** canonical_grb2_rtk_effector_model
- **Hypothesis Label:** Canonical HER2-GRB2 RTK Effector Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_grb2_rtk_effector_model
hypothesis_label: Canonical HER2-GRB2 RTK Effector Model
status: CANONICAL
description: Constitutively activated HER2 receptors create phosphotyrosine docking sites that recruit
  GRB2 adaptor complexes, coupling receptor activation to canonical RAS-MAPK and PI3K-AKT proliferative
  signaling. This is the textbook HER2+ breast cancer signaling cascade and the explicit disease-level
  instantiation of the rtk_grb2_signaling_adaptation module's canonical effector hypothesis.
evidence:
- reference: PMID:28058850
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Signaling by FGFR4 and other fibroblast growth factor receptors involves tyrosine phosphorylation
    of the receptor carboxyl terminus along with other substrates, such as FRS2, recruitment of the GRB2
    adaptor, and activation of the downstream RAS and phosphoinositide 3-kinase pathways.
  explanation: Review evidence supports the canonical RTK-to-GRB2-to-RAS/PI3K architecture that HER2+
    breast cancer instantiates.
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
**Generated:** 2026-05-26T23:12:26.883498

1. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Gathering Evidence of Mechanisms. https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
2. Zilin Xianyu, Cristina Correia, C. Ung, Shizhen Zhu, D. Billadeau et al. (2024). The Rise of Hypothesis-Driven Artificial Intelligence in Oncology. Cancers. https://www.semanticscholar.org/paper/f05721d59597ea5471ac85617fda99b4e73fb936
3. Eunhye Lee, A. Moon (2016). Identification of Biomarkers for Breast Cancer Using Databases. Journal of Cancer Prevention. https://www.semanticscholar.org/paper/9b33e30afc69380f4e374d30f12b9da9fc4ec013
4. Rossella Loria, P. Vici, F. S. Di Lisa, S. Soddu, M. Maugeri-Saccà et al. (2022). Cross-Resistance Among Sequential Cancer Therapeutics: An Emerging Issue. Frontiers in Oncology. https://www.semanticscholar.org/paper/cb43697914b25bbaa34869cbe04ffec4defb8ced
5. F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al. (2018). A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection. NPJ Systems Biology and Applications. https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
6. Jack Freeman, R. Millikin, Leo Xu, Ishaan Sharma, Bethany Moore et al. (2025). SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation. BMC Bioinformatics. https://www.semanticscholar.org/paper/ce7a6900a181708dba6ed2bf612d06b0be1d20b1
7. P. N. Lalagkas, R. Melamed (2024). Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates. Human Genomics. https://www.semanticscholar.org/paper/5ed48d880dca9568260615e67fcb2cbd68c1bb3a
8. R. Gaire, Lorey K. Smith, P. Humbert, James Bailey, Peter James Stuckey et al. (2013). Discovery and analysis of consistent active sub-networks in cancers. BMC Bioinformatics. https://www.semanticscholar.org/paper/1ba07521863c145402c23fba5ba4c92e5905e58b
9. D. Ochoa, Andrew Hercules, M. Carmona, D. Suveges, Jarrod Baker et al. (2022). The next-generation Open Targets Platform: reimagined, redesigned, rebuilt. Nucleic Acids Research. https://www.semanticscholar.org/paper/1eb72ef89e6b7722e114e195f68cd45c86e6f344
10. Whitney P. Kirschbrown, Bei Wang, Ihsan Nijem, A. Ohtsu, P. Hoff et al. (2019). Pharmacokinetic and exposure–response analysis of pertuzumab in patients with HER2-positive metastatic gastric or gastroesophageal junction cancer. Cancer Chemotherapy and Pharmacology. https://www.semanticscholar.org/paper/a492f9caf28f09d00f0c32bddf510e6551559553
11. Hailing Cheng, Pixu Liu, Carolynn E. Ohlson, Erbo Xu, Lynn K Symonds et al. (2015). PIK3CAH1047R and Her2 initiated mammary tumors escape PI3K dependency by compensatory activation of MEK-ERK signaling. Oncogene. https://www.semanticscholar.org/paper/fa9ef1dd841484add71630de5ac5f5647503006f
12. T. Honkanen, Milla E. K. Luukkainen, Antti Tikkanen, P. Karihtala, Markus J. Mäkinen et al. (2021). Immune cell profiles of metastatic HER2-positive breast cancer patients according to the sites of metastasis. Breast Cancer Research and Treatment. https://www.semanticscholar.org/paper/f95f5f3008b0b18de39a4025a3d293e414e13fdc
13. Reyk Hillert, Anne Gieseler, Andreas Krusche, D. Humme, H.-J. Röwert-Huber et al. (2016). Large molecular systems landscape uncovers T cell trapping in human skin cancer. Scientific Reports. https://www.semanticscholar.org/paper/33de2062cfd1ed11b827368d31223ecb21fac495
14. A. Oulas, Kyriaki Savva, Nestoras Karathanasis, George M. Spyrou (2023). Ranking of cell clusters in a single-cell RNA-sequencing analysis framework using prior knowledge. PLOS Computational Biology. https://www.semanticscholar.org/paper/efaf940a9b0405a5405ebf033673f32b3a1268df
15. A. Bugrim (2023). Identification of disease mechanisms and novel disease genes using clinical concept embeddings learned from massive amounts of biomedical data. bioRxiv. https://www.semanticscholar.org/paper/ee810c8e4db715b5333cf89bf7034bfcaf424245
16. Lang Qin, Z. Gan, Xu Cao, Pengcheng Jiang, Yankai Jiang et al. (2025). RareAgent: Self-Evolving Reasoning for Drug Repurposing in Rare Diseases. ArXiv. https://www.semanticscholar.org/paper/ad0dc7cd9de3e46fb22cc025706d54dfe58331a0
17. Marco Fernandes, H. Husi (2019). Integrative Systems Biology Resources and Approaches in Disease Analytics. Systems Biology. https://www.semanticscholar.org/paper/b6360f094840c900e0116b69fe90daebe3161325
18. Zifeng Wang, Zheng Chen, Ziwei Yang, Xuan Wang, Qiao Jin et al. (2025). DeepEvidence: Empowering Biomedical Discovery with Deep Knowledge Graph Research. ArXiv. https://www.semanticscholar.org/paper/f06a59cb27b36766098ecb235c9ada048e145ed0
