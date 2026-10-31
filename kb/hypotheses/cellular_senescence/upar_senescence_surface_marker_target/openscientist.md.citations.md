# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Conserved Cellular Senescence Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** upar_senescence_surface_marker_target
- **Hypothesis Label:** uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: upar_senescence_surface_marker_target
hypothesis_label: uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target
status: EMERGING
description: 'uPAR, the urokinase plasminogen activator receptor encoded by PLAUR, is upregulated on the
  surface of senescent cells and is the antigen that senolytic CAR T cells target. This hypothesis holds
  that uPAR marks the age-accumulating senescent-cell population well enough to serve as a therapeutic
  handle, so that clearing uPAR-positive cells reverses age-related tissue dysfunction. The open question
  is specificity: uPAR is expressed on non-senescent myeloid, endothelial and other cells and has roles
  in normal immunity and fibrinolysis, so how cleanly it separates senescent from non-senescent cells
  across tissues, and how far the mouse evidence extends to humans, is unresolved.'
evidence:
- reference: PMID:38267706
  reference_title: Prophylactic and long-lasting efficacy of senolytic CAR T cells against age-related
    metabolic dysfunction.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Plasma levels of soluble uPAR positively correlate with the pace of aging in humans15,16 and
    Plaur (the gene encoding uPAR) is a component of the SenMayo gene signature recently reported to identify
    senescent cells in aged tissues17.
  explanation: Ties uPAR to an established senescence gene signature and to a human aging correlate, the
    basis for treating it as a senescence marker.
- reference: PMID:38267706
  reference_title: Prophylactic and long-lasting efficacy of senolytic CAR T cells against age-related
    metabolic dysfunction.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: This increase in the fraction of uPAR-positive cells was paralleled by an increase in the percentage
    of senescence-associated beta-galactosidase (SA-β-gal)-positive cells
  explanation: Co-accumulation of uPAR-positive and SA-beta-gal-positive cells with age links the surface
    marker to a canonical senescence readout.
notes: Seeded from the anti-uPAR CAR T lead (Impetus Grants, Corina Amor). The module already records
  that uPAR is senescence-enriched rather than senescence-specific (its positive cells in aged tissue
  are mainly endothelial, myeloid, dendritic and preadipocyte). An OpenScientist run was commissioned
  on this group to test marker specificity across tissues and the strength of the human evidence; its
  assessment will be added separately.
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

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

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

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

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
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

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

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/cellular_senescence/upar_senescence_surface_marker_target/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

**Provider:** openscientist
**Generated:** 2026-10-18T05:47:52.938090

1. PMID:42806572
2. PMID:41916312
3. PMID:35974106
4. PMID:32766674
5. PMID:39623223
6. PMID:38794820
7. PMID:41476987
8. PMID:41577205
9. PMID:42425712
10. PMID:32555459
11. PMID:38267706
12. PMID:41291258
13. PMID:40602406
14. PMID:42442548
15. PMID:42312503