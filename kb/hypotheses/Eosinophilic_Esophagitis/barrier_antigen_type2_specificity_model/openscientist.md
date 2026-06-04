---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-04T00:21:40.225152'
end_time: '2026-06-04T01:08:19.144453'
duration_seconds: 2798.92
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Eosinophilic Esophagitis
  category: Complex
  hypothesis_group_id: barrier_antigen_type2_specificity_model
  hypothesis_label: Barrier-Antigen Type 2 Specificity Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: barrier_antigen_type2_specificity_model\n\
    hypothesis_label: Barrier-Antigen Type 2 Specificity Model\nstatus: EMERGING\n\
    description: Esophageal epithelial barrier dysfunction increases exposure to food\
    \ and aeroallergen antigens\n  and triggers epithelial alarmin release. TSLP and\
    \ IL-33 then polarize local ILC2/Th2 inflammation, IL-5/IL-13\n  responses, and\
    \ CCL26-mediated eosinophil recruitment. The broad barrier-to-type-2 axis is well\
    \ supported,\n  but the patient-specific selection of food antigens remains an\
    \ open mechanistic subproblem rather than\n  a settled causal edge.\nevidence:\n\
    - reference: PMID:19596009\n  reference_title: Biology and treatment of eosinophilic\
    \ esophagitis.\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Eosinophilic\
    \ esophagitis is a recently recognized but expanding disorder characterized by\
    \ antigen-driven\n    eosinophil accumulation in the esophagus.\n  explanation:\
    \ Establishes antigen-driven eosinophil accumulation as a central EoE mechanism.\n\
    - reference: PMID:19596009\n  reference_title: Biology and treatment of eosinophilic\
    \ esophagitis.\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: The\
    \ pathogenesis of eosinophilic esophagitis involves environmental and genetic\
    \ factors, particularly\n    food antigens and expression level of the eosinophil\
    \ chemoattractant eotaxin-3, respectively.\n  explanation: Links food antigens\
    \ and eotaxin-3/CCL26 biology within the mechanistic model.\n- reference: PMID:29980278\n\
    \  reference_title: Epithelial origin of eosinophilic esophagitis.\n  supports:\
    \ SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Furthermore, genetic\
    \ and functional data establish a primary role for impaired epithelial barrier\n\
    \    function in disease susceptibility and pathoetiology.\n  explanation: Supports\
    \ the epithelial barrier component of the model."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
citation_count: 35
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Eosinophilic Esophagitis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** barrier_antigen_type2_specificity_model
- **Hypothesis Label:** Barrier-Antigen Type 2 Specificity Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: barrier_antigen_type2_specificity_model
hypothesis_label: Barrier-Antigen Type 2 Specificity Model
status: EMERGING
description: Esophageal epithelial barrier dysfunction increases exposure to food and aeroallergen antigens
  and triggers epithelial alarmin release. TSLP and IL-33 then polarize local ILC2/Th2 inflammation, IL-5/IL-13
  responses, and CCL26-mediated eosinophil recruitment. The broad barrier-to-type-2 axis is well supported,
  but the patient-specific selection of food antigens remains an open mechanistic subproblem rather than
  a settled causal edge.
evidence:
- reference: PMID:19596009
  reference_title: Biology and treatment of eosinophilic esophagitis.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Eosinophilic esophagitis is a recently recognized but expanding disorder characterized by antigen-driven
    eosinophil accumulation in the esophagus.
  explanation: Establishes antigen-driven eosinophil accumulation as a central EoE mechanism.
- reference: PMID:19596009
  reference_title: Biology and treatment of eosinophilic esophagitis.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: The pathogenesis of eosinophilic esophagitis involves environmental and genetic factors, particularly
    food antigens and expression level of the eosinophil chemoattractant eotaxin-3, respectively.
  explanation: Links food antigens and eotaxin-3/CCL26 biology within the mechanistic model.
- reference: PMID:29980278
  reference_title: Epithelial origin of eosinophilic esophagitis.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Furthermore, genetic and functional data establish a primary role for impaired epithelial barrier
    function in disease susceptibility and pathoetiology.
  explanation: Supports the epithelial barrier component of the model.
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

# Barrier-Antigen Type 2 Specificity Model for Eosinophilic Esophagitis: Hypothesis Evaluation Report

**Hypothesis ID:** `barrier_antigen_type2_specificity_model`  
**Disease:** Eosinophilic Esophagitis (EoE)  
**Category:** Complex  
**Status in KB:** EMERGING  
**Report Date:** 2026-06-04  
**Papers Reviewed:** 100  
**Confirmed Findings:** 6  

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — core axis approaching ESTABLISHED; antigen specificity arm remains UNRESOLVED**

The Barrier-Antigen Type 2 Specificity Model posits that esophageal epithelial barrier dysfunction increases exposure to food and aeroallergen antigens, triggering epithelial alarmin release (TSLP, IL-33), which polarizes local ILC2/Th2 inflammation and IL-5/IL-13 responses, culminating in CCL26-mediated eosinophil recruitment. This investigation, drawing on 100 primary papers and reviews, finds that the **core mechanistic axis — from barrier dysfunction through alarmin release to IL-13-driven eotaxin-3 induction and eosinophil recruitment — is strongly supported** by converging genetic, functional, transcriptomic, and clinical trial evidence. However, three critical caveats prevent a full upgrade to ESTABLISHED status:

1. **Food antigen specificity is mechanistically unresolved.** The hypothesis correctly identifies this as an "open mechanistic subproblem." EoE is non-IgE-mediated, conventional allergy testing has poor predictive value for dietary triggers, and the immunological pathway by which individual patients select their trigger foods remains unknown.

2. **Eosinophils may not be the primary symptom mediators.** Anti-IL-5 therapy (mepolizumab, reslizumab) reduces esophageal eosinophils but fails to improve symptoms, while mast cells persist in remission subgroups and independently disrupt barrier function. The model's terminal step (CCL26 → eosinophil recruitment → disease) oversimplifies symptom pathogenesis.

3. **Molecular heterogeneity exists within the type 2 axis.** Unsupervised clustering of 312 patients across 10 sites reveals at least five molecular subgroups with distinct cytokine expression profiles that are not proportional to disease severity, suggesting the single linear causal chain captures the dominant pathway but not the full disease landscape.

---

## Summary

Eosinophilic esophagitis (EoE) is a chronic, antigen-driven inflammatory disease of the esophagus with rising incidence over the past three decades. The Barrier-Antigen Type 2 Specificity Model provides the most comprehensive current framework for understanding EoE pathogenesis, proposing a linear causal chain from epithelial barrier disruption through type 2 immune polarization to eosinophilic tissue infiltration. This report evaluates each node in this causal chain against the available primary literature.

The investigation confirms that each major step in the core pathway has independent genetic and functional support. Genome-wide association studies identify epithelial barrier genes (CAPN14 at 2p23, DSP/PPL desmosomal variants) and alarmin genes (TSLP at 5q22) as EoE susceptibility loci. Functional studies demonstrate that IL-13 signaling through the type II IL-4 receptor on epithelial cells is necessary and sufficient for the EoE transcriptional program, and phase 3 trials of dupilumab (anti-IL-4Rα) achieving 60–68% histologic remission provide therapeutic validation. However, the model's claim of antigen-driven specificity — the "A" in "Barrier-**Antigen**-Type 2" — rests on the weakest evidence: elemental diets achieve ~91% remission confirming food-driven disease, but the immunological mechanism by which individual patients select their trigger foods remains unknown. This gap has direct clinical consequences, as no reliable test exists to predict dietary triggers.

Additionally, the model's implicit assumption that eosinophils are the terminal effectors causing symptoms is challenged by anti-IL-5 trial data showing eosinophil reduction without symptom benefit, and by emerging evidence that mast cells persist independently in remission subgroups and actively disrupt barrier function via oncostatin M signaling. The model therefore requires amendment to incorporate mast cells as parallel effectors and to explicitly flag eosinophils' role as potentially more pathological marker than symptom driver.

---

## Key Findings

### Finding 1: Epithelial Barrier Dysfunction Is Genetically and Functionally Central to EoE Pathogenesis

The upstream node of the hypothesis — that epithelial barrier dysfunction initiates disease — has the strongest multi-modal support of any component. GWAS identifies the **CAPN14** locus at 2p23 and **TSLP** at 5q22 as major EoE susceptibility loci, both encoding epithelial products. As established in a key review of the epithelial origin of EoE: "genetic and functional data establish a primary role for impaired epithelial barrier function in disease susceptibility and pathoetiology" ([PMID: 29980278](https://pubmed.ncbi.nlm.nih.gov/29980278/)). Rare heterozygous missense variants in the desmosome-associated genes **DSP** (desmoplakin) and **PPL** (periplakin) were identified in 21% of multiplex EoE families: "A series of rare, heterozygous, missense variants are identified in the genes encoding the desmosome-associated proteins DSP and PPL in 21% of the multiplex families" ([PMID: 34815391](https://pubmed.ncbi.nlm.nih.gov/34815391/)). These variants affect barrier integrity and are susceptible to CAPN14-mediated degradation, providing direct genetic evidence that barrier integrity defects segregate with disease in families.

Critically, barrier dysfunction is not merely a consequence of active inflammation but appears to be an intrinsic epithelial trait. Multi-omic profiling demonstrated that "Among the dysregulated genes (up-/downregulated 310/112) and proteins (up-/downregulated 68/16) between active EoE and controls, 17 genes, and 6 proteins remained dysregulated in inactive EoE" — including persistent DSG1 downregulation even in histologic remission ([PMID: 39343172](https://pubmed.ncbi.nlm.nih.gov/39343172/)). This persistence of molecular barrier defects in the absence of eosinophilic inflammation supports the model's claim that barrier disruption is upstream of, rather than secondary to, the inflammatory cascade.

Additional functional evidence comes from studies of **SPINK7** (a serine protease inhibitor lost in EoE epithelium that unleashes protease activity and alarmin release), the **IKKβ/NF-κB** pathway (whose conditional epithelial knockout exacerbates experimental EoE; [PMID: 39724973](https://pubmed.ncbi.nlm.nih.gov/39724973/)), and the **LOX/BMP axis** (which restores epithelial differentiation and barrier function even in the presence of IL-13 stimulation; [PMID: 38340809](https://pubmed.ncbi.nlm.nih.gov/38340809/)).

### Finding 2: TSLP and IL-33 Have Non-Redundant Roles as Upstream Alarmins Driving Type 2 Inflammation

The alarmin node of the hypothesis is supported by both overexpression data and knockout studies. TSLP and IL-33 are overexpressed in both human and experimental EoE. A pivotal study demonstrated that "TSLP and IL-33 have non-redundant functions in experimental EoE. This study highlights TSLP as an upstream regulator of IL-13 and a potential therapeutic target for EoE" ([PMID: 40060399](https://pubmed.ncbi.nlm.nih.gov/40060399/)). Esophageal mast cells display the highest TSLPR expression among immune cells, positioning them as a critical alarmin-responsive cell population.

In a complementary model, IL-33-induced eosinophilia was **ablated in IL-13 null mice** — "IL-33-induced eosinophilia was ablated in IL-13 null mice" ([PMID: 26514775](https://pubmed.ncbi.nlm.nih.gov/26514775/)) — demonstrating that IL-33 drives EoE-like pathology through an IL-13-dependent mechanism. This places both alarmins upstream of IL-13 in the causal chain but via distinct pathways — TSLP primarily through TSLPR on mast cells and possibly ILC2s, IL-33 through ST2 on ILC2s and T cells.

The TSLP locus at 5q22 is one of the most replicated GWAS hits for EoE, and eQTL studies show that protective alleles (rs3806932, rs2416257) correlate with decreased TSLP expression in bronchial epithelial cells ([PMID: 26119467](https://pubmed.ncbi.nlm.nih.gov/26119467/)), though esophageal-specific eQTL data remain limited.

### Finding 3: IL-13 Signaling via Type II IL-4 Receptor on Epithelial Cells Is the Definitive Effector Pathway

The IL-13/epithelial cell node represents perhaps the single best-validated edge in the entire causal chain. Targeted deletion of IL-13Rα1 in esophageal epithelial cells renders mice fully protected from experimental EoE, and "Single-cell RNA sequencing analysis of human EoE biopsies revealed predominant expression of IL-13Rα1 in epithelial cells and that EoE signature genes correlated with IL-13 expression compared with IL-4" ([PMID: 36070083](https://pubmed.ncbi.nlm.nih.gov/36070083/)).

Therapeutic validation comes from the landmark **LIBERTY EoE TREET** phase 3 trial of dupilumab, which "blocks the shared receptor component for interleukin-4 and interleukin-13, which have key roles in eosinophilic esophagitis" ([PMID: 36546624](https://pubmed.ncbi.nlm.nih.gov/36546624/)). In adults/adolescents, dupilumab achieved histologic remission (≤6 eos/hpf) in approximately 60% vs. 5% placebo (Part A: 25/42 vs 2/39; difference 55 percentage points, 95% CI 40–71, P < 0.001). In children aged 1–11, higher-exposure dupilumab achieved 68% vs. 3% remission (difference 65 pp, 95% CI 48–81, P < 0.001) ([PMID: 38924731](https://pubmed.ncbi.nlm.nih.gov/38924731/)). These effects were maintained through 52 weeks ([PMID: 37660704](https://pubmed.ncbi.nlm.nih.gov/37660704/)).

The conserved EoE transcriptome across Japanese and Western patients further supports IL-13 as the central hub: microarray analysis showed strong overlap in IL-13-inducible and eosinophil-related gene signatures, including CCL26/eotaxin-3 ([PMID: 26117258](https://pubmed.ncbi.nlm.nih.gov/26117258/)). IL-13 also drives eotaxin-3 expression in fibroblasts via the JAK-STAT6 pathway, extending the effector mechanism to subepithelial tissue ([PMID: 27310888](https://pubmed.ncbi.nlm.nih.gov/27310888/)).

{{figure:evidence_matrix.png|caption=Evidence matrix summarizing support level, evidence type, and confidence for each mechanistic claim in the Barrier-Antigen Type 2 Specificity Model}}

### Finding 4: Anti-IL-5 Reduces Eosinophils but Not Symptoms, Dissociating Eosinophilia from Clinical Manifestations

A critical challenge to the model's implicit endpoint — that eosinophil recruitment causes symptoms — comes from anti-IL-5 trials. "Mepolizumab and reslizumab, two anti-IL-5 antibodies, were studied in children and adults with EoE and resulted in reduction of esophageal tissue and blood eosinophils, but no significant reduction in symptoms" ([PMID: 29372536](https://pubmed.ncbi.nlm.nih.gov/29372536/)). Network meta-analysis ranks anti-IL-5 agents below topical corticosteroids and anti-IL-13 biologics for overall efficacy ([PMID: 32398629](https://pubmed.ncbi.nlm.nih.gov/32398629/)).

This finding has profound implications: it suggests that the model's terminal step (CCL26 → eosinophil recruitment → symptoms/tissue damage) is incomplete. The disease phenotype likely arises from the broader IL-13-driven epithelial reprogramming — including barrier dysfunction, basal cell hyperplasia, fibrosis via TGF-β, and mast cell activation — rather than eosinophil infiltration per se. In contrast, dupilumab's efficacy in both reducing eosinophils *and* improving symptoms supports IL-13 as the more proximal disease driver, acting on the epithelium directly rather than solely through eosinophil-mediated tissue damage.

### Finding 5: Food Antigen Specificity in EoE Is Non-IgE Mediated and Mechanistically Unresolved

The "Antigen" component of the model is paradoxically both clinically validated and mechanistically opaque. Elemental (amino acid-based) diets achieve ~90.8% remission rates, definitively confirming that food antigens drive disease. Cow's milk is the single most common trigger, with >60% of pediatric patients responding to milk elimination alone ([PMID: 39861395](https://pubmed.ncbi.nlm.nih.gov/39861395/)).

However, the immunological mechanism of food trigger selection remains unknown. "Although food has been recognized as a trigger factor of EoE, the mechanism by which it initiates or facilitates eosinophilic inflammation appears to be largely independent of IgE and needs to be further investigated" ([PMID: 26799684](https://pubmed.ncbi.nlm.nih.gov/26799684/)). Furthermore, "EoE is not a classical IgE-mediated food allergy, and conventional allergy tests have a poor predictive value in guiding dietary interventions" ([PMID: 41423303](https://pubmed.ncbi.nlm.nih.gov/41423303/)). Anti-IgE therapy (omalizumab) is ineffective in EoE. Delayed-type T-cell hypersensitivity is considered the most likely mechanism, but the antigen-presenting pathway, the role of IgG4 (which may be a bystander), and the molecular basis for why specific individuals react to specific foods remain uncharacterized.

Aeroallergens represent an additional complicating factor. One study demonstrated that six-food elimination diet (SFED) response dropped from 77.3% to 21.4% during pollen season in pollen-sensitized patients (P = 0.003) ([PMID: 37307575](https://pubmed.ncbi.nlm.nih.gov/37307575/)), and case reports of EoE induced by sublingual immunotherapy ([PMID: 38567182](https://pubmed.ncbi.nlm.nih.gov/38567182/)) support a role for aeroallergens in a subset of patients. However, the overall weight of evidence suggests aeroallergens play a modifying rather than primary role ([PMID: 29356936](https://pubmed.ncbi.nlm.nih.gov/29356936/)).

### Finding 6: Mast Cells Are Major but Underappreciated Effectors in EoE Pathogenesis

Mast cells emerge from this investigation as a parallel effector population that may explain the gap between eosinophil reduction and symptom persistence. "Mast cells (MCs) accumulate in the epithelium of patients with eosinophilic esophagitis (EoE), an inflammatory disorder characterized by extensive esophageal eosinophilic infiltration. Esophageal barrier dysfunction plays an important role in the pathophysiology of EoE" ([PMID: 37302713](https://pubmed.ncbi.nlm.nih.gov/37302713/)). IgE-activated mast cells decrease epithelial resistance by 30% and increase permeability by 22% via oncostatin M (OSM) signaling, which also downregulates filaggrin, DSG1, and involucrin.

Critically, "whereas epithelial mast cells and eosinophils were high in active EoE, some patients in remission, e.g. normalised epithelial eosinophils, showed remaining high numbers of mast cells" ([PMID: 29772120](https://pubmed.ncbi.nlm.nih.gov/29772120/)). This persistence of mast cells independent of eosinophils during remission suggests an independent pathogenic role. Machine learning analysis of esophageal biopsies shows mast cell density correlates with epithelial eosinophilia, basal zone hyperplasia, and lamina propria fibrosis ([PMID: 38395083](https://pubmed.ncbi.nlm.nih.gov/38395083/)).

Mast cells also display the highest TSLPR expression among esophageal immune cells ([PMID: 40060399](https://pubmed.ncbi.nlm.nih.gov/40060399/)), directly linking them to the alarmin arm of the model and suggesting they may be a primary cellular transducer of TSLP signals, creating a potential positive feedback loop: barrier dysfunction → alarmin release → mast cell activation → further barrier disruption via OSM.

---

## Mechanistic Model / Causal Chain

The following diagram represents the causal chain implied by the hypothesis, annotated with evidence strength at each node:

```
UPSTREAM TRIGGERS (Genetic susceptibility + Environmental factors)
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ EPITHELIAL BARRIER DYSFUNCTION                                  │  ◀── ESTABLISHED
│ (CAPN14, DSP/PPL variants, DSG1↓, SPINK7 loss, IKKβ pathway)  │      GWAS + functional + persistent in remission
└──────────────────────────┬──────────────────────────────────────┘
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
┌──────────────────┐              ┌──────────────────────────┐
│ FOOD/AEROALLERGEN│              │ ALARMIN RELEASE           │  ◀── ESTABLISHED
│ PENETRATION      │              │ (TSLP, IL-33, IL-25)      │      (overexpression + non-redundant
│                  │              └──────────┬───────────────┘       KO data + GWAS)
│  ◀── UNRESOLVED  │                        │
│  (non-IgE; T-cell│         ┌──────────────┼──────────────┐
│   mechanism?)    │         ▼              ▼              ▼
└──────────────────┘  ┌───────────┐  ┌───────────┐  ┌──────────────┐
                      │ ILC2      │  │ Th2 cells │  │ MAST CELLS   │
                      │ expansion │  │ (IL-4,    │  │ (TSLPR-high, │ ◀── EMERGING
                      └─────┬─────┘  │ IL-13)    │  │  CPA3,       │
                            │        └─────┬─────┘  │  tryptase)   │
                            │              │        └──────┬───────┘
                            └──────┬───────┘               │
                                   ▼                       │
                      ┌────────────────────────┐           │
                      │ IL-5 / IL-13 SECRETION │           │
                      └──────────┬─────────────┘           │
                                 │                         │
                    ┌────────────┴──────────┐              │
                    ▼                       ▼              ▼
         ┌────────────────┐     ┌──────────────────┐  ┌─────────────────┐
         │ EPITHELIAL     │     │ CCL26/EOTAXIN-3  │  │ BARRIER DISRUPT │
         │ REPROGRAMMING  │     │ INDUCTION →      │  │ VIA OSM         │
         │ (BZH, EMT,     │     │ EOSINOPHIL       │  │ (DSG1↓,         │
         │  fibrosis)     │     │ RECRUITMENT      │  │  filaggrin↓)    │
         └────────────────┘     └────────┬─────────┘  └────────┬────────┘
                                         │                     │
                    ◀── ESTABLISHED ─────┤         POSITIVE    │
                     (CCL26 most over-   │        FEEDBACK ────┘
                      expressed gene;    │          LOOP
                      JAK-STAT6)         ▼
                              ┌────────────────────┐
                              │ TISSUE EOSINOPHILIA│
                              │ (≥15 eos/hpf)     │
                              └────────┬───────────┘
                                       │
                              ◀── QUALIFIED (anti-IL-5
                                   reduces eos but
                                   NOT symptoms)
                                       ▼
                           ┌──────────────────────┐
                           │ CLINICAL DISEASE      │
                           │ (dysphagia, food      │
                           │  impaction,            │
                           │  fibrostenosis)        │
                           └──────────────────────┘
```

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram for the Barrier-Antigen Type 2 Specificity Model, showing evidence strength at each node}}

**Strong links (ESTABLISHED):** Barrier dysfunction → alarmin release → IL-13 secretion → CCL26/eotaxin-3 induction → eosinophil recruitment. Each has independent genetic, functional, and/or pharmacological validation.

**Weak/missing links:** (1) Allergen penetration → immune recognition (non-IgE mechanism unknown); (2) Eosinophil infiltration → clinical symptoms (dissociated by anti-IL-5 data); (3) Mast cell activation → symptom generation (emerging but not yet causally tested in humans).

**Feedback loop:** IL-13-induced CAPN14 expression degrades DSP/PPL, further compromising the barrier and creating a self-amplifying cycle ([PMID: 34815391](https://pubmed.ncbi.nlm.nih.gov/34815391/)).

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|-------------------|-------------|---------|------------|
| 1 | [PMID: 29980278](https://pubmed.ncbi.nlm.nih.gov/29980278/) | Human genetic/functional | **SUPPORT** | Barrier dysfunction is primary | GWAS loci (CAPN14, TSLP) encode epithelial products; SPINK7 loss triggers alarmin release | All EoE | HIGH |
| 2 | [PMID: 34815391](https://pubmed.ncbi.nlm.nih.gov/34815391/) | Human genetic + in vitro | **SUPPORT** | Desmosomal variants → barrier defect | DSP/PPL rare variants in 21% of multiplex families; susceptible to CAPN14 degradation | Familial EoE | HIGH |
| 3 | [PMID: 39343172](https://pubmed.ncbi.nlm.nih.gov/39343172/) | Human clinical (multi-omic) | **SUPPORT + QUALIFIES** | Persistent barrier defects in remission | DSG1 downregulation and 17 genes/6 proteins remain dysregulated in inactive EoE | Active + inactive EoE | HIGH |
| 4 | [PMID: 40060399](https://pubmed.ncbi.nlm.nih.gov/40060399/) | Model organism (mouse KO) | **SUPPORT** | TSLP/IL-33 non-redundant alarmins | TSLP upstream of IL-13; distinct from IL-33; mast cells express highest TSLPR | Experimental EoE | HIGH |
| 5 | [PMID: 26514775](https://pubmed.ncbi.nlm.nih.gov/26514775/) | Model organism (mouse) | **SUPPORT** | IL-33 → IL-13 → EoE | IL-33-induced eosinophilia ablated in IL-13 null mice | Experimental EoE | HIGH |
| 6 | [PMID: 36070083](https://pubmed.ncbi.nlm.nih.gov/36070083/) | Model organism + human scRNA-seq | **SUPPORT** | Epithelial IL-13Rα1 is essential | Epithelial-specific IL-13Rα1 KO protects from EoE; IL-13 > IL-4 in driving EoE genes | Experimental + human | VERY HIGH |
| 7 | [PMID: 36546624](https://pubmed.ncbi.nlm.nih.gov/36546624/) | Human RCT (Phase 3) | **SUPPORT** | IL-4/IL-13 blockade treats EoE | Dupilumab: ~60% vs 5% histologic remission (P < 0.001) | Adults/adolescents | VERY HIGH |
| 8 | [PMID: 38924731](https://pubmed.ncbi.nlm.nih.gov/38924731/) | Human RCT (Phase 3) | **SUPPORT** | Type 2 axis validated in children | Dupilumab: 68% vs 3% remission (P < 0.001) | Children 1–11 yr | VERY HIGH |
| 9 | [PMID: 37660704](https://pubmed.ncbi.nlm.nih.gov/37660704/) | Human RCT (Phase 3) | **SUPPORT** | Long-term efficacy maintained | Histologic and symptomatic improvements sustained through 52 weeks | Adults/adolescents | VERY HIGH |
| 10 | [PMID: 29372536](https://pubmed.ncbi.nlm.nih.gov/29372536/) | Review of RCTs | **QUALIFIES** | Eosinophils ≠ primary symptom drivers | Anti-IL-5 reduces eos but not symptoms | Adults and children | HIGH |
| 11 | [PMID: 26799684](https://pubmed.ncbi.nlm.nih.gov/26799684/) | Human clinical | **QUALIFIES** | Food triggers are non-IgE | Food-triggered EoE is largely IgE-independent; mechanism needs investigation | All EoE | HIGH |
| 12 | [PMID: 41423303](https://pubmed.ncbi.nlm.nih.gov/41423303/) | Review + clinical | **QUALIFIES** | Allergy tests predict triggers poorly | Conventional allergy tests have poor predictive value for EoE dietary triggers | All EoE | HIGH |
| 13 | [PMID: 37302713](https://pubmed.ncbi.nlm.nih.gov/37302713/) | In vitro + human tissue | **COMPETING** | Mast cells disrupt barrier via OSM | IgE-activated MCs decrease epithelial resistance 30%, increase permeability 22% | EoE epithelium | MODERATE–HIGH |
| 14 | [PMID: 29772120](https://pubmed.ncbi.nlm.nih.gov/29772120/) | Human clinical | **QUALIFIES** | Mast cells persist in remission | Epithelial MCs remain elevated in subgroup with normalized eosinophils | Treated EoE | MODERATE |
| 15 | [PMID: 38395083](https://pubmed.ncbi.nlm.nih.gov/38395083/) | Computational + human tissue | **SUPPORTS (mast cell role)** | MC density correlates with pathology | MC density correlates with BZH, eosinophilia, LP fibrosis; increased degranulation | EoE biopsies | MODERATE |
| 16 | [PMID: 32197970](https://pubmed.ncbi.nlm.nih.gov/32197970/) | Human clinical (multisite) | **QUALIFIES** | Type 2 heterogeneity | 5 molecular subgroups; type 2 expression not proportional to disease features | n = 312, 10 sites | HIGH |
| 17 | [PMID: 37307575](https://pubmed.ncbi.nlm.nih.gov/37307575/) | Human clinical | **SUPPORTS** | Aeroallergens contribute | SFED: 21.4% vs 77.3% response during vs outside pollen season (P = 0.003) | Pollen-sensitized adults | MODERATE |
| 18 | [PMID: 34627858](https://pubmed.ncbi.nlm.nih.gov/34627858/) | Model organism + human | **QUALIFIES** | Microbiome modulates EoE | Antibiotic-induced dysbiosis exacerbates EoE; Lactobacillales lost in EoE | Experimental + clinical | MODERATE |
| 19 | [PMID: 39884574](https://pubmed.ncbi.nlm.nih.gov/39884574/) | Human scRNA-seq + in vitro | **QUALIFIES** | IFN-γ disrupts barrier | IFN-γ from CD8+ T cells disrupts differentiation, barrier, induces apoptosis | Active EoE | MODERATE |
| 20 | [PMID: 41865802](https://pubmed.ncbi.nlm.nih.gov/41865802/) | Human GWAS meta-analysis | **SUPPORTS** | Shared atopic genetic architecture | MTAG expanded risk loci; improved PRS; shared genetic underpinnings with atopy | European ancestry | HIGH |
| 21 | [PMID: 29129581](https://pubmed.ncbi.nlm.nih.gov/29129581/) | Human genetic | **SUPPORTS** | EoE-specific + atopic gene synergy | CAPN14/TSLP are EoE-specific; IL4/KIF3A and other atopic loci synergize | n = 700 cases | HIGH |
| 22 | [PMID: 26117258](https://pubmed.ncbi.nlm.nih.gov/26117258/) | Human transcriptomic | **SUPPORTS** | Conserved IL-13/CCL26 signature | Japanese and US EoE patients share IL-13-inducible transcriptome including CCL26 | Cross-population | MODERATE |
| 23 | [PMID: 24323578](https://pubmed.ncbi.nlm.nih.gov/24323578/) | Human + in vitro | **SUPPORTS** | Epigenetic CCL26 regulation | CCL26 promoter hypomethylated in allergic tissue; inversely correlates with expression | Allergic vs control | MODERATE |
| 24 | [PMID: 27310888](https://pubmed.ncbi.nlm.nih.gov/27310888/) | In vitro | **SUPPORTS** | JAK-STAT6 in fibroblasts | Th2 cytokines drive eotaxin-3 in fibroblasts via JAK-STAT6; JAK inhibitors block it | EoE fibroblasts | MODERATE |
| 25 | [PMID: 39724973](https://pubmed.ncbi.nlm.nih.gov/39724973/) | Model organism | **SUPPORTS** | Epithelial IKKβ maintains homeostasis | IKKβ knockout in esophageal epithelium exacerbates experimental EoE | Mouse model | MODERATE |

---

## Limitations and Knowledge Gaps

### Gap 1: Food Antigen Specificity Mechanism (CRITICAL)

**Scope:** The mechanism by which individual patients develop immune responses to specific food antigens is entirely unknown.  
**Why it matters:** This is the central "open mechanistic subproblem" acknowledged in the seed hypothesis and has direct clinical consequences — no reliable diagnostic test exists to predict food triggers, forcing empiric elimination diets with serial endoscopies. Elemental diet (~91% remission) confirms food-driven disease, but predicting *which* foods for *which* patients remains impossible.  
**What was checked:** Literature on IgE, IgG4, T-cell responses, FIRE phenomenon, allergy testing accuracy, elemental diet outcomes, and omalizumab trial data.  
**Resolution needed:** Antigen-specific T-cell repertoire studies from esophageal biopsies; single-cell TCR sequencing of esophageal T cells before and after food reintroduction; HLA typing in dietary responder cohorts; in vitro antigen presentation assays with patient-specific food proteins.

### Gap 2: Eosinophil vs. Mast Cell Contribution to Symptoms (HIGH PRIORITY)

**Scope:** Anti-IL-5 data dissociate eosinophil counts from symptom improvement, but no trial has specifically targeted mast cells in EoE.  
**Why it matters:** If mast cells are the primary symptom mediators, eosinophil-based monitoring (the current clinical standard) may miss clinically relevant disease activity, and treatment targeting should shift accordingly.  
**What was checked:** Anti-IL-5 trials (mepolizumab, reslizumab), mast cell persistence studies, OSM signaling data, fibroblast transcriptomic studies, MC-AI computational analysis.  
**Resolution needed:** A clinical trial of mast cell-targeted therapy (e.g., anti-SIGLEC-8 lirentelimab, anti-KIT inhibitor) with both eosinophil and symptom endpoints; co-monitoring of mast cell and eosinophil counts with validated symptom scores.

### Gap 3: Barrier Dysfunction — Cause or Consequence?

**Scope:** Directionality of the barrier-inflammation relationship.  
**Why it matters:** Determines whether barrier-targeted therapies would be preventive or merely palliative.  
**What was checked:** GWAS evidence, persistence in remission, functional studies, conditional knockout models.  
**Current state:** Genetic evidence (CAPN14, DSP/PPL) and persistent DSG1 downregulation in remission favor a primary barrier defect. However, IL-13 itself impairs barrier function, creating a feedback loop. The initial trigger vs. amplification mechanism remains ambiguous.  
**Resolution needed:** Longitudinal birth cohort studies in at-risk individuals with serial barrier function measurements before disease onset; conditional barrier-gene rescue in animal models.

### Gap 4: Type 2 Molecular Heterogeneity (MODERATE)

**Scope:** Unsupervised clustering of 312 patients identified 5 molecular subgroups with heterogeneous type 2 gene expression that was not proportional to disease features ([PMID: 32197970](https://pubmed.ncbi.nlm.nih.gov/32197970/)).  
**Why it matters:** The model assumes a uniform pathway, but molecular endotypes may require distinct therapeutic strategies.  
**Resolution needed:** Prospective molecular endotyping linked to treatment response data; endotype-stratified clinical trials.

### Gap 5: IFN-γ/Type 1 Immune Contribution (EMERGING)

**Scope:** scRNA-seq studies identify upregulated interferon response signature genes in EoE epithelium, with IFN-γ from CD8+ T cells disrupting barrier function and inducing apoptosis via caspase activation ([PMID: 39884574](https://pubmed.ncbi.nlm.nih.gov/39884574/)).  
**Why it matters:** Represents a non-type-2 pathway that could explain treatment-refractory cases.  
**Resolution needed:** IFN-γ blockade in EoE patients refractory to type 2-targeted therapy; characterization of CD8+ T cell clones in EoE tissue.

### Gap 6: Source-Level and Dataset Absences

- **No GenCC or ClinGen curated gene-disease validity assertions** specific to EoE were identified in this search
- **No completed randomized trial of anti-TSLP (tezepelumab)** in EoE despite TSLP being a GWAS-implicated and functionally validated target
- **No large-scale longitudinal cohort data** tracking barrier dysfunction biomarkers prospectively before EoE onset
- **No esophageal-specific eQTL data** for TSLP or CAPN14 loci (available data derives from bronchial epithelium)
- **Limited ancestry diversity**: Most GWAS are in European populations; one African American study identified ancestry-specific loci ([PMID: 36400179](https://pubmed.ncbi.nlm.nih.gov/36400179/)) but replication is needed
- **No published single-cell profiling of ILC2 specifically in human EoE tissue** (ILC2 evidence is primarily from mouse models)

---

## Alternative Models

### 1. Mast Cell-Centric Effector Model
**Relationship to seed hypothesis:** Parallel/competing effector pathway  
Mast cells, not eosinophils, may be the primary disease effectors. MCs disrupt barrier function via OSM ([PMID: 37302713](https://pubmed.ncbi.nlm.nih.gov/37302713/)), persist in remission independently of eosinophils ([PMID: 29772120](https://pubmed.ncbi.nlm.nih.gov/29772120/)), and may drive esophageal dysmotility and even achalasia-like presentations ([PMID: 33355505](https://pubmed.ncbi.nlm.nih.gov/33355505/)). This model is complementary to the seed hypothesis but challenges its emphasis on eosinophils as terminal effectors.

### 2. Epithelial-Intrinsic Model (SPINK7/Protease/Alarmin Cascade)
**Relationship:** Upstream refinement of seed hypothesis  
The primary defect is epithelial-intrinsic loss of SPINK7, which unleashes proteolytic activity, damages barrier integrity, and autonomously triggers alarmin release and type 2 inflammation without requiring antigen penetration as a necessary intermediate step ([PMID: 29980278](https://pubmed.ncbi.nlm.nih.gov/29980278/)). This may explain how barrier dysfunction alone could initiate inflammation.

### 3. Microbiome–Barrier–Immune Axis
**Relationship:** Upstream environmental modifier  
Early-life microbiome disruption (loss of Lactobacillales) alters esophageal epithelial gene expression including barrier function genes, priming the tissue for exaggerated type 2 inflammation upon allergen exposure ([PMID: 34627858](https://pubmed.ncbi.nlm.nih.gov/34627858/)). Complementary to the seed hypothesis; provides an environmental context for barrier dysfunction development.

### 4. IFN-γ / Mixed Immune Model
**Relationship:** Parallel/modifying pathway  
IFN-γ from CD8+ T cells disrupts esophageal epithelial differentiation, barrier integrity, and induces apoptosis via caspase activation ([PMID: 39884574](https://pubmed.ncbi.nlm.nih.gov/39884574/)). Suggests the immune environment in EoE is not purely type 2 and could explain molecular heterogeneity and treatment-refractory subgroups.

### 5. Fibrosis-Remodeling as Independent Disease Driver
**Relationship:** Downstream parallel pathway  
TGF-β-driven fibrosis and subepithelial remodeling may become self-sustaining independently of ongoing type 2 inflammation, explaining treatment-refractory fibrostenotic disease. Nonepithelial gene expression (predominantly fibroblast-derived) correlates more strongly with symptom severity than epithelial genes ([PMID: 38768900](https://pubmed.ncbi.nlm.nih.gov/38768900/)).

### 6. Epigenetic Priming Model
**Relationship:** Upstream/complementary  
Demethylation of the CCL26 promoter inversely correlates with eotaxin-3 expression in allergic tissue ([PMID: 24323578](https://pubmed.ncbi.nlm.nih.gov/24323578/)). Amniotic fluid exposure modifies esophageal epithelial differentiation and IL-13 responsiveness ([PMID: 39189791](https://pubmed.ncbi.nlm.nih.gov/39189791/)). Early-life epigenetic programming may predispose to EoE.

---

## Proposed Discriminating Tests and Follow-up Experiments

### Test 1: Antigen-Specific T-Cell Profiling After Controlled Food Challenge
- **Purpose:** Resolve the food antigen specificity gap — the most critical unknown
- **Patient stratification:** Active EoE patients on elemental diet achieving remission, then single-food reintroduction (e.g., milk)
- **Sample type:** Esophageal biopsies + paired blood
- **Assay:** Single-cell TCR-seq + antigen-loaded tetramer/multimer staining; HLA typing
- **Expected result if hypothesis correct:** Clonal expansion of food-specific T cells in esophageal tissue after trigger food reintroduction; shared TCR motifs across patients responding to the same food
- **If negative:** Food antigen specificity may be stochastic or governed by non-TCR mechanisms

### Test 2: Mast Cell-Targeted Therapy Trial
- **Purpose:** Discriminate mast cell vs. eosinophil contributions to symptoms
- **Patient stratification:** EoE patients with persistent symptoms despite eosinophil depletion (anti-IL-5) OR patients in eosinophil remission with persistent mast cells
- **Intervention:** Anti-SIGLEC-8 (lirentelimab) or anti-KIT inhibitor
- **Biomarkers:** Tryptase, CPA3, OSM in biopsies; DSQ and EEsAI symptom scores
- **Expected result if MC-centric model holds:** Symptom improvement independent of eosinophil change

### Test 3: Anti-TSLP (Tezepelumab) Trial in EoE
- **Purpose:** Test whether upstream alarmin blockade is as/more effective than downstream cytokine blockade
- **Design:** Phase 2 RCT stratified by TSLP genotype (rs3806932)
- **Expected result if alarmin axis is critical:** Histologic and symptomatic improvement; genotype-dependent response
- **If negative:** TSLP may be redundant with IL-33; downstream IL-13 blockade may be sufficient

### Test 4: Longitudinal Birth Cohort with Barrier Biomarkers
- **Purpose:** Determine whether barrier dysfunction precedes inflammation (barrier-first vs. inflammation-first)
- **Cohort:** High-risk neonates (family history of EoE/atopy)
- **Sampling:** Serial esophageal string tests or Cytosponge for barrier markers (DSG1, SPINK7, CAPN14), microbiome profiling, dietary exposure tracking
- **Expected result if barrier-first model correct:** Barrier marker abnormalities detectable before first EoE diagnosis

### Test 5: Molecular Endotype-Guided Therapy Trial
- **Design:** Prospective stratification of EoE patients by the 5 molecular subgroups ([PMID: 32197970](https://pubmed.ncbi.nlm.nih.gov/32197970/)) followed by randomization to dupilumab vs. anti-TSLP vs. dietary elimination
- **Expected result:** Differential treatment response by endotype; high-TSLP/CCL26 subgroups responding better to anti-TSLP, high-IL-13 subgroups to dupilumab
- **Impact:** Would enable personalized treatment selection in EoE

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base, requiring curator verification.*

### Candidate Evidence References (with verified snippets)

1. **[PMID: 40060399](https://pubmed.ncbi.nlm.nih.gov/40060399/)** — Supports TSLP → IL-13 edge upgrade. Verified snippet: "TSLP and IL-33 have non-redundant functions in experimental EoE. This study highlights TSLP as an upstream regulator of IL-13 and a potential therapeutic target for EoE."

2. **[PMID: 36070083](https://pubmed.ncbi.nlm.nih.gov/36070083/)** — Supports epithelial IL-13 signaling as ESTABLISHED. Verified snippet: "Single-cell RNA sequencing analysis of human EoE biopsies revealed predominant expression of IL-13Rα1 in epithelial cells and that EoE signature genes correlated with IL-13 expression compared with IL-4."

3. **[PMID: 34815391](https://pubmed.ncbi.nlm.nih.gov/34815391/)** — Supports barrier gene variants edge. Verified snippet: "A series of rare, heterozygous, missense variants are identified in the genes encoding the desmosome-associated proteins DSP and PPL in 21% of the multiplex families."

4. **[PMID: 29372536](https://pubmed.ncbi.nlm.nih.gov/29372536/)** — Qualifies eosinophil-to-symptom edge. Verified snippet: "Mepolizumab and reslizumab, two anti-IL-5 antibodies, were studied in children and adults with EoE and resulted in reduction of esophageal tissue and blood eosinophils, but no significant reduction in symptoms."

5. **[PMID: 37302713](https://pubmed.ncbi.nlm.nih.gov/37302713/)** — Candidate new edge: mast cell → barrier disruption via OSM. Verified snippet: "Mast cells (MCs) accumulate in the epithelium of patients with eosinophilic esophagitis (EoE), an inflammatory disorder characterized by extensive esophageal eosinophilic infiltration. Esophageal barrier dysfunction plays an important role in the pathophysiology of EoE."

6. **[PMID: 29772120](https://pubmed.ncbi.nlm.nih.gov/29772120/)** — Supports mast cell persistence as independent effector. Verified snippet: "Interestingly, whereas epithelial mast cells and eosinophils were high in active EoE, some patients in remission, e.g. normalised epithelial eosinophils, showed remaining high numbers of mast cells."

### Candidate Pathophysiology Nodes and Edges

| Type | Element | Status | Evidence |
|------|---------|--------|----------|
| New node | Mast cell (MCTC subtype) as parallel effector | EMERGING | PMID: 37302713, 29772120, 38395083 |
| New edge | TSLP → mast cell activation (via TSLPR) | EMERGING | PMID: 40060399 |
| New edge | Mast cell → OSM → barrier disruption (feedback loop) | EMERGING | PMID: 37302713 |
| Qualify edge | Eosinophil infiltration → symptoms | WEAKLY SUPPORTED | PMID: 29372536 |
| New edge | IFN-γ (CD8+ T cells) → epithelial barrier disruption | SPECULATIVE | PMID: 39884574 |
| New edge | Microbiome dysbiosis → barrier gene modification | SPECULATIVE | PMID: 34627858 |

### Candidate Ontology Terms

| Entity | Ontology | Term |
|--------|----------|------|
| Esophageal epithelial cell | CL | CL:0002252 |
| ILC2 | CL | CL:0001069 |
| Mast cell | CL | CL:0000097 |
| Eosinophil chemotaxis | GO | GO:0048245 |
| Type 2 immune response | GO | GO:0042092 |
| Mast cell degranulation | GO | GO:0043303 |
| TSLP signaling | Reactome | R-HSA-5362517 |
| IL-13 signaling | Reactome | R-HSA-6785807 |

### Candidate Status Changes

- **Core barrier → alarmin → IL-13 → CCL26 axis:** Consider splitting and upgrading to ESTABLISHED
- **Food antigen specificity mechanism:** Explicitly flag as UNRESOLVED knowledge_gap
- **Eosinophil as terminal symptom effector:** Downgrade from implicit ESTABLISHED → WEAKLY SUPPORTED
- **Mast cell effector arm:** Add as EMERGING parallel pathway
- **Overall hypothesis status:** Maintain EMERGING with annotation that core axis approaches ESTABLISHED while antigen specificity arm is UNRESOLVED

### Candidate Knowledge Gaps for KB

1. **food_antigen_specificity_mechanism:** Non-IgE mechanism of patient-specific food antigen selection is unknown; T cell-mediated delayed hypersensitivity is hypothesized but unconfirmed at the molecular level
2. **eosinophil_symptom_causation:** Whether eosinophils or mast cells are primary symptom drivers; anti-IL-5 trial data challenge eosinophil-centric view
3. **barrier_cause_vs_consequence:** Whether epithelial barrier dysfunction precedes or follows inflammation requires longitudinal pre-disease studies
4. **anti_TSLP_EoE_trial_absence:** No completed RCT of tezepelumab in EoE despite strong rationale
5. **ILC2_human_EoE_profiling_absence:** ILC2 evidence primarily from mouse models
6. **ancestry_diversity_gap:** Limited GWAS data outside European ancestry populations

---

*Report generated 2026-06-04. Based on systematic evaluation of 100 papers and 6 confirmed findings across 1 investigation iteration.*
