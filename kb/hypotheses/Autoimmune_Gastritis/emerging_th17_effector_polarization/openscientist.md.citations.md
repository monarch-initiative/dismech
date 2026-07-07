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
notes: 'A claude_code hypothesis-search report (kb/hypotheses/Autoimmune_Gastritis/emerging_th17_effector_polarization)
  graded this PARTIALLY SUPPORTED: the Th17/IL-17 mechanistic contribution is well established (H+/K+
  ATPase-specific gastric IL-17A/F production; IL-17RA signaling drives parietal-cell apoptosis; Th17
  transfer alone gives the most severe gastritis in the TxA23 model), but which effector arm dominates
  human disease is unresolved, Th1 remains the more extensively validated axis, and IL-17 can be protective
  in H. pylori-associated gastric carcinogenesis (IL-17RA-deficient mice develop gastric cancer faster),
  cautioning against a simple "block IL-17" therapeutic inference; no human anti-IL-17 data exist in AIG.
  Retained EMERGING. Run performed with the claude_code provider; an openscientist run is pending.'
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
**Generated:** 2026-07-01T16:33:30.602581

1. PMID:35911678
2. PMID:31080562
3. PMID:18641328
4. PMID:40471463
5. PMID:12645953
6. PMID:19050237
7. PMID:19539565
8. PMID:15242679
9. PMID:38639570
10. PMID:38014948
11. PMID:18928529
12. PMID:23277173
13. PMID:27259856
14. PMID:14978094
15. PMID:17671757
16. PMID:19812196
17. PMID:18200634
18. PMID:23299619
19. PMID:19166417
20. PMID:18948106
21. PMID:34145262
22. PMID:10963131
23. PMID:27183623
24. PMID:39837221