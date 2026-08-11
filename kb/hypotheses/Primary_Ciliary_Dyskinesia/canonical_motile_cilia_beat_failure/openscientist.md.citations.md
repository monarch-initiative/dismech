# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Primary_Ciliary_Dyskinesia
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_motile_cilia_beat_failure
- **Hypothesis Label:** Canonical Axonemal Motile-Cilia Beat-Failure / Mucociliary Clearance Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_motile_cilia_beat_failure
hypothesis_label: Canonical Axonemal Motile-Cilia Beat-Failure / Mucociliary Clearance Model
status: CANONICAL
description: 'The accepted disease mechanism: biallelic (or, for FOXJ1, dominant) defects in axonemal
  motor, regulatory, or assembly components abolish or disorganize the coordinated beat of respiratory
  motile cilia. The resulting failure of mucociliary clearance leaves the airways unable to clear inhaled
  pathogens, producing chronic bacterial infection, a self-amplifying neutrophilic inflammatory response,
  progressive bronchiectasis and airway-wall remodeling, and ultimately obstructive lung-function decline.
  This is the motile-cilium arm that the ciliopathy_dysfunction module''s "Motile Cilia Beat Dysfunction"
  node captures, and to which the disorder''s lead pathophysiology node conforms.'
evidence:
- reference: PMID:19818430
  reference_title: '[Primary ciliary dyskinesia. Ciliopathies].'
  supports: SUPPORT
  snippet: Primary ciliary dyskinesia is a genetically inherited syndrome characterized by cilia immotility
    or dysmotility. Deficiency in mucociliary clearance produces chronic respiratory infections since
    birth, male sterility by spermatozoid immotility and situs inversus in 40-50% of patients (Kartagener's
    syndrome).
  explanation: Supports the core ciliary-immotility to impaired-clearance to chronic-infection cascade
    as the canonical mechanism.
- reference: PMID:11376511
  reference_title: Pathophysiology and treatment of airway mucociliary clearance. A moving tale.
  supports: SUPPORT
  snippet: Failure to keep the airways sterile by MCC results in a host inflammatory response to the persistent
    microorganisms which, if it becomes chronic, causes damage to the airway wall and upregulation of
    mucus production manifest clinically as bronchiectasis, sinusitis and otitis.
  explanation: Supports the infection-inflammation-bronchiectasis arm of the canonical model.
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
**Generated:** 2026-06-19T18:07:27.584850

1. PMID:42026914
2. PMID:38076675
3. PMID:40963409
4. PMID:32380069
5. PMID:24213915
6. PMID:41582098
7. PMID:23290188
8. PMID:31772028
9. PMID:38378235
10. PMID:15806596
11. PMID:24568568
12. PMID:18022865
13. PMID:26909801
14. PMID:28915070
15. PMID:30471718
16. PMID:38072392
17. PMID:24747639
18. PMID:25048963
19. PMID:26777464
20. PMID:24189859
21. PMID:34132502
22. PMID:37813609
23. PMID:40294271
24. PMID:26585432
25. PMID:16617444
26. PMID:38962571
27. PMID:26373788
28. PMID:36990030
29. PMID:23891471
30. PMID:23686703
31. PMID:8575342
32. PMID:25073043
33. PMID:23418344
34. PMID:35011687
35. PMID:42112810
36. PMID:33141819
37. PMID:23040496
38. PMID:26348919
39. PMID:37660715
40. PMID:39269762
41. PMID:28947038
42. PMID:22771515
43. PMID:39433023
44. PMID:24068019
45. PMID:35854386
46. PMID:36341771
47. PMID:41738162
48. PMID:32897034