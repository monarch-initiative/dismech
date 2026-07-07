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
- **Hypothesis ID:** emerging_th17_effector_polarization
- **Hypothesis Label:** Emerging Th17/IL-17 Effector Contribution
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: emerging_th17_effector_polarization
hypothesis_label: Emerging Th17/IL-17 Effector Contribution
status: EMERGING
description: Human data show a gastric H+/K+ ATPase-specific Th17/IL-17 signature, and effector-transfer
  models show that Th1, Th2, and Th17 cells can each induce autoimmune gastritis with distinct pathology
  and differing susceptibility to regulatory T-cell suppression. Which effector arm dominates human disease,
  and whether it shifts over the disease course, is unresolved and carries therapeutic implications (e.g.,
  anti-IL-17 blockade).
evidence:
- reference: PMID:35911678
  reference_title: Gastric Th17 Cells Specific for H+/K+-ATPase and Serum IL-17 Signature in Gastric Autoimmunity.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Gastric LPMCs from all AIG patients, but not those from HCs, were activated by H+/K+-ATPase
    and were able to proliferate and produce high levels of IL-17A and IL-17F.
  explanation: Human gastric T cells produce IL-17A/IL-17F on H+/K+ ATPase stimulation, evidencing a Th17
    effector contribution.
- reference: PMID:18641328
  reference_title: Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological
    pattern and in susceptibility to suppression by regulatory T cells.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We have evaluated the capacity of fully differentiated Th1, Th2, and Th17 cells derived from
    a mouse bearing a transgenic TCR specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,
    to induce autoimmune gastritis after transfer to immunodeficient recipients.
  explanation: Th17 effector cells can independently induce autoimmune gastritis in the transfer model,
    supporting an emerging Th17 arm.
- reference: PMID:31080562
  reference_title: Intrinsic factor recognition promotes T helper 17/T helper 1 autoimmune gastric inflammation
    in patients with pernicious anemia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Most of these clones (94%) showed a T helper 17 or T helper 1 profile.
  explanation: In pernicious anemia, intrinsic-factor-specific gastric CD4 clones are predominantly Th17/Th1
    (Th17-skewed), evidencing a Th17 contribution in the intrinsic-factor-reactive compartment.
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
**Generated:** 2026-07-01T14:13:13.539858

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC9328118
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2561289/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6499598/
4. https://pubmed.ncbi.nlm.nih.gov/29930985/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC11639209/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC11638189/
7. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1450558/full
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/
9. https://link.springer.com/article/10.1007/s12026-025-09643-4
10. https://www.tandfonline.com/doi/full/10.1080/08916934.2023.2174531