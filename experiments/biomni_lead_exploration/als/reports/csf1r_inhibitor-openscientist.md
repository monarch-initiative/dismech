---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T12:57:44.247461'
end_time: '2026-11-11T13:21:06.276669'
duration_seconds: 1402.03
template_file: experiments/biomni_lead_exploration/repurposing_template.md
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis
  drug: a CSF1R inhibitor such as pexidartinib
  drug_action: blocking colony-stimulating factor 1 receptor signalling, on which
    microglia and macrophages depend
  mechanism: neuroinflammation driven by activated microglia and infiltrating macrophages
    in spinal cord and along peripheral motor nerves
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 10
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: csf1r_inhibitor-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: csf1r_inhibitor-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Drug Repurposing Hypothesis Assessment

## The Hypothesis

- **Disease:** Amyotrophic Lateral Sclerosis
- **Drug:** a CSF1R inhibitor such as pexidartinib
- **Drug's target and action:** blocking colony-stimulating factor 1 receptor signalling, on which microglia and macrophages depend
- **Disease mechanism the drug would act on:** neuroinflammation driven by activated microglia and infiltrating macrophages in spinal cord and along peripheral motor nerves

The hypothesis is that a CSF1R inhibitor such as pexidartinib, by blocking colony-stimulating factor 1 receptor signalling, on which microglia and macrophages depend, would benefit patients with
Amyotrophic Lateral Sclerosis because it interrupts "neuroinflammation driven by activated microglia and infiltrating macrophages in spinal cord and along peripheral motor nerves". Your job is to assess this
hypothesis, not to advocate for it. Evidence against it is as valuable as evidence for it.

Every factual claim MUST cite a primary source by PMID (or DOI, or NCT number for a
trial registration) and include a short verbatim quote from the cited abstract or record.
Do not paraphrase quotes. Do not invent identifiers. Separate established findings from
your own inference, and label which is which.

## Questions

### 1. Is the mechanism active in this disease?

- Evidence that the drug's target or pathway is active, elevated or genetically implicated
  in patients with Amyotrophic Lateral Sclerosis: in affected tissue, in blood, or through human genetics.
- Whether activity is uniform or confined to a subgroup of patients, and how that subgroup
  is identified (a biomarker, a clinical feature).

### 2. Does blocking it help?

- Clinical trials of a CSF1R inhibitor such as pexidartinib in Amyotrophic Lateral Sclerosis: registration numbers, phase, status and
  reported results, if any exist.
- Trials of other drugs acting on the same target or pathway in Amyotrophic Lateral Sclerosis, with their
  outcomes, including failures.
- Results of a CSF1R inhibitor such as pexidartinib in related diseases that share the mechanism, and how far those results
  should transfer here.
- Animal or human tissue experiments in which blocking the pathway changed
  Amyotrophic Lateral Sclerosis-like features.

### 3. Reasons it might fail

- Redundant pathways, wrong cell compartment, wrong disease stage, drug not reaching the
  affected tissue, or trial endpoints that cannot detect the effect.
- Safety concerns specific to this patient population.

### 4. Verdict

- One paragraph: how strong is the case, and what single experiment or trial design would
  most efficiently test it?
- List the PMIDs and trial identifiers that carry the most weight, with one line each.


## Output

# Drug Repurposing Hypothesis Assessment: CSF1R Inhibition (Pexidartinib) in Amyotrophic Lateral Sclerosis

## Summary

The hypothesis holds that a CSF1R inhibitor such as **pexidartinib**, by blocking colony-stimulating factor 1 receptor (CSF1R) signalling on which microglia and macrophages depend, would benefit patients with **Amyotrophic Lateral Sclerosis (ALS)** by interrupting neuroinflammation driven by activated microglia and infiltrating macrophages in the spinal cord and along peripheral motor nerves. After five iterations reviewing 31 primary sources and recording 11 confirmed findings, our verdict is that **the pathway is a legitimate target, but the proposed molecule (pexidartinib) and strategy (broad CSF1R blockade / microglial depletion) are the weak links**. The case is mechanistically plausible but not decisively supported, and important counter-evidence exists.

On the "is the mechanism active?" question, the evidence is affirmative and multi-layered: CSF1R/CSF1 signalling is upregulated and drives microgliosis in ALS spinal cord and peripheral nerve ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/)); neuroinflammation defines a specific, stratifiable ALS molecular subtype ("ALS-Glia") rather than a universal feature ([PMID: 39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/)); peripheral-nerve macrophages react in both mouse models and patients ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)); and peripheral myeloid activation is measurable in ALS blood and tracks disease severity ([PMID: 34402459](https://pubmed.ncbi.nlm.nih.gov/34402459/), [PMID: 32246039](https://pubmed.ncbi.nlm.nih.gov/32246039/)). On the "does blocking it help?" question, CSF1R-active drugs (GW2580, masitinib) slow disease and extend survival in rodent models, and masitinib has human ALS trial data ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/), [PMID: 27400786](https://pubmed.ncbi.nlm.nih.gov/27400786/), [PMID: 31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/)).

However, three substantial problems temper the case. First, directly ablating proliferating spinal microglia had **no effect** on motor neuron degeneration in SOD1 mice ([PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/)), and microglial *phenotype* — not mere presence — determines toxicity, with wild-type microglia being protective ([PMID: 17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/)). Second, human genetics implicates neuroinflammation only nominally, and CSF1R is not an established ALS risk gene ([PMID: 42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/)). Third, CSF1R is required for microglial homeostasis — its loss-of-function causes a human neurodegenerative leukoencephalopathy ([PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/)) — and pexidartinib specifically carries an **FDA black-box warning for fatal hepatotoxicity** ([PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/), [PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/)). The net assessment: pursue the pathway with a brain-penetrant, titratable CSF1R *modulator* in a biomarker-enriched neuroinflammatory subgroup — not all-comers, and not pexidartinib.

---

## Key Findings

### Finding 1 — CSF1R/CSF1 signalling is upregulated and drives microgliosis in ALS spinal cord and peripheral nerve

The strongest single piece of pro-hypothesis evidence comes from the SOD1(G93A) mouse model. Microglial proliferation in the spinal cord correlates with CSF1R and CSF1 expression, and the selective CSF1R inhibitor **GW2580** produced a coherent set of benefits: *"Administration of GW2580, a selective CSF1R inhibitor, reduced microglial cell proliferation in SOD1(G93A) mice"* and *"GW2580 treatment slowed disease progression, attenuated motoneuron cell death and extended survival of SOD1(G93A) mice"* ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/)). Critically for the peripheral-nerve arm of the hypothesis, macrophages invaded peripheral nerve before microgliosis, and *"treatment with GW2580 attenuated the influx of macrophages into the nerve"* ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/)). A review corroborates that CSF-1R expression *"is significantly increased in neurodegenerative diseases, including Alzheimer's disease (AD), Parkinson's disease (PD), Huntington's disease (HD), amyotrophic lateral sclerosis (ALS)"* ([PMID: 35366105](https://pubmed.ncbi.nlm.nih.gov/35366105/)). **(Established finding.)** This is the proof-of-concept that CSF1R blockade is both pharmacologically achievable and disease-modifying in a standard ALS model, touching both the central and peripheral compartments named in the hypothesis.

### Finding 2 — Masitinib, a CSF-1R/kinase inhibitor, reduces neuroinflammation and has human ALS trial data

Masitinib provides the closest human-relevant parallel to the hypothesis. It *"selectively inhibited the tyrosine kinase receptor colony-stimulating factor 1R (CSF-1R) at nanomolar concentrations"*, and *"Oral administration of masitinib to SOD1(G93A) rats starting after paralysis onset decreased the number of aberrant glial cells, microgliosis, and motor neuron pathology"* ([PMID: 27400786](https://pubmed.ncbi.nlm.nih.gov/27400786/)). Importantly, a randomized clinical trial tested masitinib as an add-on to riluzole in ALS patients ([PMID: 31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/)). **(Established finding.)** Masitinib is a multi-target kinase inhibitor rather than a selective CSF1R blocker, so it is an imperfect proxy — but it is the only same-pathway agent to reach ALS patients, and its preclinical mechanism aligns directly with the hypothesis.

### Finding 3 — CSF1R signalling is essential for homeostatic microglia; loss-of-function causes human neurodegeneration (safety counterpoint)

A central caution: CSF1R is not merely a disease amplifier but a homeostatic necessity. *"Heterozygous CSF1R variants have been known to cause hereditary diffuse leukoencephalopathy with spheroids (HDLS, MIM# 221820), an adult-onset leukoencephalopathy characterized by loss of motor functions and cognitive decline"* ([PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/)). In this disorder, *"microglia in white matter in HDLS lose their homeostatic phenotype"* ([PMID: 32430064](https://pubmed.ncbi.nlm.nih.gov/32430064/)). **(Established finding.)** This is a profound mechanistic paradox for the hypothesis: too *little* CSF1R signalling causes an adult-onset neurodegenerative disease with motor decline that superficially resembles the very condition the drug aims to treat. Chronic pharmacological CSF1R blockade risks recapitulating this loss-of-function phenotype.

### Finding 4 — Pexidartinib carries a black-box hepatotoxicity warning (drug-specific safety concern)

The specific molecule named in the hypothesis has a serious, well-documented safety liability. Pexidartinib (TURALIO), approved for tenosynovial giant cell tumor (TGCT), has a *"potential to cause fatal liver injury [that] has prompted the U.S. FDA to issue a black box warning"* ([PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/)). In a pooled TGCT safety analysis, *"95% of patients with TGCTs (133/140) treated with pexidartinib (median duration of exposure, 19 months [range, 1-76]), experienced a hepatic AR"* ([PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/)). **(Established finding.)** For a chronic neurodegenerative disease requiring long-term dosing, a near-universal hepatic adverse-reaction rate and a fatal-injury warning are poorly compatible with a repurposing strategy in a frail patient population.

### Finding 5 — Neuroinflammation defines a specific ALS molecular subtype (ALS-Glia), not all patients

Neuroinflammation is not a uniform feature of ALS but rather defines a stratifiable subset. Postmortem motor cortex transcriptomics groups ALS patients into molecular subtypes including one defined by *"microglial activation and neuroinflammation (ALS-Glia)"*, and *"ALS-Glia signatures in spinal cord"* correlate with disease duration ([PMID: 39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/)). In human tissue, *"LMN degeneration and microglial activation were highest at disease onset sites"* ([PMID: 42141072](https://pubmed.ncbi.nlm.nih.gov/42141072/)), and *"TMEM119-immunopositive resident microglia were abundant in the motor cortex and subcortical white matter (SWM) of the motor area"* ([PMID: 38788796](https://pubmed.ncbi.nlm.nih.gov/38788796/)). **(Established finding; inference that this enables stratification.)** This is pivotal for trial design: an all-comers CSF1R trial would dilute any effect by enrolling patients whose disease is not neuroinflammation-driven. The ALS-Glia signature offers a concrete enrichment biomarker.

### Finding 6 — In human ALS CNS, resident microglia are activated but monocyte-derived macrophage infiltration is NOT elevated (compartment caveat)

The hypothesis explicitly invokes "infiltrating macrophages in spinal cord." Human tissue data partially contradict this. In postmortem ALS brain and spinal cord, *"CCR2-immunopositive MoDM [monocyte-derived macrophages] was similar to control cases"*, whereas TMEM119+ resident microglia were increased ([PMID: 38788796](https://pubmed.ncbi.nlm.nih.gov/38788796/)). **(Established finding.)** This qualifies the hypothesis: in the human CNS, the dominant myeloid player appears to be the *resident* microglion, not infiltrating monocyte-derived macrophages. This matters because CSF1R dependence differs between these populations, and the therapeutic rationale shifts accordingly.

### Finding 7 — Microglial phenotype (not mere presence) drives ALS toxicity; wild-type microglia are protective

Perhaps the most important conceptual caveat. In mSOD1(G93A)/PU.1(−/−) chimeras, *"wild-type donor-derived microglia slowed motoneuron loss and prolonged disease duration and survival"*, while *"mSOD1(G93A) microglia produced and released more superoxide and nitrite+nitrate, and induced more neuronal death"* ([PMID: 17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/)). **(Established finding.)** This establishes two things simultaneously: activated mutant microglia are directly neurotoxic (the causal basis for targeting them), but healthy microglia are actively *protective*. A therapy that indiscriminately depletes or silences all microglia via CSF1R blockade could remove the protective population along with the harmful one — arguing for *phenotype-reprogramming* over *depletion*.

### Finding 8 — Peripheral macrophages along motor axons react in ALS (mice AND patients); modifying them suppresses microglia and extends survival

The peripheral-nerve arm of the hypothesis is genuinely supported. *"Macrophages along peripheral motor neuron axons in mouse models and patients with ALS react to neurodegeneration"*, and *"Modifying peripheral macrophages suppressed proinflammatory microglial responses, with a shift toward neuronal support"*, delaying symptoms and increasing survival ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)). Critically, however, *"peripheral myeloid cell infiltration into the spinal cord was limited and depended on disease duration"* ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)). **(Established finding.)** This both supports the peripheral-macrophage target and, consistent with Finding 6, qualifies the "infiltration into spinal cord" claim — the peripheral and central compartments are linked by signalling more than by physical cell migration.

### Finding 9 — Human genetic support for neuroinflammation in ALS is nominal; CSF1R itself is not an ALS risk gene

Human genetics — often the most reliable guide to causal, druggable targets — gives only weak support. In a cross-disorder GWAS analysis (Project MinE ALS, effective N = 87,381), microglia-mediated synaptic pruning showed *"nominal but consistent signals in ALS (GSEA NES=1.40, p=0.011; TWAS HLA-B)"*, weaker than in major depressive disorder, with the ALS-specific signal dominated by *"autophagy collapse in ALS versus RNA processing and immune dysregulation in MDD"* ([PMID: 42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/)). **(Established finding.)** CSF1R is not an established ALS risk gene. The absence of strong human genetic validation is a meaningful negative, because immunomodulatory strategies in ALS have a poor track record and genetics would be the ideal counterweight.

### Finding 10 — COUNTER-EVIDENCE: Ablating proliferating microglia had no effect on motor neuron degeneration in SOD1 ALS mice

The single most direct challenge to the hypothesis's core premise. In CD11b-TK(mut-30);SOD1(G93A) mice, *"a 50% reduction in reactive microglia specifically in the lumbar spinal cord of CD11b-TK(mut-30); SOD1(G93A) doubly transgenic mice had no effect on motor neuron degeneration"*, leading the authors to conclude that *"proliferating microglia-expressing mutant SOD1 are not central contributors of the neurodegenerative process in ALS caused by mutant SOD1"* ([PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/)). **(Established finding — negative result.)** Because CSF1R inhibitors act largely by curbing microglial proliferation/survival, this result directly questions whether the proposed mechanism of action translates into neuroprotection. It stands in tension with the GW2580 result (Finding 1), and the discrepancy may reflect differences between partial *modulation* (GW2580 also reduced peripheral macrophage influx and may reprogram phenotype) versus pure *proliferation ablation*.

### Finding 11 — Peripheral myeloid/immune activation is measurable in ALS blood and tracks disease severity — supports biomarker-based stratification

A practical path to patient selection. ALS is *"a systemic disease"* in which *"circulating blood monocytes and natural killer cells are pro-inflammatory"* ([PMID: 34402459](https://pubmed.ncbi.nlm.nih.gov/34402459/)); ALS monocytes carry an inflammatory transcriptomic signature (233 DEGs vs controls; [PMID: 28437540](https://pubmed.ncbi.nlm.nih.gov/28437540/)). A peripheral immune profile *"shifted towards a Th1/Th17 cell-mediated pro-inflammatory immune response and correlated to disease severity and progression"* — though notably *"In CSF samples, no relevant alteration of the immune profile was found"* ([PMID: 32246039](https://pubmed.ncbi.nlm.nih.gov/32246039/)). Single-cell/spatial profiling highlights *"stratified immunomodulation as a potential therapeutic strategy"* ([PMID: 42135512](https://pubmed.ncbi.nlm.nih.gov/42135512/)). **(Established finding; inference that this enables blood-based stratification.)** The CSF caveat warns that a peripheral biomarker may not reflect the central compartment the drug must reach.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent but double-edged model of CSF1R in ALS:

```
            PERIPHERY                              CNS (spinal cord / motor cortex)
  ┌──────────────────────────────┐      ┌──────────────────────────────────────────┐
  │  Blood monocytes / NK cells  │      │  Resident microglia (TMEM119+)             │
  │  pro-inflammatory (F11)      │      │  ACTIVATED at disease-onset sites (F5)     │
  │  tracks severity             │      │  ↑ CSF1R / CSF1 expression (F1)            │
  │                              │      │                                            │
  │  Macrophages along motor     │      │  Phenotype matters: mutant = toxic,        │
  │  axons REACT (mice+patients) │─────▶│  wild-type = PROTECTIVE (F7)               │
  │  (F8)                        │ sig- │                                            │
  │                              │ nal  │  BUT: monocyte-derived macrophage          │
  │  Limited physical            │      │  INFILTRATION is NOT elevated (F6)         │
  │  infiltration into cord (F8) │      │  Ablating proliferating microglia =        │
  └──────────────────────────────┘      │  NO EFFECT on MN degeneration (F10)        │
                                        └──────────────────────────────────────────┘
        CSF1R INHIBITOR (GW2580, masitinib) slows disease + extends survival in
        rodents (F1, F2) ── but CSF1R loss-of-function causes human leukoencephalopathy
        with motor decline (F3), and pexidartinib = black-box fatal hepatotoxicity (F4)
```

The pathway is **active** (Findings 1, 5, 8, 11) and **pharmacologically responsive in rodents** (Findings 1, 2). But three structural problems undercut the leap from this to "pexidartinib will help patients":

1. **Phenotype vs. presence.** CSF1R blockade reduces microglial numbers, yet the toxic signal is phenotype-specific (Finding 7), and reducing proliferating microglia alone does nothing (Finding 10). The therapeutic goal should be *reprogramming* the toxic phenotype, not *depleting* the compartment — a goal that broad CSF1R blockade is poorly matched to.

2. **Homeostatic dependence and the therapeutic window.** Because CSF1R sustains protective, homeostatic microglia (Finding 3), the dose that silences toxic microglia may also disable beneficial ones. A *partial/titratable* modulator with a defined target-engagement window is required, not maximal blockade.

3. **Wrong molecule.** Pexidartinib's fatal-hepatotoxicity profile (Finding 4) makes it a poor repurposing candidate for chronic dosing in ALS, independent of whether the pathway is correct.

The reconciling interpretation of the GW2580 "win" (Finding 1) versus the microglial-ablation "null" (Finding 10) is that GW2580's benefit may derive substantially from its action on the **peripheral macrophage compartment** (Finding 8) and from phenotype modulation, rather than from spinal microglial depletion per se. This reframes the most promising target as the **peripheral myeloid axis**, accessible to a drug that need not fully penetrate the CNS.

---

## Evidence Base

| PMID | Role | How it bears on the hypothesis |
|------|------|-------------------------------|
| [27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/) | **Supports** | GW2580 (selective CSF1R inhibitor) slows disease, extends survival, reduces microgliosis AND peripheral-nerve macrophage influx in SOD1 mice — the core proof of concept. |
| [27400786](https://pubmed.ncbi.nlm.nih.gov/27400786/) | **Supports** | Masitinib inhibits CSF-1R at nanomolar levels and reduces microgliosis/MN pathology in SOD1 rats even post-paralysis. |
| [31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/) | **Supports (human)** | Randomized trial of masitinib add-on to riluzole in ALS — the only same-pathway human trial. |
| [33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/) | **Supports w/ caveat** | Peripheral macrophages react in ALS mice and patients; modifying them extends survival; but CNS infiltration is limited. |
| [39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/) | **Supports (stratification)** | Defines ALS-Glia neuroinflammatory subtype — the enrichment population. |
| [38788796](https://pubmed.ncbi.nlm.nih.gov/38788796/) | **Mixed** | Resident microglia increased in human ALS CNS, but monocyte-derived macrophage infiltration is NOT elevated. |
| [34402459](https://pubmed.ncbi.nlm.nih.gov/34402459/) | **Supports (biomarker)** | ALS is systemic; blood monocytes/NK cells are pro-inflammatory. |
| [32246039](https://pubmed.ncbi.nlm.nih.gov/32246039/) | **Supports w/ caveat** | Peripheral Th1/Th17 shift tracks severity; but CSF immune profile unaltered (compartment decoupling). |
| [42135512](https://pubmed.ncbi.nlm.nih.gov/42135512/) | **Supports (stratification)** | Single-cell/spatial data advocate stratified immunomodulation. |
| [28437540](https://pubmed.ncbi.nlm.nih.gov/28437540/) | **Supports (biomarker)** | ALS monocytes carry a 233-gene inflammatory signature; worse in rapid progressors. |
| [17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/) | **Challenges strategy** | Microglial phenotype, not presence, drives toxicity; wild-type microglia are protective. |
| [18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/) | **Refutes core premise** | 50% ablation of proliferating spinal microglia had NO effect on MN degeneration. |
| [42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/) | **Challenges (genetics)** | Microglial/neuroinflammation signal in ALS genetics is only nominal; autophagy dominates. |
| [33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/) | **Safety (mechanism)** | CSF1R loss-of-function causes human leukoencephalopathy with motor decline. |
| [32430064](https://pubmed.ncbi.nlm.nih.gov/32430064/) | **Safety (mechanism)** | CSF1R required for microglial homeostasis in humans. |
| [40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/) | **Safety (drug)** | Pexidartinib FDA black-box fatal-hepatotoxicity warning; reactive metabolites. |
| [33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/) | **Safety (drug)** | 95% hepatic adverse-reaction rate with chronic pexidartinib dosing. |
| [35366105](https://pubmed.ncbi.nlm.nih.gov/35366105/) | **Supports (context)** | CSF-1R expression increased across neurodegenerative diseases including ALS. |

### Answers to the posed questions

**1. Is the mechanism active in this disease?** Yes, with qualifications. CSF1R/CSF1 is elevated in ALS tissue and drives microgliosis ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/), [PMID: 35366105](https://pubmed.ncbi.nlm.nih.gov/35366105/)); peripheral-nerve macrophages react in mice and patients ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)); peripheral myeloid cells are activated in blood and track severity ([PMID: 34402459](https://pubmed.ncbi.nlm.nih.gov/34402459/), [PMID: 32246039](https://pubmed.ncbi.nlm.nih.gov/32246039/), [PMID: 28437540](https://pubmed.ncbi.nlm.nih.gov/28437540/)). Activity is **confined to a subgroup** — the ALS-Glia molecular subtype — identifiable by transcriptomic signature ([PMID: 39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/)) and peripheral myeloid biomarkers ([PMID: 42135512](https://pubmed.ncbi.nlm.nih.gov/42135512/)). Human genetics, however, supports neuroinflammation only nominally ([PMID: 42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/)).

**2. Does blocking it help?** No CSF1R-inhibitor/pexidartinib ALS trial exists. The only same-pathway human data are the masitinib add-on trial ([PMID: 31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/)). In animals, CSF1R blockade (GW2580) and masitinib slow disease and reduce pathology ([PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/), [PMID: 27400786](https://pubmed.ncbi.nlm.nih.gov/27400786/)), and modifying peripheral macrophages extends survival ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)) — but ablating proliferating microglia does not ([PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/)). Pexidartinib's related-disease (TGCT) experience is defined by hepatotoxicity rather than neuroprotection ([PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/)), and transfer to ALS is low because TGCT is a peripheral tumour, not a CNS disease.

**3. Reasons it might fail.** Wrong cell compartment (resident microglia dominate, not infiltrating macrophages — [PMID: 38788796](https://pubmed.ncbi.nlm.nih.gov/38788796/)); phenotype not presence drives toxicity ([PMID: 17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/)); microglial proliferation may not be causal ([PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/)); homeostatic CSF1R loss is itself neurodegenerative ([PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/), [PMID: 32430064](https://pubmed.ncbi.nlm.nih.gov/32430064/)); ALSFRS-R endpoints may be too insensitive; and pexidartinib's fatal hepatotoxicity is a population-specific safety barrier ([PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/), [PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/)).

---

## Limitations and Knowledge Gaps

1. **No CSF1R-inhibitor ALS trial exists.** The only same-pathway human data come from masitinib ([PMID: 31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/)), a multi-target kinase inhibitor whose effects cannot be attributed to CSF1R specifically. There is no registered trial of pexidartinib or a selective CSF1R inhibitor in ALS.

2. **Model dependence.** Nearly all preclinical evidence derives from SOD1(G93A) rodents, representing ~2% of ALS (familial SOD1). Generalization to the ~97% of TDP-43-pathology, non-SOD1 ALS is unproven.

3. **The GW2580 vs. microglial-ablation contradiction is unresolved.** Findings 1 and 10 give opposite answers about whether reducing spinal microglia helps. The mechanism of GW2580's benefit (peripheral vs. central, depletion vs. reprogramming) is not pinned down.

4. **Compartment decoupling.** Human CNS shows activated resident microglia but no elevated macrophage infiltration ([PMID: 38788796](https://pubmed.ncbi.nlm.nih.gov/38788796/)), and the CSF immune profile is unaltered ([PMID: 32246039](https://pubmed.ncbi.nlm.nih.gov/32246039/)). A blood biomarker may not report on the target tissue, complicating both patient selection and target-engagement readout.

5. **No CNS target-engagement data for pexidartinib in ALS.** Brain penetrance, achievable microglial CSF1R occupancy, and the therapeutic window relative to the homeostatic-loss threshold are unknown.

6. **Weak human genetics.** The absence of CSF1R or strong neuroinflammatory genetic signal in ALS ([PMID: 42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/)) means the target lacks the causal human validation that de-risks the best drug programs.

---

## Proposed Follow-up Experiments / Actions

1. **Dissect the GW2580 mechanism (preclinical, highest priority).** In SOD1 and, crucially, a **TDP-43 model**, use conditional/compartment-restricted CSF1R modulation to separate the peripheral-nerve macrophage contribution from spinal microglial depletion, and measure whether benefit tracks *phenotype reprogramming* (single-cell RNA-seq of myeloid states) rather than cell-number reduction. This directly resolves the Finding 1 vs. Finding 10 contradiction.

2. **Target-engagement and therapeutic-window study.** Use a CSF1R PET tracer to define, in non-human primates or patients, the CSF1R occupancy that suppresses toxic microglia *without* crossing the homeostatic-loss threshold implied by HDLS ([PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/)).

3. **Biomarker-enriched Phase 2a design (the single most efficient test).** Trial a **brain-penetrant, titratable, selective CSF1R modulator — explicitly NOT pexidartinib** — restricted to the **neuroinflammatory ALS-Glia subgroup**, identified by the molecular subtype signature ([PMID: 39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/)) and a peripheral myeloid inflammatory signature ([PMID: 28437540](https://pubmed.ncbi.nlm.nih.gov/28437540/), [PMID: 34402459](https://pubmed.ncbi.nlm.nih.gov/34402459/)). Primary readout: **target-engagement biomarkers** (TSPO/CSF1R PET, neurofilament light, myeloid activation markers) rather than ALSFRS-R alone, which is likely too insensitive for a short Phase 2a.

4. **Peripheral-only strategy as an alternative.** Given the peripheral-macrophage evidence ([PMID: 33077946](https://pubmed.ncbi.nlm.nih.gov/33077946/)) and limited CNS infiltration, test whether a *non-CNS-penetrant* myeloid modulator captures much of the benefit while avoiding the homeostatic-microglia and hepatotoxicity risks.

5. **Explicitly do NOT advance pexidartinib.** Its black-box fatal-hepatotoxicity profile and ~95% hepatic adverse-reaction rate on chronic dosing ([PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/), [PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/)) make it an unsuitable chronic therapy for a frail ALS population regardless of pathway validity.

---

## Verdict

The case is **moderate in strength and conditional**: the CSF1R/microglia–macrophage pathway is genuinely active in ALS and is disease-modifying when modulated in rodent models, giving real mechanistic plausibility. But the hypothesis as literally stated — that **pexidartinib** benefits ALS patients by broadly blocking CSF1R — has three load-bearing weaknesses: (i) depleting proliferating microglia alone does not slow degeneration ([PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/)) and microglial *phenotype*, not number, is what matters ([PMID: 17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/)); (ii) CSF1R is a homeostatic necessity whose loss causes human neurodegeneration ([PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/)); and (iii) pexidartinib specifically carries a fatal-hepatotoxicity black-box warning unsuited to chronic ALS dosing ([PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/)). **The pathway is worth pursuing; pexidartinib and pan-microglial depletion are the wrong molecule and wrong strategy.** The single most efficient test is a **biomarker-enriched Phase 2a trial of a brain-penetrant, titratable, selective CSF1R *modulator* in the neuroinflammatory ALS-Glia subgroup, read out by target-engagement biomarkers** rather than ALSFRS-R alone.

**Highest-weight identifiers:**
- [PMID: 27174644](https://pubmed.ncbi.nlm.nih.gov/27174644/) — GW2580 CSF1R blockade slows ALS and extends survival in SOD1 mice (strongest pro evidence).
- [PMID: 18842883](https://pubmed.ncbi.nlm.nih.gov/18842883/) — Microglial-proliferation ablation had NO effect on MN degeneration (strongest con evidence).
- [PMID: 17043238](https://pubmed.ncbi.nlm.nih.gov/17043238/) — Microglial phenotype, not presence, drives toxicity; wild-type microglia protective.
- [PMID: 33749994](https://pubmed.ncbi.nlm.nih.gov/33749994/) — CSF1R loss-of-function causes human neurodegeneration (mechanism-level safety).
- [PMID: 40554835](https://pubmed.ncbi.nlm.nih.gov/40554835/) / [PMID: 33289960](https://pubmed.ncbi.nlm.nih.gov/33289960/) — Pexidartinib fatal-hepatotoxicity black box; 95% hepatic AR rate (drug-level safety).
- [PMID: 39651269](https://pubmed.ncbi.nlm.nih.gov/39651269/) — ALS-Glia molecular subtype defines the enrichment population for any trial.
- [PMID: 31280619](https://pubmed.ncbi.nlm.nih.gov/31280619/) — Masitinib (CSF-1R-active) randomized ALS trial, the only same-pathway human data.
- [PMID: 42006515](https://pubmed.ncbi.nlm.nih.gov/42006515/) — Human genetics implicate neuroinflammation only nominally; CSF1R not an ALS risk gene.


## Artifacts

- [OpenScientist final report](csf1r_inhibitor-openscientist_artifacts/final_report.html)
- [OpenScientist final report](csf1r_inhibitor-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.
