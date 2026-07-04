---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-01T14:08:38.169929'
end_time: '2026-07-01T15:00:08.716366'
duration_seconds: 3090.55
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
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 35
artifact_count: 18
artifact_sources:
  openscientist_artifacts_zip: 18
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
- filename: provenance_causal_chain.json
  path: openscientist_artifacts/provenance_causal_chain.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain
- filename: provenance_causal_chain.png
  path: openscientist_artifacts/provenance_causal_chain.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist causal chain
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
- filename: provenance_evidence_synthesis.json
  path: openscientist_artifacts/provenance_evidence_synthesis.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence synthesis
- filename: provenance_evidence_synthesis.png
  path: openscientist_artifacts/provenance_evidence_synthesis.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence synthesis
- filename: provenance_final_synthesis.json
  path: openscientist_artifacts/provenance_final_synthesis.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final synthesis
- filename: provenance_final_synthesis.png
  path: openscientist_artifacts/provenance_final_synthesis.png
  media_type: image/png
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final synthesis
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

# Hypothesis Evaluation Report: H. pylori Molecular-Mimicry ("Hit-and-Run") Origin of Autoimmune Gastritis

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the hypothesis is plausible for a subset of patients but cannot explain the full spectrum of autoimmune gastritis (AIG).**

The molecular mimicry hypothesis is supported by direct evidence of cross-reactive CD4+ Th1 T cells in the gastric mucosa of H. pylori-infected patients with gastric autoimmunity (Amedei et al., 2003; D'Elios et al., 2001), sequence homology between H. pylori urease and H+/K+ ATPase (Uibo et al., 1995), Lewis antigen-based molecular mimicry via H. pylori LPS (Appelmelk et al., 1996), cross-reactive antibodies recognizing both Hp and gastric mucosal structures (Negrini et al., 1997), and critically, the demonstration that early-stage (non-atrophic) autoimmune gastritis can be healed by H. pylori eradication in 80% of cases (Müller et al., 2001; Stolte et al., 1998). However, the hypothesis is significantly limited by: (1) the cross-reactive T cell evidence comes primarily from a single research group; (2) absorption studies found that human autoantibodies are NOT generated through molecular mimicry (Faller et al., 2002; Appelmelk, 1998); (3) a substantial proportion of AIG patients (29–79%) have no evidence of prior H. pylori exposure (Vavallo et al., 2026; Pacheco et al., 2025); (4) the largest AIG cohort (n=1,598; Lenti et al., 2024) identifies H. pylori-naive AIG as a distinct clinical entity with stronger familial/genetic autoimmune signatures; (5) well-replicated mouse models demonstrate that AIG arises from intrinsic tolerance failure (Treg depletion) without any infectious trigger (Field et al., 2005; Kobayashi et al., 2004); and (6) immune checkpoint inhibitor-induced AIG in Hp-negative patients demonstrates tolerance breakdown without infection (Sugimoto et al., 2026).

The most parsimonious interpretation is that AIG is etiologically heterogeneous: H. pylori infection via molecular mimicry may initiate or accelerate disease in a genetically susceptible subset, while a substantial proportion of cases arise through intrinsic autoimmune tolerance breakdown (AIRE defects, Treg dysfunction, genetic predisposition via HLA/PTPN22, immune checkpoint dysregulation). The "hit-and-run" concept—where the infection triggers autoimmunity that persists after bacterial clearance—is supported by the Müller/Stolte eradication data showing early-stage reversibility, implying a time-dependent window. However, the key intermediate causal steps (epitope spreading, self-perpetuation after H. pylori clearance) lack direct experimental evidence in humans. Confounding evidence from Furuta et al. (2018) that AIG patients are frequently misdiagnosed as having refractory Hp infection (due to urease-positive non-Hp bacteria in achlorhydric stomachs) suggests that some Hp-AIG associations may be inflated by diagnostic misclassification.

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Context | Confidence & Limitations |
|----------|--------------|-----------|--------------------------|-------------|---------|-------------------------|
| Amedei et al. 2003 (PMID:14568977) | Human clinical | **SUPPORTS** | Cross-reactive T cells between Hp and H+/K+ ATPase | Gastric CD4+ T cells from Hp-infected AIG patients recognize both ATPase and 9 Hp protein epitopes | AIG + active Hp infection | Moderate — single research group (Florence); not independently replicated |
| D'Elios et al. 2001 (PMID:11159878) | Human clinical | **SUPPORTS** | ATPase-specific Th1 cells in gastric mucosa | 25% of gastric CD4+ clones react to H+/K+ ATPase; 88% Th1 profile; cytotoxic/proapoptotic | 5 AIG patients | Moderate — small n; same research group |
| D'Elios et al. 2004 (PMID:15242679) | Review + human data | **SUPPORTS** | Molecular mimicry mechanism in AIG | Activated CD4+ Th1 cells cross-recognize Hp and self-ATPase epitopes | Review synthesis | Moderate — review-level, same primary data |
| D'Elios et al. 2005 (PMID:15866204) | Human clinical | **SUPPORTS** | Cross-reactive T cells in Hp gastric autoimmunity | "Cytolytic T cells infiltrating the gastric mucosa cross-recognize different epitopes of H. pylori proteins and H+K+ ATPase autoantigen" | Hp-infected patients with AIG | Moderate — same group |
| Uibo et al. 1995 (PMID:7599605) | Human population + bioinformatics | **SUPPORTS** | Sequence homology urease/ATPase | 72% homology in 25 amino acid overlap between Hp urease β-subunit and H+/K+ ATPase β-subunit | Population-based (n=1,461) | Low — sequence homology alone does not prove functional mimicry |
| Appelmelk et al. 1996 (PMID:8675304) | Animal + in vitro | **SUPPORTS** (Lewis antigen path) | Lewis antigen-based molecular mimicry | Hp LPS expresses Lewis x/y antigens; anti-Lewis antibodies cause gastritis in mice | Mouse model + human sera | Moderate — Lewis-based mimicry ≠ protein-based mimicry |
| Asante et al. 1999 (PMID:10654796) | Human clinical | **SUPPORTS** (association) | Hp association with parietal cell antibodies | OR 4.0 (95% CI 1.79–9.07) for PCA if Hp-positive; CagA-negative strains more associated | Case-control (n=115) | Moderate — association, not causation |
| Kotera et al. 2023 (PMID:36742095) | Human case report | **SUPPORTS** (reversal) | AIG regression after Hp eradication | Gastric mucosal atrophy improved after Hp eradication | Single case | Very low — case report |
| Kaptan et al. 2000 (PMID:10809040) | Human cohort | **SUPPORTS** (partial reversibility) | Hp eradication improves B12 deficiency | Hp eradication improved anemia and B12 in 40% of infected patients | n=138 with B12 deficiency | Moderate — B12 improvement ≠ AIG reversal |
| Faller et al. 2002 (PMID:11815766) | Human clinical | **REFUTES** | Molecular mimicry generates autoantibodies | Antigastric autoantibodies could NOT be absorbed to Hp; no evidence for mimicry in adolescents | Adolescents (n=78) | Moderate — tests humoral, not cellular mimicry |
| Faller & Kirchner 2001 (PMID:11225441) | Human clinical | **REFUTES** | Molecular mimicry role in autoantibody formation | "Molecular mimicry between H. pylori and the host does not play a pathogenic role" | Review of their data | Moderate |
| Faller & Kirchner 2000 (PMID:10738313) | Human clinical | **REFUTES** | Molecular mimicry responsible for autoreactivity | "Molecular mimicry...does not seem to be responsible for the generation of this type of autoreactivity" | Review | Moderate |
| Appelmelk 1998 (PMID:10077749) | Human + animal | **QUALIFIES** | Lewis vs. protein mimicry differs by species | In humans, autoantibodies target protein epitopes of ATPase NOT induced through mimicry (contrast with pig model) | Human patients vs. orally infected pigs | Moderate — critical species-dependent finding |
| Vavallo et al. 2026 (PMID:41484031) | Human clinical | **QUALIFIES** | Prior Hp exposure prevalence in AAG | ~29% AAG patients have NO seroreactivity to any of 13 Hp proteins; overall seroprevalence 21.1% vs 10.3% (p=0.06, NS) | Case-control (n=178), multiplex serology | High — most sensitive Hp exposure assay |
| Lenti et al. 2024 (PMID:38976374) | Human cohort | **QUALIFIES** | Hp-naive vs. Hp-exposed AIG phenotypes | Hp-naive AIG: more familial AIG (14.7% vs 8.9%, p=0.012), T1D (4.9% vs 2.3%, p=0.025), PA (30.9% vs 21.1%, p=0.003) | ARIOSO study, n=1,598 | High — largest AIG cohort; multicenter |
| Field et al. 2005 (PMID:15763991) | Mouse model | **COMPETING** | Intrinsic tolerance failure causes EAG | EAG induced by neonatal thymectomy in BALB/c; "origins of the disease are intrinsic"; no infection needed | Well-replicated mouse model | High — extensive replication |
| Kobayashi et al. 2004 (PMID:15147343) | Mouse model | **COMPETING** | Treg depletion + poly I:C causes aggressive AIG | 100% of thymectomized + poly I:C mice develop all 3 AIG features without Hp | BALB/c mice | High |
| Wenzlau et al. 2015 (PMID:26405069) | Human genetics | **COMPETING** | Genetic basis of parietal cell autoimmunity | PCA heritability 71–95%; HLA DRB1*0404, PTPN22 R620W associations | T1D Genetics Consortium (n=6,749) | High — large cohort, robust genetics |
| Garelli et al. 2021 (PMID:34003463) | Human clinical | **COMPETING** | AIRE mutations cause AIG in APS-1 | AIG in 25.9% of APS-1 patients with AIRE gene defects | Italian APS-1 registry (n=158) | High — monogenic causation |
| Liu et al. 2026 (PMID:41963817) | Meta-analysis | **QUALIFIES** | Hp-negative AIG cancer risk | Hp-negative AIG patients: higher GC risk (HR=4.31) vs. Hp-positive AIG (HR=2.36) | 8 studies, 10 cohorts | High — meta-analysis |
| Chiaro et al. 2026 (PMID:41867096) | Human clinical | **COMPETING** | AIG in children with autoimmune comorbidities | AIG found in 5.4% of children with autoimmune diseases screened; without reference to Hp | Pediatric prospective (n=203) | Moderate — pediatric population |
| Müller et al. 2001 (PMID:11549834) | Human clinical (retrospective) | **SUPPORTS** (reversibility) | Early-stage AIG healed by Hp eradication | 80% (64/80) healing of active non-atrophic autoimmune corpus gastritis after Hp eradication; reduced lymphocytic infiltration, glandular destruction | Active non-atrophic AIG with Hp | Moderate — retrospective, uncontrolled; strongest interventional evidence |
| Stolte et al. 1998 (PMID:9773482) | Human case report | **SUPPORTS** (reversibility) | Cure of AIG by Hp eradication | Complete histological resolution of AIG in 21-year-old male 15 months post-eradication | Young patient, early AIG | Low — single case; but compelling |
| Negrini et al. 1997 (PMID:9432348) | Review + human/animal data | **SUPPORTS** (humoral mimicry) | Anti-Hp antibodies cross-react with gastric mucosal cells | Cross-reactive antibodies to parietal cell canaliculi and gastrin-producing cells in humans and rodents | Hp infection | Moderate — partially contradicts Faller |
| Furuta et al. 2018 (PMID:29920721) | Human clinical | **QUALIFIES** (diagnostic confounding) | AIG misdiagnosed as refractory Hp | 18.2% of multiple Hp eradication failures are AIG; urease-positive non-Hp bacteria cause false-positive breath tests in achlorhydric patients | Japanese clinic (n=404) | High — important confounding factor |
| Sugimoto et al. 2026 (PMID:42106905) | Human case report | **COMPETING** | AIG from ICI tolerance breakdown | PA with PCA+ after atezolizumab in Hp-negative patient; AIG from immune checkpoint removal alone | Cancer immunotherapy | Low (case report) — but mechanistically important |
| Toh 2017 (PMID:27538411) | Review | **QUALIFIES** (framework) | Pathophysiology framework for PA | "Asymptomatic autoimmune gastritis...precedes corpus atrophy by 10-20 years"; "associated with autoimmune thyroiditis and type 1 diabetes mellitus" | Comprehensive review | High — authoritative review |
| Hershko & Skikne 2009 (PMID:19786202) | Review + clinical data | **SUPPORTS** (interventional) | Hp eradication cures refractory IDA | "Cure of previously refractory IDA by H pylori eradication provides strong evidence supporting a cause-and-effect relation" | Unexplained IDA patients | Moderate — cure of IDA ≠ AIG reversal |
| Zhang & Tang 2025 (PMID:39854274) | Review | **QUALIFIES** (subtype biology) | Hp-negative AIG has distinct cancer biology | Cancer risk mainly from concurrent/past Hp; reparative metaplasia in pure AIG; T cell-dominated microenvironment less carcinogenic | Hp-negative AIG | High — supports etiological heterogeneity |
| Vavallo et al. 2026 (PMID:41484031) | Human clinical | **QUALIFIES** (two models) | "Two pathogenetic models are proposed: pure autoimmune or Hp-triggered" | Explicitly frames the dual-origin debate; Hp seropositivity 21.1% vs 10.3% (NS) | 178 subjects, multiplex serology | High — most methodologically rigorous seroprevalence study |
| Qian et al. 2026 (PMID:41670890) | Review | **QUALIFIES** (mechanistic) | Synergistic role of humoral and cellular immunity in AIG | Reviews inflammatory cascade centered on CD4-mediated parietal cell self-attack; acknowledges humoral role | Immunological review | Moderate — updates mechanistic framework |
| Sakagami et al. 1996 (PMID:9026476) | Mouse model | **QUALIFIES** (host factors) | Host genetics determine Helicobacter-induced corpus atrophy | H. felis causes corpus atrophy in SJL, C3H, DBA/2, C57BL/6 but NOT in BALB/c or CBA mice; atrophy in corpus despite antral colonization | 6 mouse strains | High — demonstrates host-dependent autoimmune-like response to Helicobacter |
| Li et al. 2025 (PMID:41425574) | Mendelian randomization | **QUALIFIES** (confounding) | AITD causally increases risk of both PA and Hp infection | MR shows shared autoimmune genetics may confound the Hp-AIG association; susceptibility genes increase both PA and Hp infection risk | MR systematic review (123 studies) | Moderate — indirect (AITD→PA/Hp, not AIG directly); raises confounding concern |
| Allakky 2023 (PMID:37885562) | Systematic review | **QUALIFIES** | Hp association with anti-IF and anti-PCA in PA | "Multifaceted relationship" between Hp and gastric autoantibodies | Systematic review | Moderate — details truncated |

---

## Mechanistic Causal Chain

The hypothesis proposes the following causal chain from upstream trigger to clinical disease:

### Step 1: Genetic Susceptibility (STRONG evidence)
- **Claim:** Genetically susceptible individuals (specific HLA alleles, PTPN22 variants) are predisposed to autoimmune gastritis.
- **Evidence:** HLA-DRB1*0404, DPB1*0201, PTPN22 R620W associated with PCA (PMID:26405069). Heritability 71–95%. AIG occurs in 25.9% of APS-1 patients with AIRE mutations (PMID:34003463).
- **Strength of link:** **STRONG** — well-replicated genetic associations.

### Step 2: H. pylori Infection (ESTABLISHED but not universal)
- **Claim:** H. pylori colonizes the gastric mucosa and provides the initial antigenic stimulus.
- **Evidence:** H. pylori infects ~50% of the global population. Association with PCA: OR 4.0 (PMID:10654796).
- **Strength of link:** **MODERATE** — association demonstrated, but ~29% of AAG patients show NO evidence of prior Hp exposure (PMID:41484031).

### Step 3: Molecular Mimicry — Cross-Reactive T-Cell Activation (MODERATE evidence, disputed)
- **Claim:** H. pylori antigens share structural epitopes with H+/K+ ATPase, activating cross-reactive CD4+ Th1 T cells.
- **Evidence FOR:** Cross-reactive T cell clones identified from 9 Hp proteins (PMID:14568977). 72% sequence homology between Hp urease and ATPase β-subunit (PMID:7599605).
- **Evidence AGAINST:** Autoantibodies could NOT be absorbed to Hp (PMID:11815766). Human autoantibodies target protein epitopes NOT induced through mimicry (PMID:10077749).
- **Strength of link:** **DISPUTED** — T-cell mimicry supported by one group; humoral mimicry refuted by multiple groups. The T-cell and B-cell arms may operate through different mechanisms.

### Step 4: Epitope Spreading and Bystander Activation (WEAK/INFERRED)
- **Claim:** Initial cross-reactive response spreads to additional self-epitopes, becoming self-perpetuating.
- **Evidence:** No direct evidence of epitope spreading in AIG. Inferred from general autoimmunity principles and the observation that established AIG is often Hp-negative.
- **Strength of link:** **WEAK** — entirely inferred; no AIG-specific studies.

### Step 5: Self-Perpetuating Autoimmunity / "Hit-and-Run" (PARTIALLY SUPPORTED — stage-dependent)
- **Claim:** Autoimmunity persists after H. pylori clearance (spontaneous or therapeutic), explaining why established AIG is frequently Hp-negative.
- **Evidence FOR stage-dependent model:** Müller et al. (2001, PMID:11549834) showed 80% healing of EARLY (non-atrophic) autoimmune gastritis after Hp eradication. Stolte et al. (1998, PMID:9773482) reported complete cure in a young patient. This strongly implies that at early stages, the autoimmune process is still Hp-dependent and reversible.
- **Evidence FOR self-perpetuation:** Established (atrophic) AIG is often Hp-negative. The healing rate in Müller's study was for non-atrophic disease only — atrophic disease was not studied and is presumably irreversible, consistent with a "point of no return" after which the autoimmunity has become self-sustaining.
- **Strength of link:** **MODERATE** — the stage-dependent model is supported: early AIG may be Hp-dependent and reversible; late AIG appears self-perpetuating. However, no study has directly tracked the transition from reversible to irreversible disease, and the 20% non-responders in Müller's study remain unexplained.

### Step 6: Parietal Cell Destruction → Clinical Disease (STRONG)
- **Claim:** Th1-mediated destruction of parietal cells leads to achlorhydria, atrophic gastritis, vitamin B12/iron deficiency, and hypergastrinemia with neuroendocrine cell hyperplasia.
- **Evidence:** Fas/FasL and perforin-mediated killing of parietal cells by CD4+ Th1 cells (PMID:15763993, PMID:11159878). Clinical endpoints are well-established.
- **Strength of link:** **STRONG** — effector mechanisms well-characterized.

---

## Knowledge Gaps

### 1. Lack of Independent Replication of Cross-Reactive T-Cell Evidence
- **Scope:** The cross-reactive T-cell data (the strongest direct evidence for mimicry) comes exclusively from D'Elios, Amedei, and Del Prete's group in Florence (PMID:14568977, 15242679, 15596126, 15866204).
- **Why it matters:** Independent replication is the cornerstone of scientific validation. No other group has published confirmation of cross-reactive T cells recognizing both Hp antigens and H+/K+ ATPase.
- **What was checked:** PubMed search for cross-reactive T cells + H. pylori + ATPase.
- **Resolution:** Independent laboratories should attempt to isolate cross-reactive T cell clones from AIG patients with active or past Hp infection using modern TCR sequencing/tetramer technology.

### 2. No Direct Evidence of Epitope Spreading in AIG
- **Scope:** The hypothesis posits that initial mimicry-triggered responses spread to additional self-epitopes, becoming self-perpetuating. No study has demonstrated epitope spreading in AIG.
- **Why it matters:** This is the critical mechanistic step that converts a pathogen-triggered response into autonomous autoimmunity.
- **What was checked:** PubMed searches for "autoimmune gastritis epitope spreading" and "autoimmune gastritis bystander activation."
- **Resolution:** Longitudinal studies tracking the breadth of anti-ATPase T-cell and antibody responses during and after Hp infection, using peptide arrays or epitope mapping.

### 3. No Longitudinal "Hit-and-Run" Tracking Study
- **Scope:** No study has prospectively followed patients from Hp infection → development of autoimmunity → Hp clearance → persistent AIG.
- **Why it matters:** The "hit-and-run" concept is the central claim distinguishing this hypothesis from simple Hp-associated gastritis, yet it has never been directly observed longitudinally.
- **What was checked:** PubMed searches for "hit and run" + autoimmune gastritis; eradication + reversal studies.
- **Resolution:** Prospective cohort of Hp-infected individuals with serial autoantibody testing and gastric biopsies before and after eradication, with long-term follow-up for AIG development.

### 4. Contradictory Evidence on Mimicry at the Humoral Level
- **Scope:** Faller's group (PMID:11815766, 11225441, 10738313) and Appelmelk (PMID:10077749) found that autoantibodies in human Hp gastritis are NOT generated through molecular mimicry, directly contradicting the mimicry mechanism for humoral immunity.
- **Why it matters:** The hypothesis implies both T-cell and B-cell mimicry, but the evidence supports only T-cell cross-reactivity (from one group) while refuting humoral mimicry.
- **What was checked:** Multiple absorption and immunoprecipitation studies.
- **Resolution:** Clarify whether T-cell mimicry operates independently of humoral mimicry, and whether T-cell mimicry alone is sufficient for disease initiation.

### 5. Proportion of AIG Attributable to H. pylori
- **Scope:** Vavallo et al. (2026) found ~29% of AAG patients had ZERO seroreactivity to Hp by multiplex serology. The ARIOSO study shows distinct Hp-naive and Hp-exposed subpopulations. The true proportion of AIG triggered by Hp remains unknown.
- **Why it matters:** If only 20–30% of AIG is Hp-triggered, the hypothesis explains a subset, not the disease.
- **What was checked:** Multiplex serology studies, ARIOSO cohort data, T1D-associated AIG studies.
- **Resolution:** Large-scale multiplex serology + genetic profiling studies to quantify what fraction of AIG has evidence of prior Hp exposure and whether Hp-exposed AIG differs mechanistically.

### 6. CagA and Virulence Factor Specificity
- **Scope:** Asante et al. (1999, PMID:10654796) found CagA-negative strains more associated with PCA, suggesting strain-specific effects. This has not been followed up systematically.
- **Why it matters:** If specific Hp strain characteristics determine autoimmune risk, this is critical for understanding the mimicry mechanism and identifying at-risk patients.
- **What was checked:** Search for CagA + autoimmune gastritis yielded only the Asante study.
- **Resolution:** CagA/VacA typing in large AIG cohorts with Hp exposure.

### 7. No GWAS for AIG Specifically
- **Scope:** While genetic associations exist for PCA from candidate-gene studies (HLA, PTPN22), no genome-wide association study specifically for AIG/pernicious anemia has been published.
- **Why it matters:** GWAS would identify novel susceptibility loci and potentially reveal whether Hp-triggered and intrinsic AIG share or differ in genetic architecture.
- **What was checked:** PubMed search for "autoimmune gastritis GWAS" found only a cross-trait analysis with Alzheimer's disease.
- **Resolution:** Well-powered GWAS in AIG cohorts, ideally stratified by Hp exposure status.

### 8. No Randomized Controlled Trial of Early Hp Eradication to Prevent/Reverse AIG
- **Scope:** The corollary that early eradication can prevent or reverse AIG has been supported by one retrospective, uncontrolled study (Müller et al., 2001, PMID:11549834: 80% healing of non-atrophic AIG) and case reports (Stolte et al., 1998; Kotera et al., 2023), but has never been tested in a randomized controlled trial.
- **Why it matters:** The Müller study is the strongest interventional evidence supporting the hypothesis but has major limitations (retrospective, uncontrolled, no autoantibody tracking). An RCT would provide definitive causal evidence and has direct clinical implications for early intervention.
- **What was checked:** PubMed searches for eradication + AIG prevention/reversal/RCT.
- **Resolution:** Randomized controlled trial of Hp eradication in PCA-positive, Hp-positive patients at early (non-atrophic) disease stages, with histological, serological (PCA titers, pepsinogen I/II), and clinical endpoints, and long-term follow-up to assess durability of response.

### 9. Diagnostic Confounding: AIG Misdiagnosed as Refractory H. pylori
- **Scope:** Furuta et al. (2018, PMID:29920721) found 18.2% of patients with ≥2 Hp eradication failures actually had AIG, with urease-positive non-Hp bacteria causing false-positive breath tests. This confounding may inflate the apparent association between Hp and AIG.
- **Why it matters:** If AIG patients are systematically misclassified as Hp-positive (due to false-positive testing), epidemiological studies overestimate Hp prevalence in AIG, biasing evidence toward the mimicry hypothesis.
- **What was checked:** Studies of Hp eradication failure and AIG.
- **Resolution:** Studies of AIG should use multiplex serology (not breath test alone) to determine prior Hp exposure, and should screen for urease-positive non-Hp bacteria.

---

## Alternative Models

### 1. Intrinsic Autoimmune Tolerance Failure (COMPETING — strongest alternative)
- **Relationship:** Alternative upstream cause; directly competes with Hp-trigger model.
- **Evidence:** Experimental autoimmune gastritis (EAG) in mice occurs via neonatal thymectomy (Treg depletion) without any infection (PMID:15763991). The disease is "intrinsic" — no environmental modifiers needed. This is the dominant mouse model of AIG.
- **Assessment:** This model better explains: (a) AIG in APS-1 (AIRE mutations), (b) AIG in children with autoimmune comorbidities, (c) the 29% of AAG patients with no Hp seroreactivity, (d) the strong familial clustering and heritability of PCA.
- **Conclusion:** This is likely the mechanism for a substantial proportion of human AIG cases, possibly the majority.

### 2. Lewis Antigen LPS-Based Mimicry (COMPLEMENTARY — overlapping mechanism)
- **Relationship:** Parallel mechanism within the mimicry framework; both protein-epitope and carbohydrate-epitope mimicry may contribute.
- **Evidence:** Hp LPS expresses Lewis x/y antigens that mimic gastric mucosa (PMID:8675304). Anti-Lewis antibodies cause gastritis in mice. However, in humans, autoantibodies target protein epitopes not induced through Lewis mimicry (PMID:10077749).
- **Assessment:** Lewis mimicry is better established in animal models than in humans. It may contribute to Hp-associated (type B) gastritis rather than classical autoimmune (type A) gastritis.

### 3. Bystander Activation / Inflammation-Triggered Autoimmunity (COMPLEMENTARY)
- **Relationship:** Alternative mechanism by which Hp infection triggers autoimmunity without requiring direct molecular mimicry.
- **Evidence:** Hp-induced chronic inflammation could cause enhanced presentation of self-antigens from damaged parietal cells, activating autoreactive T cells through bystander activation rather than molecular mimicry. D'Elios et al. (2004, PMID:15242679) acknowledge this possibility.
- **Assessment:** Not mutually exclusive with mimicry; both mechanisms may operate. No direct evidence distinguishes them in human AIG.

### 4. Immune Checkpoint Dysregulation (EMERGING)
- **Relationship:** Downstream consequence of tolerance failure; provides modern mechanism for "tolerance breakdown."
- **Evidence:** Sugimoto et al. (2026, PMID:42106905) reported pernicious anemia developing after atezolizumab (anti-PD-L1) treatment, with PCA positivity and Hp-negative status. This demonstrates that releasing immune checkpoints can cause AIG without Hp.
- **Assessment:** Supports the concept that AIG can arise from any perturbation of immune tolerance, not only Hp infection.

### 5. Microbiome Dysbiosis Post-Hp Eradication (EMERGING)
- **Relationship:** Downstream modifier that may influence disease progression.
- **Evidence:** Gastric microbiome changes after Hp eradication and in achlorhydric states may contribute to ongoing inflammation. This is speculative for AIG specifically. No 16S sequencing or gastric microbiome studies specific to AIG were found.
- **Assessment:** No direct evidence linking gastric dysbiosis to AIG pathogenesis.

### 6. Shared Autoimmune Genetics Confounding (EMERGING — from MR evidence)
- **Relationship:** Alternative explanation for the epidemiological Hp-AIG association; challenges the causal direction.
- **Evidence:** Li et al. (2025, PMID:41425574) showed via MR that autoimmune thyroid disease (which shares genetic susceptibility with AIG) causally increases risk of BOTH pernicious anemia AND H. pylori infection. This implies that autoimmune-susceptibility genes may independently increase both Hp infection risk (via altered gastric immunity) and AIG risk, creating a confounded association that mimics causation.
- **Assessment:** If shared genetics explain the Hp-AIG co-occurrence, the mimicry hypothesis becomes unnecessary for most cases. However, this does not disprove mimicry — both confounding and causal mechanisms could co-exist. A direct MR study of Hp→AIG is needed.

### 7. Distinct Cancer Biology Supports Etiological Heterogeneity (EMERGING)
- **Relationship:** Downstream consequence that distinguishes Hp-associated from Hp-naive AIG.
- **Evidence:** Zhang & Tang (2025, PMID:39854274) showed that cancer risk in AIG is primarily from concurrent/past Hp infection. Hp-negative AIG features reparative (pseudopyloric, complete intestinal) metaplasia vs. the aggressive incomplete IM in Hp-induced gastritis. Rugge et al. (2023, PMID:35772926) found no excess GC risk in 211 Hp-naive AIG patients over 10,541 person-years.
- **Assessment:** If Hp-triggered and Hp-naive AIG produce qualitatively different disease courses and cancer risks, this is consistent with etiological heterogeneity and supports viewing the molecular mimicry pathway as one of multiple independent triggers.

---

## Discriminating Tests

### Test 1: Prospective Hp Eradication Trial in Early AIG
- **Design:** Randomized controlled trial in Hp-positive patients with positive PCA and early (non-atrophic) corpus gastritis.
- **Intervention:** Standard Hp eradication vs. standard of care.
- **Endpoints:** PCA titers, histological atrophy progression, pepsinogen I/II ratio, gastrin levels at 1, 2, and 5 years.
- **Expected result if mimicry is causal:** Eradication group shows PCA decline and atrophy stabilization/regression.
- **Sample stratification:** HLA genotype, CagA status, baseline PCA titer, presence of other autoimmune diseases.

### Test 2: TCR Repertoire Analysis of Gastric T Cells
- **Design:** Single-cell TCR sequencing of gastric mucosal T cells from: (a) AIG + Hp-positive, (b) AIG + Hp-naive, (c) Hp gastritis without autoimmunity, (d) healthy controls.
- **Assay:** scTCR-seq + tetramer staining with Hp peptides and H+/K+ ATPase peptides.
- **Expected result if mimicry is causal:** Shared TCR clonotypes between Hp-reactive and ATPase-reactive populations in group (a) but not (b).
- **Power:** Would independently replicate or refute the cross-reactive T-cell findings from D'Elios's group.

### Test 3: Multiplex Serology + Genetic Profiling in Large AIG Cohort
- **Design:** Apply Hp multiplex serology (≥13 antigens) + HLA typing + PTPN22/CTLA4 genotyping to ≥1,000 AIG patients.
- **Biomarker panel:** PCA, AIFA, Hp-specific antibodies, pepsinogens, gastrin.
- **Expected result:** Identification of genetically distinct subgroups: (a) Hp-triggered AIG (Hp-seropositive, lower genetic risk scores), (b) intrinsic autoimmune AIG (Hp-seronegative, higher genetic risk, more polyautoimmunity).
- **Impact:** Would quantify the proportion of AIG attributable to each pathway.

### Test 4: Longitudinal Autoantibody Tracking During Hp Infection
- **Design:** Prospective cohort of newly diagnosed Hp-infected individuals with serial PCA testing over 10+ years.
- **Endpoints:** Incidence of PCA seroconversion, time course relative to Hp infection duration, and fate after eradication.
- **Expected result if "hit-and-run" is real:** PCA appear during infection and persist (or continue rising) after Hp eradication in a subset.

### Test 5: Mendelian Randomization of Hp→AIG
- **Design:** Two-sample bidirectional MR using GWAS summary statistics for H. pylori infection and AIG/pernicious anemia.
- **Instruments:** SNPs associated with Hp infection susceptibility (exposure) and AIG/PA (outcome), and vice versa.
- **Expected result if mimicry is causal:** Hp infection genetic instruments predict increased AIG/PA risk (causal direction: Hp→AIG).
- **Expected result if confounding:** Bidirectional effects or null in Hp→AIG direction, with AIG genetic variants predicting Hp infection risk (reverse causation or pleiotropy).
- **Impact:** Would resolve whether the Hp-AIG association is causal or confounded by shared autoimmune genetics. No such study exists as of search date (July 2026).

### Test 6: Epitope Spreading Analysis
- **Design:** Use peptide microarrays covering full H+/K+ ATPase α and β subunits to map the breadth of T-cell and antibody responses at different AIG stages.
- **Comparisons:** Early AIG vs. late AIG; Hp-positive vs. Hp-naive AIG.
- **Expected result if epitope spreading occurs:** Broader epitope reactivity in later-stage disease and in Hp-triggered (initially focal mimicry) cases.

---

## Curation Leads

*All leads below are candidates for curator verification, not confirmed KB updates.*

### Candidate Evidence References

1. **PMID:14568977** (Amedei et al., 2003) — Primary evidence for cross-reactive T cells. Snippet: *"H. pylori-infected patients with gastric autoimmunity harbor in vivo-activated gastric CD4+ T cells that recognize both H+, K+-adenosine triphosphatase and H. pylori antigens."* → Should be added as SUPPORT evidence for the hypothesis.

2. **PMID:41484031** (Vavallo et al., 2026) — Multiplex serology showing low Hp seroprevalence. Snippet: *"Complete absence of seroreactivity was similar in AAG and Ctr-HS (29.3% vs 38.5%, p=0.23)."* → Should be added as QUALIFYING evidence limiting the scope of the hypothesis.

3. **PMID:38976374** (Lenti et al., 2024) — ARIOSO cohort. Snippet: *"H. pylori-naive patients were more likely to have a first-degree family history of AIG (14.7% vs 8.9%; P = 0.012)."* → Should be added as QUALIFYING evidence identifying distinct AIG subtypes.

4. **PMID:11815766** (Faller et al., 2002) — Absorption study refuting humoral mimicry. Snippet: *"AGA...could not be absorbed to H pylori. No evidence for a role of molecular mimicry between H pylori and the host at this young age could be found."* → Should be added as REFUTING evidence.

5. **PMID:15763991** (Field et al., 2005) — Mouse model of intrinsic origin. Snippet: *"no specific environmental modifiers are identifiable, the origins of the disease are intrinsic."* → Should support a competing hypothesis node (intrinsic tolerance failure).

6. **PMID:26405069** (Wenzlau et al., 2015) — Genetic architecture of PCA. → Should support a competing hypothesis node (genetic susceptibility).

7. **PMID:11549834** (Müller et al., 2001) — Healing of early AIG by Hp eradication. Snippet: *"In 64 patients (80%), H. pylori eradication treatment was followed by healing of the active autoimmune corpus gastritis."* → Should be added as SUPPORT evidence for the hypothesis, specifically for the reversibility corollary.

8. **PMID:29920721** (Furuta et al., 2018) — AIG misdiagnosed as refractory Hp. Snippet: *"A total of 43 patients were diagnosed as having AIG, of whom...40 failed treatment at least twice (18.2%, 40/220)."* → Should be added as QUALIFYING evidence (diagnostic confounding) and as a candidate knowledge gap.

9. **PMID:9432348** (Negrini et al., 1997) — Cross-reactive antibodies. Snippet: *"antibodies against H. pylori have been found to cross-react with both antral mucosal cells...and gastrin-producing cells."* → Should be added as SUPPORT evidence (humoral arm), but note conflict with Faller's absorption data.

10. **PMID:42106905** (Sugimoto et al., 2026) — ICI-induced AIG. Snippet: *"removal of immune checkpoint brakes by atezolizumab may reveal this pathogenesis."* → Should support a competing hypothesis node (immune checkpoint/tolerance failure mechanism).

11. **PMID:41425574** (Li et al., 2025) — MR evidence. Snippet: *"MR analyses indicated that AITD significantly increased the risk of...pernicious anemia, Helicobacter pylori infection."* → Should be added as a candidate knowledge gap: shared autoimmune genetics may confound the Hp-AIG association.

12. **PMID:9026476** (Sakagami et al., 1996) — Host-dependent Helicobacter atrophy. Snippet: *"In SJL, C3H/He, DBA/2, and C57BL/6 infected mice, severe to moderate chronic active gastritis was observed only in the body of the stomach."* → Should support both the mimicry hypothesis (infection can trigger corpus atrophy) and the genetic susceptibility model (host genetics determine outcome).

### Candidate Pathophysiology Nodes/Edges

- **Node:** "Intrinsic autoimmune tolerance failure" → should exist as a LEADING alternative or competing hypothesis in the KB.
- **Edge:** "H. pylori infection → cross-reactive CD4+ Th1 activation" — status: PARTIAL (only T-cell arm supported; humoral arm refuted).
- **Edge:** "Cross-reactive T-cell activation → epitope spreading" — status: INFERRED (no direct evidence).
- **Edge:** "Epitope spreading → self-perpetuating autoimmunity" — status: INFERRED.

### Candidate Ontology Terms

- Cell types: `CL:0000162` (parietal cell), `CL:0000492` (CD4+ Th1 cell), `CL:0002086` (regulatory T cell)
- Biological processes: `GO:0002377` (immunoglobulin production), `GO:0002449` (lymphocyte mediated immunity), `GO:0006955` (immune response)
- Disease: `MONDO:0007093` (autoimmune gastritis), `MONDO:0008223` (pernicious anemia)

### Candidate Subtype Restrictions

The hypothesis should be annotated as applicable to a **subset** of AIG cases:
- Best supported for: **H. pylori-exposed, genetically susceptible adults** developing AIG in mid-life
- Poorly applicable to: **APS-1 patients (AIRE mutations), pediatric AIG, AIG in H. pylori-naive patients with polyautoimmune syndromes**

### Candidate Status Change

Current status: **ALTERNATIVE**
Suggested status: **ALTERNATIVE** (maintain) — with explicit annotation that it explains a subset, not the majority, of AIG cases. The hypothesis could be upgraded to SUPPORTED for an Hp-triggered subtype if independent replication of cross-reactive T cells is achieved.

### Candidate Knowledge Gaps for KB

1. **"No independent replication of cross-reactive T cell evidence"** — Priority: HIGH. All human T-cell cross-reactivity data comes from one group.
2. **"Proportion of AIG attributable to H. pylori unknown"** — Priority: HIGH. Current estimates range from 20–70% depending on methodology.
3. **"No RCT of Hp eradication for AIG prevention"** — Priority: HIGH. Only case reports exist.
4. **"Epitope spreading in AIG not demonstrated"** — Priority: MEDIUM. Central to the "self-perpetuation" claim.
5. **"No GWAS for AIG"** — Priority: MEDIUM. Would distinguish genetic architecture of Hp-triggered vs. intrinsic AIG.
6. **"CagA/virulence factor specificity unexplored in AIG"** — Priority: LOW. One study suggests CagA-negative strains more associated.
7. **"Diagnostic confounding from false-positive Hp testing in AIG"** — Priority: HIGH. Urease-positive non-Hp bacteria in achlorhydric stomachs inflate Hp prevalence estimates in AIG.
8. **"No scRNAseq or modern TCR profiling of AIG gastric mucosa"** — Priority: MEDIUM. Would resolve whether cross-reactive T cells exist and how they relate to intrinsic autoreactive clones. Searched: "autoimmune gastritis single cell RNA sequencing," "gastric autoimmunity T cell receptor repertoire sequencing" — no results found.
9. **"Stage-dependent reversibility window undefined"** — Priority: HIGH. The Müller study suggests early-stage AIG is reversible but the transition to irreversible disease is not characterized.
10. **"No gastric microbiome studies specific to AIG"** — Priority: MEDIUM. The role of non-Hp bacteria colonizing achlorhydric stomachs in perpetuating inflammation is unknown. Searched: "autoimmune gastritis microbiome 16S sequencing" — no results found.
11. **"No animal model combining Helicobacter infection + genetic susceptibility → autoimmune gastritis with autoantibodies"** — Priority: HIGH. Sakagami 1996 showed host-dependent corpus atrophy but did not test for PCA or ATPase-specific T cells. No study has combined Helicobacter infection with Treg depletion or genetic susceptibility models. Searched: "Helicobacter infection neonatal thymectomy mouse autoimmune gastritis synergistic" — no results found.
12. **"No transcriptomic/proteomic comparison of Hp-associated vs. Hp-naive AIG"** — Priority: MEDIUM. Would reveal whether different upstream triggers produce molecularly distinct disease states. Searched: "autoimmune gastritis transcriptomics proteomics gene expression" — no results found.
13. **"Potential confounding by shared autoimmune genetics"** — Priority: HIGH. Li et al. (2025, PMID:41425574) showed via Mendelian randomization that autoimmune thyroid disease causally increases risk of BOTH pernicious anemia AND H. pylori infection. This raises the possibility that the Hp-AIG association is confounded by shared autoimmune genetics rather than representing a causal trigger. No direct MR study of Hp→AIG has been performed. Searched: "Mendelian randomization Helicobacter pylori pernicious anemia autoimmune gastritis causal" — no direct MR found.
14. **"No registered clinical trials for AIG treatment or prevention"** — Priority: MEDIUM. Searched: "autoimmune gastritis clinical trial registered treatment intervention" — no results found. The absence of any clinical trials reflects the orphan status of AIG therapeutics research.

---

## Summary

The H. pylori molecular mimicry "hit-and-run" hypothesis for autoimmune gastritis is **partially supported**. The strongest evidence comes from: (a) cross-reactive T cells between Hp proteins and H+/K+ ATPase (Amedei et al., 2003 — but from a single research group), (b) cross-reactive antibodies to gastric mucosal structures (Negrini et al., 1997), (c) the demonstration that early-stage (non-atrophic) AIG is healable by Hp eradication in 80% of cases (Müller et al., 2001), and (d) an epidemiological association (OR 4.0) between Hp and parietal cell antibodies (Asante et al., 1999).

The hypothesis is **significantly limited** by: (1) lack of independent replication of the cross-reactive T-cell findings, (2) contradictory evidence that human autoantibodies are NOT generated through molecular mimicry (Faller et al., 2002), (3) a substantial H. pylori-naive AIG subpopulation (~29% with zero Hp seroreactivity; Vavallo et al., 2026) that has distinct clinical and genetic features (ARIOSO cohort, n=1,598; Lenti et al., 2024), (4) robust alternative models of intrinsic tolerance failure (mouse models; APS-1; ICI-induced AIG), and (5) diagnostic confounding from false-positive Hp testing in achlorhydric AIG patients (Furuta et al., 2018).

### Claim Status Summary

| Claim | Status | Evidence Level |
|-------|--------|---------------|
| Hp antigens share epitopes with H+/K+ ATPase | **Established** (sequence + T cell) | Moderate (single group for T cells; bioinformatic for sequence) |
| Cross-reactive T cells exist in human AIG | **Emerging** (unconfirmed) | Moderate — awaiting independent replication |
| Autoantibodies are generated via molecular mimicry | **Contradicted** | Moderate — absorption studies refute; Negrini partially supports |
| Lewis antigen mimicry contributes to gastritis | **Established** in animal models | Moderate — human relevance uncertain |
| Early-stage AIG is reversible with Hp eradication | **Emerging** (strong signal) | Moderate — retrospective, uncontrolled (Müller 2001) |
| Established AIG is self-perpetuating ("hit-and-run") | **Speculative** | Weak — inferred from epidemiology, never directly demonstrated |
| Epitope spreading occurs in AIG | **Speculative** | No evidence — entirely inferred |
| Hp is necessary for all AIG | **Refuted** | High — multiplex serology, mouse models, ICI-induced AIG, APS-1 |
| Hp can trigger AIG in a subset | **Partially supported** | Moderate — consistent evidence across lines |
| AIG is etiologically heterogeneous | **Emerging consensus** | High — ARIOSO cohort, cancer biology differences, multiplex serology |
| Hp-AIG association is causal (not confounded) | **Unresolved** | No MR study exists; MR of AITD→PA+Hp raises confounding concern |

The most accurate current model is **etiological heterogeneity with a stage-dependent reversibility window**: H. pylori may trigger AIG in a genetically susceptible subset, with a critical early window where eradication can heal the gastritis. After a yet-undefined point, the autoimmunity becomes self-perpetuating (the "hit-and-run" phase). Simultaneously, a comparable or larger proportion of AIG cases arise through intrinsic autoimmune mechanisms independent of H. pylori. The critical missing evidence includes: (a) independent replication of cross-reactive T cells using modern TCR sequencing, (b) a prospective longitudinal study tracking the Hp infection → autoimmunity → clearance → persistent AIG sequence, (c) a randomized controlled trial of Hp eradication in early-stage AIG, (d) characterization of the reversibility window, and (e) a direct Mendelian randomization study of Hp→AIG to resolve whether the association is causal or confounded by shared autoimmune genetics.

---

## Conclusion and Recommendation

### For the Knowledge Base

**Maintain the ALTERNATIVE status** for the H. pylori molecular mimicry "hit-and-run" hypothesis. The hypothesis is partially supported as one of multiple etiological pathways but should be explicitly annotated with:

1. **Subtype restriction:** Best supported for Hp-exposed, genetically susceptible adults with early-stage (non-atrophic) autoimmune gastritis. Poorly applicable to APS-1/AIRE-mediated AIG, pediatric AIG, AIG in Hp-naive polyautoimmune patients, and ICI-induced AIG.

2. **Stage-dependent annotation:** The reversibility corollary (early eradication heals AIG) has moderate evidence (Müller 2001, 80% healing rate, uncontrolled) and represents the most clinically actionable component of the hypothesis.

3. **Key unresolved edges:** The causal chain has two critically weak links — (a) the molecular mimicry → epitope spreading transition (entirely speculative, no evidence) and (b) whether the Hp-AIG epidemiological association is causal or confounded by shared autoimmune genetics (MR evidence raises concern).

4. **Competing hypothesis node:** An "Intrinsic autoimmune tolerance failure" hypothesis should be added or elevated as a LEADING alternative, supported by extensive mouse model data, human genetics (PCA heritability 71-95%), APS-1, and ICI-induced AIG cases.

### Literature Coverage Summary

| Category | Papers Found | Key Sources |
|----------|-------------|-------------|
| Direct mimicry evidence (T cell) | 4 | D'Elios/Amedei group (Florence) |
| Direct mimicry evidence (antibody) | 4 | Negrini, Appelmelk, Faller (conflicting) |
| Epidemiological association | 5 | Asante, Uibo, Vavallo, Lenti (ARIOSO) |
| Eradication reversal | 3 | Müller, Stolte, Kotera |
| Mouse models (tolerance) | 4 | Toh/Alderuccio, Kobayashi |
| Mouse models (infection) | 1 | Sakagami |
| Genetic/heritability | 3 | Wenzlau, Garelli, Li (MR) |
| Cancer biology differences | 3 | Zhang & Tang, Liu, Rugge |
| ICI-induced AIG | 1 | Sugimoto |
| Diagnostic confounding | 1 | Furuta |
| Recent reviews (2025-2026) | 5 | Feng, Lenti, Qian, Zhang & Tang, Vavallo |
| **Total unique PMIDs cited** | **~35** | |

### Search Completeness Assessment

- **Well-covered:** Molecular mimicry evidence (T cell and antibody), epidemiological associations, mouse models, genetic susceptibility, eradication reversal data, competing hypotheses
- **Partially covered:** Recent 2025-2026 literature (some abstracts truncated), Lewis antigen pathway
- **Not found despite searching:** scRNAseq/TCR profiling of AIG, gastric microbiome studies, AIG-specific GWAS, clinical trials, direct Hp→AIG MR study, transcriptomic comparison of Hp+ vs Hp- AIG, animal models combining infection + genetic susceptibility
- **Not searched (out of scope):** Epigenetic mechanisms, single-nucleotide-level epitope mapping, non-Western cohort data

*Report generated: July 2026. Based on PubMed searches across 5 iterative search rounds with ~100 papers reviewed.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist causal chain](openscientist_artifacts/provenance_causal_chain.json)
![OpenScientist causal chain](openscientist_artifacts/provenance_causal_chain.png)
- [OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.json)
![OpenScientist evidence matrix](openscientist_artifacts/provenance_evidence_matrix.png)
- [OpenScientist evidence synthesis](openscientist_artifacts/provenance_evidence_synthesis.json)
![OpenScientist evidence synthesis](openscientist_artifacts/provenance_evidence_synthesis.png)
- [OpenScientist final synthesis](openscientist_artifacts/provenance_final_synthesis.json)
![OpenScientist final synthesis](openscientist_artifacts/provenance_final_synthesis.png)
- [OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.json)
![OpenScientist plot 1](openscientist_artifacts/provenance_plot_1.png)
- [OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.json)
![OpenScientist plot 2](openscientist_artifacts/provenance_plot_2.png)
- [OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.json)
![OpenScientist plot 3](openscientist_artifacts/provenance_plot_3.png)
- [OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.json)
![OpenScientist plot 4](openscientist_artifacts/provenance_plot_4.png)