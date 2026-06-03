---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-03T09:44:22.937220'
end_time: '2026-06-03T10:15:53.121961'
duration_seconds: 1890.18
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
  category: Complex
  hypothesis_group_id: exertion_perfusion_muscle_immunometabolic_pem_model
  hypothesis_label: Exertion-Perfusion-Muscle Immunometabolic PEM Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: exertion_perfusion_muscle_immunometabolic_pem_model\n\
    hypothesis_label: Exertion-Perfusion-Muscle Immunometabolic PEM Model\nstatus:\
    \ EMERGING\ndescription: |\n  Physical or cognitive exertion unmasks impaired\
    \ peripheral oxygen extraction, microcirculation, skeletal muscle oxidative phosphorylation,\
    \ and ionic homeostasis; local metabolites and inflammatory mediators then amplify\
    \ autonomic and central nervous system dysfunction into delayed post-exertional\
    \ malaise.\nnotes: |\n  Seeded for issue #3665 as an integrated working model\
    \ rather than an established causal chain. It groups microvascular, skeletal-muscle,\
    \ mitochondrial, immune-metabolic, autonomic, and CNS amplification mechanisms\
    \ that may be subtype-specific or temporally staged.\nevidence:\n- reference:\
    \ PMID:39240417\n  reference_title: 'Towards an understanding of physical activity-induced\
    \ post-exertional malaise: Insights\n    into microvascular alterations and immunometabolic\
    \ interactions in post-COVID condition and myalgic\n    encephalomyelitis/chronic\
    \ fatigue syndrome.'\n  supports: SUPPORT\n  evidence_source: OTHER\n  snippet:\
    \ Aggravating deficits in tissue perfusion and oxygen utilization during activities\
    \ cause exertional\n    intolerance that are frequently accompanied by tachycardia,\
    \ dyspnea, early cessation of activity and\n    elicit downstream metabolic effects.\n\
    \  explanation: Review-level synthesis supports an exertion-to-perfusion/oxygen-utilization-to-metabolic-effects\n\
    \    chain relevant to PEM.\n- reference: PMID:31277442\n  reference_title: Post-Exertional\
    \ Malaise Is Associated with Hypermetabolism, Hypoacetylation and Purine\n   \
    \ Metabolism Deregulation in ME/CFS Cases.\n  supports: SUPPORT\n  evidence_source:\
    \ HUMAN_CLINICAL\n  snippet: The principal biochemical change related to the 7-day\
    \ severity of PEM was the fall in the purine\n    metabolite, hypoxanthine.\n\
    \  explanation: Human observational metabolomics links PEM severity over a 7-day\
    \ window to a biochemical\n    change in purine metabolism."
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
citation_count: 29
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** exertion_perfusion_muscle_immunometabolic_pem_model
- **Hypothesis Label:** Exertion-Perfusion-Muscle Immunometabolic PEM Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: exertion_perfusion_muscle_immunometabolic_pem_model
hypothesis_label: Exertion-Perfusion-Muscle Immunometabolic PEM Model
status: EMERGING
description: |
  Physical or cognitive exertion unmasks impaired peripheral oxygen extraction, microcirculation, skeletal muscle oxidative phosphorylation, and ionic homeostasis; local metabolites and inflammatory mediators then amplify autonomic and central nervous system dysfunction into delayed post-exertional malaise.
notes: |
  Seeded for issue #3665 as an integrated working model rather than an established causal chain. It groups microvascular, skeletal-muscle, mitochondrial, immune-metabolic, autonomic, and CNS amplification mechanisms that may be subtype-specific or temporally staged.
evidence:
- reference: PMID:39240417
  reference_title: 'Towards an understanding of physical activity-induced post-exertional malaise: Insights
    into microvascular alterations and immunometabolic interactions in post-COVID condition and myalgic
    encephalomyelitis/chronic fatigue syndrome.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Aggravating deficits in tissue perfusion and oxygen utilization during activities cause exertional
    intolerance that are frequently accompanied by tachycardia, dyspnea, early cessation of activity and
    elicit downstream metabolic effects.
  explanation: Review-level synthesis supports an exertion-to-perfusion/oxygen-utilization-to-metabolic-effects
    chain relevant to PEM.
- reference: PMID:31277442
  reference_title: Post-Exertional Malaise Is Associated with Hypermetabolism, Hypoacetylation and Purine
    Metabolism Deregulation in ME/CFS Cases.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The principal biochemical change related to the 7-day severity of PEM was the fall in the purine
    metabolite, hypoxanthine.
  explanation: Human observational metabolomics links PEM severity over a 7-day window to a biochemical
    change in purine metabolism.
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

# Mechanistic Hypothesis Evaluation: Exertion-Perfusion-Muscle Immunometabolic PEM Model in ME/CFS

**Hypothesis ID:** `exertion_perfusion_muscle_immunometabolic_pem_model`
**Status in KB:** EMERGING
**Report Date:** 2026-06-03

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED — the hypothesis should maintain EMERGING status.**

The Exertion-Perfusion-Muscle Immunometabolic PEM Model posits that physical or cognitive exertion unmasks impaired peripheral oxygen extraction, microcirculation, skeletal muscle oxidative phosphorylation, and ionic homeostasis, with local metabolites and inflammatory mediators then amplifying autonomic and central nervous system dysfunction into delayed post-exertional malaise (PEM). After systematic evaluation of 72 primary research papers and reviews, this report concludes that the model is **partially supported**: each of its major mechanistic nodes — impaired oxygen extraction, endothelial/microvascular dysfunction, skeletal muscle mitochondrial damage, purine/metabolic deregulation, and autonomic dysfunction — is individually backed by moderate-to-strong human clinical evidence. However, the causal chain linking these nodes sequentially from exertion trigger to PEM remains **inferred from cross-sectional data**, not demonstrated by perturbation or longitudinal studies. Critically, the ionic homeostasis component (Na+/Ca2+ overload in muscle) is entirely theoretical, lacking any direct human measurement in ME/CFS.

Important qualifying evidence limits the model's universality: a 2026 study failed to replicate the hallmark 2-day CPET decline; an early MRS study found normal muscle metabolism with central activation failure instead of peripheral dysfunction; and post-exercise cytokine studies have yielded inconsistent results. These findings suggest the model likely applies to specific ME/CFS subtypes rather than uniformly to all patients. The hypothesis remains the most comprehensive integrative framework for PEM pathophysiology in the current literature, but it requires formal causal testing — particularly vasodilator trials with invasive hemodynamic endpoints, 23Na-MRI of exercising muscle, and multi-timepoint immune profiling — before it can be promoted beyond EMERGING status.

---

## Summary

The Exertion-Perfusion-Muscle Immunometabolic PEM Model is an integrative working hypothesis that attempts to unify six distinct but overlapping pathophysiological domains in ME/CFS: (1) microvascular perfusion deficits, (2) impaired peripheral oxygen extraction, (3) skeletal muscle mitochondrial dysfunction, (4) metabolic derangements including purine metabolism deregulation, (5) autonomic nervous system dysfunction, and (6) CNS amplification of peripheral signals into the subjective experience of PEM. Our evidence search reveals that each of these nodes has at least one well-designed human clinical study providing direct support, but no single study has tested the complete causal chain from exertion trigger through to delayed symptom exacerbation.

The strongest direct evidence comes from invasive cardiopulmonary exercise testing (iCPET) demonstrating peripheral neurovascular dysregulation with impaired oxygen extraction ([PMID: 33577778](https://pubmed.ncbi.nlm.nih.gov/33577778/)), electron microscopy showing skeletal muscle mitochondrial damage with preferential subsarcolemmal localization ([PMID: 39727052](https://pubmed.ncbi.nlm.nih.gov/39727052/)), flow-mediated dilation studies confirming endothelial dysfunction ([PMID: 36730360](https://pubmed.ncbi.nlm.nih.gov/36730360/)), and metabolomics linking PEM severity to purine metabolism deregulation ([PMID: 31277442](https://pubmed.ncbi.nlm.nih.gov/31277442/)). However, the model faces challenges from evidence of central activation failure ([PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/)), a failure to replicate 2-day CPET declines in a 2026 study ([PMID: 42212259](https://pubmed.ncbi.nlm.nih.gov/42212259/)), and inconsistent cytokine responses to exercise. The hypothesis is best understood not as a single linear causal chain but as a network of interacting pathologies, likely varying in prominence across patient subtypes and disease stages.

---

## Key Findings

### Finding 1: Two-Day CPET Demonstrates Objective PEM with Impaired Oxygen Consumption — But with Heterogeneity

The 2-day cardiopulmonary exercise test (CPET) protocol is considered the most objective laboratory measure of PEM. A meta-analysis of 2-day CPET studies ([PMID: 33327624](https://pubmed.ncbi.nlm.nih.gov/33327624/)) found that ME/CFS patients show significant declines in VO2 and workload at the ventilatory threshold on day 2 versus day 1, while healthy controls improve. The difference between patients and controls was highly significant at workload at VT (overall mean: -10.8 at Test 1 vs. -33.0 at Test 2). The largest individual 2-day CPET study (n=84 ME/CFS, n=71 controls; [PMID: 38965566](https://pubmed.ncbi.nlm.nih.gov/38965566/)) confirmed that "unlike CTL, ME/CFS failed to reproduce CPET-1 measures during CPET-2 with significant declines at peak exertion in work, exercise time."

However, a critical qualifying finding emerged from a 2026 study by Mancini et al. (n=58 ME/CFS; [PMID: 42212259](https://pubmed.ncbi.nlm.nih.gov/42212259/)) which found "no significant changes in peak VO2 between days" and concluded that "the data do not support using the 2-day CPET protocol to define PEM or disability." This study did note that ME/CFS patients had greater perception of exertion throughout exercise and lower maximum heart rate than controls, suggesting that subjective and autonomic components of PEM may operate independently of measurable aerobic capacity declines. This heterogeneity is a crucial caveat: the 2-day CPET decline may characterize a subset of patients rather than the entire ME/CFS population.

### Finding 2: Invasive CPET Reveals Peripheral Neurovascular Dysregulation with Impaired O2 Extraction

The most mechanistically informative study for this hypothesis is the invasive CPET (iCPET) investigation by Joseph et al. ([PMID: 33577778](https://pubmed.ncbi.nlm.nih.gov/33577778/)), which studied 160 ME/CFS patients versus 36 controls with direct hemodynamic measurements including right heart catheterization. ME/CFS patients showed significantly lower right atrial pressure (1.9 +/- 2 vs. 8.3 +/- 1.5, P < 0.0001), indicating impaired preload, and lower peak VO2. The study identified "two types of peripheral neurovascular dysregulation that are biologically plausible contributors to ME/CFS exertional intolerance — depressed cardiac output from impaired venous return, and impaired peripheral oxygen extraction." Approximately 50% of patients had objective small fiber neuropathy on skin biopsy, providing a structural correlate for the neurovascular dysregulation.

This finding provides the most direct evidence for the model's core claim that exertion unmasks impaired peripheral oxygen extraction. The identification of small fiber neuropathy as an upstream driver — potentially causing microvascular shunting of oxygenated blood away from capillary beds — represents a concrete mechanistic link between the autonomic and perfusion components of the hypothesis.

### Finding 3: Skeletal Muscle Mitochondrial Damage Confirmed by Electron Microscopy

Direct ultrastructural evidence for the muscle component of the hypothesis comes from electron microscopy studies ([PMID: 39727052](https://pubmed.ncbi.nlm.nih.gov/39727052/)) demonstrating "damage of mitochondria in skeletal muscle of ME/CFS patients with a preferential subsarcolemmal localization but not in PCS [post-COVID syndrome without ME/CFS]." Biopsies taken one day after exercise showed "simultaneous presence of necroses and signs of regeneration," supporting the concept of repeated exercise-induced damage cycles. This finding is critical because it demonstrates tissue-level pathology directly in the organ system that the hypothesis implicates.

Complementary in vitro evidence ([PMID: 33106563](https://pubmed.ncbi.nlm.nih.gov/33106563/)) showed that "CFS skeletal muscle cells are unable to utilise glucose to the same extent as healthy control cells" while "galactose and fatty acids [were oxidized] normally, indicating that the bioenergetic dysfunction lies upstream of the TCA cycle." This retained dysfunction in cultured cells suggests an intrinsic cellular defect rather than a systemic factor, pointing to a cell-autonomous metabolic impairment in ME/CFS muscle.

### Finding 4: Endothelial Dysfunction and Microvascular Impairment

The microvascular component of the hypothesis is supported by multiple independent lines of evidence. Scherbakov et al. ([PMID: 36730360](https://pubmed.ncbi.nlm.nih.gov/36730360/)) demonstrated that "ME/CFS patients had markedly reduced FMD compared to healthy controls at baseline (5.1% vs. 8.2%, p < 0.0001)" and "significantly lower microvascular regulation measured by PORH than healthy controls (1354 PU vs. 2208 PU, p = 0.002)." This dual impairment — in both conduit artery and microvascular function — establishes that vascular dysfunction in ME/CFS is not limited to one vascular bed.

A 2024 mechanistic review ([PMID: 38399482](https://pubmed.ncbi.nlm.nih.gov/38399482/)) provides a model describing how "capillary blood flow is impaired not only by pathological blood components but also by prothrombotic changes in the vascular wall, endothelial dysfunction, and the expression of adhesion molecules in the capillaries." Additionally, Saha et al. ([PMID: 30594919](https://pubmed.ncbi.nlm.nih.gov/30594919/)) demonstrated that "RBCs isolated from ME/CFS patients were significantly stiffer than those from healthy controls," adding a hemorheological component: even if capillaries are structurally normal, reduced red blood cell deformability would impair oxygen delivery to tissues.

{{figure:evidence_matrix.png|caption=Evidence matrix heatmap showing the strength and type of evidence supporting each node of the Exertion-Perfusion-Muscle Immunometabolic PEM Model}}

### Finding 5: PEM Associated with Purine Deregulation, Hypermetabolism, and Muscle Protein Degradation

The metabolic consequences of exertion in ME/CFS were characterized by McGregor et al. ([PMID: 31277442](https://pubmed.ncbi.nlm.nih.gov/31277442/)), who found that "the principal biochemical change related to the 7-day severity of PEM was the fall in the purine metabolite, hypoxanthine. This decrease correlated with alterations in the glucose:lactate ratio highly suggestive of a glycolytic anomaly." The study also demonstrated "increased excretion of urine metabolites within the 7-day response period indicated a hypermetabolic event was occurring," including methylhistidine (a marker of muscle protein degradation), mannitol (intestinal barrier deregulation), and acetate.

CSF metabolomics from Baraniuk ([PMID: 39941050](https://pubmed.ncbi.nlm.nih.gov/39941050/)) extended these findings to the central nervous system: "Exercise led to consumption of lipids in ME/CFS and controls while metabolites were consumed in ME/CFS but generated in controls," with elevated serine pathway suggesting dysfunctional folate and one-carbon metabolism. This provides a potential link between peripheral metabolic stress and central nervous system dysfunction — a key bridge in the hypothesis's causal chain from muscle to CNS amplification.

Broader metabolomic profiling by Naviaux et al. ([PMID: 27573827](https://pubmed.ncbi.nlm.nih.gov/27573827/)) identified abnormalities in 20 metabolic pathways in ME/CFS, with "80% of the diagnostic metabolites decreased, consistent with a hypometabolic syndrome," including purine, sphingolipid, phospholipid, and mitochondrial metabolism pathways.

### Finding 6: Shared Autonomic Phenotype with Reduced Cerebral Blood Flow

A retrospective study of 143 Long COVID and 170 ME/CFS patients versus 73 healthy controls ([PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/)) revealed "extensive similarities between Long COVID and ME/CFS, including reduced orthostatic CBFv (92%/88% in Long COVID/ME/CFS)." This high prevalence of reduced cerebral blood flow velocity on orthostatic challenge supports the hypothesis's claim that autonomic dysfunction amplifies peripheral signals into CNS symptoms (brain fog, cognitive impairment). The overlap between Long COVID and ME/CFS autonomic phenotypes also suggests shared pathophysiological mechanisms, potentially strengthening the model's generalizability across post-infectious fatigue conditions.

### Finding 7: Central Activation Failure Complicates the Peripheral Muscle Hypothesis

A pivotal qualifying finding comes from Kent-Braun et al. ([PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/)), who demonstrated that during sustained maximal isometric exercise, CFS patients showed "normal fatigability and metabolism at both the intracellular and systemic levels, normal muscle membrane function and excitation-contraction coupling, and an inability to fully activate skeletal muscle during intense, sustained exercise." This central activation failure suggests that in at least some patients, the primary defect may be in the CNS drive to muscle rather than in the muscle itself — a finding that partially inverts the causal direction assumed by the hypothesis.

Lane et al. ([PMID: 9527150](https://pubmed.ncbi.nlm.nih.gov/9527150/)) found that "muscle histometry in patients with chronic fatigue syndrome generally did not show the changes expected as a result of inactivity," with type 1 fibre predominance (23%) more common than type 2 (3%) and fibre atrophy in only 10.4%. This heterogeneous muscle histology is consistent with the view that peripheral muscle pathology is not universal in ME/CFS.

{{figure:mechanistic_chain.png|caption=Mechanistic causal chain diagram showing evidence-supported links (solid) and inferred/speculative links (dashed) in the Exertion-Perfusion-Muscle Immunometabolic PEM Model}}

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Disease Context | Confidence |
|----------|--------------|-----------|--------------------------|-------------|-----------------|------------|
| [PMID: 33577778](https://pubmed.ncbi.nlm.nih.gov/33577778/) | Human clinical (iCPET) | **Supports** | Impaired peripheral O2 extraction | Two mechanisms: depressed cardiac output from impaired venous return + impaired peripheral O2 extraction; ~50% had small fiber neuropathy | ME/CFS (n=160) | **High** — invasive gold-standard measures |
| [PMID: 33327624](https://pubmed.ncbi.nlm.nih.gov/33327624/) | Meta-analysis | **Supports** | Exertion unmasks aerobic impairment | Significant day-2 CPET decline in ME/CFS vs. improvement in controls | ME/CFS (multiple cohorts) | **Moderate-High** — heterogeneity across studies |
| [PMID: 38965566](https://pubmed.ncbi.nlm.nih.gov/38965566/) | Human clinical | **Supports** | Day-2 CPET decline | Largest study: ME/CFS failed to reproduce CPET-1 measures on CPET-2 | ME/CFS (n=84) | **High** — largest single-center study |
| [PMID: 42212259](https://pubmed.ncbi.nlm.nih.gov/42212259/) | Human clinical | **Qualifies/Refutes** | Day-2 CPET decline | No significant day-2 changes in peak VO2; greater perceived exertion and lower max HR | ME/CFS (n=58) | **Moderate** — challenges universality |
| [PMID: 39727052](https://pubmed.ncbi.nlm.nih.gov/39727052/) | Human clinical (EM) | **Supports** | Skeletal muscle mitochondrial damage | EM-confirmed mitochondrial damage with subsarcolemmal localization; post-exercise necrosis + regeneration | ME/CFS and PC-ME/CFS | **High** — direct ultrastructural evidence |
| [PMID: 33106563](https://pubmed.ncbi.nlm.nih.gov/33106563/) | In vitro | **Supports** | Intrinsic muscle metabolic dysfunction | CFS muscle cells unable to utilize glucose normally; galactose and FAO normal — dysfunction upstream of TCA | CFS (n=9 vs. n=11 controls) | **Moderate** — small sample, in vitro |
| [PMID: 36730360](https://pubmed.ncbi.nlm.nih.gov/36730360/) | Human clinical | **Supports** | Endothelial dysfunction | FMD: 5.1% vs. 8.2% (p<0.0001); PORH: 1354 vs. 2208 PU (p=0.002) | ME/CFS | **High** — well-controlled |
| [PMID: 38399482](https://pubmed.ncbi.nlm.nih.gov/38399482/) | Review/Model | **Supports** | Microvascular impairment mechanisms | Comprehensive model: pathological blood components, prothrombotic endothelial changes, adhesion molecules, hypovolemia | ME/CFS (review) | **Moderate** — review-level synthesis |
| [PMID: 30594919](https://pubmed.ncbi.nlm.nih.gov/30594919/) | Human clinical | **Supports** | Hemorheological impairment | RBCs from ME/CFS patients significantly stiffer than controls | ME/CFS | **Moderate** — single study |
| [PMID: 31277442](https://pubmed.ncbi.nlm.nih.gov/31277442/) | Human clinical | **Supports** | PEM linked to metabolic derangement | Principal PEM-severity biochemical change: fall in hypoxanthine; glucose:lactate ratio anomaly; hypermetabolic event | ME/CFS (n=47) | **Moderate-High** — targeted metabolomics |
| [PMID: 39941050](https://pubmed.ncbi.nlm.nih.gov/39941050/) | Human clinical | **Supports** | CNS metabolic response to exercise | CSF metabolites consumed in ME/CFS but generated in controls post-exercise | ME/CFS | **Moderate** — novel but small |
| [PMID: 27573827](https://pubmed.ncbi.nlm.nih.gov/27573827/) | Human clinical | **Supports** | Systemic metabolic dysfunction | 20 pathway abnormalities; 80% diagnostic metabolites decreased (hypometabolic syndrome) | ME/CFS (n=84) | **High** — comprehensive metabolomics |
| [PMID: 41576003](https://pubmed.ncbi.nlm.nih.gov/41576003/) | Human clinical | **Supports** | Autonomic dysfunction / reduced CBF | Reduced orthostatic CBFv in 92% Long COVID, 88% ME/CFS | ME/CFS + Long COVID | **Moderate-High** — large cohort |
| [PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/) | Human clinical (MRS) | **Qualifies** | Peripheral muscle dysfunction | Normal muscle fatigability, metabolism, and membrane function; central activation failure present | CFS | **High** — gold-standard MRS |
| [PMID: 9527150](https://pubmed.ncbi.nlm.nih.gov/9527150/) | Human clinical (biopsy) | **Qualifies** | Muscle deconditioning/atrophy | Muscle histometry not consistent with deconditioning; heterogeneous findings | CFS (n=105) | **Moderate-High** — large biopsy study |
| [PMID: 39240417](https://pubmed.ncbi.nlm.nih.gov/39240417/) | Review | **Supports** | Integrated PEM model | Review-level synthesis of exertion to perfusion/O2 utilization to metabolic effects chain | ME/CFS and PCC | **Moderate** — review-level |
| [PMID: 32247028](https://pubmed.ncbi.nlm.nih.gov/32247028/) | Review/Hypothesis | **Competing** | Autoantibody-mediated vasoconstriction | Beta2-AdR and M3AChR autoantibodies cause vasoconstriction and hypoxemia | ME/CFS subset | **Low-Moderate** — hypothesis paper |
| [PMID: 36043493](https://pubmed.ncbi.nlm.nih.gov/36043493/) | Review/Hypothesis | **Competing** | Ischaemia-reperfusion injury | Fibrin amyloid microclots block capillaries during exercise; reperfusion injury on cessation | ME/CFS, Long COVID | **Low** — theoretical |
| [PMID: 38232699](https://pubmed.ncbi.nlm.nih.gov/38232699/) | Human clinical (scRNA-seq) | **Qualifies** | Post-exercise immune activation | Monocyte dysregulation at baseline; improper platelet activation post-exercise; minimal other immune changes | ME/CFS | **Moderate-High** — single-cell resolution |
| [PMID: 26148446](https://pubmed.ncbi.nlm.nih.gov/26148446/) | Systematic review | **Qualifies** | Post-exercise cytokine elevation | Only TGF-beta consistently elevated; "circulating cytokines do not seem to explain the core characteristic of post-exertional fatigue" | CFS | **Moderate-High** — systematic review |

---

## Mechanistic Causal Chain

The hypothesis implies the following sequential causal chain from upstream trigger to clinical manifestation. Below, we annotate each link with the strength of evidence:

```
UPSTREAM TRIGGER
  Physical or cognitive exertion
        |
        v
NODE 1: IMPAIRED PERFUSION & O2 EXTRACTION ---- [STRONG evidence]
  * Endothelial dysfunction (FMD down, PORH down)    <-- PMID:36730360
  * Small fiber neuropathy --> microvascular           <-- PMID:33577778
    shunting of oxygenated blood
  * Reduced RBC deformability                         <-- PMID:30594919
  * Depressed cardiac output (low preload)            <-- PMID:33577778
        |
        v
NODE 2: SKELETAL MUSCLE OXIDATIVE PHOSPHORYLATION FAILURE -- [MODERATE-STRONG]
  * Mitochondrial damage (subsarcolemmal, EM)          <-- PMID:39727052
  * Impaired glucose utilization (in vitro)            <-- PMID:33106563
  * BUT: normal MRS metabolism in some patients        <-- PMID:8423875 [QUALIFYING]
        |
        v
NODE 3: IONIC HOMEOSTASIS DISRUPTION ---- [SPECULATIVE - NO DIRECT EVIDENCE]
  * Na+/Ca2+ overload in exercising muscle
  * No 23Na-MRI or calcium imaging data in ME/CFS
  * Inferred from general exercise physiology
        |
        v
NODE 4: LOCAL METABOLITE ACCUMULATION ---- [MODERATE-STRONG evidence]
  * Purine metabolism deregulation (hypoxanthine down) <-- PMID:31277442
  * Lactate/glucose ratio anomaly                      <-- PMID:31277442
  * Hypometabolic syndrome (20 pathway defects)        <-- PMID:27573827
  * Oxidative stress / ROS accumulation                <-- PMID:39240417
        |
        v
NODE 5: LOCAL & SYSTEMIC IMMUNE ACTIVATION ---- [INCONSISTENT evidence]
  * Monocyte dysregulation at baseline                 <-- PMID:38232699
  * Platelet activation post-exercise                  <-- PMID:38232699
  * TGF-beta elevated, but other cytokines inconsistent <-- PMID:26148446
  * No significant post-exercise cytokine diff.        <-- PMID:10226888, 24027260
  * Complement C4a activation (level B evidence)       <-- PMID:24974723
        |
        v
NODE 6: AUTONOMIC & CNS AMPLIFICATION ---- [MODERATE evidence]
  * Reduced orthostatic cerebral blood flow (88-92%)   <-- PMID:41576003
  * CSF metabolite consumption vs. generation          <-- PMID:39941050
  * Central activation failure                         <-- PMID:8423875
        |
        v
CLINICAL OUTCOME: DELAYED POST-EXERTIONAL MALAISE
  * Symptom exacerbation 12-72 hours post-exertion
  * Fatigue, cognitive impairment, pain, autonomic symptoms
```

**Where the chain is strong:** Nodes 1 (perfusion/O2 extraction), 2 (muscle mitochondria), and 4 (metabolite accumulation) each have direct human clinical evidence from independent laboratories. The connection between exertion and impaired aerobic performance (Nodes 1 to 2) is well-supported by iCPET and 2-day CPET data.

**Where the chain is inferred:** The links between Nodes 2 to 3 to 4 (mitochondrial failure to ionic disruption to metabolite accumulation) and Nodes 4 to 5 to 6 (metabolites to immune activation to CNS amplification) are logical but have not been demonstrated in longitudinal or perturbation studies. The temporal ordering is assumed, not proven.

**Where the chain is missing:** Node 3 (ionic homeostasis) has zero direct evidence in ME/CFS. Node 5 (immune activation) has inconsistent evidence, with several studies failing to find post-exercise cytokine differences. The mechanism by which peripheral metabolic stress is transduced to CNS symptoms (Node 5 to 6) remains largely theoretical.

---

## Alternative Models

### 1. Autoantibody-Mediated Vasomotor Dysregulation
**Relationship to seed hypothesis: Upstream cause / parallel mechanism**

A receptor-autoantibody model ([PMID: 32247028](https://pubmed.ncbi.nlm.nih.gov/32247028/)) proposes that autoantibodies against beta2-adrenergic receptors and M3 muscarinic acetylcholine receptors cause vasoconstriction and hypoxemia, which could explain impaired perfusion as a downstream consequence of autoimmunity rather than as a primary microvascular defect. Loebel et al. ([PMID: 33889154](https://pubmed.ncbi.nlm.nih.gov/33889154/)) found associations between autoantibody levels and cardiovascular/immunological parameters in infection-triggered ME/CFS. If validated, this model would situate the perfusion deficits of the seed hypothesis as secondary to immune-mediated receptor dysfunction, potentially making the autoantibody the more parsimonious upstream cause.

### 2. Ischaemia-Reperfusion Injury Model
**Relationship: Parallel mechanism / alternative explanation for PEM trigger**

Pretorius et al. ([PMID: 36043493](https://pubmed.ncbi.nlm.nih.gov/36043493/)) argue that fibrin amyloid microclots block capillaries during exercise, and that the reoxygenation phase after exercise cessation constitutes ischaemia-reperfusion (I-R) injury producing reactive oxygen species bursts, hyperinflammation, and mast cell activation. This model could explain both the breathlessness/fatigue during exertion and the delayed PEM, offering an alternative to the "metabolite accumulation to immune activation" link in the seed hypothesis. Currently speculative with limited direct evidence in ME/CFS.

### 3. Central Sensitization / CNS-Primary Model
**Relationship: Alternative causal direction**

The finding of central activation failure ([PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/)) and normal peripheral muscle metabolism in some patients raises the possibility that PEM is primarily a CNS phenomenon — a disorder of effort perception, interoception, or central motor drive — rather than a consequence of peripheral metabolic failure feeding back to the brain. The CSF metabolomics data ([PMID: 39941050](https://pubmed.ncbi.nlm.nih.gov/39941050/)) showing abnormal central metabolite handling could support either direction of causation.

### 4. Gut Microbiome-Immune Axis Model
**Relationship: Parallel mechanism / upstream modifier**

Multiple studies document gut dysbiosis in ME/CFS with reduced butyrate-producing bacteria and increased intestinal permeability ([PMID: 40980765](https://pubmed.ncbi.nlm.nih.gov/40980765/)). The "leaky gut" hypothesis posits that microbial translocation drives systemic inflammation, which could set the immunological baseline upon which exertion-triggered PEM is superimposed. This model is complementary rather than competing — it may explain why some patients have baseline immune activation that is then amplified by exercise.

### 5. TRPM3 Ion Channel Dysfunction / NK Cell Cytotoxicity Model
**Relationship: Parallel mechanism**

Impaired TRPM3 ion channel function with reduced Ca2+ signaling has been consistently identified in ME/CFS NK cells ([PMID: 42177403](https://pubmed.ncbi.nlm.nih.gov/42177403/); [PMID: 39483457](https://pubmed.ncbi.nlm.nih.gov/39483457/)). NK cell cytotoxicity is reduced to approximately half of healthy control levels. While this immune defect is consistent with the "immune dysfunction" node of the seed hypothesis, it operates through a different mechanism (ion channel dysfunction) than the metabolite-driven immune activation proposed in the model.

---

## Knowledge Gaps

### Gap 1: Ionic Homeostasis in Exercising Muscle — No Direct Evidence
**Scope:** The seed hypothesis claims that ionic homeostasis (Na+/Ca2+) is disrupted in ME/CFS skeletal muscle during exertion. **No study has directly measured intramuscular sodium or calcium dynamics in ME/CFS patients during or after exercise.** 23Na-MRI, which can quantify tissue sodium content non-invasively, has not been applied to ME/CFS. Calcium imaging of ME/CFS muscle biopsies is similarly absent. **Why it matters:** This is a claimed causal link with zero supporting evidence. **Resolution:** 23Na-MRI of exercising skeletal muscle in ME/CFS patients vs. controls, combined with serial muscle biopsies assessing calcium handling proteins (SERCA, RyR).

### Gap 2: Causal Ordering of Nodes — No Longitudinal/Perturbation Data
**Scope:** All evidence linking the hypothesis's nodes is cross-sectional. No study has tested whether correcting one node (e.g., improving perfusion with a vasodilator) alleviates downstream nodes (e.g., metabolic derangement, PEM). **Why it matters:** Cross-sectional associations cannot distinguish cause from consequence. The entire causal chain is inferred. **Resolution:** Interventional studies — e.g., acute vasodilator administration with iCPET + metabolomics before/after; IVIG in small fiber neuropathy patients with iCPET endpoints.

### Gap 3: Inconsistent Post-Exercise Immune Activation
**Scope:** While some studies show complement activation (C4a), altered gene expression (TLR4, IL-10), and platelet activation post-exercise, others find no significant post-exercise cytokine differences ([PMID: 10226888](https://pubmed.ncbi.nlm.nih.gov/10226888/); [PMID: 24027260](https://pubmed.ncbi.nlm.nih.gov/24027260/)). A systematic review ([PMID: 26148446](https://pubmed.ncbi.nlm.nih.gov/26148446/)) concluded that "circulating cytokines do not seem to explain the core characteristic of post-exertional fatigue." **Why it matters:** The "metabolite to immune activation to CNS amplification" link is a critical bridge in the model. If post-exercise immune activation is not robust, the mechanism by which peripheral metabolic stress becomes systemic and central remains unexplained. **Resolution:** Multi-timepoint (0, 4, 24, 48, 72h) immune profiling using single-cell approaches in well-phenotyped ME/CFS cohorts stratified by PEM severity.

### Gap 4: Subtype Specificity Unknown
**Scope:** The 2026 CPET non-replication ([PMID: 42212259](https://pubmed.ncbi.nlm.nih.gov/42212259/)) and the central activation failure finding ([PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/)) suggest the model does not apply uniformly. No study has prospectively stratified patients by the presence/absence of each mechanistic node (perfusion deficit, mitochondrial damage, immune activation) to determine which combinations define clinical subtypes. **Why it matters:** Treating ME/CFS as a single entity may obscure subtype-specific mechanisms. **Resolution:** Multi-modal phenotyping study combining iCPET, muscle biopsy, metabolomics, immune profiling, and autonomic testing in the same cohort with unsupervised clustering.

### Gap 5: No GenCC/ClinGen or Genetic Architecture Data
**Scope:** No genome-wide association studies (GWAS) or genetic studies have been linked specifically to the mechanistic nodes of this hypothesis. There is no GenCC or ClinGen entry for ME/CFS. Genetic susceptibility to mitochondrial dysfunction, endothelial dysfunction, or autonomic dysregulation in ME/CFS is unknown. **Resolution:** Large-scale GWAS with phenotypic stratification by mechanistic subtype.

### Gap 6: Absence of Clinical Trial Evidence Targeting the Specific Mechanism
**Scope:** No registered clinical trial specifically tests the exertion-perfusion-muscle immunometabolic chain. The rituximab ([PMID: 39042627](https://pubmed.ncbi.nlm.nih.gov/39042627/)) and cyclophosphamide trials target autoimmunity, not the perfusion-metabolic axis directly. **Resolution:** Trials of vasodilators, mitochondrial-targeted agents (e.g., MitoQ), or exercise-titrated interventions with mechanistic endpoints.

---

## Discriminating Tests

### Test 1: Vasodilator Challenge with iCPET + Metabolomics
**Design:** Randomized crossover trial of an acute vasodilator (e.g., sodium nitroprusside or sildenafil) vs. placebo in ME/CFS patients undergoing iCPET with simultaneous blood/urine metabolomics sampling at baseline, peak exercise, and 24h post-exercise.
**Patient stratification:** Patients with confirmed small fiber neuropathy (skin biopsy) vs. without; patients with vs. without day-2 CPET decline.
**Expected result if hypothesis is correct:** Vasodilator improves peripheral O2 extraction, reduces purine deregulation markers, and attenuates PEM severity.
**Expected result if CNS-primary model is correct:** Vasodilator improves hemodynamics but does not attenuate PEM or metabolic markers.

### Test 2: 23Na-MRI of Exercising Skeletal Muscle
**Design:** 23Na-MRI and 31P-MRS of calf muscle before, during, and after sustained isometric exercise in ME/CFS patients vs. sedentary controls.
**Biomarkers:** Tissue sodium content (23Na-MRI), intracellular pH, PCr/Pi ratio (31P-MRS).
**Expected result if ionic homeostasis hypothesis is correct:** ME/CFS patients show exaggerated sodium accumulation and delayed PCr recovery.
**Expected result if ionic homeostasis is not involved:** Normal sodium dynamics with abnormal energy metabolism only.

### Test 3: Multi-Timepoint Immune Profiling Post-Exercise
**Design:** Single-cell RNA-seq + multiplex cytokine panel at 0, 4, 12, 24, 48, and 72h post-standardized exercise challenge (e.g., submaximal CPET at 70% predicted peak).
**Patient stratification:** By PEM severity (mild vs. severe PEM responders, identified by prospective symptom diaries).
**Expected result if metabolite to immune to CNS chain operates:** Immune activation peaks coincide with or precede PEM symptom peaks at 24-48h; correlation between immune markers and metabolite levels.

### Test 4: Muscle Biopsy with Mitochondrial Functional Assays Pre- and Post-Exercise
**Design:** Paired vastus lateralis biopsies at rest and 24h post-submaximal exercise, with mitochondrial respirometry (Oroboros), electron microscopy, and transcriptomics.
**Patient stratification:** By iCPET phenotype (impaired O2 extraction vs. impaired preload vs. both).
**Expected result if hypothesis is correct:** Exercise-induced mitochondrial respiratory decline correlates with O2 extraction deficit; subsarcolemmal mitochondrial damage increases post-exercise.

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base, labeled as leads requiring curator verification.*

### Candidate Evidence References

1. **[PMID: 33577778](https://pubmed.ncbi.nlm.nih.gov/33577778/)** — *Insights From Invasive Cardiopulmonary Exercise Testing of Patients With Myalgic Encephalomyelitis/Chronic Fatigue Syndrome*
   - Snippet: "These results identify two types of peripheral neurovascular dysregulation that are biologically plausible contributors to ME/CFS exertional intolerance-depressed Qc from impaired venous return, and impaired peripheral oxygen extraction."
   - **Candidate edge:** Small fiber neuropathy --> microvascular shunting --> impaired O2 extraction --> exertional intolerance
   - **Evidence source:** HUMAN_CLINICAL
   - **Direction:** SUPPORT

2. **[PMID: 42212259](https://pubmed.ncbi.nlm.nih.gov/42212259/)** — *Cardiopulmonary exercise test results do not change over two sequential days in patients with chronic fatigue syndrome*
   - Snippet: "Our data indicate that 2-day CPET provides exercise-related results that are the same in ME/CFS patients and CON subjects."
   - **Candidate role:** QUALIFIES the 2-day CPET decline claim; suggests subtype specificity
   - **Evidence source:** HUMAN_CLINICAL
   - **Direction:** REFUTE (partial)

3. **[PMID: 8423875](https://pubmed.ncbi.nlm.nih.gov/8423875/)** — *Central basis of muscle fatigue in chronic fatigue syndrome*
   - Snippet: "voluntary activation of the tibialis was significantly lower in the patients during maximal sustained exercise. The results indicate that patients with CFS have normal fatigability and metabolism... and an inability to fully activate skeletal muscle during intense, sustained exercise."
   - **Candidate competing edge:** CNS motor drive failure --> perceived exertional intolerance (alternative to peripheral muscle dysfunction)
   - **Direction:** QUALIFIES

4. **[PMID: 38232699](https://pubmed.ncbi.nlm.nih.gov/38232699/)** — *Single-cell transcriptomics of the immune system in ME/CFS at baseline and following symptom provocation*
   - Snippet: "At baseline, ME/CFS patients display classical monocyte dysregulation suggestive of inappropriate differentiation and migration to tissue... Comparing the transcriptome at baseline and postexercise challenge, we discover patterns indicative of improper platelet activation in patients."
   - **Candidate node:** Platelet activation as a post-exertional immune event
   - **Direction:** SUPPORT (qualifies — platelet rather than cytokine-mediated)

5. **[PMID: 41591477](https://pubmed.ncbi.nlm.nih.gov/41591477/)** — *Genetic depletion of the early autophagy protein ATG13 impairs mitochondrial energy metabolism*
   - Snippet: "ablation of the atg13 gene resulted in increased infiltration of M1 macrophages into the muscle vasculature, deterioration of myelin integrity in nerve bundles, and a reduction in muscle strength following treadmill exercise"
   - **Candidate mechanistic link:** Impaired autophagy --> mitochondrial dysfunction --> M1 macrophage infiltration --> muscle-nerve damage --> PEM
   - **Direction:** SUPPORT (model organism)

6. **[PMID: 36730360](https://pubmed.ncbi.nlm.nih.gov/36730360/)** — *Endothelial dysfunction in ME/CFS patients*
   - Snippet: "ME/CFS patients had markedly reduced FMD compared to healthy controls at baseline (5.1% vs. 8.2%, p< 0.0001), and significantly lower microvascular regulation measured by PORH than healthy controls (1354 PU vs. 2208 PU, p = 0.002)."
   - **Candidate edge:** Endothelial dysfunction --> impaired tissue perfusion
   - **Evidence source:** HUMAN_CLINICAL
   - **Direction:** SUPPORT

7. **[PMID: 27573827](https://pubmed.ncbi.nlm.nih.gov/27573827/)** — *Metabolic features of chronic fatigue syndrome*
   - Snippet: "Eighty percent of the diagnostic metabolites were decreased, consistent with a hypometabolic syndrome."
   - **Candidate edge:** Systemic metabolic shutdown (dauer-like response) as context for exertional metabolic failure
   - **Evidence source:** HUMAN_CLINICAL
   - **Direction:** SUPPORT

### Candidate Pathophysiology Nodes/Edges

| Source Node | Target Node | Candidate Edge | Evidence Level |
|-------------|-------------|----------------|---------------|
| Small fiber neuropathy | Microvascular shunting | SFN causes arteriolar dilation leading to capillary bypass | Moderate (PMID: 33577778) |
| Exertion | Purine depletion | Hypoxanthine fall correlates with PEM severity | Moderate (PMID: 31277442) |
| Endothelial dysfunction | Impaired tissue perfusion | FMD and PORH reduction leads to reduced O2 delivery | Strong (PMID: 36730360) |
| Mitochondrial damage | Metabolite accumulation | Subsarcolemmal mitochondrial injury leads to impaired OXPHOS | Moderate (PMID: 39727052) |
| RBC stiffness | Impaired capillary flow | Reduced deformability leads to microvascular obstruction | Low-Moderate (PMID: 30594919) |
| Peripheral metabolic stress | CNS dysfunction | CSF metabolite abnormalities post-exercise | Low-Moderate (PMID: 39941050) |
| Impaired autophagy | Mitochondrial dysfunction and neuroinflammation | ATG13 ablation model shows muscle-nerve axis damage | Low (PMID: 41591477, model organism) |

### Candidate Ontology Terms

- **Cell types:** Endothelial cells (CL:0000115), skeletal muscle cells (CL:0000188), classical monocytes (CL:0000860), NK cells (CL:0000623), platelets (CL:0000233), small fiber sensory neurons
- **Biological processes:** Oxidative phosphorylation (GO:0006119), purine nucleotide metabolic process (GO:0006163), vasodilation (GO:0042311), mitochondrial organization (GO:0007005), autophagy (GO:0006914)
- **Phenotype terms:** Post-exertional malaise (HP:0030973), exercise intolerance (HP:0003546), orthostatic intolerance

### Candidate Status and Subtype Recommendations

- **Status recommendation:** Maintain **EMERGING**. Individual nodes are well-supported, but the integrated causal chain lacks perturbation evidence and the ionic homeostasis component is entirely unsubstantiated.
- **Subtype restriction note:** The model likely applies most strongly to ME/CFS patients with:
  - Confirmed small fiber neuropathy
  - Demonstrable day-2 CPET decline
  - Post-infectious onset (especially post-COVID)
  - Patients *without* these features may be better explained by the CNS-primary or autoimmune models.

### Candidate Knowledge Gaps for KB

1. **Ionic homeostasis in ME/CFS muscle:** No 23Na-MRI or calcium imaging data exist. This is the weakest link in the chain.
2. **Causal ordering:** No perturbation study has tested whether fixing one node resolves downstream nodes.
3. **Post-exercise immune activation:** Inconsistent evidence — cytokine studies conflict; single-cell data show platelet/monocyte changes but not the classical pro-inflammatory cytokine cascade the model predicts.
4. **Subtype boundaries:** No prospective study has stratified patients by all mechanistic nodes simultaneously.

---

## Limitations of This Report

1. **Search scope:** This evaluation was based on 72 papers identified through PubMed searches. Relevant evidence in conference abstracts, preprints, or non-English literature may have been missed.
2. **Publication bias:** Positive findings are more likely to be published; negative CPET or metabolomics studies may be underrepresented.
3. **Diagnostic heterogeneity:** Studies used different ME/CFS diagnostic criteria (Fukuda, Canadian Consensus, IOM), potentially mixing distinct patient populations.
4. **Cross-sectional limitation:** Nearly all evidence is cross-sectional, precluding causal inference about the temporal ordering of nodes in the proposed chain.
5. **Small sample sizes:** Many key studies (e.g., in vitro muscle studies, CSF metabolomics) have sample sizes below 20, limiting generalizability.
6. **The hypothesis is a composite:** Testing the "integrated model" requires simultaneous measurement of perfusion, metabolism, immunity, and autonomic function in the same patients — a study design that has not been implemented.

---

## Proposed Follow-up Experiments and Actions

1. **Priority 1 — Multi-modal phenotyping study:** Combine iCPET, 2-day standard CPET, muscle biopsy (EM + respirometry), metabolomics (blood + urine), single-cell immune profiling, and autonomic testing in a single well-powered cohort (n>=100 ME/CFS, n>=50 controls). Apply unsupervised clustering to identify mechanistic subtypes and determine which nodes co-occur.

2. **Priority 2 — Vasodilator intervention with mechanistic endpoints:** Crossover trial of sildenafil or similar vasodilator with iCPET + metabolomics before and after. This directly tests the causal ordering: if perfusion improvement reduces metabolic derangement and PEM, the perfusion to metabolism to PEM chain is supported.

3. **Priority 3 — 23Na-MRI study:** Apply sodium MRI to calf muscle during/after exercise in ME/CFS vs. controls to fill the ionic homeostasis evidence gap.

4. **Priority 4 — Dense temporal immune profiling:** Multi-timepoint (0-72h) single-cell immune profiling post-exercise, stratified by PEM severity, to resolve the inconsistent immune activation evidence.

5. **Priority 5 — Autoantibody stratification:** Measure beta2-AdR and M3AChR autoantibodies in the same cohort undergoing iCPET to determine whether the autoantibody model and the perfusion model converge or diverge.

6. **KB action:** Maintain EMERGING status. Add candidate evidence references from this report pending curator verification of abstract snippets. Add a knowledge gap annotation for ionic homeostasis and causal ordering.

{{figure:plot_1.png|caption=Visual summary of the mechanistic causal chain with evidence strength annotations for each node and link}}

{{figure:plot_2.png|caption=Summary visualization of evidence strength across hypothesis nodes}}

---

*Report generated 2026-06-03. Based on systematic evaluation of 72 papers from PubMed and 7 confirmed findings from iterative hypothesis testing.*
