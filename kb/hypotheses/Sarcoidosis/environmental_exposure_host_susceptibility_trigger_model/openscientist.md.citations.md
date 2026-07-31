# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Sarcoidosis
- **Category:** Immune

## Target Hypothesis
- **Hypothesis ID:** environmental_exposure_host_susceptibility_trigger_model
- **Hypothesis Label:** Environmental Exposure × Host Susceptibility Trigger Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: environmental_exposure_host_susceptibility_trigger_model
hypothesis_label: Environmental Exposure × Host Susceptibility Trigger Model
status: EMERGING
applies_to_subtypes:
- Pulmonary Sarcoidosis
description: Specific inhaled bioaerosols or inorganic particles may, in some susceptible hosts, initiate
  pulmonary sarcoidosis by engaging exposure-specific innate sensing or antigen-presentation programs
  that alter CD4+ T-cell polarization. HLA and other immune-risk alleles may modify these early responses
  and the resulting disease phenotype. This upstream trigger model complements the existing antigen-persistence/granuloma-chronicity
  model; it does not assert that distinct exposure classes share one receptor or causal pathway. The exposure-specific
  sensors, intermediates, and exposure-by-genotype combinations remain unresolved.
notes: Seed hypothesis for GitHub issue 6971. It requires disease-level OpenScientist research followed
  by a focused hypothesis investigation before any exposure-specific trigger edge or status change is
  curated.
evidence:
- reference: PMID:42471775
  reference_title: Current understanding of environmental exposures and sarcoidosis.
  supports: PARTIAL
  evidence_source: OTHER
  snippet: The identification of multiple exposures across different sarcoidosis manifestations suggests
    a possible gene-environment-phenotype relationship, which may explain some of the difficulty with
    identifying specific causes to date.
  explanation: This review motivates an exposure-by-host-susceptibility model while explicitly presenting
    the relationship as possible rather than causal.
- reference: PMID:19382531
  reference_title: HLA and environmental interactions in sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Significant interaction was observed between HLA DRB1*1101 and insecticide exposure at work
    (p < 0.10) and suggestive interaction was observed between HLA DRB1*1101 and exposure to mold and
    musty odors and DRB1*1501 and insecticide exposure at work (P < 0.15).
  explanation: The ACCESS case-control analysis provides exposure-by-HLA leads, but its exploratory significance
    thresholds and phenotype stratification require independent replication before these pairs are modeled
    as causal.
- reference: PMID:31126090
  reference_title: Genetic Variants Associated with FDNY WTC-Related Sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Seventeen allele variants of human leukocyte antigen (HLA) and non-HLA genes were found to
    be associated with sarcoidosis, and all were within chromosomes 1 and 6.
  explanation: The uniformly WTC-exposed case-control cohort supplies candidate susceptibility variants,
    but it cannot by itself establish a genotype-by-exposure interaction.
- reference: PMID:31126090
  reference_title: Genetic Variants Associated with FDNY WTC-Related Sarcoidosis.
  supports: REFUTE
  evidence_source: HUMAN_CLINICAL
  snippet: In our secondary analysis, we did not find statistical evidence of an interaction between common
    variants and the degree of WTC exposure.
  explanation: This small candidate-gene study did not detect effect modification by its WTC exposure-severity
    measure, directly constraining a dose-dependent gene-exposure claim.
- reference: PMID:30134122
  reference_title: IL-13-regulated Macrophage Polarization during Granuloma Formation in an In Vitro Human
    Sarcoidosis Model.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Compared with identically treated PBMCs of control subjects (n = 5), purified protein derivative-treated
    sarcoidosis PBMCs (n = 6) were distinguished by the formation of cellular aggregates resembling granulomas.
  explanation: Patient-cell responses to a putative mycobacterial antigen provide an experimental antigen-to-granuloma
    bridge, but the small in-vitro model does not identify an environmental trigger in vivo.
- reference: PMID:20813038
  reference_title: No evidence of altered alveolar macrophage polarization, but reduced expression of
    TLR2, in bronchoalveolar lavage cells in sarcoidosis.
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Overall, there was no evidence for alveolar macrophage polarization in sarcoidosis. However,
    there was a reduced TLR2 mRNA expression in patients with Löfgren's syndrome, which may be of relevance
    for macrophage interactions with a postulated sarcoidosis pathogen, and for the characteristics of
    the ensuing T cell response.
  explanation: Human bronchoalveolar data make TLR2 a phenotype-specific lead while directly cautioning
    against a uniform macrophage-polarization or PRR mechanism across sarcoidosis subtypes.
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
**Generated:** 2026-07-26T03:30:55.985074

1. PMID:33630763
2. PMID:20427584
3. PMID:24912188
4. PMID:20356827
5. PMID:19382531
6. PMID:25305207
7. PMID:20813038
8. PMID:15347561
9. PMID:41963075
10. PMID:41691440
11. PMID:22952805
12. PMID:26649486
13. PMID:34431542
14. PMID:30134122
15. PMID:31126090
16. PMID:17975675
17. PMID:22552860
18. PMID:32941653
19. PMID:32701676
20. PMID:41479893
21. PMID:41257857
22. PMID:41320317
23. PMID:22767391
