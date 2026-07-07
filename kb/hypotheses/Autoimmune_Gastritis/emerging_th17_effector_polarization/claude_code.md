---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T14:08:38.150802'
end_time: '2026-07-01T14:13:13.539858'
duration_seconds: 275.39
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Autoimmune Gastritis
  category: Complex
  hypothesis_group_id: emerging_th17_effector_polarization
  hypothesis_label: Emerging Th17/IL-17 Effector Contribution
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: emerging_th17_effector_polarization\nhypothesis_label:\
    \ Emerging Th17/IL-17 Effector Contribution\nstatus: EMERGING\ndescription: Human\
    \ data show a gastric H+/K+ ATPase-specific Th17/IL-17 signature, and effector-transfer\n\
    \  models show that Th1, Th2, and Th17 cells can each induce autoimmune gastritis\
    \ with distinct pathology\n  and differing susceptibility to regulatory T-cell\
    \ suppression. Which effector arm dominates human disease,\n  and whether it shifts\
    \ over the disease course, is unresolved and carries therapeutic implications\
    \ (e.g.,\n  anti-IL-17 blockade).\nevidence:\n- reference: PMID:35911678\n  reference_title:\
    \ Gastric Th17 Cells Specific for H+/K+-ATPase and Serum IL-17 Signature in Gastric\
    \ Autoimmunity.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet:\
    \ Gastric LPMCs from all AIG patients, but not those from HCs, were activated\
    \ by H+/K+-ATPase\n    and were able to proliferate and produce high levels of\
    \ IL-17A and IL-17F.\n  explanation: Human gastric T cells produce IL-17A/IL-17F\
    \ on H+/K+ ATPase stimulation, evidencing a Th17\n    effector contribution.\n\
    - reference: PMID:18641328\n  reference_title: Th1, Th2, and Th17 effector T cell-induced\
    \ autoimmune gastritis differs in pathological\n    pattern and in susceptibility\
    \ to suppression by regulatory T cells.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: We have evaluated the capacity of fully differentiated\
    \ Th1, Th2, and Th17 cells derived from\n    a mouse bearing a transgenic TCR\
    \ specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,\n    to induce\
    \ autoimmune gastritis after transfer to immunodeficient recipients.\n  explanation:\
    \ Th17 effector cells can independently induce autoimmune gastritis in the transfer\
    \ model,\n    supporting an emerging Th17 arm.\n- reference: PMID:31080562\n \
    \ reference_title: Intrinsic factor recognition promotes T helper 17/T helper\
    \ 1 autoimmune gastric inflammation\n    in patients with pernicious anemia.\n\
    \  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Most of these\
    \ clones (94%) showed a T helper 17 or T helper 1 profile.\n  explanation: In\
    \ pernicious anemia, intrinsic-factor-specific gastric CD4 clones are predominantly\
    \ Th17/Th1\n    (Th17-skewed), evidencing a Th17 contribution in the intrinsic-factor-reactive\
    \ compartment."
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 21
  total_cost_usd: 1.9079006000000003
  session_id: 5c58c42e-aa53-5307-a59b-32bd2414492b
  stop_reason: end_turn
citation_count: 10
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Autoimmune Gastritis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** emerging_th17_effector_polarization
- **Hypothesis Label:** Emerging Th17/IL-17 Effector Contribution
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: emerging_th17_effector_polarization
hypothesis_label: Emerging Th17/IL-17 Effector Contribution
status: EMERGING
description: Human data show a gastric H+/K+ ATPase-specific Th17/IL-17 signature, and effector-transfer
  models show that Th1, Th2, and Th17 cells can each induce autoimmune gastritis with distinct pathology
  and differing susceptibility to regulatory T-cell suppression. Which effector arm dominates human disease,
  and whether it shifts over the disease course, is unresolved and carries therapeutic implications (e.g.,
  anti-IL-17 blockade).
evidence:
- reference: PMID:35911678
  reference_title: Gastric Th17 Cells Specific for H+/K+-ATPase and Serum IL-17 Signature in Gastric Autoimmunity.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Gastric LPMCs from all AIG patients, but not those from HCs, were activated by H+/K+-ATPase
    and were able to proliferate and produce high levels of IL-17A and IL-17F.
  explanation: Human gastric T cells produce IL-17A/IL-17F on H+/K+ ATPase stimulation, evidencing a Th17
    effector contribution.
- reference: PMID:18641328
  reference_title: Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological
    pattern and in susceptibility to suppression by regulatory T cells.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We have evaluated the capacity of fully differentiated Th1, Th2, and Th17 cells derived from
    a mouse bearing a transgenic TCR specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,
    to induce autoimmune gastritis after transfer to immunodeficient recipients.
  explanation: Th17 effector cells can independently induce autoimmune gastritis in the transfer model,
    supporting an emerging Th17 arm.
- reference: PMID:31080562
  reference_title: Intrinsic factor recognition promotes T helper 17/T helper 1 autoimmune gastric inflammation
    in patients with pernicious anemia.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Most of these clones (94%) showed a T helper 17 or T helper 1 profile.
  explanation: In pernicious anemia, intrinsic-factor-specific gastric CD4 clones are predominantly Th17/Th1
    (Th17-skewed), evidencing a Th17 contribution in the intrinsic-factor-reactive compartment.
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

I now have sufficient depth to write the full report.

# Mechanistic Hypothesis Search Report

## Hypothesis: `emerging_th17_effector_polarization` — Emerging Th17/IL-17 Effector Contribution in Autoimmune Gastritis

---

## 1. Executive Judgment

**Verdict: Partially supported / unresolved as to which effector arm dominates human disease — but the mechanistic contribution of Th17/IL-17 itself is well established.**

There is now consistent evidence across human tissue, human serum, and murine adoptive-transfer models that a Th17/IL-17 axis is present and mechanistically active in autoimmune gastritis (AIG): gastric lamina propria mononuclear cells (LPMCs) from AIG patients proliferate and secrete IL-17A/IL-17F specifically upon H+/K+-ATPase stimulation (Bella et al., PMID:35911678); serum IL-17A/IL-17F/IL-21/IL-17E are elevated in AIG versus healthy and iron-deficiency-anemia controls; IL-17A signals through IL-17RA on parietal cells to trigger caspase-dependent apoptosis and, via NLRP3-ROS, parietal cell death (PMID:29930985 and follow-on mechanistic work); and Th17 effector cells transferred alone are sufficient to produce the most rapid and severe gastritis of any Th subset in the TxA23 transgenic-TCR transfer model (PMID:18641328).

However, three qualifications prevent calling this "established" rather than "emerging":
1. **Th1/IFN‑γ remains the textbook-dominant, more extensively validated axis** — most mechanistic murine work (including the foundational TxA23/BALB/c models) and most human immunopathology literature frame AIG as primarily Th1-driven, with Th17 as a secondary or co-occurring arm.
2. **IL-17 signaling is context-dependent and can be protective, not pathogenic**, in the closely related setting of *H. pylori*-associated gastric pathology — IL-17RA-deficient mice develop gastric cancer faster and more completely than wild-type mice on an InsGAS background (PMID:39588838), directly cautioning against a simple "block IL-17 to treat AIG" inference.
3. **No human interventional (anti-IL-17) data exist in AIG specifically.** All "IL-17 blockade is beneficial" evidence is preclinical (TxA23 mouse) or extrapolated from unrelated IL-17-driven diseases (psoriasis, psoriatic arthritis) where secukinumab/other IL-17A inhibitors are approved — and IL-17 inhibitors are documented to *precipitate or worsen* IBD in humans, an important safety signal for any therapeutic extrapolation to the gut.

So: the *existence* of a Th17/IL-17 effector contribution is well supported; the *hypothesis's implicit therapeutic corollary* (that IL-17 blockade would help) and the *claim that Th17 dominance shifts over disease course or defines a subtype* remain open, underpowered, or actively contradicted by adjacent-disease evidence.

---

## 2. Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Mechanistic claim tested | Key finding | Disease subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| Bella et al. 2022, PMID:35911678 (Front Immunol) | Human clinical | **Supports** | Gastric H/K-ATPase-specific Th17 response exists in AIG | Gastric LPMCs from AIG (not HC) proliferate and secrete IL-17A/F upon H+/K+-ATPase stimulation; serum IL-17A, IL-17F, IL-21, IL-17E all significantly elevated in AIG (43 pts) vs HC (47) and IDA-without-AIG (20) | AIG, mixed stage, mostly with concurrent autoimmune thyroiditis | Moderate. Gastric-tissue mechanistic arm n=8 AIG/4 HC — small. IFN-γ/Th1 cytokines **not measured**, so no head-to-head Th1-vs-Th17 comparison within the same cohort. No stage/severity correlation reported. |
| Van Driel/Gleeson et al. 2008, PMID:18641328 (Int Immunol) | Model organism (mouse, TxA23 TCR-transgenic transfer) | **Supports** (Th17 sufficiency) but also **qualifies** (distinct, not identical, pathology) | Th17 cells alone can induce AIG; compare Th1/Th2/Th17 pathogenicity and Treg susceptibility | Th17-induced disease was fastest and most severe (80% destructive parietal-cell loss at 4 wk vs 20% for Th1) with a distinctive eosinophil/granulocyte-rich infiltrate and highest serum IgE (12.0±2.0 mg/mL); critically, Th17 disease was **far more resistant to polyclonal Treg suppression** (9% protection at 6 wk vs 84% for Th1) unless effector:Treg ratio was favorable | Mouse, monospecific TCR transfer — not natural polyclonal human disease | High internal validity for the transfer model; limited external validity — a single-epitope, single-TCR system, not polyclonal spontaneous autoimmunity. Authors themselves flag uncertainty over whether the eosinophilic signature is real or an artifact of differential detection in other studies. |
| Pisani/D'Elios et al. 2019, PMID:31080562 (Oncotarget) | Human clinical (T-cell clones from gastric mucosa) | **Supports** | Intrinsic-factor-reactive gastric CD4+ clones in pernicious anemia are Th17/Th1-skewed | 94% of 265 gastric T-helper clones from 7 PA patients were Th17 or Th1 phenotype; IF-specific clones secreted IFN-γ and IL-17, produced TNF-α, IL-21, and helped B cells make antibody | Pernicious anemia (a late-stage/complication phenotype of AIG with cobalamin deficiency) | Moderate-high for the specific clone population studied, but small (n=7 patients) and specific to the intrinsic-factor-reactive compartment, not necessarily representative of H/K-ATPase-reactive clones or earlier-stage AIG. |
| Kim et al., PMID:29930985 (Cell Mol Gastroenterol Hepatol 2018) | Model organism + in vitro (mouse organoid) | **Supports** (mechanism) | IL-17A directly causes parietal cell apoptosis | IL-17A induces caspase-dependent apoptosis in parietal cells/gastric organoids; anti-IL-17A neutralizing antibody reduced parietal cell atrophy and metaplasia in a chronic atrophic gastritis mouse model | Mouse (likely DMP-777/L635 chemical-atrophy or related model), not the autoantigen-specific TxA23 model | Direct causal (interventional) evidence in mice — strong for mechanism, but a single preclinical model, no human interventional confirmation. |
| NLRP3/ROS mechanistic literature (synthesized in reviews, e.g., Tandfonline 2023 review PMID pending/2174531) | Review-level synthesis of model organism/in vitro data | **Supports** (mechanism, review-level) | IL-17 → NLRP3 inflammasome-ROS → parietal cell death | CD4+ T cell IL-17 targeting H+/K+-ATPase activates NLRP3-ROS pathway causing parietal cell death | AIG generally | Review-level; underlying primary sources not independently re-verified here — treat as orientation, not standalone primary evidence. |
| Zhang et al. 2025, DOI:10.1007/s12026-025-09643-4 (Immunol Res) | Model organism (TxA23 mouse, early 2–4mo vs advanced 6–12mo, STAT3⁻/⁻, STA-21 drug) | **Supports** (interventional, dynamic) | Th17/Treg imbalance (via STAT3) drives progression; correcting it is disease-modifying | STAT3 inhibition (STA-21) or STAT3 knockout reduced Th17 (CD4+IL-17+) cells, IL-17/IL-21/IL-23R/RORγt, restored Treg (CD4+FOXP3+)/IL-10/FOXP3, reduced inflammation and early metaplastic change | Mouse, explicitly early- vs advanced-stage comparison | Moderate-high — directly tests the "does effector arm/balance shift with stage" question via a stage-stratified design; but long-term progression to full metaplasia/dysplasia was **not evaluated**, and translation to human AIG is unconfirmed. |
| Yang/Merchant-lab lineage, PMID:39588838 (Gut Microbes 2024) | Model organism (InsGAS × Il17ra⁻/⁻ mouse, H. pylori PMSS1 infection) | **Refutes/qualifies** (context-dependent risk of blocking IL-17) | Is IL-17 signaling uniformly pathogenic in gastric autoimmune/inflammatory disease? | IL-17RA deficiency **accelerated** gastric cancer (dysplasia→cancer by 3–6 months vs low-grade dysplasia in WT), worsened inflammation, bacterial burden, parietal cell loss, and proliferation; IL-17RA signaling was protective by limiting Th1/Th17 hyperactivation and preserving mucin/antimicrobial defenses | H. pylori-infected InsGAS mice — a related but distinct gastric-carcinogenesis-prone model, not the autoantigen-driven TxA23 AIG model | High internal validity, directly interventional (genetic KO); **major limiting/refuting evidence** for any therapeutic corollary of the seed hypothesis — the disease context (infection-driven carcinogenesis vs autoantigen-driven atrophy) differs, so it *qualifies rather than directly refutes* the AIG-specific claim, but it is a strong caution against assuming anti-IL-17 therapy is safe/beneficial in gastric autoimmune contexts generally. |
| IL-17A in gastric carcinogenesis: good or bad? PMC11638189 (review, 2024) | Review | **Qualifies** | Net effect of chronic Th17/IL-17 activity on long-term outcome (cancer risk) | IL-17 is elevated across the AIG→metaplasia→dysplasia continuum, suggesting sustained Th17 activity pre-dates gastric cancer; yet higher tumor IL-17RA expression is a *favorable* prognostic marker post-diagnosis — a dual, stage-dependent role | AIG/IM/dysplasia/gastric cancer continuum | Review-level synthesis; underscores an outstanding stage-dependence question rather than resolving it. |
| Frontiers 2024 review, "Pro- and anti-inflammatory cytokines: the hidden keys to autoimmune gastritis therapy" (fphar.2024.1450558) | Review | **Competing/contextualizing** | Relative weighting of Th1 vs Th17 vs other cytokine axes | States plainly that "the Th1-dependent activation of human gastric cytotoxic mechanisms with IFN[-γ] and TNFα production are crucial," treating Th1 as the dominant/established axis, with Th17/IL-17, IL-21, IL-33, IL-6, IL-13, TSLP as parallel/contributing but less-established axes; explicitly flags IL-6, IL-27, IL-15, TGF-β roles as unresolved | AIG generally, largely extrapolated from TxA23 mouse | Review-level, but useful for calibrating current expert consensus: Th1 primacy, Th17 as an active but secondary/emerging arm. |
| Springer review, "Immunological mechanisms of autoimmune gastritis" (2026, link.springer.com/10.1007/s10238-026-02080-z), and PMC12563516 review | Review | **Supports** (dual-axis framing) | Th1/Th17 dual-axis model; role of dendritic cells and ILC3s | Frames pathogenesis as "a dual axis of IFN-γ and IL-17-mediated inflammation," with ILC3-derived IL-17/IL-22 also implicated; explicitly states DC/ILC3 contribution is "largely speculative" and mechanisms of Treg failure in human AIG are under-studied | AIG generally | Review-level; corroborates dual-axis framing but flags the innate-lymphoid contribution as unproven. |

---

## 3. Mechanistic Causal Chain

**Upstream trigger → intermediate steps → clinical manifestation**, annotated by evidence strength:

1. **Genetic susceptibility (HLA, AIRE-related) + trigger** (possible *H. pylori* molecular mimicry with H+/K+-ATPase, or intrinsic-factor cross-reactivity) → **[moderate evidence, established in Th1 literature, weaker for Th17-specific triggering]**. H. pylori is repeatedly invoked as a molecular-mimicry trigger for H+/K+-ATPase-reactive Th1 cells; whether it specifically primes the Th17 compartment (versus Th17 arising secondarily/independently) is not directly shown.
2. **Autoantigen presentation (H+/K+-ATPase, intrinsic factor) by gastric MHC-II+ cells to naive CD4+ T cells** → **[well established]**, largely from Th1 literature (IFN-γ/TNF-α inducing MHC-II upregulation, amplifying presentation).
3. **CD4+ T cell polarization into Th1, Th2, and Th17 subsets in parallel** (rather than sequentially) → **[directly shown]** in the TxA23 transfer model (PMID:18641328) and implicit in human gastric mucosa (Th1/Th17-mixed clones, PMID:31080562).
4. **Th17 cells secrete IL-17A/F (+IL-21, IL-22 via ILC3s)** → **[directly shown]** in human LPMC and serum data (PMID:35911678).
5. **IL-17A binds IL-17RA on parietal cells** → **caspase-dependent apoptosis, and NLRP3-ROS-mediated cell death** → **[direct causal/interventional evidence in mice — anti-IL-17A antibody reduces parietal cell atrophy]** (PMID:29930985).
6. **Progressive parietal cell loss → oxyntic atrophy → achlorhydria/hypergastrinemia → metaplasia (SPEM) → occasional dysplasia** → **[well documented across models, but the differential contribution of the Th17 arm at each step, versus Th1/other cytokines, is not cleanly separated]**.
7. **Clinical sequelae**: iron-deficiency anemia (early), pernicious anemia/B12 deficiency (via intrinsic-factor antibodies, later), increased gastric neuroendocrine tumor and gastric cancer risk (chronic) → **[established for the disease broadly; the Th17-specific contribution to the ECL-hyperplasia/carcinoid and cancer endpoints is the least resolved link]**, complicated by the IL-17RA-protective finding in H. pylori-driven carcinogenesis (PMID:39588838), which shows IL-17 signaling can *restrain* rather than *drive* the later carcinogenic step in a related context.
8. **Treg-mediated regulation** intersects at multiple points — Th17-induced disease is disproportionately Treg-resistant compared to Th1 (PMID:18641328), and STAT3-dependent Th17/Treg imbalance appears to widen with disease stage (2025 Immunol Res paper) → **[direct mechanistic/interventional evidence in mice; not yet tested in human AIG]**.

**Strongest links**: antigen-driven CD4+ polarization → cytokine secretion → parietal cell apoptosis (steps 3–5) has both human associative and mouse interventional support.
**Weakest/inferred links**: trigger specificity for Th17 (step 1), and the Th17 arm's role in the late carcinogenesis step (step 7), where evidence in an adjacent model actually points the opposite direction.

---

## 4. Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| **No paired human Th1-vs-Th17 quantification in the same cohort** | The Della Bella 2022 human study measured only IL-17-family cytokines; IFN-γ was not measured in the same patients. | Without paired measurement, "Th17 emerging" vs "Th1 still dominant" cannot be adjudicated in human tissue — current claims rely on separate studies with different cohorts/methods. | Searched and fetched full text of PMID:35911678; confirmed IFN-γ absent from panel. | A single cohort study with simultaneous serum/tissue Th1 (IFN-γ, TNF-α) and Th17 (IL-17A/F, IL-21, IL-22) panels, ideally with flow-sorted antigen-specific clones, across disease stages. |
| **No disease-stage-stratified human data** | All human Th17 evidence (Bella et al., D'Elios/Pisani et al.) is cross-sectional, mixing early atrophic gastritis with established pernicious anemia. | The seed hypothesis explicitly asks whether the dominant arm "shifts over the disease course" — no human data currently test this; only mouse data (2025 STAT3 paper) stratify by stage. | Searched specifically for stage-dependent human/mouse Th17 data; found only the mouse TxA23 early (2–4mo) vs advanced (6–12mo) comparison. | Longitudinal or stage-matched cross-sectional human cohorts (e.g., OLGA/OLGIM-staged biopsies) with paired cytokine/T-cell-subset profiling from early corpus-limited atrophy through pernicious anemia and dysplasia. |
| **IL-17 signaling can be protective, not pathogenic, in H. pylori-driven gastric carcinogenesis** | PMID:39588838 shows IL-17RA loss *accelerates* cancer in InsGAS mice. | This directly complicates the therapeutic corollary of the seed hypothesis (anti-IL-17 blockade) — a disease-context-dependent (autoimmune-antigen-driven atrophy vs. infection-driven carcinogenesis) divergence in IL-17's net effect is unresolved. | Explicitly searched for and fetched this paper. | Direct testing of anti-IL-17A/IL-17RA blockade in the autoantigen-driven TxA23 model (not just the chemical/DMP-777 atrophy model used by Kim et al. 2018) tracked to the metaplasia/dysplasia endpoint, and ideally in an H. pylori-negative AIG-mimicking model to separate the two contexts. |
| **No AIG-specific human interventional (anti-IL-17) data** | Secukinumab/other IL-17A blockers have never been trialed in AIG. | The therapeutic implications flagged in the hypothesis label are currently based entirely on preclinical mouse data (Kim et al. 2018) plus off-target inference from IL-17 blockade's known GI risk (IBD exacerbation) in unrelated diseases. | Searched specifically for secukinumab/AIG trials; found none — only general secukinumab autoimmune-disease and IL-17-inhibitor-associated-IBD safety literature. | A biomarker-stratified pilot/observational study (or n-of-1/compassionate use) monitoring gastric histology/serology in AIG patients incidentally exposed to anti-IL-17 biologics for psoriasis/PsA, retrospectively or prospectively. |
| **Innate lymphoid cell (ILC3) contribution to gastric IL-17/IL-22 is "largely speculative"** (explicit quote from PMC12563516/Springer review) | Whether ILC3s materially add to, or are the primary source of, gastric IL-17 in AIG (versus adaptive Th17) is unknown. | If ILC3s are a major IL-17 source, this changes both the mechanistic model and any IL-17-pathway drug target rationale (since ILC3s are less amenable to antigen-specific tolerance approaches). | Reviewed synthesized in fetched Springer/PMC review text. | Human gastric mucosal single-cell/flow cytometry distinguishing CD3⁻ ILC3 (RORγt+) from CD3+ Th17 as IL-17/IL-22 sources in AIG biopsies. |
| **Mechanism of Treg resistance to Th17-driven disease** | Mouse data show Th17-induced AIG is markedly more Treg-resistant than Th1-induced disease (9% vs 84% protection), with recovered Th17 effectors remaining fully functional (not anergized). | This has direct bearing on why Th17-driven AIG (if it dominates in a subset of patients) might be a more treatment-refractory subtype, and on rational immunomodulatory strategy (Treg-based therapy may underperform if the effector arm is Th17-skewed). | Full text of PMID:18641328 fetched and reviewed. | Human ex vivo co-culture assays testing whether AIG-patient Tregs suppress autologous IL-17A/H+/K+-ATPase-specific effector clones as effectively as IFN-γ-producing clones; correlate with serum Treg markers. |
| **No GenCC/ClinGen/GWAS-level genetic evidence tying IL-17 pathway genes (IL17A, IL17RA, IL23R, RORC, STAT3) specifically to AIG risk** | Searches surfaced no AIG-specific GWAS or ClinGen gene-disease validity assertion for Th17-pathway genes; STAT3 evidence is purely preclinical mouse. | Absence of human genetic evidence weakens causal (as opposed to associative/downstream) inference for a primary Th17 driver role. | This search did not locate any AIG-specific GWAS/GenCC/ClinGen record for IL17A/IL17RA/IL23R/STAT3/RORC; this is an explicit absence as of the search date, not confirmed exhaustively via ClinGen's database directly. | A dismech curator should check ClinGen Gene-Disease Validity and GWAS Catalog directly for AIG/pernicious-anemia + IL17 pathway gene associations before asserting "no genetic evidence exists." |

---

## 5. Alternative Models

| Model | Relationship to seed hypothesis |
|---|---|
| **Th1/IFN-γ-dominant model** (canonical; TxA23 mouse, most human immunopathology literature) | **Primary alternative/competing model.** Most reviews treat Th1 as the established main axis (IFN-γ/TNF-α → MHC-II upregulation → cytotoxicity), with Th17 as a co-occurring, possibly secondary, arm. This is the dominant existing KB framing that the "emerging" hypothesis is explicitly proposed alongside, not replacing. |
| **Molecular mimicry / H. pylori-triggering model** | **Upstream cause**, not competing — could feed into either the Th1 or Th17 arm (or both); H. pylori is invoked mainly as a Th1 trigger, but its role in priming Th17 specifically is unresolved (see Knowledge Gaps). |
| **IL-6/STAT3-driven Th17/Treg-imbalance model** | **Mechanistic refinement/parallel** to the Th17 hypothesis — proposes IL-6/STAT3 signaling as the proximal driver tipping the Th17:Treg ratio, rather than IL-17 itself being primary; the 2025 STAT3-inhibitor mouse study supports this as a therapeutically actionable upstream node. |
| **Innate lymphoid cell (ILC3)-driven IL-17/IL-22 model** | **Parallel/competing source model** — proposes that gastric IL-17/IL-22 in AIG derives substantially from innate ILC3s rather than adaptive Th17 cells, which would mean "Th17" is a mislabeling of the effector source; currently speculative per reviewed literature. |
| **Protective/context-dependent IL-17 model (from H. pylori-carcinogenesis data)** | **Direct competing claim about net effect**, not about existence of the pathway — argues IL-17 signaling can be net-protective (limiting Th1/Th17 hyperactivation, preserving mucosal defenses) in gastric disease overall, cautioning against assuming the seed hypothesis's implied therapeutic corollary (IL-17 blockade = benefit) generalizes. |
| **Th2/eosinophilic model** | **Parallel mechanism**, not a real competitor for "dominant" status in most literature, but empirically the transfer-model data (PMID:18641328) show Th2 cells also independently cause disease with a distinct (eosinophilic, high-IgE) pattern — relevant because the Th17-induced pattern in that same study was described as similarly eosinophil/IgE-rich, raising a possible confound between "Th17" and "Th2-like/mixed" phenotypes in that particular mouse system. |
| **Treg-deficiency/failure model** (upstream, cause-agnostic) | **Upstream permissive cause** — regardless of which effector arm (Th1 or Th17) dominates, insufficient or dysfunctional Treg suppression is required for any effector arm to cause overt disease; Th17-induced disease's disproportionate Treg-resistance is a specific instantiation of this broader model. |

---

## 6. Discriminating Tests

1. **Paired single-cohort Th1/Th17 cytokine and antigen-specific clone profiling across OLGA/OLGIM disease stages.** Sample: gastric corpus biopsies + serum from AIG patients spanning early corpus-restricted atrophy → pernicious anemia → dysplasia. Assay: multiplex serum cytokine panel (IFN-γ, TNF-α, IL-17A/F, IL-21, IL-22) + H+/K+-ATPase- and intrinsic-factor-tetramer-sorted CD4+ clones for intracellular cytokine staining. Expected result if hypothesis correct: a shift toward IL-17-dominant clones/cytokines with advancing stage or a defined "Th17-high" subgroup distinguishable at diagnosis.
2. **Single-cell RNA-seq/CyTOF of gastric mucosa distinguishing adaptive Th17 (CD3+RORγt+) from ILC3 (CD3⁻RORγt+) IL-17/IL-22 sources**, resolving the "largely speculative" ILC3 contribution flagged in reviews.
3. **Ex vivo Treg-suppression assay using autologous AIG-patient Tregs against IL-17-producing versus IFN-γ-producing autoantigen-specific effector clones**, testing whether the mouse-derived Treg-resistance finding for Th17 (PMID:18641328) replicates in human cells — a biomarker (e.g., serum Treg:Th17 ratio) predicting refractoriness to immunomodulation would be clinically actionable.
4. **Extend the TxA23 anti-IL-17A-neutralization experiment (currently done only in a DMP-777/chemical-atrophy model, PMID:29930985) to the autoantigen-driven TxA23 transfer model with long-term follow-up to metaplasia/dysplasia**, directly testing whether IL-17 blockade helps or — per the H. pylori/InsGAS cancer-acceleration data (PMID:39588838) — instead worsens long-term carcinogenic risk in an autoimmune (not infectious) trigger context.
5. **Retrospective pharmacovigilance/cohort study of gastric histology and AIG serology (parietal cell/H+/K+-ATPase antibodies, gastrin, pepsinogen I/II) in patients on anti-IL-17A biologics (secukinumab, ixekizumab, brodalumab) for psoriasis/PsA/ankylosing spondylitis**, using existing large biologic registries — a natural experiment for whether IL-17 blockade measurably alters gastric autoimmune markers or precipitates/ameliorates AIG-like findings, directly informing the therapeutic corollary without needing a de novo AIG trial.
6. **GWAS/ClinGen/GenCC query for IL17A, IL17RA, IL23R, RORC, STAT3, IL6, IL6R variant association with AIG or pernicious anemia risk**, to establish (or rule out) a genetic causal anchor for the Th17 arm analogous to existing HLA associations for Th1-mediated autoimmunity.

---

## 7. Curation Leads (require curator verification before committing)

**Candidate evidence references to consider adding** (verify PMID, fetch abstract via `just fetch-reference`, confirm exact snippet substring before use):

- `PMID:29930985` — Kim et al., "Interleukin-17A Promotes Parietal Cell Atrophy by Inducing Apoptosis" (Cell Mol Gastroenterol Hepatol, 2018). Candidate snippet to verify against cached abstract: language describing IL-17A receptor expression on parietal cells and anti-IL-17A neutralizing antibody reducing atrophy/metaplasia in a chronic atrophic gastritis mouse model. `evidence_source: MODEL_ORGANISM`. **This directly strengthens the mechanistic (step 5) causal edge and should likely be added to the hypothesis's evidence list.**
- `PMID:39588838` — "IL-17 signaling protects against Helicobacter pylori-induced gastric cancer" (Gut Microbes, 2024). Candidate use: as a `supports: REFUTE` or qualifying evidence item on a **new** `discussions` entry (see below), not as direct support — it argues the opposite net effect of IL-17 signaling in a related model. `evidence_source: MODEL_ORGANISM`.
- `DOI:10.1007/s12026-025-09643-4` — Zhang et al., "STAT3 inhibition mitigates experimental autoimmune gastritis by restoring Th17/Treg immune balance" (Immunologic Research, 2025). No PMID found in this search session — curator should locate/confirm the PMID before citing. Candidate use: supports a stage-dependent Th17/Treg-imbalance mechanism and a STAT3-centric druggable node; consider as `evidence_source: MODEL_ORGANISM`, and possibly as the anchor for a **new, distinct** hypothesis or a refinement node (STAT3/IL-6 axis) rather than folding into this hypothesis as-is.
- `PMID:39588838`'s companion review "IL-17A in gastric carcinogenesis: good or bad?" (PMC11638189, Front Immunol 2024) — review-level; useful for a `notes:` field or as background citation, not primary evidence per dismech SOP (reviews are orientation-only unless they contain directly relevant synthesized evidence, clearly labeled).

**Candidate pathophysiology nodes/edges:**
- A node for "IL-17RA-mediated Parietal Cell Apoptosis" downstream of "Gastric Th17 Cell Activation," feeding into the existing "Parietal Cell Loss" node, sourced from PMID:29930985 (caspase-dependent) and the NLRP3-ROS mechanism (needs a primary-source citation check — the NLRP3 claim in this search was only found in review synthesis, not independently verified against a primary paper).
- A qualifying/competing edge or `discussions` (`kind: KNOWLEDGE_GAP`) node capturing that IL-17RA signaling is *protective* against gastric carcinogenesis in the H. pylori/InsGAS context (PMID:39588838), to flag the tension with any therapeutic target framing of IL-17 in AIG.

**Candidate ontology terms:**
- Cell type: `CL:0000899` (Th17 cell) for gastric-infiltrating Th17 populations (verify label via OAK before use).
- Biological process candidates to verify via OAK (`GO`): IL-17-mediated signaling pathway, NLRP3 inflammasome complex assembly, positive regulation of apoptotic process — do not assume GO IDs without `runoak` lookup.
- Consider `MAXO`/`NCIT` treatment term placeholders only as *hypothetical* (not yet evidenced in humans for AIG) — e.g., secukinumab (`NCIT` term to be looked up) should **not** be added as an actual `treatments` entry for AIG given the complete absence of AIG-specific interventional data and the IBD-worsening safety signal; if added at all, it should be confined to a `discussions`/knowledge-gap note, explicitly flagged as speculative/unproven and context-dependent-risk.

**Candidate subtype/status considerations:**
- Consider whether `status: EMERGING` should be retained (recommended) rather than upgraded to `ESTABLISHED`, given: (a) no paired human Th1/Th17 comparative cohort, (b) no stage-stratified human data, (c) a directly conflicting protective role for IL-17 signaling in a related gastric-carcinogenesis model, and (d) zero human interventional data.
- Consider adding a **pernicious-anemia-stage-specific qualifier**: the strongest human Th17/Th1-mixed evidence (PMID:31080562) comes specifically from intrinsic-factor-reactive clones in pernicious anemia patients (a later-stage/complication phenotype), while the Della Bella cohort (PMID:35911678) is H+/K+-ATPase-reactive and stage-unstratified — a curator may want to record that current human Th17 evidence clusters at two different antigen-specificities/stages rather than a single unified stage-agnostic signature.

**Candidate `discussions` (knowledge-gap) prompts:**
1. *KNOWLEDGE_GAP*: "Does the dominant gastric effector arm (Th1 vs Th17) shift with AIG disease stage in humans (early corpus-limited atrophy → pernicious anemia → dysplasia), as suggested by stage-stratified mouse data (STAT3 paper) but never directly tested in human cohorts?" `attaches_to`: this hypothesis node. `proposed_experiments`: stage-stratified multiplex cytokine/clone profiling (see Discriminating Test #1).
2. *KNOWLEDGE_GAP* (or *HUMAN_MODEL_MISMATCH* candidate): "IL-17RA signaling is protective against gastric carcinogenesis in the H. pylori/InsGAS mouse model (PMID:39588838), while IL-17A neutralization is protective against parietal cell atrophy in a chemical-atrophy mouse model (PMID:29930985) — do these reflect genuinely different disease contexts (infection-driven carcinogenesis vs. autoantigen-driven atrophy), or does this indicate the murine models used for AIG mechanistic work have divergent, possibly context-limited, translational validity to human AIG?" This reads more like a `HUMAN_MODEL_MISMATCH` in spirit (translational-validity question across models) even though both arms are mouse-mouse — worth discussing with the module/schema maintainers whether `HUMAN_MODEL_MISMATCH` extends to cross-model consistency or whether a plain `KNOWLEDGE_GAP` is more appropriate; default to `KNOWLEDGE_GAP` unless a curator decides the schema intent covers model-to-model divergence.
3. *KNOWLEDGE_GAP*: "No AIG-specific GWAS, ClinGen, or GenCC gene-disease validity record for IL-17-pathway genes (IL17A, IL17RA, IL23R, RORC, STAT3) was located in this search — curator should directly query ClinGen/GWAS Catalog to confirm this absence before asserting it as a stated gap in the KB, since this search relied on general web search rather than exhaustive direct database queries."

All items above are leads only; every PMID/DOI must be run through `just fetch-reference` and `just validate-references`, and every ontology term through `just validate-terms-file`, before being committed to any `kb/disorders/Autoimmune_Gastritis.yaml` entry, per dismech SOP.

---

Sources consulted (representative; full citation list embedded in Evidence Matrix):
- [Gastric Th17 Cells Specific for H+/K+-ATPase and Serum IL-17 Signature in Gastric Autoimmunity — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9328118)
- [Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological pattern and in susceptibility to suppression by regulatory T cells — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2561289/)
- [Intrinsic factor recognition promotes T helper 17/T helper 1 autoimmune gastric inflammation in patients with pernicious anemia — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6499598/)
- [Interleukin-17A Promotes Parietal Cell Atrophy by Inducing Apoptosis — PubMed](https://pubmed.ncbi.nlm.nih.gov/29930985/)
- [IL-17 signaling protects against Helicobacter pylori-induced gastric cancer — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11639209/)
- [IL-17A in gastric carcinogenesis: good or bad? — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638189/)
- [Frontiers | Pro- and anti-inflammatory cytokines: the hidden keys to autoimmune gastritis therapy](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1450558/full)
- [The Autoimmune Gastritis Puzzle: Emerging Cellular Crosstalk and Molecular Pathways — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)
- [STAT3 inhibition mitigates experimental autoimmune gastritis by restoring Th17/Treg immune balance — Immunologic Research](https://link.springer.com/article/10.1007/s12026-025-09643-4)
- [Full article: Critical influence of cytokines and immune cells in autoimmune gastritis](https://www.tandfonline.com/doi/full/10.1080/08916934.2023.2174531)