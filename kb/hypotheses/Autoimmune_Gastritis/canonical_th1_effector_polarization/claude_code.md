---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T07:59:03.969156'
end_time: '2026-07-01T08:03:18.729534'
duration_seconds: 254.76
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
    \ H+/K+ ATPase\n    induces autoimmune gastritis."
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
  num_turns: 22
  total_cost_usd: 1.6181878999999997
  session_id: 5c58c42e-aa53-5307-a59b-32bd2414492b
  stop_reason: end_turn
citation_count: 12
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

# Mechanistic Hypothesis Search Report: Canonical Th1/IFN-γ Effector Polarization in Autoimmune Gastritis

## Executive Judgment

**Verdict: Partially supported — established but incomplete, and now superseded in emphasis.**

The Th1/IFN-γ paradigm is genuinely foundational: it is reproducible in the TxA23 TCR-transgenic and neonatal-thymectomy mouse models (Judkowski/Ronchetti group), and it is directly corroborated in human tissue — D'Elios and colleagues showed that gastric-mucosa-derived CD4+ T-cell clones from AIG patients are predominantly Th1, secrete IFN-γ/TNF-α, and are cytotoxic via perforin and Fas-FasL (PMID:15763992). Neutralizing anti-IFN-γ antibody blocks thymectomy-induced murine gastritis, giving reasonably direct causal (not just correlative) support.

However, three independent lines of more recent evidence qualify or partially compete with a "canonical, exclusive Th1" model:

1. **Cellular source mismatch**: In the polyclonal mouse model, IL-17 is produced almost exclusively by CD4+ T cells, while the *majority of IFN-γ* is produced by **CD8+ T cells**, not the CD4+ Th1 population the hypothesis emphasizes (Tu et al., PMID:22777705).
2. **Neither cytokine is individually necessary for disease initiation** — IFN-γ-deficient and IL-17-deficient effector T cells both still induce gastritis, only less severely; both cytokines together are required for progression to severe, destructive disease (PMID:22777705).
3. **Human disease, especially the intrinsic-factor-reactive/pernicious-anemia arm, is Th17-dominant, not Th1-dominant**: 94% of intrinsic-factor-specific gastric clones from pernicious anemia patients are Th17 or Th1, with a Th17:Th1 ratio of roughly 2:1 (28 Th17 vs 14 Th1 clones) (PMID:31080562), and serum/mucosal IL-17 family cytokines are elevated over Th1 readouts in a separate human cohort (PMID:35911678).

So the hypothesis should be read as **historically canonical and still mechanistically real, but not the sole or even necessarily the dominant effector axis** — particularly for late-stage/severe disease and for the intrinsic-factor-reactive compartment linked to pernicious anemia. It is best framed as one arm of a Th1/Th17/CD8 co-dependent effector program rather than a stand-alone sufficient mechanism.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Mechanistic claim tested | Key finding | Disease context | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:18641328 (Ronchetti group) | Model organism (TCR-transgenic TxA23 effector transfer) | Supports (Th1 causes gastritis) but **qualifies exclusivity** | Do fully differentiated Th1/Th2/Th17 cells specific for H+/K+-ATPase each induce gastritis? | All three subsets caused disease; Th17 caused the *most destructive* pattern (eosinophilic infiltrate, high IgE) and was resistant to Treg suppression, while Th1-induced disease was readily Treg-suppressible | Mouse, antigen-specific transfer model | High internal validity for the model; species/antigen-specific TCR system, not spontaneous human disease |
| PMID:22777705 Tu et al. 2012, *Eur J Immunol* | Model organism | **Qualifies** (source and necessity of IFN-γ) | Are IFN-γ and IL-17 each required, and which cells make them? | IL-17 made solely by CD4+ T cells; **majority of IFN-γ made by CD8+ T cells**; IFN-γ-deficient or IL-17-deficient T cells still cause gastritis but less severely; both required for progression to severe disease | Mouse polyclonal thymectomy-type model | Directly undercuts the "CD4+ Th1 as the IFN-γ source" framing of the seed hypothesis; strong mechanistic (KO) design |
| PMID:15763992 D'Elios et al. | Human clinical (ex vivo T-cell clones) | **Supports** | Are gastric-mucosa CD4+ T cells in human AIG Th1-polarized and cytotoxic? | Majority of H+/K+-ATPase-reactive clones secrete IFN-γ (Th1 profile); all produce TNF-α, help B-cell Ig production, and kill via perforin/Fas-FasL | Human AIG/atrophic gastritis | Strong direct human evidence; small clone-based sampling, cross-sectional |
| PMID:31080562 (Oncotarget 2019) | Human clinical (ex vivo T-cell clones) | **Competing/qualifies** | Is the intrinsic-factor-reactive compartment also Th1-dominant? | 94% of IF-specific clones are Th17 or Th1, but the **majority (28/51) are Th17**, not Th1 (14/51); all produce TNF-α; IL-17+ clones co-produce IL-21 and help B cells | Human pernicious anemia (IF-reactive arm) | Directly competes with a Th1-exclusive framing for the PA/IF-antibody-positive subset; clone-based, single cohort |
| PMID:35911678 Vitale et al. 2022 | Human clinical (LPMC + serum) | **Competing/qualifies** | Is there a dominant Th17/IL-17 signature in AIG gastric mucosa and serum? | Gastric LPMCs from AIG (not controls) proliferate to H+/K+-ATPase and secrete high IL-17A/F; serum IL-17A/F, IL-21, IL-17E elevated vs controls and vs iron-deficiency-anemia-without-AIG | Human AIG (43 patients) | No comparative Th1 arm reported in this study — cannot directly quantify Th1 vs Th17 dominance, only shows Th17 axis is robustly present |
| PMC2194239 / JEM (Rockefeller Press) H. pylori mimicry paper | Human clinical + in vitro | **Supports** (upstream trigger for Th1) | Does H. pylori antigenic mimicry with H+/K+-ATPase drive Th1 polarization? | Cross-reactive H. pylori peptides (9 identified proteins) induce T-cell proliferation and Th1 cytokine expression in genetically susceptible individuals | Human, H. pylori-associated AIG | Supports an upstream trigger mechanism for Th1 activation; does not address Th17/CD8 contributions |
| Bookshelf NBK2439 ("Gastric Autoimmunity," H. pylori text) | Review, synthesizing mouse + human | Review-level support | Synthesizes CD4-dependence, Th1 dominance, Fas-FasL killing | Anti-IFN-γ antibody prevents thymectomy-induced gastritis (direct blockade); CD4+ (not CD8+) T cells required in EAIG; B-cell-deficient mice still develop full pathology (autoantibodies dispensable); β-subunit epitopes initiate response, α-subunit epitopes arise via epitope spreading | Mouse + human synthesis | Review, but cites primary blockade/KO experiments; strongest single source for causal (not just correlative) IFN-γ dependence |
| Frontiers (2026) "Autoimmune gastritis: comprehensive review" | Review | Review-level, balanced | Synthesizes Th1, Th17, CD8, PCA/IFA roles, H. pylori, genetics | States PCA pathogenic role is "debated"; genetic loci HLA-DRB1*03/*04, PTPN22, CTLA4, IL10; explicit gap: no approved Treg-restoring immunomodulatory therapy; H. pylori-eradication reversibility of AIG is "a subject of intense controversy" | Human synthesis | Orientation-level; useful for gap-mapping, not primary evidence |
| PMC12563516 review ("Autoimmune Gastritis Puzzle") | Review | Review-level, flags gaps | Synthesizes Th1/Th17 dual axis, DC/ILC3 contribution, complement/ADCC, ECL hyperplasia | Explicitly states DC/ILC contribution is "largely speculative," ER-stress evidence in human AIG is "limited," Treg-dysfunction "mechanistic data ... remain limited" | Human + mouse synthesis | Directly enumerates knowledge gaps relevant to curation (see below) |
| PMC11347309 review (cytokine-therapy review) | Review, cites Lenti 2022 human organ-culture data | Review-level support + therapeutic angle | Surveys IFN-γ, TNF-α, IL-17, IL-21, IL-13, IL-6 in human AIG tissue/serum | TNF-α elevated in AIG organ-culture supernatants (Lenti et al. 2022) vs controls; IL-13 elevated in blood/mucosa and in TxA23 mice, required for metaplasia (IL-13R-KO mice show no metaplasia); frames AIG as multi-cytokine, not Th1-exclusive, disease | Human + mouse synthesis | Useful for identifying that IL-13/Th2-associated metaplasia signal is a distinct, non-Th1 downstream arm |
| Nat Commun 2021 (GWAS, doi:10.1038/s41467-021-24051-6) | Human clinical (genetic, population-scale) | Contextual (does not directly test Th1 vs Th17) | Genetic architecture of pernicious anemia | Risk loci: PTPN22, PNPT1, HLA-DQB1, IL2RA, AIRE; susceptibility mapped to HLA-DR15 haplotype | Human, population genetics (2,166 cases / 659,516 controls) | Supports a general adaptive-autoimmune (T-cell antigen-presentation/tolerance) architecture consistent with *some* effector-T-cell model, but does not discriminate Th1 vs Th17 vs CD8 |

---

## Mechanistic Causal Chain

**As implied by the seed hypothesis:**

1. **Upstream trigger** — Loss of central/peripheral tolerance to gastric H+/K+-ATPase (β-subunit epitopes implicated as initiating; α-subunit epitopes arise by epitope spreading), potentiated by genetic susceptibility (HLA-DR15/DRB1*03/*04, PTPN22, AIRE, IL2RA) and, in many patients, molecular mimicry with H. pylori antigens. — *Moderately strong*: genetic and mimicry evidence exists but each explains only a fraction of cases, and the mimicry-to-established-AIG transition is not fully tracked longitudinally in humans.
2. **CD4+ T-cell priming and Th1 polarization** — Autoreactive CD4+ T cells encounter H+/K+-ATPase peptide on MHC class II (itself IFN-γ-inducible on gastric epithelium, a feed-forward loop) and differentiate into IFN-γ/TNF-α-producing Th1 effectors. — *Strong* in both mouse (TxA23 transfer) and human (D'Elios clone) systems; this is the best-anchored link in the whole chain.
3. **Effector recruitment and amplification** — Th1 cytokines recruit/activate CD8+ T cells, macrophages, and NK cells; CD8+ T cells become the dominant *in vivo* source of IFN-γ, and CD4+ Th17 cells contribute IL-17 in parallel. — *Inferred/qualified*: this step is where the seed hypothesis's exclusivity breaks down — Tu et al. show CD8, not CD4, dominates IFN-γ production, and IL-17 is co-required, not merely supplementary.
4. **Direct cytotoxic destruction of parietal cells** — Perforin-mediated cytotoxicity and Fas-FasL apoptosis, plus IFN-γ-mediated direct epithelial killing (shown to be ~100x more concentrated and ~10x more potent than IL-17A alone at inducing epithelial death in one study). — *Strong* for the IFN-γ/Fas-FasL mechanism itself; the *relative* quantitative contribution of IFN-γ- versus IL-17-mediated killing in human tissue (as opposed to in vitro potency assays) is not established.
5. **Achlorhydria → hypergastrinemia → ECL hyperplasia; and B12/intrinsic-factor deficiency → pernicious anemia.** — *Strong and well-mapped downstream* but mechanistically decoupled from the CD4-Th1-specific question; this is where the intrinsic-factor-reactive Th17-dominant clones become relevant, since IF-reactive T cells are a distinct autoreactive population from H+/K+-ATPase-reactive Th1 cells.

**Where the chain is strong:** the CD4+ T-cell dependence of disease overall (step 2), the Fas-FasL/perforin/IFN-γ direct killing mechanism (step 4), and the downstream achlorhydria→hypergastrinemia physiology (step 5).

**Where the chain is inferred/weak:** the claim that Th1/IFN-γ from *CD4+* cells specifically (rather than CD8+ cells) is the dominant proximal effector (step 3); the *relative weighting* of Th1 vs Th17 vs CD8 contributions in human disease at different stages; and the causal sequence from H. pylori mimicry to established autoimmunity in humans (step 1→2 transition, which is inferred from cross-sectional serologic/clone data, not longitudinal cohorts).

---

## Knowledge Gaps

1. **CD4-Th1 vs CD8 as the true proximal IFN-γ source in human disease.** *Scope*: mouse data (PMID:22777705) show CD8+ T cells, not CD4+ Th1 cells, produce most IFN-γ; no equivalent human intracellular-cytokine-staining/single-cell study has been identified that resolves CD4 vs CD8 IFN-γ source in situ in human AIG gastric mucosa. *Why it matters*: the seed hypothesis's causal-chain label ("Th1/IFN-γ effector polarization") implicitly attributes IFN-γ to CD4+ Th1 cells; if CD8+ cells dominate in humans as in mice, the KB hypothesis label may need a companion/competing node for CD8-mediated cytotoxicity. *What was checked*: searched specifically for human CD8-source IFN-γ studies in AIG; none found beyond the D'Elios CD4-clone-focused work, which by design only samples CD4+ clones. *Resolving experiment*: single-cell RNA-seq/CyTOF of human gastric-mucosa infiltrates in biopsy-confirmed AIG stratified by stage, with intracellular IFN-γ/IL-17 staining by CD4/CD8 lineage.

2. **Relative quantitative contribution of Th1 vs Th17 across disease stage and subtype (H+/K+-ATPase-reactive vs intrinsic-factor-reactive).** *Scope*: human clone studies show H+/K+-ATPase-reactive clones skew Th1 (PMID:15763992) while intrinsic-factor-reactive clones skew Th17 (PMID:31080562); no single cohort has co-profiled both antigen-specificities with matched Th1/Th17 quantification. *Why it matters*: this could mean the seed hypothesis is stage- or antigen-specificity-restricted rather than disease-wide — a curation-relevant subtype qualifier. *What was checked*: searched for a combined H+/K+-ATPase + intrinsic-factor dual-specificity human clone study; not found. *Resolving experiment*: paired gastric-mucosa clone panels from the same AIG patients tested against both autoantigens with full Th-subset immunophenotyping, stratified by early (PCA+/IFA-) vs late (IFA+, B12-deficient) stage.

3. **Necessity vs sufficiency of IFN-γ blockade in human AIG.** *Scope*: murine anti-IFN-γ antibody blocks thymectomy-induced gastritis (Bookshelf NBK2439 synthesis of primary literature), but no human interventional trial of IFN-γ blockade (e.g., emapalumab) in AIG has been run; this is proposed only as "preclinical-model-supported" in the PMC11347309 review. *Why it matters*: this is the most direct test of whether Th1/IFN-γ is causally necessary (not just correlated) in human disease, and would directly discriminate the canonical hypothesis from the Th17-co-dependent alternative. *What was checked*: searched clinicaltrials.gov-adjacent literature mentions; none found for AIG specifically (emapalumab is approved for HLH, not trialed in AIG). *Resolving experiment*: a proof-of-concept trial or expanded-access case series of anti-IFN-γ (emapalumab) or anti-IL-17 (secukinumab) monotherapy in biopsy-confirmed, early-stage AIG with serial gastric biopsy and cytokine readouts.

4. **Reversibility of AIG after H. pylori eradication (mimicry-trigger causality).** *Scope*: the Frontiers 2026 review explicitly flags this as "a subject of intense controversy." *Why it matters*: if Th1 polarization is triggered and sustained by ongoing molecular mimicry, eradication should attenuate disease; persistence after eradication would argue for an autonomous, mimicry-independent autoimmune loop (supporting a more Treg-failure-centric or epitope-spreading model over a purely infection-driven Th1 model). *What was checked*: reviewed the Frontiers synthesis and the JEM mimicry paper (PMC2194239); no longitudinal post-eradication AIG remission/resolution cohort was surfaced in this search. *Resolving experiment*: prospective, biopsy- and cytokine-tracked cohort of H. pylori-positive AIG patients before/after eradication therapy, with H+/K+-ATPase-specific Th1/Th17 clone frequency as the primary immunologic endpoint.

5. **Treg dysfunction mechanism in human AIG.** *Scope*: mouse Treg-transfer experiments show polyclonal Tregs suppress Th1- and Th2- but not Th17-induced gastritis (PMID:18641328); PMC12563516 explicitly states "mechanistic data [on Treg failure] in AIG remain limited" in humans. *Why it matters*: this determines whether the canonical hypothesis's vulnerability (Th17 resistance to Treg suppression) is clinically relevant, i.e., whether human AIG patients have a Treg quantitative or qualitative defect that permits either subset to escape control. *What was checked*: searched for human Treg-frequency/function studies in AIG gastric mucosa; not surfaced in this search (a dedicated follow-up search would be needed). *Resolving experiment*: Treg frequency/suppressive-function assays (Foxp3, Helios, suppression co-culture) from AIG gastric mucosa vs H. pylori gastritis vs healthy controls.

6. **No dedicated ClinGen/GenCC entry** exists for AIG as a Mendelian trait (expected, since it is polygenic/complex); the closest structured genetic evidence is the population-scale GWAS (doi:10.1038/s41467-021-24051-6), which was checked and found, but it addresses **susceptibility architecture**, not **effector-T-cell-subset causality** — a source-level absence worth flagging explicitly in the KB entry: no perturbation/allele-specific data links any GWAS locus (PTPN22, IL2RA, AIRE) mechanistically back to the Th1-vs-Th17 balance.

---

## Alternative Models

| Model | Relationship to seed hypothesis | Summary |
|---|---|---|
| **Th17/IL-17-dominant effector model** | **Alternative/competing**, especially for intrinsic-factor-reactive and severe/eosinophilic disease | PMID:18641328 (Th17 most destructive, Treg-resistant), PMID:22777705 (IL-17 co-required for severe disease), PMID:31080562 (Th17 majority in human IF-reactive clones), PMID:35911678 (human IL-17 signature). Increasingly viewed as co-dominant rather than subordinate to Th1. |
| **CD8+ cytotoxic T-cell model** | **Complementary/parallel**, and a direct qualifier of the Th1 model's cellular-source claim | PMID:22777705 shows CD8+ T cells are the majority IFN-γ source in vivo; this reframes "Th1/IFN-γ" as "IFN-γ" more generally, sourced substantially from CD8, not CD4. |
| **Antibody-mediated / ADCC model (PCA, IFA, complement)** | **Parallel/complementary**, largely non-competing since most reviews treat antibodies as secondary | PCA (85–90% seropositivity) and IFA (95–100% specificity) may contribute via complement activation and ADCC (PMC12563516), but B-cell-deficient mice still develop full pathology (NBK2439), so this is a secondary/amplifying rather than primary-effector alternative. |
| **Molecular-mimicry/H. pylori-triggered model** | **Upstream cause**, not a competing effector mechanism | Explains *why* Th1 (and by extension Th17/CD8) polarization is initiated in a genetically susceptible host (PMC2194239); does not compete with the seed hypothesis but supplies its trigger. |
| **Th2/IL-13-driven metaplasia model** | **Downstream/parallel consequence**, distinct pathway | IL-13 elevated in human blood/mucosa and TxA23 mice; IL-13-receptor-deficient mice show no metaplasia (PMC11347309). This is a largely separate, non-Th1 axis governing the SPEM/metaplasia phenotype rather than parietal-cell killing itself. |
| **Genetic/tolerance-failure model (PTPN22, AIRE, IL2RA, HLA-DR15)** | **Upstream cause/permissive substrate** | GWAS-defined susceptibility architecture (doi:10.1038/s41467-021-24051-6) is agnostic to which effector T-cell subset ultimately dominates; it is the substrate on which either a Th1- or Th17-skewed response could arise. |
| **Treg-insufficiency model** | **Parallel/permissive**, could unify Th1 and Th17 observations | If Tregs are quantitatively/qualitatively deficient in human AIG (unconfirmed — see Knowledge Gap 5), this could explain why *both* Th1 and Th17 escape control rather than framing them as competing single-axis hypotheses. |

---

## Discriminating Tests

1. **Multi-parameter flow/CyTOF or single-cell RNA-seq of fresh gastric-mucosa biopsies** from biopsy-confirmed AIG patients, stratified by disease stage (early PCA+/IFA− vs late IFA+/B12-deficient) and H. pylori status, with intracellular IFN-γ/IL-17/IL-21 staining gated by CD4 vs CD8 lineage. Expected result if seed hypothesis holds: CD4+IFN-γ+ (Th1) cells dominate at all stages; if the CD8-source/Th17-co-dominance alternative holds: CD8+IFN-γ+ and/or CD4+IL-17+ populations dominate, especially at later/IFA+ stages.
2. **Dual-antigen (H+/K+-ATPase and intrinsic factor) T-cell clone panels from the same patients**, comparing Th1:Th17 ratio by antigen specificity within-patient. Expected result: if antigen-specificity (not disease stage) drives Th1 vs Th17 skewing, H+/K+-ATPase clones will remain Th1-skewed while IF clones remain Th17-skewed in the same individual — supporting an antigen-restricted rather than disease-wide effector program.
3. **Targeted cytokine-blockade proof-of-concept study** in early-stage, biopsy-confirmed AIG: a small case series or trial arm using anti-IFN-γ (emapalumab) versus anti-IL-17 (secukinumab) versus combination, with serial gastric biopsy (parietal cell density, infiltrate composition) and serologic (gastrin, PCA/IFA titer) endpoints. Expected result: if IFN-γ is truly necessary and rate-limiting, anti-IFN-γ alone should measurably slow histologic progression; if IL-17 is co-equal (per Tu et al. mouse data), only combination blockade will show a strong effect.
4. **Longitudinal H. pylori eradication cohort** with pre/post H+/K+-ATPase-specific Th1/Th17 clone frequency, gastrin, and PCA/IFA titers. Expected result: if mimicry is the dominant sustaining trigger, eradication should reduce Th1 clone frequency and halt progression; persistence would support an autonomous post-mimicry autoimmune loop.
5. **Treg frequency/suppressive-function assay** (Foxp3+Helios+ Treg proportion and in vitro suppression of autologous Th1 vs Th17 clones) from AIG gastric mucosa vs H. pylori-gastritis-without-AIG vs healthy controls. Expected result: if Treg failure is permissive for both subsets (unifying model), Treg suppressive capacity against both Th1 and Th17 effectors should be reduced in AIG; if Treg failure is Th17-specific (per the mouse Treg-resistance data), suppression of autologous Th1 clones should remain relatively intact while Th17 suppression is selectively lost.
6. **CRISPR/adoptive-transfer dissection in the TxA23 mouse**: transfer purified CD8+ vs CD4+ IFN-γ-competent/deficient populations independently (extending Tu et al. 2012) to directly quantify each lineage's contribution to parietal-cell loss, holding IL-17 constant. Expected result: would directly resolve whether CD4-Th1-derived IFN-γ specifically (versus CD8-derived) is rate-limiting for tissue destruction.

---

## Curation Leads

*All items below are leads requiring curator verification (PMID/DOI check, snippet-in-abstract confirmation, and ontology term validation per dismech SOP) before being added to the KB.*

**Candidate evidence references to verify and add:**
- `PMID:22777705` (Tu et al., *Eur J Immunol* 2012) — candidate snippet to verify against abstract: *"the majority of IFN-γ-producing cells were CD8+ T cells"* and *"production of neither IL-17 nor IFN-γ by effector T cells is essential for the initiation of autoimmune gastritis... both are required for the disease to progress to the late pathogenic stage."* Use `evidence_source: MODEL_ORGANISM`. This is a strong **REFUTE/QUALIFY** candidate against a Th1-exclusive framing of the seed hypothesis (CD4-source claim) and a **SUPPORT** for IFN-γ's role in progression specifically.
- `PMID:15763992` (D'Elios et al.) — candidate snippet: *"The majority of the autoreactive T cell clones secreted IFN-gamma and showed a T helper 1 (Th1) profile."* `evidence_source: HUMAN_CLINICAL`. Strong direct human **SUPPORT**.
- `PMID:31080562` (Oncotarget 2019, intrinsic-factor Th17/Th1) — candidate snippet: *"28 IF-specific T-cell clones were polarized Th17 clones, 14 Th clones were polarized Th1"* — a **COMPETING** hypothesis-relevant reference; consider filing as evidence for a new/alternative hypothesis node ("intrinsic-factor-reactive Th17 effector arm") rather than under the canonical Th1 node, since the antigen specificity differs from H+/K+-ATPase.
- `PMID:35911678` (Vitale et al. 2022) — candidate snippet re: serum IL-17A elevation (need exact abstract quote verified via `just fetch-reference`). `evidence_source: HUMAN_CLINICAL`.
- GWAS reference (Nat Commun 2021) — verify PMID via PubMed lookup (not confirmed in this search; DOI is `10.1038/s41467-021-24051-6`) before citing; candidate snippet re: PTPN22/HLA-DR15/AIRE/IL2RA risk loci — relevant as `notes:` context on genetic susceptibility rather than direct hypothesis evidence, since it does not test Th1-vs-Th17 causality.

**Candidate pathophysiology nodes/edges:**
- A parallel/competing node: "Th17/IL-17 Effector Polarization" (status: candidate EMERGING or ESTABLISHED depending on curator judgment), with a `downstream` edge converging on the same "Parietal Cell Destruction" node as the canonical Th1 node, to reflect the co-dependency shown in Tu et al.
- A qualifier edge/annotation on the existing canonical node clarifying that the *cellular source* of IFN-γ in the mouse model is predominantly CD8+, not CD4+ Th1 — consider a `discussions` entry with `kind: KNOWLEDGE_GAP` flagging that human confirmation of CD4 vs CD8 IFN-γ source is absent.
- A subtype/antigen-specificity qualifier distinguishing H+/K+-ATPase-reactive (Th1-skewed) vs intrinsic-factor-reactive (Th17-skewed) effector compartments, potentially as separate `pathophysiology` nodes if the KB models antigen-specific arms separately.

**Candidate ontology terms (for curator verification via OAK):**
- Cell types: `CL:0000545` (T-helper 1 cell), `CL:0000899` (Th17 cell), `CL:0000625` (CD8-positive, alpha-beta T cell) — verify exact labels.
- Biological processes: consider GO terms for "interferon-gamma-mediated signaling pathway," "T-helper 17 type immune response," and "Fas-associated death domain protein signaling" (verify exact GO IDs/labels).
- Phenotype: `HP:0011974` or similar for atrophic gastritis / parietal cell loss (verify against existing entry).

**Candidate subtype/status changes:**
- Consider whether `status: CANONICAL` should be qualified with a note that the hypothesis is *established for CD4-independent IFN-γ dependence generally* but *not established as the sole or CD4-Th1-specific mechanism*, given the CD8-source finding and the Th17-codominance in the intrinsic-factor arm.

**Candidate discussion/knowledge-gap prompts:**
- "Is IFN-γ production in human AIG gastric mucosa predominantly CD4 (Th1) or CD8-derived, as in the mouse model?" (`kind: KNOWLEDGE_GAP`)
- "Does H. pylori eradication measurably reduce H+/K+-ATPase-specific Th1 clone frequency and halt AIG progression, or does autoimmunity persist autonomously?" (`kind: KNOWLEDGE_GAP`, tied to the Frontiers 2026 review's explicit statement of controversy)
- Consider a `kind: HUMAN_MODEL_MISMATCH` discussion node: the TxA23/neonatal-thymectomy mouse models cleanly separate Th1/Th2/Th17 by adoptive transfer of purified, pre-differentiated lines, whereas human gastric mucosa contains a mixed, in vivo-differentiated repertoire (including Th17/Th1 "Th0-like" hybrid clones, per PMID:31080562) — the translational validity of the clean mouse Th-subset dichotomy to human polyclonal disease is an open question worth flagging explicitly.

Sources:
- [Th1, Th2, and Th17 Effector T Cell-Induced Autoimmune Gastritis Differs in Pathological Pattern and in Susceptibility to Suppression by Regulatory T Cells (PMID:18641328)](https://pubmed.ncbi.nlm.nih.gov/18641328/)
- [Both IFN-γ and IL-17 are required for the development of severe autoimmune gastritis (PMID:22777705)](https://pubmed.ncbi.nlm.nih.gov/22777705/)
- [Molecular specificity and functional properties of autoreactive T-cell response in human gastric autoimmunity (PMID:15763992)](https://pubmed.ncbi.nlm.nih.gov/15763992/)
- [Gastric Th17 Cells Specific for H+/K+-ATPase and Serum IL-17 Signature in Gastric Autoimmunity (PMID:35911678)](https://pubmed.ncbi.nlm.nih.gov/35911678/)
- [Intrinsic factor recognition promotes T helper 17/T helper 1 autoimmune gastric inflammation in patients with pernicious anemia (PMID:31080562)](https://pubmed.ncbi.nlm.nih.gov/31080562/)
- [Molecular Mimicry between Helicobacter pylori Antigens and H+,K+–Adenosine Triphosphatase in Human Gastric Autoimmunity (PMC2194239)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2194239/)
- [Gastric Autoimmunity — Helicobacter pylori (NCBI Bookshelf NBK2439)](https://www.ncbi.nlm.nih.gov/books/NBK2439/)
- [The Autoimmune Gastritis Puzzle: Emerging Cellular Crosstalk and Molecular Pathways Driving Parietal Cell Loss and ECL Cell Hyperplasia (PMC12563516)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563516/)
- [Pro- and anti-inflammatory cytokines: the hidden keys to autoimmune gastritis therapy (PMC11347309)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11347309/)
- [Frontiers: Autoimmune gastritis: a comprehensive review of pathophysiology, risk stratification, and management (2026)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1878128/full)
- [Genome-wide association study identifies five risk loci for pernicious anemia (Nature Communications 2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8213695/)
- [Update in Molecular Aspects and Diagnosis of Autoimmune Gastritis (PMID:37504250)](https://pubmed.ncbi.nlm.nih.gov/37504250/)