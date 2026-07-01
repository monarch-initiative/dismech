---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-01T15:19:55.863914'
end_time: '2026-07-01T16:33:30.602581'
duration_seconds: 4414.74
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
    \ compartment.\nnotes: 'A claude_code hypothesis-search report (kb/hypotheses/Autoimmune_Gastritis/emerging_th17_effector_polarization)\n\
    \  graded this PARTIALLY SUPPORTED: the Th17/IL-17 mechanistic contribution is\
    \ well established (H+/K+\n  ATPase-specific gastric IL-17A/F production; IL-17RA\
    \ signaling drives parietal-cell apoptosis; Th17\n  transfer alone gives the most\
    \ severe gastritis in the TxA23 model), but which effector arm dominates\n  human\
    \ disease is unresolved, Th1 remains the more extensively validated axis, and\
    \ IL-17 can be protective\n  in H. pylori-associated gastric carcinogenesis (IL-17RA-deficient\
    \ mice develop gastric cancer faster),\n  cautioning against a simple \"block\
    \ IL-17\" therapeutic inference; no human anti-IL-17 data exist in AIG.\n  Retained\
    \ EMERGING. Run performed with the claude_code provider; an openscientist run\
    \ is pending.'"
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
    save_artifacts: false
    artifact_max_bytes: 5242880
citation_count: 24
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
notes: 'A claude_code hypothesis-search report (kb/hypotheses/Autoimmune_Gastritis/emerging_th17_effector_polarization)
  graded this PARTIALLY SUPPORTED: the Th17/IL-17 mechanistic contribution is well established (H+/K+
  ATPase-specific gastric IL-17A/F production; IL-17RA signaling drives parietal-cell apoptosis; Th17
  transfer alone gives the most severe gastritis in the TxA23 model), but which effector arm dominates
  human disease is unresolved, Th1 remains the more extensively validated axis, and IL-17 can be protective
  in H. pylori-associated gastric carcinogenesis (IL-17RA-deficient mice develop gastric cancer faster),
  cautioning against a simple "block IL-17" therapeutic inference; no human anti-IL-17 data exist in AIG.
  Retained EMERGING. Run performed with the claude_code provider; an openscientist run is pending.'
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

# Hypothesis-Search Report: Emerging Th17/IL-17 Effector Contribution to Autoimmune Gastritis

**Hypothesis ID:** `emerging_th17_effector_polarization`  
**Disease:** Autoimmune Gastritis (AIG)  
**Status in KB:** EMERGING  
**Report Date:** 2026-07-01  
**Papers reviewed:** 81  
**Confirmed findings:** 11  
**Iterations completed:** 5  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — retain EMERGING status with critical hypothesis revision required.**

The Th17/IL-17 effector contribution to autoimmune gastritis (AIG) is substantiated by direct human evidence showing antigen-specific Th17 responses in gastric tissue and by murine transfer models demonstrating Th17-driven gastritis. However, the hypothesis as originally framed requires significant revision on three grounds: (1) IL-17 receptor A (IL-17RA) signaling on gastric epithelium is **protective**, not cytotoxic, directly contradicting the seed claim that IL-17RA drives parietal cell apoptosis; (2) IL-17RA loss paradoxically increases B cell infiltration, autoantibody production, and mononuclear inflammation, suggesting that the pathogenic Th17-derived effector molecule is more likely **IL-21** than IL-17A/F itself; and (3) the therapeutic implication of anti-IL-17 blockade is contraindicated by the protective, anti-inflammatory, and potentially anti-carcinogenic roles of IL-17 signaling in the stomach.

The strongest evidence supporting a Th17 contribution comes from Della Bella et al. (2022), who demonstrated that gastric lamina propria mononuclear cells (LPMCs) from all AIG patients produced high levels of IL-17A and IL-17F upon H⁺/K⁺-ATPase stimulation ([PMID: 35911678](https://pubmed.ncbi.nlm.nih.gov/35911678/)), and from Troilo et al. (2019), who showed that 94% of intrinsic-factor-specific gastric CD4⁺ T cell clones in pernicious anemia exhibited a Th17 or Th1 profile ([PMID: 31080562](https://pubmed.ncbi.nlm.nih.gov/31080562/)). The murine TxA23 transfer model confirms that Th17 cells independently induce the most destructive gastritis and resist polyclonal Treg suppression ([PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). A 2025 study demonstrated that STAT3 inhibition corrects the Th17/Treg imbalance and alleviates AIG in this model ([PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/)).

The most important caveats are: (a) Th1 remains the more extensively validated effector axis in human AIG — earlier studies consistently found H⁺/K⁺-ATPase-reactive gastric T cell clones secreting Th1 cytokines ([PMID: 12645953](https://pubmed.ncbi.nlm.nih.gov/12645953/)); (b) which effector arm dominates at different disease stages is unresolved; (c) no human anti-IL-17 clinical data exist in AIG; and (d) the IL-17RA protective paradox makes such an intervention potentially harmful. The hypothesis should be retained as EMERGING but reframed: Th17 cells contribute to AIG pathology, likely via IL-21 and STAT3-mediated mechanisms rather than direct IL-17A/F epithelial cytotoxicity.

---

## Summary

Autoimmune gastritis (AIG) is a chronic inflammatory disease characterized by immune-mediated destruction of gastric parietal cells, resulting in achlorhydria, pernicious anemia, and increased risk of gastric neuroendocrine tumors and adenocarcinoma. The seed hypothesis posits that Th17 cells and their signature cytokine IL-17 represent an emerging effector arm in AIG pathogenesis, with therapeutic implications for anti-IL-17 blockade.

Our systematic review of 81 papers across 5 iterations confirms that a Th17 effector contribution exists in AIG — antigen-specific Th17 responses are demonstrable in human gastric tissue, and Th17 cells are independently capable of inducing destructive gastritis in murine models. However, three lines of evidence force a critical re-evaluation of the mechanistic model: IL-17RA is protective on gastric epithelium; IL-17RA loss worsens autoimmune-relevant pathology; and the STAT3/Th17 axis operates through downstream mediators (likely IL-21) rather than IL-17A/F alone. The Th1 paradigm remains better validated in human disease, and a competing Th2/eosinophil axis has emerged as an alternative explanation for the eosinophilic pathology initially attributed to Th17 cells.

The most important actionable recommendation is that the hypothesis description should be corrected to remove the IL-17RA parietal cell apoptosis claim and the anti-IL-17 therapeutic inference, and to note IL-21 as the candidate pathogenic effector cytokine produced by Th17 cells in the gastric autoimmune context.

---

## Key Findings

### Finding 1: H⁺/K⁺-ATPase-Specific Gastric Th17 Cells Are Present in All Human AIG Patients

The most direct evidence supporting the Th17 hypothesis comes from Della Bella et al. (2022), who demonstrated that gastric LPMCs from all AIG patients — but not healthy controls — were activated by H⁺/K⁺-ATPase and produced high levels of IL-17A and IL-17F ([PMID: 35911678](https://pubmed.ncbi.nlm.nih.gov/35911678/)). This is the first study to demonstrate antigen-specific Th17 responses against the canonical AIG autoantigen in human gastric tissue. The universality of the response (100% of patients tested) and the specificity for the disease-relevant autoantigen make this the strongest single piece of evidence for the hypothesis. Additionally, serum IL-17 levels were elevated in AIG patients, suggesting a systemic Th17 signature alongside the local mucosal response.

### Finding 2: Th17 Cells Induce the Most Destructive AIG and Resist Polyclonal Treg Suppression

In the TxA23 transgenic mouse model, Stummvoll et al. (2008) demonstrated that fully differentiated Th1, Th2, and Th17 cells each induce AIG with distinct pathology after transfer to immunodeficient recipients ([PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). Critically, **Th17 cells induced the most destructive disease**, characterized by eosinophilic infiltrates and elevated serum IgE. Furthermore, polyclonal Tregs could suppress Th1-mediated but not Th17-mediated disease (except at early time points). This resistance to Treg suppression was confirmed by two follow-up studies: Huter et al. (2008) showed that only antigen-specific TGFβ-induced iTregs — not polyclonal nTregs or iTregs — could prevent Th17-mediated AIG ([PMID: 19050237](https://pubmed.ncbi.nlm.nih.gov/19050237/)), and Huter et al. (2009) confirmed that even pre-activated nTregs failed to suppress Th17 gastritis ([PMID: 19539565](https://pubmed.ncbi.nlm.nih.gov/19539565/)). These findings carry important implications: if Th17 cells dominate in human AIG, conventional Treg-based therapies may be insufficient.

### Finding 3: Intrinsic-Factor-Specific Gastric T Cells Are Predominantly Th17/Th1

Troilo et al. (2019) generated intrinsic-factor-specific CD4⁺ T cell clones from gastric biopsies of pernicious anemia patients and found that 94% showed a Th17 or Th1 profile ([PMID: 31080562](https://pubmed.ncbi.nlm.nih.gov/31080562/)). This extends the Th17 evidence beyond H⁺/K⁺-ATPase to a second major autoantigen in AIG/pernicious anemia (intrinsic factor). The predominance of Th17/Th1 profiles among intrinsic-factor-reactive clones suggests that the Th17 contribution may be particularly relevant in the pernicious anemia subtype of AIG.

### Finding 4: STAT3/Th17 Axis Drives AIG Pathogenesis; STAT3 Inhibition Is Therapeutic

Zhang et al. (2025) demonstrated that STAT3 and phospho-STAT3 are significantly upregulated in TxA23 AIG mice, correlating with inflammation, atrophy, and spasmolytic polypeptide-expressing metaplasia (SPEM) ([PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/)). STAT3 knockout (TxA23 × STAT3⁻/⁻) reduced inflammation, preserved parietal cells, and suppressed SPEM. Pharmacological STAT3 inhibition with STA-21 alleviated disease and corrected the Th17/Treg imbalance — CD4⁺IL-17⁺ (Th17) cells were increased and CD4⁺FOXP3⁺ (Treg) cells decreased in AIG, and this was reversed by STAT3 blockade. This provides proof-of-concept for targeting the upstream STAT3 pathway rather than IL-17 directly, which is mechanistically more sound given the protective role of IL-17RA on epithelium.

### Finding 5: The Th1 Paradigm Remains Better Validated in Human AIG

The Th17 hypothesis must be evaluated against the well-established Th1 paradigm. Bergman et al. (2003) generated 16 H⁺/K⁺-ATPase-reactive CD4⁺ gastric T cell clones from 4 AIG patients and found they secreted Th1 cytokines ([PMID: 12645953](https://pubmed.ncbi.nlm.nih.gov/12645953/)). D'Elios et al. (2004) demonstrated that activated CD4⁺ Th1 cells infiltrating the gastric mucosa cross-recognize H⁺/K⁺-ATPase and H. pylori proteins via molecular mimicry ([PMID: 15242679](https://pubmed.ncbi.nlm.nih.gov/15242679/)). These foundational studies predate the discovery of Th17 biology and did not assay for IL-17 production. The recent Th17 findings do not invalidate the Th1 contribution but rather suggest a mixed Th1/Th17 response, with the relative dominance potentially varying by disease stage, autoantigen target, or genetic background.

### Finding 6: IL-17RA on Gastric Epithelium Is PROTECTIVE — Contradicts the Parietal Cell Apoptosis Claim

**This is the most critical finding for hypothesis revision.** Brackman et al. (2024) used Foxa3^cre^Il17ra^fl/fl^ mice with GI-epithelial-specific IL-17RA deletion and found that epithelial IL-17RA loss led to **increased** inflammation after H. pylori infection, not decreased ([PMID: 38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/)). IL-17RA signaling on epithelial cells maintains barrier integrity and limits immunopathogenic responses ([PMID: 38014948](https://pubmed.ncbi.nlm.nih.gov/38014948/)). IL-17RC expression is confirmed in human stomach epithelial cells ([PMID: 18928529](https://pubmed.ncbi.nlm.nih.gov/18928529/)). This directly refutes any claim that IL-17 signaling through IL-17RA drives parietal cell apoptosis and argues strongly against anti-IL-17 therapy in gastric autoimmunity. The seed hypothesis notes' statement that "IL-17RA signaling drives parietal-cell apoptosis" must be removed.

### Finding 7: Significant Eosinophilic Infiltration in Human AIG

Bettington & Brown (2013) analyzed 42 AIG patients (184 biopsies) and found that AIG displays significantly more eosinophil infiltration than other gastritis types: mean 34.5 eosinophils/HPF, >30/HPF in 46.1% of cases, p < 0.001 vs. other gastritis types ([PMID: 23277173](https://pubmed.ncbi.nlm.nih.gov/23277173/)). This partially validates the murine Th17 transfer model, which showed eosinophilic infiltration with Th17-mediated disease ([PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). However, the eosinophilia may alternatively be explained by Th2 mechanisms (see Finding 8), and the same study showed neutrophil infiltration in only 44.2% of AIG biopsies, suggesting neutrophil-driven pathology is not universal.

### Finding 8: Th2-Mediated AIG Is a Distinct Competing Mechanism with Eosinophilic Pathology

Harakal et al. (2016) demonstrated that transient Treg depletion in DEREG mice leads to AIG with dominant Th2 responses: IgG1 autoantibodies, elevated IgE, and massive eosinophilic inflammation ([PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/)). Disease severity was ameliorated in IL-4-deficient or eosinophil-deficient mice, confirming the Th2/eosinophil axis is causally required. Independently, Candon et al. (2004) showed that a Th2-committed TCR transgenic mouse develops spontaneous AIG with eosinophilic infiltration ([PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/)). Fujii et al. (2007) demonstrated that the eosinophilic hypertrophic AIG phenotype in NTx BALB/c mice is driven by Th2 cytokines (IL-4, GM-CSF) and is strain-dependent ([PMID: 17671757](https://pubmed.ncbi.nlm.nih.gov/17671757/)). This establishes Th2-driven AIG as a genuine competing mechanism that can produce eosinophilic pathology indistinguishable from Th17-driven eosinophilia.

### Finding 9: IL-17RA Loss Paradoxically Increases B Cell Recruitment and Autoantibodies

Algood et al. (2009) found that IL-17RA⁻/⁻ mice infected with H. pylori developed more severe mononuclear gastric inflammation, a marked increase in gastric B cells, plasma cells, lymphoid follicles, and enhanced H. pylori-specific serum antibody responses, while showing fewer gastric neutrophils ([PMID: 19812196](https://pubmed.ncbi.nlm.nih.gov/19812196/)). The authors explicitly noted that "in contrast to many chronic inflammatory diseases in which IL-17RA signaling promotes an inflammatory response, IL-17RA signaling" in the stomach behaves oppositely. Brackman et al. (2024) confirmed that epithelial-specific IL-17RA deletion also increased T follicular helper/B cell axis activation ([PMID: 38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/)). Since autoantibodies (anti-parietal cell, anti-intrinsic factor) are central to AIG pathogenesis, this paradox strongly argues against anti-IL-17 therapy and suggests that the pathogenic Th17-derived mediator may be **IL-21**, which directly promotes B cell differentiation, class-switching, and autoantibody production.

### Finding 10: IL-23/STAT3/IL-17 Axis Confirmed in Gastric Mucosa

Caruso et al. (2008) demonstrated that IL-23 is overexpressed in H. pylori-infected gastric mucosa and that IL-23 treatment of gastric LPMCs enhanced STAT3 activation and IL-17 secretion ([PMID: 18200634](https://pubmed.ncbi.nlm.nih.gov/18200634/)). Pharmacological STAT3 inhibition prevented IL-23-driven IL-17 synthesis. Both CD4⁺ and CD8⁺ T cells produce IL-17 in H. pylori-infected samples. This establishes the upstream IL-23→STAT3→IL-17 axis in gastric tissue and connects directly to the AIG-specific STAT3 finding (Finding 4, [PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/)), supporting STAT3 as a convergent therapeutic target.

### Finding 11: IL-17 Drives Neutrophil Recruitment but Human AIG Shows Variable Neutrophil Activity

Multiple H. pylori studies confirm that IL-17 recruits neutrophils to the gastric mucosa: reduced gastric Th17 cells correlate with reduced neutrophil accumulation in infected children ([PMID: 23299619](https://pubmed.ncbi.nlm.nih.gov/23299619/)), and IL-17 knockout mice had significantly lower neutrophil infiltration and MPO activity ([PMID: 19166417](https://pubmed.ncbi.nlm.nih.gov/19166417/)). IL-17 induces neutrophil-recruiting chemokines (KC, MIP-2, LIX) from gastric epithelial cells, fibroblasts, and macrophages ([PMID: 18948106](https://pubmed.ncbi.nlm.nih.gov/18948106/)). However, in human AIG, neutrophil infiltration is present in only 44.2% of biopsies ([PMID: 23277173](https://pubmed.ncbi.nlm.nih.gov/23277173/)) — substantial but not universal. This suggests that while IL-17-driven neutrophil recruitment occurs in some AIG cases, it is not a dominant or universal feature of the disease.

---

## Mechanistic Model and Interpretation

### Revised Causal Chain

{{figure:mechanistic_diagram.png|caption=Mechanistic causal chain for the Th17/IL-17 hypothesis in autoimmune gastritis, showing established (green), emerging (yellow), and contradicted (red) steps.}}

Based on all 11 findings, the mechanistic model must be revised from the original hypothesis. The key revision is that **IL-17A/F signaling via IL-17RA on gastric epithelium is protective, not destructive**. The causal chain should be understood as follows:

```
UPSTREAM TRIGGER
  Genetic susceptibility (PTPN22, HLA; PMID:34145262)
  + Environmental trigger (H. pylori molecular mimicry; PMID:15242679)
    ↓ [MODERATE evidence]

LOSS OF TOLERANCE  
  Treg dysfunction/depletion permits autoreactive T cell expansion
    ↓ [STRONG — nTx models, DEREG, Foxp3 biology]

T CELL POLARIZATION (via IL-23 → STAT3 → RORγt)
  Naïve CD4+ → Th17 (and Th1, Th2) differentiation
    ↓ [STRONG for Th1; EMERGING for Th17; MODERATE for Th2]

EFFECTOR PHASE — Th17 cells produce multiple cytokines:
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  IL-17A/F → IL-17RA/RC on epithelium                        │
  │    → PROTECTIVE: barrier integrity, limits inflammation      │
  │    → [STRONG evidence — CONTRADICTS original hypothesis]     │
  │                                                              │
  │  IL-21 → B cells → Autoantibodies (anti-H⁺/K⁺-ATPase, IF) │
  │    → [INFERRED — IL-17RA KO ↑ B cells; IL-21 ↑ in AIG]     │
  │    → CANDIDATE PATHOGENIC EFFECTOR                           │
  │                                                              │
  │  IL-17A → CXCL chemokines → Neutrophil recruitment           │
  │    → [STRONG in H. pylori; present in ~44% of AIG]          │
  │                                                              │
  │  GM-CSF, TNF-α → Macrophage activation → Tissue damage      │
  │    → [INFERRED — not directly tested in AIG]                 │
  │                                                              │
  │  Th17 → ex-Th17 plasticity (IFN-γ+ cells)                   │
  │    → [SPECULATIVE in AIG — shown in other autoimmune models] │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
    ↓

TISSUE DAMAGE
  Parietal cell destruction via:
    - Autoantibody-mediated (complement, ADCC)? [INFERRED]
    - Fas/FasL, TNF/TNFR death pathways? [SUGGESTED, PMID:10963131]
    - NOT IL-17RA-mediated apoptosis [REFUTED, PMID:38639570]
    ↓ [MODERATE — mechanism unresolved]

CLINICAL MANIFESTATION
  Corpus-dominant atrophic gastritis
  → Achlorhydria → Hypergastrinemia → Iron/B12 deficiency
  → SPEM (STAT3-driven, PMID:40471463)
  → Neuroendocrine tumors / Adenocarcinoma risk
    [STRONG — well-established clinical progression]
```

### The IL-21 Re-Framing

The most important mechanistic insight from this investigation is that the pathogenic effector of Th17 cells in AIG may not be IL-17A/F itself. Three convergent observations support this re-framing:

1. **IL-17RA is protective on gastric epithelium** — epithelial-specific deletion increases inflammation ([PMID: 38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/))
2. **IL-17RA loss increases B cell/autoantibody responses** — the opposite of what IL-17 blockade should achieve if IL-17 were pathogenic ([PMID: 19812196](https://pubmed.ncbi.nlm.nih.gov/19812196/))
3. **Th17 cells co-produce IL-21**, which is a potent driver of B cell class-switching, germinal center reactions, and autoantibody production — all central to AIG pathogenesis

This suggests a model in which Th17 cells contribute to AIG via IL-21-driven autoantibody production while IL-17A/F simultaneously provides a counterbalancing protective signal to the epithelium. Blocking IL-17 would remove the protective arm while leaving the IL-21-driven pathogenic arm intact — potentially worsening disease.

---

## Evidence Matrix

{{figure:evidence_classification.png|caption=Classification of evidence by type (human clinical, model organism, in vitro) and verdict (supports, refutes, qualifies, competing).}}

| # | Citation | Type | Verdict | Claim Tested | Key Finding | Context | Confidence |
|---|----------|------|---------|-------------|-------------|---------|------------|
| 1 | [PMID: 35911678](https://pubmed.ncbi.nlm.nih.gov/35911678/) | Human clinical | **Supports** | Ag-specific Th17 in AIG | All AIG patients' LPMCs produce IL-17A/F on H⁺/K⁺-ATPase stimulation | Human AIG | HIGH |
| 2 | [PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/) | Model organism | **Supports** | Th17 independently causes AIG | Th17 transfer → most destructive disease; resists polyclonal Treg | TxA23 mouse | HIGH |
| 3 | [PMID: 19050237](https://pubmed.ncbi.nlm.nih.gov/19050237/) | Model organism | **Supports** | Th17 AIG resists Treg | Only Ag-specific iTreg suppress Th17-mediated AIG | TxA23 mouse | HIGH |
| 4 | [PMID: 19539565](https://pubmed.ncbi.nlm.nih.gov/19539565/) | Model organism | **Supports** | Ag-specific iTreg needed | Pre-activated nTreg fail to suppress Th17 AIG | TxA23 mouse | HIGH |
| 5 | [PMID: 31080562](https://pubmed.ncbi.nlm.nih.gov/31080562/) | Human clinical | **Supports** | Th17/Th1 in pernicious anemia | 94% of IF-specific gastric clones are Th17/Th1 | Pernicious anemia | MODERATE |
| 6 | [PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/) | Model organism | **Supports** | STAT3 drives Th17/Treg imbalance | STAT3 KO + STA-21 reduce AIG; correct Th17/Treg ratio | TxA23 mouse | HIGH |
| 7 | [PMID: 18200634](https://pubmed.ncbi.nlm.nih.gov/18200634/) | Human/in vitro | **Supports** | IL-23→STAT3→IL-17 in stomach | IL-23 drives STAT3 and IL-17 in gastric LPMCs; STAT3 inhibition blocks | H. pylori | HIGH |
| 8 | [PMID: 23299619](https://pubmed.ncbi.nlm.nih.gov/23299619/) | Human clinical | **Supports** | Th17→neutrophil recruitment | Fewer Th17 = fewer neutrophils in children | H. pylori | MODERATE |
| 9 | [PMID: 19166417](https://pubmed.ncbi.nlm.nih.gov/19166417/) | Model organism | **Supports** | IL-17 drives neutrophils | IL-17 KO: lower neutrophil infiltration and MPO | H. pylori | HIGH |
| 10 | [PMID: 12645953](https://pubmed.ncbi.nlm.nih.gov/12645953/) | Human clinical | **Competing** | Th1 is dominant effector | H⁺/K⁺-ATPase-reactive clones secrete Th1 cytokines | Human AIG | HIGH |
| 11 | [PMID: 15242679](https://pubmed.ncbi.nlm.nih.gov/15242679/) | Human clinical | **Competing** | Th1/molecular mimicry | Th1 cells cross-recognize H⁺/K⁺-ATPase and H. pylori | Human AIG | MODERATE |
| 12 | [PMID: 38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/) | Model organism | **Refutes** | IL-17RA drives epithelial damage | Epithelial IL-17RA deletion INCREASES inflammation | Cell-specific KO | HIGH |
| 13 | [PMID: 38014948](https://pubmed.ncbi.nlm.nih.gov/38014948/) | Model organism | **Refutes** | IL-17 is pathogenic on epithelium | IL-17RA maintains barrier integrity | H. pylori | HIGH |
| 14 | [PMID: 19812196](https://pubmed.ncbi.nlm.nih.gov/19812196/) | Model organism | **Qualifies** | IL-17 promotes inflammation | IL-17RA KO: ↑ B cells, autoantibodies, mononuclear inflammation | H. pylori | HIGH |
| 15 | [PMID: 18928529](https://pubmed.ncbi.nlm.nih.gov/18928529/) | Tissue survey | **Qualifies** | IL-17RC expression | IL-17RC expressed in stomach epithelial cells | Normal human | MODERATE |
| 16 | [PMID: 23277173](https://pubmed.ncbi.nlm.nih.gov/23277173/) | Human clinical | **Qualifies** | Eosinophilia in AIG | Mean 34.5 eosinophils/HPF; p<0.001 vs. other gastritis | Human AIG, n=42 | HIGH |
| 17 | [PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/) | Model organism | **Competing** | Th2 drives eosinophilic AIG | Th2-dominant AIG with IgG1, IgE, eosinophils; IL-4/eosinophil KO rescue | DEREG mice | HIGH |
| 18 | [PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/) | Model organism | **Competing** | Th2 TCR → spontaneous AIG | A51 Th2 TCR transgenic: spontaneous AIG with eosinophils | TCR transgenic | MODERATE |

---

## Knowledge Gaps

{{figure:knowledge_gaps.png|caption=Summary of knowledge gaps and proposed discriminating tests for the Th17/IL-17 hypothesis in autoimmune gastritis.}}

### Gap 1: No Direct Test of IL-21 Blockade in AIG

**Scope:** The hypothesis that IL-21 is the pathogenic Th17 effector in AIG is inferred from IL-17RA KO phenotypes but has never been directly tested.  
**Why it matters:** If IL-21 is the true effector, therapeutic targeting shifts from IL-17 to IL-21 or IL-21R.  
**What was checked:** PubMed searches for "IL-21 autoimmune gastritis" and "IL-21 blockade gastritis" returned no primary interventional studies in AIG models.  
**Resolution:** Transfer Th17 cells from TxA23 mice into RAG⁻/⁻ recipients with concurrent anti-IL-21 or anti-IL-21R treatment; assess gastritis severity, parietal cell loss, and autoantibody titers.

### Gap 2: No Human Longitudinal Profiling of Th17 vs. Th1 vs. Th2 Over Disease Course

**Scope:** Whether the effector arm shifts from Th17 to Th1 (or vice versa) during AIG progression is unknown.  
**Why it matters:** If effector plasticity occurs, therapeutic timing is critical.  
**What was checked:** No longitudinal human studies with serial gastric biopsies and T cell subset profiling were identified.  
**Resolution:** Prospective cohort of potential AIG patients (APCA+, no atrophy) with serial biopsies and flow cytometry/scRNA-seq at 6–12 month intervals.

### Gap 3: No Human Anti-IL-17 Clinical Data in AIG

**Scope:** No trials or case series exist testing anti-IL-17 in AIG.  
**Why it matters:** The IL-17RA protective paradox suggests anti-IL-17 could worsen AIG.  
**What was checked:** PubMed and ClinicalTrials.gov searches returned no results.  
**Resolution:** Retrospective analysis of gastric histology/serology in patients receiving anti-IL-17 biologics for other indications; pharmacovigilance database query.

### Gap 4: Mechanism of Parietal Cell Death in Th17-Mediated AIG

**Scope:** IL-17RA-mediated apoptosis has been refuted. Fas/FasL, TNF/TNFR, perforin/granzyme are candidates but untested in the Th17 context.  
**Why it matters:** The causal chain from Th17 to tissue damage lacks a confirmed terminal mechanism.  
**What was checked:** Seed hypothesis cited IL-17RA apoptosis (refuted by PMID:38639570). Death pathways suggested but not confirmed ([PMID: 10963131](https://pubmed.ncbi.nlm.nih.gov/10963131/)).  
**Resolution:** Th17 transfer into recipients crossed with Fas^lpr^, TNF⁻/⁻, or perforin⁻/⁻ backgrounds.

### Gap 5: Th17-to-Th1 Plasticity in AIG Is Untested

**Scope:** Th17 cells convert to "ex-Th17" IFN-γ⁺ cells in other autoimmune settings ([PMID: 27183623](https://pubmed.ncbi.nlm.nih.gov/27183623/)), but this has not been examined in AIG.  
**Why it matters:** If ex-Th17 cells are the dominant pathogenic population, the "Th1 dominance" in older studies may partly reflect ex-Th17 cells.  
**Resolution:** Fate-mapping with IL-17A^Cre^ reporters in TxA23 AIG models; scRNA-seq trajectory analysis.

### Gap 6: No scRNA-seq Dataset Exists for Human AIG Immune Infiltrate

**Scope:** No published single-cell transcriptomic dataset specifically characterizes immune cells in human AIG gastric biopsies.  
**Why it matters:** Without unbiased profiling, the relative contribution of T helper subsets remains based on candidate approaches.  
**What was checked:** One proof-of-concept study ([PMID: 39837221](https://pubmed.ncbi.nlm.nih.gov/39837221/)) performed TCR-seq on erosive gastritis but did not include AIG.  
**Resolution:** scRNA-seq of paired corpus/antrum biopsies from AIG patients and matched controls.

### Gap 7: Whether Human AIG Eosinophilia Is Th17- or Th2-Driven

**Scope:** Eosinophilia is confirmed in human AIG (PMID:23277173) but can be driven by either Th17 (PMID:18641328) or Th2 (PMID:27259856) in murine models.  
**Why it matters:** Attribution to the correct effector arm determines therapeutic target.  
**Resolution:** Correlate eosinophil density with Th17 vs. Th2 cytokine profiles in the same human AIG biopsies.

### Gap 8: No GWAS Hits in IL-17 Pathway Genes for AIG/Pernicious Anemia

**Scope:** The pernicious anemia GWAS ([PMID: 34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/)) identified PTPN22 and HLA loci but not IL-17 pathway genes (IL17A, IL17F, IL17RA, RORC, IL23R).  
**Why it matters:** Absence of genetic association in the IL-17 pathway weakens the hypothesis at the genetic level.  
**What was checked:** Direct review of the GWAS results.

### Gap 9: Source-Level Absences

- No ClinGen/GenCC entries implicating Th17-pathway genes in AIG
- No clinical trials registered for anti-IL-17 in AIG (ClinicalTrials.gov)
- No scRNA-seq or bulk RNA-seq datasets (GEO/ArrayExpress) for AIG immune profiling
- No pharmacovigilance analyses of gastric outcomes in anti-IL-17-treated patients

---

## Alternative Models

### 1. Th1/IFN-γ-Dominant Effector Model (Competing/Parallel)

The classical framework for AIG. Multiple studies demonstrate H⁺/K⁺-ATPase-reactive Th1 cells in human gastric tissue ([PMID: 12645953](https://pubmed.ncbi.nlm.nih.gov/12645953/); [PMID: 15242679](https://pubmed.ncbi.nlm.nih.gov/15242679/)). Th1-mediated molecular mimicry between H. pylori and gastric autoantigens provides a compelling initiation mechanism. More extensively validated in human tissue than Th17. Likely a **parallel mechanism** that co-exists with Th17, with relative dominance varying by patient, stage, and trigger.

### 2. Th2/Eosinophil-Driven AIG (Competing)

Multiple independent murine models demonstrate Th2-driven AIG with eosinophilic pathology indistinguishable from Th17-driven eosinophilia ([PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/); [PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/); [PMID: 17671757](https://pubmed.ncbi.nlm.nih.gov/17671757/)). A genuine **competing hypothesis** for the eosinophilic component of human AIG. TCR clonotype may determine Th1 vs. Th2 vs. Th17 polarization ([PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/)).

### 3. Treg Deficiency/Dysfunction (Upstream Cause)

AIG reliably develops upon Treg depletion in multiple models. The Treg deficiency model is an **upstream permissive event** rather than a competing hypothesis. The specific effector arm escaping control is determined by secondary factors.

### 4. IL-21 as the True Pathogenic Th17 Effector (Mechanistic Refinement)

Given protective IL-17RA and paradoxical B cell expansion with IL-17RA loss, the pathogenic Th17 cytokine may be IL-21. This is a **refinement** preserving the Th17 contribution while redirecting the effector molecule. The most promising mechanistic revision but lacking direct experimental confirmation.

### 5. Antibody/Complement-Mediated Parietal Cell Destruction (Downstream/Complementary)

Anti-parietal cell and anti-intrinsic factor antibodies are central to AIG. B cell help from Th17 (via IL-21) and Th1 cells generates pathogenic autoantibodies. This is **downstream** and **complementary** to the Th17 hypothesis.

---

## Discriminating Tests

### Test 1: IL-21 Blockade vs. IL-17 Blockade in TxA23 Th17 Transfer

**Design:** Transfer Th17-polarized TxA23 cells into RAG⁻/⁻ recipients ± anti-IL-21R, anti-IL-17A, combination, or isotype control.  
**Readout:** Gastritis severity, parietal cell counts, B cell/plasma cell infiltration, serum autoantibody titers.  
**Expected result:** Anti-IL-21R reduces disease and autoantibodies; anti-IL-17A worsens or has no effect.  
**Rationale:** The single most discriminating experiment for the IL-21 re-framing.

### Test 2: Retrospective Gastric Surveillance in Anti-IL-17 Recipients

**Design:** Chart review of psoriasis/AS patients on secukinumab/ixekizumab ≥12 months.  
**Biomarkers:** Pepsinogen I/II ratio, gastrin-17, anti-parietal cell antibodies.  
**Expected result if IL-17 is protective:** Increased incidence of gastric atrophy markers.

### Test 3: scRNA-seq of Human AIG Gastric Biopsies Across Disease Stages

**Design:** Paired corpus biopsies from early (APCA+, no atrophy), established (partial atrophy), and advanced (complete atrophy/pernicious anemia) patients.  
**Analysis:** Unsupervised clustering of CD4⁺ T cells; quantify Th1/Th2/Th17/Treg/ex-Th17 proportions; TCR clonality; IL-21 vs. IL-17A expression.  
**Resolves:** Gaps 2, 5, 6, and 7 simultaneously.

### Test 4: Fate-Mapping Th17 Cells in TxA23 AIG

**Design:** Cross IL-17A^Cre^-ROSA26^tdTomato^ mice with TxA23 model.  
**Readout:** Proportion of gastric IFN-γ⁺ cells that are fate-mapped ex-Th17.  
**Resolves:** Whether Th17 plasticity reconciles the Th1/Th17 paradigms.

### Test 5: STAT3 Inhibitor Feasibility Study

**Design:** Pilot study of oral STAT3 inhibitors in AIG with active inflammation.  
**Stratification:** Early vs. established disease.  
**Biomarkers:** Gastric Th17/Treg ratio, serum IL-17A, IL-21, anti-PCA titers.  
**Rationale:** Most mechanistically justified therapeutic target given murine proof-of-concept ([PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/)).

---

## Curation Leads

*The following are candidate KB updates requiring curator verification.*

### Candidate Evidence References to Add

| Reference | Snippet (verbatim) | Proposed Relation | Source Type |
|-----------|--------------------|--------------------|-------------|
| [PMID: 40471463](https://pubmed.ncbi.nlm.nih.gov/40471463/) | "STAT3 and p-STAT3 were significantly upregulated in TxA23 AIG mice, correlating with inflammation, atrophy, and mucus hyperplasia" | SUPPORT | Model organism |
| [PMID: 38639570](https://pubmed.ncbi.nlm.nih.gov/38639570/) | "Il17raΔGI-Epi mice develop increased inflammation compared with controls" | REFUTE (IL-17RA apoptosis claim) | Model organism |
| [PMID: 19812196](https://pubmed.ncbi.nlm.nih.gov/19812196/) | "A striking feature was a marked increase in gastric B cells, plasma cells, and lymphoid follicles" | QUALIFY | Model organism |
| [PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/) | "AIG in DEREG mice is associated with strong Th2 cell responses, including dominant IgG1 autoantibodies, elevated serum IgE" | COMPETING | Model organism |
| [PMID: 12645953](https://pubmed.ncbi.nlm.nih.gov/12645953/) | "Gastric T cell recognition of the peptide epitopes resulted in secretion of Th1 cytokines" | COMPETING | Human clinical |
| [PMID: 23277173](https://pubmed.ncbi.nlm.nih.gov/23277173/) | "eosinophil infiltration [mean 34.5/high power field (HPF), >30 eosinophils/HPF in 46.1%]" | SUPPORT (partial) | Human clinical |

### Candidate Hypothesis Description Revision

**Current problematic text:** "...which effector arm dominates human disease, and whether it shifts over the disease course, is unresolved and carries therapeutic implications (e.g., anti-IL-17 blockade)."

**Proposed revision:** "...which effector arm dominates human disease, and whether it shifts over the disease course, is unresolved. IL-17RA signaling on gastric epithelium is protective (not cytotoxic), and IL-17RA loss increases autoantibody-relevant B cell pathology, suggesting the pathogenic Th17 effector may be IL-21 rather than IL-17A/F. Anti-IL-17 blockade is not supported by current evidence and may be harmful; STAT3 inhibition is the more justified therapeutic target."

### Candidate Pathophysiology Edges

- **ADD:** STAT3 → Th17/Treg imbalance → AIG (PMID:40471463)
- **ADD:** IL-17A/F → IL-17RA → Epithelial barrier protection (PMID:38639570, 38014948)
- **ADD:** Th17 → IL-21 → B cell differentiation → Autoantibodies (inferred from PMID:19812196)
- **ADD:** IL-17RA signaling → Negative regulation of B cell recruitment (PMID:19812196)
- **REMOVE:** IL-17A/F → IL-17RA → Parietal cell apoptosis (refuted by PMID:38639570)

### Candidate Ontology Terms

- **Cell types:** Th17 cell (CL:0000899), Th1 cell (CL:0000545), Th2 cell (CL:0000546), gastric parietal cell (CL:0000163), regulatory T cell (CL:0000815)
- **Biological processes:** T-helper 17 cell differentiation (GO:0072539), interleukin-17 production (GO:0032620), interleukin-21 production (GO:0032623)
- **Disease:** Autoimmune gastritis (MONDO:0010156), Pernicious anemia (MONDO:0001061)

### Candidate Status Change

**Recommendation:** Retain EMERGING. Upgrade to ESTABLISHED requires: (1) direct IL-21 blockade data in AIG; (2) human scRNA-seq defining Th17 prevalence across disease stages; (3) resolution of Th1 vs. Th17 dominance question.

### Candidate Knowledge Gaps for KB Entry

1. IL-21 as pathogenic Th17 effector — no direct perturbation data
2. Th17-to-Th1 plasticity in AIG — untested
3. Human AIG scRNA-seq — no dataset exists
4. Anti-IL-17 safety in gastric autoimmunity — no human data
5. Mechanism of parietal cell death in Th17 context — unresolved
6. Whether eosinophilia in human AIG is Th17- or Th2-driven — unresolved

### Discussion Prompts for Curators

1. Should the hypothesis description explicitly note that anti-IL-17 blockade is contraindicated based on current evidence?
2. Should a separate hypothesis node be created for "IL-21-mediated B cell activation in AIG" as a refinement of the Th17 hypothesis?
3. Should the Th2/eosinophil pathway be represented as a competing hypothesis or as a co-pathogenic mechanism?
4. Is the IL-17RA protective finding (from H. pylori models) sufficiently generalizable to sterile autoimmune gastritis to justify modifying the hypothesis?

---

*Report generated 2026-07-01 | 81 papers reviewed | 11 confirmed findings | 5 iterations of autonomous investigation*
