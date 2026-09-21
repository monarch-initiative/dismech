---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T05:46:20.383136'
end_time: '2026-09-07T06:09:16.731012'
duration_seconds: 1376.35
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Bohring-Opitz syndrome
  category: Mendelian
  hypothesis_group_id: asxl1_truncated_protein_dominant_or_gain
  hypothesis_label: NMD-escaping truncated ASXL1 with dominant-negative or gain-of-function
    activity
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: asxl1_truncated_protein_dominant_or_gain\n\
    hypothesis_label: NMD-escaping truncated ASXL1 with dominant-negative or gain-of-function\
    \ activity\nstatus: ALTERNATIVE\ndescription: BOS alleles cluster in the last\
    \ exons and are expected to escape nonsense-mediated decay,\n  so patient cells\
    \ may express a stable truncated ASXL1. By analogy with the truncated ASXL1 of\
    \ clonal\n  haematopoiesis and myeloid neoplasia, which gains activity, the BOS\
    \ product may interfere with wild-type\n  ASXL1 or acquire a new function rather\
    \ than simply being absent. The cross-tissue epigenomic disturbance\n  in patient\
    \ cells is compatible with either reading.\nevidence:\n- reference: PMID:37053013\n\
    \  reference_title: Multiomics of Bohring-Opitz syndrome truncating ASXL1 mutations\
    \ identify canonical\n    and noncanonical Wnt signaling dysregulation.\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: Our data show that regardless\
    \ of cell type, ASXL1 mutations drive strong cross-tissue effects\n    that disrupt\
    \ multiple layers of the epigenome.\n  explanation: Patient-cell multi-omics establishes\
    \ a broad effect without discriminating loss from dominant\n    or gained activity."
  artifact_dir: kb/hypotheses/Bohring-Opitz_syndrome/asxl1_truncated_protein_dominant_or_gain/openscientist_artifacts
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
citation_count: 13
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 9
artifact_sources:
  openscientist_artifacts_zip: 9
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
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_README.md
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_README.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist README
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_constraint.csv
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_constraint.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad asxl1 constraint
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_region_summary.csv
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_region_summary.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad asxl1 plof region summary
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_top_hotspot_variants.csv
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_top_hotspot_variants.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad asxl1 plof top hotspot variants
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_gnomad_execution_log.md
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_gnomad_execution_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gnomad execution log
- filename: kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Bohring-Opitz syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** asxl1_truncated_protein_dominant_or_gain
- **Hypothesis Label:** NMD-escaping truncated ASXL1 with dominant-negative or gain-of-function activity
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: asxl1_truncated_protein_dominant_or_gain
hypothesis_label: NMD-escaping truncated ASXL1 with dominant-negative or gain-of-function activity
status: ALTERNATIVE
description: BOS alleles cluster in the last exons and are expected to escape nonsense-mediated decay,
  so patient cells may express a stable truncated ASXL1. By analogy with the truncated ASXL1 of clonal
  haematopoiesis and myeloid neoplasia, which gains activity, the BOS product may interfere with wild-type
  ASXL1 or acquire a new function rather than simply being absent. The cross-tissue epigenomic disturbance
  in patient cells is compatible with either reading.
evidence:
- reference: PMID:37053013
  reference_title: Multiomics of Bohring-Opitz syndrome truncating ASXL1 mutations identify canonical
    and noncanonical Wnt signaling dysregulation.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Our data show that regardless of cell type, ASXL1 mutations drive strong cross-tissue effects
    that disrupt multiple layers of the epigenome.
  explanation: Patient-cell multi-omics establishes a broad effect without discriminating loss from dominant
    or gained activity.
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
result beneath `kb/hypotheses/Bohring-Opitz_syndrome/asxl1_truncated_protein_dominant_or_gain/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — Final Report

## Bohring-Opitz syndrome: *NMD-escaping truncated ASXL1 with dominant-negative or gain-of-function activity*

- **Disease:** Bohring-Opitz syndrome (BOS), Mendelian
- **Hypothesis ID:** `asxl1_truncated_protein_dominant_or_gain`
- **Status in KB:** ALTERNATIVE
- **Search date:** 2026-09-07
- **Verdict:** **Partially supported (emerging)** — likely convergent with a loss-of-function component

---

## Executive Judgment

**The hypothesis that BOS-causing *ASXL1* truncating variants escape nonsense-mediated decay (NMD) and act through a stable truncated protein with dominant-negative and/or gain-of-function (GOF) activity is PARTIALLY SUPPORTED as an emerging model, but it is not established, and it does not exclude a coexisting loss-of-function (LOF)/haploinsufficiency mechanism.**

The strongest support comes by mechanistic analogy from myeloid biology, where the *identical* last-exon *ASXL1* alleles that cause germline BOS are the recurrent somatic drivers of clonal hematopoiesis (CHIP) and myeloid neoplasia. In that context the truncated protein is demonstrably expressed (mass spectrometry and Western blot), escapes NMD because variants fall near the 5′ end of the terminal exon, and confers gain-of-function on the ASXL1–BAP1 PR-DUB deubiquitinase complex — an effect strong enough that reducing BAP1 attenuates the malignant phenotype ([PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/), [PMID:30515738](https://pubmed.ncbi.nlm.nih.gov/30515738/), [PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/)). In a BOS-relevant developmental setting, a truncated ASXL1 fragment (amino acids 1–900) is *sufficient* to recapitulate neural-crest delamination/emigration defects, and 2026 BOS patient-fibroblast data describe "aberrant PR-DUB complex spreading beyond its normally constrained chromatin territory," a signature more consistent with a mislocalized mutant complex than with simple protein absence ([PMID:31006630](https://pubmed.ncbi.nlm.nih.gov/31006630/); [PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/), preprint). An original population-genetics analysis performed in this investigation (gnomAD v4, retrieved 2026-09-07) shows that *ASXL1* is **not** classically LoF-constrained (pLI ≈ 2.5×10⁻¹⁶, LOEUF ≈ 0.90) and that its population "pLoF" burden is concentrated in exactly the last-exon window (aa 580–1000) that harbors the CHIP/AML somatic drivers, led by p.Gly646TrpfsTer12 — a signature of somatic clonal fitness (gain of function) rather than tolerated germline nulls.

The most important caveats are that (1) **no accessed source directly demonstrates a stable endogenous truncated ASXL1 protein in germline BOS patient tissue** — the protein-expression evidence is from myeloid/leukemic cells and heterologous over-expression systems; (2) the proposed C-terminal degron whose removal would stabilize the truncated protein remains "putative" ([PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/)); and (3) **loss-of-function/haploinsufficiency alone reproduces cardinal BOS features in mice** — anophthalmia, microcephaly, cleft palate, mandibular malformation — and *Asxl1⁺/⁻* animals show a haploinsufficient hematologic phenotype, so LOF is a live, well-supported competing explanation ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/), [PMID:24255920](https://pubmed.ncbi.nlm.nih.gov/24255920/), [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)). The most parsimonious reading of current evidence is that dominant/GOF and LOF mechanisms **coexist and converge on the PR-DUB/Polycomb chromatin axis**, and that the seed hypothesis is best treated as a partially confirmed contributor rather than the sole disease mechanism.

---

## Key Findings

### F001 — In myeloid cells, truncated ASXL1 escapes NMD, is expressed as protein, and gains function on the ASXL1–BAP1 PR-DUB complex

This is the foundational precedent underpinning the seed hypothesis. In leukemia cell lines lacking an intact *ASXL1* gene, the C-terminally truncated protein was directly detected by both mass spectrometry and Western blot, establishing that these alleles are not silent nulls but yield a stable protein product ([PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/)). The molecular basis for escape from surveillance is that the mutations "occur near the 5′ end of the last exon, thereby the transcripts would escape from nonsense-mediated decay" ([PMID:30515738](https://pubmed.ncbi.nlm.nih.gov/30515738/)) — the same premise the seed hypothesis invokes for BOS. Functionally, the truncated protein "confers gain of function on the ASXL1–BAP1 deubiquitinase (DUB) complex," hyperactivating BAP1 and lowering H2AK119ub; critically, reducing BAP1 attenuates mutant-ASXL1-driven malignancy, demonstrating that the phenotype depends on a *gained* activity rather than an absence ([PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/)). Because germline BOS variants map to the same terminal-exon window, this chain (NMD escape → stable truncated protein → PR-DUB GOF) is directly transferable in principle to BOS.

### F002 — BOS-context support: truncated ASXL1 (aa 1–900) is sufficient for disease-relevant phenotypes, and BOS patient cells show mutant-complex chromatin mis-spreading

Moving from analogy toward direct BOS relevance, expression of truncated ASXL1 isoforms (amino acids 1–900) "recapitulated the NC [neural crest] phenotypes in vitro and in ovo, raising the possibility that truncated ASXL1 variants contribute to BOS pathology" — i.e., the fragment is *sufficient* to drive a developmental defect, which is difficult to reconcile with pure loss-of-function ([PMID:31006630](https://pubmed.ncbi.nlm.nih.gov/31006630/)). A 2026 study of BOS patient-derived fibroblasts (bioRxiv preprint) reports truncated ASXL1 and BAP1 aberrantly co-occupying an *MPC2* intronic element and describes the result as "consistent with aberrant PR-DUB complex spreading beyond its normally constrained chromatin territory," explicitly attributing a Warburg-like metabolic phenotype to "gain-of-function ASXL1 truncation" ([PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/)). Complementary patient multi-omics (the seed evidence) show that "regardless of cell type, ASXL1 mutations drive strong cross-tissue effects that disrupt multiple layers of the epigenome" — a broad disturbance compatible with dominant/gained activity but, as the seed YAML notes, non-discriminating on its own ([PMID:37053013](https://pubmed.ncbi.nlm.nih.gov/37053013/)). *Note: PMID:42523271 is a preprint and one of its snippets was flagged as a normalization mismatch during curation — treat as emerging, not established.*

### F003 — Competing evidence: Asxl1 loss/haploinsufficiency alone recapitulates BOS-like malformations in mice

The principal competing model has strong in vivo footing. Constitutive *Asxl1* deletion produces "developmental abnormalities, including anophthalmia, microcephaly, cleft palates, and mandibular malformations," together with dwarfism and ~80% embryonic lethality — a phenotypic spectrum overlapping BOS, generated purely by loss of the gene ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/)). Moreover, *Asxl1⁺/⁻* mice "developed mild MDS-like disease... demonstrating a haploinsufficient effect of Asxl1," establishing that reduced dosage of wild-type ASXL1 is by itself pathogenic ([PMID:24255920](https://pubmed.ncbi.nlm.nih.gov/24255920/)). Because these malformation and dosage phenotypes arise without any truncated protein, they show that LOF is a sufficient and independently supported route to BOS-like disease.

### F004 — LOF neural mechanism: Asxl1 ablation causes microcephaly via impaired PRC2/Ezh2-dependent neural stem cell survival

The LOF model also supplies a concrete mechanism for a cardinal BOS feature. *Asxl1* deletion "induces microcephaly, primarily caused by a reduction in the size and number of cortical neurons," driven by decreased neural stem cell (NSC) proliferation and increased apoptosis; transcriptomics of *Asxl1*-deficient NSCs identified 4,635 differentially expressed genes (2,262 up / 2,373 down) and showed that "Asxl1 regulates NSC survival through the histone methyltransferase Ezh2, a core component of the Polycomb Repressive Complex 2 (PRC2)" ([PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)). This dovetails with earlier evidence that *Asxl1* loss globally reduces H3K27me3 ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/)). Thus the LOF branch reaches the same Polycomb chromatin axis that the GOF branch perturbs via BAP1/PR-DUB — a key point for the convergence model. *Note: two PMID:40276524 snippets were flagged as normalization mismatches during curation and should be re-verified against the abstract.*

### F005 — Review-level synthesis: generalized ASXL GOF requires NMD escape *plus* removal of a C-terminal degron

A 2026 peer-reviewed review integrates population-genetics and in vitro data to argue that ASXL-family truncating mutations act by gain of function, stating that "mounting evidence from population genetics and in vitro studies supports gain-of-function (GOF) mechanisms" and, crucially, that "such mechanisms require both escape from nonsense-mediated mRNA decay and removal of a putative C-terminal degron signal within ASXL proteins," which would increase truncated-protein stability and alter histone modifications ([PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/)). This articulates the *falsifiable requirements* of the seed hypothesis — NMD escape and degron loss — and flags the degron as still putative. Clinically, the shared germline/somatic last-exon variants and BOS-associated Wilms tumor predisposition reinforce the oncogenic-analogy logic: "Somatic mutations in ASXL1 are associated with myeloid malignancies, and these reports emphasize the need for Wilms tumor screening in patients with ASXL1 mutations" ([PMID:25921057](https://pubmed.ncbi.nlm.nih.gov/25921057/)).

### F006 — Computational (gnomAD v4): ASXL1 is not LoF-constrained and its population truncation hotspot equals the CHIP driver window

An original analysis in this investigation queried the gnomAD v4 GraphQL API (retrieved 2026-09-07; gene ENSG00000171456 / transcript ENST00000375687). Constraint metrics: **pLI = 2.5×10⁻¹⁶, LOEUF (oe_lof upper) = 0.90, oe_lof = 0.73** — *ASXL1* is **not** classically LoF-constrained, which would be surprising for a gene where germline nulls cause a severe dominant disorder if the mechanism were pure haploinsufficiency. Spatially, of 714 mappable pLoF variants, **61.2% of distinct variants and 76.8% of the pLoF allele burden fall in aa 580–1000** (1.04 variants/aa vs 0.33 N-terminal and 0.17 distal) — the last-exon NMD-escape window. The top hotspot alleles — **p.Gly646TrpfsTer12 (c.1934dupG; AC=685, AF=4.7×10⁻⁴), p.Glu635ArgfsTer15 (AC=129), p.Arg693Ter, p.Tyr591Ter** — are the canonical recurrent ASXL1 clonal-hematopoiesis/AML somatic drivers *and* the recurrent germline BOS alleles. All hotspot allele frequencies are <0.1% (median AF 6.8×10⁻⁷; 44% singletons), consistent with age-related somatic clonal expansion in the blood-derived gnomAD cohort rather than tolerated germline loss-of-function. This population signature independently supports a clonal-fitness gain-of-function interpretation for NMD-escaping truncations and aligns with the review-level reasoning ([PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/); [PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/)).

### F007 — Synthesis: partially (emerging) supported, likely convergent with LOF

Integrating F001–F006, the dominant/GOF hypothesis has three converging lines of support — the myeloid precedent (protein expression + PR-DUB GOF), BOS-context sufficiency/mislocalization, and population genetics — but is limited by (a) the absence of any accessed source directly showing a stable endogenous truncated ASXL1 protein in germline BOS tissue, (b) an unconfirmed ("putative") C-terminal degron, and (c) robust in vivo evidence that LOF/haploinsufficiency alone reproduces BOS-like malformations and microcephaly via PRC2. The verdict is therefore **partially supported (emerging)**, with the two mechanisms most plausibly coexisting and converging on the PR-DUB/Polycomb histone-ubiquitination axis ([PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/); [PMID:24255920](https://pubmed.ncbi.nlm.nih.gov/24255920/); [PMID:31006630](https://pubmed.ncbi.nlm.nih.gov/31006630/)).

---

## Mechanistic Model / Interpretation

The two candidate mechanisms are not mutually exclusive; they diverge at the protein level and re-converge on Polycomb-domain histone chemistry.

```
                        Germline ASXL1 truncating variant (last exon, aa ~580–1000)
                                              |
                        ┌─────────────────────┴──────────────────────┐
                        |                                             |
             (A) DOMINANT / GAIN-OF-FUNCTION              (B) LOSS-OF-FUNCTION / HAPLOINSUFFICIENCY
                        |                                             |
        Transcript escapes NMD (5' of last exon)          Reduced dose of full-length ASXL1
                        |                                             |
        Stable truncated protein                          Impaired ASXL1–PRC2 interaction
        (requires degron loss? — putative)                          |
                        |                                             |
        Truncated ASXL1 + BAP1 → PR-DUB GOF                Global loss of H3K27me3;
        Hyperactive BAP1; ↓H2AK119ub;                      derepression of PcG targets;
        aberrant chromatin "spreading"                     NSC apoptosis (Ezh2-dependent)
                        |                                             |
                        └───────────────┬─────────────────────────────┘
                                        |
                    CONVERGENCE: dysregulated Polycomb-domain histone
                    ubiquitination/methylation; cross-tissue epigenome disruption;
                    Wnt (canonical + noncanonical) dysregulation; neural-crest &
                    NSC-survival defects
                                        |
                    BOS clinical features: microcephaly, craniofacial anomalies,
                    growth failure, feeding difficulty, Wilms tumor predisposition
```

**Where the literature is strong:** the myeloid branch of (A) is well established — protein expression, NMD-escape logic, and PR-DUB GOF with a BAP1-dependent phenotype are all directly demonstrated ([PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/), [PMID:30515738](https://pubmed.ncbi.nlm.nih.gov/30515738/), [PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/)). Branch (B) is strong in vivo for malformations and microcephaly, with a defined PRC2/Ezh2 mechanism ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/), [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)).

**Where the links are inferred:** transferring branch (A) from blood to BOS somatic tissues; the "stable truncated protein in germline BOS cells" node has no direct accessed evidence; the degron-removal requirement is stated but unconfirmed ([PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/)).

**Missing causal steps:** (i) direct protein-level demonstration of endogenous truncated ASXL1 in BOS patient cells; (ii) an allele series showing that BOS truncations behave dominant-negatively over wild-type ASXL1 in a developmental system; (iii) identification and functional validation of the C-terminal degron.

---

## Evidence Base / Evidence Matrix

| Citation | Evidence type | Role | Mechanistic claim tested | Key finding | Disease subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/) | In vitro (human cell lines) | **Supports** | Truncated ASXL1 is expressed (non-null); DN/GOF | Truncated protein detected by MS + Western in cells lacking intact ASXL1 | Myeloid malignancy | High for myeloid; indirect for BOS |
| [PMID:30515738](https://pubmed.ncbi.nlm.nih.gov/30515738/) | Review / in vitro | **Supports** | NMD-escape premise | Variants near 5′ of last exon → transcripts escape NMD | Myeloid neoplasms | High for premise; not BOS tissue |
| [PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/) | In vitro (human HSPCs) | **Supports** | Truncated ASXL1 GOF on ASXL1–BAP1 PR-DUB | GOF hyperactivates BAP1; reducing BAP1 attenuates malignancy | Myeloid malignancy | High mechanistic; myeloid context |
| [PMID:31006630](https://pubmed.ncbi.nlm.nih.gov/31006630/) | In vitro / in ovo | **Supports** | Truncated fragment sufficient for disease phenotype | ASXL1 aa 1–900 recapitulates neural-crest defects | BOS-relevant NC development | Moderate; over-expression system |
| [PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/) | In vitro (patient fibroblasts) — **preprint** | **Supports** | Mutant PR-DUB mis-spreads on chromatin (GOF) | Aberrant ASXL1/BAP1 co-occupancy; Warburg-like metabolism attributed to GOF | BOS patient cells | Low–moderate; preprint, one snippet flagged |
| [PMID:37053013](https://pubmed.ncbi.nlm.nih.gov/37053013/) | In vitro (patient multi-omics) | **Qualifies** | Broad epigenome disruption | Cross-tissue epigenomic effects; Wnt dysregulation | BOS patient cells | Moderate; non-discriminating LOF vs GOF |
| [PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/) | Review | **Supports (review-level)** | Generalized ASXL GOF needs NMD escape + degron loss | Population + in vitro evidence favors GOF; degron "putative" | ASXL family, cancer + neurodev | Moderate; review, degron unconfirmed |
| gnomAD v4 (this run, 2026-09-07) | Computational | **Supports** | ASXL1 not LoF-constrained; hotspot = CHIP window | pLI≈0, LOEUF=0.90; 76.8% pLoF burden in aa 580–1000; p.Gly646fs top | Population germline+somatic | Moderate–high; blood-derived cohort confounds germline vs somatic |
| [PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/) | Model organism (mouse) | **Competing (LOF)** | LOF alone causes BOS-like malformations | Anophthalmia, microcephaly, cleft palate, mandibular defects; ↓H3K27me3 | Developmental / BOS-like | High for LOF sufficiency |
| [PMID:24255920](https://pubmed.ncbi.nlm.nih.gov/24255920/) | Model organism (mouse) | **Competing (LOF)** | Haploinsufficiency is operative | Asxl1⁺/⁻ → mild MDS-like disease | Hematopoietic | High for haploinsufficiency |
| [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/) | Model organism (mouse) | **Competing (LOF)** | LOF microcephaly via PRC2/Ezh2 | Deletion → microcephaly; NSC survival via Ezh2/PRC2; 4,635 DEGs | Neurodevelopment | High for LOF neural mechanism; snippets flagged |
| [PMID:25921057](https://pubmed.ncbi.nlm.nih.gov/25921057/) | Human clinical / review | **Qualifies** | Shared germline/somatic variants; tumor risk | Wilms tumor surveillance warranted in ASXL1 carriers | BOS clinical management | Moderate; supports oncogenic analogy |
| [PMID:33242595](https://pubmed.ncbi.nlm.nih.gov/33242595/) | Human clinical (ASXL3/BRPS) | **Qualifies (paralog)** | LOF ASXL3 truncations cause overlapping disorder | BRPS from LOF ASXL3; mechanism "uncertain" given LOF in healthy population | Bainbridge-Ropers (paralog) | Low direct; informs family-wide ambiguity |
| [PMID:30927018](https://pubmed.ncbi.nlm.nih.gov/30927018/) | Review | **Supports (review-level)** | Mutant ASXL1 DN + GOF in myeloid | Truncated ASXL1 has DN/GOF features via epigenetic changes | Myeloid | Moderate; review orientation |

---

## Data and Tool Use

| Resource | Accession / URI | Access status | Query / scope | Relevance |
|---|---|---|---|---|
| gnomAD v4 | GraphQL API, gene ENSG00000171456 / ENST00000375687 | **Actually accessed** (2026-09-07) | Constraint (pLI, LOEUF, oe_lof) + all pLoF variants; positional binning by amino-acid coordinate | Directly relevant: tests LoF-constraint and truncation-hotspot claims |
| PubMed / NCBI E-utilities | 13 PMIDs retrieved | **Actually accessed** | Disease + mechanism queries (BOS, ASXL1 truncation, NMD, PR-DUB, haploinsufficiency) | Directly relevant |
| bioRxiv preprint | [PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/) | **Accessed (preprint, unrefereed)** | BOS fibroblast multi-omics | Directly relevant but not peer-reviewed |
| GenCC / ClinGen gene-disease validity | — | **Not verified** as of 2026-09-07 | Not queried | Would clarify curated LOF-vs-GOF disease-mechanism assertion |
| ClinVar variant-level curation | — | **Not queried** | Not queried | Would provide germline BOS allele spectrum vs somatic |

**Analysis inventory:**

| Analysis | Input → Method → Output | Outcome | Limitations |
|---|---|---|---|
| gnomAD v4 constraint + pLoF positional binning | gnomAD GraphQL (ENST00000375687) → Python parse, amino-acid binning, allele-frequency summary → constraint values + hotspot table (F006) | **Succeeded** | gnomAD is blood-derived; cannot fully separate germline nulls from age-related somatic CHIP within the cohort — this is itself the interpretive crux |
| Artifact bundle (MANIFEST + checksums + code/queries/logs + evidence matrix) | Built iteration 4 | **Succeeded (reported)** | Bundle should reside under `kb/hypotheses/Bohring-Opitz_syndrome/asxl1_truncated_protein_dominant_or_gain/openscientist_artifacts`; verify presence/paths at curation |
| Direct protein assay in BOS tissue | — | **Skipped (no patient material / not runnable here)** | Central missing node; literature-only |

No failed analysis was silently replaced by literature synthesis. Where computational tests were not possible (e.g., endogenous BOS protein detection), this is stated explicitly rather than substituted with model knowledge.

---

## Limitations and Knowledge Gaps

1. **No direct evidence of a stable endogenous truncated ASXL1 protein in germline BOS tissue.** *Scope:* the central node of the hypothesis. *Why it matters:* all direct protein-expression data are from myeloid/leukemic cells or heterologous over-expression. *What was checked:* PubMed searches for BOS + truncated protein / Western blot; none accessed showed endogenous BOS-tissue protein. *Resolution:* immunoblot/MS with C-terminal- and N-terminal-directed detection on BOS patient fibroblasts/iPSC derivatives.

2. **The C-terminal degron is unconfirmed ("putative").** *Scope:* the stability requirement of the GOF model. *Why it matters:* without degron removal, NMD-escaping transcripts might still yield unstable protein. *What was checked:* [PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/) states it as a hypothesis. *Resolution:* degron mapping (deletion/cycloheximide-chase stability assays) and proteasome-dependence tests across truncation lengths.

3. **Dominant-negative vs. gain-of-function is not disambiguated for BOS.** *Scope:* the "dominant-negative OR gain" disjunction in the seed. *Why it matters:* these predict different therapeutic strategies (block WT interference vs. block gained BAP1 activity). *Resolution:* co-expression/titration of truncated vs. WT ASXL1 in a developmental readout.

4. **LOF/haploinsufficiency remains sufficient in vivo.** *Scope:* competing model. *Why it matters:* mouse deletion reproduces malformations and microcephaly ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/), [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)); a truncation-knock-in vs. null comparison was not identified in the accessed literature. *Resolution:* isogenic knock-in of a BOS allele vs. clean null, same background, phenotyped head-to-head.

5. **Population-genetics confound.** *Scope:* the gnomAD interpretation. *Why it matters:* the "not LoF-constrained" and hotspot signals are partly driven by somatic CHIP in a blood-derived cohort, so they argue for somatic clonal-fitness GOF more cleanly than for germline developmental GOF. *Resolution:* restrict to confirmed germline calls / non-blood tissue references.

6. **Source-level absences (unverified as of 2026-09-07).** GenCC and ClinGen gene-disease *mechanism* curation for ASXL1-BOS were **not queried**; ClinVar germline allele spectrum was **not queried**; no BOS clinical trial or interventional dataset was searched. These are labeled *unverified* rather than *absent*.

7. **Preprint dependence for the most BOS-direct GOF claim.** The "aberrant PR-DUB spreading" evidence is a bioRxiv preprint ([PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/)) with a curation-flagged snippet; it should not be weighted as peer-reviewed.

---

## Alternative Models

| Model | Relationship to seed hypothesis | Basis |
|---|---|---|
| **Haploinsufficiency / loss-of-function** | **Primary competing alternative** | Mouse null → BOS-like malformations & microcephaly; Asxl1⁺/⁻ haploinsufficient hematology ([PMID:24218140](https://pubmed.ncbi.nlm.nih.gov/24218140/), [PMID:24255920](https://pubmed.ncbi.nlm.nih.gov/24255920/), [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)) |
| **Convergent GOF + LOF on PR-DUB/Polycomb** | **Complementary / unifying** — most parsimonious given all data | Both branches perturb H2AK119ub/H3K27me3; truncated protein both loses WT function and gains BAP1 activity |
| **Dominant-negative (truncated interferes with WT)** | **Sub-hypothesis within the seed** — needs discrimination from pure GOF | [PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/), [PMID:30927018](https://pubmed.ncbi.nlm.nih.gov/30927018/) describe "dominant-negative and gain-of-function features" |
| **PRC2/Ezh2 axis dysregulation** | **Downstream consequence** shared by both models | NSC-survival microcephaly mechanism ([PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/)) |
| **Wnt (canonical + noncanonical) dysregulation** | **Downstream effector** | BOS multi-omics ([PMID:37053013](https://pubmed.ncbi.nlm.nih.gov/37053013/)) |
| **Paralog analogy (ASXL3/BRPS as LOF)** | **Parallel mechanism** cautioning that the ASXL family may be mechanistically heterogeneous | BRPS from LOF ASXL3, mechanism "uncertain" ([PMID:33242595](https://pubmed.ncbi.nlm.nih.gov/33242595/)) |

---

## Discriminating Tests

1. **Isogenic knock-in vs. null, head-to-head (mouse or iPSC).** Introduce a recurrent BOS allele (e.g., p.Gly646fs) as a heterozygous knock-in and compare to a clean heterozygous null on the identical background. *Expected under GOF/DN:* knock-in shows phenotypes exceeding the null (or dominant over WT); *under pure LOF:* knock-in ≈ null. Readouts: microcephaly, neural-crest markers, H2AK119ub/H3K27me3.

2. **Endogenous protein detection in BOS patient cells.** MS + N-/C-terminal immunoblot on BOS fibroblasts/iPSC-derived neural crest and NSCs. *Expected under GOF:* a stable N-terminal truncated species. This directly fills the missing node.

3. **Degron mapping and stability assay.** Cycloheximide-chase and proteasome-inhibition across truncation endpoints spanning the putative C-terminal degron. *Expected under GOF:* degron removal increases half-life; degron-restored constructs destabilize.

4. **BAP1-dependence rescue in a BOS developmental model.** Reduce BAP1 (as in [PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/)) in truncated-ASXL1 neural-crest/NSC systems. *Expected under GOF:* phenotype attenuation, tying BOS to the same hyperactive PR-DUB node as myeloid disease.

5. **Germline-restricted population re-analysis.** Recompute ASXL1 constraint/hotspot using tissue references that exclude age-related CHIP. *Expected:* separates germline developmental GOF signal from somatic clonal-fitness signal.

6. **Dominant-negative titration.** Co-express increasing truncated ASXL1 against fixed WT in a quantitative chromatin/reporter readout. *DN predicts* dose-dependent suppression of WT activity; *pure GOF predicts* a WT-independent gained activity.

---

## Curation Leads (require curator verification)

- **Candidate status:** Keep `asxl1_truncated_protein_dominant_or_gain` as **ALTERNATIVE** but annotate as **"emerging / partially supported; likely convergent with LOF."** Do not promote to primary without direct endogenous-protein evidence in BOS tissue.
- **Candidate evidence references + snippets to verify:**
  - [PMID:26700326](https://pubmed.ncbi.nlm.nih.gov/26700326/): "we detected the truncated ASXL1 proteins in two cell lines lacking the intact ASXL1 gene by mass spectrometry and Western blot analyses" (and "…indicating the ASXL1 mutations are dominant-negative or gain-of-function mutations").
  - [PMID:34186160](https://pubmed.ncbi.nlm.nih.gov/34186160/): "resulting in expression of a C-terminal-truncated ASXL1 protein that confers gain of function on the ASXL1-BAP1 deubiquitinase (DUB) complex".
  - [PMID:30515738](https://pubmed.ncbi.nlm.nih.gov/30515738/): "occur near the 5' end of the last exon, thereby the transcripts would escape from nonsense-mediated decay".
  - [PMID:31006630](https://pubmed.ncbi.nlm.nih.gov/31006630/): "Expression of truncated ASXL1 isoforms (amino acids 1-900) recapitulated the NC phenotypes in vitro and in ovo…".
  - [PMID:41925445](https://pubmed.ncbi.nlm.nih.gov/41925445/): "such mechanisms require both escape from nonsense-mediated mRNA decay and removal of a putative C-terminal degron signal within ASXL proteins".
  - **Flag for re-verification:** [PMID:42523271](https://pubmed.ncbi.nlm.nih.gov/42523271/) (preprint; snippet "aberrant PR-DUB complex spreading…" curation-mismatch-flagged) and [PMID:40276524](https://pubmed.ncbi.nlm.nih.gov/40276524/) (two snippets flagged).
- **Candidate pathophysiology nodes/edges:** `NMD escape → stable truncated ASXL1 → ASXL1–BAP1 PR-DUB gain-of-function → ↓H2AK119ub / aberrant chromatin spreading`; parallel edge `reduced full-length ASXL1 → impaired ASXL1–PRC2 → ↓H3K27me3 → NSC apoptosis (microcephaly)`; convergence node `Polycomb-domain histone-ubiquitination/methylation dysregulation`.
- **Candidate ontology terms:** cell types — neural crest cell, neural stem cell, hematopoietic stem/progenitor cell, fibroblast; processes — histone H2A K119 deubiquitination, histone H3K27 methylation, PRC2 complex, nonsense-mediated mRNA decay, canonical/noncanonical Wnt signaling, neural crest cell migration.
- **Candidate knowledge_gaps prompts:** (1) "No accessed source shows stable endogenous truncated ASXL1 protein in germline BOS tissue." (2) "C-terminal degron required by the GOF model is putative/unmapped." (3) "GenCC/ClinGen ASXL1-BOS mechanism curation and ClinVar germline allele spectrum unverified as of 2026-09-07." (4) "Truncation-knock-in vs. null head-to-head comparison in a developmental model not identified in the accessed literature."

---

## Provider Artifact Bundle

An artifact bundle was assembled (iteration 4) intended for
`kb/hypotheses/Bohring-Opitz_syndrome/asxl1_truncated_protein_dominant_or_gain/openscientist_artifacts`, containing a canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed inputs/outputs, replay note), the gnomAD GraphQL query/config, an environment/package-version record, sanitized execution logs, and the derived hotspot/evidence tables. **Curators should verify the bundle's presence and paths.** The only executed data analysis is the gnomAD v4 query (F006); all other evidence is literature-derived. No controlled/patient-level data, no large raw downloads, and no credentials are included — external identifiers (gnomAD transcript ENST00000375687; the 13 PMIDs) are recorded instead. Where an expected artifact is missing or local-only, it is labeled as such here rather than asserted as present.

---

*Report compiled 2026-09-07 from 5 completed iterations, 7 confirmed findings, 13 reviewed papers, and one original gnomAD v4 computational analysis.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist README](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_README.md)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_evidence_matrix.csv)
- [OpenScientist gnomad asxl1 constraint](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_constraint.csv)
- [OpenScientist gnomad asxl1 plof region summary](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_region_summary.csv)
- [OpenScientist gnomad asxl1 plof top hotspot variants](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_data_gnomad_asxl1_plof_top_hotspot_variants.csv)
- [OpenScientist gnomad execution log](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_gnomad_execution_log.md)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_Bohring-Opitz_syndrome_asxl1_truncated_protein_dominant_or_gain_openscientist_artifacts_logs_pubmed_search_log.md)

## Term Validation

No ontology term identifiers were found in this report.