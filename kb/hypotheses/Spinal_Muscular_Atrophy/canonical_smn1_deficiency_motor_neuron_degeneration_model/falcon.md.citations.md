# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Spinal Muscular Atrophy
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** canonical_smn1_deficiency_motor_neuron_degeneration_model
- **Hypothesis Label:** Canonical SMN1 Deficiency / SMN Protein Loss / Motor Neuron Degeneration Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_smn1_deficiency_motor_neuron_degeneration_model
hypothesis_label: Canonical SMN1 Deficiency / SMN Protein Loss / Motor Neuron Degeneration Model
status: CANONICAL
description: Spinal muscular atrophy (SMA) is caused by biallelic loss-of-function variants in SMN1 on
  5q13, most commonly homozygous SMN1 exon 7 deletion. SMN1 encodes the ubiquitously expressed Survival
  of Motor Neuron (SMN) protein, which functions in snRNP biogenesis, axonal mRNA transport, and neuromuscular
  junction development. SMA severity is inversely modified by SMN2 copy number — a near-identical paralog
  that produces predominantly an unstable, exon-7-skipped transcript (SMN-Δ7) but generates a low level
  of full-length SMN. SMN deficiency selectively kills alpha motor neurons in the anterior horn of the
  spinal cord, producing progressive symmetric weakness, hypotonia, and respiratory failure. Three FDA-approved
  therapies — nusinersen (intrathecal antisense oligonucleotide enhancing SMN2 exon 7 inclusion), onasemnogene
  abeparvovec (AAV9-SMN1 gene therapy, single intravenous infusion), and risdiplam (oral small-molecule
  SMN2 splicing modifier) — definitively validate the SMN-deficiency axis as the canonical pathogenic
  mechanism.
evidence:
- reference: PMID:16364894
  reference_title: Spinal muscular atrophy.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: SMA is caused by mutations in a single gene, the Survival of Motor Neuron 1 (SMN1) gene.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

**Provider:** falcon
**Generated:** 2026-05-25T14:01:09.601453

1. sharma2024translationaldefectsin pages 16-20
2. servais2024realworldoutcomesin pages 1-3
3. servais2024realworldoutcomesin pages 4-6
4. lemska2024efficacyofnusinersen pages 1-2
5. liguori2024anearlytranscriptomic pages 1-2
6. grandi2024smatypeii pages 22-25
7. patel2024risdiplamutilizationadherence pages 4-5
8. haque2024recentprogressin pages 1-2
9. nowak2024molecularmechanismsin pages 10-12
10. patel2024risdiplamutilizationadherence pages 1-2
11. silva2024ametaanalysisof pages 12-15
12. grandi2024smatypeii pages 1-4
13. torres2025dissectingtherole pages 28-32
14. gao2025applicationofbiomarkers pages 25-27
15. lemska2024efficacyofnusinersen pages 2-4
16. liguori2024anearlytranscriptomic pages 10-13
17. patel2024risdiplamutilizationadherence pages 2-4
18. bitetti2023onasemnogeneabeparvovecgene pages 1-2
19. bitetti2023onasemnogeneabeparvovecgene pages 2-3
20. patel2024risdiplamutilizationadherence pages 5-7
21. belancic2025transformingspinalmuscular pages 26-28
22. belancic2025transformingspinalmuscular pages 17-19
23. https://doi.org/10.3390/cimb46060325
24. https://doi.org/10.3390/genes15080999
25. https://doi.org/10.1101/2024.02.29.582680
26. https://doi.org/10.3233/jnd-230122
27. https://doi.org/10.1038/s41434-022-00341-6
28. https://doi.org/10.3390/neurolint16060096
29. https://doi.org/10.1007/s12031-024-02251-1
30. https://doi.org/10.1186/s13023-024-03399-0
31. https://doi.org/10.3390/ijms26146887
32. https://doi.org/10.3390/cimb46060325,
33. https://doi.org/10.3233/jnd-230122,
34. https://doi.org/10.1101/2024.02.29.582680,
35. https://doi.org/10.1007/s12031-024-02251-1,
36. https://doi.org/10.3390/genes15080999,
37. https://doi.org/10.3390/neurolint16060096,
38. https://doi.org/10.1186/s13023-024-03399-0,
39. https://doi.org/10.1038/s41434-022-00341-6,
40. https://doi.org/10.3390/ijms26146887,
41. https://doi.org/10.3390/biomedicines13081939,
