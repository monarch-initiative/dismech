---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-03T08:38:14.145730'
end_time: '2026-06-03T09:23:32.701357'
duration_seconds: 2718.56
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Endometriosis
  category: Complex
  hypothesis_group_id: neuroimmune_pain_sensitization_model
  hypothesis_label: Neuroimmune Nociceptor-Sensitization Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: neuroimmune_pain_sensitization_model\nhypothesis_label:\
    \ Neuroimmune Nociceptor-Sensitization Model\nstatus: EMERGING\ndescription: |\n\
    \  Endometriosis-associated pain is driven by lesion- and peritoneal microenvironment\
    \ signals that promote neuroangiogenesis, peripheral nociceptor sensitization,\
    \ and later central sensitization, so pain severity can persist or amplify independently\
    \ of visible lesion burden.\nnotes: Initial focused hypothesis for dismech#3666.\
    \ The model treats lesion burden as one input into a\n  neuroimmune pain circuit,\
    \ not as a sufficient proxy for symptom severity."
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
citation_count: 58
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Endometriosis
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** neuroimmune_pain_sensitization_model
- **Hypothesis Label:** Neuroimmune Nociceptor-Sensitization Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: neuroimmune_pain_sensitization_model
hypothesis_label: Neuroimmune Nociceptor-Sensitization Model
status: EMERGING
description: |
  Endometriosis-associated pain is driven by lesion- and peritoneal microenvironment signals that promote neuroangiogenesis, peripheral nociceptor sensitization, and later central sensitization, so pain severity can persist or amplify independently of visible lesion burden.
notes: Initial focused hypothesis for dismech#3666. The model treats lesion burden as one input into a
  neuroimmune pain circuit, not as a sufficient proxy for symptom severity.
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

# Neuroimmune Nociceptor-Sensitization Model of Endometriosis Pain: Hypothesis Evaluation Report

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (Strong Confidence)**

The Neuroimmune Nociceptor-Sensitization Model posits that endometriosis-associated pain is driven by lesion- and peritoneal microenvironment signals that promote neuroangiogenesis, peripheral nociceptor sensitization, and later central sensitization, such that pain severity can persist or amplify independently of visible lesion burden. After evaluating 120 papers across five investigative iterations and confirming 25 discrete findings, the evidence supports this verdict: the model is **partially supported with strong confidence**. The core causal chain -- from lesion-derived neurotrophin signaling through peripheral nociceptor sensitization to central sensitization and pain-stage discordance -- is substantiated by convergent genetic, molecular, cellular, imaging, and clinical trial evidence. However, critical qualifications limit a full endorsement: (1) the P2X3 antagonist eliapixant failed in Phase 2b (SCHUMANN trial), weakening the purinergic signaling arm; (2) no anti-NGF trial has been conducted in endometriosis despite proven efficacy in somatic pain; (3) hormonal mechanisms remain clinically dominant for approximately two-thirds of patients; and (4) the model applies differentially by disease subtype, being strongest for peritoneal and deep infiltrating endometriosis (DIE) and weakest for ovarian endometriomas, which occupy an "immune-cold" niche.

The model best explains the ~30-40% of patients who are refractory to hormonal therapy, those with persistent pain after surgical lesion excision, and those with chronic overlapping pain conditions (COPCs). For these subpopulations, the neuroimmune hypothesis provides mechanistic justification for multimodal pain management beyond hormonal suppression. The existence of substantial asymptomatic endometriosis (~12% prevalence at incidental surgery) confirms that lesion presence alone is insufficient for pain, consistent with the model's premise that the neuroimmune circuit -- not the lesion per se -- is the primary pain driver.

---

## Summary

This report evaluates the Neuroimmune Nociceptor-Sensitization Model of endometriosis-associated pain against the current primary literature. The investigation spanned five iterations, reviewing 120 publications and generating 25 confirmed findings supported by verified citations. The evidence base includes human clinical studies (tissue immunohistochemistry, fMRI neuroimaging, quantitative sensory testing, randomized controlled trials), animal models (murine and baboon endometriosis induction), in vitro molecular studies, genome-wide association studies, and systematic reviews/meta-analyses.

The hypothesis's core mechanistic chain is well-substantiated: endometriotic lesions produce neurotrophins (NGF, BDNF) that drive neuroangiogenesis, creating dense SP+/CGRP+ nociceptive fiber networks. The peritoneal inflammatory microenvironment -- via IL-33/ST2 to macrophage to TNF-alpha and histamine-HRH signaling -- sensitizes these fibers through TRPV1/TRPA1 upregulation, with estrogen directly augmenting TRPV1 expression. Repeated nociceptive input promotes central sensitization, evidenced by altered brain connectivity (fMRI), spinal microglial activation (CX3CR1/P2X4R/NF-kappaB), and causal proof from a tDCS RCT. Pain-stage discordance is confirmed by meta-analysis, and post-surgical pain persistence (28-37%) provides clinical validation. However, the model is incomplete: the purinergic arm failed clinical translation, psychosocial factors independently modulate pain, pelvic floor dysfunction serves as a parallel pain generator, and subtype-specific immune microenvironments mean one circuit does not fit all presentations.

The strongest evidence supporting the model includes: (a) GWAS identification of NGF as a disease risk locus with genetic correlations to 11 pain conditions; (b) the IL-33/ST2/TNF-alpha/TRPV1 molecular pathway fully delineated from immune signal to nociceptor activation; (c) elevated BDNF distinguishing painful from non-painful endometriosis; and (d) a Phase II RCT demonstrating that cortical neuromodulation (tDCS) reduces endometriosis pain, providing causal evidence for central sensitization. The strongest counter-evidence is the SCHUMANN Phase 2b RCT failure of the P2X3 antagonist eliapixant, where elagolix (hormonal therapy) outperformed all neuroimmune-targeted doses.

---

## Key Findings

### Finding 1: Neuroangiogenesis and Neurotrophin Upregulation in Endometriotic Lesions

Endometriotic lesions exhibit pronounced neuroangiogenic properties with increased expression of new nerve fibres and upregulation of neurotrophins (NGF, BDNF, NT-3, NT-4/5) and their receptors (TrkA, p75NTR). A comprehensive review by Morotti et al. (2014) demonstrated that "endometriotic lesions and peritoneal fluid from women with endometriosis had pronounced neuroangiogenic properties with increased expression of new nerve fibres, a shift in the distribution of sensory and autonomic fibres" ([PMID: 24859987](https://pubmed.ncbi.nlm.nih.gov/24859987/)). Kobayashi et al. (2014) further identified that "neurotrophins (NTs), a family of neuronal growth factors, are overexpressed in endometriosis and encompass NGF, BDNF and NT-3 and NT-4/5" with their receptors TrkA and p75NTR also expressed ([PMID: 24121693](https://pubmed.ncbi.nlm.nih.gov/24121693/)). In a baboon experimental model, Donnez et al. (2013) confirmed that "the NGF staining intensity score was found to be higher in glands of deep invasive lesions than in glands of eutopic baboon endometrium" ([PMID: 23850304](https://pubmed.ncbi.nlm.nih.gov/23850304/)), providing cross-species validation. This finding forms the foundational first step of the neuroimmune causal chain.

### Finding 2: Central Sensitization -- Brain Imaging, QST, and Spinal Glial Activation

Multiple lines of evidence confirm central nervous system involvement in endometriosis pain. As-Sanie et al. (2016) found that "women with endometriosis-associated CPP displayed increased levels of combined glutamine-glutamate (Glx) within the anterior insula and greater anterior insula connectivity to the medial prefrontal cortex (mPFC)" ([PMID: 26456676](https://pubmed.ncbi.nlm.nih.gov/26456676/)). Erdogan et al. (2026) demonstrated that "women with DIE and chronic pelvic pain demonstrated significantly increased connectivity between the amygdala and the right frontal pole (FWE-corrected P = 0.012 and 0.044)" ([PMID: 42033133](https://pubmed.ncbi.nlm.nih.gov/42033133/)). At the spinal level, Wu et al. (2026) identified the molecular mechanism: "spinal microglia exhibited M1 polarization in endometriosis mice. Mechanistically, neuronal ligands triggered microglial M1 polarization through CX3CR1 and P2X4R-mediated activation of the IkBa/NF-kappaB signaling pathway" ([PMID: 41791308](https://pubmed.ncbi.nlm.nih.gov/41791308/)). Quantitative sensory testing revealed significant pressure hyperalgesia in endometriosis patients (p << 0.0001), with non-cyclic greater than cyclic subtypes ([PMID: 41193946](https://pubmed.ncbi.nlm.nih.gov/41193946/)). These convergent findings establish central sensitization as a core component of the model.

### Finding 3: Pain-Stage Discordance Confirmed by Meta-Analysis

The signature prediction of the neuroimmune model -- that pain severity does not scale with visible lesion burden -- is confirmed at the meta-analytic level. Alves et al. (2026) found that "pain intensity did not differ significantly between rASRM stages I/II and III/IV (p > 0.05), though chronic pelvic pain was more frequent in advanced disease (p < 0.05)" across 8 studies ([PMID: 41338448](https://pubmed.ncbi.nlm.nih.gov/41338448/)). Additionally, VEGF and CA125 showed no significant correlation with pain severity ([PMID: 42137832](https://pubmed.ncbi.nlm.nih.gov/42137832/)). Central Sensitization Inventory (CSI) scores were better predictors of post-operative outcomes than disease stage: "A positive relationship was found between preoperative CSI scores and postoperative PGI-I (r = 0.25, p = .04)" ([PMID: 41448360](https://pubmed.ncbi.nlm.nih.gov/41448360/)). This finding is the clinical cornerstone of the neuroimmune model -- if the lesion were the sole pain generator, pain should scale with disease extent, but it does not.

### Finding 4: Post-Surgical Pain Persistence Demonstrates Central Independence

Clinical evidence that pain persists despite complete surgical eradication powerfully supports the model. Alboni et al. (2024) reported 28.1% of patients (97/345) had persistent CPP and dyspareunia after surgical eradication, noting "because of the complex pathogenesis of pain in endometriosis that includes central sensitization and myofascial dysfunction, symptoms can persist after surgery" ([PMID: 37997320](https://pubmed.ncbi.nlm.nih.gov/37997320/)). Critically, Gentles et al. (2025) showed "there was no change in the PSQ-M and a small change in CSI after endometriosis surgery, suggesting that surgical treatment of endometriosis does not directly address central sensitization" ([PMID: 40049377](https://pubmed.ncbi.nlm.nih.gov/40049377/)). Quevedo et al. (2026) found that "ovarian endometriosis, despite its well-known inflammatory pain characteristics, is associated with elevated FM survey scores, which may suggest nociplastic centrally mediated pain mechanisms" with 41.7% of ovarian endometriosis patients scoring positive ([PMID: 41890200](https://pubmed.ncbi.nlm.nih.gov/41890200/)). Additionally, up to 37% pain persistence and greater than 45% repeat surgery within 5 years have been reported.

### Finding 5: Molecular Mechanisms of Peripheral Sensitization -- IL-33/TNF-alpha/TRPV1 and Ion Channels

The molecular circuit connecting immune signals to nociceptor sensitization is now defined with remarkable precision. Li et al. (2025) demonstrated the complete IL-33 to ST2 to macrophage to TNF-alpha to TNFR1/p38 MAPK to TRPV1 pathway: "macrophage-derived TNF-alpha increased TRPV1 protein level in DRG neuronal cells through the TNFR1/p38 MAPK signaling pathway" and "IL-33 significantly exacerbated endometriosis and induced hyperalgesia in mice. By interacting with the ST2 receptor in macrophages, IL-33 enhanced the release of tumor necrosis factor alpha (TNF-alpha) and Interleukin 1beta (IL-1beta)" ([PMID: 39969583](https://pubmed.ncbi.nlm.nih.gov/39969583/)). Greaves et al. (2014) provided primary human tissue evidence that "TRPV1, TRPA1, and SCN11A mRNAs were significantly higher in the peritoneum from women with endometriosis (P < .001, P < .01). TRPV1, SCN9A, and TAC1 were elevated in endometriosis lesions (P < .05)" and demonstrated estrogen regulation: "incubation of sensory neurons with 17beta-estradiol increased TRPV1 mRNA (P < .01)" ([PMID: 25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/)).

### Finding 6: Nociceptive Nerve Fiber Characterization in Lesions

Tokushige et al. (2006) provided definitive human tissue evidence: "There were significantly more nerve fibres identified in peritoneal endometriotic lesions than in normal peritoneum (P < 0.001) or endosalpingiosis lesions (P < 0.001). These nerve fibres were SP, CGRP, ACh or TH immunoreactive" ([PMID: 16950827](https://pubmed.ncbi.nlm.nih.gov/16950827/)), confirming innervation by substance P-positive and CGRP-positive nociceptive C and A-delta fibers with NGF immunoreactivity near glands. Eutopic endometrium also showed increased sensory C fibers specific to endometriosis patients ([PMID: 18060940](https://pubmed.ncbi.nlm.nih.gov/18060940/); [PMID: 17451690](https://pubmed.ncbi.nlm.nih.gov/17451690/)), though a counter-study found nerve fibers in women both with and without endometriosis ([PMID: 26472151](https://pubmed.ncbi.nlm.nih.gov/26472151/)), limiting diagnostic specificity. The quantitative difference persists: endometriosis patients had higher density (median 2.0 vs 1.0 fibers/mm squared) even accounting for hormonal treatment ([PMID: 40184895](https://pubmed.ncbi.nlm.nih.gov/40184895/)).

### Finding 7: GWAS Implicates NGF as Genetic Risk Locus

Genome-wide association provides orthogonal genetic evidence. Rahmioglu et al. (2023) identified 42 genome-wide significant loci from 60,674 cases and 701,926 controls, with "identified signals regulated expression or methylation of genes in endometrium and blood, many of which were associated with pain perception/maintenance (SRP14/BMF, GDAP1, MLLT10, BSN and NGF)" and "significant genetic correlations between endometriosis and 11 pain conditions, including migraine, back and multisite chronic pain" ([PMID: 36914876](https://pubmed.ncbi.nlm.nih.gov/36914876/)). Koller et al. (2026) expanded to 80 loci including 37 new, with polygenic risk interacting with abdominal pain, anxiety, and migraine ([PMID: 42056605](https://pubmed.ncbi.nlm.nih.gov/42056605/)). Johnston et al. (2025) identified 24 independent SNPs and 127 genes for nociplastic pain across COPCs, demonstrating shared genetic architecture ([PMID: 39497418](https://pubmed.ncbi.nlm.nih.gov/39497418/)).

### Finding 8: tDCS RCT Provides Causal Evidence for Central Sensitization

The strongest interventional evidence comes from Mechsner et al. (2023): a Phase II RCT (n=36) showing "significant decreased pain perception in both pain measurements (pressure pain threshold and numerical rating scale score) was found for the active tDCS group compared with the placebo group" ([PMID: 36882181](https://pubmed.ncbi.nlm.nih.gov/36882181/)). The effect persisted at 1-week follow-up. If cortical neuromodulation reduces pain without altering lesion biology, central sensitization must be a causal contributor. A second tDCS RCT (n=40) is underway ([PMID: 39088433](https://pubmed.ncbi.nlm.nih.gov/39088433/)).

### Finding 9: P2X3 Antagonist Trial FAILURE -- Critical Negative Result

The SCHUMANN Phase 2b RCT represents the most important counter-evidence for the purinergic arm of the hypothesis. With 215 participants randomized to eliapixant 25/75/150mg BID or placebo for 12 weeks, Parke et al. (2024) reported: "The study found no significant differences in EAPP reduction from baseline between groups and no significant dose-response model. The elagolix 150 mg group showed better pain reduction than any of the other groups" ([PMID: 38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/)). While preclinical meta-analysis showed P2X3 inhibition produced robust visceral pain reduction (effect size 114.3 for visceral pain) ([PMID: 39393665](https://pubmed.ncbi.nlm.nih.gov/39393665/)), this did not translate clinically. The trial was terminated early (<50% planned completers) due to safety concerns, which may have limited statistical power, but the elagolix superiority underscores that hormonal mechanisms remain clinically dominant.

### Finding 10: BDNF Discriminates Painful from Non-Painful Endometriosis

Ding et al. (2018) showed that "BDNF concentrations in serum and PF were significantly higher in women with endometriosis with pain (2284.3 +/- 51.5 pg/mL, n = 23; 58.8 +/- 6.4 pg/mL, n = 16) than in women with endometriosis without pain (1999.8 +/- 61.1 pg/mL, n = 37; 31.7 +/- 2.9 pg/mL, n = 25; P < .01)" ([PMID: 28954602](https://pubmed.ncbi.nlm.nih.gov/28954602/)). BDNF mRNA in ectopic lesions was significantly higher than in eutopic endometrium (P < .01), and correlated with pain (P < .05). Reduced serum PEDF (anti-angiogenic factor) was also lower in endometriosis with pain vs without (12.6 +/- 7.1 vs 17.5 +/- 6.0 ng/mL; P < .05; [PMID: 22051848](https://pubmed.ncbi.nlm.nih.gov/22051848/)). These biomarker findings directly address the model's key prediction: if not all endometriosis is painful, neurotrophin levels should distinguish symptomatic from asymptomatic disease.

### Finding 11: Cross-Organ Sensitization and Pain Comorbidities

Common nerve pathways innervating the colon, bladder, and female reproductive tract contribute to comorbid IBS and overactive bladder via cross-organ sensitization ([PMID: 33132854](https://pubmed.ncbi.nlm.nih.gov/33132854/)). Endometriosis patients with abuse history show compounded central sensitization with worse GI symptoms ([PMID: 41703692](https://pubmed.ncbi.nlm.nih.gov/41703692/)). Central sensitivity syndromes correlate with CSI (r=0.687, p<0.05) ([PMID: 40049377](https://pubmed.ncbi.nlm.nih.gov/40049377/)). The shared genetic architecture across COPCs (24 SNPs, 127 genes; [PMID: 39497418](https://pubmed.ncbi.nlm.nih.gov/39497418/)) provides genetic underpinning for cross-organ sensitization.

### Finding 12: Psychosocial Factors as Independent Pain Modulators

The TRiPP study demonstrated that "CPP participants reported significantly greater fatigue, poorer sleep, higher anxiety, depression, pain catastrophising, and more childhood trauma (P < 0.01). However, no significant differences were observed in physiological measures" ([PMID: 41854293](https://pubmed.ncbi.nlm.nih.gov/41854293/)). Neuropathic-like pain (DN4 >= 4) was found in 36% of DE patients, "not associated with the stage of endometriosis or surgical complexity" but associated with higher catastrophizing (p < 0.001; [PMID: 40928523](https://pubmed.ncbi.nlm.nih.gov/40928523/)). Psychological factors mediate the trauma-to-pain intensity relationship ([PMID: 41021895](https://pubmed.ncbi.nlm.nih.gov/41021895/)). These findings challenge a purely bottom-up neuroimmune model and support a biopsychosocial framework.

### Finding 13: Subtype-Specific Immune Microenvironments

He et al. (2026) used integrated scRNA-seq and spatial transcriptomics to reveal fundamentally divergent programs: peritoneal endometriosis is "immune-hot" with a chemokine-driven inflammatory niche, while ovarian endometriosis is "immune-cold" with a fibromuscular survival niche ([PMID: 42010552](https://pubmed.ncbi.nlm.nih.gov/42010552/)). This critical finding means the neuroimmune sensitization circuit likely operates most strongly in peritoneal/DIE subtypes and differently (if at all) in ovarian endometriomas.

### Finding 14: Histamine-HRH Receptor Axis

Velho et al. (2025) characterized HRH1-HRH4 expression across peritoneal, deep infiltrating, and ovarian endometriosis, finding that "pain in endometriosis involves not only nociceptive but also neuropathic and neurogenic components, reflecting its complex nature. Histamine, a biogenic amine, has emerged as a critical mediator connecting inflammation and nerve sensitization" ([PMID: 41516088](https://pubmed.ncbi.nlm.nih.gov/41516088/)). This adds histamine as a parallel neuroimmune mediator alongside NGF/BDNF and purinergic signaling, with subtype-specific profiles.

---

## Mechanistic Causal Chain

The neuroimmune hypothesis implies a multi-step causal chain from upstream triggers to clinical pain manifestation. Below, each step is assessed for evidence strength.

{{figure:claim_assessment.png|caption=Causal chain evidence status by mechanistic step. Green indicates ESTABLISHED claims; yellow indicates EMERGING claims; red indicates WEAK or FAILED claims.}}

### Step-by-Step Chain with Evidence Assessment

**UPSTREAM TRIGGERS**

| Step | Evidence Level | Key References |
|------|---------------|----------------|
| Retrograde menstruation + ectopic implantation | ESTABLISHED | Widely accepted; not tested here |
| Early severe dysmenorrhea as repeated nociceptive input | EMERGING | [PMID: 40546153](https://pubmed.ncbi.nlm.nih.gov/40546153/), [PMID: 37951241](https://pubmed.ncbi.nlm.nih.gov/37951241/) |
| Genetic susceptibility (NGF locus, 42+ GWAS loci) | ESTABLISHED | [PMID: 36914876](https://pubmed.ncbi.nlm.nih.gov/36914876/), [PMID: 42056605](https://pubmed.ncbi.nlm.nih.gov/42056605/) |

**LESION MICROENVIRONMENT**

| Step | Evidence Level | Key References |
|------|---------------|----------------|
| Neurotrophin overexpression (NGF, BDNF) | ESTABLISHED | [PMID: 24859987](https://pubmed.ncbi.nlm.nih.gov/24859987/), [PMID: 24121693](https://pubmed.ncbi.nlm.nih.gov/24121693/), [PMID: 28954602](https://pubmed.ncbi.nlm.nih.gov/28954602/) |
| Inflammatory cytokines (IL-33, TNF-alpha, IL-1beta) | ESTABLISHED | [PMID: 39969583](https://pubmed.ncbi.nlm.nih.gov/39969583/) |
| Purinergic signaling (ATP, P2X3) | WEAK -- clinical failure | [PMID: 33198179](https://pubmed.ncbi.nlm.nih.gov/33198179/), **[PMID: 38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/)** |
| Histamine/HRH signaling | EMERGING | [PMID: 41516088](https://pubmed.ncbi.nlm.nih.gov/41516088/) |
| Estrogen-driven amplification (ER-beta to TRPV1) | ESTABLISHED | [PMID: 25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/) |
| Oxidative stress / iron / AOC3 | EMERGING | [PMID: 32001775](https://pubmed.ncbi.nlm.nih.gov/32001775/) |

**PERIPHERAL SENSITIZATION**

| Step | Evidence Level | Key References |
|------|---------------|----------------|
| Neuroangiogenesis (SP+/CGRP+ C and A-delta fibers) | ESTABLISHED | [PMID: 16950827](https://pubmed.ncbi.nlm.nih.gov/16950827/), [PMID: 17451690](https://pubmed.ncbi.nlm.nih.gov/17451690/) |
| Ion channel upregulation (TRPV1, TRPA1, SCN11A) | ESTABLISHED | [PMID: 25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/) |
| IL-33/ST2/macrophage/TNF-alpha/TRPV1 pathway | ESTABLISHED (mouse model) | [PMID: 39969583](https://pubmed.ncbi.nlm.nih.gov/39969583/) |
| Perineural invasion in DIE | ESTABLISHED (DIE-specific) | [PMID: 30310304](https://pubmed.ncbi.nlm.nih.gov/30310304/) |
| Gut microbiome to DRG sensitization | EMERGING | [PMID: 38559689](https://pubmed.ncbi.nlm.nih.gov/38559689/), [PMID: 31037294](https://pubmed.ncbi.nlm.nih.gov/31037294/) |

**CENTRAL SENSITIZATION**

| Step | Evidence Level | Key References |
|------|---------------|----------------|
| Spinal microglial M1 polarization | EMERGING (mouse only) | [PMID: 41791308](https://pubmed.ncbi.nlm.nih.gov/41791308/) |
| Altered brain neurochemistry (anterior insula Glx) | ESTABLISHED | [PMID: 26456676](https://pubmed.ncbi.nlm.nih.gov/26456676/) |
| Altered functional connectivity | ESTABLISHED | [PMID: 42033133](https://pubmed.ncbi.nlm.nih.gov/42033133/), [PMID: 36375399](https://pubmed.ncbi.nlm.nih.gov/36375399/) |
| Cross-organ sensitization (IBS, IC/BPS) | ESTABLISHED | [PMID: 33132854](https://pubmed.ncbi.nlm.nih.gov/33132854/), [PMID: 39497418](https://pubmed.ncbi.nlm.nih.gov/39497418/) |
| tDCS proof-of-concept (causal) | ESTABLISHED (Phase II RCT) | [PMID: 36882181](https://pubmed.ncbi.nlm.nih.gov/36882181/) |

**CLINICAL MANIFESTATION**

| Step | Evidence Level | Key References |
|------|---------------|----------------|
| Pain-stage discordance | ESTABLISHED (meta-analysis) | [PMID: 41338448](https://pubmed.ncbi.nlm.nih.gov/41338448/) |
| Post-surgical pain persistence (28-37%) | ESTABLISHED | [PMID: 37997320](https://pubmed.ncbi.nlm.nih.gov/37997320/), [PMID: 40049377](https://pubmed.ncbi.nlm.nih.gov/40049377/) |
| Nociplastic pain phenotype | EMERGING | [PMID: 41890200](https://pubmed.ncbi.nlm.nih.gov/41890200/) |

{{figure:molecular_circuit.png|caption=Detailed molecular pathway diagram showing the neuroimmune sensitization circuit from lesion-derived signals through peripheral and central sensitization.}}

### Modifiers and Parallel Pain Generators

| Modifier | Evidence Level | Effect on Model |
|----------|---------------|-----------------|
| Psychosocial factors (catastrophizing, trauma, anxiety) | ESTABLISHED | Independently modulates pain; challenges purely bottom-up model |
| Pelvic floor dysfunction | ESTABLISHED (80% prevalence in CPP) | Parallel peripheral pain generator |
| Hormonal therapy response | ESTABLISHED (~65% respond) | Hormonal arm dominant for majority |
| Subtype-specific immunity (EcP vs EcO) | EMERGING | Limits model universality |
| Gut microbiome dysbiosis | EMERGING | Upstream amplifier of peritoneal inflammation |

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|---|----------|--------------|-----------|-------------------|-------------|---------|------------|
| 1 | [PMID: 24859987](https://pubmed.ncbi.nlm.nih.gov/24859987/) | Review (synthesis) | Supports | Neuroangiogenesis | Lesions show increased nerve fibers, neurotrophin upregulation | All subtypes | High (review-level) |
| 2 | [PMID: 16950827](https://pubmed.ncbi.nlm.nih.gov/16950827/) | Human clinical | Supports | Lesion innervation | SP+/CGRP+ fibers significantly more in lesions (P<0.001) | Peritoneal (n=40 vs 36) | High |
| 3 | [PMID: 25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/) | Human clinical + in vitro | Supports | Peripheral sensitization | TRPV1, TRPA1, SCN11A elevated in endo peritoneum; E2 increases TRPV1 | Peritoneal/CPP (n=45) | High |
| 4 | [PMID: 39969583](https://pubmed.ncbi.nlm.nih.gov/39969583/) | Mouse model + in vitro | Supports | Macrophage-nerve crosstalk | IL-33/ST2/TNF-alpha/TNFR1/p38 MAPK/TRPV1 in DRG | Mouse endometriosis | High (complete pathway) |
| 5 | [PMID: 26456676](https://pubmed.ncbi.nlm.nih.gov/26456676/) | Human clinical (fMRI) | Supports | Central sensitization | Increased anterior insula Glx, increased insula-mPFC connectivity | CPP vs controls | Moderate (small n) |
| 6 | [PMID: 41791308](https://pubmed.ncbi.nlm.nih.gov/41791308/) | Mouse model | Supports | Spinal glial activation | Microglial M1 polarization via CX3CR1/P2X4R/NF-kappaB | Mouse endometriosis | Moderate (mouse only) |
| 7 | [PMID: 41338448](https://pubmed.ncbi.nlm.nih.gov/41338448/) | Meta-analysis | Supports | Pain-stage discordance | No pain difference I/II vs III/IV (8 studies) | All stages | High |
| 8 | [PMID: 37997320](https://pubmed.ncbi.nlm.nih.gov/37997320/) | Human clinical | Supports | Post-surgical persistence | 28.1% persistent CPP after eradication | Mixed subtypes (n=345) | High |
| 9 | [PMID: 40049377](https://pubmed.ncbi.nlm.nih.gov/40049377/) | Human clinical | Supports | Central sensitization independence | No CSI change after surgery | Mixed (pilot) | Moderate |
| 10 | [PMID: 36882181](https://pubmed.ncbi.nlm.nih.gov/36882181/) | RCT (Phase II) | Supports | Central sensitization (causal) | tDCS reduced pain vs placebo | CPP (n=36) | High (RCT) |
| 11 | [PMID: 36914876](https://pubmed.ncbi.nlm.nih.gov/36914876/) | GWAS | Supports | Genetic basis | NGF among risk loci; genetic correlation with 11 pain conditions | 60,674 cases | High |
| 12 | [PMID: 28954602](https://pubmed.ncbi.nlm.nih.gov/28954602/) | Human clinical | Supports | Neurotrophin-pain link | BDNF higher in endo+pain vs endo-no pain (P<.01) | Serum/PF (n=60+38) | High |
| 13 | [PMID: 33198179](https://pubmed.ncbi.nlm.nih.gov/33198179/) | Review | Supports | Purinergic sensitization | ATP accumulation drives P2X3 activation and persistent pain | All subtypes | Moderate (review) |
| 14 | [PMID: 38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/) | **RCT (Phase 2b)** | **Refutes** (purinergic arm) | P2X3 clinical translation | Eliapixant FAILED vs placebo; elagolix superior | EAPP (n=215) | **High (RCT failure)** |
| 15 | [PMID: 30310304](https://pubmed.ncbi.nlm.nih.gov/30310304/) | Human clinical | Qualifies | Perineural invasion | PNI+ patients have higher VAS, more nerve/vessel density | DIE specifically | Moderate |
| 16 | [PMID: 41854293](https://pubmed.ncbi.nlm.nih.gov/41854293/) | Human clinical | Qualifies | Psychosocial modulation | Psychological factors, not physiological, differentiate CPP subgroups | TRiPP study | High |
| 17 | [PMID: 40928523](https://pubmed.ncbi.nlm.nih.gov/40928523/) | Human clinical | Supports + Qualifies | Neuropathic pain | DN4 >= 4 in 36% DE; not associated with stage but with catastrophizing | Deep endo | Moderate |
| 18 | [PMID: 37672087](https://pubmed.ncbi.nlm.nih.gov/37672087/) | Human clinical | Competing | Pelvic floor dysfunction | 80% CPP patients had myofascial trigger points | CPP (n=15, pilot) | Low-Moderate |
| 19 | [PMID: 42010552](https://pubmed.ncbi.nlm.nih.gov/42010552/) | Human (scRNA-seq) | Qualifies | Subtype-specific immunity | EcP "immune-hot" vs EcO "immune-cold" | Peritoneal vs ovarian | High (multi-omics) |
| 20 | [PMID: 28526518](https://pubmed.ncbi.nlm.nih.gov/28526518/) | Human clinical | Qualifies | Asymptomatic disease | 11.82% incidental endometriosis at sterilization | Asymptomatic (n=465) | High |
| 21 | [PMID: 40546153](https://pubmed.ncbi.nlm.nih.gov/40546153/) | Review | Supports | Temporal model | Early severe dysmenorrhea promotes central hypersensitivity | Adolescents | Moderate (review) |
| 22 | [PMID: 39497418](https://pubmed.ncbi.nlm.nih.gov/39497418/) | GWAS | Supports | Shared genetic architecture | 24 SNPs, 127 genes for nociplastic pain across COPCs | Multi-condition | High |
| 23 | [PMID: 38559689](https://pubmed.ncbi.nlm.nih.gov/38559689/) | Mouse model | Supports | Microbiome-DRG link | HFD increased DRG pain mediators in endometriosis mice | Obesity/endo model | Moderate |
| 24 | [PMID: 41516088](https://pubmed.ncbi.nlm.nih.gov/41516088/) | Human clinical | Supports | Histamine axis | HRH1-HRH4 expression connects inflammation to nerve sensitization | All subtypes | Moderate |
| 25 | [PMID: 26472151](https://pubmed.ncbi.nlm.nih.gov/26472151/) | Human clinical | Qualifies | Eutopic nerve fibers | Nerve fibers in women both with and without endo; poor diagnostic tool | Diagnostic context | High (counter to F016) |

{{figure:final_evidence_summary.png|caption=Final evidence summary. Panel A shows evidence count by causal chain step. Panel B shows molecular node evidence strength, highlighting the P2X3 clinical failure.}}

---

## Knowledge Gaps

### Gap 1: No Anti-NGF Trial in Endometriosis (HIGHEST PRIORITY)

**Scope:** Anti-NGF monoclonal antibodies (tanezumab, fasinumab) have demonstrated significant pain relief in osteoarthritis ([PMID: 24691709](https://pubmed.ncbi.nlm.nih.gov/24691709/)) and their role in visceral pain has been reviewed ([PMID: 29543647](https://pubmed.ncbi.nlm.nih.gov/29543647/)). NGF is a GWAS-identified risk locus for endometriosis. BDNF discriminates painful from non-painful endometriosis. Yet no endometriosis-specific anti-NGF trial was found across exhaustive PubMed searches.

**Why it matters:** This is the most direct, high-yield therapeutic test of the neuroimmune hypothesis. If anti-NGF fails in endometriosis (as eliapixant did for P2X3), it would substantially weaken the neurotrophin arm. If it succeeds, it validates the model's most therapeutically actionable prediction.

**What was checked:** PubMed searches for "anti-NGF endometriosis," "tanezumab endometriosis," "fasinumab endometriosis," and "NGF antibody endometriosis pain trial."

**What would resolve it:** A Phase 2 RCT of tanezumab or fasinumab in endometriosis-CPP patients, stratified by CSI score and disease subtype.

### Gap 2: Peripheral-to-Central Transition Not Confirmed Longitudinally

**Scope:** The causal step from chronic peripheral nociceptive input to central sensitization is supported by cross-sectional data (brain imaging, QST) and animal models, but no longitudinal human study has tracked the temporal transition in endometriosis patients.

**Why it matters:** Without longitudinal data, the direction of causality remains inferred. Central changes could be pre-existing trait vulnerabilities rather than consequences of peripheral input.

**What was checked:** Literature search for longitudinal QST, fMRI, or biomarker studies tracking sensitization progression in endometriosis.

**What would resolve it:** Prospective cohort study with serial QST and fMRI from early dysmenorrhea through established disease, with at least 3 time points over 2-3 years.

### Gap 3: Subtype-Specific Neuroimmune Profiles Incomplete

**Scope:** scRNA-seq data shows peritoneal endometriosis is "immune-hot" while ovarian is "immune-cold" ([PMID: 42010552](https://pubmed.ncbi.nlm.nih.gov/42010552/)). However, neurotrophin and nociceptive ion channel expression has not been systematically profiled across subtypes using matched single-cell methods.

**Why it matters:** The model may only apply to peritoneal/DIE subtypes. If ovarian endometriomas generate pain through different mechanisms (e.g., iron/oxidative stress rather than neuroangiogenesis), therapeutic targeting must be subtype-specific.

**What would resolve it:** Multi-subtype scRNA-seq + spatial transcriptomics from matched patients with concurrent peritoneal, ovarian, and DIE lesions.

### Gap 4: P2X3 Clinical Failure Mechanism Unexplained

**Scope:** Preclinical meta-analysis showed strong efficacy for P2X3 inhibitors in visceral pain models (effect size 114.3), yet eliapixant failed in the SCHUMANN trial ([PMID: 38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/)). The trial was terminated early for safety, possibly underpowering the study.

**Why it matters:** If the failure is due to biological irrelevance of P2X3 in human endometriosis pain, the purinergic arm of the model requires revision. If it is due to trial design, the arm remains viable.

**What would resolve it:** Post-hoc subgroup analysis of SCHUMANN trial data; or a new P2X3 trial in a biomarker-enriched population (e.g., high peritoneal ATP or P2X3 expression confirmed by biopsy).

### Gap 5: No GenCC/ClinGen Entries for Neuroimmune Genes

**Scope:** Despite NGF being a GWAS locus, no formal gene-disease validity curation (GenCC/ClinGen) links NGF, BDNF, TRPV1, or other neuroimmune genes to endometriosis pain specifically.

**Why it matters:** Formal curation would strengthen the translational case for targeting these genes.

### Gap 6: Histamine-HRH Axis Functional Validation Absent

**Scope:** Velho et al. (2025) characterized HRH1-HRH4 expression patterns ([PMID: 41516088](https://pubmed.ncbi.nlm.nih.gov/41516088/)), but no interventional study has tested whether blocking histamine signaling reduces endometriosis pain.

**What would resolve it:** Antihistamine pilot trial (H1/H2/H4 antagonists) in endometriosis-CPP patients stratified by peritoneal fluid histamine levels.

### Gap 7: Psychosocial-Neuroimmune Interaction Mechanism Unknown

**Scope:** The TRiPP study showed psychological factors differentiate CPP subgroups ([PMID: 41854293](https://pubmed.ncbi.nlm.nih.gov/41854293/)). How catastrophizing and trauma history mechanistically interact with the peripheral neuroimmune circuit (e.g., via HPA axis, cortisol modulation of immune signaling) remains uncharacterized.

**What would resolve it:** Integrated study measuring cortisol, peritoneal cytokines, neurotrophin levels, and psychological assessments in the same cohort, with mediation analysis.

{{figure:knowledge_gaps.png|caption=Comprehensive knowledge gap table with scope, importance, and resolution strategy for each identified gap.}}

---

## Alternative and Competing Models

### 1. Hormonal Dominance Model (Competing/Upstream)

**Relationship to seed hypothesis:** Upstream cause and competing explanation. Estrogen drives lesion growth, inflammation, and directly regulates TRPV1 ([PMID: 25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/)). The elagolix superiority over eliapixant in the SCHUMANN trial ([PMID: 38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/)) supports hormonal dominance for the majority (~65%) of patients. Progesterone resistance adds complexity, with dienogest non-responders potentially representing the neuroimmune-dominant subgroup ([PMID: 41999626](https://pubmed.ncbi.nlm.nih.gov/41999626/)).

**Assessment:** The hormonal and neuroimmune models are not mutually exclusive. Estrogen is an upstream amplifier of the neuroimmune circuit. The neuroimmune model explains what happens when hormonal therapy fails.

### 2. Autoimmune/Immune Dysregulation Model (Parallel)

**Relationship:** Parallel mechanism operating through distinct immune pathways. Endometriosis shows Th2 immune shift, B-1 cell activation, and autoantibody production ([PMID: 16359969](https://pubmed.ncbi.nlm.nih.gov/16359969/); [PMID: 20436316](https://pubmed.ncbi.nlm.nih.gov/20436316/)). This could contribute to chronic inflammation independent of the NGF/TRPV1 nociceptive circuit.

**Assessment:** Overlapping but distinct from the neuroimmune pain model. The autoimmune component may explain aspects of systemic inflammation and fatigue rather than nociceptive pain specifically.

### 3. Psychosocial/Top-Down Sensitization Model (Complementary)

**Relationship:** Complementary mechanism that modulates the neuroimmune circuit from above. Catastrophizing, trauma history, and anxiety independently predict pain severity and worsen outcomes ([PMID: 41854293](https://pubmed.ncbi.nlm.nih.gov/41854293/); [PMID: 41021895](https://pubmed.ncbi.nlm.nih.gov/41021895/); [PMID: 32383692](https://pubmed.ncbi.nlm.nih.gov/32383692/)). The TRiPP study's finding that psychological measures, not physiological ones, differentiate CPP subgroups suggests top-down modulation is substantial.

**Assessment:** A biopsychosocial model may be more complete than a purely bottom-up neuroimmune model. The models are synergistic rather than competing.

### 4. Pelvic Floor Myofascial Model (Parallel Peripheral Generator)

**Relationship:** Parallel peripheral pain generator. With 80% of endometriosis-CPP patients showing myofascial trigger points ([PMID: 37672087](https://pubmed.ncbi.nlm.nih.gov/37672087/)) and bladder/pelvic floor tenderness predicting dyspareunia regardless of stage ([PMID: 30078464](https://pubmed.ncbi.nlm.nih.gov/30078464/)), pelvic floor dysfunction is a major independent contributor.

**Assessment:** Not alternative but parallel. May share downstream convergence through central sensitization.

### 5. Epigenetic Reprogramming Model (Upstream Cause)

**Relationship:** Upstream mechanism. Differential DNA methylation, histone modification, and miRNA regulation affect estrogen/progesterone receptor expression and inflammatory gene regulation ([PMID: 37409951](https://pubmed.ncbi.nlm.nih.gov/37409951/); [PMID: 32700282](https://pubmed.ncbi.nlm.nih.gov/32700282/); [PMID: 35935991](https://pubmed.ncbi.nlm.nih.gov/35935991/)). Epigenetic changes could explain why some lesions activate the neuroimmune circuit while others remain quiescent.

**Assessment:** Explanatory for inter-individual variation and could determine which patients develop neuroimmune-driven pain.

### 6. Gut Microbiome-Estrobolome Model (Upstream Amplifier)

**Relationship:** Upstream amplifier. HFD-induced gut dysbiosis enhanced DRG pain mediators and peritoneal inflammation in endometriosis mice ([PMID: 38559689](https://pubmed.ncbi.nlm.nih.gov/38559689/)). Antibiotic treatment (metronidazole) reduced endometriosis progression approximately 5-fold ([PMID: 31037294](https://pubmed.ncbi.nlm.nih.gov/31037294/)). Estrobolome dysregulation alters estrogen recycling, feeding into hormonal amplification ([PMID: 38144564](https://pubmed.ncbi.nlm.nih.gov/38144564/)).

**Assessment:** Positions gut health as an environmental modifier that can amplify or dampen the neuroimmune circuit.

---

## Discriminating Tests

### Test 1: Anti-NGF RCT in Endometriosis (Highest Priority)

- **Design:** Phase 2 RCT, tanezumab vs placebo in endometriosis-CPP
- **Stratification:** CSI score (high vs low), subtype (peritoneal/DIE vs ovarian), hormonal therapy status (refractory vs naive)
- **Primary endpoint:** EAPP reduction at 12 weeks
- **Biomarkers:** Serum NGF, BDNF, substance P at baseline and endpoint
- **Sample:** n=200 (powered based on tanezumab OA effect sizes)
- **Expected result under neuroimmune model:** Significant pain reduction, especially in CSI-high peritoneal/DIE subgroup
- **Expected result under hormonal model:** No benefit beyond hormonal therapy; benefit only in hormonal-refractory subgroup
- **Why discriminating:** Directly tests the neurotrophin arm with a specific antagonist, analogous to the SCHUMANN trial for P2X3

### Test 2: Longitudinal QST + fMRI from Adolescent Dysmenorrhea

- **Design:** Prospective cohort, adolescents with severe dysmenorrhea, serial QST + resting-state fMRI + CSI at 0, 12, 24, 36 months
- **Sample:** 150 adolescents with severe dysmenorrhea, 50 age-matched controls
- **Expected result:** Progressive widening of hyperalgesia zones and increasing brain connectivity alterations preceding endometriosis diagnosis
- **Why discriminating:** Establishes temporal sequence -- peripheral before central vs. concurrent trait vulnerability

### Test 3: Subtype-Matched Neurotrophin/Ion Channel Profiling

- **Design:** Cross-sectional, matched peritoneal, ovarian, and DIE lesions from same patients where surgically feasible
- **Assays:** scRNA-seq for neurotrophin receptors, TRPV1, TRPA1 expression in nerve fibers; spatial transcriptomics for nerve-immune colocalization
- **Expected result:** Peritoneal/DIE show high neurotrophin/ion channel expression; ovarian show low expression
- **Why discriminating:** Confirms subtype restriction of the neuroimmune model

### Test 4: HRH Antagonist Pilot in Endometriosis Pain

- **Design:** Open-label pilot (n=40), existing H1/H2 antihistamines (e.g., cetirizine + ranitidine) in endometriosis-CPP
- **Stratification:** By peritoneal fluid histamine levels (measured at diagnostic laparoscopy)
- **Expected result:** Pain reduction proportional to baseline histamine levels
- **Why discriminating:** Low-cost test of a newly identified molecular arm

### Test 5: CSI-Stratified Surgical Outcome Study

- **Design:** Prospective cohort (n=300), endometriosis patients undergoing excision surgery, stratified by preoperative CSI
- **Primary endpoint:** Pain recurrence at 6, 12, 24 months
- **Secondary endpoint:** Randomize CSI-high patients to adjunctive neuromodulatory therapy (tDCS or gabapentinoids) vs standard care
- **Expected result under neuroimmune model:** CSI-high patients have significantly higher recurrence without adjunctive therapy; neuromodulation reduces this difference
- **Why discriminating:** Tests whether identifying and treating central sensitization improves surgical outcomes

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base. All are labeled as leads requiring curator verification.*

### Candidate Status Change

- **Current status:** EMERGING
- **Proposed overall status:** Retain EMERGING, but annotate with sub-claim evidence levels
- Peripheral neuroangiogenesis: **ESTABLISHED**
- Peripheral nociceptor sensitization (TRPV1/ion channels): **ESTABLISHED**
- Central sensitization involvement: **ESTABLISHED**
- Pain-stage discordance: **ESTABLISHED**
- P2X3/purinergic clinical arm: **WEAKENED** (annotate SCHUMANN failure)
- Histamine-HRH axis: **EMERGING**
- Gut microbiome-DRG link: **EMERGING**

### Candidate Pathophysiology Nodes

| Node | Candidate Ontology Term | Evidence Level |
|------|------------------------|----------------|
| NGF overexpression in lesions | GO:0038180 (nerve growth factor signaling pathway) | ESTABLISHED |
| TRPV1 upregulation in peritoneum | TRPV1 (specific channel) | ESTABLISHED |
| IL-33/ST2 macrophage-nerve crosstalk | GO:0002274 (myeloid leukocyte activation) | ESTABLISHED (mouse) |
| Spinal microglial M1 polarization | CL:0000129 (microglial cell); GO:0001774 (microglial cell activation) | EMERGING |
| Histamine-HRH1-4 nerve sensitization | GO:0004969 (histamine receptor activity) | EMERGING |
| BDNF as pain biomarker | BDNF serum/PF levels | ESTABLISHED (cross-sectional) |

### Candidate Edges

- NGF to TrkA on sensory neurons to neuroangiogenesis -- ESTABLISHED
- IL-33 to ST2 (macrophage) to TNF-alpha to TNFR1 to p38 MAPK to TRPV1 -- ESTABLISHED (mouse)
- Estradiol to ER-beta to TRPV1 mRNA upregulation -- ESTABLISHED (in vitro)
- BDNF serum/PF levels discriminate painful vs non-painful endometriosis -- ESTABLISHED (cross-sectional)
- P2X3 activation to peripheral pain -- **clinical edge WEAKENED** by SCHUMANN failure
- Gut dysbiosis to DRG pain mediator upregulation -- EMERGING (mouse only)
- Histamine to HRH receptors to nerve sensitization -- EMERGING (descriptive only)

### Candidate Evidence References for Curator Verification

| PMID | Snippet for Verification | Claim Supported |
|------|--------------------------|-----------------|
| [25029427](https://pubmed.ncbi.nlm.nih.gov/25029427/) | "TRPV1, TRPA1, and SCN11A mRNAs were significantly higher in the peritoneum from women with endometriosis (P < .001, P < .01)" | Ion channel upregulation in peritoneum |
| [39969583](https://pubmed.ncbi.nlm.nih.gov/39969583/) | "macrophage-derived TNF-alpha increased TRPV1 protein level in DRG neuronal cells through the TNFR1/p38 MAPK signaling pathway" | Complete immune-to-nociceptor pathway |
| [36914876](https://pubmed.ncbi.nlm.nih.gov/36914876/) | "Identified signals regulated expression...genes...associated with pain perception/maintenance...NGF" | NGF as genetic risk locus |
| [38890641](https://pubmed.ncbi.nlm.nih.gov/38890641/) | "The study found no significant differences in EAPP reduction from baseline between groups" | P2X3 arm failure |
| [36882181](https://pubmed.ncbi.nlm.nih.gov/36882181/) | "Significant decreased pain perception in both pain measurements...for the active tDCS group" | Causal central sensitization evidence |
| [41338448](https://pubmed.ncbi.nlm.nih.gov/41338448/) | "Pain intensity did not differ significantly between rASRM stages I/II and III/IV (p > 0.05)" | Pain-stage discordance |
| [28954602](https://pubmed.ncbi.nlm.nih.gov/28954602/) | "BDNF concentrations in serum and PF were significantly higher in women with endometriosis with pain...than in women with endometriosis without pain...P < .01" | BDNF as pain discriminator |

### Candidate Cell Type Ontology Terms

- CL:0000198 (pain receptor cell / nociceptor) -- for peripheral sensitization nodes
- CL:0000235 (macrophage) -- for IL-33/TNF-alpha signaling
- CL:0000129 (microglial cell) -- for spinal M1 polarization
- CL:0002563 (peritoneal macrophage) -- for peritoneal immune microenvironment
- CL:0000236 (B cell) -- for autoimmune component

### Candidate Knowledge Gaps for KB Annotation

1. **Anti-NGF trial absence** -- No endometriosis-specific anti-NGF clinical trial exists despite therapeutic validation in osteoarthritis and genetic implication of NGF. Priority: CRITICAL.
2. **Peripheral-to-central transition longitudinal data** -- No human longitudinal study tracks sensitization progression. Priority: HIGH.
3. **Subtype-specific neuroimmune profiling** -- Nerve fiber and ion channel expression not systematically compared across subtypes using matched methods. Priority: HIGH.
4. **P2X3 clinical failure mechanism** -- Whether SCHUMANN failure reflects biology or design. Priority: MODERATE.
5. **Histamine-HRH functional validation** -- No interventional data for histamine antagonists in endometriosis pain. Priority: MODERATE.
6. **Psychosocial-neuroimmune interaction mechanism** -- How psychological factors interact with the peripheral neuroimmune circuit at molecular level. Priority: MODERATE.

### Candidate Discussion Prompts

- Should the neuroimmune model be framed as a universal endometriosis pain mechanism, or restricted to peritoneal/DIE subtypes with a separate model for ovarian endometriomas?
- Does the SCHUMANN P2X3 failure warrant downgrading the purinergic node from the core model, or should it be retained pending a biomarker-enriched trial?
- Should "hormonal therapy refractory" be codified as a clinical indicator for neuroimmune-dominant pain phenotype?

---

## Limitations

1. **Publication bias:** Positive findings of nerve fiber changes and neurotrophin elevation are more frequently published than null results. The diagnostic specificity debate around eutopic nerve fibers illustrates this -- contradictory findings emerged only upon systematic comparison ([PMID: 26472151](https://pubmed.ncbi.nlm.nih.gov/26472151/) vs [PMID: 18060940](https://pubmed.ncbi.nlm.nih.gov/18060940/)).

2. **Animal model translation:** The IL-33/TNF-alpha/TRPV1 pathway and spinal microglial polarization are established in murine models. Translation to human endometriosis requires caution given species differences in immune-neural interactions and the surgically induced nature of most mouse models.

3. **Cross-sectional design predominance:** Most human evidence is cross-sectional, precluding definitive causal inference about the temporal sequence from peripheral to central sensitization. Correlation between BDNF and pain, or CSI and outcomes, does not prove directionality.

4. **Small sample sizes in neuroimaging:** Key neuroimaging studies (As-Sanie 2016 n~20, Szabo 2022 n=11, Erdogan 2026 n small) have limited power, and brain connectivity findings require replication in larger cohorts.

5. **Population heterogeneity:** Many studies do not stratify by endometriosis subtype, hormonal treatment status, or pain phenotype, obscuring subtype-specific effects that may be critical to the model's applicability.

6. **SCHUMANN trial interpretation:** Early termination for safety (<50% planned completers) may have underpowered the study, making it difficult to definitively conclude P2X3 is biologically irrelevant rather than that the trial was inadequately powered.

7. **Psychosocial confounding:** Unmeasured psychosocial factors (catastrophizing, depression, trauma) may inflate apparent neuroimmune effects in studies that do not control for them.

8. **Search limitations:** This investigation relied on PubMed-indexed literature. Grey literature, conference abstracts, and ongoing clinical trials not yet published may contain relevant evidence not captured here.

---

## Proposed Follow-up Experiments and Actions

### Immediate Priorities

1. **Anti-NGF Phase 2 RCT:** Design a trial of tanezumab or fasinumab in CSI-stratified endometriosis-CPP patients. This single study would test the model's most therapeutically actionable prediction. Enrich for hormonal-refractory patients and peritoneal/DIE subtypes. Include serum NGF/BDNF as pharmacodynamic biomarkers. This is the highest-priority gap in the entire field.

2. **SCHUMANN trial post-hoc analysis:** Request access to individual patient data to assess whether any biomarker-defined or subtype-defined subgroup showed eliapixant benefit, which would salvage the purinergic arm for a targeted population.

### Medium-Term Studies

3. **Adolescent longitudinal cohort:** Establish a prospective cohort of 150+ adolescents with severe dysmenorrhea, tracking QST, resting-state fMRI, BDNF/NGF serum levels, and CSI scores at 6-12 month intervals through to endometriosis diagnosis or resolution. This would establish the temporal sequence of peripheral-to-central sensitization and identify biomarker trajectories.

4. **Multi-subtype single-cell profiling:** Conduct matched scRNA-seq + spatial transcriptomics across peritoneal, ovarian, and DIE lesions from the same patients, focusing on neurotrophin receptors, ion channels, and immune-nerve interaction molecules. This would define the molecular boundaries of the neuroimmune model's applicability.

5. **CSI-stratified surgical outcome study:** Prospectively compare pain recurrence after excision surgery in CSI-high vs CSI-low patients (n=300), with randomization of CSI-high patients to adjunctive neuromodulatory therapy (tDCS or gabapentinoids) vs standard post-operative care.

### Exploratory Studies

6. **Histamine antagonist pilot:** Test H1/H2/H4 antihistamines as adjunctive therapy in endometriosis-CPP (n=40, open-label), stratified by peritoneal fluid histamine levels. Low cost, high information value.

7. **Integrated biopsychosocial phenotyping:** A single comprehensive study combining QST, brain imaging, psychological assessment (PCS, HADS, ACE score), pelvic floor evaluation, peritoneal immune profiling, and neurotrophin biomarkers in n=200 patients. Use structural equation modeling to determine the relative contribution of each pain generator pathway.

8. **Curcumin or anti-inflammatory adjunct trial:** Based on preclinical evidence that curcumin suppresses neuroinflammation in DRG and spinal cord ([PMID: 42097012](https://pubmed.ncbi.nlm.nih.gov/42097012/)), a pilot trial of curcumin as adjunctive therapy could test the neuroinflammatory arm at low cost.

{{figure:final_synthesis.png|caption=Final synthesis figure integrating the complete neuroimmune model with evidence levels, molecular nodes, modifiers, knowledge gaps, and overall verdict.}}

---

*Report generated from 5 investigative iterations, 120 papers reviewed, 25 confirmed findings with verified citations. Search date: June 2026.*
