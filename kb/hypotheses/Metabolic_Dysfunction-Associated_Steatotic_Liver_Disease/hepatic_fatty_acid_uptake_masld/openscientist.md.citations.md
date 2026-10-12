# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Metabolic Dysfunction-Associated Steatotic Liver Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** hepatic_fatty_acid_uptake_masld
- **Hypothesis Label:** Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable step
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: hepatic_fatty_acid_uptake_masld
hypothesis_label: Transporter-mediated hepatic fatty acid uptake as a rate-limiting, druggable step
status: EMERGING
description: 'The canonical model treats the hepatocyte as a passive sink for the non-esterified fatty
  acid load that adipose insulin resistance releases. This hypothesis holds instead that entry into the
  hepatocyte is itself protein-mediated and rate-limiting, so that the fatty acid transport proteins on
  the basolateral hepatocyte membrane — FATP5 (SLC27A5), which is expressed exclusively by liver, and
  FATP2 (SLC27A2) — set how much of that load actually reaches the hepatic lipid pool, and blocking them
  reverses steatosis that is already established. The strong form of the claim is therapeutic: hepatic
  fatty acid uptake is a target in its own right, upstream of and separable from the lipogenic and oxidative
  arms the approved agents act on. It is modeled as EMERGING, not canonical, for two reasons the curated
  evidence states directly. First, every causal experiment is murine knockdown or knockout; no FATP-directed
  agent has been tested in human MASLD, and no human genetic evidence linking SLC27A5 or SLC27A2 variation
  to MASLD is curated here. Second, hepatic FATP5 knockdown also reduced whole-animal caloric uptake,
  so the reported protection is not cleanly attributable to the hepatic uptake step alone — a confound
  the source paper reports rather than one imputed to it. A curator strengthening this arm should look
  for the human evidence that is missing, not for more rodent replication.'
evidence:
- reference: PMID:16618416
  reference_title: 'Targeted deletion of FATP5 reveals multiple functions in liver metabolism: alterations
    in hepatic lipid homeostasis.'
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Our findings support the hypothesis that efficient hepatocellular uptake of LCFAs, and thus
    liver lipid homeostasis in general, is largely a protein-mediated process requiring FATP5.
  explanation: States the core premise of this hypothesis — that hepatocellular long-chain fatty acid
    entry is protein-mediated rather than passive — from a whole-animal knockout.
- reference: PMID:18524776
  reference_title: Silencing of hepatic fatty acid transporter protein 5 in vivo reverses diet-induced
    non-alcoholic fatty liver disease and improves hyperglycemia.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: knockdown of fatty acid transport protein 5 was also able to reverse already established non-alcoholic
    fatty liver disease, resulting in significantly improved whole-body glucose homeostasis.
  explanation: Supplies the therapeutic form of the claim — reversal of established disease, not just
    prevention — which is what makes the uptake step worth modeling separately from lipid overload. Murine,
    which is why the hypothesis stays emerging.
- reference: PMID:18524776
  reference_title: Silencing of hepatic fatty acid transporter protein 5 in vivo reverses diet-induced
    non-alcoholic fatty liver disease and improves hyperglycemia.
  supports: SUPPORT
  directness: INDIRECT
  evidence_source: MODEL_ORGANISM
  snippet: resulting in a marked reduction of hepatic dietary fatty acid uptake, reduced caloric uptake,
    and concomitant protection from diet-induced non-alcoholic fatty liver disease.
  explanation: 'Retained deliberately as the bounding quote: the same sentence that reports protection
    also reports reduced caloric uptake, so the hepatic effect is confounded with a whole-animal energy-intake
    effect. Graded INDIRECT because the protection follows from the uptake block only through that unresolved
    intermediate.'
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
result beneath `kb/hypotheses/Metabolic_Dysfunction-Associated_Steatotic_Liver_Disease/hepatic_fatty_acid_uptake_masld/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

**Provider:** openscientist
**Generated:** 2026-10-07T01:05:45.358047

1. PMID:15864352
2. PMID:16618416
3. PMID:25061560
4. PMID:40840619
5. PMID:18524776
6. PMID:21270117
7. PMID:38642829
8. PMID:28062946
9. PMID:40935652
10. PMID:42564069
11. PMID:42687024
12. PMID:24719358