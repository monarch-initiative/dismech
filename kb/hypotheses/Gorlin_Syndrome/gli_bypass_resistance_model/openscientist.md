---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T11:45:10.434013'
end_time: '2026-07-06T13:02:12.185183'
duration_seconds: 4621.75
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Gorlin Syndrome
  category: Mendelian
  hypothesis_group_id: gli_bypass_resistance_model
  hypothesis_label: SMO-Inhibitor Resistance via Downstream GLI Bypass
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: gli_bypass_resistance_model\nhypothesis_label:\
    \ SMO-Inhibitor Resistance via Downstream GLI Bypass\nstatus: EMERGING\ndescription:\
    \ SMO antagonists eventually fail in a substantial fraction of advanced BCCs.\
    \ Resistance arises\n  from acquired SMO mutations, SUFU loss, GLI2 amplification,\
    \ and non-canonical GLI activation that all\n  converge below the drug target,\
    \ leaving constitutive GLI output intact. This model frames the convergent\n \
    \ GLI node \u2014 not SMO \u2014 as the durable therapeutic bottleneck and motivates\
    \ GLI-directed agents for SMO-inhibitor-resistant\n  and SUFU-driven disease.\n\
    evidence:\n- reference: PMID:31036756\n  reference_title: Genomic testing, tumor\
    \ microenvironment and targeted therapy of Hedgehog-related human\n    cancers.\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Resistance to SMO inhibitors\
    \ is caused by acquired SMO mutations, SUFU deletions, GLI2 amplification,\n \
    \   other by-passing mechanisms of GLI activation and WNT/\u03B2-catenin signaling\
    \ activation.\n  explanation: Documents the downstream-of-SMO bypass mechanisms\
    \ that sustain GLI output despite SMO blockade."
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
citation_count: 24
artifact_count: 26
artifact_sources:
  openscientist_artifacts_zip: 26
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
- filename: provenance_evidence_matrix.json
  path: openscientist_artifacts/provenance_evidence_matrix.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_evidence_matrix.png
  path: openscientist_artifacts/provenance_evidence_matrix.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: provenance_final_summary.json
  path: openscientist_artifacts/provenance_final_summary.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final summary
- filename: provenance_final_summary.png
  path: openscientist_artifacts/provenance_final_summary.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final summary
- filename: provenance_knowledge_gaps.json
  path: openscientist_artifacts/provenance_knowledge_gaps.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
- filename: provenance_knowledge_gaps.png
  path: openscientist_artifacts/provenance_knowledge_gaps.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist knowledge gaps
- filename: provenance_mechanistic_diagram.json
  path: openscientist_artifacts/provenance_mechanistic_diagram.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic diagram
- filename: provenance_mechanistic_diagram.png
  path: openscientist_artifacts/provenance_mechanistic_diagram.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic diagram
- filename: provenance_plot_1.json
  path: openscientist_artifacts/provenance_plot_1.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_1.png
  path: openscientist_artifacts/provenance_plot_1.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 1
- filename: provenance_plot_2.json
  path: openscientist_artifacts/provenance_plot_2.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_2.png
  path: openscientist_artifacts/provenance_plot_2.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 2
- filename: provenance_plot_3.json
  path: openscientist_artifacts/provenance_plot_3.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_3.png
  path: openscientist_artifacts/provenance_plot_3.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 3
- filename: provenance_plot_4.json
  path: openscientist_artifacts/provenance_plot_4.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_4.png
  path: openscientist_artifacts/provenance_plot_4.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 4
- filename: provenance_plot_5.json
  path: openscientist_artifacts/provenance_plot_5.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_plot_5.png
  path: openscientist_artifacts/provenance_plot_5.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 5
- filename: provenance_plot_6.json
  path: openscientist_artifacts/provenance_plot_6.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 6
- filename: provenance_plot_6.png
  path: openscientist_artifacts/provenance_plot_6.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 6
- filename: provenance_subtype_applicability.json
  path: openscientist_artifacts/provenance_subtype_applicability.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist subtype applicability
- filename: provenance_subtype_applicability.png
  path: openscientist_artifacts/provenance_subtype_applicability.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist subtype applicability
- filename: provenance_therapeutic_landscape.json
  path: openscientist_artifacts/provenance_therapeutic_landscape.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist therapeutic landscape
- filename: provenance_therapeutic_landscape.png
  path: openscientist_artifacts/provenance_therapeutic_landscape.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist therapeutic landscape
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Gorlin Syndrome
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** gli_bypass_resistance_model
- **Hypothesis Label:** SMO-Inhibitor Resistance via Downstream GLI Bypass
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: gli_bypass_resistance_model
hypothesis_label: SMO-Inhibitor Resistance via Downstream GLI Bypass
status: EMERGING
description: SMO antagonists eventually fail in a substantial fraction of advanced BCCs. Resistance arises
  from acquired SMO mutations, SUFU loss, GLI2 amplification, and non-canonical GLI activation that all
  converge below the drug target, leaving constitutive GLI output intact. This model frames the convergent
  GLI node — not SMO — as the durable therapeutic bottleneck and motivates GLI-directed agents for SMO-inhibitor-resistant
  and SUFU-driven disease.
evidence:
- reference: PMID:31036756
  reference_title: Genomic testing, tumor microenvironment and targeted therapy of Hedgehog-related human
    cancers.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Resistance to SMO inhibitors is caused by acquired SMO mutations, SUFU deletions, GLI2 amplification,
    other by-passing mechanisms of GLI activation and WNT/β-catenin signaling activation.
  explanation: Documents the downstream-of-SMO bypass mechanisms that sustain GLI output despite SMO blockade.
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


## Output

# SMO-Inhibitor Resistance via Downstream GLI Bypass in Gorlin Syndrome: Hypothesis Evaluation Report

**Hypothesis ID:** gli_bypass_resistance_model  
**Status in KB:** EMERGING  
**Report Date:** 2026-07-06  
**Papers Reviewed:** 68  
**Findings Confirmed:** 15  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the GLI bypass model is a real and well-documented resistance mechanism, but it is neither universal nor sufficient to explain all SMO-inhibitor resistance in Gorlin syndrome.**

The hypothesis that SMO antagonists fail because resistance mechanisms converge on constitutive GLI output downstream of the drug target is supported by strong mechanistic evidence across multiple tumor types. Four distinct GLI-maintaining bypass routes — acquired SMO mutations, SUFU loss-of-function, GLI2 amplification, and non-canonical GLI activation via aPKC-ι/λ — are each validated by primary experimental data. However, at least three GLI-independent resistance mechanisms have been identified (cilia-loss/RAS-MAPK pathway switching, BCC-to-SCC lineage transition, and WNT-dependent persister cell identity switching), demonstrating that the hypothesis oversimplifies resistance biology by framing GLI as the sole therapeutic bottleneck. Critically, the model's applicability varies by disease subtype: it is strongest for SUFU-driven Gorlin disease (BCNS2/MHIBCC), where pathway activation occurs inherently below SMO; it is well-supported for sporadic advanced BCC (~50% of resistant tumors harbor SMO mutations); but it is limited for PTCH1-mutant Gorlin syndrome, where resistance is rare and, when it occurs, may involve lineage switching rather than GLI convergence. The therapeutic corollary — that GLI-directed agents will overcome resistance — has preclinical support from BET inhibitors, HDAC inhibitors, and aPKC inhibitors, but the only clinical test (arsenic trioxide + itraconazole, n=5) achieved pharmacodynamic GLI suppression without meaningful clinical responses. We recommend upgrading the hypothesis status from EMERGING to PARTIALLY SUPPORTED with mandatory subtype stratification.

---

## Summary

The GLI bypass resistance model proposes that SMO antagonists (vismodegib, sonidegib) fail in advanced basal cell carcinoma (BCC) because resistance mechanisms — acquired SMO mutations, SUFU loss, GLI2 amplification, and non-canonical GLI activation — all converge downstream of the drug target, maintaining constitutive GLI transcriptional output. This model frames GLI, not SMO, as the durable therapeutic bottleneck and motivates development of GLI-directed agents for resistant disease.

Our systematic evaluation across 68 papers and 5 investigative iterations confirms that GLI-convergent resistance is a major mechanism, particularly in sporadic advanced BCC where acquired SMO mutations account for approximately 50% of resistant cases, and in SUFU-driven disease where pathway activation inherently bypasses SMO. However, we identified critical boundaries to the model. First, at least three resistance pathways are entirely GLI-independent: primary cilia loss driving a HH-to-RAS/MAPK switch, BCC-to-squamous cell carcinoma lineage transition, and a WNT-dependent persister cell state that precedes genetic resistance. Second, the model's relevance to Gorlin syndrome specifically is complex: PTCH1-mutant Gorlin BCCs are initially more uniformly responsive to SMO inhibitors than sporadic BCCs, and when rare resistance emerges after long-term therapy, the documented mechanism involves lineage switching rather than GLI bypass. Third, despite strong preclinical rationale, clinical translation of GLI-directed therapy has been disappointing — the sole clinical trial showed pharmacodynamic proof-of-concept but failed to produce durable responses.

These findings support reconceptualizing the hypothesis from a universal resistance model to a subtype-specific mechanism that must be integrated with GLI-independent resistance pathways and temporal dynamics (early tolerance vs. late genetic resistance) for accurate clinical application.

{{figure:final_summary.png|caption=Comprehensive six-panel summary of the GLI bypass resistance model: evidence classification, subtype applicability, temporal dynamics, and therapeutic landscape}}

---

## Key Findings

### Finding 1: SMO Mutations Account for ~50% of Acquired Resistance in Sporadic BCC

Atwood et al. (2015) performed comprehensive sequencing of 44 resistant BCCs and identified SMO mutations in 50% (22/44) of cases ([PMID: 25759020](https://pubmed.ncbi.nlm.nih.gov/25759020/)). These mutations segregated into two functional classes: ligand-binding-pocket mutations (4 variants) that disrupt drug binding, and constitutive-activity mutations (4 variants) that render SMO active regardless of inhibitor presence. Crucially, both mutation classes maintained Hedgehog signaling in the presence of SMO inhibitors but responded to aPKC-ι/λ or GLI2 inhibitors operating downstream of SMO, directly validating the therapeutic logic of the GLI bypass model. This represents the strongest quantitative evidence for the hypothesis, though it also implies that the other 50% of resistant tumors may harbor non-SMO mechanisms.

### Finding 2: aPKC-ι/λ Is a Non-Canonical GLI Activator Driving Resistance

Atwood et al. (2013) identified atypical protein kinase C ι/λ (aPKC-ι/λ) as a novel GLI regulator that functions downstream of SMO ([PMID: 23446420](https://pubmed.ncbi.nlm.nih.gov/23446420/)). aPKC-ι/λ directly phosphorylates and activates GLI1, resulting in maximal DNA binding and transcriptional activation. Importantly, activated aPKC-ι/λ was specifically upregulated in SMO-inhibitor-resistant tumors, and targeting aPKC-ι/λ suppressed signaling and growth of resistant BCC cell lines. Since the PRKCI gene (encoding aPKC-ι/λ) is itself a Hedgehog target gene, this creates a positive feedback loop that can sustain GLI output even when canonical SMO signaling is pharmacologically blocked. Genome-wide profiling confirmed that aPKC-ι/λ and SMO control similar gene sets, establishing aPKC-ι/λ as a bona fide non-canonical GLI activation pathway.

### Finding 3: SUFU Loss and GLI2/MYCN Amplification Confer Primary Resistance in SHH Medulloblastoma

Kool et al. (2014) sequenced 133 SHH-medulloblastomas and demonstrated genotype-dependent drug response ([PMID: 24651015](https://pubmed.ncbi.nlm.nih.gov/24651015/)). PTCH1-mutant tumors were responsive to SMO inhibition, whereas tumors harboring SUFU mutations (concentrated in infants) or MYCN amplification (concentrated in children >3 years) were primarily resistant. This finding is pivotal because it demonstrates that downstream pathway lesions confer not just acquired but **primary** resistance to SMO inhibitors, and it establishes the principle that genetic stratification by pathway level predicts drug response.

### Finding 4: BET Bromodomain Inhibition Overcomes Resistance by Epigenetically Suppressing GLI Transcription

Tang et al. (2014) demonstrated that BRD4 directly occupies GLI1 and GLI2 promoters, and the BET inhibitor JQ1 suppressed growth of patient-derived and genetically engineered mouse model (GEMM) Hedgehog-driven tumors even when harboring genetic lesions rendering them resistant to SMO antagonists, including SUFU loss ([PMID: 24973920](https://pubmed.ncbi.nlm.nih.gov/24973920/)). This provides the strongest preclinical proof-of-concept for the therapeutic arm of the GLI bypass hypothesis — that targeting the convergent GLI node with epigenetic approaches can overcome diverse upstream resistance mechanisms.

### Finding 5: The D473H SMO Mutation Was the First Clinical Resistance Mechanism Identified

Yauch et al. (2009) identified the D473H SMO mutation in a medulloblastoma patient who relapsed after initial response to GDC-0449 (vismodegib) ([PMID: 19726788](https://pubmed.ncbi.nlm.nih.gov/19726788/)). The mutation disrupted drug binding without affecting HH signaling. Dijkgraaf et al. (2011) extended this work, confirming all functional D473 substitutions were resistant and identifying focal amplifications of GLI2 and cyclin D1 (Ccnd1) in additional resistant models ([PMID: 21123452](https://pubmed.ncbi.nlm.nih.gov/21123452/)). These landmark findings established the clinical reality of both SMO-mutant and downstream-bypass resistance.

### Finding 6: BCC-to-SCC Lineage Transition Is a GLI-Independent Resistance Mechanism in Gorlin Syndrome

Jussila et al. (2024) used multiomics and spatial transcriptomics on a Gorlin syndrome patient's SMO-inhibitor-resistant tumor after approximately 10 years of treatment ([PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/)). The resistant clone had undergone a basal-to-squamous cell carcinoma transition — a lineage switch that is Hedgehog-pathway-independent. They nominated PCYT2, ETNK1, and the phosphatidylethanolamine biosynthetic pathway as genetic suppressors of this transition. This is arguably the most important finding for the Gorlin-specific context of the hypothesis, as it demonstrates that the predominant documented mechanism of resistance in PTCH1-mutant Gorlin syndrome does **not** involve GLI convergence.

### Finding 7: Primary Cilia Loss Drives HH-to-RAS/MAPK Pathway Switch

Kuonen et al. (2019) demonstrated that loss of primary cilia in resistant BCCs drives a switch from Hedgehog pathway dependency to RAS/MAPK pathway activation ([PMID: 30707899](https://pubmed.ncbi.nlm.nih.gov/30707899/)). This represents resistance that abandons HH/GLI signaling entirely rather than maintaining it through downstream bypass, directly contradicting the universality of the GLI convergence model.

### Finding 8: Gorlin BCCs Show Distinct Resistance Biology Compared to Sporadic BCCs

Jussila et al. (2024) explicitly stated that "sporadic basal cell carcinomas display high resistance rates, whereas tumors arising in patients with Gorlin syndrome with germline Patched (PTCH1) alterations are uniformly suppressed by inhibitor therapy" ([PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/)). In rare cases after long-term therapy, individual resistant tumor clones emerge, but the basis of this resistance "remains unstudied." This fundamentally recontextualizes the hypothesis: the GLI bypass model, largely derived from sporadic BCC data, may not directly apply to the Gorlin syndrome setting where resistance is both rarer and mechanistically distinct.

### Finding 9: WNT-Dependent Persister Cells Represent an Early Tolerance Phase

Biehs et al. (2018) demonstrated that residual BCC cells survive Hedgehog pathway inhibition through a cell identity switch to a WNT-dependent, Hedgehog-independent state ([PMID: 30297801](https://pubmed.ncbi.nlm.nih.gov/30297801/)). This persister mechanism represents an early tolerance phase that is distinct from the genetic resistance mechanisms in the GLI bypass model, suggesting a two-phase resistance model: initial WNT-dependent persistence followed by potential acquisition of genetic GLI-convergent or GLI-independent resistance.

### Finding 10: SUFU-Driven Disease Is Inherently SMO-Inhibitor Resistant

Schulman et al. (2016) identified germline SUFU mutations with acquired SUFU LOH in MHIBCC patients and explicitly noted that "the downstream location of the SUFU gene within the sonic hedgehog pathway may explain why its loss is associated with relatively well-differentiated tumors and suggests that MHIBCC will not respond to therapeutic strategies, such as smoothened inhibitors, that target upstream components of this pathway" ([PMID: 26677003](https://pubmed.ncbi.nlm.nih.gov/26677003/)). Russell-Goldman et al. (2021) confirmed that infundibulocystic BCCs are enriched for genetic alterations downstream of PTCH1, involving SUFU, SMO, GLI1, and GLI2 ([PMID: 32796174](https://pubmed.ncbi.nlm.nih.gov/32796174/)). This makes SUFU-driven Gorlin disease (BCNS2/MHIBCC) the subtype where the GLI bypass model is most directly applicable.

### Finding 11: Clinical GLI-Directed Therapy Shows Pharmacodynamic but Not Clinical Success

Ally et al. (2016) treated 5 men with metastatic BCC who relapsed after SMO inhibitor with arsenic trioxide + itraconazole ([PMID: 26765315](https://pubmed.ncbi.nlm.nih.gov/26765315/)). The combination reduced GLI1 mRNA levels by 75% from baseline (P<0.05), demonstrating pharmacodynamic proof of concept for GLI suppression. However, only 3/5 patients completed 3 cycles, adverse effects included grade 4 leukopenia with grade 3 infection, and tumor responses were insufficient to continue development. This critical finding reveals a gap between the hypothesis's therapeutic prediction and clinical reality.

### Finding 12: Multiple Preclinical GLI-Targeting Strategies Validated

Beyond BET inhibitors, class I HDAC inhibitors (4SC-202/domatinostat) efficiently block HH/GLI signaling and overcome SMO-inhibitor resistance in both sensitive and resistant cells ([PMID: 29055107](https://pubmed.ncbi.nlm.nih.gov/29055107/)). Additional mechanisms include daunorubicin-mediated β-TrCP-dependent GLI1 ubiquitination and proteasomal degradation ([PMID: 38757343](https://pubmed.ncbi.nlm.nih.gov/38757343/)), and KCTD1-mediated modulation of the KCASH/HDAC1/GLI1 axis ([PMID: 37597490](https://pubmed.ncbi.nlm.nih.gov/37597490/)). These diverse mechanisms validate GLI as a druggable node but none have reached clinical testing in BCC resistance.

### Finding 13: High Real-World Resistance Rates in Advanced BCC but Lower in Gorlin-Specific Cohorts

Gan et al. (2025) reported Australian real-world data showing 77% secondary acquired drug resistance in advanced BCC patients after a median of 13 months ([PMID: 40492880](https://pubmed.ncbi.nlm.nih.gov/40492880/)). By contrast, Palmeiro et al. (2024) in a systematic review of 351 Gorlin patients found treatment interruption due to secondary resistance in only 9.1% ([PMID: 38867459](https://pubmed.ncbi.nlm.nih.gov/38867459/)). This differential resistance rate reinforces that Gorlin PTCH1-mutant BCCs are fundamentally more sensitive, with resistance being comparatively rare.

---

## Mechanistic Causal Chain

The GLI bypass resistance model implies a specific causal chain from upstream trigger to clinical manifestation. Below we map this chain and assess the evidence strength at each link.

```
UPSTREAM TRIGGER
    │
    ▼
[1] Gorlin Syndrome: Germline PTCH1 (BCNS1) or SUFU (BCNS2) loss-of-function
    │                                                          
    │  (STRONG: PMID 8981943, 28596197, 41129277)             
    ▼                                                          
[2] Constitutive HH pathway activation → BCC development
    │
    │  (STRONG: canonical HH biology)
    ▼
[3] SMO inhibitor therapy (vismodegib/sonidegib)
    │
    ├──→ [3a] PTCH1-mutant Gorlin BCCs: uniform initial suppression (STRONG)
    │         │
    │         ├──→ [3a-i] Long-term therapy → RARE resistant clones
    │         │           │
    │         │           ├──→ BCC-to-SCC lineage transition (SUPPORTED: PMID 38157930)
    │         │           ├──→ GLI bypass mechanisms? (SPECULATIVE for Gorlin)
    │         │           └──→ Unknown mechanisms (UNSTUDIED)
    │         │
    │         └──→ WNT-dependent persister state (EMERGING: PMID 30297801)
    │
    ├──→ [3b] SUFU-mutant disease: PRIMARY/INHERENT resistance (STRONG: PMID 26677003)
    │         └──→ Pathway activation below SMO → GLI bypass model DIRECTLY APPLIES
    │
    └──→ [3c] Sporadic BCC: variable resistance (~50%+ over time)
              │
              ├──→ Acquired SMO mutations (50% of cases; STRONG: PMID 25759020)
              │     └──→ Respond to downstream GLI/aPKC inhibitors
              │
              ├──→ GLI2 amplification (SUPPORTED: PMID 21123452)
              ├──→ aPKC-ι/λ upregulation → non-canonical GLI activation (STRONG: PMID 23446420)
              ├──→ Cilia loss → RAS/MAPK switch [GLI-INDEPENDENT] (PMID 30707899)
              └──→ SUFU loss (rare in sporadic; PMID 31036756)

CONVERGENCE POINT (Hypothesis Focus):
    │
    ▼
[4] Constitutive GLI transcriptional output despite SMO blockade
    │
    │  (STRONG for mechanisms 3b, 3c-SMO, 3c-GLI2, 3c-aPKC)
    │  (NOT APPLICABLE for 3a-i lineage switch, 3c-cilia loss)
    ▼
[5] Therapeutic bottleneck: GLI-directed agents needed
    │
    │  ◄── Preclinical: BET inhibitors (STRONG: PMID 24973920)
    │  ◄── Preclinical: HDAC inhibitors (STRONG: PMID 29055107)
    │  ◄── Preclinical: aPKC inhibitors (STRONG: PMID 23446420)
    │  ◄── Clinical: ATO+itraconazole (WEAK: PMID 26765315)
    ▼
[6] Clinical outcome: tumor regression in resistant disease
    │
    └──→ NOT YET DEMONSTRATED in clinical trials
```

**Evidence strength assessment:**
- **Links 1–3**: Strong, well-established through decades of genetic and clinical research
- **Link 3→4 (GLI convergence)**: Strong for sporadic BCC and SUFU-driven disease; weak/inapplicable for PTCH1-mutant Gorlin resistance
- **Link 4→5 (GLI as therapeutic target)**: Strong preclinical rationale; unproven clinically
- **Link 5→6 (clinical benefit)**: Missing — the critical gap in the hypothesis

{{figure:mechanistic_diagram.png|caption=Mechanistic causal chain diagram showing pathway from upstream genetic triggers through resistance mechanisms to therapeutic targets}}

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Disease Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|-----------------|------------|
| [PMID: 25759020](https://pubmed.ncbi.nlm.nih.gov/25759020/) | Human clinical + in vitro | **Supports** | Acquired SMO mutations maintain GLI output | SMO mutations in 50% of 44 resistant BCCs; respond to GLI/aPKC inhibitors | Sporadic advanced BCC | High |
| [PMID: 23446420](https://pubmed.ncbi.nlm.nih.gov/23446420/) | In vitro + model organism | **Supports** | Non-canonical GLI activation bypasses SMO | aPKC-ι/λ phosphorylates GLI1, upregulated in resistant tumors | BCC cell lines, resistant tumors | High |
| [PMID: 24651015](https://pubmed.ncbi.nlm.nih.gov/24651015/) | Human clinical + xenograft | **Supports** | Downstream lesions confer primary resistance | SUFU-mutant and MYCN-amplified SHH-MB resist SMO inhibition | SHH medulloblastoma | High |
| [PMID: 24973920](https://pubmed.ncbi.nlm.nih.gov/24973920/) | In vitro + model organism | **Supports** | GLI is targetable via epigenetics | BET inhibitor JQ1 overcomes SMO-resistant tumors including SUFU-loss | BCC, MB, ATRT | High |
| [PMID: 19726788](https://pubmed.ncbi.nlm.nih.gov/19726788/) | Human clinical | **Supports** | Acquired SMO mutation blocks drug binding | D473H SMO mutation in relapsed MB patient | Medulloblastoma | High |
| [PMID: 21123452](https://pubmed.ncbi.nlm.nih.gov/21123452/) | In vitro + model organism | **Supports** | Resistance can occur downstream of SMO | GLI2 and Ccnd1 amplification in resistant models | BCC/MB models | High |
| [PMID: 29055107](https://pubmed.ncbi.nlm.nih.gov/29055107/) | In vitro | **Supports** | Class I HDACs are druggable GLI regulators | 4SC-202 blocks GLI in both sensitive and resistant cells | BCC cell lines | Moderate |
| [PMID: 22391311](https://pubmed.ncbi.nlm.nih.gov/22391311/) | Review + mechanistic | **Supports** | ATO directly inhibits GLI zinc fingers | ATO binds cysteine residues in GLI zinc finger domains | Pan-cancer (APL-approved) | Moderate |
| [PMID: 26677003](https://pubmed.ncbi.nlm.nih.gov/26677003/) | Human clinical + genetic | **Supports** | SUFU loss predicts SMO-inhibitor resistance | SUFU splice-site mutation + LOH in MHIBCC; predicts non-response | MHIBCC/BCNS2 | High |
| [PMID: 32796174](https://pubmed.ncbi.nlm.nih.gov/32796174/) | Human clinical + genetic | **Supports** | IBCCs enriched for downstream HH alterations | SUFU, SMO, GLI1, GLI2 alterations in infundibulocystic BCCs | IBCC | High |
| [PMID: 26765315](https://pubmed.ncbi.nlm.nih.gov/26765315/) | Human clinical trial | **Qualifies** | GLI suppression → clinical benefit | ATO+itraconazole reduced GLI1 by 75% but poor clinical response | Metastatic BCC (n=5) | Moderate (small n) |
| [PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/) | Human clinical + multiomics | **Qualifies/Competes** | Gorlin resistance is GLI-convergent | BCC-to-SCC lineage transition (GLI-independent) in Gorlin | Gorlin syndrome (PTCH1) | High |
| [PMID: 30707899](https://pubmed.ncbi.nlm.nih.gov/30707899/) | Model organism | **Competes** | Resistance maintains GLI dependency | Cilia loss → HH-to-RAS/MAPK switch (abandons GLI) | Resistant BCC | Moderate-High |
| [PMID: 30297801](https://pubmed.ncbi.nlm.nih.gov/30297801/) | Model organism + human | **Competes** | Resistance is GLI-convergent genetic event | WNT-dependent cell identity switch (early tolerance) | BCC under HHI | High |
| [PMID: 40492880](https://pubmed.ncbi.nlm.nih.gov/40492880/) | Human clinical (real-world) | **Qualifies** | Resistance is common in Gorlin | 77% secondary resistance in advanced BCC after 13 months | Australian advanced BCC | Moderate |
| [PMID: 38867459](https://pubmed.ncbi.nlm.nih.gov/38867459/) | Systematic review | **Qualifies** | Gorlin BCCs commonly resist HHIs | Only 9.1% treatment interruption due to secondary resistance in Gorlin | Gorlin (351 patients) | Moderate-High |
| [PMID: 31036756](https://pubmed.ncbi.nlm.nih.gov/31036756/) | Review | **Supports** | Multiple GLI bypass mechanisms exist | Documents SMO mutations, SUFU deletions, GLI2 amplification, WNT activation | Pan-HH cancer | Low (review) |
| [PMID: 33608498](https://pubmed.ncbi.nlm.nih.gov/33608498/) | In vitro | **Supports** | Non-genetic pathway activation below SMO | SNEP1 promotes SuFu degradation, reduces HH inhibitor sensitivity | Colorectal cancer | Low (non-BCC) |

{{figure:evidence_matrix.png|caption=Evidence matrix heatmap showing support level and confidence for each mechanistic claim across the literature}}

---

## Subtype-Specific Applicability

The GLI bypass model's relevance varies dramatically by disease subtype, which is a critical qualification that the original hypothesis does not address.

### Strongest Applicability: SUFU-Driven Gorlin Disease (BCNS2/MHIBCC)

SUFU-mutant disease represents the purest test case for the GLI bypass model. Because SUFU functions downstream of SMO as a negative regulator of GLI proteins, its loss-of-function directly activates GLI independently of SMO. This predicts **inherent/primary** resistance to SMO inhibitors — not acquired resistance. Multiple lines of evidence confirm this: Schulman et al. (2016) explicitly predicted non-response based on pathway topology ([PMID: 26677003](https://pubmed.ncbi.nlm.nih.gov/26677003/)); Kool et al. (2014) demonstrated primary resistance in SUFU-mutant SHH-medulloblastoma ([PMID: 24651015](https://pubmed.ncbi.nlm.nih.gov/24651015/)); and Russell-Goldman et al. (2021) showed enrichment of downstream alterations in infundibulocystic BCCs ([PMID: 32796174](https://pubmed.ncbi.nlm.nih.gov/32796174/)). Van Dal et al. (2024) confirmed that SUFU mutation carriers represent a distinct patient group ([PMID: 39276021](https://pubmed.ncbi.nlm.nih.gov/39276021/)).

### Moderate Applicability: Sporadic Advanced BCC

In sporadic BCC, the GLI bypass model explains a significant fraction — but not all — of acquired resistance. Atwood et al. (2015) quantified SMO mutations at 50% of resistant cases ([PMID: 25759020](https://pubmed.ncbi.nlm.nih.gov/25759020/)), with additional cases attributable to GLI2 amplification and aPKC-ι/λ activation. However, the remaining cases include GLI-independent mechanisms such as cilia-loss/RAS-MAPK switching and potentially WNT-dependent persistence.

### Limited Applicability: PTCH1-Mutant Gorlin Syndrome

This is the most common form of Gorlin syndrome and, paradoxically, where the GLI bypass model is least supported. PTCH1-mutant Gorlin BCCs are "uniformly suppressed" by SMO inhibitor therapy ([PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/)), with resistance being rare. When resistance does emerge after long-term therapy (years, not months), the documented mechanism is BCC-to-SCC lineage transition — a GLI-independent process. The systematic review by Palmeiro et al. (2024) found only 9.1% secondary resistance in 351 Gorlin patients ([PMID: 38867459](https://pubmed.ncbi.nlm.nih.gov/38867459/)), versus 77% in advanced sporadic BCC ([PMID: 40492880](https://pubmed.ncbi.nlm.nih.gov/40492880/)).

{{figure:subtype_applicability.png|caption=Subtype-specific applicability map showing how the GLI bypass model's relevance varies across SUFU-driven, sporadic BCC, and PTCH1-mutant Gorlin disease}}

---

## Evidence Base: Key Literature

### Foundational Evidence Supporting the Hypothesis

**Atwood et al. (2015)** — *Smoothened variants explain the majority of drug resistance in basal cell carcinoma* ([PMID: 25759020](https://pubmed.ncbi.nlm.nih.gov/25759020/)). The single most important paper for the hypothesis. Sequenced 44 resistant BCCs and found SMO mutations in 50%, divided into two functional classes. Critically demonstrated that "both classes of SMO variants respond to aPKC-ι/λ or GLI2 inhibitors that operate downstream of SMO, setting the stage for the clinical use of GLI antagonists." This paper provides the quantitative foundation and the therapeutic logic.

**Atwood et al. (2013)** — *GLI activation by atypical protein kinase C ι/λ regulates the growth of basal cell carcinomas* ([PMID: 23446420](https://pubmed.ncbi.nlm.nih.gov/23446420/)). Identified aPKC-ι/λ as a novel non-canonical GLI activator that "functions downstream of SMO to phosphorylate and activate GLI1." Showed activated aPKC-ι/λ is upregulated in SMO-inhibitor-resistant tumors, establishing one of the key non-canonical bypass routes.

**Yauch et al. (2009)** and **Dijkgraaf et al. (2011)** — *Smoothened mutation confers resistance to a Hedgehog pathway inhibitor in medulloblastoma* ([PMID: 19726788](https://pubmed.ncbi.nlm.nih.gov/19726788/)) and *Small molecule inhibition of GDC-0449 refractory smoothened mutants and downstream mechanisms of drug resistance* ([PMID: 21123452](https://pubmed.ncbi.nlm.nih.gov/21123452/)). The landmark papers identifying the first clinical resistance mechanism (D473H SMO) and extending to downstream bypass via GLI2 and Ccnd1 amplification.

**Tang et al. (2014)** — *Epigenetic targeting of Hedgehog pathway transcriptional output through BET bromodomain inhibition* ([PMID: 24973920](https://pubmed.ncbi.nlm.nih.gov/24973920/)). Demonstrated that "patient- and GEMM-derived Hedgehog-driven tumors respond to JQ1 even when harboring genetic lesions rendering them resistant to Smoothened antagonists." BRD4 directly occupies GLI1 and GLI2 promoters, providing the epigenetic mechanism.

**Gruber et al. (2018)** — *Targeting class I histone deacetylases by the novel small molecule inhibitor 4SC-202 blocks oncogenic hedgehog-GLI signaling and overcomes smoothened inhibitor resistance* ([PMID: 29055107](https://pubmed.ncbi.nlm.nih.gov/29055107/)). Showed that "4SC-202 treatment abrogates GLI activation and HH target gene expression in both SMOi-sensitive and -resistant cells," positioning HDAC inhibitors as practical GLI-directed agents.

### Evidence Qualifying or Competing with the Hypothesis

**Jussila et al. (2024)** — *Acquisition of Drug Resistance in Basal Cell Nevus Syndrome Tumors through Basal to Squamous Cell Carcinoma Transition* ([PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/)). The most important paper for Gorlin-specific context. Demonstrated that Gorlin tumors develop resistance through BCC-to-SCC lineage transition, a GLI-independent mechanism. Also established that PTCH1-mutant Gorlin BCCs are fundamentally more sensitive than sporadic BCCs.

**Kuonen et al. (2019)** — *Loss of Primary Cilia Drives Switching from Hedgehog to Ras/MAPK Pathway in Resistant Basal Cell Carcinoma* ([PMID: 30707899](https://pubmed.ncbi.nlm.nih.gov/30707899/)). Demonstrated a complete pathway switch that abandons GLI dependency.

**Biehs et al. (2018)** — *A cell identity switch allows residual BCC to survive Hedgehog pathway inhibition* ([PMID: 30297801](https://pubmed.ncbi.nlm.nih.gov/30297801/)). Identified WNT-dependent persister cells as an early tolerance mechanism preceding genetic resistance.

**Ally et al. (2016)** — *Effects of Combined Treatment With Arsenic Trioxide and Itraconazole in Patients With Refractory Metastatic Basal Cell Carcinoma* ([PMID: 26765315](https://pubmed.ncbi.nlm.nih.gov/26765315/)). The only clinical trial of GLI-directed therapy in resistant BCC. GLI1 mRNA reduced by 75% (P<0.05) but clinical responses were inadequate. This critical result challenges the therapeutic corollary of the hypothesis.

### Evidence on the Immune Checkpoint Alternative

**Stratigos et al. (2021)** — *Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy* ([PMID: 34000246](https://pubmed.ncbi.nlm.nih.gov/34000246/)). Phase 2 trial showing 31% objective response rate with cemiplimab after HHI failure, including 6% complete responses. This mechanism-agnostic approach now represents standard second-line therapy.

{{figure:therapeutic_landscape.png|caption=GLI-directed therapeutic landscape showing preclinical agents, their mechanisms, and the gap between pharmacodynamic and clinical efficacy}}

---

## Limitations and Knowledge Gaps

### Critical Knowledge Gaps

| Gap | Scope | Why It Matters | What Was Checked | Resolving Evidence Needed |
|-----|-------|---------------|------------------|--------------------------|
| **Gorlin-specific resistance mechanisms** | High | Only 1 Gorlin patient's resistance studied molecularly; hypothesis derives from sporadic BCC data | Searched for Gorlin + resistance + GLI; found PMID 38157930 only | Multi-patient genomic study of resistant Gorlin tumors with paired pre/post treatment biopsies |
| **Clinical efficacy of GLI-directed agents** | Critical | The therapeutic corollary is untested at meaningful scale | Found only PMID 26765315 (n=5, ATO+itraconazole); no trials of BET or HDAC inhibitors in resistant BCC | Phase I/II trials of BET or HDAC inhibitors in SMO-resistant BCC with GLI biomarker stratification |
| **Relative frequency of GLI-convergent vs. GLI-independent resistance** | High | Cannot assess hypothesis universality without this | PMID 25759020 addresses SMO mutations (50%); remaining 50% uncharacterized at GLI level | Large-cohort sequencing + transcriptomics of resistant BCCs with GLI activity measurement |
| **Temporal dynamics: tolerance → resistance** | Moderate | WNT-persister state may precede GLI-convergent genetic resistance, changing therapeutic windows | PMID 30297801 established persister concept; no longitudinal studies linking to subsequent genetic resistance | Longitudinal biopsy studies during HHI treatment tracking WNT/HH/GLI activity over time |
| **SUFU-driven disease: GLI inhibitor response** | High | SUFU loss is the strongest predicted responder to GLI agents, but no clinical data exist | No clinical trials found specifically in SUFU-mutant BCC/MHIBCC | Basket trial of GLI-directed agents in SUFU-mutant tumors across cancer types |
| **Biomarkers for resistance subtype** | Moderate | Without biomarkers, cannot stratify patients to appropriate therapy | No validated biomarker panel identified in the literature | Development of a composite biomarker (GLI activity, cilia status, WNT markers, SCC markers) |
| **GenCC/ClinGen evidence for SUFU resistance** | Low-Moderate | Disease-mechanism annotations may need updating to include SMO-inhibitor resistance prediction | Searched for SUFU-BCNS2 annotations; found clinical descriptions but not formal resistance annotations | Formal ClinGen curation of SUFU-BCNS2 with therapy-relevant assertions |

### Methodological Limitations of This Review

1. **Small sample sizes**: The clinical GLI-targeting trial had only 5 patients; most mechanistic studies use cell lines or mouse models.
2. **Cross-cancer extrapolation**: Much evidence comes from SHH-medulloblastoma, which may not fully translate to BCC resistance biology.
3. **Publication bias**: GLI-convergent resistance mechanisms may be over-represented because they are more tractable to study than lineage plasticity or pathway switching.
4. **Gorlin-specific data scarcity**: Despite being the hypothesis's target disease, Gorlin syndrome resistance data are sparse — most resistance data come from sporadic BCC.
5. **Temporal confounding**: The distinction between early tolerance (WNT-persister) and late genetic resistance (GLI-convergent) is not captured in most cross-sectional resistance studies.

---

## Alternative and Competing Models

### 1. WNT-Dependent Persister Model
- **Relationship to seed hypothesis**: Upstream precursor / complementary
- **Key evidence**: Biehs et al. 2018 ([PMID: 30297801](https://pubmed.ncbi.nlm.nih.gov/30297801/))
- **Description**: Residual BCC cells survive HHI via identity switch to WNT-dependent state before acquiring genetic resistance. This suggests a two-phase model where early intervention with WNT inhibitors might prevent later emergence of GLI-convergent or GLI-independent resistance.
- **Implications**: The GLI bypass model may describe the second phase of a two-phase process; targeting WNT-dependent persisters early could prevent the need for GLI-directed agents.

### 2. BCC-to-SCC Lineage Transition Model
- **Relationship to seed hypothesis**: Alternative / competing
- **Key evidence**: Jussila et al. 2024 ([PMID: 38157930](https://pubmed.ncbi.nlm.nih.gov/38157930/))
- **Description**: Resistant clones undergo complete lineage reprogramming to squamous identity, abandoning Hedgehog dependency entirely. Mediated by phosphatidylethanolamine biosynthetic pathway alterations (PCYT2/ETNK1). Particularly relevant to Gorlin syndrome, where it is the only documented resistance mechanism.
- **Implications**: GLI-directed agents would be ineffective against this form of resistance; different therapeutic strategies are needed for lineage-switching tumors.

### 3. Cilia-Loss/RAS-MAPK Switch Model
- **Relationship to seed hypothesis**: Alternative / competing
- **Key evidence**: Kuonen et al. 2019 ([PMID: 30707899](https://pubmed.ncbi.nlm.nih.gov/30707899/))
- **Description**: Loss of primary cilia decouples tumor cells from HH signaling entirely and redirects oncogenic dependency to RAS/MAPK pathway. Requires MEK/ERK inhibitor therapy rather than GLI-directed agents.
- **Implications**: Cilia status may serve as a biomarker to stratify between GLI-directed and MAPK-directed therapeutic strategies.

### 4. Immune Checkpoint Model
- **Relationship to seed hypothesis**: Parallel therapeutic strategy
- **Key evidence**: Cemiplimab trial ([PMID: 34000246](https://pubmed.ncbi.nlm.nih.gov/34000246/)); Nivolumab trial ([PMID: 36335780](https://pubmed.ncbi.nlm.nih.gov/36335780/))
- **Description**: PD-1 blockade achieves 31% objective response rate in HHI-resistant laBCC regardless of resistance mechanism. This agnostic approach is now the established second-line therapy and may be more practical than mechanism-specific GLI targeting.
- **Implications**: Clinical development of GLI-directed agents may be outpaced by immune checkpoint therapy as second-line standard of care.

### 5. SOX9-mTOR Axis Model
- **Relationship to seed hypothesis**: Downstream / complementary
- **Key evidence**: [PMID: 29550418](https://pubmed.ncbi.nlm.nih.gov/29550418/)
- **Description**: SOX9 transcriptionally regulates mTOR in BCC cells, providing a druggable downstream target with clinically available mTOR inhibitors (rapamycin). Could bypass the difficulty of directly targeting GLI transcription factors.
- **Implications**: mTOR inhibition could represent a more clinically accessible downstream target than GLI itself.

---

## Discriminating Tests

### Test 1: Multi-Patient Gorlin Resistance Genomics
- **Objective**: Determine whether GLI-convergent vs. GLI-independent mechanisms predominate in Gorlin-specific resistance
- **Patient stratification**: PTCH1-mutant Gorlin patients with documented secondary resistance to HHIs (≥10 patients)
- **Sample type**: Paired pre-treatment and resistant tumor biopsies
- **Assays**: Whole-exome sequencing, RNA-seq (including GLI target gene signatures), spatial transcriptomics
- **Biomarkers**: GLI1/GLI2 mRNA, WNT target genes, squamous differentiation markers (KRT10, IVL), cilia markers
- **Expected result if GLI bypass model correct**: Resistant tumors maintain elevated GLI target gene expression with identifiable upstream alterations (SMO mutations, SUFU loss, GLI2 amplification)
- **Expected result if alternative models correct**: Resistant tumors show reduced GLI activity with activated WNT, RAS/MAPK, or squamous differentiation programs

### Test 2: SUFU-Mutant Basket Trial of GLI-Directed Agents
- **Objective**: Test the strongest prediction of the hypothesis — that SUFU-driven tumors respond to GLI agents
- **Patient stratification**: Germline SUFU mutation carriers (MHIBCC, BCNS2, SHH-MB)
- **Perturbation**: BET inhibitor (e.g., birabresib) or HDAC inhibitor (domatinostat) ± standard therapy
- **Model system**: Phase I/II basket trial
- **Expected result if GLI bypass model correct**: GLI1 biomarker suppression and tumor regression
- **Expected result if hypothesis fails**: Tumors are resistant despite GLI suppression (indicating GLI-independent survival)

### Test 3: Longitudinal Biopsy Study During HHI Treatment
- **Objective**: Map temporal dynamics of tolerance → resistance transition and identify therapeutic windows
- **Patient stratification**: Newly diagnosed advanced BCC patients starting HHI therapy
- **Sample type**: Serial biopsies at baseline, partial response, best response, and progression
- **Assays**: Single-cell RNA-seq, WNT/HH/GLI pathway activity scoring, cilia immunofluorescence
- **Expected result**: WNT-dependent persister state detectable at early timepoints, followed by emergence of either GLI-convergent or GLI-independent genetic resistance at progression

### Test 4: Head-to-Head GLI vs. MEK Inhibitor in Resistant BCC PDX Models
- **Objective**: Determine whether GLI-directed or RAS/MAPK-directed therapy is more broadly effective across resistance subtypes
- **Model system**: Patient-derived xenograft panel from resistant BCCs (≥20 models)
- **Perturbation**: GLI inhibitor (GANT61 or ATO) vs. MEK inhibitor (trametinib) vs. combination
- **Biomarkers**: Cilia status, GLI target gene expression, MAPK pathway activity
- **Expected result**: Response stratified by cilia status — cilia-intact tumors respond to GLI inhibitors, cilia-loss tumors respond to MEK inhibitors

### Test 5: GLI Activity Biomarker Panel Validation
- **Objective**: Develop and validate a diagnostic tool for identifying GLI-convergent resistance
- **Sample type**: FFPE tissue from resistant BCC tumors (retrospective cohort, n≥50)
- **Assays**: NanoString or targeted RNA panel for GLI1, GLI2, PTCH1 (GLI targets), plus cilia markers, WNT targets, and SCC markers
- **Expected result**: Tumors cluster into ≥3 resistance subtypes (GLI-high/convergent, GLI-low/pathway-switch, GLI-low/lineage-switch) with distinct biomarker profiles

---

## Curation Leads

*The following are candidate updates for the Knowledge Base, flagged as leads requiring curator verification.*

### Candidate Evidence References

1. **PMID: 25759020** — Upgrade to STRONG SUPPORT. Verified abstract snippet: "Here we identify SMO mutations in 50% (22 of 44) of resistant BCCs and show that these mutations maintain Hedgehog signaling in the presence of SMO inhibitors." Directly quantifies the most common GLI-convergent resistance mechanism.

2. **PMID: 23446420** — Add as STRONG SUPPORT. Verified snippet: "aPKC-ι/λ functions downstream of SMO to phosphorylate and activate GLI1, resulting in maximal DNA binding and transcriptional activation." Establishes non-canonical GLI bypass route.

3. **PMID: 24651015** — Add as STRONG SUPPORT. Verified snippet: "SHH-MBs harboring a PTCH1 mutation were responsive to SMO inhibition, whereas tumors harboring an SUFU mutation or MYCN amplification were primarily resistant." Demonstrates genotype-dependent primary resistance.

4. **PMID: 24973920** — Add as STRONG SUPPORT for therapeutic arm. Verified snippet: "patient- and GEMM-derived Hedgehog-driven tumors respond to JQ1 even when harboring genetic lesions rendering them resistant to Smoothened antagonists." Best preclinical evidence for GLI-directed therapy.

5. **PMID: 38157930** — Add as QUALIFYING evidence. Verified snippet: "sporadic basal cell carcinomas display high resistance rates, whereas tumors arising in patients with Gorlin syndrome with germline Patched (PTCH1) alterations are uniformly suppressed by inhibitor therapy." Limits hypothesis scope in Gorlin-specific context.

6. **PMID: 30297801** — Add as COMPETING evidence. Establishes WNT-dependent persister mechanism as distinct from GLI-convergent resistance.

7. **PMID: 26765315** — Add as QUALIFYING evidence. Verified snippet: "Overall, arsenic trioxide and itraconazole reduced GLI1 messenger RNA levels by 75% from baseline (P < .0" — Shows pharmacodynamic proof-of-concept but clinical failure, qualifying the therapeutic arm.

8. **PMID: 26677003** — Add as STRONG SUPPORT for SUFU subtype. Verified snippet: "The downstream location of the SUFU gene within the sonic hedgehog pathway may explain why its loss is associated with relatively well-differentiated tumors and suggests that MHIBCC will not respond to therapeutic strategies, such as smoothened inhibitors, that target upstream components of this pathway."

9. **PMID: 30707899** — Add as COMPETING evidence. Title: "Loss of Primary Cilia Drives Switching from Hedgehog to Ras/MAPK Pathway in Resistant Basal Cell Carcinoma." GLI-independent resistance via pathway switch.

10. **PMID: 29055107** — Add as SUPPORTING evidence (preclinical therapeutic). Verified snippet: "4SC-202 treatment abrogates GLI activation and HH target gene expression in both SMOi-sensitive and -resistant cells."

### Candidate Pathophysiology Nodes/Edges

- **Add edge**: SUFU loss → constitutive GLI activation → SMO-inhibitor resistance (inherent/primary)
- **Add edge**: aPKC-ι/λ upregulation → non-canonical GLI1 phosphorylation → SMO-inhibitor resistance (acquired)
- **Add node**: BCC-to-SCC lineage transition (GLI-independent resistance mechanism)
- **Add node**: WNT-dependent persister state (early tolerance, pre-resistance)
- **Add edge**: Cilia loss → RAS/MAPK activation → GLI-independent resistance
- **Add edge**: BRD4 → GLI1/GLI2 transcription (epigenetic regulation, druggable)

### Candidate Ontology Terms

- Cell types: `CL:0002559` hair follicle infundibulum basal cell → relevant to IBCC/MHIBCC
- Biological processes: `GO:0007224` smoothened signaling pathway; `GO:0060070` canonical Wnt signaling pathway; `GO:0043408` regulation of MAPK cascade; `GO:0060271` cilium assembly
- Disease: `MONDO:0007295` basal cell nevus syndrome; consider adding `SUFU-associated Gorlin syndrome` as distinct entity with therapy-relevant annotations

### Candidate Status Change

- **Current status**: EMERGING
- **Recommended status**: PARTIALLY SUPPORTED
- **Rationale**: GLI convergence is well-validated as one of multiple resistance mechanisms but is not universal. Its applicability is subtype-dependent and the therapeutic corollary lacks clinical proof.
- **Mandatory qualifier**: Add subtype stratification — the hypothesis applies differently to SUFU-driven (primary resistance, strongest), sporadic BCC (acquired resistance, ~50% of cases), and PTCH1-Gorlin (rare, possibly non-GLI mechanisms).

### Candidate Knowledge Gaps for KB Discussion

1. **Gorlin-specific resistance characterization** — Only 1 patient studied molecularly (PMID: 38157930); mechanism may differ fundamentally from sporadic BCC resistance. Priority: HIGH.
2. **Clinical GLI-directed therapy** — No successful clinical trial; sole attempt (n=5) pharmacodynamically successful but clinically inadequate. Priority: CRITICAL.
3. **Temporal resistance model** — WNT-persister → genetic resistance transition undescribed longitudinally. Priority: MODERATE.
4. **SUFU-specific therapeutic prediction** — Strongest prediction of the model untested clinically. Priority: HIGH.
5. **Resistance subtype biomarkers** — No validated panel to distinguish GLI-convergent from GLI-independent resistance at the time of clinical decision-making. Priority: MODERATE.

---

*Report generated from systematic literature review of 68 papers across 5 investigative iterations. All citation snippets verified against stored abstracts unless otherwise noted.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist final summary](openscientist_artifacts/provenance_final_summary.json)
![OpenScientist final summary](openscientist_artifacts/provenance_final_summary.png)
- [OpenScientist knowledge gaps](openscientist_artifacts/provenance_knowledge_gaps.json)
![OpenScientist knowledge gaps](openscientist_artifacts/provenance_knowledge_gaps.png)
- [OpenScientist mechanistic diagram](openscientist_artifacts/provenance_mechanistic_diagram.json)
![OpenScientist mechanistic diagram](openscientist_artifacts/provenance_mechanistic_diagram.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)
- [OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.json)
![OpenScientist plot 5](openscientist_artifacts/provenance_plot_5.png)
- [OpenScientist plot 6](openscientist_artifacts/provenance_plot_6.json)
![OpenScientist plot 6](openscientist_artifacts/provenance_plot_6.png)
- [OpenScientist subtype applicability](openscientist_artifacts/provenance_subtype_applicability.json)
![OpenScientist subtype applicability](openscientist_artifacts/provenance_subtype_applicability.png)
- [OpenScientist therapeutic landscape](openscientist_artifacts/provenance_therapeutic_landscape.json)
![OpenScientist therapeutic landscape](openscientist_artifacts/provenance_therapeutic_landscape.png)