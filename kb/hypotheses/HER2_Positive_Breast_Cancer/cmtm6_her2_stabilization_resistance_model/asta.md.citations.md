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
- **Hypothesis ID:** cmtm6_her2_stabilization_resistance_model
- **Hypothesis Label:** CMTM6 HER2 Stabilization Resistance Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cmtm6_her2_stabilization_resistance_model
hypothesis_label: CMTM6 HER2 Stabilization Resistance Model
status: EMERGING
description: Trastuzumab resistance is sustained in part by post-translational stabilization of the HER2
  receptor protein at the cell surface. CMTM6 (CKLF-like MARVEL transmembrane domain-containing 6) directly
  interacts with HER2 and inhibits HER2 ubiquitination, preserving the GRB2-adaptor output even under
  trastuzumab pressure. Under the interactome- rebalancing framing, CMTM6 acts as a separate post-translational
  pivot point in parallel to GRB2 conformational state, and degrading or inhibiting CMTM6 may resensitize
  tumors to HER2-targeted therapy. This hypothesis is independent of (and complementary to) GRB2-level
  conformational control.
evidence:
- reference: PMID:36627608
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: these findings highlight that CMTM6 stabilizes HER2 protein, contributing to trastuzumab resistance
    and implicate CMTM6 as a potential prognostic marker and therapeutic target for overcoming trastuzumab
    resistance in HER2+ breast cancer
  explanation: Xu et al. directly establish CMTM6-mediated post-translational HER2 stabilization as a
    trastuzumab-resistance mechanism.
- reference: PMID:36627608
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: CMTM6 expression was upregulated in trastuzumab-resistant HER2+ breast cancer cell
  explanation: Co-localization, co-immunoprecipitation, and ubiquitination data link CMTM6 expression
    to the trastuzumab-resistant state.
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
**Generated:** 2026-05-26T23:19:07.703533

1. Veli-Pekka Parkkinen, Christian Wallmann, Michael Wilde, B. Clarke, P. Illari et al. (2018). Gathering Evidence of Mechanisms. https://www.semanticscholar.org/paper/06480fd932fc88915a4efb4c894a5ae4ed98452d
2. Eunhye Lee, A. Moon (2016). Identification of Biomarkers for Breast Cancer Using Databases. Journal of Cancer Prevention. https://www.semanticscholar.org/paper/9b33e30afc69380f4e374d30f12b9da9fc4ec013
3. Rossella Loria, P. Vici, F. S. Di Lisa, S. Soddu, M. Maugeri-Saccà et al. (2022). Cross-Resistance Among Sequential Cancer Therapeutics: An Emerging Issue. Frontiers in Oncology. https://www.semanticscholar.org/paper/cb43697914b25bbaa34869cbe04ffec4defb8ced
4. Whitney P. Kirschbrown, Bei Wang, Ihsan Nijem, A. Ohtsu, P. Hoff et al. (2019). Pharmacokinetic and exposure–response analysis of pertuzumab in patients with HER2-positive metastatic gastric or gastroesophageal junction cancer. Cancer Chemotherapy and Pharmacology. https://www.semanticscholar.org/paper/a492f9caf28f09d00f0c32bddf510e6551559553
5. Jack Freeman, R. Millikin, Leo Xu, Ishaan Sharma, Bethany Moore et al. (2025). SKiM-GPT: combining biomedical literature-based discovery with large language model hypothesis evaluation. BMC Bioinformatics. https://www.semanticscholar.org/paper/ce7a6900a181708dba6ed2bf612d06b0be1d20b1
6. T. Honkanen, Milla E. K. Luukkainen, Antti Tikkanen, P. Karihtala, Markus J. Mäkinen et al. (2021). Immune cell profiles of metastatic HER2-positive breast cancer patients according to the sites of metastasis. Breast Cancer Research and Treatment. https://www.semanticscholar.org/paper/f95f5f3008b0b18de39a4025a3d293e414e13fdc
7. T. Fujii, T. Kogawa, Jimin Wu, A. Sahin, Dian Liu et al. (2017). Nomogram to predict pathologic complete response in HER2-positive breast cancer treated with neoadjuvant systemic therapy. British Journal of Cancer. https://www.semanticscholar.org/paper/5dd1997db04466e24a85b0ce97b07fdd746e4ffa
8. C. Denkert, J. Huober, S. Loibl, J. Prinzler, R. Kronenwett et al. (2013). HER2 and ESR1 mRNA expression levels and response to neoadjuvant trastuzumab plus chemotherapy in patients with primary breast cancer. Breast Cancer Research : BCR. https://www.semanticscholar.org/paper/bbb3e4e5254ae4f1d7d01e34ceaa3294c787b51e
9. Magdalena Mileva, E. de Vries, T. Guiot, Z. Wimana, Anne-Leen Deleu et al. (2024). Molecular imaging predicts lack of T-DM1 response in advanced HER2-positive breast cancer (final results of ZEPHIR trial). NPJ Breast Cancer. https://www.semanticscholar.org/paper/0ff3a54a786d12f7955bb2b72f2d31f507472ecf
10. T. Fehm, S. Becker, S. Duerr-Stoerzer, K. Sotlar, V. Mueller et al. (2007). Determination of HER2 status using both serum HER2 levels and circulating tumor cells in patients with recurrent breast cancer whose primary tumor was HER2 negative or of unknown HER2 status. Breast cancer research : BCR. https://www.semanticscholar.org/paper/d978813f071eae7f40906131650b58285b8073bc
11. P. N. Lalagkas, R. Melamed (2024). Shared genetics between breast cancer and predisposing diseases identifies novel breast cancer treatment candidates. Human Genomics. https://www.semanticscholar.org/paper/5ed48d880dca9568260615e67fcb2cbd68c1bb3a
12. F. Langhauser, A. I. Casas, V. Dao, E. Guney, Jörg Menche et al. (2018). A diseasome cluster-based drug repurposing of soluble guanylate cyclase activators from smooth muscle relaxation to direct neuroprotection. NPJ Systems Biology and Applications. https://www.semanticscholar.org/paper/44d6cd1d0dd2993b9a9f6b17e3f9705fb04892b8
13. S. Riethdorf, V. Müller, Liling Zhang, T. Rau, S. Loibl et al. (2010). Detection and HER2 Expression of Circulating Tumor Cells: Prospective Monitoring in Breast Cancer Patients Treated in the Neoadjuvant GeparQuattro Trial. Clinical Cancer Research. https://www.semanticscholar.org/paper/e3e313d07b1e35bbcc2e79faa787d099a75d3ff3
14. Jie Zhang, Yan-Tao Yin, Chi Wu, Ronglin Qiu, Wenli Jiang et al. (2019). AK4 Promotes the Progression of HER2-Positive Breast Cancer by Facilitating Cell Proliferation and Invasion. Disease Markers. https://www.semanticscholar.org/paper/c51af8ad2760e81edb65d5bd78c40938244e28d1
15. A. Erickson, S. Habbous, Christianne Hoey, K. Jerzak, Sunit Das (2021). Dual- versus single-agent HER2 inhibition and incidence of intracranial metastatic disease: a systematic review and meta-analysis. NPJ Breast Cancer. https://www.semanticscholar.org/paper/6781ca0c03e097d469bae59ccc225f2a5e25ed6f
16. A. Erickson, S. Habbous, Christianne Hoey, K. Jerzak, Sunit Das (2021). Dual- versus single-agent HER2 inhibition and incidence of intracranial metastatic disease: a systematic review and meta-analysis. npj Breast Cancer. https://www.semanticscholar.org/paper/bb2940449df9cf69f1f5aab07fd1e518029d8a8d
17. Chun-Chi Liu, Y. Tseng, Wenyuan Li, Chia-Yu Wu, I. Mayzus et al. (2014). DiseaseConnect: a comprehensive web server for mechanism-based disease–disease connections. Nucleic Acids Research. https://www.semanticscholar.org/paper/164eec8e3e9af7dd3b1182e46be7577b90d44e1b
18. Noortje Verschoor, M. Bos, I. D. de Kruijff, M. Van, J. Kraan et al. (2024). Trastuzumab and first-line taxane chemotherapy in metastatic breast cancer patients with a HER2-negative tumor and HER2-positive circulating tumor cells: a phase II trial. Breast Cancer Research and Treatment. https://www.semanticscholar.org/paper/27666f62e949ba4071df10978655085b62820f45
