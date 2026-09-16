---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T05:46:20.384441'
end_time: '2026-09-07T06:06:44.220361'
duration_seconds: 1223.84
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Arboleda-Tham Syndrome
  category: Mendelian
  hypothesis_group_id: late_truncating_nmd_escape
  hypothesis_label: Late-Truncating NMD-Escape Branch
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: late_truncating_nmd_escape\nhypothesis_label:\
    \ Late-Truncating NMD-Escape Branch\nstatus: ALTERNATIVE\ndescription: Truncating\
    \ variants in the last two exons (16-17) escape nonsense-mediated decay and are\n\
    \  predicted to yield a translated but dysfunctional protein with possible gain-of-function\
    \ or dominant-negative\n  effects. This branch is associated with more severe\
    \ developmental delay and a higher frequency of several\n  syndromic features.\
    \ Direct demonstration of mutant protein and its mode of action in patient tissue\n\
    \  remains an evidence gap.\nevidence:\n- reference: PMID:30245513\n  reference_title:\
    \ 'KAT6A Syndrome: genotype-phenotype correlation in 76 patients with pathogenic\
    \ KAT6A\n    variants.'\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: 95% of late truncating cases (exon 16 and 17) were rated as moderate\
    \ or severe, while 60% of\n    early truncating cases (exons 1-15) were rated\
    \ as mild\n  explanation: The cohort documents the more severe developmental phenotype\
    \ associated with the NMD-escaping\n    late-truncating branch."
  artifact_dir: kb/hypotheses/Arboleda-Tham_Syndrome/late_truncating_nmd_escape/openscientist_artifacts
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0043966
    ontology_label: obsolete histone H3 acetylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 8
artifact_sources:
  openscientist_artifacts_zip: 8
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_config_environment.md
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_config_environment.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist environment
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_gnomad_constraint_KAT6A.json
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_gnomad_constraint_KAT6A.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad constraint KAT6A
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter1.md
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter1.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log iter1
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter3.md
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter3.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log iter3
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_kat6a_exon_structure.csv
  path: openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_kat6a_exon_structure.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist kat6a exon structure
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Arboleda-Tham Syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** late_truncating_nmd_escape
- **Hypothesis Label:** Late-Truncating NMD-Escape Branch
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: late_truncating_nmd_escape
hypothesis_label: Late-Truncating NMD-Escape Branch
status: ALTERNATIVE
description: Truncating variants in the last two exons (16-17) escape nonsense-mediated decay and are
  predicted to yield a translated but dysfunctional protein with possible gain-of-function or dominant-negative
  effects. This branch is associated with more severe developmental delay and a higher frequency of several
  syndromic features. Direct demonstration of mutant protein and its mode of action in patient tissue
  remains an evidence gap.
evidence:
- reference: PMID:30245513
  reference_title: 'KAT6A Syndrome: genotype-phenotype correlation in 76 patients with pathogenic KAT6A
    variants.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: 95% of late truncating cases (exon 16 and 17) were rated as moderate or severe, while 60% of
    early truncating cases (exons 1-15) were rated as mild
  explanation: The cohort documents the more severe developmental phenotype associated with the NMD-escaping
    late-truncating branch.
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
result beneath `kb/hypotheses/Arboleda-Tham_Syndrome/late_truncating_nmd_escape/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Final Report

## Arboleda-Tham Syndrome (KAT6A Syndrome)
### Hypothesis: `late_truncating_nmd_escape` — "Late-Truncating NMD-Escape Branch"
### KB Status: ALTERNATIVE — Search date: 2026-09-07

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED.**

The Late-Truncating NMD-Escape Branch hypothesis has two logically separable claims, and they stand on very different evidentiary footing.

1. **The clinical claim** — that truncating variants in the last two exons (16–17) of *KAT6A* are associated with a more severe Arboleda-Tham syndrome (ARTHS) phenotype (more severe developmental delay, higher frequency of syndromic features) — is **robustly and reproducibly supported**. Three independent human clinical cohorts (Kennedy et al. 2019, n=76; St John et al. 2022, n=49; Ng et al. 2024, n=15) converge on the same directional genotype–phenotype gradient.

2. **The molecular-mechanistic claim** — that these variants escape nonsense-mediated decay (NMD) and produce a *translated, dysfunctional protein acting by gain-of-function or dominant-negative interference* in patient tissue — is **structurally plausible but experimentally unproven**. The NMD-escape premise itself is well founded on transcript architecture (a 5,389-nt terminal exon; last exon–exon junction at protein aa ~1117). However, the distinguishing step — direct demonstration of a stable mutant protein and its trans-acting mode of action in patient-derived material — has **not been demonstrated**. This is explicitly acknowledged as an evidence gap in the seed YAML, and our search did not close it.

**Most important caveat:** *KAT6A* is an extreme loss-of-function–intolerant gene (gnomAD pLI = 1.0; LOEUF = 0.079, top decile), and NMD-competent early-truncating (exon 1–15) variants are unambiguously pathogenic. This establishes **haploinsufficiency as the baseline pathogenic mechanism** for ARTHS. Consequently, the late-truncating branch is best interpreted — and best curated — as a **severity modifier layered on top of haploinsufficiency** (loss of the C-terminal transactivation module ± a dominant-negative contribution), *not* as a competing primary mechanism that replaces haploinsufficiency. The KB "ALTERNATIVE" status is appropriate, with the qualification that the clinical severity gradient is essentially established while the mechanistic mode of action remains speculative.

---

## Summary

Arboleda-Tham syndrome is a Mendelian neurodevelopmental disorder caused by de novo heterozygous pathogenic variants in *KAT6A* (MOZ/MYST3), a MYST-family histone acetyltransferase. The seed hypothesis proposes a distinct pathogenic *branch*: truncating variants located in exons 16–17 escape NMD, are translated into a truncated protein, and cause a more severe phenotype — potentially through gain-of-function or dominant-negative activity rather than simple protein loss.

Across five iterations, this investigation established that the **clinical severity gradient is real and reproducible**, and that the **transcript architecture genuinely supports NMD escape** for exon 16–17 premature termination codons (PTCs). Computational analysis of the canonical transcript (Ensembl ENST00000265713; UniProt Q92794) confirmed a giant terminal exon and located the final exon–exon junction near protein residue 1117, so PTCs downstream of ~aa 1100 fall outside the 50–55-nt NMD-triggering window. A late-truncated protein would therefore retain the double PHD fingers and the complete MYST-type HAT catalytic domain, while selectively deleting the C-terminal disordered transactivation region — including a C-terminal RUNX1 activation segment (aa 1913–1948) and PML/RUNX1 interaction surfaces (aa 1517–1741).

However, the investigation also surfaced a strong **competing mechanism**: MOZ/KAT6A **haploinsufficiency**. Mouse genetics show that reduced MOZ dosage alone is developmentally deleterious (DiGeorge-like phenotypes via the Tbx1 locus; cardiac septal defects via Tbx1/Tbx5; altered B-cell/Meis1/Hox programs; behavioral/learning deficits in a heterozygous Kat6a LoF mouse). gnomAD constraint confirms severe selection against heterozygous LoF. Because NMD-competent early truncations are themselves pathogenic, haploinsufficiency is sufficient to cause ARTHS. The late-truncating branch's added severity is therefore most parsimoniously explained as **partial loss of a separable C-terminal coactivation function** (RUNX1 coactivation is separable from HAT activity; Perez-Campo et al. 2009), possibly compounded by a dominant-negative effect — but the dominant-negative/gain-of-function step remains **an untested inference**, with no patient-RNA NMD assay, no mutant-protein detection, and no trans-interference experiment reported. **Bottom line:** the hypothesis is a well-motivated, structurally coherent severity-modifier model with strong clinical correlation but a missing causal keystone (the mutant protein and its mechanism in vivo).

---

## Key Findings

### Finding F001 — The late-truncating severity gradient replicates across three independent cohorts

The clinical core of the hypothesis is its strongest element. Three independent human clinical cohorts, using different instruments and different patient populations, all report that truncating variants in the last two exons associate with worse outcomes:

- **Kennedy et al. 2019 (n=76)** — *KAT6A Syndrome: genotype-phenotype correlation in 76 patients* [PMID: 30245513](https://pubmed.ncbi.nlm.nih.gov/30245513/). Late-truncating pathogenic variants (exons 16–17) were "significantly more prevalent" among patients with the core severe features (intellectual disability, speech delay, microcephaly, cardiac, gastrointestinal). The seed YAML quotes the headline statistic: **95% of late-truncating cases were rated moderate or severe, versus 60% of early-truncating cases rated mild.**
- **St John et al. 2022 (n=49)** — *Speech and language development and genotype-phenotype correlation* [PMID: 35892268](https://pubmed.ncbi.nlm.nih.gov/35892268/). "Truncating variants in the last two exons of KAT6A were associated with poorer communication, daily-living skills, and socialization outcomes."
- **Ng et al. 2024 (n=15)** — *Neuropsychological profile associated with KAT6A syndrome* [PMID: 38741077](https://pubmed.ncbi.nlm.nih.gov/38741077/). "Late-truncating variants associated with a more severe form of intellectual disability."

The effect is **directionally consistent across all three studies**. The important limitation is methodological: these are small, cross-sectional cohorts using categorical/ordinal severity ratings. No formal meta-analytic pooled effect size was computed, and — critically — none of the three performed a molecular NMD assay to *confirm* transcript escape in the patients whose phenotypes they scored. The correlation is between *variant position* and *phenotype*, not between *measured protein/transcript state* and phenotype.

### Finding F002 — MOZ/KAT6A haploinsufficiency is an established competing mechanism for the core features

Model-organism genetics provide direct causal evidence that **reduced MOZ dosage alone**, with no truncated protein required, produces developmental anomalies overlapping ARTHS:

- Moz-null phenocopies **DiGeorge syndrome**; MOZ occupies and activates the *Tbx1* locus, and heterozygous Moz mutation partially phenocopies DiGeorge when combined with Tbx1 haploinsufficiency — "lack of the histone acetyltransferase MOZ (MYST3/KAT6A) phenocopies DiGeorge syndrome" [PMID: 22921202](https://pubmed.ncbi.nlm.nih.gov/22921202/).
- Mesodermal (Mesp1-cre) deletion of Moz causes highly penetrant **ventricular septal defects** via loss of Tbx1/Tbx5 activation — "Mesp1-cre-mediated deletion of Moz results in high penetrance of VSDs" [PMID: 25912687](https://pubmed.ncbi.nlm.nih.gov/25912687/).
- Moz haploinsufficiency alters **B-cell progenitor and Meis1/Hox programs** [PMID: 25605372](https://pubmed.ncbi.nlm.nih.gov/25605372/).
- A heterozygous **Kat6a loss-of-function mouse** recapitulates behavioral/learning deficits that are pharmacologically rescuable with acetyl-carnitine [PMID: 41702672](https://pubmed.ncbi.nlm.nih.gov/41702672/).

These data show a dosage/haploinsufficiency mechanism that **does not require NMD escape or a mutant protein** and is sufficient to generate core ARTHS-relevant phenotypes. This is the principal competing model and the reason the seed hypothesis must be framed as an *added* branch rather than the primary mechanism.

### Finding F003 — Transcript architecture makes exon 16–17 truncations bona fide NMD-escape variants that keep the HAT domain but lose the C-terminal transactivation region

Computational analysis of the canonical *KAT6A* transcript (Ensembl ENST00000265713 / ENSP00000265713; UniProt Q92794; retrieved 2026-09-07) confirms the structural premise of the hypothesis:

| Feature | Value |
|---|---|
| Exons | 17 |
| Terminal exon (17) length | **5,389 nt** (vs median internal exon ~140 nt) |
| 5′UTR | 412 nt |
| CDS | 6,012 nt (2,004 aa) |
| Normal stop codon | cDNA position 6,427 (deep inside exon 17) |
| Last exon–exon junction (16/17) | cDNA 3,764 → protein aa **~1117** |

By the canonical **50–55-nt NMD rule**, a PTC located >~50 nt upstream of the last exon–exon junction triggers decay, whereas PTCs downstream escape. Here, that junction sits at aa ~1117, so:

- PTCs in **exons 1–15 and proximal exon 16 (aa < ~1100)** → **NMD-competent** (transcript degraded → haploinsufficiency).
- PTCs in **distal exon 16 and all of exon 17 (aa ~1100–2004)** → **NMD-escaping** (transcript stable → potential truncated protein).

Mapping the truncation point onto UniProt Q92794 domains, a late-truncated protein **retains** the winged-helix (1–77), H15 (95–171), double PHD fingers (206–313), and the **complete MYST-type HAT catalytic domain (504–778)** (with the BRPF1-interaction/activity region 507–810). It **loses** the C-terminal intrinsically disordered transactivation region, including the C-terminal RUNX1-2 activation segment (1913–1948) and the C-terminal PML/RUNX1 interaction regions (1517–1741). This is exactly the domain configuration the hypothesis requires: catalytically intact but transactivation-deficient.

### Finding F004 — gnomAD constraint confirms KAT6A is extremely LoF-intolerant, fixing haploinsufficiency as the pathogenic baseline

Querying the gnomAD GraphQL API (GRCh38, retrieved 2026-09-07) for *KAT6A* (ENSG00000083168):

| Metric | Value | Interpretation |
|---|---|---|
| pLI | **1.0** | Maximal LoF intolerance |
| LOEUF (oe_lof_upper) | **0.079** | Top decile of LoF-constrained genes |
| Observed/Expected LoF | 9 / 198.4 (o/e = 0.045) | ~95% depletion of LoF alleles |
| LoF Z | 11.4 | Extreme constraint |
| Missense Z | 3.69 | Also missense-constrained |

The near-complete depletion of loss-of-function alleles in the general population demonstrates **strong negative selection against heterozygous KAT6A LoF**. This is the quantitative backbone of the competing haploinsufficiency model: losing one functional allele is, by itself, strongly deleterious.

### Finding F005 — Domain-function data give the late-truncated protein a plausible partial-loss/dominant-negative route via the RUNX1/PML module

MOZ/KAT6A carries **two separable RUNX1 coactivation domains plus a HAT catalytic domain**, and critically, **HAT activity is dispensable for RUNX1 coactivation** (Perez-Campo et al. 2009):

- "2 coactivation domains for the transcription factor Runx1/acute myeloid leukemia 1 and a histone acetyl transferase (HAT) catalytic domain" [PMID: 19264921](https://pubmed.ncbi.nlm.nih.gov/19264921/).
- "MOZ HAT activity is not required either for its role as Runx1 coactivator" [PMID: 19264921](https://pubmed.ncbi.nlm.nih.gov/19264921/).

UniProt Q92794 localizes an N-terminal RUNX1-activation region (aa 1–144) and a C-terminal RUNX1-2 activation region (aa 1913–1948), with C-terminal PML/RUNX1 interaction regions (1517–1741). Combined with the exon-16/17 junction at aa ~1117 (F003), a late-truncated protein would **retain the PHD fingers, HAT domain, and N-terminal RUNX1-activation region** but **selectively delete the C-terminal RUNX1-2 activation domain and PML surface**. MOZ activates RUNX1- and TBX1-dependent transcription (PMIDs [19264921](https://pubmed.ncbi.nlm.nih.gov/19264921/), [12771199](https://pubmed.ncbi.nlm.nih.gov/12771199/), [22921202](https://pubmed.ncbi.nlm.nih.gov/22921202/)). This provides a coherent *molecular route* to added severity: a catalytically competent but transactivation-truncated protein could (a) fail to coactivate a subset of C-terminally dependent targets and/or (b) act as a dominant-negative by occupying complexes/DNA without productive C-terminal output. Both remain **inferred, not demonstrated**.

---

## Mechanistic Model / Interpretation

### Two-tier causal model

The evidence assembles into a two-tier model in which haploinsufficiency is the floor and the late-truncating branch is an added modifier:

```
                          De novo heterozygous KAT6A variant
                                        │
             ┌──────────────────────────┴───────────────────────────┐
             │                                                        │
   EARLY truncating (exons 1–15,                     LATE truncating (distal exon 16 – exon 17,
   proximal exon 16; PTC aa <~1100)                  PTC aa ~1100–2004)
             │                                                        │
   PTC >50 nt upstream of                            PTC downstream of last junction (aa 1117)
   last exon–exon junction                                            │
             │                                                        │
     NMD DEGRADES transcript                          NMD ESCAPE → stable transcript
             │                                                        │
     ~50% protein dose                                Truncated protein PREDICTED:
     (HAPLOINSUFFICIENCY)                             retains PHD + MYST-HAT catalytic domain;
             │                                        loses C-terminal RUNX1-2 (1913–1948)
             │                                        + PML/RUNX1 (1517–1741) transactivation
             │                                                        │
             │                             ┌──────────────────────────┤
             │                             │                          │
             │                     Partial loss of              Dominant-negative /
             │                     C-terminal coactivation      gain-of-function
             │                     (separable from HAT)         (UNPROVEN in patient tissue)
             │                             │                          │
             ▼                             ▼                          ▼
   Core ARTHS features            ───► ADDED SEVERITY: more severe DD/ID, higher
   (ID, speech delay,                   frequency of syndromic features
   microcephaly, cardiac, GI)
```

**Where the literature is strong:** the de novo → phenotype link (ARTHS is an established Mendelian disorder); the **haploinsufficiency floor** (gnomAD constraint; multiple mouse dosage models; pathogenic early truncations); the **NMD-escape premise** for exon 16–17 (transcript architecture is unambiguous); the **domain map** (retained HAT, lost C-terminal transactivation) and the *separability* of RUNX1 coactivation from HAT activity; and the **clinical output** (three-cohort severity gradient).

**Where the links are inferred:** that the escaped transcript is actually **translated to a stable protein in patient cells** (no protein detection reported); and that the retained-HAT/lost-transactivation protein produces a **specific molecular deficit** (partial coactivation loss) rather than being functionally inert.

**Missing causal steps (the keystone gap):** the **dominant-negative / gain-of-function mode of action**. No experiment demonstrates trans-interference of the truncated protein with wild-type KAT6A or with RUNX1/PML complexes in patient-relevant tissue. Without it, the "branch" is mechanistically indistinguishable at the bench from "haploinsufficiency plus a modest extra loss of a C-terminal function."

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Disease subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 30245513](https://pubmed.ncbi.nlm.nih.gov/30245513/) | Human clinical (n=76) | **Supports** | Late (exon 16–17) truncation → greater severity | Late-truncating variants significantly more prevalent among core severe features; 95% moderate/severe vs 60% early mild | ARTHS, mixed truncating variants | Moderate–high; cross-sectional, ordinal severity, no NMD assay |
| [PMID: 35892268](https://pubmed.ncbi.nlm.nih.gov/35892268/) | Human clinical (n=49) | **Supports** | Last-two-exon truncation → worse adaptive/communication | Poorer communication, daily-living, socialization | ARTHS, speech/language focus | Moderate; small n, no molecular confirmation |
| [PMID: 38741077](https://pubmed.ncbi.nlm.nih.gov/38741077/) | Human clinical (n=15) | **Supports** | Late truncation → more severe ID | Late-truncating variants associated with more severe intellectual disability | ARTHS, neuropsychological profile | Low–moderate; very small n |
| ENST00000265713 / Q92794 (computational, this run) | Computational | **Supports (premise)** | Exon 16–17 PTCs escape NMD; retain HAT, lose C-terminal TAD | 5,389-nt terminal exon; last junction aa ~1117; PTCs aa >~1100 escape 50-nt rule | Molecular architecture | High for architecture; NMD prediction rule-based, not assayed |
| gnomAD ENSG00000083168 (computational, this run) | Computational | **Competing (baseline)** | Haploinsufficiency is pathogenic | pLI 1.0; LOEUF 0.079; o/e LoF 0.045 | General population constraint | High; establishes LoF intolerance, does not address late-truncation mechanism |
| [PMID: 22921202](https://pubmed.ncbi.nlm.nih.gov/22921202/) | Model organism (mouse) | **Competing** | MOZ dosage loss alone is deleterious | Moz loss phenocopies DiGeorge via Tbx1 | Cardiac/pharyngeal development | High for dosage mechanism; not ARTHS brain phenotype directly |
| [PMID: 25912687](https://pubmed.ncbi.nlm.nih.gov/25912687/) | Model organism (mouse) | **Competing** | MOZ dosage loss → cardiac defects | Mesodermal Moz deletion → high-penetrance VSDs via Tbx1/Tbx5 | Cardiac septation | High for dosage mechanism |
| [PMID: 25605372](https://pubmed.ncbi.nlm.nih.gov/25605372/) | Model organism (mouse) | **Competing / context** | Moz haploinsufficiency alters transcription programs | Reduced B-cell progenitors; Meis1/Hox dysregulation | Hematopoiesis | High for haploinsufficiency effect; tissue not neural |
| [PMID: 41702672](https://pubmed.ncbi.nlm.nih.gov/41702672/) | Model organism (mouse) | **Competing / therapeutic** | Heterozygous Kat6a LoF → behavioral deficits, rescuable | Acetyl-carnitine improves hyperactivity/learning in Kat6a+/- mouse | Neurodevelopment/behavior | Moderate–high; models LoF, not late-truncation branch |
| [PMID: 19264921](https://pubmed.ncbi.nlm.nih.gov/19264921/) | In vitro / functional | **Qualifies (supports mechanism route)** | RUNX1 coactivation is separable from HAT | MOZ has 2 RUNX1 coactivation domains; HAT dispensable for coactivation | Hematopoietic transcription | High in vitro; not tested in ARTHS truncation context |
| [PMID: 12771199](https://pubmed.ncbi.nlm.nih.gov/12771199/) | In vitro / functional | **Qualifies** | MOZ coactivates RUNX1 targets | MOZ activates MIP-1α promoter, RUNX1-site dependent, synergistic with RUNX1 | Transcriptional coactivation | Supporting context for C-terminal function |
| [PMID: 27939639](https://pubmed.ncbi.nlm.nih.gov/27939639/) | Human clinical / in vitro | **Qualifies (analogy)** | Truncating variant in a partner (BRPF1) escapes decay → truncated protein | BRPF1 frameshift mRNA not reduced; likely truncated protein; causes ID | Related HAT-complex disorder | Analogy only; different gene |

---

## Data and Tool Use

This run combined literature retrieval (PubMed) with two computational lookups against public molecular resources. No patient-level or controlled-access data were used. All analyses were **descriptive/rule-based**, not statistical inference on primary datasets.

| Source | Accession / URI | Repository | Version / snapshot | Retrieval date | Access status | Query / scope | Relevance |
|---|---|---|---|---|---|---|---|
| KAT6A canonical transcript | ENST00000265713 / ENSP00000265713 | Ensembl | GRCh38 (2026 release) | 2026-09-07 | **Accessed** | Exon count/lengths, CDS, UTR, exon–exon junction positions, stop codon location | Directly relevant — establishes NMD-escape architecture |
| KAT6A protein | Q92794 | UniProt | 2026-09-07 entry | 2026-09-07 | **Accessed** | Domain boundaries (PHD, MYST-HAT, RUNX1/PML regions) | Directly relevant — maps retained vs lost domains |
| KAT6A gene constraint | ENSG00000083168 | gnomAD (GraphQL API) | gnomAD GRCh38 | 2026-09-07 | **Accessed** | pLI, LOEUF, o/e LoF, LoF/mis Z | Directly relevant — quantifies haploinsufficiency baseline |
| PubMed literature | 15 PMIDs (see Evidence Base) | NCBI PubMed | — | across iterations | **Accessed** | KAT6A / MOZ + phenotype/NMD/haploinsufficiency terms | Directly relevant |

**Analysis inventory (input → method → output → outcome):**

1. **NMD-escape boundary calculation** — Input: ENST00000265713 exon/CDS coordinates. Method: applied 50–55-nt last-junction rule; computed junction at cDNA 3,764 → aa ~1117. Output: classification of PTC positions into NMD-competent vs NMD-escaping. **Outcome: succeeded (rule-based prediction, not an experimental NMD assay).** Limitation: predictive only; not validated against patient RNA.
2. **Domain-retention mapping** — Input: UniProt Q92794 domain table + junction position. Method: interval overlap. Output: retained (winged-helix, H15, PHD, MYST-HAT) vs lost (C-terminal RUNX1-2, PML/RUNX1) domains. **Outcome: succeeded.** Limitation: assumes canonical isoform; protein stability not assessed.
3. **Constraint retrieval** — Input: ENSG00000083168. Method: gnomAD GraphQL query. Output: pLI/LOEUF/o-e table. **Outcome: succeeded.** Limitation: constraint reflects all LoF, cannot isolate late-truncation behavior.

**Not performed / not available (explicitly):** No patient-derived RNA NMD assay, no Western blot / mass-spec detection of truncated KAT6A protein, no co-immunoprecipitation or reporter trans-interference assay, and no formal meta-analysis pooling the three cohorts were performed in this run — these require primary wet-lab or individual-level data not accessible here. No fallback substituted literature prose for these missing experiments; the corresponding claims are labeled unproven throughout.

---

## Limitations and Knowledge Gaps

### Gap 1 — The mutant protein has never been demonstrated in patient tissue
**Scope:** The keystone step (translation of a stable truncated KAT6A protein in patient cells). **Why it matters:** Without protein detection, the entire "translated but dysfunctional protein" premise is inferential. **What was checked:** Literature search for KAT6A truncated-protein detection returned no primary demonstration in ARTHS patient material; the closest analogy is BRPF1 (PMID 27939639), a different gene. **Resolution:** Western blot / targeted mass-spec on patient fibroblasts or iPSC-neurons carrying exon 16–17 truncations, plus allele-specific RNA quantification.

### Gap 2 — NMD escape is predicted, not assayed, in patients
**Scope:** Whether exon 16–17 patient transcripts actually escape decay in vivo. **Why it matters:** The 50-nt rule has exceptions (long exons, position effects). **What was checked:** Rule-based computation only (this run). **Resolution:** Allele-specific expression / RNA-seq on patient cells ± cycloheximide (NMD inhibition) to compare mutant:WT transcript ratios by variant class.

### Gap 3 — Gain-of-function vs dominant-negative vs simple C-terminal partial-loss is unresolved
**Scope:** Mode of action of the truncated protein. **Why it matters:** These have different therapeutic implications (allele-specific knockdown vs dosage restoration). **What was checked:** No functional trans-interference data found. **Resolution:** Reporter assays (RUNX1/TBX1 targets) co-expressing WT + truncated KAT6A; degron/rescue experiments.

### Gap 4 — No formal pooled effect size for the severity gradient
**Scope:** Quantitative magnitude of the late vs early severity difference. **Why it matters:** Current support is directional across three small cohorts; heterogeneity and rating-scale differences preclude a clean estimate. **What was checked:** Three cohorts reviewed; no meta-analysis exists. **Resolution:** Harmonized multi-cohort reanalysis with a common severity instrument and variant re-annotation.

### Gap 5 — Source/database absences (as of 2026-09-07)
- **GenCC / ClinGen dosage-and-mechanism curation** specific to the late-truncating branch was **not retrieved** in this run; label **unverified** rather than absent. A negative claim would require the database, version, query, and date.
- **No ARTHS-specific omics dataset** (patient brain/neuronal transcriptome stratified by variant class) was located.
- **No interventional trial** targeting the late-truncating subtype was found; the acetyl-carnitine result (PMID 41702672) is a haploinsufficiency-model preclinical finding, not a branch-specific trial.

---

## Alternative Models

| Model | Relationship to seed hypothesis | Basis |
|---|---|---|
| **Haploinsufficiency (dosage)** | **Competing primary mechanism / baseline** — the seed branch sits on top of this | gnomAD pLI 1.0/LOEUF 0.079 (F004); pathogenic NMD-competent early truncations; multiple Moz-dosage mouse models (F002) |
| **C-terminal partial loss-of-function (no dominant-negative)** | **More parsimonious version of the seed** — explains added severity without requiring GoF/DN | Late-truncated protein loses separable C-terminal RUNX1-2/PML transactivation (F003, F005); RUNX1 coactivation separable from HAT (PMID 19264921) |
| **Dominant-negative interference** | **The seed's distinguishing sub-claim** — truncated protein poisons WT complexes | Structurally plausible (retained PHD/HAT could occupy chromatin/complexes) but **unproven** |
| **Gain-of-function neomorph** | **The seed's alternative sub-claim** | Speculative; no supporting functional data found |
| **Missense/HAT-domain hypomorph mechanism** | **Parallel mechanism** for non-truncating variants | KAT6A is also missense-constrained (mis_z 3.69); not addressed by the truncation branch |

The most parsimonious reading is that **haploinsufficiency + C-terminal partial loss-of-function** explains the late-truncating severity gradient without invoking a dominant-negative or neomorph. The seed hypothesis's added value is precisely the DN/GoF claim — which is exactly the part that lacks evidence.

---

## Discriminating Tests

1. **Patient-RNA NMD assay (highest priority).** Stratify patient fibroblasts/iPSC-neurons by variant class (early exon 1–15 vs late exon 16–17). Allele-specific RNA-seq ± cycloheximide. *Expected if hypothesis true:* late-truncating transcripts retained near WT levels; early-truncating transcripts depleted.
2. **Mutant protein detection.** Targeted mass-spec / C-terminal-aware Western on the same cells. *Expected:* stable truncated protein only in the late-truncating group.
3. **Trans-interference reporter assay.** Co-express WT + truncated KAT6A on RUNX1/TBX1-dependent reporters and endogenous target ChIP. *Expected if dominant-negative:* truncated protein suppresses WT activity below the 50% dosage baseline. *If simple partial-loss:* activity tracks WT dosage, no extra suppression.
4. **Isoallelic mouse/organoid comparison.** Knock-in an exon-17 truncation vs a null allele; compare severity. *Expected if branch is real:* truncation allele more severe than null at matched dosage.
5. **Harmonized cohort meta-analysis** with uniform severity scoring and variant re-annotation to produce a pooled effect size and test for a distal-to-proximal severity trend within exon 16.

---

## Curation Leads (require curator verification)

**Candidate status/framing:** Retain **ALTERNATIVE**, but annotate that the *clinical severity gradient* sub-claim is essentially **established** (three-cohort replication) while the *dominant-negative/gain-of-function mode of action* sub-claim is **speculative/unconfirmed**. Consider splitting the hypothesis into (a) a supported severity-modifier edge and (b) an unresolved mechanism-of-action edge.

**Candidate evidence references + snippets to verify:**
- PMID:30245513 — "late-truncating pathogenic variants (exons 16-17) are significantly more prevalent"
- PMID:35892268 — "Truncating variants in the last two exons of KAT6A were associated with poorer communication, daily-living skills, and socialization outcomes."
- PMID:38741077 — "late-truncating variants associated with a more severe form of intellectual disability"
- PMID:19264921 — "MOZ HAT activity is not required either for its role as Runx1 coactivator"
- PMID:22921202 — "lack of the histone acetyltransferase MOZ (MYST3/KAT6A) phenocopies DiGeorge syndrome"
- PMID:25912687 — "Mesp1-cre-mediated deletion of Moz results in high penetrance of VSDs"

**Candidate pathophysiology nodes/edges:**
- Node: "NMD-escaping late-truncated KAT6A transcript (exon 16–17 PTC)" → Edge: "retains MYST-HAT catalytic domain; deletes C-terminal RUNX1-2 (aa 1913–1948) + PML/RUNX1 (aa 1517–1741) transactivation."
- Edge (baseline): "KAT6A LoF (pLI 1.0, LOEUF 0.079) → haploinsufficiency → core ARTHS features."
- Edge (unconfirmed): "late-truncated protein → dominant-negative interference with WT KAT6A/RUNX1 complexes" — flag as **needs direct perturbation evidence**.

**Candidate ontology terms:** histone H3 acetylation (GO:0043966); MYST-type HAT activity; RUNX1/CBFβ transcriptional coactivation; nonsense-mediated decay (GO:0000184); neurodevelopmental/intellectual-disability phenotype terms (HPO).

**Candidate knowledge_gaps / discussion prompts:**
- "No patient-tissue demonstration of truncated KAT6A protein or NMD escape as of 2026-09-07."
- "Dominant-negative vs C-terminal partial-loss remains undistinguished."
- "GenCC/ClinGen dosage-mechanism curation for the late-truncating branch: unverified (not queried this run)."

**Provider artifact bundle:** Computational lookups (Ensembl transcript coordinates, UniProt domain map, gnomAD constraint) and the PubMed search logs supporting F001–F005 should be deposited under `kb/hypotheses/Arboleda-Tham_Syndrome/late_truncating_nmd_escape/openscientist_artifacts` with a `MANIFEST.yaml` recording the retrieval date (2026-09-07), the exact accessions (ENST00000265713, Q92794, ENSG00000083168), and the rule-based (not assayed) status of the NMD prediction. No patient-level or controlled data were accessed; none should be bundled.

---

## Evidence Base (literature summary)

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [30245513](https://pubmed.ncbi.nlm.nih.gov/30245513/) | KAT6A Syndrome genotype–phenotype, n=76 | Primary support, severity gradient |
| [35892268](https://pubmed.ncbi.nlm.nih.gov/35892268/) | Speech/language genotype–phenotype, n=49 | Independent replication |
| [38741077](https://pubmed.ncbi.nlm.nih.gov/38741077/) | Neuropsychological profile, n=15 | Third-cohort replication |
| [19264921](https://pubmed.ncbi.nlm.nih.gov/19264921/) | MOZ HAT/RUNX1 coactivation domains | Mechanism route (separable coactivation) |
| [22921202](https://pubmed.ncbi.nlm.nih.gov/22921202/) | MOZ–Tbx1 / DiGeorge phenocopy | Competing haploinsufficiency |
| [25912687](https://pubmed.ncbi.nlm.nih.gov/25912687/) | Moz mesodermal deletion → VSDs | Competing haploinsufficiency |
| [25605372](https://pubmed.ncbi.nlm.nih.gov/25605372/) | Moz haploinsufficiency, B-cell/Meis1 | Competing haploinsufficiency |
| [41702672](https://pubmed.ncbi.nlm.nih.gov/41702672/) | Kat6a+/- mouse, acetyl-carnitine rescue | Competing model + therapeutic lead |
| [12771199](https://pubmed.ncbi.nlm.nih.gov/12771199/) | RUNX1/MOZ MIP-1α promoter | C-terminal coactivation context |
| [27939639](https://pubmed.ncbi.nlm.nih.gov/27939639/) | BRPF1 frameshift → truncated protein | Analogy for NMD escape in a partner gene |
| [18754862](https://pubmed.ncbi.nlm.nih.gov/18754862/) | MOZ in normal/malignant hematopoiesis | Review-level orientation |
| [18224409](https://pubmed.ncbi.nlm.nih.gov/18224409/) | AML1 complex chromatin regulation | Review-level orientation (PML/MOZ context) |
| [16917507](https://pubmed.ncbi.nlm.nih.gov/16917507/) | HIPK1/2 in AML1/p300 transcription | Review-level orientation |
| [33552646](https://pubmed.ncbi.nlm.nih.gov/33552646/) | Novel KAT6A frameshift, pancraniosynostosis | Phenotype breadth |
| [29806701](https://pubmed.ncbi.nlm.nih.gov/29806701/) | Neonatal leukaemia (KAT6A-CREBBP) | Somatic KAT6A context (orientation) |

---

## Proposed Follow-up Experiments / Actions

1. **Run the patient-RNA NMD assay and mutant-protein detection** (Discriminating Tests 1–2) — closes the keystone gap and would convert the hypothesis from "partially supported" to "supported" or "refuted."
2. **Perform the trans-interference reporter assay** (Test 3) to distinguish dominant-negative from simple C-terminal partial-loss — the single most decisive experiment for the seed's distinguishing claim.
3. **Commission a harmonized three-cohort meta-analysis** (Test 5) to produce a pooled, quantitative severity effect size and test for a within-exon-16 proximal-to-distal gradient.
4. **Query GenCC and ClinGen** with recorded version/date to convert Gap 5 from "unverified" to a documented positive/negative curation finding.
5. **Deposit the computational artifact bundle** (Ensembl/UniProt/gnomAD lookups + PubMed logs) with a checksummed `MANIFEST.yaml` and explicitly flag the NMD prediction as rule-based, not assayed.

---

*Report prepared for the Disorder Mechanisms Knowledge Base. Verdict: the Late-Truncating NMD-Escape Branch is PARTIALLY SUPPORTED — a reproducible clinical severity modifier with a structurally sound NMD-escape premise, but an experimentally unproven dominant-negative/gain-of-function mode of action layered atop an established haploinsufficiency baseline.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist environment](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_config_environment.md)
- [OpenScientist gnomad constraint KAT6A](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_gnomad_constraint_KAT6A.json)
- [OpenScientist pubmed search log iter1](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter1.md)
- [OpenScientist pubmed search log iter3](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_logs_pubmed_search_log_iter3.md)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_evidence_matrix.csv)
- [OpenScientist kat6a exon structure](openscientist_artifacts/kb_hypotheses_Arboleda-Tham_Syndrome_late_truncating_nmd_escape_openscientist_artifacts_tables_kat6a_exon_structure.csv)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043966` (obsolete histone H3 acetylation) (1 mention)

1 of 2 terms resolved to a current term; the rest could not be looked up either way.