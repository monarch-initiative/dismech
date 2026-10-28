# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hypermetabolism Due To Uncoupled Mitochondrial Oxidative Phosphorylation 2
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** coupling_versus_catalysis_allelic_split
- **Hypothesis Label:** ATP5F1B variants split into a coupling-defect arm causing hypermetabolism and a catalytic-defect arm causing dystonia
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: coupling_versus_catalysis_allelic_split
hypothesis_label: ATP5F1B variants split into a coupling-defect arm causing hypermetabolism and a catalytic-defect
  arm causing dystonia
status: EMERGING
description: 'Heterozygous ATP5F1B variants produce two clinically disjoint phenotypes, and both arms
  are reported as dominant-negative, so the dominance mode does not separate them. The hypothesis is that
  what differs is which function of the beta subunit the mutant protein spoils. In the hypermetabolic
  arm, p.Leu335Pro leaves proton translocation and complex V assembly intact but loosens the coupling
  between stalk rotation and ATP synthesis, so energy leaves as heat and respiration rises. In the movement-disorder
  arm, p.Thr334Pro and p.Val482Ala leave beta subunit abundance intact but severely reduce complex V activity,
  and a splice variant lowers ATP5F1B mRNA and impairs ATPase activity, so the result is insufficient
  ATP and a basal-ganglia-predominant phenotype. The prediction that distinguishes them is the direction
  of respiratory flux: the coupling arm should show elevated oxygen consumption with low membrane potential,
  while the catalytic arm should show reduced complex V activity. Both arms report a low membrane potential,
  so membrane potential alone does not discriminate. Two observations argue against any simple structural
  reading of the split. p.Thr334Pro and p.Leu335Pro are proline substitutions at adjacent residues with
  opposite clinical consequences, which no published work explains or directly compares. And no study
  has measured respiration and complex V activity side by side across variants from both arms in one assay,
  so the flux contrast above is assembled across laboratories rather than observed.'
evidence:
- reference: PMID:36239646
  reference_title: Congenital Hypermetabolism and Uncoupled Oxidative Phosphorylation.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: these results suggest the increased oxygen consumption rate is caused by dissipation of the
    proton motive force, without a corresponding increase in ATP synthesis
  explanation: 'Establishes the coupling-defect arm: raised respiration attributable to dissipated proton
    motive force rather than to ATP demand.'
- reference: PMID:36860166
  reference_title: Variants in ATP5F1B are associated with dominantly inherited dystonia.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Functional studies in mutant fibroblasts revealed no decrease of ATP5F1B protein amount but
    severe reduction of complex V activity and impaired mitochondrial membrane potential, suggesting a
    dominant-negative effect.
  explanation: Establishes the catalytic-defect arm, and shows it is also dominant-negative with normal
    subunit abundance, which is why the hypothesis turns on which function is lost rather than on the
    dominance mode.
- reference: PMID:36860166
  reference_title: Variants in ATP5F1B are associated with dominantly inherited dystonia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: two different ATP5F1B missense variants (c.1000A>C; p.Thr334Pro and c.1445T>C; p.Val482Ala)
    segregating with early-onset isolated dystonia in two families
  explanation: Supplies the dystonia-arm variant coordinates, including the p.Thr334Pro residue adjacent
    to the hypermetabolism arm's p.Leu335Pro.
- reference: PMID:40276935
  reference_title: Expanding the Allelic and Clinical Heterogeneity of Movement Disorders Linked to Defects
    of Mitochondrial Adenosine Triphosphate Synthase.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: A third heterozygous variant, c.1074+1G>T, affected a canonical donor splice site of ATP5F1B
    and resulted in exon skipping with significantly diminished ATP5F1B mRNA levels, as well as impaired
    ATPase activity. The associated phenotype consisted of cerebral palsy (CP) with prominent generalized
    dystonia.
  explanation: A reduction-of-output allele, by a different molecular route from the missense variants,
    also produces a movement disorder, which supports grouping loss of ATP synthase output with the dystonia
    arm.
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
result beneath `kb/hypotheses/Hypermetabolism_Due_To_Uncoupled_Mitochondrial_Oxidative_Phosphorylation_2/coupling_versus_catalysis_allelic_split/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

**Provider:** openscientist
**Generated:** 2026-10-25T03:55:25.182224

1. PMID:36239646
2. PMID:1249587
3. PMID:36860166
4. PMID:40276935
5. PMID:34636445
6. PMID:40672495
7. PMID:18003896
8. PMID:18579516