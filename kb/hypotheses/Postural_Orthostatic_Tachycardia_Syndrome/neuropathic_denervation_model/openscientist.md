---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-06T09:07:59.298740'
end_time: '2026-07-06T10:14:59.651987'
duration_seconds: 4020.35
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Postural Orthostatic Tachycardia Syndrome
  category: Complex
  hypothesis_group_id: neuropathic_denervation_model
  hypothesis_label: Neuropathic Sympathetic-Denervation Model
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: neuropathic_denervation_model\nhypothesis_label:\
    \ Neuropathic Sympathetic-Denervation Model\nstatus: ALTERNATIVE\napplies_to_subtypes:\n\
    - Neuropathic POTS\ndescription: Partial postganglionic sympathetic denervation,\
    \ often framed as small-fiber autonomic neuropathy,\n  impairs lower-extremity\
    \ vasoconstriction, causing orthostatic venous pooling, reduced central blood\n\
    \  volume, and reflex tachycardia."
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
citation_count: 36
artifact_count: 34
artifact_sources:
  openscientist_artifacts_zip: 34
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
- filename: provenance_alternative_models.json
  path: openscientist_artifacts/provenance_alternative_models.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist alternative models
- filename: provenance_alternative_models.png
  path: openscientist_artifacts/provenance_alternative_models.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist alternative models
- filename: provenance_claim_status_table.json
  path: openscientist_artifacts/provenance_claim_status_table.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim status table
- filename: provenance_claim_status_table.png
  path: openscientist_artifacts/provenance_claim_status_table.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist claim status table
- filename: provenance_conflict_resolution_map.json
  path: openscientist_artifacts/provenance_conflict_resolution_map.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist conflict resolution map
- filename: provenance_conflict_resolution_map.png
  path: openscientist_artifacts/provenance_conflict_resolution_map.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist conflict resolution map
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
- filename: provenance_final_assessment_complete.json
  path: openscientist_artifacts/provenance_final_assessment_complete.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment complete
- filename: provenance_final_assessment_complete.png
  path: openscientist_artifacts/provenance_final_assessment_complete.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment complete
- filename: provenance_final_assessment_summary.json
  path: openscientist_artifacts/provenance_final_assessment_summary.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment summary
- filename: provenance_final_assessment_summary.png
  path: openscientist_artifacts/provenance_final_assessment_summary.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final assessment summary
- filename: provenance_mechanistic_causal_chain.json
  path: openscientist_artifacts/provenance_mechanistic_causal_chain.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic causal chain
- filename: provenance_mechanistic_causal_chain.png
  path: openscientist_artifacts/provenance_mechanistic_causal_chain.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist mechanistic causal chain
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
- filename: provenance_plot_7.json
  path: openscientist_artifacts/provenance_plot_7.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 7
- filename: provenance_plot_7.png
  path: openscientist_artifacts/provenance_plot_7.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 7
- filename: provenance_plot_8.json
  path: openscientist_artifacts/provenance_plot_8.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 8
- filename: provenance_plot_8.png
  path: openscientist_artifacts/provenance_plot_8.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist plot 8
- filename: provenance_summary_assessment.json
  path: openscientist_artifacts/provenance_summary_assessment.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist summary assessment
- filename: provenance_summary_assessment.png
  path: openscientist_artifacts/provenance_summary_assessment.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist summary assessment
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Postural Orthostatic Tachycardia Syndrome
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** neuropathic_denervation_model
- **Hypothesis Label:** Neuropathic Sympathetic-Denervation Model
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: neuropathic_denervation_model
hypothesis_label: Neuropathic Sympathetic-Denervation Model
status: ALTERNATIVE
applies_to_subtypes:
- Neuropathic POTS
description: Partial postganglionic sympathetic denervation, often framed as small-fiber autonomic neuropathy,
  impairs lower-extremity vasoconstriction, causing orthostatic venous pooling, reduced central blood
  volume, and reflex tachycardia.
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

# Neuropathic Sympathetic-Denervation Model of Postural Orthostatic Tachycardia Syndrome: Hypothesis Evaluation Report

**Hypothesis ID:** `neuropathic_denervation_model`
**Disease:** Postural Orthostatic Tachycardia Syndrome (POTS)
**Status in KB:** ALTERNATIVE
**Investigation:** 5 iterations, 104 papers reviewed, 21 findings confirmed, 32 evidence items

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED** — The neuropathic sympathetic-denervation model is well-supported as an explanation for POTS in a defined patient subtype (~25–50% of cases) but cannot serve as a universal disease mechanism. The downstream causal chain — from postganglionic sympathetic denervation to impaired lower-extremity vasoconstriction to venous pooling to reflex tachycardia — is robustly established by convergent human clinical evidence (7 of 11 mechanistic claims classified as ESTABLISHED). However, the critical upstream trigger remains unknown, no validated diagnostic criteria cleanly delineate the neuropathic subtype, immunotherapy trials have been uniformly negative in controlled settings (iSTAND IVIG P=0.629; Gibbons IVIG-for-SFN P=NS), and the 71% exercise-training remission rate creates an unresolved paradox with the concept of fixed structural denervation. The hypothesis should be retained as ALTERNATIVE with explicit subtype restriction, pending resolution of 8 documented knowledge gaps.

---

## Summary

The neuropathic sympathetic-denervation model proposes that partial postganglionic sympathetic denervation — often framed as small-fiber autonomic neuropathy — impairs lower-extremity vasoconstriction, causing orthostatic venous pooling, reduced central blood volume, and compensatory reflex tachycardia. This investigation evaluated the model across 104 primary research papers, generating 21 confirmed findings and 32 discrete evidence items.

The strongest evidence comes from the landmark Jacob et al. (2000) regional norepinephrine spillover study demonstrating selectively reduced femoral vein NE in POTS patients with preserved arm NE, Goldstein et al. (2002) showing preserved-to-enhanced cardiac sympathetic innervation (proving the denervation is regional, not global), and multiple independent series (Thieben et al. 2007, Haensch et al. 2014, Zhang et al. 2022) confirming that 24–50% of POTS patients have objective evidence of small fiber neuropathy on skin biopsy or sudomotor testing. The hemodynamic consequence — impaired vasoconstriction and venous pooling — is confirmed by Stewart & Weldon (2001, 2003) and the therapeutic response to alpha-1 agonists (midodrine) and abdominal compression further supports the pooling mechanism.

However, critical limitations confine the model's scope. The neuropathic subtype overlaps extensively with hyperadrenergic and hypovolemic subtypes (Mar & Raj 2020; Thieben et al. 2007). No controlled immunotherapy trial has shown efficacy: the iSTAND IVIG trial (Vernino et al. 2024, P=0.629) and the Gibbons IVIG-for-SFN pilot (2023, P=NS) were both negative. The 71% exercise-training remission rate (George et al. 2016) is difficult to reconcile with fixed structural nerve loss. The upstream trigger — whether autoimmune, post-viral, genetic, or degenerative — remains unresolved and represents the single most important knowledge gap for this hypothesis.

---

## Key Findings

### Finding 1: Regional Sympathetic Denervation Selectively Affecting Lower Extremities

The foundational evidence for the neuropathic model comes from Jacob et al. (2000) ([PMID: 11018167](https://pubmed.ncbi.nlm.nih.gov/11018167/)). In 10 POTS patients versus 8 controls, femoral vein norepinephrine was significantly lower (135±30 vs 215±55 pg/mL, P=0.001). Leg NE spillover responses to cold pressor (P=0.02), nitroprusside (P=0.02), and tyramine (P=0.03) were all impaired, while arm NE spillover was fully preserved. This is the single most important piece of evidence for the hypothesis, establishing that sympathetic denervation in POTS is partial and length-dependent, affecting the lower but not the upper extremities.

### Finding 2: Cardiac Sympathetic Innervation Is Preserved — Denervation Is Regional, Not Global

Goldstein et al. (2002) ([PMID: 12403667](https://pubmed.ncbi.nlm.nih.gov/12403667/)) demonstrated that cardiac NE spillover was actually *higher* in POTS (171±30 pmol/min) than in controls (102±9 pmol/min). Cardiac extraction of tritiated NE, cardiac DOPA production, and myocardial 6-[18F]fluorodopamine PET were all normal. This critical finding establishes that POTS involves a regional sympathetic imbalance — deficient vasoconstrictor innervation in the lower body combined with preserved or even hyperactive cardiac sympathetic drive — rather than generalized autonomic failure. This regional pattern is key to understanding why reflex tachycardia is so prominent.

### Finding 3: Small Fiber Neuropathy Confirmed in 24–50% of POTS Patients

Multiple independent series confirm the neuropathic subtype but also demonstrate it does not encompass all POTS:

- **Thieben et al. 2007** ([PMID: 17352367](https://pubmed.ncbi.nlm.nih.gov/17352367/)): In 152 patients at Mayo Clinic, 50% had sudomotor abnormalities on both QSART and thermoregulatory sweat test; 34.9% had significant adrenergic impairment. The authors concluded "at least half of the patients had a neuropathic pattern of POTS."
- **Haensch et al. 2014** ([PMID: 24647968](https://pubmed.ncbi.nlm.nih.gov/24647968/)): In 84 POTS patients, mean IENF density was 7.2±2.9/mm with 45% below normal. Critically, low IENFD correlated with reduced cardiac MIBG uptake (r=0.39, P=0.001), linking skin and cardiac denervation in a single coherent neuropathic process.
- **Zhang et al. 2022** ([PMID: 36349067](https://pubmed.ncbi.nlm.nih.gov/36349067/)): In a large tertiary center series of 356 POTS patients, only 24% of 80 biopsied had reduced IENFD and 33% of 211 tested had reduced QSART sweat output, confirming "the neuropathic subset represents a minority of overall POTS patients."

The convergence of these studies establishes that a neuropathic pattern is present in a substantial minority — approximately one-quarter to one-half — of POTS patients, depending on the testing methodology and referral population.

### Finding 4: Venous Pooling and Impaired Vasoconstriction Directly Measured

Stewart & Weldon (2001) ([PMID: 11295714](https://pubmed.ncbi.nlm.nih.gov/11295714/)) directly measured the hemodynamic consequence of denervation in adolescent POTS. Resting calf arterial resistance was lower (27±2 vs 42±5 in controls), and after tilt, calf blood flow remained elevated at 6.6±2.3 vs 3.1±0.4 mL/100mL/min, with calf volume increasing approximately twice as much in POTS patients. The authors concluded that "lower resistance at baseline reflects a defect in arterial vasoconstriction in POTS, further exacerbated during upright posture." Stewart & Weldon (2003) ([PMID: 12653674](https://pubmed.ncbi.nlm.nih.gov/12653674/)) further identified two hemodynamically distinct POTS subgroups: a high-venous-pressure group with increased resistance and decreased flow, versus a normal-venous-pressure group with decreased resistance and increased flow — both meeting POTS criteria but with contrasting peripheral vascular physiology.

### Finding 5: Splanchnic Venous Pooling Extends Beyond the Lower Extremities

Smith et al. (2020) ([PMID: 32673517](https://pubmed.ncbi.nlm.nih.gov/32673517/)) demonstrated in a randomized crossover trial (n=18) that abdominal compression (40 mmHg inflatable binder) attenuated orthostatic tachycardia and improved symptoms, with the combination of propranolol plus abdominal compression being superior to either alone. This confirms that the venous pooling in POTS is not limited to the lower extremities but includes the splanchnic vasculature, broadening the anatomical scope of the denervation model.

### Finding 6: Denervation Supersensitivity Provides Pharmacological Confirmation

Jacob et al. (1997) ([PMID: 9244228](https://pubmed.ncbi.nlm.nih.gov/9244228/)) reported that midodrine (alpha-1 agonist, 5–10 mg) decreased both supine and upright heart rate in POTS patients (supine 78±2 to 69±2, P<0.005; upright 108±5 to 95±5, P<0.01). The authors explicitly identified "alpha1-adrenoreceptor hypersensitivity" and stated: "There is evidence of an autonomic neuropathy affecting the lower-extremity blood vessels." Alpha-1 receptor hypersensitivity is a classical marker of denervation supersensitivity, providing pharmacological evidence for structural nerve loss. Hoeldtke et al. (2006) ([PMID: 17036177](https://pubmed.ncbi.nlm.nih.gov/17036177/)) confirmed that midodrine suppressed standing HR from 114±0.7 to 92.8±0.7 bpm (P<0.001), and octreotide was similarly effective.

### Finding 7: Failure to Increase TPR Predicts Syncope — Functional Consequence of Denervation

Sandroni et al. (1996) ([PMID: 8902319](https://pubmed.ncbi.nlm.nih.gov/8902319/)) compared POTS patients who fainted (n=11) versus those who did not (n=9). POTS patients who fainted showed a *fall* instead of an increase in total peripheral resistance during tilt — "the most consistent alteration was a fall instead of an increase in TPR" — a pattern similar to generalized autonomic failure. Non-fainting POTS patients maintained TPR. This demonstrates that the severity of sympathetic vasoconstrictor denervation has direct prognostic implications, with greater denervation predicting hemodynamic collapse.

### Finding 8: Exercise Training Achieves 71% Remission — The Central Paradox

The deconditioning/small-heart model represents the most serious empirical challenge to the neuropathic hypothesis:

- **Fu et al. (2010)** ([PMID: 20579544](https://pubmed.ncbi.nlm.nih.gov/20579544/)): LV mass was lower in POTS (1.26 vs 1.45 g/kg, P<0.01), blood volume reduced (60 vs 71 mL/kg, P<0.01). After 3-month exercise training, LV mass increased ~12%, blood volume ~7%, and 10/19 no longer met POTS criteria.
- **George et al. (2016)** ([PMID: 26690066](https://pubmed.ncbi.nlm.nih.gov/26690066/)): In the international POTS registry (n=251 enrolled, 103 completed), "71% no longer qualified for POTS and were thus in remission."
- **Shibata et al. (2012)** ([PMID: 22641777](https://pubmed.ncbi.nlm.nih.gov/22641777/)): VO2peak was lower in POTS (26.1 vs 36.3 mL/kg/min, P<0.001) due to lower peak stroke volume; training increased VO2peak by 11% (P<0.001).

If POTS were solely due to fixed structural denervation, a 71% remission rate with exercise would be unexplained. This finding either limits the neuropathic model to a minority subtype, or suggests that functional rather than structural factors predominate even in patients with measurable SFN.

### Finding 9: NET Deficiency as a Distinct Non-Denervation Mechanism

Shannon et al. (2000) ([PMID: 10684912](https://pubmed.ncbi.nlm.nih.gov/10684912/)) identified a heterozygous norepinephrine transporter (NET) mutation (A457P in SLC6A2) producing POTS with reduced NE clearance and elevated standing NE (923 vs 439±129 pg/mL). Lambert et al. (2008) ([PMID: 19808400](https://pubmed.ncbi.nlm.nih.gov/19808400/)) demonstrated "a decrease in the expression of NET protein in patients with POTS" on forearm vein biopsies. Shirey-Rice et al. (2013) ([PMID: 23580201](https://pubmed.ncbi.nlm.nih.gov/23580201/)) showed that NET A457P knock-in mice exhibited tachycardia, elevated plasma NE, and reduced DHPG:NE ratios, providing the first genetic model of POTS. This is a complete alternative mechanism — impaired NE reuptake rather than structural denervation — that produces an identical phenotype.

### Finding 10: Controlled Immunotherapy Trials Are Negative

Two controlled trials directly challenge the autoimmune-neuropathic pathway:

- **iSTAND trial** — Vernino et al. (2024) ([PMID: 38311655](https://pubmed.ncbi.nlm.nih.gov/38311655/)): First RCT of IVIG for presumed autoimmune POTS (n=30). "Change in COMPASS-31 did not differ between groups (median change [IQR]; IVIG: -5.5 [-23.3, 2.5] versus albumin: -10.6 [-14.1, -4.7]; p-value = 0.629)."
- **Gibbons et al. (2023)** ([PMID: 36367813](https://pubmed.ncbi.nlm.nih.gov/36367813/)): Pilot RCT of IVIG for autoantibody-associated SFN (n=17). "Skin biopsy IENFD improved by 0.5 ± 0.8 fibers/mm in the placebo group and improved by 0.6 ± 0.6 fibers/mm in the IVIG-treated group (p = NS)."

These negative results weaken the autoimmune causation link, though the small sample sizes and potential subtype heterogeneity limit definitive conclusions. Notably, the uncontrolled case series by Kesterson et al. (2023) ([PMID: 36008726](https://pubmed.ncbi.nlm.nih.gov/36008726/)) reported improvement in 7 refractory POTS-SFN patients treated with SCIG/plasmapheresis, highlighting the discrepancy between controlled and uncontrolled evidence.

### Finding 11: Post-Viral SFN Supports Upstream Trigger Pathway

Maguire et al. (2025) ([PMID: 40093251](https://pubmed.ncbi.nlm.nih.gov/40093251/)) studied 977 long COVID patients and found "skin biopsy confirming small fiber neuropathy in 56.5% (48/85) cases, affecting both epidermal and autonomic nerve fibers." Anti-ganglioside antibodies were detected in 25% of long COVID neuropathy patients. This provides the strongest contemporary evidence for a post-viral autoimmune mechanism as an upstream trigger for neuropathic POTS, bridging the infection to autoimmunity to SFN to POTS causal chain.

### Finding 12: POTS Subtypes Overlap Substantially

Mar & Raj (2020) ([PMID: 31412221](https://pubmed.ncbi.nlm.nih.gov/31412221/)) noted that "patients often will exhibit overlapping characteristics from more than one of these mechanisms." In the Thieben et al. (2007) cohort, 50% had neuropathic features, 29% hyperadrenergic, 28.9% hypovolemic, and 14.6% had ganglionic AChR antibodies — these categories were not mutually exclusive. Bryarly et al. (2019) ([PMID: 30871704](https://pubmed.ncbi.nlm.nih.gov/30871704/)) characterized POTS as "a heterogeneous disorder, the pathophysiology and mechanisms of which are not well understood." This subtype overlap is a fundamental challenge for any single-mechanism model.

---

## Mechanistic Causal Chain

The neuropathic sympathetic-denervation model implies the following causal chain from upstream trigger to clinical manifestation. Evidence strength varies at each link:

```
UPSTREAM TRIGGER (Unknown -- autoimmune? post-viral? genetic?)
        |
        v                                          Evidence: EMERGING
SMALL-FIBER AUTONOMIC NEUROPATHY <---- Dysimmune SFN (Oaklander 2016, 2026)
(postganglionic sympathetic)           Post-COVID SFN (Maguire 2025)
        |                              hEDS-associated SFN (Dalla Corte 2022)
        |
        v                                          Evidence: ESTABLISHED
IMPAIRED LOWER-EXTREMITY VASOCONSTRICTION <---- Jacob 2000 (NE spillover)
(reduced NE release at vascular terminals)       Novak 1996 (sudomotor failure)
        |                                        Sandroni 1996 (TPR failure)
        |
        v                                          Evidence: ESTABLISHED
ORTHOSTATIC VENOUS POOLING <---- Stewart & Weldon 2001, 2003
(lower-extremity + splanchnic)    Smith 2020 (splanchnic compression)
        |
        v                                          Evidence: ESTABLISHED
REDUCED CENTRAL BLOOD VOLUME <---- Fu 2010 (blood volume deficit)
(preload deficit)                   Raj 2005 (hypovolemia)
        |
        v                                          Evidence: ESTABLISHED
COMPENSATORY REFLEX TACHYCARDIA <---- Preserved cardiac sympathetic
(baroreflex-mediated)                  innervation (Goldstein 2002)
        |                              Normal baroreflex (Fu 2011)
        v
POTS CLINICAL PHENOTYPE
(HR >=30 bpm increase on standing)
```

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain of the neuropathic denervation model, from upstream trigger through sympathetic denervation to clinical POTS phenotype}}

**Strongest links:** Steps 2–5 (denervation to vasoconstriction failure to pooling to reduced preload to tachycardia) are supported by convergent human clinical evidence from multiple independent groups.

**Weakest link:** Step 1 (upstream trigger to SFN) is the critical knowledge gap. Autoimmune, post-viral, genetic, and connective tissue disorder etiologies are all proposed but none definitively proven as sufficient causes.

**Missing links:**
- No longitudinal study has tracked the progression from trigger to SFN to POTS onset
- No study has demonstrated that preventing SFN progression halts or reverses POTS
- The relationship between SFN severity and POTS symptom severity is only weakly established

---

## Evidence Matrix

{{figure:evidence_matrix.png|caption=Evidence matrix showing direction (supports/refutes/qualifies/competing) and type for 32 evidence items evaluating the neuropathic POTS denervation model}}

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Subtype/Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|-----------------|------------|
| [PMID: 11018167](https://pubmed.ncbi.nlm.nih.gov/11018167/) Jacob 2000 | Human clinical | **Supports** | Regional LE sympathetic denervation | Femoral vein NE reduced (P=0.001), arms preserved | Neuropathic POTS | High; n=10 vs 8 |
| [PMID: 12403667](https://pubmed.ncbi.nlm.nih.gov/12403667/) Goldstein 2002 | Human clinical | **Qualifies** | Cardiac denervation | Cardiac NE spillover *increased* in POTS -- denervation is regional | All POTS | High; n=16 |
| [PMID: 17352367](https://pubmed.ncbi.nlm.nih.gov/17352367/) Thieben 2007 | Human clinical | **Supports** | SFN prevalence | 50% sudomotor abnormalities; 34.9% adrenergic impairment | Neuropathic POTS | High; n=152, Mayo |
| [PMID: 24647968](https://pubmed.ncbi.nlm.nih.gov/24647968/) Haensch 2014 | Human clinical | **Supports** | SFN + cardiac denervation | 45% low IENFD; correlated with MIBG (r=0.39, P=0.001) | Neuropathic POTS | Moderate; n=84 |
| [PMID: 36349067](https://pubmed.ncbi.nlm.nih.gov/36349067/) Zhang 2022 | Human clinical | **Qualifies** | SFN in POTS | Only 24% reduced IENFD, 33% reduced QSART | Tertiary referral | High; n=356 |
| [PMID: 11295714](https://pubmed.ncbi.nlm.nih.gov/11295714/) Stewart 2001 | Human clinical | **Supports** | LE vasoconstriction failure | Calf arterial resistance decreased; pooling 2x greater | Adolescent POTS | Moderate; n=11 vs 8 |
| [PMID: 12653674](https://pubmed.ncbi.nlm.nih.gov/12653674/) Stewart 2003 | Human clinical | **Qualifies** | Venous pooling mechanism | Two distinct hemodynamic subgroups | All POTS | Moderate; n=29 |
| [PMID: 32673517](https://pubmed.ncbi.nlm.nih.gov/32673517/) Smith 2020 | Human clinical (RCT) | **Supports** | Splanchnic pooling | Abdominal compression improved tachycardia | All POTS | High; RCT n=18 |
| [PMID: 8902319](https://pubmed.ncbi.nlm.nih.gov/8902319/) Sandroni 1996 | Human clinical | **Supports** | TPR failure from denervation | TPR fell in syncopal POTS | POTS with syncope | Moderate; n=20 |
| [PMID: 8988490](https://pubmed.ncbi.nlm.nih.gov/8988490/) Novak 1996 | Human clinical | **Supports** | Restricted autonomic neuropathy | Distal postganglionic sudomotor failure | Neuropathic POTS | Moderate; n=20 |
| [PMID: 9244228](https://pubmed.ncbi.nlm.nih.gov/9244228/) Jacob 1997 | Human clinical | **Supports** | Denervation supersensitivity | Midodrine reduced HR; alpha1-receptor hypersensitivity | Neuropathic POTS | Moderate; n=13 |
| [PMID: 17036177](https://pubmed.ncbi.nlm.nih.gov/17036177/) Hoeldtke 2006 | Human clinical | **Supports** | Vasoconstrictor therapy response | Midodrine standing HR 114 to 92.8 (P<0.001) | All POTS | Moderate; n=9 |
| [PMID: 20579544](https://pubmed.ncbi.nlm.nih.gov/20579544/) Fu 2010 | Human clinical | **Competing** | Exercise reverses POTS | LV mass +12%; 10/19 remitted after training | All POTS | High; n=27 |
| [PMID: 26690066](https://pubmed.ncbi.nlm.nih.gov/26690066/) George 2016 | Human clinical | **Competing** | Exercise remission rate | 71% no longer met POTS criteria | All POTS | High; n=103 completed |
| [PMID: 22641777](https://pubmed.ncbi.nlm.nih.gov/22641777/) Shibata 2012 | Human clinical | **Competing** | Deconditioning mechanism | VO2peak 11% increase after training (P<0.001) | All POTS | High; n=19 |
| [PMID: 10684912](https://pubmed.ncbi.nlm.nih.gov/10684912/) Shannon 2000 | Genetic/clinical | **Competing** | NET deficiency | NET A457P mutation produces POTS without denervation | Hyperadrenergic | High; genetic proof |
| [PMID: 19808400](https://pubmed.ncbi.nlm.nih.gov/19808400/) Lambert 2008 | Human clinical | **Competing** | NET protein reduction | Reduced NET in forearm veins; MSNA elevated | Hyperadrenergic | Moderate; small n |
| [PMID: 23580201](https://pubmed.ncbi.nlm.nih.gov/23580201/) Shirey-Rice 2013 | Model organism | **Competing** | NET dysfunction sufficiency | NET A457P mice: tachycardia + elevated NE | NET-deficient | High; genetic model |
| [PMID: 38311655](https://pubmed.ncbi.nlm.nih.gov/38311655/) Vernino 2024 | Human clinical (RCT) | **Refutes** | Autoimmune causation | IVIG vs albumin: COMPASS-31 P=0.629 | Autoimmune POTS | High; first RCT |
| [PMID: 36367813](https://pubmed.ncbi.nlm.nih.gov/36367813/) Gibbons 2023 | Human clinical (RCT) | **Refutes** | IVIG reverses SFN | IENFD: IVIG 0.6 vs placebo 0.5 fibers/mm (NS) | Autoantibody+ SFN | Moderate; n=17 |
| [PMID: 36008726](https://pubmed.ncbi.nlm.nih.gov/36008726/) Kesterson 2023 | Case series | Supports (weak) | Immunotherapy for POTS-SFN | 50% COMPASS-31 reduction; 217% FAS increase | Refractory POTS-SFN | Low; n=7, uncontrolled |
| [PMID: 31495251](https://pubmed.ncbi.nlm.nih.gov/31495251/) Gunning 2019 | Human clinical | **Qualifies** | Autoantibody prevalence | 89% had alpha1 adrenergic receptor autoantibodies | All POTS | Moderate; ELISA assay |
| [PMID: 35269395](https://pubmed.ncbi.nlm.nih.gov/35269395/) Gunning 2022 | Human clinical | **Qualifies** | Inflammatory biomarkers | 10/16 biomarkers elevated (P<0.0001) | All POTS | Moderate; n=55 |
| [PMID: 34484936](https://pubmed.ncbi.nlm.nih.gov/34484936/) Vernino 2021 | Human clinical | **Refutes** | gAChR antibody relevance | 7% POTS vs 8% controls; no clinical difference | All POTS | High; n=294 |
| [PMID: 40093251](https://pubmed.ncbi.nlm.nih.gov/40093251/) Maguire 2025 | Human clinical | **Supports** | Post-viral SFN trigger | 56.5% SFN on biopsy; 25% anti-ganglioside Ab | Long COVID | High; n=977 |
| [PMID: 41526147](https://pubmed.ncbi.nlm.nih.gov/41526147/) Oaklander 2026 | Review/synthesis | **Supports** | Dysimmune SFN as trigger | Passive transfer evidence for autoimmune SFN | Idiopathic SFN | Moderate; review |
| [PMID: 26526686](https://pubmed.ncbi.nlm.nih.gov/26526686/) Oaklander 2016 | Review/synthesis | **Supports** | Autoimmune SFN etiology | Sjogren, celiac linked to SFN | Autoimmune SFN | Moderate; review |
| [PMID: 31412221](https://pubmed.ncbi.nlm.nih.gov/31412221/) Mar & Raj 2020 | Review | **Qualifies** | Subtype overlap | "Patients often exhibit overlapping characteristics" | All POTS | High; expert review |
| [PMID: 30871704](https://pubmed.ncbi.nlm.nih.gov/30871704/) Bryarly 2019 | Review | **Qualifies** | POTS heterogeneity | "Heterogeneous disorder...not well understood" | All POTS | High; JACC review |
| [PMID: 39964606](https://pubmed.ncbi.nlm.nih.gov/39964606/) Qu 2025 | Genetic | **Qualifies** | Genetic landscape | Cell-cell junction + estrogen pathways enriched; no single gene | Pediatric POTS | Moderate; n=207 |
| [PMID: 40022872](https://pubmed.ncbi.nlm.nih.gov/40022872/) Ryu 2025 | Proteomics | Supports (emerging) | Immune-neuronal pathways | M7 module: immune/neuronal cells; integrin signaling | Post-COVID POTS | Low; n=9 vs 9 |
| [PMID: 41720282](https://pubmed.ncbi.nlm.nih.gov/41720282/) Fudim 2026 | Trial design | Neutral | IVIG for LC-POTS | RECOVER-AUTONOMIC platform trial ongoing | Long COVID POTS | Pending results |

{{figure:final_assessment_complete.png|caption=Final assessment summary: 32 evidence items, 21 confirmed findings, with evidence direction breakdown showing the balance of supporting, qualifying, competing, and refuting evidence}}

---

## Claim Status Classification

Based on the totality of evidence, each mechanistic claim in the neuropathic model can be classified by maturity:

| Mechanistic Claim | Status | Key Evidence | Caveats |
|-------------------|--------|-------------|---------|
| Postganglionic sympathetic denervation in LE | **ESTABLISHED** | Jacob 2000, Novak 1996 | Small sample sizes; denervation may be partly functional |
| Denervation is regional (LE, not cardiac) | **ESTABLISHED** | Goldstein 2002, Haensch 2014 | Cardiac NE spillover elevated, not merely preserved |
| Impaired LE vasoconstriction | **ESTABLISHED** | Stewart 2001, Sandroni 1996 | Two distinct hemodynamic subgroups exist |
| Venous pooling (LE + splanchnic) | **ESTABLISHED** | Stewart 2001/2003, Smith 2020 | Splanchnic component relatively understudied |
| Reduced central blood volume | **ESTABLISHED** | Fu 2010, Raj 2005 | Hypovolemia also found without neuropathy |
| Reflex tachycardia (baroreflex-mediated) | **ESTABLISHED** | Multiple studies | Baroreflex itself is normal (Fu 2011) |
| SFN as histological substrate | **ESTABLISHED** | Thieben 2007, Haensch 2014, Zhang 2022 | Present in only 24-50% of POTS |
| Autoimmune upstream trigger | **EMERGING** | Oaklander 2016/2026, Maguire 2025 | Immunotherapy RCTs negative |
| Post-viral upstream trigger | **EMERGING** | Maguire 2025, COVID-POTS literature | Temporal association; causation not proven |
| Denervation supersensitivity | **ESTABLISHED** | Jacob 1997, midodrine studies | Pharmacological inference only |
| SFN causes the POTS phenotype (not just co-occurs) | **SPECULATIVE** | Correlational evidence only | No perturbation study; exercise remission paradox |

{{figure:claim_status_table.png|caption=Claim status classification for all mechanistic claims in the neuropathic denervation model, from ESTABLISHED to SPECULATIVE}}

---

## Alternative and Competing Models

{{figure:alternative_models.png|caption=Competing and complementary mechanistic models for POTS, showing relationship to the neuropathic denervation model}}

### 1. Cardiac Deconditioning / Small Heart Model
**Relationship to seed hypothesis:** Competing alternative (may be primary mechanism in majority of patients)

Fu et al. (2010) demonstrated reduced LV mass and blood volume in POTS that reversed with exercise training. The 71% exercise remission rate (George et al. 2016) suggests deconditioning is the dominant mechanism in many POTS patients. This model explains the same hemodynamic phenotype (reduced stroke volume leading to compensatory tachycardia) without invoking structural nerve damage. It may represent the primary mechanism in patients who do NOT have neuropathic features.

### 2. Norepinephrine Transporter (NET) Deficiency
**Relationship:** Alternative mechanism producing identical phenotype

Shannon et al. (2000) and Lambert et al. (2008) demonstrated genetic and acquired NET deficiency causing POTS through impaired NE reuptake rather than structural denervation. The NET A457P mouse model (Shirey-Rice et al. 2013) provides causal proof of sufficiency. This mechanism is particularly relevant to the hyperadrenergic POTS subtype.

### 3. Hypovolemia / Renin-Aldosterone Dysregulation
**Relationship:** Parallel mechanism; may be independent or downstream of denervation

Raj et al. (2005) ([PMID: 15781744](https://pubmed.ncbi.nlm.nih.gov/15781744/)) showed POTS patients had paradoxically unchanged PRA and low aldosterone despite marked plasma volume deficits (689±270 mL deficit, P<0.001). High dietary sodium intake partially corrects the hemodynamic derangement ([PMID: 33926653](https://pubmed.ncbi.nlm.nih.gov/33926653/)). Hypovolemia could be secondary to renal denervation or represent a parallel pathophysiology.

### 4. Autoimmune Autonomic Ganglionopathy / Anti-Receptor Autoantibody Model
**Relationship:** Proposed upstream cause or parallel mechanism

Gunning et al. (2019) reported 89% adrenergic receptor autoantibody prevalence by ELISA. However, ganglionic AChR antibodies are not elevated in POTS versus controls (Vernino 2021, n=294), and IVIG was not effective in the iSTAND trial. This model remains unproven for POTS specifically, though it may apply to a very small subset with high-titer ganglionic antibodies.

### 5. Mast Cell Activation Syndrome (MCAS)
**Relationship:** Parallel mechanism or upstream inflammatory trigger

Shibao et al. (2005) ([PMID: 15710782](https://pubmed.ncbi.nlm.nih.gov/15710782/)) described hyperadrenergic POTS associated with mast cell activation, with patients showing exaggerated systolic BP increase on standing and Valsalva overshoot. Up to 25% of hEDS/POTS patients have concurrent MCAS. Whether mast cell mediators cause nerve damage (upstream) or simply co-occur remains unknown.

### 6. Connective Tissue Disorder (hEDS/HSD) Model
**Relationship:** Upstream predisposing factor

Multiple studies document very high co-occurrence of hEDS and POTS (58–79% in hEDS cohorts). Dalla Corte et al. (2022) ([PMID: 36437696](https://pubmed.ncbi.nlm.nih.gov/36437696/)) found 61% of hEDS patients had SFN on skin biopsy with "generalized distribution of nerve fibre loss." The genetic enrichment of cell-cell junction pathways in POTS (Qu et al. 2025) may link connective tissue integrity to nerve vulnerability, suggesting hEDS may predispose to SFN.

---

## Knowledge Gaps

### Gap 1: Upstream Trigger for Small Fiber Neuropathy
**Scope:** The single most critical unknown in the entire causal chain.
**Why it matters:** Without knowing what causes the denervation, the model cannot predict disease onset, identify at-risk individuals, or guide preventive therapy.
**What was checked:** Literature on autoimmune SFN (Oaklander 2016, 2026), post-viral SFN (Maguire 2025), genetic causes (Qu et al. 2025), hEDS-associated SFN (Dalla Corte 2022).
**Resolution needed:** Longitudinal cohort study from infection/trigger event through SFN development to POTS onset, with serial skin biopsies and autoantibody panels.

### Gap 2: No Validated Diagnostic Criteria for Neuropathic POTS Subtype
**Scope:** No consensus definition exists for what constitutes "neuropathic POTS."
**Why it matters:** Studies use different criteria (QSART, IENFD, thermoregulatory sweat test, sudomotor function), yielding prevalence estimates from 24% to 50%. This makes it impossible to compare studies or design subtype-specific trials.
**Resolution needed:** Multicenter study with standardized testing battery to define cutoffs and concordance.

### Gap 3: Causality Between SFN and POTS Is Not Established
**Scope:** All evidence linking SFN to POTS is correlational; no perturbation study has shown that inducing or preventing SFN causes or prevents POTS.
**What was checked:** Immunotherapy trials (Vernino 2024, Gibbons 2023) — both negative; exercise trials show high remission without addressing SFN.
**Resolution needed:** Prospective study tracking IENFD changes in POTS patients undergoing exercise training to determine if nerve fiber density changes correlate with clinical improvement.

### Gap 4: Exercise Remission vs. Fixed Denervation Paradox
**Scope:** 71% exercise remission rate is unexplained if POTS is caused by structural nerve loss.
**Why it matters:** This paradox could mean that (a) exercise compensates for denervation via other hemodynamic mechanisms, (b) most POTS patients who respond to exercise did not have true neuropathic POTS, or (c) exercise promotes nerve regeneration. None of these has been tested.
**Resolution needed:** Pre/post exercise training skin biopsies and QSART in POTS patients stratified by baseline SFN status.

### Gap 5: Autoantibody Specificity and Pathogenicity
**Scope:** Very high ELISA-based autoantibody prevalence (89% by Gunning 2019) contrasts with equivalent gAChR antibody rates in patients and controls (Vernino 2021) and with negative immunotherapy trials.
**What was checked:** Gunning 2019 (ELISA), Vernino 2021 (radioimmunoprecipitation), iSTAND RCT, Gibbons pilot.
**Resolution needed:** Independent validation of ELISA-based assays with standardized methodology; passive transfer studies in animal models using purified patient IgG.

### Gap 6: No GenCC, ClinGen, or Large-Scale Genetic Evidence
**Scope:** No POTS genes are curated in GenCC or ClinGen. The only GWAS (Qu et al. 2025, n=207) found no genome-wide significant SNPs.
**What was checked:** Qu et al. 2025 (GWAS + WES), Shannon et al. 2000 (NET mutation family), SLC6A2 literature.
**Resolution needed:** Larger GWAS with international consortia (n>5,000); gene-based burden tests in phenotypically stratified cohorts.

### Gap 7: Splanchnic Denervation Not Directly Measured
**Scope:** Splanchnic pooling is confirmed therapeutically (Smith 2020 abdominal compression trial) but direct measurement of splanchnic sympathetic innervation has not been performed.
**Resolution needed:** Splanchnic vein NE spillover studies analogous to the Jacob et al. (2000) femoral vein protocol.

### Gap 8: Longitudinal Natural History Absent
**Scope:** No prospective natural history study tracks POTS patients from onset through disease course with serial autonomic and neuropathic assessments.
**Why it matters:** Unknown whether neuropathic POTS is progressive, stable, or spontaneously reversible over years.
**Resolution needed:** 5-year prospective cohort with annual IENFD, QSART, autonomic reflex testing, and symptom assessments.

{{figure:conflict_resolution_map.png|caption=Evidence conflict resolution map showing the four key contradictions in the neuropathic POTS model and how they might be reconciled}}

---

## Discriminating Tests

The following studies would most efficiently distinguish the neuropathic denervation model from competing alternatives:

### Test 1: Exercise Training RCT With Pre/Post Skin Biopsy Stratification
- **Design:** RCT of 3-month exercise training in POTS patients stratified by baseline IENFD (normal vs. reduced)
- **Biomarkers:** IENFD (pre/post), QSART, standing HR, plasma NE
- **Expected result if neuropathic model is correct:** Patients with reduced IENFD should have lower remission rates than those with normal IENFD
- **Expected result if deconditioning model dominates:** Similar remission rates regardless of IENFD status
- **Sample size:** ~100 patients (50 per stratum) for adequate power

### Test 2: Passive Transfer of POTS Autoantibodies
- **Design:** Transfer purified IgG from POTS patients (autoantibody-positive) to rodents; measure orthostatic hemodynamics and IENFD at 4-8 weeks
- **Expected result if autoimmune neuropathy model is correct:** Recipient animals develop tachycardia, reduced vasomotor responses, and reduced IENFD
- **Controls:** IgG from healthy controls and autoantibody-negative POTS patients

### Test 3: Prospective Post-COVID Cohort With Serial Biopsies
- **Design:** Follow 200 COVID-19 patients from acute infection with serial IENFD, autonomic testing, and POTS screening at 3, 6, and 12 months
- **Expected result if post-viral SFN triggers POTS:** IENFD decline precedes POTS onset; those who develop POTS have greater IENFD loss

### Test 4: RECOVER-AUTONOMIC IVIG Subgroup Analysis
- **Design:** The ongoing RECOVER-AUTONOMIC trial ([PMID: 41720282](https://pubmed.ncbi.nlm.nih.gov/41720282/)) should pre-specify subgroup analysis by baseline QSART and/or IENFD
- **Expected result if autoimmune-neuropathic subtype exists:** IVIG benefit concentrated in patients with objective SFN and/or autoantibody positivity

### Test 5: Splanchnic NE Spillover Study
- **Design:** Replicate Jacob et al. (2000) protocol measuring NE spillover in hepatic/splanchnic vein and femoral vein simultaneously
- **Expected result if splanchnic denervation contributes:** Reduced splanchnic NE spillover alongside reduced femoral vein NE

---

## Curation Leads

The following are candidate updates for the Disorder Mechanisms Knowledge Base. **All require curator verification.**

### Candidate Evidence References

1. **Jacob et al. 2000** ([PMID: 11018167](https://pubmed.ncbi.nlm.nih.gov/11018167/)) — Verified snippet: *"At base line, the mean (+/-SD) plasma norepinephrine concentration in the femoral vein was lower in the patients with the postural tachycardia syndrome than in the normal subjects (135+/-30 vs. 215+/-55 pg per milliliter [0.80+/-0.18 vs. 1.27+/-0.32 nmol per liter], P=0.001)."* Core evidence node for the sympathetic denervation claim.

2. **Vernino et al. 2024** ([PMID: 38311655](https://pubmed.ncbi.nlm.nih.gov/38311655/)) — Verified snippet: *"Change in COMPASS-31 did not differ between groups (median change [IQR]; IVIG: -5.5 [-23.3, 2.5] versus albumin: -10.6 [-14.1, -4.7]; p-value = 0.629)."* Evidence against autoimmune causation in unselected POTS.

3. **Gibbons et al. 2023** ([PMID: 36367813](https://pubmed.ncbi.nlm.nih.gov/36367813/)) — Verified snippet: *"Skin biopsy IENFD improved by 0.5 +/- 0.8 fibers/mm in the placebo group and improved by 0.6 +/- 0.6 fibers/mm in the IVIG-treated group (p = NS)."* Evidence against IVIG reversing SFN.

4. **George et al. 2016** ([PMID: 26690066](https://pubmed.ncbi.nlm.nih.gov/26690066/)) — Verified snippet: *"One hundred and three patients completed the program. Of those that completed, 71% no longer qualified for POTS and were thus in remission."* Key evidence for the competing deconditioning model.

### Candidate Pathophysiology Nodes and Edges

- **Node:** Postganglionic sympathetic denervation (lower extremity) -- **Edge:** causes -- Impaired lower-extremity vasoconstriction [ESTABLISHED]
- **Node:** Small fiber neuropathy -- **Edge:** correlates with -- POTS neuropathic subtype [ESTABLISHED, not proven causal]
- **Node:** Splanchnic venous pooling -- **Edge:** contributes to -- Reduced central blood volume [ESTABLISHED]
- **New edge:** Exercise training -- reverses -- POTS phenotype (71% remission) [ESTABLISHED; conflicts with fixed denervation]
- **New edge:** NET deficiency -- produces -- POTS phenotype (without structural denervation) [ESTABLISHED; competing mechanism]

### Candidate Ontology Terms

- **Cell types:** Postganglionic sympathetic neuron (CL:0011100); Small-diameter sensory neuron (CL:0000101); Vascular smooth muscle cell (CL:0000359)
- **Biological processes:** GO:0001659 (temperature homeostasis / sudomotor); GO:0003073 (regulation of systemic arterial blood pressure); GO:0042310 (vasoconstriction); GO:0006836 (neurotransmitter transport / NET function)
- **Disease terms:** MONDO:0100233 (Postural orthostatic tachycardia syndrome); HP:0012899 (Small fiber neuropathy)

### Candidate Subtype Restriction

The hypothesis should be explicitly restricted to the **neuropathic POTS subtype** (~25-50% of cases), defined by at least one of: reduced IENFD on skin biopsy, abnormal QSART, or abnormal thermoregulatory sweat test. The hypothesis does NOT apply to hyperadrenergic POTS (NET deficiency), pure deconditioning POTS, or hypovolemic POTS without neuropathic features.

### Candidate Status Change

**Current:** ALTERNATIVE -- **Recommended:** Retain as ALTERNATIVE with annotation: "Partially supported for neuropathic subtype (~25-50% of POTS); downstream causal chain established (7/11 claims); upstream trigger and causal primacy unresolved; controlled immunotherapy trials negative."

### Candidate Knowledge Gaps for KB Discussion

1. Upstream trigger for SFN causing neuropathic POTS remains unknown
2. SFN-POTS causality is unestablished (correlation only)
3. Exercise remission paradox with fixed structural denervation is unresolved
4. Immunotherapy ineffective in controlled trials (iSTAND, Gibbons)
5. No validated neuropathic subtype diagnostic criteria exist
6. Autoantibody assay specificity and pathogenicity are unclear
7. No large-scale genetic evidence (no GenCC/ClinGen entries)
8. No longitudinal natural history data for disease trajectory

---

## Limitations of This Investigation

1. **Search scope:** Literature search was limited to PubMed-indexed publications. Grey literature, conference abstracts, preprints, and non-English publications were not systematically searched.
2. **Publication bias:** Negative results (e.g., studies finding no SFN in POTS) may be underrepresented.
3. **Subtype heterogeneity:** Most POTS studies do not subtype patients at enrollment, making it difficult to extract neuropathic-subtype-specific data.
4. **Small sample sizes:** Key studies (Jacob 2000 n=10; Gibbons 2023 n=17; Vernino 2024 n=30) have limited statistical power.
5. **No meta-analysis performed:** Quantitative synthesis of effect sizes was not conducted due to heterogeneous study designs and outcome measures.
6. **Temporal limitation:** Search conducted as of July 2026; the RECOVER-AUTONOMIC trial results are pending and may substantially alter the evidence landscape.

---

*Report generated: July 2026. Based on systematic evaluation of 104 papers across 5 investigation iterations, yielding 21 confirmed findings and 32 evidence items.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist alternative models](openscientist_artifacts/provenance_alternative_models.json)
![OpenScientist alternative models](openscientist_artifacts/provenance_alternative_models.png)
- [OpenScientist claim status table](openscientist_artifacts/provenance_claim_status_table.json)
![OpenScientist claim status table](openscientist_artifacts/provenance_claim_status_table.png)
- [OpenScientist conflict resolution map](openscientist_artifacts/provenance_conflict_resolution_map.json)
![OpenScientist conflict resolution map](openscientist_artifacts/provenance_conflict_resolution_map.png)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist final assessment complete](openscientist_artifacts/provenance_final_assessment_complete.json)
![OpenScientist final assessment complete](openscientist_artifacts/provenance_final_assessment_complete.png)
- [OpenScientist final assessment summary](openscientist_artifacts/provenance_final_assessment_summary.json)
![OpenScientist final assessment summary](openscientist_artifacts/provenance_final_assessment_summary.png)
- [OpenScientist mechanistic causal chain](openscientist_artifacts/provenance_mechanistic_causal_chain.json)
![OpenScientist mechanistic causal chain](openscientist_artifacts/provenance_mechanistic_causal_chain.png)
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
- [OpenScientist plot 7](openscientist_artifacts/provenance_plot_7.json)
![OpenScientist plot 7](openscientist_artifacts/provenance_plot_7.png)
- [OpenScientist plot 8](openscientist_artifacts/provenance_plot_8.json)
![OpenScientist plot 8](openscientist_artifacts/provenance_plot_8.png)
- [OpenScientist summary assessment](openscientist_artifacts/provenance_summary_assessment.json)
![OpenScientist summary assessment](openscientist_artifacts/provenance_summary_assessment.png)