---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T07:58:54.980931'
end_time: '2026-07-01T08:02:42.111955'
duration_seconds: 227.13
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Autoimmune Gastritis
  category: Complex
  hypothesis_group_id: canonical_primary_autoimmune_hk_atpase_origin
  hypothesis_label: Canonical Primary Autoimmunity Against the Gastric H+/K+ ATPase
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_primary_autoimmune_hk_atpase_origin\n\
    hypothesis_label: Canonical Primary Autoimmunity Against the Gastric H+/K+ ATPase\n\
    status: CANONICAL\ndescription: 'Autoimmune gastritis is a primary organ-specific\
    \ autoimmune disease driven by a breakdown\n  of self-tolerance to the parietal-cell\
    \ H+/K+ ATPase (ATP4A/ATP4B), with CD4 T-cell-mediated parietal\n  cell destruction\
    \ that is self-sustaining and independent of any persistent infection. Central-tolerance\n\
    \  biology supports a primary origin: the H/K-ATPase alpha-subunit is expressed\
    \ in the thymus, and the\n  murine disease induced by neonatal thymectomy is T-cell-mediated,\
    \ while monogenic tolerance defects\n  (AIRE/APECED, FOXP3/IPEX) produce autoimmune\
    \ gastritis as part of polyautoimmunity.'\nevidence:\n- reference: PMID:9272282\n\
    \  reference_title: Expression of the gastric H/K-ATPase alpha-subunit in the\
    \ thymus may explain the dominant\n    role of the beta-subunit in the pathogenesis\
    \ of autoimmune gastritis.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: The murine disease induced by neonatal thymectomy is T cell-mediated.\n\
    \  explanation: Thymic expression of the H/K-ATPase and the T-cell-mediated thymectomy\
    \ model support a\n    primary central-tolerance origin of autoimmune gastritis."
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
  web_search_requests: 16
  num_turns: 18
  total_cost_usd: 1.7466380000000001
  session_id: 5c58c42e-aa53-5307-a59b-32bd2414492b
  stop_reason: end_turn
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
- **Hypothesis ID:** canonical_primary_autoimmune_hk_atpase_origin
- **Hypothesis Label:** Canonical Primary Autoimmunity Against the Gastric H+/K+ ATPase
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_primary_autoimmune_hk_atpase_origin
hypothesis_label: Canonical Primary Autoimmunity Against the Gastric H+/K+ ATPase
status: CANONICAL
description: 'Autoimmune gastritis is a primary organ-specific autoimmune disease driven by a breakdown
  of self-tolerance to the parietal-cell H+/K+ ATPase (ATP4A/ATP4B), with CD4 T-cell-mediated parietal
  cell destruction that is self-sustaining and independent of any persistent infection. Central-tolerance
  biology supports a primary origin: the H/K-ATPase alpha-subunit is expressed in the thymus, and the
  murine disease induced by neonatal thymectomy is T-cell-mediated, while monogenic tolerance defects
  (AIRE/APECED, FOXP3/IPEX) produce autoimmune gastritis as part of polyautoimmunity.'
evidence:
- reference: PMID:9272282
  reference_title: Expression of the gastric H/K-ATPase alpha-subunit in the thymus may explain the dominant
    role of the beta-subunit in the pathogenesis of autoimmune gastritis.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: The murine disease induced by neonatal thymectomy is T cell-mediated.
  explanation: Thymic expression of the H/K-ATPase and the T-cell-mediated thymectomy model support a
    primary central-tolerance origin of autoimmune gastritis.
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

# Mechanistic Hypothesis Search: Canonical Primary Autoimmunity Against the Gastric H+/K+ ATPase (Autoimmune Gastritis)

## Executive Judgment

**Verdict: Partially supported — well-established as the proximate effector mechanism, but "primary" and "independent of persistent infection" are overstated as absolute claims.**

The core claim that CD4+ T-cell-mediated destruction of parietal cells, targeting the gastric H+/K+-ATPase (ATP4A/ATP4B), is the proximate immunopathogenic mechanism of autoimmune gastritis is **very strongly supported** by four decades of concordant human and murine evidence: the neonatal-thymectomy mouse model, adoptive-transfer experiments, TCR-transgenic tolerance studies, human autoantibody/T-cell reactivity data, and monogenic-tolerance human syndromes (APECED/AIRE, IPEX/FOXP3) all converge on H/K-ATPase-directed, CD4-driven, Th1/Th17-mediated parietal cell loss (PMID:9272282; PMID:9640252; PMID:8759770; PMID:10064084; PMID:7517707; PMID:35911678).

However, two qualifiers weaken the "primary, infection-independent" framing embedded in the hypothesis label:

1. **The central-tolerance evidence is more nuanced than the seed snippet implies.** The cited paper (PMID:9272282) does not simply show that thymic alpha-subunit expression *causes* autoimmunity — it shows the *opposite logic*: the alpha subunit is thymically expressed (in an Aire-independent manner) and thus partially tolerizes, while the beta subunit is **not** expressed in the thymus and becomes the dominant pathogenic autoantigen; only forced transgenic thymic expression of the beta subunit (not the naturally-expressed alpha subunit) confers protection (PMID:8390962-class transgenic studies, Rockefeller JEM 1993). This is evidence for a tolerance-breakdown model, but the specific causal mechanism is subtler than "thymic self-antigen expression establishes tolerance" — it is a story of *incomplete/subunit-selective* central tolerance.
2. **"Independent of any persistent infection" is contradicted by a substantial parallel literature on *Helicobacter pylori* molecular mimicry**, in which cross-reactive H. pylori CD4+ T-cell epitopes are demonstrated in human gastric autoimmunity (PMID:14568977; PMID:15242679; PMID:15596126). This does not refute the T-cell/H-K-ATPase mechanism itself, but it directly challenges the claim that the autoimmune process is necessarily primary and infection-independent in humans — the two are better read as complementary/competing *initiating-trigger* hypotheses layered on a shared *effector* mechanism.

So: the **effector mechanism** (CD4+ T-cell/H-K-ATPase-directed parietal cell destruction, self-sustaining once established) is well supported and should remain CANONICAL. The **etiological claim of a purely primary, tolerance-defect origin excluding infectious triggers** is unresolved and should be qualified or split into a distinct "trigger" layer in the KB.

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Mechanistic claim tested | Key finding | Context/subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| PMID:9272282 (Alderuccio et al., *Autoimmunity* 1997) | Model organism | Supports (with nuance) | Thymic self-antigen expression shapes autoreactive T-cell repertoire | H/K-ATPase alpha subunit is expressed in normal BALB/c thymus (Aire-independent); beta subunit is not — explaining why beta becomes the dominant pathogenic target | Murine, neonatal-thymectomy model | Moderate. Supports central-tolerance framework but shows *incomplete* tolerance, not simple confirmation |
| Rockefeller JEM 1993 ("An autoimmune disease with multiple molecular targets abrogated by transgenic expression of a single autoantigen in the thymus") | Model organism | Supports | Forced thymic beta-subunit expression prevents disease | Transgenic thymic beta-subunit expression abrogates gastritis; thymocytes from transgenic mice fail to transfer disease | Murine, BALB/c thymectomy model | High for causality in mice; translational gap to human unclear |
| PMID:9640252 | Model organism | Supports | CD4 (not CD8) T cells are necessary and sufficient | CD4+ T-cell depletion abolishes gastric infiltrates and autoantibody production in d3Tx BALB/c mice | Murine post-thymectomy model | High internal validity; classic mouse-model result |
| PMID:8759770; PMID:10064084 | Model organism | Supports | H/K-ATPase-reactive CD4 T cells are pathogenic and drive post-thymectomy disease | Identification and fine-specificity mapping of anti-H/K-ATPase CD4 T cells causing gastritis | Murine | High for mechanism; species-specific fine specificity |
| PMID:7517707 | Human clinical / serology | Supports | Alpha and beta subunits are concordant human autoantigens | Human parietal cell autoantibodies target both H/K-ATPase subunits concordantly | Human pernicious anemia / AIG | High — direct human confirmation of the murine target |
| PMID:16214318 (review) | Review | Supports (synthesis) | T-cell repertoire shaping to H/K-ATPase | Synthesizes thymic/peripheral tolerance data into the "bona fide autoantigen" model | Human + mouse | Review-level, orientation only |
| Frontiers Immunol 2026 (comprehensive review); PMC11010983 (2024 clinical review); PMC10378041 (2023) | Review | Supports | Th1/CD4-driven parietal-cell destruction; Fas/perforin cytotoxicity | Synthesizes CD4+ Th1-driven, IFN-γ-mediated, perforin/FasL cytotoxic parietal-cell destruction as core mechanism | Human AIG, general | Review-level, consistent across independent reviews |
| PMID:35911678 / PMC9328118 | Human clinical | Supports/extends | Th17 (not just Th1) contributes | Gastric H/K-ATPase-reactive Th17 cells and elevated serum IL-17A/F, IL-21 in AIG patients | Human AIG | Moderate-high; extends canonical Th1 model, does not refute it |
| PMC2561289 (Th1/Th2/Th17 comparison, mouse) | Model organism | Qualifies | Effector subset determines histopathologic pattern | Th1, Th2, Th17 transfer each produce distinct gastritis patterns and differ in Treg susceptibility | Murine adoptive transfer | Moderate; shows mechanistic heterogeneity within the "CD4 T cell" umbrella |
| PMID:29907148 (IPEX case) | Human clinical, monogenic | Supports | Central Treg/tolerance failure produces AIG | Boy with FOXP3 mutation (IPEX) developed metaplastic atrophic gastritis | Human, monogenic IPEX | Moderate — single case, but mechanistically clean (FOXP3 loss → Treg failure → AIG) |
| PMID:6698825-class APECED reviews | Human clinical, monogenic | Supports (partial) | AIRE loss produces organ-specific autoimmunity including gastric | APECED/AIRE-deficient patients develop anti-parietal-cell/anti-IF antibodies, pernicious anemia; Aire-deficient mice develop gastritis | Human APECED (minority of patients); mouse strain-dependent | Moderate. Gastric autoimmunity is a minority (non-endocrine) manifestation in APECED, and one report noted anti-GIEC (not anti-parietal-cell) antibodies — target antigen not fully consistent |
| PMC4912916 (Treg depletion, Read/Alderuccio-lineage work) | Model organism | Supports | Peripheral Treg loss (not only central tolerance) triggers disease | Transient Treg depletion in adult mice → long-lasting AIG with H/K-ATPase and intrinsic-factor autoantibodies | Murine, adult (not neonatal) | High — shows disease can arise from *peripheral* tolerance breakdown, not only developmental/thymic defects |
| PLOS ONE 2011 (PMC, "Convenient model...without perturbation of regulatory T cells") | Model organism | Qualifies/competing | Disease can occur via polyclonal effector T-cell transfer without any Treg perturbation | Severe AIG induced by polyclonal effector T cells, Treg compartment intact | Murine | Moderate — shows tolerance breakdown is not strictly required; effector-cell dose/activation alone can suffice, complicating a purely "tolerance-defect-primary" narrative |
| PMID:14568977 (Amedei et al., *J Exp Med* 2003); PMID:15242679; PMID:15596126 (D'Elios reviews) | Human clinical + in vitro | **Competing/qualifying** | Molecular mimicry with H. pylori antigens triggers gastric CD4 T-cell autoreactivity | H. pylori-infected AIG patients harbor gastric CD4+ T cells cross-reactive with both H. pylori proteins (9 identified) and H/K-ATPase; cross-reactive peptides drive Th1 proliferation | Human, H. pylori-associated subset | Moderate-high for the immunological cross-reactivity data; causal/initiating role in disease *onset* (vs. epiphenomenon in already-autoimmune stomachs) "remains to be conclusively established" per the same literature |
| PMC11748404; Karger CRG 2023 (PMID:36742095); PMC10292996 | Human clinical, case reports | **Conflicting** | Does eradicating H. pylori resolve or reveal AIG? | Mixed: some patients regress after eradication, others show *rapid progression* of AIG after eradication; histology can remain AIG-consistent despite falling PCA titers | Human, case-report level | Low-moderate — small numbers, contradictory directionality, no controlled cohort resolving causality |
| PMC7699377; PMC5667734; Springer 2025 (neuroendocrine tumor microbiota) | Human clinical, microbiome | Competing/parallel | Non-H. pylori dysbiosis (Streptococcus, Proteobacteria, Fusobacteriota expansion) associates with AIG and persists after H. pylori eradication | Distinct microbial signature in AIG vs. H. pylori-gastritis vs. PPI-induced hypochlorhydria | Human | Low-moderate; associative, mechanism (driver vs. bystander of achlorhydria) unresolved |
| Case series (ICI gastritis; PMC12518205; PMC9286772; PMC8274081) | Human clinical | Supports (proof-of-concept for T-cell sufficiency) | Releasing peripheral immune checkpoints (anti-PD-1/anti-CTLA-4) alone is sufficient to precipitate a gastritis with autoimmune histology | ICI-treated cancer patients develop chronic active gastritis with mucosal changes consistent with an autoimmune process, in the absence of any additional infectious trigger | Human, iatrogenic (checkpoint blockade) | Moderate — strong *conceptual* support that removing peripheral T-cell brakes alone (no new infection) can precipitate gastric autoimmunity, consistent with "self-sustaining, tolerance-defect-driven" model; parietal-cell-antigen specificity of ICI gastritis is not well characterized in the retrieved literature (an explicit gap) |
| Frontiers 2026 review (HLA-DRB1*03:01/04:05, PTPN22, CTLA4) | Review (secondary synthesis) | Supports (weak) | Genetic susceptibility loci overlap with general organ-specific autoimmunity | States specific HLA-DRB1 alleles and PTPN22/CTLA4 involvement in AIG | Human | **Low confidence** — this claim was recovered only from a review-level synthesis; no primary GWAS or case-control association study specific to autoimmune gastritis was found in this search (see Knowledge Gaps) |
| PMC11354099 | Human clinical, diagnostics | Supports (methodological) | H/K-ATPase-specific antibody assays outperform generic parietal-cell antibody assays | Argues for moving diagnosis from PCA (sensitive, non-specific, ~90% sens/low spec) to H/K-ATPase-specific antibody testing; intrinsic-factor antibodies are highly specific (~100%) but low sensitivity (~37%) | Human | Moderate-high, diagnostic-focused, indirectly supports H/K-ATPase as the biologically correct antigen target |

---

## Mechanistic Causal Chain

**Upstream trigger → Loss of self-tolerance → Effector phase → Tissue destruction → Clinical manifestation**

1. **Susceptibility substrate (moderately supported, weakly characterized in AIG specifically):** Genetic background (HLA class II alleles; candidate PTPN22/CTLA4 variants inferred by analogy to other organ-specific autoimmune diseases) plus **incomplete central tolerance** to the H/K-ATPase — alpha subunit is thymically expressed (Aire-independent) and partially purges alpha-reactive clones, but the **beta subunit escapes thymic expression**, leaving beta-reactive T cells as the dominant surviving repertoire (PMID:9272282). *Strong in mice; genetic-association evidence in humans specific to AIG is thin.*

2. **Trigger/initiation (contested — this is the crux of the hypothesis debate):** Two non-mutually-exclusive candidate initiating events:
   - (a) **Primary/spontaneous breakdown of peripheral tolerance** — demonstrated causally in adult mice by transient Treg depletion alone, without any exogenous antigen, yielding durable AIG (PMC4912916), and in monogenic human tolerance disorders (AIRE/APECED, FOXP3/IPEX) where gastric autoimmunity arises as one manifestation of global tolerance failure (PMID:29907148 and APECED literature). ICI-induced gastritis in cancer patients is a clean human "natural experiment" showing that releasing peripheral checkpoints alone, without any new infection, can precipitate gastric autoimmune inflammation.
   - (b) **Infection-triggered mimicry** — H. pylori-elicited CD4+ T cells cross-react with H/K-ATPase epitopes in genetically susceptible individuals, seeding the autoreactive Th1 response (PMID:14568977). This is a *parallel upstream pathway converging on the same effector step*, not obviously excludable by current evidence.
   - The causal chain is therefore **branched at the top**, and the literature does not establish which branch (or what mixture) predominates in a given patient; the "primary, infection-independent" framing in the hypothesis label asserts branch (a) exclusively, which is not what the evidence shows.

3. **Effector phase (strongly supported):** Autoreactive CD4+ T cells (predominantly Th1, IFN-γ-secreting; a Th17/IL-17A/IL-17F/IL-21 axis also documented; Th2-skewed patterns produce distinct histopathology in mice) infiltrate the gastric corpus mucosa, recognize H/K-ATPase alpha/beta subunit epitopes presented on parietal cells or local APCs, and drive cytotoxic destruction via IFN-γ, Fas/FasL, and perforin-mediated pathways (multiple 2023–2025 reviews; PMID:35911678). CD4+CD25+ Treg cells normally suppress this process in a cytokine-independent manner; their functional or numerical failure (whether congenital as in IPEX, or transient as in the adult Treg-depletion model) permits disease.

4. **Tissue destruction and downstream physiology (strongly supported, well-characterized):** Progressive loss of parietal cells (and often chief/zymogenic cells) → loss of acid (HCl) and intrinsic factor secretion → chronic hypochlorhydria/achlorhydria → compensatory G-cell hyperplasia and hypergastrinemia → gastrin-driven ECL-cell hyperplasia via CCK2R signaling → risk of type 1 gastric neuroendocrine tumors (carcinoid) and, via the hyperplasia-dysplasia-neoplasia sequence, gastric adenocarcinoma risk. Intrinsic factor loss produces malabsorptive vitamin B12 deficiency and pernicious anemia.

**Where the chain is strong:** effector CD4-T-cell/H-K-ATPase specificity, cytotoxic mechanism, and the downstream achlorhydria→hypergastrinemia→ECL hyperplasia physiology are all robustly supported by concordant human and mouse data.

**Where the chain is inferred/weak:** (i) the specific human genetic susceptibility architecture (HLA/PTPN22/CTLA4) rests on review-level, not primary, AIG-specific association data in this search; (ii) the relative contribution of central-tolerance failure (thymic) versus peripheral-tolerance failure (Treg dysfunction/depletion) in the typical adult-onset human case is unknown — most causal murine data come from neonatal thymectomy or transgenic/Treg-depletion models that may not represent spontaneous adult human disease onset; (iii) whether/how an infectious trigger (H. pylori or another organism) is required, sufficient, or merely incidental in human disease onset is unresolved and contested by conflicting eradication case reports.

---

## Knowledge Gaps

1. **Human causal proof of central-tolerance-origin hypothesis.** *Scope:* the seed hypothesis's central claim (thymic tolerance breakdown to H/K-ATPase is the primary driver) is demonstrated causally only in mice (thymectomy, TCR-transgenics). *Why it matters:* if peripheral tolerance failure (adult Treg dysfunction, as in PMC4912916) is actually the dominant human route, "primary autoimmunity via central tolerance defect" over-specifies the mechanism. *What was checked:* murine thymectomy/transgenic literature (strong), human monogenic tolerance-defect case reports (supportive but rare/anecdotal — IPEX gastritis is "rarely reported"). *What would resolve it:* longitudinal immune-repertoire/thymic-output studies (e.g., TREC assays, TCR repertoire sequencing) in new-onset adult human AIG patients versus age-matched controls.

2. **Causal role (if any) of H. pylori / microbiome in human disease initiation vs. epiphenomenon.** *Scope:* molecular-mimicry cross-reactivity is demonstrated in vitro/ex vivo (PMID:14568977), but whether H. pylori infection actually *initiates* AIG in previously non-autoimmune stomachs, versus autoimmune destruction independently uncovering/altering a pre-existing H. pylori or dysbiotic microbiome, is unresolved. *Why it matters:* directly determines whether "independent of any persistent infection" in the hypothesis label is defensible. *What was checked:* both directions of case-report literature on H. pylori eradication (some regress, some progress) — genuinely conflicting, not merely absent. *What would resolve it:* prospective cohorts with H. pylori serostatus/genotype documented *before* AIG autoantibody seroconversion; germ-free/gnotobiotic mouse experiments introducing H. pylori into tolerant vs. genetically susceptible backgrounds with longitudinal autoantibody tracking.

3. **Human genetic architecture specific to AIG.** *Scope:* no primary GWAS or case-control study specific to autoimmune gastritis (as opposed to pernicious anemia broadly or other organ-specific autoimmune diseases) was found in this search; the HLA-DRB1*03:01/04:05 and PTPN22/CTLA4 claims trace to a single review-level synthesis. *Why it matters:* the hypothesis implicitly assumes a heritable tolerance-defect susceptibility; without primary genetic data this is unconfirmed for AIG specifically. *What would resolve it:* a dedicated GWAS/immunochip study in AIG cohorts (analogous to what exists for T1D, APS, Hashimoto's), or systematic candidate-gene case-control replication.

4. **Alpha- vs. beta-subunit dominance discrepancy.** *Scope:* the seed hypothesis cites alpha-subunit thymic expression as evidence for tolerance biology, but the same paper's actual conclusion is that thymic tolerance to the *beta* subunit (which is NOT thymically expressed) is what's protective, and forced ectopic beta expression—not natural alpha expression—prevents disease. *Why it matters:* the KB hypothesis snippet should be corrected/qualified to avoid implying alpha-subunit thymic tolerance is protective; it demonstrably fails to prevent disease in these models. *What would resolve it:* re-review of PMID:9272282 and the follow-on transgenic-tolerance papers when updating the KB snippet/explanation.

5. **Whether Treg-independent, polyclonal effector-driven disease (PLOS ONE 2011 model) represents a distinct route or the same pathway downstream of transient tolerance loss.** *Scope:* this model produces severe AIG "without perturbation of regulatory T cells," which is in tension with an obligatory tolerance-defect framing. *Why it matters:* if sufficiently activated/expanded effector T cells can cause disease with intact Tregs, "breakdown of self-tolerance" may not be the only necessary upstream event — sufficient antigen-experienced effector mass might suffice. *What would resolve it:* head-to-head comparison of Treg function/number at disease onset across multiple murine AIG induction models and in newly diagnosed human patients.

6. **ICI-gastritis antigen specificity.** *Scope:* immune-checkpoint-inhibitor-induced gastritis is histologically autoimmune-like, but the retrieved case series/reviews did not report systematic parietal-cell antibody or H/K-ATPase-specific T-cell testing in these patients. *Why it matters:* ICI gastritis is a rare "clean" natural experiment for testing whether removing peripheral checkpoints alone reproduces the canonical antigen-specific mechanism (vs. a distinct, less antigen-specific "ICI-itis" phenomenon). *What would resolve it:* systematic PCA/H-K-ATPase-antibody and gastric-biopsy immunophenotyping study in ICI-gastritis cohorts.

7. **Source-level absence:** no ClinGen, GenCC, or dedicated AIG clinical-trial evidence was found relevant to this specific hypothesis (unsurprising, since AIG is not a monogenic disorder in GenCC's usual sense); this is a genuine absence, not just an unchecked gap, since ClinGen/GenCC searches specifically target monogenic gene-disease curation.

---

## Alternative Models

| Model | Relationship to seed hypothesis | Summary |
|---|---|---|
| **H. pylori molecular-mimicry trigger model** | Competing/upstream-alternative for *initiation*; complementary for effector mechanism | Cross-reactive H. pylori CD4 T-cell epitopes trigger the same H/K-ATPase-directed Th1 response (PMID:14568977, PMID:15242679). Explains geographic/temporal correlation of AIG with H. pylori exposure history and some post-eradication disease trajectories better than a purely endogenous-tolerance-defect model, but does not explain AIG cases with no H. pylori history or monogenic-tolerance-defect cases (IPEX/APECED). |
| **Peripheral Treg-dysfunction model (adult-onset)** | Refinement/parallel mechanism within the same tolerance-defect family, but distinct locus of failure (peripheral vs. central/thymic) | Demonstrated causally by adult transient Treg depletion (PMC4912916) and by the CD4+CD25+ Treg-suppression literature (Springer chapter). May better explain adult-onset sporadic AIG than neonatal-thymectomy-derived central-tolerance models. |
| **Th17/IL-17-IL-21 axis model** | Complementary/extension, not competing | Elevates the mechanistic picture beyond classic Th1/IFN-γ to include Th17 effector cells and serum IL-17/IL-21 signatures (PMID:35911678); may define a distinct inflammatory endotype or disease-severity axis rather than a wholly separate etiology. |
| **Polyautoimmunity / monogenic tolerance-checkpoint failure model (AIRE, FOXP3)** | Special-case confirmation of the seed hypothesis, but with caveats | APECED and IPEX show gastric autoimmunity as *one* manifestation of a broader tolerance-checkpoint failure, supporting a primary-autoimmunity framework, but gastric involvement is a minority phenotype and antigen specificity (anti-parietal-cell vs. anti-GIEC) is inconsistent even within APECED. |
| **Gastric dysbiosis (non-H. pylori microbiome) model** | Parallel/complicating factor, possibly downstream consequence rather than cause | A distinct dysbiotic signature (Streptococcus, Proteobacteria, Fusobacteriota expansion) is associated with AIG and persists post-H. pylori-eradication; direction of causality (dysbiosis as driver of ongoing mucosal inflammation vs. consequence of achlorhydria) is unresolved. |
| **Iatrogenic checkpoint-blockade model (ICI gastritis)** | Supportive analog/proof-of-concept, not a genuine alternative etiology | Demonstrates that peripheral immune-checkpoint loss alone, without infection, can precipitate gastritis with an autoimmune histological signature — mechanistically consistent with (and supportive of) primary-autoimmunity framing, though antigen specificity is unconfirmed. |

None of these alternatives outright *refute* the CD4+ T-cell/H-K-ATPase effector mechanism; they mainly compete over **what initiates the tolerance breakdown** (endogenous developmental/Treg failure vs. exogenous infectious mimicry vs. iatrogenic checkpoint removal) and **which effector subset (Th1 vs. Th17) predominates**.

---

## Discriminating Tests

1. **Prospective birth-cohort or high-risk-family cohort with serial H. pylori serology/genotyping + AIG autoantibody (PCA, IF-Ab, H/K-ATPase-specific Ab) surveillance.** Expected result if primary-autoimmunity model dominates: autoantibody seroconversion occurs independent of H. pylori exposure timing. Expected result if mimicry model dominates: seroconversion clusters temporally after documented H. pylori infection.

2. **TCR repertoire / thymic output (TREC) analysis in new-onset adult AIG patients vs. age/sex-matched controls**, stratified by H. pylori exposure history. Would distinguish central-tolerance-defect signatures (reduced thymic output, oligoclonal autoreactive expansions present from an early age) from peripheral/late-onset Treg-dysfunction signatures (normal thymic output, acquired Treg functional deficits).

3. **Treg functional assays (suppression assays, FOXP3 methylation/Treg stability markers) at AIG diagnosis**, comparing Treg number/function against both the polyclonal-effector-sufficient mouse model (Treg-intact disease) and the Treg-depletion mouse model (Treg-deficient disease) to determine which murine paradigm the typical human case resembles.

4. **Systematic H/K-ATPase-specific T-cell and antibody phenotyping in ICI-gastritis cohorts** (cancer patients on anti-PD-1/anti-CTLA-4 who develop gastritis) vs. ICI patients without gastritis, to test whether checkpoint blockade alone reproduces the canonical antigen-specific signature — a natural human "tolerance-knockout" experiment analogous to the mouse Treg-depletion model.

5. **Germ-free or antibiotic-decontaminated genetically-susceptible mouse strains (e.g., BALB/c neonatal-thymectomy-susceptible) with controlled H. pylori mono-colonization vs. sham**, tracking time-to-autoantibody-seroconversion and histologic severity, to directly test whether infection *accelerates or is required for* disease onset versus a purely spontaneous tolerance-defect trajectory.

6. **Dedicated AIG case-control GWAS/immunochip study** (currently absent per this search) powered to detect HLA and non-HLA (PTPN22, CTLA4, AIRE-pathway) associations specific to autoimmune gastritis, stratified by H. pylori serostatus, to determine whether genetic susceptibility differs between "infection-associated" and "infection-negative" AIG subgroups.

---

## Curation Leads *(require curator verification before use)*

**Candidate evidence references to verify (exact PMID + snippet check required before adding):**
- PMID:9640252 — verify exact abstract snippet on CD4+ (not CD8+) requirement for murine autoimmune gastritis.
- PMID:7517707 — verify snippet on concordant alpha/beta subunit targeting by human parietal-cell autoantibodies (MODEL_ORGANISM vs HUMAN_CLINICAL — likely human sera, so HUMAN_CLINICAL).
- PMID:14568977 (Amedei et al., J Exp Med 2003) — candidate evidence for a **competing/qualifying** `hypothesis_group_id` (H. pylori molecular mimicry trigger) rather than the canonical group; evidence_source HUMAN_CLINICAL/IN_VITRO (mixed paper — split if both human ex vivo T-cell and biochemical cross-reactivity data appear).
- PMID:35911678 — candidate evidence for a Th17-axis refinement node; HUMAN_CLINICAL.
- PMID:29907148 — candidate evidence node for IPEX/FOXP3 polyautoimmunity link to AIG (already partially reflected per hypothesis description — confirm exact quoted snippet from case report abstract before adding).
- **Caution:** do NOT add the HLA-DRB1*03:01/04:05 / PTPN22 / CTLA4 claim from the Frontiers 2026 review without first tracing it to a primary case-control study — this search could not independently verify a primary source for that specific claim.

**Candidate pathophysiology nodes/edges:**
- Node: "Incomplete Central Tolerance to H/K-ATPase Beta Subunit" (upstream of "CD4+ Th1/Th17-Mediated Parietal Cell Destruction") — distinguishing alpha (thymically expressed, partially tolerizing) vs. beta (not thymically expressed, dominant autoantigen) subunit tolerance.
- Competing/parallel node: "H. pylori-Driven Molecular Mimicry Initiation" feeding into the same "CD4+ T-cell-Mediated Parietal Cell Destruction" node — modeled as an alternative upstream trigger under a new or `COMPETING` hypothesis group, not folded into the canonical primary-autoimmunity group.
- Downstream nodes already implied and worth confirming are present: "Achlorhydria/Hypochlorhydria" → "Hypergastrinemia" → "ECL Cell Hyperplasia" → "Type 1 Gastric Neuroendocrine Tumor Risk."

**Candidate ontology terms:**
- Cell types: parietal cell (CL:0000155), gastric ECL/enterochromaffin-like cell (check CL for exact term), CD4+ Th1 cell / CD4+ Th17 cell, CD4+CD25+FOXP3+ regulatory T cell.
- Biological processes: GO term for "T cell mediated cytotoxicity" (Fas/perforin pathway), IFN-gamma production, IL-17 production.
- Genes: `hgnc:` entries for ATP4A, ATP4B, AIRE, FOXP3, PTPN22, CTLA4 (verify lowercase `hgnc:` per repo convention).

**Candidate subtype/status changes:**
- Consider splitting the current single CANONICAL hypothesis into (a) a CANONICAL "effector mechanism" hypothesis (CD4+ T-cell/H-K-ATPase-directed destruction — very strongly supported) and (b) a separate, lower-confidence "etiological trigger" hypothesis layer distinguishing central-tolerance-defect vs. H. pylori-mimicry vs. peripheral-Treg-dysfunction origins, each with its own evidence and status (the mimicry model probably warrants `EMERGING` or `COMPETING`, not folded silently into the canonical primary-autoimmunity narrative).
- Revise the hypothesis `description`/`explanation` text to correct the alpha/beta-subunit tolerance nuance described above (the cited paper supports beta-subunit escape from thymic tolerance, not alpha-subunit-mediated protection).

**Candidate discussion/knowledge-gap prompts:**
- `KNOWLEDGE_GAP`: "Is central (thymic) or peripheral (Treg) tolerance failure the dominant route to sporadic adult-onset human autoimmune gastritis, given that murine causal evidence comes almost entirely from neonatal thymectomy or artificial Treg depletion?"
- `KNOWLEDGE_GAP`: "Does H. pylori infection initiate autoimmune gastritis via molecular mimicry in a subset of patients, or does it merely coexist with/complicate an independently arising autoimmune process? Conflicting eradication case reports (regression vs. rapid progression) leave this unresolved."
- `HUMAN_MODEL_MISMATCH`: "Neonatal-thymectomy and TCR-transgenic mouse models of autoimmune gastritis reproduce the H/K-ATPase-specific CD4 T-cell effector mechanism, but their induction paradigms (neonatal thymic ablation, transgenic TCR fixation) do not obviously model spontaneous adult-onset human disease; fidelity of these models to human disease timing/onset is unconfirmed." Proposed experiments: TREC/thymic-output and Treg-functional profiling in new-onset adult human AIG, benchmarked against both mouse paradigms.

**Discriminating artifacts** (for curator use — mechanistic diagram / evidence table above already provided in this report; recommend adding as supplementary review-level citation material rather than as a single evidence item, since this is a synthesis rather than a primary source).