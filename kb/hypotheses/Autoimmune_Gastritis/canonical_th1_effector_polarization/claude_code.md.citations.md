# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Autoimmune Gastritis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_th1_effector_polarization
- **Hypothesis Label:** Canonical Th1/IFN-gamma Effector Polarization
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_th1_effector_polarization
hypothesis_label: Canonical Th1/IFN-gamma Effector Polarization
status: CANONICAL
description: The effector arm driving parietal-cell destruction has classically been modeled as Th1/IFN-gamma-polarized,
  based on murine neonatal-thymectomy and TCR-transgenic effector-transfer systems specific for the H+/K+
  ATPase.
evidence:
- reference: PMID:18641328
  reference_title: Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological
    pattern and in susceptibility to suppression by regulatory T cells.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We have evaluated the capacity of fully differentiated Th1, Th2, and Th17 cells derived from
    a mouse bearing a transgenic TCR specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,
    to induce autoimmune gastritis after transfer to immunodeficient recipients.
  explanation: Effector-transfer model in which Th1 (among other subsets) specific for the H+/K+ ATPase
    induces autoimmune gastritis.
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

**Provider:** claude_code
**Generated:** 2026-07-01T08:03:18.729534

1. https://pubmed.ncbi.nlm.nih.gov/18641328/
2. https://pubmed.ncbi.nlm.nih.gov/22777705/
3. https://pubmed.ncbi.nlm.nih.gov/15763992/
4. https://pubmed.ncbi.nlm.nih.gov/35911678/
5. https://pubmed.ncbi.nlm.nih.gov/31080562/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC2194239/
7. https://www.ncbi.nlm.nih.gov/books/NBK2439/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC11347309/
10. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full
11. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8213695/
12. https://pubmed.ncbi.nlm.nih.gov/37504250/