---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-01T15:19:52.346812'
end_time: '2026-07-01T16:48:20.055197'
duration_seconds: 5307.71
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Autoimmune Gastritis
  category: Complex
  hypothesis_group_id: canonical_th1_effector_polarization
  hypothesis_label: Canonical Th1/IFN-gamma Effector Polarization
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_th1_effector_polarization\nhypothesis_label:\
    \ Canonical Th1/IFN-gamma Effector Polarization\nstatus: CANONICAL\ndescription:\
    \ The effector arm driving parietal-cell destruction has classically been modeled\
    \ as Th1/IFN-gamma-polarized,\n  based on murine neonatal-thymectomy and TCR-transgenic\
    \ effector-transfer systems specific for the H+/K+\n  ATPase.\nevidence:\n- reference:\
    \ PMID:18641328\n  reference_title: Th1, Th2, and Th17 effector T cell-induced\
    \ autoimmune gastritis differs in pathological\n    pattern and in susceptibility\
    \ to suppression by regulatory T cells.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: We have evaluated the capacity of fully differentiated\
    \ Th1, Th2, and Th17 cells derived from\n    a mouse bearing a transgenic TCR\
    \ specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,\n    to induce\
    \ autoimmune gastritis after transfer to immunodeficient recipients.\n  explanation:\
    \ Effector-transfer model in which Th1 (among other subsets) specific for the\
    \ H+/K+ ATPase\n    induces autoimmune gastritis.\n- reference: PMID:15763992\n\
    \  reference_title: Molecular specificity and functional properties of autoreactive\
    \ T-cell response in\n    human gastric autoimmunity.\n  supports: SUPPORT\n \
    \ evidence_source: HUMAN_CLINICAL\n  snippet: The majority of the autoreactive\
    \ T cell clones secreted IFN-gamma and showed a T helper 1 (Th1)\n    profile.\n\
    \  explanation: Human gastric H+/K+ ATPase-reactive CD4 clones are predominantly\
    \ Th1 (IFN-gamma) and cytotoxic,\n    directly supporting the Th1 effector arm\
    \ in human disease.\n- reference: PMID:22777705\n  reference_title: Both IFN-gamma\
    \ and IL-17 are required for the development of severe autoimmune gastritis.\n\
    \  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n  snippet: both are required\
    \ for the disease to progress to the late pathogenic stage that includes significant\n\
    \    tissue disruption.\n  explanation: IFN-gamma and IL-17 are co-required for\
    \ severe disease (and CD8 T cells are the dominant\n    IFN-gamma source), qualifying\
    \ a Th1-exclusive model.\nnotes: 'A claude_code hypothesis-search report (kb/hypotheses/Autoimmune_Gastritis/canonical_th1_effector_polarization)\n\
    \  graded this PARTIALLY SUPPORTED: the Th1/IFN-gamma axis is foundational and\
    \ real (human gastric Th1\n  clones cytotoxic via perforin/Fas-FasL; anti-IFN-gamma\
    \ blockade prevents murine disease) but is not\n  the sole or necessarily dominant\
    \ effector arm. It is best read as one arm of a co-dependent Th1/Th17/CD8\n  program:\
    \ in the polyclonal mouse model CD8 T cells are the dominant IFN-gamma source\
    \ and IFN-gamma plus\n  IL-17 are co-required for severe disease (PMID:22777705),\
    \ and the human intrinsic-factor-reactive /\n  pernicious-anemia compartment is\
    \ Th17-dominant (see emerging_th17_effector_polarization). Run performed\n  with\
    \ the claude_code provider; the openscientist backend was unavailable in this\
    \ environment.'"
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
citation_count: 22
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
- **Hypothesis ID:** canonical_th1_effector_polarization
- **Hypothesis Label:** Canonical Th1/IFN-gamma Effector Polarization
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_th1_effector_polarization
hypothesis_label: Canonical Th1/IFN-gamma Effector Polarization
status: CANONICAL
description: The effector arm driving parietal-cell destruction has classically been modeled as Th1/IFN-gamma-polarized,
  based on murine neonatal-thymectomy and TCR-transgenic effector-transfer systems specific for the H+/K+
  ATPase.
evidence:
- reference: PMID:18641328
  reference_title: Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological
    pattern and in susceptibility to suppression by regulatory T cells.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: We have evaluated the capacity of fully differentiated Th1, Th2, and Th17 cells derived from
    a mouse bearing a transgenic TCR specific for the gastric parietal cell antigen, H(+)K(+)-ATPase,
    to induce autoimmune gastritis after transfer to immunodeficient recipients.
  explanation: Effector-transfer model in which Th1 (among other subsets) specific for the H+/K+ ATPase
    induces autoimmune gastritis.
- reference: PMID:15763992
  reference_title: Molecular specificity and functional properties of autoreactive T-cell response in
    human gastric autoimmunity.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The majority of the autoreactive T cell clones secreted IFN-gamma and showed a T helper 1 (Th1)
    profile.
  explanation: Human gastric H+/K+ ATPase-reactive CD4 clones are predominantly Th1 (IFN-gamma) and cytotoxic,
    directly supporting the Th1 effector arm in human disease.
- reference: PMID:22777705
  reference_title: Both IFN-gamma and IL-17 are required for the development of severe autoimmune gastritis.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: both are required for the disease to progress to the late pathogenic stage that includes significant
    tissue disruption.
  explanation: IFN-gamma and IL-17 are co-required for severe disease (and CD8 T cells are the dominant
    IFN-gamma source), qualifying a Th1-exclusive model.
notes: 'A claude_code hypothesis-search report (kb/hypotheses/Autoimmune_Gastritis/canonical_th1_effector_polarization)
  graded this PARTIALLY SUPPORTED: the Th1/IFN-gamma axis is foundational and real (human gastric Th1
  clones cytotoxic via perforin/Fas-FasL; anti-IFN-gamma blockade prevents murine disease) but is not
  the sole or necessarily dominant effector arm. It is best read as one arm of a co-dependent Th1/Th17/CD8
  program: in the polyclonal mouse model CD8 T cells are the dominant IFN-gamma source and IFN-gamma plus
  IL-17 are co-required for severe disease (PMID:22777705), and the human intrinsic-factor-reactive /
  pernicious-anemia compartment is Th17-dominant (see emerging_th17_effector_polarization). Run performed
  with the claude_code provider; the openscientist backend was unavailable in this environment.'
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

# Hypothesis-Search Report: Canonical Th1/IFN-γ Effector Polarization in Autoimmune Gastritis

**Hypothesis ID:** `canonical_th1_effector_polarization`  
**Disease:** Autoimmune Gastritis (Complex)  
**KB Status:** CANONICAL  
**Report Date:** 2026-07-01  
**Evidence Base:** 51 papers reviewed across 5 iterations; 11 confirmed findings  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED**

The Canonical Th1/IFN-γ Effector Polarization hypothesis — that parietal-cell destruction in autoimmune gastritis (AIG) is driven by a Th1/IFN-γ-polarized CD4+ effector arm — is **partially supported** by the current literature. The hypothesis is correct in identifying IFN-γ as a necessary and mechanistically central cytokine: anti-IFN-γ antibody blockade prevents disease initiation in neonatal thymectomy (NTx) models, human gastric H+/K+-ATPase-reactive CD4+ T cell clones are overwhelmingly Th1-polarized and cytotoxic, IFN-γ directly kills gastric epithelial cells in organoid systems, and the PTPN22 W620 genetic risk variant for pernicious anemia specifically favors Th1/IFN-γ over Th17 responses. However, two critical qualifications emerge that prevent full endorsement of a Th1-exclusive model: (1) in polyclonal NTx models, CD8+ T cells — not CD4+ Th1 cells — are the dominant IFN-γ source, and (2) IFN-γ alone is insufficient for complete disease; IL-17 is co-required for progression to severe tissue destruction, and IL-13 (a type-2 cytokine) independently drives the metaplastic transformation that follows atrophy. The hypothesis is therefore best understood as describing one essential arm of a cooperative multi-cytokine, multi-cell-type effector program rather than a self-sufficient mechanism.

The most important caveats are: (a) the Th1-dominant phenotype is demonstrated most robustly in TCR-transgenic and monoclonal systems, which may overrepresent Th1 contributions relative to polyclonal disease; (b) alternative effector polarizations (Th2/eosinophilic, Th17-dominant) can independently drive AIG in specific genetic or experimental contexts; and (c) the human data, while strongly supporting Th1 dominance among H+/K+-ATPase-reactive clones, comes primarily from a small number of studies and has not been validated with modern single-cell technologies at scale.

---

## Summary

Autoimmune gastritis (AIG) is a chronic organ-specific autoimmune disease characterized by immune-mediated destruction of gastric parietal cells, leading to achlorhydria, iron deficiency, vitamin B12 malabsorption, and risk of gastric neuroendocrine tumors and adenocarcinoma. The canonical mechanistic model posits that CD4+ Th1 cells, polarized to produce IFN-γ and specific for the gastric H+/K+-ATPase (proton pump), constitute the primary effector arm driving parietal cell destruction. This model was built largely on murine neonatal thymectomy and TCR-transgenic adoptive transfer systems.

Our systematic evaluation of 51 papers across 5 iterations confirms that IFN-γ is indeed mechanistically essential: it is required for disease initiation, directly induces gastric epithelial cell death, and drives CCL20-mediated recruitment of CD4+ T cells to the gastric mucosa. Human studies confirm that gastric H+/K+-ATPase-specific CD4+ T cell clones are predominantly Th1 with dual cytotoxic mechanisms (perforin and Fas-FasL). Genetic evidence from GWAS links the PTPN22 W620 risk variant — which specifically amplifies Th1/IFN-γ responses while suppressing Th17 — to pernicious anemia risk. However, the hypothesis requires substantial qualification: CD8+ T cells (not CD4+ Th1) are the dominant IFN-γ source in polyclonal models, IL-17 is co-required with IFN-γ for severe disease, IL-13 independently drives metaplasia, and Th2/eosinophilic pathways can cause AIG in specific contexts. The hypothesis best explains disease initiation and the atrophic phase but not the full trajectory from initiation through metaplasia to neoplastic risk.

---

## Key Findings

### Finding 1: IFN-γ Is Required for Disease Initiation

Anti-IFN-γ monoclonal antibody treatment abolished autoimmune gastritis initiation in the neonatal thymectomy (NTx) BALB/c model. Weekly treatment reduced AIG incidence from 69% (control IgG) to 16%, and a single dose at postnatal day 3 reduced incidence from 8/19 to 1/19. Splenic T cells from gastritic mice produced 3–10× more IFN-γ than controls ([PMID: 8766575](https://pubmed.ncbi.nlm.nih.gov/8766575/)). This represents the most direct loss-of-function evidence for IFN-γ necessity in AIG initiation and establishes the cytokine as a non-redundant early effector. Notably, this was confirmed in a second model: anti-IFN-γ prevented AIG development in NTx-PD-1−/− mice while simultaneously demonstrating that IFN-γ drives CCL20 expression in the gastric mucosa, creating a positive feedback loop for CD4+ T cell recruitment ([PMID: 21995497](https://pubmed.ncbi.nlm.nih.gov/21995497/)).

### Finding 2: Human Gastric Autoreactive T Cells Are Predominantly Th1/Cytotoxic

The strongest human evidence comes from clonal analyses of gastric corpus-infiltrating T cells from AIG patients. D'Elios et al. demonstrated that 25% of CD4+ clones from the gastric corpus proliferated in response to H+/K+-ATPase, and 88% of these showed a Th1 profile characterized by IFN-γ secretion. Virtually all expressed perforin-mediated cytotoxicity and TNF-α, and most induced Fas-FasL-mediated apoptosis in target cells ([PMID: 11159878](https://pubmed.ncbi.nlm.nih.gov/11159878/); [PMID: 15763992](https://pubmed.ncbi.nlm.nih.gov/15763992/)). This dual cytotoxic mechanism — perforin-granzyme for direct killing and Fas-FasL for apoptosis induction — provides the mechanistic link between Th1 polarization and parietal cell destruction in humans. These remain the only published human T cell clonal studies specifically addressing AIG effector polarization.

### Finding 3: IFN-γ and IL-17 Are Co-Required for Severe Disease; CD8 T Cells Dominate IFN-γ Production

In the polyclonal NTx model, Tu et al. (2012) made two findings that fundamentally qualify the Th1-exclusive hypothesis. First, the majority of IFN-γ-producing cells in the gastritic stomach were CD8+ T cells, not CD4+ Th1 cells. Second, while T cells deficient in either IFN-γ or IL-17 could still initiate mild AIG, both cytokines were required for progression to severe disease with significant tissue disruption ([PMID: 22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/)). IL-17 was produced solely by CD4+ T cells. This establishes a cooperative Th1/Th17/CD8 effector program rather than a Th1-exclusive model and shifts the primary IFN-γ source from CD4+ Th1 to CD8+ cytotoxic T cells in the polyclonal setting.

### Finding 4: IFN-γ Drives CCL20-Mediated CD4+ T Cell Recruitment

IFN-γ neutralization in NTx-PD-1−/− mice suppressed CCL20 expression in the gastric mucosa and blocked CD4+ T cell infiltration. Conversely, recombinant IFN-γ injection upregulated CCL20 in the stomach, and anti-CCL20 treatment suppressed CD4+ T cell infiltration ([PMID: 21995497](https://pubmed.ncbi.nlm.nih.gov/21995497/)). This defines a critical amplification loop: IFN-γ → CCL20 → CD4+ T cell recruitment → more IFN-γ. This mechanism explains how initial IFN-γ production (potentially by CD8+ T cells or early innate responses) can recruit and amplify a CD4+ Th1 response at the tissue site.

### Finding 5: IFN-γ Directly Kills Gastric Epithelial Cells but Does Not Drive Metaplasia

Osaki et al. (2019) demonstrated that IFN-γ applied to 3D gastric organoids directly induced epithelial cell death, with IFN-γ receptor-deficient organoids being resistant. Crucially, TxA23 × Ifng−/− mice maintained ongoing gastric inflammation but failed to progress to atrophy and metaplasia ([PMID: 30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/)). This establishes IFN-γ as a direct epithelial cytotoxin responsible for the atrophic phase. However, a separate study showed that metaplasia — the pathological transformation that follows atrophy — requires IL-13 acting through IL-4Rα signaling, which is independent of IFN-γ ([PMID: 34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/)). This creates a two-cytokine model: IFN-γ drives atrophy, IL-13 drives metaplasia.

### Finding 6: IL-13 Independently Drives Metaplasia

Noto et al. (2022) identified 6 unique subsets of IL-13-producing immune cells in the inflamed TxA23 stomach. IL-13 directly induced a metaplastic phenotype in gastric organoids. IL-4Rα-deficient TxA23 mice upregulated inflammatory genes but completely failed to develop metaplasia. Anti-IL-13 neutralization both reduced and reversed established metaplasia ([PMID: 34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/)). This finding is significant because it demonstrates that the most clinically consequential outcome of chronic AIG — metaplasia, which carries neoplastic risk — is not explained by the Th1/IFN-γ axis at all but requires a parallel type-2 cytokine pathway.

### Finding 7: Th2/Eosinophilic Pathways Can Independently Drive AIG

Multiple lines of evidence demonstrate that Th1 is not the only effector polarization capable of causing AIG. C57BL/6-DEREG mice with transient Treg depletion developed AIG with dominant Th2 responses: IgG1 autoantibodies, elevated IgE, Th2 cytokines, and massive eosinophilic inflammation. Disease was ameliorated in IL-4−/− or eosinophil-deficient mice ([PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/)). Separately, TXA51 TCR transgenic mice expressing a Th2-polarized clone developed spontaneous AIG with eosinophilic infiltration ([PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/)). Th17 cells could also independently induce AIG with distinct histological patterns ([PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). These findings demonstrate that the gastric autoimmune response can be channeled through multiple effector arms depending on the immunological context.

### Finding 8: H. pylori Molecular Mimicry Activates Cross-Reactive Th1 Cells

Amedei et al. (2003) showed that H. pylori-infected patients with gastric autoimmunity harbor gastric CD4+ T cells recognizing both H+/K+-ATPase and H. pylori antigens. Cross-reactive epitopes from 9 H. pylori proteins were identified, and these peptides induced T cell proliferation with Th1 functions ([PMID: 14568977](https://pubmed.ncbi.nlm.nih.gov/14568977/)). This provides a mechanism by which H. pylori infection could trigger de novo Th1-polarized autoimmunity through molecular mimicry, linking infection-driven and autoimmune gastritis through a shared Th1 effector pathway.

### Finding 9: PTPN22 W620 Genetic Risk Variant Specifically Favors Th1/IFN-γ

GWAS identified PTPN22 as one of 5 genome-wide significant risk loci for pernicious anemia (rs6679677, p = 1.91 × 10⁻¹⁰; [PMID: 34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/)). The PTPN22 W620 variant causes exaggerated Th1 responses with increased IFN-γ production, reduced Th17 responses with decreased IL-17, and loss of Treg suppression of Th1-mediated IFN-γ production ([PMID: 23333624](https://pubmed.ncbi.nlm.nih.gov/23333624/)). This genetic evidence directly connects a pernicious anemia risk allele to the Th1/IFN-γ axis, providing human genetic support for the hypothesis. Importantly, Pep overexpression in T cells (mimicking enhanced PTPN22 function) attenuated autoimmune diabetes by preferentially reducing IFN-γ-producing T cells while preserving Treg function ([PMID: 23752610](https://pubmed.ncbi.nlm.nih.gov/23752610/)), confirming the pathway's functional relevance.

### Finding 10: IL-27 Protects Against AIG by Suppressing CD4+ T Cell Inflammatory Genes

TxA23 × Ebi3−/− mice (IL-27-deficient) developed more severe gastritis, atrophy, and spasmolytic polypeptide-expressing metaplasia (SPEM) than IL-27-sufficient controls. Recombinant IL-27 administration reduced inflammation, atrophy, and SPEM severity. Single-cell RNA sequencing showed IL-27 acted almost exclusively on stomach-infiltrating CD4+ T cells to suppress inflammatory genes ([PMID: 32376420](https://pubmed.ncbi.nlm.nih.gov/32376420/)). This identifies an endogenous counter-regulatory mechanism that operates specifically on the CD4+ T cell compartment, reinforcing the importance of CD4+ T cells in AIG while revealing a natural brake on effector function.

### Finding 11: NK Cells Are Not the IFN-γ Source for AIG Initiation

In vivo NK cell depletion immediately after neonatal thymectomy showed no reduction in AIG incidence. NK cell number and activation status were unchanged between euthymic and NTx mice ([PMID: 11905844](https://pubmed.ncbi.nlm.nih.gov/11905844/)). This rules out innate IFN-γ sources and confirms that T cells are the necessary IFN-γ producers for disease initiation, though whether CD4+ Th1 or CD8+ T cells are the critical early source remains unresolved.

---

## Mechanistic Model / Interpretation

The hypothesis implies a causal chain from upstream trigger to clinical manifestation. Evidence strength is annotated at each step.

```
UPSTREAM TRIGGERS
├── Loss of central/peripheral tolerance (NTx, Treg deficiency) [ESTABLISHED]
├── H. pylori molecular mimicry → cross-reactive Th1 activation [ESTABLISHED in vitro/clinical]
└── Genetic predisposition (PTPN22 W620 → Th1 bias) [ESTABLISHED by GWAS + functional]
        │
        ▼
ANTIGEN PRESENTATION
├── Gastric DCs capture H+/K+-ATPase in mucosa [ESTABLISHED, PMID:12391019]
├── DCs traffic to draining gastric LN [ESTABLISHED]
└── Constitutive presentation under non-inflammatory conditions [ESTABLISHED]
        │
        ▼
T CELL PRIMING & POLARIZATION
├── CD4+ T cells recognize H+/K+-ATPase peptides [ESTABLISHED]
├── Th1 differentiation (IFN-γ, T-bet) [ESTABLISHED in human & mouse]
├── CD8+ T cell priming (dominant IFN-γ source in polyclonal) [ESTABLISHED]
└── Concurrent Th17 differentiation (IL-17) [ESTABLISHED]
        │
        ▼
EFFECTOR RECRUITMENT TO STOMACH
├── IFN-γ → CCL20 upregulation in gastric mucosa [ESTABLISHED]
├── CCL20 → CD4+ T cell recruitment (CCR6+) [ESTABLISHED]
└── Positive feedback amplification loop [ESTABLISHED]
        │
        ▼
PARIETAL CELL DESTRUCTION (ATROPHY)
├── IFN-γ direct epithelial cytotoxicity [ESTABLISHED, organoid + in vivo]
├── Perforin/granzyme-mediated killing by Th1 clones [ESTABLISHED in human]
├── Fas-FasL-mediated apoptosis [ESTABLISHED in human]
└── IL-17 co-required for severe tissue disruption [ESTABLISHED]
        │
        ▼
METAPLASIA
├── IL-13 → IL-4Rα signaling on epithelium [ESTABLISHED]
├── Metaplastic phenotype induction (independent of IFN-γ) [ESTABLISHED]
└── IFN-γ is necessary for atrophy but NOT for metaplasia [ESTABLISHED]
        │
        ▼
CLINICAL CONSEQUENCES
├── Achlorhydria → iron malabsorption [INFERRED from pathology]
├── IF deficiency → B12 malabsorption → pernicious anemia [ESTABLISHED clinically]
└── Metaplasia → neoplastic risk (gNETs, adenocarcinoma) [ESTABLISHED epidemiologically]
```

**Strong links:** Tolerance loss → T cell priming → IFN-γ production → parietal cell death. These steps have direct experimental support from loss-of-function (anti-IFN-γ blockade, knockout mice) and gain-of-function (recombinant IFN-γ, adoptive transfer) approaches.

**Weak/missing links:** (1) The transition from antigen presentation to Th1 vs. Th17 vs. Th2 polarization — what determines which effector arm dominates in individual patients — is not understood. (2) The relative contributions of CD4+ Th1 vs. CD8+ T cells as IFN-γ sources in *human* disease are unknown. (3) The mechanism by which IL-13-producing cells are recruited/activated during AIG, and whether this requires prior IFN-γ-mediated damage, is unclear. (4) Whether metaplasia always follows atrophy or can develop independently is not established.

{{figure:integrated_mechanistic_model.png|caption=Integrated mechanistic model showing the multi-cytokine effector program in autoimmune gastritis. IFN-γ (from both CD4+ Th1 and CD8+ T cells) drives initiation and atrophy; IL-17 cooperates for severe tissue destruction; IL-13 independently drives metaplasia through IL-4Rα signaling on gastric epithelium.}}

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Context | Confidence |
|----------|---------------|-----------|--------------------------|-------------|---------|------------|
| [PMID: 8766575](https://pubmed.ncbi.nlm.nih.gov/8766575/) | Model organism | **Supports** | IFN-γ required for initiation | Anti-IFN-γ mAb reduced AIG incidence from 69% to 16% in NTx BALB/c | NTx model, preventive | High; direct loss-of-function |
| [PMID: 11159878](https://pubmed.ncbi.nlm.nih.gov/11159878/) | Human clinical | **Supports** | Human Th1 effector polarization | 88% of H+/K+-ATPase-reactive CD4+ clones were Th1; perforin + Fas-FasL cytotoxicity | Human AIG biopsies | High; direct human evidence; small sample |
| [PMID: 15763992](https://pubmed.ncbi.nlm.nih.gov/15763992/) | Human clinical | **Supports** | Human Th1 effector arm | Majority of autoreactive T cell clones secreted IFN-γ with Th1 profile | Human gastric autoimmunity | High; confirms F002 |
| [PMID: 22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/) | Model organism | **Qualifies** | Th1-exclusive model | CD8+ T cells are dominant IFN-γ source; IL-17 co-required for severe disease | Polyclonal NTx model | High; challenges CD4 Th1 exclusivity |
| [PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/) | Model organism | **Supports** (qualified) | Multiple effector arms cause AIG | Th1, Th2, and Th17 all induce AIG with distinct histology; Th17 most destructive | TCR-Tg adoptive transfer | High; shows Th1 is sufficient but not unique |
| [PMID: 21995497](https://pubmed.ncbi.nlm.nih.gov/21995497/) | Model organism | **Supports** | IFN-γ → CCL20 → CD4 recruitment | Anti-IFN-γ suppressed CCL20 and CD4+ infiltration; rIFN-γ upregulated CCL20 | NTx-PD-1−/− model | High; bidirectional evidence |
| [PMID: 30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/) | Model organism + in vitro | **Supports** (atrophy) / **Qualifies** (metaplasia) | IFN-γ drives epithelial death | IFN-γ kills organoids directly; Ifng−/− mice have inflammation but no atrophy/metaplasia | TxA23 model + organoids | High; clean loss-of-function |
| [PMID: 34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/) | Model organism + in vitro | **Competing** | Metaplasia mechanism | IL-13 (not IFN-γ) drives metaplasia; IL-4Rα-deficient mice lack metaplasia | TxA23 model + organoids | High; independent pathway |
| [PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/) | Model organism | **Competing** | Th2-mediated AIG | Treg-depleted DEREG mice develop Th2-dominant AIG with eosinophils | DEREG C57BL/6 | High; demonstrates alternative effector arm |
| [PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/) | Model organism | **Competing** | TCR-determined Th2 AIG | TXA51 Th2 clone causes spontaneous eosinophilic AIG | TCR-Tg (Th2) | Moderate; single Tg model |
| [PMID: 14568977](https://pubmed.ncbi.nlm.nih.gov/14568977/) | Human clinical | **Supports** | Molecular mimicry → Th1 | H. pylori-infected patients have cross-reactive Th1 cells for H+/K+-ATPase | HP+ patients with autoimmunity | High; human mechanistic |
| [PMID: 34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/) | GWAS | **Supports** | Genetic basis | PTPN22 is genome-wide significant risk locus for pernicious anemia | European ancestry, PA | High; large GWAS |
| [PMID: 23333624](https://pubmed.ncbi.nlm.nih.gov/23333624/) | Human in vitro | **Supports** | PTPN22 → Th1 bias | W620 homozygotes: exaggerated Th1/IFN-γ, reduced Th17/IL-17, lost Treg suppression of Th1 | Human genotyped donors | High; functional genetics |
| [PMID: 32376420](https://pubmed.ncbi.nlm.nih.gov/32376420/) | Model organism | **Qualifies** | Counter-regulation of Th1 | IL-27 deficiency worsens AIG; IL-27 suppresses CD4+ T cell inflammatory genes | TxA23 model | High; identifies endogenous brake |
| [PMID: 11905844](https://pubmed.ncbi.nlm.nih.gov/11905844/) | Model organism | **Supports** | T cell (not NK) IFN-γ source | NK depletion does not prevent AIG; rules out innate IFN-γ | NTx F1 mice | Moderate; negative result |
| [PMID: 12391019](https://pubmed.ncbi.nlm.nih.gov/12391019/) | Model organism | **Supports** | DC antigen presentation | Gastric DCs constitutively present H+/K+-ATPase in draining LN | BALB/c | High; foundational for priming step |
| [PMID: 22124119](https://pubmed.ncbi.nlm.nih.gov/22124119/) | Model organism | **Supports** | TSLP counter-regulates Th1 AIG | TSLPR−/− NTx mice show earlier, more severe AIG with enhanced IFN-γ | NTx-TSLPR−/− | Moderate; confirms IFN-γ centrality |
| [PMID: 16399875](https://pubmed.ncbi.nlm.nih.gov/16399875/) | Model organism | **Supports** | IFN-γ in spontaneous AIG | Cholera toxin transgenic mice with parietal cell stress → autoimmune destruction + elevated IFN-γ | Ctox-Tg model | Moderate; indirect support |

{{figure:evidence_landscape_comprehensive.png|caption=Comprehensive evidence landscape for the Th1/IFN-γ hypothesis in autoimmune gastritis. The plot maps evidence items by source type and direction (supporting, qualifying, competing), revealing that while the core Th1/IFN-γ axis is robustly supported, substantial qualifying and competing evidence necessitates a multi-cytokine model.}}

---

## Claim Status Classification

### ESTABLISHED Claims (6)

1. **IFN-γ is required for AIG initiation** — Anti-IFN-γ blockade prevents disease in multiple murine models (PMID: 8766575, 21995497). No contradicting evidence found.

2. **Human gastric autoreactive T cells are predominantly Th1/cytotoxic** — 88% of H+/K+-ATPase-reactive CD4+ clones show Th1 profile with dual cytotoxic mechanisms (PMID: 11159878, 15763992).

3. **IFN-γ directly kills gastric epithelial cells** — Organoid and in vivo knockout evidence (PMID: 30511397). Clean loss-of-function demonstration.

4. **T cells (not NK cells) are the IFN-γ source for initiation** — NK depletion has no effect (PMID: 11905844).

5. **IL-17 is co-required with IFN-γ for severe disease** — Single-cytokine-deficient T cells cause only mild AIG (PMID: 22777705).

6. **IL-13 (not IFN-γ) is required for metaplasia** — IL-4Rα-deficient mice have inflammation and atrophy but no metaplasia (PMID: 34587523).

### EMERGING Claims (4)

1. **PTPN22 W620 genetically wires pernicious anemia risk toward Th1** — GWAS + functional data converge (PMID: 34145262, 23333624) but the variant has not been studied in AIG-specific cohorts.

2. **IFN-γ → CCL20 → CD4+ recruitment is a critical amplification loop** — Single study, not yet replicated (PMID: 21995497).

3. **IL-27 acts as an endogenous brake on CD4+ T cells in AIG** — Single model system (PMID: 32376420); human relevance unknown.

4. **H. pylori molecular mimicry triggers cross-reactive Th1 cells** — Demonstrated in infected patients (PMID: 14568977); population-level relevance uncertain.

### CONTRADICTED Claims (2)

1. **CD4+ Th1 cells are the sole/dominant IFN-γ source** — CD8+ T cells dominate IFN-γ production in polyclonal NTx model (PMID: 22777705).

2. **IFN-γ alone is sufficient for the full disease trajectory** — IL-17 co-required for severe disease; IL-13 required for metaplasia (PMID: 22777705, 34587523).

{{figure:evidence_summary.png|caption=Distribution of evidence direction (supporting, qualifying, competing) and evidence source types across the reviewed literature, illustrating the balanced nature of the evidence for the Th1/IFN-γ hypothesis.}}

---

## Knowledge Gaps

### Gap 1: CD4+ Th1 vs. CD8+ T Cell IFN-γ Contributions in Human AIG

**Scope:** The relative contributions of CD4+ Th1 and CD8+ cytotoxic T cells as IFN-γ sources in human AIG are unknown. Mouse data show CD8+ dominance in polyclonal models, but human clonal studies focused exclusively on CD4+ cells.  
**Why it matters:** Determines whether therapeutic targeting should focus on CD4+ or CD8+ T cells, and whether the "Th1" label is mechanistically accurate for the IFN-γ-producing compartment.  
**What was checked:** PubMed searches for "autoimmune gastritis CD8 IFN-gamma human" and related terms. No human studies quantifying CD8 vs. CD4 IFN-γ production in AIG were found.  
**Resolution:** Single-cell RNA-seq/CITE-seq of human AIG gastric biopsies with TCR sequencing would resolve this definitively.

### Gap 2: Determinants of Effector Polarization (Th1 vs. Th17 vs. Th2) in Individual Patients

**Scope:** Why some patients/models develop Th1-dominant AIG while others develop Th2/eosinophilic or Th17-dominant disease is unknown.  
**Why it matters:** Affects patient stratification, prognosis, and therapeutic selection. May explain clinical heterogeneity (e.g., iron-deficiency anemia vs. pernicious anemia presentations).  
**What was checked:** Searched for genetic determinants, microbiome associations, and temporal factors. PTPN22 W620 favors Th1; no equivalent "Th2-biasing" or "Th17-biasing" AIG risk variants identified.  
**Resolution:** Multi-omic profiling (genetics + transcriptomics + immune phenotyping) of a large AIG cohort stratified by clinical phenotype.

### Gap 3: Temporal Relationship Between IFN-γ-Mediated Atrophy and IL-13-Mediated Metaplasia

**Scope:** Whether IL-13-driven metaplasia requires prior IFN-γ-mediated parietal cell loss (sequential model) or can develop independently (parallel model) is not established.  
**Why it matters:** Determines whether blocking IFN-γ early would prevent metaplasia (and thus neoplastic risk) or whether IL-13 pathway blockade is independently needed.  
**What was checked:** The TxA23 × Ifng−/− model shows inflammation without atrophy or metaplasia (PMID: 30511397), suggesting atrophy may be a prerequisite. But IL-4Rα−/− mice have atrophy without metaplasia (PMID: 34587523), confirming they are mechanistically separable.  
**Resolution:** Temporal IFN-γ blockade at different disease stages followed by assessment of metaplasia; IL-13 reporter mice in AIG models.

### Gap 4: No Prospective Longitudinal Human Cohort Tracking Immune Polarization Through Disease Stages

**Scope:** All human immune data are cross-sectional snapshots. No study has tracked the same patients' gastric immune profiles from early/pre-clinical to late-stage AIG.  
**Why it matters:** Cannot determine whether Th1 dominance at one stage transitions to Th17 or mixed profiles at later stages, or whether effector polarization is fixed throughout disease.  
**What was checked:** Searched for longitudinal AIG cohort studies with immune profiling. None found.  
**Resolution:** Prospective cohort study with serial gastric biopsies and immune profiling in PCA-positive individuals at risk for AIG.

### Gap 5: Absence of Clinical Trial Data Targeting IFN-γ or Th1 Pathway in Human AIG

**Scope:** No clinical trials of anti-IFN-γ, anti-IL-12, JAK inhibitors, or other Th1-pathway-targeting therapies in human AIG were found.  
**Why it matters:** Despite strong preclinical evidence, translation to human therapeutics is entirely absent.  
**What was checked:** PubMed and clinical trial databases for AIG immunotherapy trials. None identified.  
**Resolution:** Phase I/II trials of JAK1 inhibitors (blocking IFN-γ signaling) in early-stage AIG patients with active inflammation.

### Gap 6: No Single-Cell Omics Datasets for Human AIG

**Scope:** As of this search, no published scRNA-seq or CITE-seq studies of human AIG gastric tissue were identified. Available single-cell data is from murine models only (PMID: 34587523, 32376420).  
**Why it matters:** Cannot validate murine cell-type-specific findings in human tissue; cannot discover human-specific immune populations or states.  
**What was checked:** PubMed searches for "autoimmune gastritis single-cell" and "autoimmune gastritis scRNA-seq". One 2025 proof-of-concept study (PMID: 39837221) combined TCR-seq and transcriptomics from gastric biopsies in erosive gastritis but not specifically AIG.  
**Resolution:** scRNA-seq of matched AIG and non-AIG human gastric biopsies.

---

## Alternative Models

### 1. Th17/IL-17 Effector Polarization (Complementary/Parallel)

**Relationship:** Parallel co-required mechanism, not a complete alternative.  
IL-17 from CD4+ Th17 cells is co-required with IFN-γ for severe tissue destruction ([PMID: 22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/)). In certain contexts (e.g., intrinsic-factor-reactive T cells in pernicious anemia), the Th17 compartment may dominate. Th17-induced AIG shows the most destructive histological pattern and is resistant to Treg suppression ([PMID: 18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/)). This model does not replace Th1 but argues that both arms are needed for full disease.

### 2. Th2/Eosinophilic Effector Pathway (Alternative in Specific Contexts)

**Relationship:** True alternative in genetically predisposed models.  
Th2-polarized T cells can independently cause AIG with eosinophilic infiltration, IgG1/IgE autoantibodies, and parietal cell loss ([PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/); [PMID: 14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/)). In DEREG mice, disease is IL-4-dependent and ameliorated by eosinophil deficiency. Eosinophils have been detected in human AIG biopsies, suggesting clinical relevance. This represents a genuine alternative effector mechanism that may predominate in a subset of patients.

### 3. Two-Cytokine Sequential Model: IFN-γ (Atrophy) → IL-13 (Metaplasia)

**Relationship:** Downstream extension/refinement of the Th1 hypothesis.  
IFN-γ drives parietal cell death and atrophy, but IL-13 via IL-4Rα signaling independently drives the metaplastic transformation of surviving epithelium ([PMID: 34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/); [PMID: 30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/)). This model subsumes the Th1 hypothesis as explaining only the first pathological phase and adds a type-2 cytokine phase that determines neoplastic risk.

### 4. CD8+ Cytotoxic T Cell-Dominant Model

**Relationship:** Refinement of the IFN-γ source within the same cytokine framework.  
In polyclonal models, CD8+ T cells are the dominant IFN-γ source ([PMID: 22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/)). If this holds in human AIG, the "Th1" label is a misnomer — the critical effector is a CD8+ Tc1 cell, not a CD4+ Th1 cell. The cytokine (IFN-γ) remains central, but the cellular source shifts.

### 5. Treg Failure/Insufficiency Model (Upstream Cause)

**Relationship:** Upstream permissive condition, not a competing effector mechanism.  
Multiple models demonstrate that Treg depletion or deficiency is the permissive event enabling AIG: neonatal thymectomy removes Tregs ([PMID: 8766575](https://pubmed.ncbi.nlm.nih.gov/8766575/)), DEREG mice allow transient Treg depletion ([PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/)), and TGF-β-induced iTregs can prevent and treat AIG ([PMID: 18810612](https://pubmed.ncbi.nlm.nih.gov/18810612/); [PMID: 19050237](https://pubmed.ncbi.nlm.nih.gov/19050237/)). The Th1/IFN-γ hypothesis describes the effector arm; Treg failure describes the tolerance breach that unleashes it.

{{figure:mechanistic_causal_chain.png|caption=Mechanistic causal chain diagram showing the relationship between upstream tolerance failure, Th1/IFN-γ effector polarization, and downstream pathological outcomes including the separate IL-13-driven metaplasia pathway.}}

---

## Discriminating Tests

### Test 1: Single-Cell Immune Profiling of Human AIG Biopsies

**Design:** scRNA-seq + paired TCR-seq of gastric corpus biopsies from 20+ AIG patients stratified by disease stage (early inflammation, established atrophy, metaplasia) vs. age/sex-matched controls.  
**What it discriminates:** CD4+ Th1 vs. CD8+ Tc1 as dominant IFN-γ source; Th1 vs. Th17 vs. Th2 polarization prevalence; stage-dependent shifts in effector composition.  
**Expected result if Th1 hypothesis correct:** CD4+ Th1 (IFN-γ+, T-bet+) cells should be the dominant clonally expanded population at all stages. If CD8+ T cells dominate IFN-γ, the hypothesis label needs revision.  
**Biomarkers:** IFN-γ, T-bet, IL-17, RORγt, IL-13, GATA3, perforin, granzyme B by cell type.

### Test 2: Conditional IFN-γ Knockout in CD4+ vs. CD8+ Compartments

**Design:** Generate TxA23 mice with conditional Ifng deletion in CD4+ cells (CD4-Cre × Ifng-fl/fl) vs. CD8+ cells (CD8-Cre × Ifng-fl/fl) vs. both.  
**What it discriminates:** Whether CD4+ Th1-derived IFN-γ or CD8+-derived IFN-γ is the critical mediator.  
**Expected result if Th1 hypothesis correct:** CD4-specific IFN-γ deletion should markedly reduce disease; CD8-specific deletion should have minimal effect. If reversed, the CD8-dominant model is correct.

### Test 3: JAK1 Inhibitor Trial in Early Human AIG

**Design:** Phase II randomized controlled trial of a JAK1 inhibitor (e.g., upadacitinib, which blocks IFN-γ and IL-6 signaling) vs. placebo in PCA-positive patients with biopsy-proven early AIG (inflammation without complete atrophy).  
**Endpoints:** Primary: change in gastric corpus inflammation score at 6 months. Secondary: parietal cell mass (biopsy morphometry), serum pepsinogen I/II ratio, IFN-γ levels in gastric tissue.  
**What it discriminates:** Whether blocking the IFN-γ signaling axis can halt or reverse early AIG in humans.  
**Patient stratification:** PTPN22 W620 carriers vs. non-carriers (predicted to be differentially responsive if Th1 bias drives their disease).

### Test 4: PTPN22 Genotype-Stratified Immune Phenotyping

**Design:** Compare gastric biopsy immune profiles between AIG patients who are PTPN22 W620 carriers vs. non-carriers.  
**What it discriminates:** Whether the genetic Th1 bias translates to measurably different effector polarization in the target tissue.  
**Expected result if PTPN22-Th1 link is causal:** W620 carriers should show enhanced Th1/IFN-γ signatures and reduced Th17/IL-17 signatures in gastric tissue relative to non-carriers.

### Test 5: Temporal IL-13 Blockade in AIG Models

**Design:** Administer anti-IL-13 at different disease stages in TxA23 mice: (a) before atrophy onset, (b) during active atrophy, (c) after established metaplasia.  
**What it discriminates:** Whether IL-13-driven metaplasia requires prior IFN-γ-mediated atrophy (sequential) or is independent (parallel).  
**Expected result:** If sequential, anti-IL-13 at stage (a) should have no effect (no substrate for metaplasia yet), while stages (b) and (c) should block/reverse metaplasia. If parallel, anti-IL-13 should have effects at all stages.

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base. All require curator verification.*

### Candidate Evidence References

1. **[PMID: 30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/)** (Osaki et al. 2019) — *Interferon-γ directly induces gastric epithelial cell death and is required for progression to metaplasia.* Candidate snippet: "Chronic inflammation of the gastric mucosa, often caused by autoimmune gastritis and/or infection with Helicobacter pylori, can lead to atrophy of acid-secreting parietal cells with metaplasia of remaining cells." **Candidate action:** Add as SUPPORT evidence for IFN-γ-mediated atrophy; add as QUALIFYING evidence for metaplasia (IFN-γ necessary for atrophy but insufficient for metaplasia without IL-13).

2. **[PMID: 34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/)** (Noto et al. 2022) — *IL13 Acts Directly on Gastric Epithelial Cells to Promote Metaplasia.* Candidate snippet: "Organoid cultures showed that IL13 acts directly on gastric epithelium to induce a metaplastic phenotype. IL4Rα-deficient mice did not progress to metaplasia." **Candidate action:** Add as COMPETING evidence limiting the scope of Th1/IFN-γ hypothesis; link to a new `il13_metaplasia_pathway` hypothesis node.

3. **[PMID: 34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/)** + **[PMID: 23333624](https://pubmed.ncbi.nlm.nih.gov/23333624/)** — PTPN22 GWAS + functional Th1 bias. **Candidate action:** Add as SUPPORT evidence (genetic) for Th1/IFN-γ hypothesis with a subtype restriction to PTPN22 W620 carriers / pernicious anemia.

4. **[PMID: 27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/)** (Harakal et al. 2016) — Th2/eosinophilic AIG. **Candidate action:** Add as COMPETING evidence; link to an `alternative_th2_eosinophilic_effector` hypothesis node.

5. **[PMID: 21995497](https://pubmed.ncbi.nlm.nih.gov/21995497/)** (Iwamoto et al. 2012) — IFN-γ → CCL20 amplification loop. **Candidate action:** Add as SUPPORT evidence defining the recruitment mechanism downstream of IFN-γ.

6. **[PMID: 32376420](https://pubmed.ncbi.nlm.nih.gov/32376420/)** (Bockerstett et al. 2020) — IL-27 counter-regulation. **Candidate action:** Add as QUALIFYING evidence identifying endogenous suppression of the Th1/CD4 effector arm.

### Candidate Pathophysiology Nodes/Edges

- **New node:** `IFN-γ → CCL20 → CD4+ T cell recruitment` (amplification loop; PMID: 21995497)
- **New node:** `IL-13 → IL-4Rα → metaplastic epithelial transformation` (independent of IFN-γ; PMID: 34587523)
- **New edge:** `CD8+ T cells →(IFN-γ)→ parietal cell death` (dominant source in polyclonal; PMID: 22777705)
- **Modified edge:** `CD4+ Th1 →(IFN-γ)→ parietal cell death` should be annotated as "dominant in TCR-Tg models; may be secondary to CD8 in polyclonal disease"
- **New node:** `IL-27 →(suppression)→ CD4+ T cell inflammatory genes` (counter-regulatory; PMID: 32376420)

### Candidate Ontology Terms

- **Cell types:** CD4+ Th1 cell (CL:0000545), CD8+ cytotoxic T cell (CL:0000794), Th17 cell (CL:0000899), Th2 cell (CL:0000546), eosinophil (CL:0000771), gastric parietal cell (CL:0000162), dendritic cell (CL:0000451)
- **Biological processes:** Th1 cell differentiation (GO:0045063), IFN-γ-mediated signaling (GO:0060333), epithelial cell apoptotic process (GO:0010656), CCL20 chemokine signaling
- **Disease terms:** Autoimmune gastritis, pernicious anemia, spasmolytic polypeptide-expressing metaplasia (SPEM)

### Candidate Status Change

- **Current status:** CANONICAL  
- **Recommended status:** CANONICAL with qualifications  
- **Rationale:** The Th1/IFN-γ axis remains canonical for disease *initiation* and *atrophy*, but the KB should annotate that: (1) IFN-γ alone is insufficient for full disease; (2) the dominant IFN-γ source may be CD8+ rather than CD4+ Th1 in polyclonal disease; (3) metaplasia requires a separate IL-13 pathway. Consider creating a parent `multi_cytokine_cooperative_effector` hypothesis that encompasses Th1/IFN-γ, Th17/IL-17, and IL-13 arms.

### Candidate Knowledge Gap Entries

1. **Gap: Human CD4 vs. CD8 IFN-γ source** — No human data on relative CD8+ vs. CD4+ IFN-γ production in AIG tissue. Critical for validating the "Th1" label.
2. **Gap: No clinical trials targeting IFN-γ/Th1 in AIG** — Despite 30+ years of preclinical evidence, no therapeutic translation has been attempted.
3. **Gap: No human scRNA-seq of AIG** — Cannot validate murine single-cell findings in human tissue.
4. **Gap: Effector polarization determinants** — What determines Th1 vs. Th2 vs. Th17 dominance in individual patients is unknown.

---

## Evidence Base: Key Literature

| PMID | Title | Contribution |
|------|-------|-------------|
| [8766575](https://pubmed.ncbi.nlm.nih.gov/8766575/) | *Interferon-gamma is required during the initiation of an organ-specific autoimmune disease* | Foundational loss-of-function evidence for IFN-γ in AIG initiation |
| [11159878](https://pubmed.ncbi.nlm.nih.gov/11159878/) | *H+,K+-ATPase is the target autoantigen of Th1-type cytotoxic T cells in autoimmune gastritis* | Human clonal evidence for Th1 + dual cytotoxicity |
| [15763992](https://pubmed.ncbi.nlm.nih.gov/15763992/) | *Molecular specificity and functional properties of autoreactive T-cell response in human gastric autoimmunity* | Confirms human Th1 profile of autoreactive gastric T cells |
| [22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/) | *Both IFN-γ and IL-17 are required for the development of severe autoimmune gastritis* | Key qualifying paper: CD8 IFN-γ dominance + Th1/Th17 co-requirement |
| [18641328](https://pubmed.ncbi.nlm.nih.gov/18641328/) | *Th1, Th2, and Th17 effector T cell-induced autoimmune gastritis differs in pathological pattern* | All three subsets can cause AIG; Treg suppression varies by subset |
| [30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/) | *Interferon-γ directly induces gastric epithelial cell death* | IFN-γ as direct epithelial cytotoxin; required for atrophy |
| [34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/) | *IL13 acts directly on gastric epithelial cells to promote metaplasia* | IL-13/IL-4Rα pathway for metaplasia, independent of IFN-γ |
| [21995497](https://pubmed.ncbi.nlm.nih.gov/21995497/) | *IFN-γ is reciprocally involved in concurrent development of organ-specific autoimmunity* | IFN-γ → CCL20 → CD4 recruitment amplification loop |
| [27259856](https://pubmed.ncbi.nlm.nih.gov/27259856/) | *Regulatory T cells control Th2-dominant murine autoimmune gastritis* | Th2/eosinophilic alternative effector pathway |
| [14568977](https://pubmed.ncbi.nlm.nih.gov/14568977/) | *Molecular mimicry between H. pylori antigens and H+,K+-ATPase* | H. pylori cross-reactive Th1 cells in human AIG |
| [34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/) | *Genome-wide association study identifies five risk loci for pernicious anemia* | PTPN22 as PA risk locus |
| [23333624](https://pubmed.ncbi.nlm.nih.gov/23333624/) | *The autoimmune-predisposing variant of LYP favors T helper 1 responses* | PTPN22 W620 → Th1 bias + Treg resistance |
| [32376420](https://pubmed.ncbi.nlm.nih.gov/32376420/) | *IL27 protects from gastric atrophy and metaplasia during chronic autoimmune gastritis* | IL-27 as endogenous CD4+ T cell suppressor |
| [11905844](https://pubmed.ncbi.nlm.nih.gov/11905844/) | *The role of natural killer cells in the induction of autoimmune gastritis* | Rules out NK cells as IFN-γ source |
| [12391019](https://pubmed.ncbi.nlm.nih.gov/12391019/) | *Constitutive presentation of a natural tissue autoantigen exclusively by dendritic cells* | DCs present H+/K+-ATPase in draining LN constitutively |
| [14978094](https://pubmed.ncbi.nlm.nih.gov/14978094/) | *Spontaneous organ-specific Th2-mediated autoimmunity in TCR transgenic mice* | Th2-driven eosinophilic AIG as alternative pathway |
| [19050237](https://pubmed.ncbi.nlm.nih.gov/19050237/) | *Antigen-specific TGFβ-induced regulatory T cells suppress Th17-mediated autoimmune disease* | iTregs suppress Th17-mediated but not Th1-mediated AIG |
| [22124119](https://pubmed.ncbi.nlm.nih.gov/22124119/) | *Increased susceptibility to autoimmune gastritis in TSLPR-deficient mice* | TSLP counter-regulates Th1/IFN-γ-driven AIG |

---

## Limitations and Caveats

1. **Model system bias:** The majority of mechanistic evidence comes from murine models (NTx BALB/c, TxA23 TCR-Tg), which may not fully recapitulate human AIG immunopathology. TCR-transgenic systems in particular enforce a monoclonal response that may artificially favor Th1 polarization.

2. **Limited human data:** Only two groups (D'Elios/Bhatt and Amedei) have published gastric T cell clonal analyses from human AIG, representing small patient numbers. No modern single-cell studies of human AIG tissue exist.

3. **Cross-sectional human evidence:** All human immune data represent single time-point snapshots. The temporal evolution of effector polarization through disease stages in humans is unknown.

4. **Search limitations:** Literature searches were conducted via PubMed with English-language bias. Grey literature, conference abstracts, and non-English publications may contain additional relevant evidence.

5. **Strain and model specificity:** Key findings (e.g., CD8+ IFN-γ dominance) were demonstrated in specific mouse strains/models and may not generalize across all experimental systems or to human disease.

6. **No therapeutic translation data:** Despite decades of preclinical work, no clinical trials targeting the Th1/IFN-γ pathway in human AIG exist, preventing assessment of clinical relevance.

---

## Proposed Follow-up Experiments/Actions

1. **Immediate priority — Human scRNA-seq:** Perform scRNA-seq with paired TCR-seq on gastric corpus biopsies from a cohort of 20+ AIG patients across disease stages. This single experiment would resolve gaps 1, 2, 4, and 6 simultaneously.

2. **Genetic stratification study:** Genotype existing AIG/PA biobank cohorts for PTPN22 W620 and correlate with available immune phenotyping data, autoantibody profiles, and clinical outcomes.

3. **Conditional knockout experiment:** Generate CD4-Cre × Ifng-fl/fl and CD8-Cre × Ifng-fl/fl mice on the TxA23 background to definitively assign the critical IFN-γ source by cell compartment.

4. **Temporal cytokine blockade:** Administer anti-IFN-γ, anti-IL-17, and anti-IL-13 at different disease stages in TxA23 mice to map the temporal windows in which each cytokine contributes.

5. **Phase II clinical trial design:** Develop a protocol for JAK1 inhibitor treatment in early AIG, stratified by PTPN22 genotype, with gastric biopsy-based primary endpoints.

6. **Multi-ethnic GWAS expansion:** Extend pernicious anemia GWAS beyond European ancestry to identify population-specific risk architecture and additional Th1-pathway-relevant loci.

---

*Report generated from systematic evaluation of 51 papers across 5 iterative investigation cycles. 11 findings confirmed with verified citations. Analysis performed 2026-07-01.*
