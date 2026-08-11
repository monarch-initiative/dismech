# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Metastatic Pancreatic Adenocarcinoma
- **Category:** 

## Target Hypothesis
- **Hypothesis ID:** ras_on_inhibitor_acquired_resistance
- **Hypothesis Label:** Acquired Resistance to RAS(ON) Multiselective Inhibition
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ras_on_inhibitor_acquired_resistance
hypothesis_label: Acquired Resistance to RAS(ON) Multiselective Inhibition
status: EMERGING
description: In RASolute 302 essentially all patients eventually progressed on daraxonrasib (median progression-free
  survival 7.3 months in the RAS G12 population), implying that metastatic PDAC reliably acquires resistance
  to RAS(ON) multiselective, tri-complex inhibition. The molecular basis of that escape is unresolved
  for this drug class. Candidate mechanisms to evaluate include reactivation of RAS-MAPK signaling through
  receptor tyrosine kinase and feedback loops (e.g., EGFR, FGFR, SHP2/PTPN11) that restore downstream
  ERK activity despite RAS(ON) engagement; secondary or on-target RAS alterations and KRAS amplification
  that raise the inhibition threshold; bypass through PI3K-AKT-mTOR signaling; and adaptive transcriptional
  or lineage plasticity. Distinguishing which routes dominate, and whether they are pre-existing or selected
  under treatment, would define rational combination and sequencing strategies.
evidence:
- reference: PMID:42223072
  reference_title: Daraxonrasib or Chemotherapy in Previously Treated Metastatic Pancreatic Cancer.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The median progression-free survival in the RAS G12 population was 7.3 months with daraxonrasib
    and 3.5 months with chemotherapy, and that in the overall population was 7.2 months and 3.6 months,
    respectively; the hazard ratios were 0.45 and 0.49, respectively (P<0.001 for both comparisons).
  explanation: The finite progression-free survival on daraxonrasib establishes that acquired resistance
    to RAS(ON) inhibition emerges in previously treated metastatic PDAC; the responsible mechanism is
    the open question this hypothesis frames.
notes: Seed hypothesis for OpenScientist deep-research exploration of RAS(ON) inhibitor resistance mechanisms.
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
**Generated:** 2026-07-24T01:28:18.090810

1. PMID:42223072
2. PMID:42090791
3. PMID:41165456
4. PMID:36355783
5. PMID:25736685
6. PMID:42465359
7. PMID:40713971
8. PMID:41959066
9. PMID:41572361
10. PMID:39586491
11. PMID:41545339
12. PMID:42465401
13. PMID:40057911
14. PMID:32194992
15. PMID:40966362
16. PMID:42226005