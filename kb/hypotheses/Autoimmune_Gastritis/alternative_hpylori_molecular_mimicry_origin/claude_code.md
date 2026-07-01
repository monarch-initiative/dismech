---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T14:08:38.153058'
end_time: '2026-07-01T14:13:03.864853'
duration_seconds: 265.71
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Autoimmune Gastritis
  category: Complex
  hypothesis_group_id: alternative_hpylori_molecular_mimicry_origin
  hypothesis_label: Alternative H. pylori Molecular-Mimicry ("Hit-and-Run") Origin
  hypothesis_status: ALTERNATIVE
  hypothesis_yaml: "hypothesis_group_id: alternative_hpylori_molecular_mimicry_origin\n\
    hypothesis_label: Alternative H. pylori Molecular-Mimicry (\"Hit-and-Run\") Origin\n\
    status: ALTERNATIVE\ndescription: Autoimmune gastritis is initiated by Helicobacter\
    \ pylori infection via molecular mimicry\n  between H. pylori antigens and the\
    \ gastric H+/K+ ATPase, generating cross-reactive T- and B-cell responses\n  that,\
    \ through epitope spreading and bystander activation in a genetically susceptible\
    \ host, become self-perpetuating\n  autoimmunity and persist after the organism\
    \ is cleared (established AIG is frequently H. pylori-negative).\n  A corollary\
    \ is that a subset of cases are reversible with early eradication. Causation in\
    \ humans remains\n  unproven and is the basis of a knowledge-gap discussion.\n\
    evidence:\n- reference: PMID:21174235\n  reference_title: Cutting edge issues\
    \ in autoimmune gastritis.\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: a role for Helicobacter pylori as an infective trigger through molecular\
    \ mimicry\n  explanation: States H. pylori as a candidate infective trigger of\
    \ autoimmune gastritis via molecular\n    mimicry.\n- reference: PMID:42254085\n\
    \  reference_title: 'Pernicious Anemia and Helicobacter pylori Infection: What\
    \ a Hematologist Needs to\n    Know?'\n  supports: PARTIAL\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: Rapid eradication of H. pylori can significantly\
    \ improve hematologic parameters and prevent\n    the progression of autoimmune\
    \ gastritis.\n  explanation: A reversible, H. pylori-attributable presentation\
    \ is consistent with an infection-triggered\n    origin in a subset of cases."
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
  web_search_requests: 15
  num_turns: 20
  total_cost_usd: 1.9019688000000001
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
- **Hypothesis ID:** alternative_hpylori_molecular_mimicry_origin
- **Hypothesis Label:** Alternative H. pylori Molecular-Mimicry ("Hit-and-Run") Origin
- **Status in KB:** ALTERNATIVE

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: alternative_hpylori_molecular_mimicry_origin
hypothesis_label: Alternative H. pylori Molecular-Mimicry ("Hit-and-Run") Origin
status: ALTERNATIVE
description: Autoimmune gastritis is initiated by Helicobacter pylori infection via molecular mimicry
  between H. pylori antigens and the gastric H+/K+ ATPase, generating cross-reactive T- and B-cell responses
  that, through epitope spreading and bystander activation in a genetically susceptible host, become self-perpetuating
  autoimmunity and persist after the organism is cleared (established AIG is frequently H. pylori-negative).
  A corollary is that a subset of cases are reversible with early eradication. Causation in humans remains
  unproven and is the basis of a knowledge-gap discussion.
evidence:
- reference: PMID:21174235
  reference_title: Cutting edge issues in autoimmune gastritis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: a role for Helicobacter pylori as an infective trigger through molecular mimicry
  explanation: States H. pylori as a candidate infective trigger of autoimmune gastritis via molecular
    mimicry.
- reference: PMID:42254085
  reference_title: 'Pernicious Anemia and Helicobacter pylori Infection: What a Hematologist Needs to
    Know?'
  supports: PARTIAL
  evidence_source: HUMAN_CLINICAL
  snippet: Rapid eradication of H. pylori can significantly improve hematologic parameters and prevent
    the progression of autoimmune gastritis.
  explanation: A reversible, H. pylori-attributable presentation is consistent with an infection-triggered
    origin in a subset of cases.
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

# Mechanistic Hypothesis Search Report: H. pylori Molecular-Mimicry ("Hit-and-Run") Origin of Autoimmune Gastritis

## Executive Judgment

**Verdict: Partially supported / unresolved — a biologically plausible but causally unproven "trigger" hypothesis, most defensible as a subset mechanism rather than a general explanation.**

The core immunological claim — that H. pylori-reactive CD4+ T cells and antibodies can cross-react with gastric H+/K+-ATPase — is well-documented at the cellular and serological level in humans (D'Elios/Amedei 2003, PMID:14568977; Negrini 1996, PMID:8780570) and is mechanistically coherent (LPS Lewis-antigen mimicry, urease β-subunit homology, cross-reactive CD4+ T-cell clones against nine H. pylori proteins). However, three major weaknesses prevent the hypothesis from being considered established causation:

1. **No consistent case-control association** between H. pylori seropositivity/current infection and autoimmune gastritis (AIG) or anti-parietal cell antibody (APCA) positivity across studies; some studies show association, others show none (PMID:21796548; PMC10598509/PMID:37885562 — no poolable OR could even be calculated due to heterogeneity).
2. **AIG occurs and progresses in patients with no current or documented past H. pylori infection**, including in pediatric cases with no epidemiologic infection risk factors, and animal Lewis-antigen mimicry findings do not replicate in human autoantibody specificity (autoantibodies in infected humans target H,K-ATPase protein epitopes, not the Lewis-glycan mimics seen in the pig model) — a direct species-level failure of the strong version of the mimicry story.
3. **Eradication trials give mixed results**: some cohorts show reduced APCA titers and histological improvement after cure (Karger 2002 "Healing of Active, Non-Atrophic Autoimmune Gastritis by H. pylori Eradication"; Müller et al., ~80% resolution of active gastritis in non-atrophic AIG), but other case reports document new-onset AIG or accelerating atrophy in the 1–3 years *after* successful eradication (Ihara et al. 2023), which is difficult to reconcile with a simple hit-and-run model unless one invokes a already-primed autoimmune process unmasked by loss of H. pylori's local immunomodulatory/competitive effects.

The hypothesis is best read as **one plausible initiating/potentiating trigger in a genetically susceptible subset of patients with early, non-atrophic, still-inflamed corpus mucosa**, not as the universal or necessary cause of AIG — consistent with the KB's own framing ("causation in humans remains unproven... basis of a knowledge-gap discussion").

---

## Evidence Matrix

| Citation | Evidence type | Supports/Refutes/Qualifies | Mechanistic claim tested | Key finding | Context/Subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| D'Elios, Amedei et al., *J Exp Med* 2003 (PMID:14568977) | Human clinical (ex vivo T-cell clones) | **SUPPORTS** | CD4+ T-cell cross-reactivity between H. pylori antigens and H,K-ATPase | Gastric CD4+ T-cell clones from H. pylori-infected AIG patients proliferated to both H,K-ATPase and H. pylori lysate; cross-reactive epitopes mapped to 9 H. pylori proteins; cross-reactive peptides drove Th1 polarization (IFN-γ) | Adult, H. pylori-positive AIG (mixed infection/autoimmunity) | Moderate-high for the immunological phenomenon; small clone/patient numbers; correlative, not interventional |
| Negrini et al., *Gastroenterology* 1996 (PMID:8780570) | Human clinical + monoclonal Ab | **SUPPORTS** | Antigenic cross-reactivity of anti-H. pylori antibodies with gastric mucosal antigens (incl. H,K-ATPase) | Majority of H. pylori-infected patients had autoantibodies cross-reacting with gastric mucosal antigens; earlier foundational mimicry evidence | Adult chronic gastritis cohort | Moderate; early study, serology-based, predates modern H,K-ATPase ELISA standardization |
| Faller/Negrini pig model (Lewis-antigen LPS mimicry studies, e.g. PMC174033, *Infect Immun* 1996) | Model organism (pig) + human comparison | **QUALIFIES/PARTIALLY REFUTES** | Lewis-antigen (LPS) mimicry as the operative epitope | In orally infected pigs, cross-reactive autoantibodies targeted Lewis-glycan epitopes on H,K-ATPase β-chain; **in human patients, autoantibodies instead target protein epitopes not generated through Lewis mimicry** | Cross-species comparison | Important — shows the *mechanism* of mimicry differs between the animal proof-of-concept and human disease; limits generalization of the Lewis-mimicry sub-hypothesis to humans |
| Toh, Chan, Kyaw, Alderuccio, *Clin Rev Allergy Immunol* 2012 (PMID:21174235) — seed citation | Review (human clinical synthesis) | **SUPPORTS (review-level)** | H. pylori as candidate infective trigger via molecular mimicry | States H. pylori as a candidate trigger through molecular mimicry among epidemiology, immunogenetics, immunopathogenesis topics reviewed | General AIG review | Review-level orientation; not primary data; frequently cited as the "textbook" mimicry statement |
| Systematic review, pernicious anemia & H. pylori/APCA/AIFA, PMID:37885562 (2023, PMC10598509) | Review of 13 human clinical studies | **QUALIFIES/WEAKENS** | Population-level association between H. pylori infection and APCA/AIFA | No poolable odds ratio could be derived; individual studies range from 9.9% APCA-positive among H. pylori+ patients to 58% H. pylori+ among APCA+ subjects — highly heterogeneous; authors explicitly urge caution on causal interpretation | Pernicious anemia cohorts, mixed populations | Low-moderate; heterogeneity and study-design disparities are the review's own stated limitation |
| Bergman et al. / follow-up serology studies (cited via secondary review) | Human clinical, longitudinal | **REFUTES "hit" step at population level in some cohorts** | Whether cure of infection abolishes APCA | APCA did not decrease after H. pylori cure over 1-year follow-up in a subset; one subject developed APCA over 32 years while H. pylori-negative at both baseline and endpoint | Longitudinal general population cohort | Moderate; small subsets, long follow-up but limited mechanistic granularity |
| Müller et al. (cited via MDPI 2025 review, PMID for review 26:16:7737) | Human clinical, longitudinal (39.5-month follow-up) | **SUPPORTS "reversibility" corollary** | Eradication improves early, non-atrophic AIG | ~80% resolution of active gastritis in non-atrophic AIG patients after H. pylori eradication | Early/non-atrophic AIG subtype | Moderate; single-cohort, not RCT; selection toward earlier-stage disease likely inflates apparent benefit |
| Karger *Digestion* 2002, "Healing of Active, Non-Atrophic Autoimmune Gastritis by H. pylori Eradication" | Human clinical, case series | **SUPPORTS** | Eradication reverses active AIG in non-atrophic stage | Documented histological healing and antibody decline post-eradication | Non-atrophic AIG | Moderate; small case series |
| PMID:42254085, "Pernicious Anemia and H. pylori Infection: What a Hematologist Needs to Know?" — seed citation | Human clinical (review/clinical synthesis) | **PARTIAL** | Reversibility of AIG-associated hematologic disease with eradication | "Rapid eradication... can significantly improve hematologic parameters and prevent progression of autoimmune gastritis" | Pernicious anemia subset | Moderate; review-level, treat as orientation pending primary-source verification (see Curation Leads) |
| Ihara et al. 2023 (cited via MDPI review) | Human clinical, case report | **REFUTES/COMPLICATES reversibility corollary** | Whether eradication halts/reverses progression | New AIG onset with rapid gastric body atrophy within 3 years *after* successful H. pylori eradication | Case report, adult | Low (single case) but mechanistically important counter-example |
| Meta-analysis, H. pylori & autoimmune diseases incl. AIG, *Ann Saudi Med*/ScienceDirect (S1684118220302097) | Human clinical, meta-analysis (43 studies, ~5052 patients) | **SUPPORTS at strain level, qualifies overall** | Whether cagA+ H. pylori strains specifically associate with autoimmune disease including AIG | CagA+ strain infection significantly associated with autoimmune disease development across pooled autoimmune cohorts (SLE, RA, AIG, AIP) | Pooled autoimmune cohort, not AIG-specific subgroup analysis reported in retrieved excerpt | Moderate; pooling across unrelated autoimmune diseases weakens AIG-specific inference |
| Population-based study, Germany (AACR CEBP, 22(5):821) | Human clinical, large population cohort | **QUALIFIES** | Population co-occurrence of APCA and H. pylori serology | Documents co-occurrence patterns but conflicting relationship strength across strata; some studies in same literature report *no* relation between H. pylori and APCA | General population, elderly | Moderate; cross-sectional, cannot establish temporality |
| Amedei et al., PMID:15763992, "Molecular specificity and functional properties of autoreactive T-cell response in human gastric autoimmunity" | Human clinical (T-cell) | **SUPPORTS/extends** | Autoreactive T-cell epitope specificity (α vs β chain of H,K-ATPase) | Of 13 cross-reactive clones, 11 recognized epitopes in the ATPase α-chain, 2 in the β-chain — refines epitope map from the 2003 JEM paper | Adult AIG/H. pylori co-infected | Moderate; small numbers, single-center |
| Th1/Th2/Th17 mouse gastritis model, PMID:18641328 (PMC2561289) | Model organism (mouse, adoptive transfer) | **Supports downstream mechanism, not mimicry origin per se** | Which effector T-cell subset drives parietal-cell loss/atrophy | Th17-polarized transfer produced most destructive gastritis (eosinophilic infiltrate, high IgE); Th1 transfer also pathogenic via Fas/perforin-granzyme cytotoxicity | Mouse H,K-ATPase-immunization model (not H. pylori-triggered) | High for downstream effector mechanism; does **not** test the infectious trigger, only the self-antigen-driven arm — relevant to distinguishing "what perpetuates" from "what initiates" |
| H. felis mouse model (PMID:16234583 and related) | Model organism (mouse) | **Supports role of infection in initiating a Th1 gastritis, ambiguous on autoimmunity vs. anti-bacterial response** | Whether Helicobacter infection alone (without demonstrated mimicry) produces gastritis via adaptive T-cell response | H. felis-specific Th1 spleen-cell adoptive transfer enhances gastric inflammation in naive recipients; disease severity tracks T-cell phenotype, not demonstrated autoantigen cross-reactivity | Mouse | Moderate; this classic model shows infection-driven, CD4-dependent gastritis but does not itself establish molecular mimicry — it is compatible with either mimicry or non-mimicry (bystander) mechanisms |

---

## Mechanistic Causal Chain

**Upstream trigger → intermediate steps → clinical manifestation, with confidence annotated:**

1. **H. pylori colonization of gastric mucosa** (well established, epidemiologically common) →
2. **Presentation of H. pylori antigens (urease β-subunit, other of ≥9 cross-reactive proteins, LPS Lewis x/y glycans) to gastric mucosal CD4+ T cells and B cells** (well established for antigen presentation generally; the *specific* cross-reactive antigen set is more provisional — mapped mainly by D'Elios/Amedei in a small patient series) →
3. **Generation of H. pylori-specific Th1 (and Th17) responses that cross-react with H,K-ATPase α/β subunits (molecular mimicry) in a genetically susceptible host (HLA-DRB1*03/*04, PTPN22, AIRE, CTLA4, IL10 risk variants)** — *moderately supported at the cellular level in a small number of co-infected AIG patients; the genetic-susceptibility gating step is supported independently by GWAS/HLA data but has not been directly linked mechanistically to the mimicry step in the same patients* →
4. **Epitope spreading and bystander activation broaden the autoreactive repertoire beyond the original mimicry epitope, engaging additional Th1/Th17 clones and autoantibody specificities (APCA, anti-IF)** — *plausible and consistent with general epitope-spreading biology in organ-specific autoimmunity (e.g., bullous disease literature), but not directly demonstrated with longitudinal single-patient epitope mapping in AIG* →
5. **Self-perpetuating autoimmune destruction of parietal cells (Fas/FasL, perforin/granzyme B cytotoxicity, Th17-driven eosinophilic/IgE-associated tissue damage) independent of continued H. pylori presence ("hit-and-run")** — *supported by the mouse Th1/Th17 adoptive-transfer models showing self-antigen-driven pathology without ongoing infection, and by the clinical observation that established AIG is frequently H. pylori-negative; but this is also equally consistent with AIG arising from a wholly independent, infection-unrelated autoimmune process that simply happens to co-occur with prior/incidental H. pylori exposure (confounding by high population H. pylori seroprevalence)* →
6. **Progressive oxyntic atrophy, hypochlorhydria, hypergastrinemia, ECL-cell hyperplasia, loss of intrinsic factor → pernicious anemia / vitamin B12 deficiency** (well established, robust natural history literature) →
7. **Corollary: early eradication reverses the process in a subset (still-inflamed, non-atrophic mucosa) but not in established atrophic disease** — *supported by several case series (Müller et al.; Karger 2002) but directly contradicted by other case reports of new-onset/accelerating AIG post-eradication (Ihara 2023), suggesting the "reversibility window," if real, is narrow and stage-dependent, or that eradication timing coincides with — rather than causes — natural fluctuation.*

**Where the chain is strongest:** step 1→2 (colonization/antigen exposure) and the downstream self-antigen-driven effector mechanism (step 5→6) are both independently well supported.

**Where the chain is weakest / most inferred:** the specific mimicry-epitope link (step 3) rests on a small number of patient-derived T-cell clones from one research group's series; the transition from "cross-reactive clone exists" to "this is what actually initiated disease in vivo" is not demonstrated by any interventional or fate-mapping experiment. Step 4 (epitope spreading) is asserted by analogy to other autoimmune diseases rather than directly traced in AIG. Step 7 (reversibility) is contradicted in a nontrivial minority of reported cases.

---

## Knowledge Gaps

1. **No direct in vivo demonstration that mimicry-epitope-specific T cells are the *initiating* clone population, as opposed to one of many T-cell responses recruited secondarily.** Scope: causal step 3. Why it matters: without this, the hypothesis cannot be distinguished from "H. pylori-driven chronic inflammation nonspecifically unmasks/accelerates a pre-existing autoimmune predisposition" (bystander activation without true mimicry). What was checked: primary T-cell clone papers (D'Elios/Amedei 2003, 2005) — these are cross-sectional, ex vivo. What would resolve it: longitudinal single-cell TCR/epitope tracking from infection onset through seroconversion to APCA/AIFA positivity in a prospective human cohort, or a humanized mouse model with fate-mapped H. pylori-epitope-specific TCR transgenics followed for autoimmune outcome after infection clearance.

2. **Population-level case-control/seroprevalence data are inconsistent** (some studies show association, several show none, and the largest recent systematic review could not even pool an effect estimate, PMID:37885562). Scope: whether H. pylori infection is even statistically enriched in AIG/pernicious anemia versus background. Why it matters: a necessary (though not sufficient) condition for a general causal role is a robust epidemiological association; its absence in several well-conducted studies is a direct qualifier on hypothesis strength. What was checked: the 2023 systematic review (13 studies) and the German population-based cohort. What would resolve it: a large, prospectively followed, geographically diverse cohort with standardized modern serology (H,K-ATPase ELISA, not older APCA immunofluorescence) and H. pylori status determined by both serology (to capture past infection) and stool antigen/biopsy (current infection), stratified by cagA status and country-level H. pylori prevalence (to control confounding by exposure base rates).

3. **The mechanistic mimicry epitope demonstrated in animal models (Lewis-antigen glycan mimicry) does not match the epitope specificity found in human patients (protein epitopes, not glycan).** Scope: cross-species translational validity — this is a `HUMAN_MODEL_MISMATCH`-type gap, not a simple absence of evidence. Why it matters: it means the strongest mechanistic proof-of-concept (pig model, direct pathogenic anti-Lewis monoclonal antibody causing histological gastritis) may not be the operative mechanism in human disease at all, and the "true" human-relevant epitope set (9 H. pylori proteins, D'Elios/Amedei) has not been shown to be pathogenic when introduced into an animal model. What was checked: comparative pig-vs-human antibody specificity literature (PMC174033 and related). What would resolve it: transfer of the *human*-identified cross-reactive T-cell epitopes (not the Lewis-glycan epitopes) into a relevant animal model to test whether they alone are sufficient to cause gastritis, closing the loop the pig model started with the wrong epitope.

4. **Reversibility with eradication is contradicted by post-eradication AIG onset/acceleration cases (Ihara 2023) and by longitudinal cohorts where APCA does not fall after cure.** Scope: the "reversible in a subset" corollary. Why it matters: this corollary is central to the hypothesis's clinical relevance (it is the actionable claim); if unmasking/accelerating cases are as common as healing cases, the corollary needs major qualification by disease stage. What was checked: case-series/case-report literature on both sides. What would resolve it: a prospective randomized or at least matched-cohort eradication trial in early, biopsy-confirmed non-atrophic AIG with H. pylori co-infection, with pre-specified histological and serological (APCA/AIFA titer, gastrin-17, pepsinogen I/II ratio) endpoints at 1, 3, and 5 years — none appears to exist yet (no relevant registered RCT was identified beyond the unrelated betaine-HCl hypergastrinemia trial, NCT06272500, which does not test eradication-as-treatment).

5. **No genetic-epidemiology study has jointly tested whether HLA-DRB1*03/*04, PTPN22, or AIRE risk genotypes modify the effect of H. pylori exposure on AIG risk (gene-environment interaction).** Scope: the "genetically susceptible host" clause of the hypothesis. Why it matters: without a demonstrated interaction term, "genetic susceptibility" is asserted rather than tested as a moderator of the infectious trigger specifically (as opposed to being an independent, infection-unrelated risk factor, which the pernicious-anemia GWAS data — PTPN22 rs6679677, AIRE rs74203920, HLA-DR15 — are equally consistent with). What was checked: HLA/GWAS literature (pernicious anemia GWAS, AIRE/APECED literature) and the mimicry T-cell literature — these two literatures have not been cross-referenced in the same patient cohort. What would resolve it: a cohort stratified by HLA-DRB1*03/*04 and PTPN22 genotype, comparing AIG incidence/severity between H. pylori-exposed and -unexposed subgroups to test for a statistical interaction, not just two independent main effects.

6. **No dataset/source found in this search that directly disambiguates NEC-style confusion in this literature** (i.e., whether "autoimmune gastritis" cohorts in some older mimicry papers included corpus-predominant H. pylori multifocal atrophic gastritis (environmental/type B) rather than true immune-mediated AIG). This is a source-level gap worth flagging for curator follow-up, since some historical seroprevalence studies predate the H,K-ATPase-antibody-based diagnostic refinement (PMC11354099) and may have misclassified overlapping gastritis phenotypes.

---

## Alternative Models

| Model | Relationship to seed hypothesis | Summary |
|---|---|---|
| **Primary, infection-independent autoimmune predisposition** (HLA-DRB1*03/*04, PTPN22, AIRE, CTLA4, IL10 polymorphisms; APECED/AIRE-deficiency gastritis) driving intrinsic loss of tolerance to H,K-ATPase | **Competing/alternative** — the mainline (presumably canonical, non-ALTERNATIVE status in the KB) hypothesis for AIG; explains H. pylori-negative and pediatric AIG cases that molecular mimicry cannot | Genetic susceptibility alone, without any specific infectious trigger required, better explains cases with no infection history and the co-occurrence of AIG with other organ-specific autoimmune diseases (autoimmune thyroiditis, T1DM, vitiligo) in the same patients/families (autoimmune polyendocrine syndrome pattern) |
| **Non-specific bystander/inflammation model (no true mimicry)** — chronic H. pylori-driven gastric inflammation nonspecifically activates and expands pre-existing low-affinity autoreactive T/B cell clones via cytokine milieu and tissue damage, without requiring structural antigen similarity | **Parallel/competing mechanism**, mechanistically distinct from mimicry though clinically hard to distinguish | Cusick/Libbey/Fujinami (PMID:22095454) explicitly flag that structural relatedness does not fully explain T-cell activation in several molecular-mimicry-invoked diseases and propose dual-TCR-expressing T cells (reactive to both self and microbial antigen without true cross-reactive recognition of a single TCR) as an alternative explanation for the same clinical observation of "infection co-occurring with autoimmunity" |
| **Lewis-glycan LPS mimicry (a variant/sub-hypothesis)** | **Nested alternative within the mimicry family**, but mechanistically distinct from the protein-epitope mimicry in the seed hypothesis | Supported in the pig model (direct pathogenicity of anti-Lewis monoclonal antibody) but not replicated as the human autoantibody target — likely a distinct or minor contributor in humans, if any |
| **Non-atrophic H. pylori gastritis as protective against progression to atrophy in some contexts** ("H. pylori infection can stop atrophic gastritis from developing by causing antral inflammation," per one retrieved source) | **Opposing/inverse relationship**, not a downstream consequence — suggests context-dependent (topography-dependent: antral vs. corpus-predominant) effects of infection | If corroborated, this would argue against a simple linear "infection → autoimmunity" model and toward a more complex topographic/immunologic balance model |
| **Environmental "multifocal atrophic gastritis" (type B/H. pylori-driven, non-autoimmune) as a phenocopy** | **Confounder/mimic**, not a true alternative mechanism for AIG itself, but a diagnostic-overlap issue relevant to the epidemiological data | Explains why some older seroprevalence studies may show apparent "H. pylori-AIG association" that is actually misclassification between two distinct atrophic gastritis entities |
| **AIRE-deficiency/APECED-type central tolerance failure model** | **Upstream cause, largely independent of infection** | Mouse AIRE-knockout and human APECED literature show gastric autoimmunity arising from thymic tolerance failure with no infectious trigger required — a genuinely infection-independent route to the same clinical endpoint |

---

## Discriminating Tests

1. **Prospective, HLA/PTPN22/AIRE-genotyped birth or adolescent cohort study** tracking incident H. pylori infection, seroconversion to H,K-ATPase autoantibodies, and gastric histology over 10–20 years. Stratify by genotype to directly test the gene-environment interaction term (Gap 5). Expected result if the hypothesis is correct: infection-exposed high-risk-genotype carriers show markedly higher incident APCA/AIFA seroconversion than infection-unexposed high-risk carriers or infection-exposed low-risk carriers.

2. **Epitope-specific longitudinal TCR/BCR repertoire sequencing** in newly H. pylori-infected individuals (e.g., from an eradication/re-infection natural-history cohort or a controlled human infection model, if ethically feasible with attenuated strains) tracking whether H,K-ATPase-cross-reactive clones identified at baseline expand and persist after clearance (true hit-and-run signature) versus contract with the bacterial antigen (dependent, non-autonomous response).

3. **Human-epitope-based animal model**: immunize mice/pigs with the specific D'Elios/Amedei-identified H. pylori peptides (rather than whole bacterium or LPS) and test whether this alone is sufficient to generate H,K-ATPase-reactive T cells and gastritis, resolving the human/animal epitope-mismatch gap (Gap 3) directly.

4. **Stage-stratified, adequately powered eradication RCT** in biopsy-confirmed early/non-atrophic, H. pylori-co-infected AIG (excluding overtly atrophic disease), with pre-registered co-primary endpoints (histological corpus inflammation score, APCA/AIFA titer, pepsinogen I/II ratio, gastrin-17) at 12, 36, and 60 months, powered to detect both improvement and the "unmasking/acceleration" signal seen in case reports (Gap 4). This is the single most decisive experiment not yet identified in the literature search.

5. **Multi-omics comparison of H. pylori-positive vs. H. pylori-negative AIG** (transcriptomic/TCR-seq of gastric mucosal infiltrates) to test whether the two groups converge on the same final effector phenotype (Th1/Th17, cytotoxic) — if so, this argues H. pylori is one of several equivalent triggers converging on a common autoimmune pathway (consistent with hit-and-run as *a* trigger, not *the* trigger), rather than a unique upstream driver.

6. **Re-analysis of existing GWAS/biobank data** (e.g., UK Biobank, FinnGen) cross-referencing H. pylori serology (where available) with incident pernicious anemia/AIG diagnosis codes and HLA-DR15/DRB1*03/*04 genotype, as a lower-cost interim test of Gap 5 before a de novo prospective cohort.

---

## Curation Leads

*(All require curator verification before entry into the KB — flagged per dismech SOP; PMIDs/snippets below are leads, not yet fetched/validated via `just fetch-reference`.)*

**Candidate evidence references to fetch and verify (`just fetch-reference PMID:XXXX`):**
- `PMID:14568977` — D'Elios et al., *J Exp Med* 2003, "Molecular mimicry between Helicobacter pylori antigens and H+,K+-adenosine triphosphatase in human gastric autoimmunity." Candidate snippet to verify against abstract: language describing cross-reactive gastric CD4+ T-cell clones and the 9 H. pylori protein epitopes. **SUPPORT**, HUMAN_CLINICAL (T-cell/ex vivo — note: technically in vitro assay on human-derived cells; classify per dismech rules as HUMAN_CLINICAL if patient-derived primary cells studied ex vivo, or IN_VITRO if the analytic focus is the cell-culture assay — curator should apply the dismech evidence_source decision rule carefully here).
- `PMID:8780570` — Negrini et al., *Gastroenterology* 1996, "Antigenic mimicry between Helicobacter pylori and gastric mucosa in the pathogenesis of body atrophic gastritis." Candidate for foundational **SUPPORT** evidence of antibody cross-reactivity.
- `PMID:21796548` — "Is there a relationship between Helicobacter pylori and gastric autoimmunity?" — candidate **REFUTE/PARTIAL** evidence documenting inconsistent association.
- `PMID:37885562` — systematic review (13 studies) on H. pylori and anti-IF/anti-PCA antibodies in pernicious anemia — candidate **PARTIAL/qualifying** evidence citing heterogeneity and lack of poolable effect estimate; useful direct citation for the "causation in humans remains unproven" clause already in the KB description.
- `PMID:22095454` — Cusick, Libbey, Fujinami, "Molecular mimicry as a mechanism of autoimmune disease" — candidate general **QUALIFY** evidence for the knowledge-gap discussion, supporting a methodological caveat (dual-TCR alternative explanation) about molecular mimicry claims generally.
- The seed hypothesis's `PMID:42254085` should be independently re-verified on PubMed before further use, given its unusually high numeric value for the stated corpus vintage — standard NEC/hallucination preflight applies (fetch and confirm title/journal/author match before citing further).

**Candidate pathophysiology nodes/edges:**
- A node such as "H. pylori Antigen–H,K-ATPase Cross-Reactive CD4+ T-Cell Priming" upstream of the existing autoimmune-gastritis causal chain, with `modifier: INCREASED` on Th1/Th17 activation, sourced to PMID:14568977.
- A parallel/alternative node "Lewis-Antigen LPS Glycan Mimicry (animal-model-restricted)" explicitly flagged with a `HUMAN_MODEL_MISMATCH` discussion, since the pig-model epitope specificity does not match the human autoantibody epitope specificity (per PMC174033-derived findings) — this is a strong candidate for the `kind: HUMAN_MODEL_MISMATCH` discussion type described in CLAUDE.md, with `prompt`: "Does the Lewis-glycan mimicry mechanism demonstrated in the porcine H. pylori model operate in human autoimmune gastritis, given that human autoantibodies target protein rather than glycan epitopes of H,K-ATPase?"

**Candidate ontology terms:**
- Cell types: `CL:0000980` (plasmablast) or relevant B-cell/T-cell CL terms for cross-reactive CD4+ Th1/Th17 clones (verify exact CL ID/label via OAK before use); parietal cell `CL:0000155` (verify label).
- Biological processes: GO terms for "molecular mimicry"-adjacent processes are limited in GO; consider `GO:0002443` (adaptive immune response) or a more specific T-cell activation term — verify via `runoak -i sqlite:obo:go search`.
- Genes: `hgnc:` terms for `ATP4A` and `ATP4B` (H,K-ATPase subunits) if not already present in the entry; `PTPN22`, `AIRE`, `CTLA4`, `IL10` as HGNC-bound genetic-susceptibility descriptors — verify HGNC IDs before adding.

**Candidate subtype/status considerations:**
- Consider whether the KB should scope this hypothesis's `status: ALTERNATIVE` label with an explicit subtype qualifier (e.g., restricting strongest applicability to "early/non-atrophic, H. pylori-co-infected AIG" rather than AIG broadly), given that the literature most strongly supports the trigger/reversibility narrative in that stage-restricted subgroup and most strongly contradicts a general/necessary role.

**Candidate knowledge-gap / discussion prompts:**
- `kind: KNOWLEDGE_GAP`: "No prospective gene (HLA-DRB1*03/*04, PTPN22, AIRE) × H. pylori-exposure interaction study has been conducted to test whether genetic susceptibility specifically moderates the infectious-trigger step, as opposed to acting as an independent risk factor for AIG."
- `kind: KNOWLEDGE_GAP`: "No adequately powered, stage-stratified RCT of H. pylori eradication in early/non-atrophic AIG exists; current evidence for the reversibility corollary is limited to small case series and is directly contradicted by case reports of post-eradication AIG onset/acceleration."
- `kind: HUMAN_MODEL_MISMATCH`: as specified above, for the Lewis-antigen porcine model vs. human autoantibody epitope specificity mismatch.

---

**Search coverage note:** This report is based on a targeted set of ~14 web searches and 3 full-document fetches (MDPI 2025 review, PMC11899966 2024/2025 review, PMC10598509 2023 systematic review) covering primary mimicry literature (D'Elios/Amedei, Negrini/Faller), animal models (H. felis, Th1/Th17 adoptive transfer), genetic-susceptibility literature (HLA, PTPN22, AIRE GWAS), and reversibility/eradication case literature. It did not include a full PubMed API systematic search, ClinicalTrials.gov registry search beyond the one incidentally retrieved trial (NCT06272500, unrelated to eradication), or direct verification of every PMID against cached abstracts — those steps are explicitly deferred to the curator per the Curation Leads section and the dismech reference-validation SOP.