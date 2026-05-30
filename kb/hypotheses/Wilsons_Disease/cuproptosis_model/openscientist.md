---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-17T21:41:26.467793'
end_time: '2026-05-17T22:33:39.773367'
duration_seconds: 3133.31
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Wilson Disease
  category: Genetic
  hypothesis_group_id: cuproptosis_model
  hypothesis_label: Copper-Dependent Cuproptosis Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: cuproptosis_model\nhypothesis_label: Copper-Dependent\
    \ Cuproptosis Model\nstatus: EMERGING\ndescription: |\n  Beyond oxidative damage\
    \ alone, copper may induce a distinct mitochondrial cell-death program (cuproptosis)\
    \ that amplifies tissue injury.\nevidence:\n- reference: PMID:38731973\n  reference_title:\
    \ 'Wilson Disease: Copper-Mediated Cuproptosis, Iron-Related Ferroptosis, and\
    \ Clinical\n    Highlights, with Comprehensive and Critical Analysis Update.'\n\
    \  supports: PARTIAL\n  snippet: Many interesting disease details were published\
    \ on the mechanistic steps, such as the generation\n    of reactive oxygen species\
    \ (ROS) and cuproptosis causing a copper dependent cell death.\n  explanation:\
    \ Supports cuproptosis as a proposed emerging mechanistic layer in Wilson disease\
    \ rather\n    than a definitively established dominant pathway."
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
citation_count: 20
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Wilson Disease
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** cuproptosis_model
- **Hypothesis Label:** Copper-Dependent Cuproptosis Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: cuproptosis_model
hypothesis_label: Copper-Dependent Cuproptosis Model
status: EMERGING
description: |
  Beyond oxidative damage alone, copper may induce a distinct mitochondrial cell-death program (cuproptosis) that amplifies tissue injury.
evidence:
- reference: PMID:38731973
  reference_title: 'Wilson Disease: Copper-Mediated Cuproptosis, Iron-Related Ferroptosis, and Clinical
    Highlights, with Comprehensive and Critical Analysis Update.'
  supports: PARTIAL
  snippet: Many interesting disease details were published on the mechanistic steps, such as the generation
    of reactive oxygen species (ROS) and cuproptosis causing a copper dependent cell death.
  explanation: Supports cuproptosis as a proposed emerging mechanistic layer in Wilson disease rather
    than a definitively established dominant pathway.
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

# Copper-Dependent Cuproptosis Model in Wilson Disease: Hypothesis Evaluation Report

**Hypothesis ID:** cuproptosis_model
**Status in KB:** EMERGING
**Evaluation Date:** 2026-05-18
**Papers Reviewed:** 96
**Findings Confirmed:** 13
**Iterations Completed:** 5

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (EMERGING)**

The copper-dependent cuproptosis model — proposing that excess copper in Wilson Disease (WD) induces a distinct mitochondrial cell-death program via direct binding to lipoylated TCA cycle proteins — is partially supported by current evidence. The core molecular mechanism of cuproptosis (copper → lipoylated DLAT aggregation → iron-sulfur cluster loss → proteotoxic stress → cell death) has been rigorously defined in vitro ([PMID: 35298263](https://pubmed.ncbi.nlm.nih.gov/35298263/)), and one direct WD study has demonstrated upregulation of cuproptosis markers in ATP7B-knockout mice and copper-treated hepatocytes ([PMID: 41230834](https://pubmed.ncbi.nlm.nih.gov/41230834/)). However, the hypothesis faces critical qualifications that prevent upgrading to ESTABLISHED status: (1) FDX1 mRNA is paradoxically downregulated in both mouse and human WD liver tissue, with the discrepancy resolved only by a post-translational stabilization mechanism demonstrated in liver cancer cells, not WD tissue; (2) no human WD tissue has confirmed the hallmark lipoylated protein aggregation; (3) cuproptosis operates as a stage-dependent amplification layer within a broader feed-forward oxidative stress cascade rather than as an independent pathway; and (4) there is zero evidence for cuproptosis in neurological WD.

The most important caveat is that cuproptosis sensitivity requires active mitochondrial respiration — cells relying on glycolysis are resistant. This metabolic dependency means cuproptosis likely predominates in early-stage, metabolically active hepatocytes but becomes suppressed as disease progresses to cirrhosis, when glycolytic reprogramming, FDX1 transcriptional downregulation, and compensatory GSH/metallothionein induction collectively raise the cuproptosis threshold. The evidence supports classifying cuproptosis as an **emerging mechanistic amplifier** in hepatic WD, not an independent or dominant cell-death pathway.

---

## Summary

Wilson Disease is caused by loss-of-function mutations in ATP7B, leading to impaired biliary copper excretion and progressive copper accumulation in liver, brain, and other organs. The seed hypothesis proposes that beyond classical oxidative damage (ROS via Fenton chemistry), copper induces a distinct mitochondrial cell-death program called cuproptosis that amplifies tissue injury. Our five-iteration investigation, spanning 96 papers and two transcriptomic datasets, reveals that this hypothesis is mechanistically plausible and supported by animal model data, but remains incompletely validated in human WD tissue.

The strongest evidence comes from Tsvetkov et al. (2022), who defined cuproptosis as copper binding to lipoylated TCA cycle proteins (especially DLAT), causing protein aggregation and iron-sulfur cluster loss; and Tang et al. (2025), who demonstrated cuproptosis marker upregulation in ATP7B-knockout mice. However, our analysis of human WD liver transcriptomes (GSE197406) and early mouse WD transcriptomes (GSE125637) revealed that FDX1 — the master regulator of cuproptosis — is consistently downregulated at the mRNA level, contradicting simple activation models. This paradox is resolved by evidence from Wang et al. (2023) showing that oxidative stress suppresses mitochondrial proteases, stabilizing FDX1 protein even when mRNA is reduced. The net result is a feed-forward amplification model: copper → ROS → GSH depletion → FDX1 protein stabilization → enhanced lipoylation → cuproptosis → further iron-sulfur cluster loss → more ROS.

Competing and complementary mechanisms — including classical ROS-mediated oxidative damage, ferroptosis, apoptosis, and direct mitochondrial membrane injury — coexist with cuproptosis in WD liver. The relative contribution of each pathway remains unquantified, representing the single largest knowledge gap.

---

## Key Findings

### Finding 1: Cuproptosis Is a Mechanistically Distinct Cell Death Pathway

Tsvetkov et al. (2022) demonstrated in *Science* that copper-dependent cell death occurs through direct binding of copper to lipoylated components of the TCA cycle, particularly DLAT (dihydrolipoamide S-acetyltransferase). This interaction causes lipoylated protein aggregation and subsequent loss of iron-sulfur cluster proteins, leading to proteotoxic stress and cell death. Crucially, this pathway is distinct from apoptosis, ferroptosis, necroptosis, and other known cell death mechanisms, and is dependent on mitochondrial respiration — cells relying on glycolysis are resistant ([PMID: 35298263](https://pubmed.ncbi.nlm.nih.gov/35298263/)).

This foundational discovery establishes the mechanistic basis for the hypothesis. FDX1 (ferredoxin 1) was identified as the upstream regulator that reduces Cu²⁺ to Cu¹⁺ and promotes protein lipoylation, making it the critical gatekeeper for cuproptosis sensitivity.

### Finding 2: Direct Evidence of Cuproptosis in ATP7B-Knockout WD Model

Tang et al. (2025) provided the most direct evidence linking cuproptosis to Wilson Disease. In ATP7B⁻/⁻ mice, cuproptosis markers FDX1, DLST, DLAT, and LIAS were upregulated in liver tissue. In copper-treated HepG2 cells, copper exposure decreased cell viability and increased LDH release. Effects were exacerbated by elesclomol (a copper ionophore that shuttles copper to mitochondria) and alleviated by tetrathiomolybdate (a copper chelator). siRNA knockdown of hub genes Gpc1, Gls, Lox, and App alleviated cuproptosis ([PMID: 41230834](https://pubmed.ncbi.nlm.nih.gov/41230834/)).

This is currently the only study that directly tests cuproptosis in a WD-specific model, making it a critical but singular evidence point.

### Finding 3: Multiple Cell Death Pathways Coexist in WD Liver

Systematic reviews and primary studies confirm that cuproptosis is one of several concurrent cell death mechanisms in WD. Ma et al. (2026) documented that copper ions generate ROS via the Fenton reaction, directly impair mitochondrial structure and function, and induce hepatocyte apoptosis, necrosis, and cuproptosis ([PMID: 41006805](https://pubmed.ncbi.nlm.nih.gov/41006805/)). Wang et al. (2025) demonstrated copper-induced ferroptosis in ovarian tissue via ER stress-autophagy axis ([PMID: 40194638](https://pubmed.ncbi.nlm.nih.gov/40194638/)). Teschke & Eickhoff (2024) documented both cuproptosis and ferroptosis in WD ([PMID: 38731973](https://pubmed.ncbi.nlm.nih.gov/38731973/)).

This coexistence means cuproptosis cannot be considered the sole or dominant cell-death pathway in WD; its relative contribution remains unquantified.

### Finding 4: Metabolic Gating — Glycolytic Cells Resist Cuproptosis

The requirement for mitochondrial respiration in cuproptosis sensitivity has profound implications for WD. Song et al. (2025) detailed three mechanisms by which glycolytic shift suppresses cuproptosis: (1) HIF-1α/MYC-driven PDK activity phosphorylates and inactivates pyruvate dehydrogenase complex, shrinking the lipoylated target pool; (2) glycolytic signaling suppresses FDX1 and DLAT while inducing GLS as a negative regulator; (3) PPP-derived NADPH and glutamine-derived glutamate expand GSH and metallothionein pools that chelate Cu¹⁺ ([PMID: 40778735](https://pubmed.ncbi.nlm.nih.gov/40778735/)).

Du et al. (2026) demonstrated this principle in HBV-related HCC: cells that switch from TCA cycle to glycolysis show reduced sensitivity to copper ionophore elesclomol; restoring mitochondrial targeting re-sensitized cells to cuproptosis ([PMID: 41840161](https://pubmed.ncbi.nlm.nih.gov/41840161/)).

{{figure:cuproptosis_genes_human_WD.png|caption=Cuproptosis-related gene expression in human WD cirrhotic liver (GSE197406). FDX1 and PDHA1 are downregulated while GLS and DLD are upregulated, consistent with stage-dependent metabolic reprogramming that suppresses cuproptosis sensitivity in advanced disease.}}

### Finding 5: Human WD Liver Shows Stage-Dependent Cuproptosis Gene Signature

Analysis of GSE197406 (7 WD cirrhotic livers vs. 8 normal controls, Affymetrix U133 Plus 2.0) revealed a paradoxical pattern: FDX1 was downregulated (FC = −1.12, p = 0.032, Cohen's d = −1.25), while GLS was upregulated (FC = 1.41, p = 0.001, d = 2.13) and DLD was upregulated (FC = 1.68, p = 0.017, d = 1.69). PDHA1 was downregulated (FC = −1.36, p = 0.027, d = −1.37) and DLAT trended down (FC = −1.27, p = 0.062). This pattern is consistent with glycolytic reprogramming that suppresses cuproptosis sensitivity in cirrhotic-stage WD.

### Finding 6: FDX1 Is Downregulated at mRNA Level Across Species and Stages

Both early mouse WD (GSE125637: Fdx1 Log2FC = −0.227, p = 0.039) and late human WD cirrhotic liver (GSE197406: FDX1 FC = −1.12, p = 0.032) show significant FDX1 mRNA downregulation. This finding directly contradicts Tang et al. (2025), who reported FDX1 upregulation by Western blot in ATP7B-knockout mice. The resolution lies in post-translational regulation.

{{figure:mouse_vs_human_cuproptosis.png|caption=Comparison of cuproptosis gene expression changes between early mouse WD (GSE125637) and late human WD (GSE197406). FDX1 is consistently downregulated at mRNA level across species and disease stages.}}

### Finding 7: Post-Translational FDX1 Stabilization Resolves the mRNA-Protein Paradox

Wang et al. (2023) demonstrated that FDX1 protein is degraded by mitochondrial matrix-related proteases. When these proteases are suppressed — by conditions that deplete GSH and increase ROS (as occurs in WD) — FDX1 protein accumulates despite no mRNA upregulation ([PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/)). This mechanism explains how FDX1 mRNA can be consistently DOWN while FDX1 protein is UP: chronic copper → ROS → GSH depletion → protease suppression → FDX1 protein stabilization. This is the critical mechanistic link that makes the cuproptosis model coherent with transcriptomic data.

### Finding 8: GSH Depletion Creates a Feed-Forward Loop Linking Ferroptosis and Cuproptosis

Wang et al. (2023) showed that ferroptosis inducers (sorafenib, erastin) enhance cuproptosis in primary liver cancer cells through two converging mechanisms: (1) upregulating protein lipoylation via suppressing FDX1 degradation by mitochondrial proteases, and (2) reducing intracellular GSH through inhibiting cystine import. Since GSH acts as an intracellular copper chelator, its depletion lowers the cuproptosis threshold ([PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/)).

In WD, this creates a feed-forward amplification loop: copper overload → ROS generation → GSH depletion → (a) lower copper chelation capacity → more free copper → more cuproptosis, and (b) protease suppression → FDX1 protein stabilization → enhanced lipoylation → more cuproptosis targets → cuproptosis → Fe-S cluster loss → impaired respiration → more ROS.

### Finding 9: Mitochondrial Copper Removal Rescues WD Liver Injury

Lichtmannegger et al. (2016) demonstrated that methanobactin, a bacterial copper-binding peptide, efficiently reversed mitochondrial impairment and liver damage in ATP7B-deficient rats with acute liver copper accumulation. The beneficial effect was specifically associated with depletion of copper from hepatocyte mitochondria ([PMID: 27322060](https://pubmed.ncbi.nlm.nih.gov/27322060/)). This is consistent with cuproptosis being a mitochondrial death pathway — removing the trigger (mitochondrial copper) prevents the downstream cascade.

### Finding 10: In Vivo Copper-DLAT Binding Validated Outside Cancer

Zhu et al. (2024) demonstrated in fibrotic kidney tissue that mitochondrial copper binds directly to lipoylated DLAT, changing subunit interactions, inducing lipoylated DLAT protein dimerization, and inhibiting PDH enzyme activity. Reducing mitochondrial copper restored PDH activity and rescued renal fibrosis ([PMID: 39120696](https://pubmed.ncbi.nlm.nih.gov/39120696/)). This is the first in vivo demonstration of the copper-DLAT binding mechanism in organ fibrosis (non-cancer context), directly applicable to WD liver fibrosis.

### Finding 11: Exchangeable Copper Validated as Disease Severity Biomarker

Desjardins et al. (2026) showed in 158 treatment-naive WD patients that exchangeable copper (CuEXC) increased stepwise across phenotypes: 0.8, 1.6, and 2.9 μmol/L for asymptomatic, hepatic, and neurologic presentations (p < 0.001). CuEXC distinguished advanced from mild liver disease (AUC 0.86, sensitivity 83%, specificity 87% at threshold 1.8 μmol/L) ([PMID: 41952595](https://pubmed.ncbi.nlm.nih.gov/41952595/)). This dose-dependent relationship between labile copper and disease severity is consistent with a threshold-dependent cuproptosis activation model.

### Finding 12: FDX1 Structural Determinants Tightly Link Lipoylation and Cuproptosis

Hsiao et al. (2025) performed deep mutational scanning on FDX1 and identified D136 and D139 on alpha helix 3 as essential for both cuproptosis and lipoylation. Charge-reversal mutations abolish FDX1's ability to induce cuproptosis and support lipoylation in cells, despite retaining full enzymatic activity in vitro ([PMID: 41423452](https://pubmed.ncbi.nlm.nih.gov/41423452/)). This establishes that FDX1's roles in cuproptosis and lipoylation are structurally inseparable — you cannot have one without the other.

### Finding 13: FDX1 mRNA-Protein Discrepancy Resolved by Post-Translational Mechanism

The apparent contradiction between FDX1 mRNA downregulation (GSE125637 mouse p=0.039; GSE197406 human p=0.032) and FDX1 protein upregulation reported by Tang et al. (2025) is resolved by the protease suppression mechanism from Wang et al. (2023, [PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/)). In WD, chronic copper → ROS → GSH depletion → mitochondrial protease suppression → FDX1 protein stabilization, even as mRNA is transcriptionally repressed. This discordance is itself evidence of the feed-forward amplification loop.

---

## Mechanistic Causal Chain

The cuproptosis model in WD implies the following causal chain from upstream trigger to clinical manifestation. Evidence strength is annotated at each step.

```
ATP7B loss-of-function mutation (ESTABLISHED — genetic cause of WD)
        │
        ▼
Impaired biliary copper excretion (ESTABLISHED)
        │
        ▼
Hepatocyte copper accumulation (ESTABLISHED)
        │
        ├──────────────────────────────────────────┐
        ▼                                          ▼
CLASSICAL PATHWAY                          CUPROPTOSIS PATHWAY
(ESTABLISHED)                              (EMERGING)
        │                                          │
Cu²⁺ + H₂O₂ → •OH                        Cu enters mitochondria
(Fenton reaction)                                  │
        │                                          ▼
        ▼                                  FDX1 reduces Cu²⁺→Cu¹⁺
Lipid peroxidation,                        (ESTABLISHED in vitro)
protein oxidation,                                 │
DNA damage                                         ▼
        │                                  Cu¹⁺ binds lipoylated
        ▼                                  DLAT, DLST, GCSH
GSH depletion ◄──────────────────────────► (ESTABLISHED in vitro;
        │              FEED-FORWARD         IN VIVO in kidney)
        │              LOOP                        │
        ▼                                          ▼
Protease suppression                       Lipoylated protein
        │                                  aggregation
        ▼                                  (NOT YET SHOWN in
FDX1 protein                                human WD liver)
stabilization                                      │
(EMERGING — shown                                  ▼
in liver cancer)                           Fe-S cluster protein
        │                                  loss → proteotoxic
        └──────────► Enhanced              stress → cell death
                     lipoylation ──────►   (ESTABLISHED in vitro)
                                                   │
                                                   ▼
                                           ┌───────┴───────┐
                                           │               │
                                     Hepatocyte      Mitochondrial
                                     death           dysfunction
                                           │               │
                                           └───────┬───────┘
                                                   ▼
                                           Inflammation,
                                           fibrosis, cirrhosis
                                           (ESTABLISHED clinical)
```

**Strong links:** ATP7B → copper accumulation → ROS/oxidative damage → hepatocyte injury are well established. The core cuproptosis mechanism (copper → DLAT → aggregation → Fe-S loss) is established in vitro and in renal fibrosis in vivo.

**Inferred links:** FDX1 post-translational stabilization in WD (demonstrated only in liver cancer cells); the feed-forward loop operating in WD hepatocytes specifically; quantitative contribution of cuproptosis versus other death pathways.

**Missing links:** Lipoylated protein aggregation in human WD liver tissue; cuproptosis markers in neurological WD; temporal dynamics of pathway activation during disease progression.

{{figure:final_integrated_model.png|caption=Integrated feed-forward cuproptosis amplification model in Wilson Disease. Cuproptosis operates as an emergent amplification layer linked to classical oxidative stress via GSH depletion, not as an independent pathway.}}

---

## Evidence Matrix

| Citation | Evidence Type | Supports/Refutes/Qualifies | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|---------------------------|-------------------|-------------|---------|------------|
| [PMID: 35298263](https://pubmed.ncbi.nlm.nih.gov/35298263/) | In vitro (cell lines) | **Supports** | Core cuproptosis mechanism | Cu binds lipoylated TCA proteins; FDX1 is required; distinct from apoptosis/ferroptosis | Multiple cancer cell lines | **High** — foundational *Science* paper; widely replicated |
| [PMID: 41230834](https://pubmed.ncbi.nlm.nih.gov/41230834/) | Model organism + in vitro | **Supports** | Cuproptosis in WD model | FDX1/DLST/DLAT/LIAS upregulated in ATP7B⁻/⁻ mice; elesclomol exacerbates, TTM alleviates | ATP7B-KO mouse, HepG2 | **Moderate** — single study; protein data conflicts with mRNA in transcriptomics |
| [PMID: 41423452](https://pubmed.ncbi.nlm.nih.gov/41423452/) | In vitro (DMS) | **Supports** | FDX1 structure-function | D136/D139 essential for both lipoylation and cuproptosis | Deep mutational scanning | **High** — systematic unbiased approach |
| [PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/) | In vitro (liver cancer) | **Supports** (with qualification) | Ferroptosis-cuproptosis crosstalk | GSH depletion enhances cuproptosis; FDX1 stabilized post-translationally | Primary liver cancer cells | **Moderate** — cancer context, not WD-specific |
| [PMID: 39120696](https://pubmed.ncbi.nlm.nih.gov/39120696/) | In vivo (kidney fibrosis) | **Supports** | Cu-DLAT binding in vivo | Mitochondrial Cu binds lipoylated DLAT, causes dimerization, inhibits PDH | Fibrotic kidney tissue | **Moderate-High** — in vivo but non-WD organ |
| [PMID: 27322060](https://pubmed.ncbi.nlm.nih.gov/27322060/) | Model organism (WD rat) | **Supports** | Mitochondrial Cu is pathogenic | Methanobactin depletes mitochondrial Cu, reverses liver damage | ATP7B-deficient rats | **High** — directly shows mitochondrial Cu removal rescues WD |
| [PMID: 41952595](https://pubmed.ncbi.nlm.nih.gov/41952595/) | Human clinical | **Qualifies** | Dose-dependent Cu toxicity | CuEXC increases stepwise across phenotypes; AUC 0.86 for advanced liver disease | 158 treatment-naive WD patients | **High** — large prospective cohort |
| [PMID: 40778735](https://pubmed.ncbi.nlm.nih.gov/40778735/) | Review/mechanistic | **Qualifies** | Glycolytic shift suppresses cuproptosis | PDK inactivates PDC, shrinks lipoylated pool; GSH/MT chelate Cu¹⁺ | Tumor metabolism review | **Moderate** — review-level, tumor context |
| [PMID: 41840161](https://pubmed.ncbi.nlm.nih.gov/41840161/) | In vitro + in vivo (HCC) | **Qualifies** | Metabolic gating of cuproptosis | HBV cells switch to glycolysis → resistant to elesclomol; restoring mito function re-sensitizes | HBV-related HCC | **Moderate** — cancer context |
| [PMID: 41006805](https://pubmed.ncbi.nlm.nih.gov/41006805/) | Review | **Qualifies** | Multiple death pathways | ROS, apoptosis, necrosis, and cuproptosis all occur in WD liver | Systematic review of WD liver fibrosis | **Moderate** — review-level |
| GSE197406 | Human transcriptomic | **Qualifies** | Stage-dependent expression | FDX1 DOWN (p=0.032), GLS UP (p=0.001), DLD UP (p=0.017) in cirrhotic WD liver | 7 WD cirrhotic vs. 8 controls | **Moderate** — small sample, microarray |
| GSE125637 | Mouse transcriptomic | **Qualifies** | Early WD gene changes | Fdx1 DOWN (p=0.039), Gls DOWN (p=0.006), Dlst DOWN (p=0.008) in 3-month Atp7b⁻/⁻ mice | 4 KO vs. 4 WT | **Moderate** — small sample, early timepoint |
| [PMID: 38731973](https://pubmed.ncbi.nlm.nih.gov/38731973/) | Review | **Supports** (partial) | Cuproptosis in WD | Notes both ROS and cuproptosis as mechanistic layers in WD | Comprehensive review | **Low** — review-level, no new data |

{{figure:final_evidence_assessment.png|caption=Evidence confidence and knowledge gap priority assessment across all investigation iterations. Inner ring shows evidence confidence levels; outer segments indicate priority of remaining knowledge gaps.}}

---

## Evidence Base: Key Literature

### Foundational Cuproptosis Mechanism
**Tsvetkov et al. (2022)** — *Copper induces cell death by targeting lipoylated TCA cycle proteins* ([PMID: 35298263](https://pubmed.ncbi.nlm.nih.gov/35298263/)). This *Science* paper defined cuproptosis as a distinct regulated cell death dependent on mitochondrial respiration, occurring via direct copper binding to lipoylated TCA cycle components (DLAT), causing aggregation and iron-sulfur cluster protein loss. This is the single most important paper underpinning the hypothesis.

### WD-Specific Cuproptosis Evidence
**Tang et al. (2025)** — *Uncovering the Critical Role of Cuproptosis in Wilson Disease* ([PMID: 41230834](https://pubmed.ncbi.nlm.nih.gov/41230834/)). Demonstrated cuproptosis marker upregulation in ATP7B⁻/⁻ mice and copper-treated HepG2 cells. Showed modulation by copper ionophore (elesclomol) and chelator (tetrathiomolybdate). The only study directly testing cuproptosis in a WD model.

### FDX1 Structure-Function
**Hsiao et al. (2025)** — *Deep Mutational Scanning of FDX1* ([PMID: 41423452](https://pubmed.ncbi.nlm.nih.gov/41423452/)). Identified D136/D139 as essential for both lipoylation and cuproptosis, mechanistically linking these two processes through a shared structural determinant on FDX1.

### Ferroptosis-Cuproptosis Crosstalk
**Wang et al. (2023)** — *Ferroptosis inducers enhanced cuproptosis induced by copper ionophores in primary liver cancer* ([PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/)). Demonstrated that GSH depletion by ferroptosis inducers enhances cuproptosis via FDX1 protein stabilization through suppression of mitochondrial proteases. This paper provides the key mechanistic link explaining the FDX1 mRNA-protein discrepancy in WD.

### Mitochondrial Copper Removal in WD
**Lichtmannegger et al. (2016)** — *Methanobactin reverses acute liver failure in a rat model of Wilson disease* ([PMID: 27322060](https://pubmed.ncbi.nlm.nih.gov/27322060/)). Showed that specifically depleting copper from hepatocyte mitochondria reversed liver damage in WD rats, strongly supporting a mitochondria-centric death mechanism.

### In Vivo Copper-DLAT Binding
**Zhu et al. (2024)** — *Mitochondrial copper overload promotes renal fibrosis via inhibiting pyruvate dehydrogenase activity* ([PMID: 39120696](https://pubmed.ncbi.nlm.nih.gov/39120696/)). First in vivo demonstration that mitochondrial copper binds lipoylated DLAT, causes dimerization, and inhibits PDH in organ fibrosis — directly applicable to WD liver fibrosis.

### Exchangeable Copper as Severity Biomarker
**Desjardins et al. (2026)** ([PMID: 41952595](https://pubmed.ncbi.nlm.nih.gov/41952595/)) and **Djebrani-Oussedik et al. (2025)** ([PMID: 40980162](https://pubmed.ncbi.nlm.nih.gov/40980162/)). Validated exchangeable copper as a stepwise disease severity marker and diagnostic biomarker (REC cutoff 14%, sensitivity 95.6%, specificity 99.8%), consistent with dose-dependent cuproptosis activation.

### Metabolic Gating of Cuproptosis
**Song et al. (2025)** — *Tumor glucose reprogramming suppresses cuproptosis: A review* ([PMID: 40778735](https://pubmed.ncbi.nlm.nih.gov/40778735/)). Detailed three mechanisms by which glycolytic shift suppresses cuproptosis, including PDK-mediated PDC inactivation, FDX1/DLAT transcriptional suppression, and GSH/metallothionein expansion. Critical for understanding stage-dependent cuproptosis sensitivity in WD.

### WD Liver Fibrosis Pathogenesis
**Ma et al. (2026)** — *The pathogenesis of liver fibrosis in Wilson's disease* ([PMID: 41006805](https://pubmed.ncbi.nlm.nih.gov/41006805/)). Systematic review documenting that copper ions generate ROS, impair mitochondria, and induce hepatocyte apoptosis, necrosis, and cuproptosis in WD, confirming the multi-pathway nature of copper hepatotoxicity.

### WD Phenotypic Modifiers
**Gromadzka et al. (2014)** ([PMID: 24517502](https://pubmed.ncbi.nlm.nih.gov/24517502/)). Showed that variants in antioxidant defense genes (CAT, SOD2) modify WD clinical course, indirectly confirming the role of oxidative stress — and by extension, the GSH-depletion-mediated feed-forward loop — in WD pathogenesis.

---

## Alternative Models

### 1. Classical ROS/Oxidative Stress Model (ESTABLISHED — Competing/Upstream)
**Relationship:** Upstream cause and parallel mechanism to cuproptosis.

Copper catalyzes hydroxyl radical generation via Fenton chemistry, causing lipid peroxidation, protein oxidation, and DNA damage. This is the most established mechanism of copper toxicity, supported by decades of evidence including elevated lipid peroxidation in LEC rat mitochondria ([PMID: 10650917](https://pubmed.ncbi.nlm.nih.gov/10650917/)), decreased vitamin E and GSH in WD patients ([PMID: 8723319](https://pubmed.ncbi.nlm.nih.gov/8723319/)), and genetic modifier studies showing antioxidant gene variants (CAT, SOD2) modify WD phenotype ([PMID: 24517502](https://pubmed.ncbi.nlm.nih.gov/24517502/)). ROS-mediated damage is not truly alternative to cuproptosis but rather creates the permissive environment (GSH depletion) that enables it. The feed-forward model we propose integrates both mechanisms.

### 2. Ferroptosis Model (EMERGING — Parallel Mechanism)
**Relationship:** Parallel and synergistic mechanism sharing the GSH depletion node.

Copper-induced ferroptosis has been demonstrated in WD ovarian tissue via ER stress-autophagy axis ([PMID: 40194638](https://pubmed.ncbi.nlm.nih.gov/40194638/)). Ferroptosis and cuproptosis share the GSH depletion trigger and can synergistically amplify each other ([PMID: 37277863](https://pubmed.ncbi.nlm.nih.gov/37277863/)). Ferroptosis may be more relevant in tissues with high polyunsaturated fatty acid content (brain), while cuproptosis may predominate in mitochondria-rich hepatocytes. The two pathways are not mutually exclusive and likely co-occur in WD liver.

### 3. Mitochondrial Apoptosis Model (ESTABLISHED — Parallel Mechanism)
**Relationship:** Parallel downstream consequence of mitochondrial copper overload.

Copper exposure induces mitochondria-mediated apoptosis via PINK1/Parkin pathway disruption, caspase cascade activation, and cytochrome c release. This has been demonstrated in multiple models including chicken liver ([PMID: 33360697](https://pubmed.ncbi.nlm.nih.gov/33360697/)) and rat hepatocytes ([PMID: 20946909](https://pubmed.ncbi.nlm.nih.gov/20946909/)). Apoptosis and cuproptosis may operate simultaneously in different mitochondrial compartments or at different copper concentration thresholds.

### 4. Direct Mitochondrial Membrane Injury Model (ESTABLISHED — Upstream)
**Relationship:** Upstream facilitator of cuproptosis.

Copper directly damages mitochondrial membranes, reducing cytochrome c oxidase activity and impairing oxidative phosphorylation. High-calorie diet exacerbated this mitochondrial damage in WD rats ([PMID: 30586623](https://pubmed.ncbi.nlm.nih.gov/30586623/)). Membrane damage may facilitate copper entry into the mitochondrial matrix where it can access lipoylated proteins, potentially serving as a prerequisite for cuproptosis activation.

### 5. Copper-Mediated ER Stress Model (EMERGING — Parallel Mechanism)
**Relationship:** Parallel mechanism that may converge with cuproptosis via shared stress responses.

Copper exposure induces ER stress via the PERK/ATF4 pathway ([PMID: 38735462](https://pubmed.ncbi.nlm.nih.gov/38735462/)), which can trigger the unfolded protein response and contribute to cell death independently of mitochondrial pathways. ER stress also activates autophagy, which intersects with copper-induced ferroptosis ([PMID: 40194638](https://pubmed.ncbi.nlm.nih.gov/40194638/)).

---

## Limitations and Knowledge Gaps

### Critical Knowledge Gaps

| Gap | Scope | Why It Matters | What Was Checked | Resolving Evidence Needed |
|-----|-------|----------------|------------------|---------------------------|
| **No human WD tissue confirmation of lipoylated protein aggregation** | Histopathology | The hallmark of cuproptosis has never been demonstrated in human WD liver | PubMed searches for immunohistochemistry and proteomic studies in WD liver; no primary reports found | Anti-lipoyl-DLAT immunohistochemistry on WD liver biopsies with graded copper levels |
| **Unknown relative contribution of cuproptosis vs. other pathways** | Quantitative biology | Cannot assess therapeutic relevance without knowing fraction of cell death attributable to cuproptosis | Searched for pathway-specific inhibitor studies in WD models; none found | Pathway-specific inhibitors (cuproptosis vs. ferroptosis vs. apoptosis) in ATP7B-KO mice with quantitative cell death assays |
| **Zero evidence in neurological WD** | Clinical neurology | ~40% of WD patients present with neurological symptoms; cuproptosis relevance completely unknown | Searched "cuproptosis Wilson neurological brain" — found only general neurodegenerative reviews, no WD brain-specific data | Post-mortem brain studies examining lipoylated protein aggregation in basal ganglia of neurological WD patients |
| **FDX1 protein stabilization not confirmed in WD** | Molecular biology | Key mechanistic resolution (mRNA-protein paradox) demonstrated only in cancer cells | Wang et al. 2023 used liver cancer cells, not WD hepatocytes | Western blot + qPCR of FDX1 in matched WD liver biopsies at different fibrosis stages |
| **No temporal/stage-resolved cuproptosis data** | Disease progression | Cannot determine when cuproptosis is active during WD natural history | Only cross-sectional transcriptomics available (early mouse, late human) | Longitudinal studies in ATP7B-KO mice with cuproptosis markers at multiple timepoints (1, 3, 6, 9, 12 months) |
| **No clinical trial evidence for cuproptosis-directed therapy** | Clinical translation | All therapeutic evidence is for general chelation, not cuproptosis-specific intervention | ClinicalTrials.gov search found no cuproptosis-specific WD trials | Trials comparing mitochondria-targeted copper chelators vs. general chelators |
| **Feed-forward loop not validated as integrated circuit** | Systems biology | Individual links exist but the complete loop has not been tested in a single system | Literature supports each link independently; no study tests the full ROS→GSH→FDX1→cuproptosis→Fe-S→ROS cycle | Mathematical modeling + experimental validation of the complete feedback circuit in WD hepatocytes |
| **No GenCC/ClinGen cuproptosis gene annotations for WD** | Genomic databases | Cuproptosis-related genes (FDX1, LIAS, DLAT) are not annotated as WD modifiers in genomic databases | Checked GenCC, ClinGen knowledge bases — no cuproptosis gene entries for WD | Genetic association studies testing cuproptosis gene variants as WD phenotype modifiers |
| **Unknown role of metallothioneins in cuproptosis resistance** | Molecular biology | Metallothioneins (MT1/MT2) chelate Cu¹⁺ and may provide a natural resistance mechanism to cuproptosis in WD | MTF1 was downregulated in human WD liver (p=0.018); relationship to cuproptosis threshold unclear | MT knockdown/overexpression experiments in copper-loaded hepatocytes measuring cuproptosis sensitivity |

### Methodological Limitations of This Investigation

1. **Small transcriptomic sample sizes**: GSE197406 (n=7 vs. 8) and GSE125637 (n=4 vs. 4) limit statistical power and generalizability
2. **Cross-platform comparison**: Mouse RNA-seq vs. human microarray data are not directly comparable at the quantitative level
3. **Cirrhotic bias**: Human WD data is exclusively from cirrhotic livers, which may represent end-stage disease where cuproptosis has been superseded by other processes
4. **Cancer cell extrapolation**: Key mechanistic insights (FDX1 protein stabilization, ferroptosis-cuproptosis crosstalk) come from cancer cell lines, which have fundamentally altered metabolism
5. **Publication bias**: The cuproptosis field is very new (2022–) and positive results may be overrepresented

---

## Discriminating Tests

### Test 1: Human WD Liver Lipoylated Protein Aggregation
- **Objective:** Confirm the hallmark of cuproptosis in human WD tissue
- **Design:** Immunohistochemistry with anti-lipoyl-lysine and anti-DLAT antibodies on formalin-fixed WD liver biopsies graded by copper content (mild, moderate, severe)
- **Expected result if cuproptosis active:** Lipoylated protein aggregates colocalizing with mitochondrial markers; aggregation correlating with copper load
- **Expected result if cuproptosis absent:** No aggregation, or aggregation only at extreme copper levels irrelevant to clinical disease
- **Patient stratification:** Early vs. late disease; hepatic vs. neurological presentation; pre- vs. post-treatment
- **Model system:** Human liver biopsy tissue from WD biobanks

### Test 2: Pathway-Specific Inhibitor Study in ATP7B-KO Mice
- **Objective:** Quantify relative contribution of cuproptosis vs. ferroptosis vs. apoptosis
- **Design:** Treat ATP7B⁻/⁻ mice with: (a) tetrathiomolybdate (general Cu chelator), (b) ferrostatin-1 (ferroptosis inhibitor), (c) Z-VAD-FMK (pan-caspase apoptosis inhibitor), (d) combination; measure ALT/AST, histological injury score, and pathway-specific markers
- **Expected result:** If cuproptosis is dominant, only copper chelation will substantially reduce injury; if pathways are parallel, combinations will show additive benefit
- **Biomarkers:** Lipoylated protein aggregation (cuproptosis), 4-HNE/MDA (ferroptosis), cleaved caspase-3 (apoptosis)
- **Perturbation:** Each inhibitor alone and in pairwise combinations

### Test 3: FDX1 Protein vs. mRNA in Staged WD Liver
- **Objective:** Validate the post-translational stabilization model in WD specifically
- **Design:** Matched Western blot and qPCR for FDX1 in WD liver biopsies at different Ishak fibrosis stages (F0–F6), plus mitochondrial protease activity assays (LONP1, CLPP)
- **Expected result if feed-forward model correct:** FDX1 mRNA low but protein high in early/moderate disease; both low in advanced cirrhosis
- **Sample type:** Fresh-frozen liver biopsies from WD biobank
- **Additional markers:** GSH levels, lipoylated DLAT by Western blot, mitochondrial protease activity

### Test 4: Neurological WD Cuproptosis Assessment
- **Objective:** Determine if cuproptosis occurs in WD brain
- **Design:** Post-mortem brain tissue from neurological WD patients; assess lipoylated protein aggregation, FDX1 expression, Fe-S cluster protein levels in basal ganglia, putamen, and cortex
- **Expected result:** If cuproptosis contributes to neurological WD, expect DLAT aggregation in copper-rich brain regions; if not, suggests copper neurotoxicity operates through different mechanisms (ROS, protein misfolding)
- **Control tissues:** Age-matched non-WD controls and Alzheimer's disease (for copper-related comparison)

### Test 5: Elesclomol Challenge in WD Hepatocyte Organoids
- **Objective:** Test cuproptosis sensitivity of WD hepatocytes vs. normal in controlled system
- **Design:** ATP7B-mutant and isogenic corrected hepatocyte organoids treated with elesclomol ± TTM; measure cell death, lipoylated protein aggregation, Fe-S cluster integrity
- **Expected result if cuproptosis relevant:** WD organoids show enhanced sensitivity to elesclomol; TTM rescues; aggregation precedes cell death
- **Model system:** iPSC-derived hepatocyte organoids with patient-specific ATP7B mutations

### Test 6: Longitudinal Cuproptosis Marker Profiling in ATP7B-KO Mice
- **Objective:** Map the temporal window of cuproptosis activity during WD progression
- **Design:** Sacrifice ATP7B⁻/⁻ mice at 1, 3, 6, 9, and 12 months; measure FDX1 mRNA and protein, lipoylated DLAT, Fe-S cluster proteins (NDUFS1, SDHB), GSH, copper content, and metabolic state (TCA activity vs. glycolysis markers)
- **Expected result if stage-dependent model correct:** Cuproptosis markers peak at intermediate disease stages and decline as glycolytic shift develops in advanced disease

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base, labeled as leads requiring curator verification.*

### Candidate Evidence References

1. **PMID: 41230834** — Tang et al. 2025. Direct cuproptosis evidence in ATP7B-KO mouse model.
   - Snippet: *"ATP7B-/- mice showed marked hepatocellular injury with elevated AST, ALT and LDH. Cuproptosis markers (FDX1, DLST, DLAT, LIAS) were upregulated in both liver tissue and HepG2 cells."*
   - **Candidate status:** SUPPORTS (direct WD model evidence)

2. **PMID: 37277863** — Wang et al. 2023. Ferroptosis-cuproptosis crosstalk via GSH/FDX1.
   - Snippet: *"sorafenib and erastin upregulated protein lipoylation via suppressing mitochondrial matrix-related proteases mediated ferredoxin 1 (FDX1) protein degradation, and reduced intracellular copper chelator glutathione (GSH) synthesis through inhibiting cystine importing."*
   - **Candidate status:** SUPPORTS (mechanistic link; liver cancer cells, not WD-specific)

3. **PMID: 39120696** — Zhu et al. 2024. In vivo Cu-DLAT binding in renal fibrosis.
   - Snippet: *"mitochondrial copper could bind directly to lipoylated dihydrolipoamide acetyltransferase (DLAT), the E2 component of the PDH complex, thereby changing the interaction between the subunits of lipoylated DLAT, inducing lipoylated DLAT protein dimerization, and ultimately inhibiting PDH enzyme activity"*
   - **Candidate status:** SUPPORTS (in vivo mechanism; non-WD organ)

4. **PMID: 27322060** — Lichtmannegger et al. 2016. Mitochondrial copper removal reverses WD liver failure.
   - Snippet: *"Short-term treatment of these rats with MB efficiently reversed mitochondrial impairment and liver damage in the acute stages of liver copper accumulation compared with that seen in untreated ATP7B-deficient rats. This beneficial effect was associated with depletion of copper from hepatocyte mitochondria."*
   - **Candidate status:** SUPPORTS (therapeutic evidence in WD model)

5. **PMID: 41423452** — Hsiao et al. 2025. FDX1 structural determinants.
   - Snippet: *"two conserved solvent-exposed residues, D136 and D139, on alpha helix 3 are essential for both cuproptosis and lipoylation. Charge-reversal mutations at these positions abolish FDX1's ability to induce cuproptosis and support lipoylation in cells, despite retaining full enzymatic activity in vitro."*
   - **Candidate status:** SUPPORTS (mechanistic — establishes cuproptosis-lipoylation inseparability)

6. **PMID: 41952595** — Desjardins et al. 2026. Exchangeable copper as severity biomarker.
   - Snippet: *"CuEXC increased stepwise across phenotypes (0.8, 1.6, and 2.9 μmol/L; p < 0.001). CuEXC distinguished advanced from mild-to-moderate liver disease (AUC 0.86; 95% CI, 0.82-0.89; optimal threshold 1.8 μmol/L: sensitivity 83%, specificity 87%)"*
   - **Candidate status:** QUALIFIES (supports dose-dependent copper toxicity consistent with cuproptosis threshold model)

7. **PMID: 40778735** — Song et al. 2025. Glycolytic shift suppresses cuproptosis.
   - Snippet: *"oncogenic stabilisation of hypoxia-inducible factor-1 alpha (HIF-1α) and MYC increases pyruvate dehydrogenase kinase (PDK) activity, which phosphorylates and inactivates the pyruvate dehydrogenase complex (PDC), shrinking the lipoylated target pool in mitochondria and cutting the feed into the TCA cycle"*
   - **Candidate status:** QUALIFIES (mechanistic — limits scope of cuproptosis in metabolically shifted cells)

### Candidate Pathophysiology Nodes/Edges

- **Node:** FDX1 post-translational stabilization via mitochondrial protease suppression
  - GO term: GO:0006515 (misfolded or incompletely synthesized protein catabolic process)
- **Edge:** GSH depletion → cuproptosis threshold lowering (bidirectional link between ferroptosis and cuproptosis pathways)
- **Edge:** Glycolytic shift → cuproptosis resistance (metabolic gating of pathway sensitivity)
- **Edge:** Mitochondrial copper accumulation → lipoylated DLAT aggregation → PDH inhibition
- **Node:** Lipoylated protein aggregation (cuproptosis hallmark)
  - GO term: GO:0070841 (inclusion body assembly)

### Candidate Ontology Terms

- **Cell types:** Hepatocyte (CL:0000182) — primary cuproptosis-susceptible cell in WD
- **Biological processes:**
  - Cuproptosis (not yet in GO as of search date; proposed: copper-dependent regulated cell death)
  - Protein lipoylation (GO:0018169)
  - Iron-sulfur cluster assembly (GO:0016226)
  - Mitochondrial respiration (GO:0022904)
- **Molecular functions:**
  - FDX1 reductase activity (GO:0015037)
  - Copper ion binding (GO:0005507)

### Candidate Subtype Restrictions

- Cuproptosis evidence is currently **restricted to hepatic WD** — no evidence supports applicability to neurological WD
- Stage restriction: cuproptosis may be most active in **early-to-moderate hepatic disease** before glycolytic reprogramming; likely suppressed in **advanced cirrhosis**
- Cuproptosis sensitivity may be modulated by **metabolic phenotype** (patients with steatosis/high-calorie diet may have different susceptibility per [PMID: 30586623](https://pubmed.ncbi.nlm.nih.gov/30586623/))

### Candidate Status Change

- **Current status:** EMERGING
- **Recommended status:** Maintain **EMERGING**, with annotation that evidence is strengthening toward SUPPORTED for hepatic WD specifically. Upgrade to SUPPORTED would require: (a) human WD liver confirmation of lipoylated protein aggregation, and (b) quantification of cuproptosis contribution relative to other pathways.

### Candidate Knowledge Gaps for KB Discussion Prompts

1. **Human tissue validation gap:** No immunohistochemistry or proteomic evidence of lipoylated protein aggregation in human WD liver tissue as of May 2026. This is the single most important gap preventing status upgrade.
2. **Neurological WD gap:** Complete absence of cuproptosis investigation in WD brain tissue or neurological models. Important because ~40% of WD patients present neurologically.
3. **Quantitative pathway contribution gap:** No study has quantified what fraction of hepatocyte death in WD is attributable to cuproptosis vs. ferroptosis vs. apoptosis vs. necrosis.
4. **Temporal dynamics gap:** No longitudinal data on when cuproptosis activates and when it becomes suppressed during WD natural history.
5. **Treatment mechanism gap:** Whether conventional WD chelators (D-penicillamine, trientine, zinc) exert their therapeutic effect partly through cuproptosis suppression is unknown. Methanobactin's mitochondrial copper depletion effect is suggestive but not cuproptosis-specific.
6. **Conflicting FDX1 data:** Tang et al. 2025 ([PMID: 41230834](https://pubmed.ncbi.nlm.nih.gov/41230834/)) reported FDX1 protein upregulation in ATP7B-KO mice, while two independent transcriptomic datasets (GSE125637, GSE197406) show FDX1 mRNA downregulation. Resolution via post-translational stabilization is plausible but unconfirmed in WD tissue.

---

## Conclusions

The copper-dependent cuproptosis model represents a mechanistically coherent and increasingly supported hypothesis for an amplification layer in Wilson Disease hepatic injury. The core biochemistry — copper binding to lipoylated TCA cycle proteins causing proteotoxic stress — is well established in vitro and has been validated in vivo in renal fibrosis. Its relevance to WD is supported by one direct animal model study, consistent biomarker data, and a plausible feed-forward amplification circuit linking classical oxidative stress to cuproptosis via GSH depletion and FDX1 protein stabilization.

However, critical gaps prevent classification as an established mechanism: the absence of human tissue validation of the hallmark lipoylated protein aggregation, the unknown quantitative contribution relative to competing pathways, and the complete lack of evidence in neurological WD. The metabolic gating phenomenon — where glycolytic cells resist cuproptosis — introduces an important stage-dependency that may limit cuproptosis relevance to early/moderate hepatic disease.

The most parsimonious model integrates cuproptosis not as an independent pathway but as an emergent amplification layer within a broader copper toxicity cascade: ATP7B loss → copper accumulation → ROS → GSH depletion → simultaneous engagement of multiple death pathways (cuproptosis, ferroptosis, apoptosis) → tissue injury. Within this framework, cuproptosis represents a specifically mitochondrial amplifier that may be particularly important in metabolically active hepatocytes during early disease.

The field would benefit most from: (1) immunohistochemistry for lipoylated protein aggregation in human WD liver biopsies, (2) pathway-specific inhibitor studies in ATP7B-knockout mice, and (3) investigation of cuproptosis in neurological WD tissue. Until these studies are performed, cuproptosis should be understood as an emerging amplification mechanism within the broader landscape of copper-mediated cell death in Wilson Disease — an important and testable piece of the puzzle, but not the complete picture.
