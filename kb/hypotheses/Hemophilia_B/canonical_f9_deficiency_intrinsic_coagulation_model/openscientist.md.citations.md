# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hemophilia B
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_f9_deficiency_intrinsic_coagulation_model
- **Hypothesis Label:** Canonical F9 Deficiency / Intrinsic Coagulation Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_f9_deficiency_intrinsic_coagulation_model
hypothesis_label: Canonical F9 Deficiency / Intrinsic Coagulation Failure Model
status: CANONICAL
description: Hemophilia B (Christmas disease) is caused by loss-of-function variants in F9 on Xq27.1 encoding
  coagulation factor IX (FIX). FIX is activated to FIXa by the FVIIa/tissue-factor complex and by FXIa,
  then partners with FVIIIa on activated platelet membranes as the intrinsic tenase complex to activate
  factor X. Loss of FIX activity disables propagation of the intrinsic pathway, abolishes the thrombin
  burst, and produces severe spontaneous joint, soft-tissue, and CNS bleeding analogous to hemophilia
  A. FIX replacement therapy (recombinant or plasma-derived), extended-half-life Fc/albumin-fusion FIX,
  and AAV-mediated F9 gene therapy (etranacogene dezaparvovec, fidanacogene elaparvovec) all support the
  F9-deficiency-as-rate-limiting-lesion model by restoring FIX activity and hemostatic competence.
evidence:
- reference: PMID:23430394
  reference_title: 'Hemophilia B: where are we now and what does the future hold?'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Hemophilia B is a recessive X-linked bleeding disorder characterized by deficiency of the coagulation
    factor IX (FIX).
  explanation: |
    Canonical mechanism reference used as the seed for the hypothesis-search deep-research run.
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
**Generated:** 2026-05-23T21:53:07.494491

1. PMID:31499529
2. PMID:41358585
3. PMID:38437857
4. PMID:40188458
5. PMID:39321362
6. PMID:40239068
7. PMID:41110511
8. PMID:23472758
9. PMID:1631121
10. PMID:8499951
11. PMID:40053895
12. PMID:33587824
13. PMID:33570646
14. PMID:40515600
15. PMID:33656538
16. PMID:31219805
17. PMID:19686262
18. PMID:15230944
19. PMID:28550758
20. PMID:18624700
21. PMID:33082527
22. PMID:24533955
23. PMID:36163649
24. PMID:29925096
25. PMID:23601006
26. PMID:11545609
27. PMID:28508290
28. PMID:32775489
29. PMID:34649996
30. PMID:22123568
31. PMID:21707870
32. PMID:38700550
33. PMID:36407152
34. PMID:39613145
35. PMID:34117910
36. PMID:22292576
37. PMID:21391975
38. PMID:42119948
39. PMID:9883841
40. PMID:25675273
41. PMID:11434702
42. PMID:28826659
43. PMID:15735797
44. PMID:17822515
