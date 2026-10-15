---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T04:02:16.157259'
end_time: '2026-08-28T04:29:44.838594'
duration_seconds: 1648.68
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Opioid Use Disorder
  category: Psychiatric
  hypothesis_group_id: ibogaine_kappa_biased_agonism_model
  hypothesis_label: Noribogaine G-protein-biased kappa-opioid agonism model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: ibogaine_kappa_biased_agonism_model\nhypothesis_label:\
    \ Noribogaine G-protein-biased kappa-opioid agonism model\nstatus: EMERGING\n\
    description: 'Proposes that the anti-opioid action of ibogaine is carried principally\
    \ by noribogaine''s\n  G-protein-biased agonism at the kappa-opioid receptor,\
    \ with weak mu-opioid antagonism as a secondary\n  contributor. Bias away from\
    \ beta-arrestin recruitment is invoked to explain why the compound lacks the\n\
    \  dysphoria of conventional kappa agonists, and functional inhibition of dynorphin-driven\
    \ beta-arrestin\n  signalling is invoked to explain relief of the hyperkatifeia/anti-reward\
    \ state. The strongest support\n  is structural rather than loss-of-function:\
    \ iboga analogues engineered as potent kappa agonists retain\n  long-lasting suppression\
    \ of opioid intake and reverse opioid-induced hyperalgesia while shedding the\n\
    \  cardiac liability. That establishes kappa agonism as sufficient in rodents,\
    \ not that ibogaine itself\n  acts through kappa.'\nnotes: 'Distinguishing test:\
    \ a selective kappa antagonist, or a kappa-receptor knockout, should abolish\n\
    \  ibogaine''s suppression of opioid self-administration if this model holds.\
    \ Note also that the micromolar\n  affinities involved mean the model depends\
    \ on brain concentrations actually reached at therapeutic doses,\n  which is where\
    \ the CYP2D6-driven exposure variability becomes mechanistically relevant rather\
    \ than merely\n  a safety issue.'\nevidence:\n- reference: PMID:26302653\n  reference_title:\
    \ Noribogaine is a G-protein biased \u03BA-opioid receptor agonist.\n  supports:\
    \ SUPPORT\n  evidence_source: IN_VITRO\n  snippet: noribogaine was a G-protein\
    \ biased kappa agonist 75% as efficacious as dynorphin A at stimulating\n    GDP-GTP\
    \ exchange\n  explanation: Characterizes the biased kappa pharmacology the model\
    \ is built on.\n- reference: PMID:26302653\n  reference_title: Noribogaine is\
    \ a G-protein biased \u03BA-opioid receptor agonist.\n  supports: PARTIAL\n  evidence_source:\
    \ IN_VITRO\n  snippet: Noribogaine was a weak mu antagonist with a functional\
    \ inhibition constants (Ke) of 20 \u03BCM at\n    the G-protein and \u03B2-arrestin\
    \ signaling pathways\n  explanation: Constrains the mu contribution to weak antagonism,\
    \ which argues against withdrawal relief\n    being explained by opioid-agonist\
    \ substitution.\n- reference: PMID:7796150\n  reference_title: Radioligand-binding\
    \ study of noribogaine, a likely metabolite of ibogaine.\n  supports: SUPPORT\n\
    \  evidence_source: IN_VITRO\n  snippet: Noribogaine showed a higher affinity\
    \ than ibogaine for all of the opioid receptors\n  explanation: Supports assigning\
    \ the opioid-receptor component of the effect to the long-lived metabolite\n \
    \   rather than the parent drug.\n- reference: PMID:39304653\n  reference_title:\
    \ Oxa-Iboga alkaloids lack cardiac risk and disrupt opioid use in animal models.\n\
    \  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n  snippet: Oxa-noribogaine\
    \ induces long-lasting suppression of morphine, heroin, and fentanyl intake after\n\
    \    a single dose or a short treatment regimen, reversal of persistent opioid-induced\
    \ hyperalgesia, and\n    suppression of opioid drug seeking in rodent relapse\
    \ models\n  explanation: Shows kappa-agonist iboga analogues are sufficient to\
    \ produce the target behavioural effect,\n    without establishing that ibogaine\
    \ acts through kappa."
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
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 25
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
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
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Opioid Use Disorder
- **Category:** Psychiatric

## Target Hypothesis
- **Hypothesis ID:** ibogaine_kappa_biased_agonism_model
- **Hypothesis Label:** Noribogaine G-protein-biased kappa-opioid agonism model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ibogaine_kappa_biased_agonism_model
hypothesis_label: Noribogaine G-protein-biased kappa-opioid agonism model
status: EMERGING
description: 'Proposes that the anti-opioid action of ibogaine is carried principally by noribogaine''s
  G-protein-biased agonism at the kappa-opioid receptor, with weak mu-opioid antagonism as a secondary
  contributor. Bias away from beta-arrestin recruitment is invoked to explain why the compound lacks the
  dysphoria of conventional kappa agonists, and functional inhibition of dynorphin-driven beta-arrestin
  signalling is invoked to explain relief of the hyperkatifeia/anti-reward state. The strongest support
  is structural rather than loss-of-function: iboga analogues engineered as potent kappa agonists retain
  long-lasting suppression of opioid intake and reverse opioid-induced hyperalgesia while shedding the
  cardiac liability. That establishes kappa agonism as sufficient in rodents, not that ibogaine itself
  acts through kappa.'
notes: 'Distinguishing test: a selective kappa antagonist, or a kappa-receptor knockout, should abolish
  ibogaine''s suppression of opioid self-administration if this model holds. Note also that the micromolar
  affinities involved mean the model depends on brain concentrations actually reached at therapeutic doses,
  which is where the CYP2D6-driven exposure variability becomes mechanistically relevant rather than merely
  a safety issue.'
evidence:
- reference: PMID:26302653
  reference_title: Noribogaine is a G-protein biased κ-opioid receptor agonist.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: noribogaine was a G-protein biased kappa agonist 75% as efficacious as dynorphin A at stimulating
    GDP-GTP exchange
  explanation: Characterizes the biased kappa pharmacology the model is built on.
- reference: PMID:26302653
  reference_title: Noribogaine is a G-protein biased κ-opioid receptor agonist.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: Noribogaine was a weak mu antagonist with a functional inhibition constants (Ke) of 20 μM at
    the G-protein and β-arrestin signaling pathways
  explanation: Constrains the mu contribution to weak antagonism, which argues against withdrawal relief
    being explained by opioid-agonist substitution.
- reference: PMID:7796150
  reference_title: Radioligand-binding study of noribogaine, a likely metabolite of ibogaine.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Noribogaine showed a higher affinity than ibogaine for all of the opioid receptors
  explanation: Supports assigning the opioid-receptor component of the effect to the long-lived metabolite
    rather than the parent drug.
- reference: PMID:39304653
  reference_title: Oxa-Iboga alkaloids lack cardiac risk and disrupt opioid use in animal models.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: Oxa-noribogaine induces long-lasting suppression of morphine, heroin, and fentanyl intake after
    a single dose or a short treatment regimen, reversal of persistent opioid-induced hyperalgesia, and
    suppression of opioid drug seeking in rodent relapse models
  explanation: Shows kappa-agonist iboga analogues are sufficient to produce the target behavioural effect,
    without establishing that ibogaine acts through kappa.
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

# Mechanistic Hypothesis Search — Noribogaine G-protein-biased kappa-opioid agonism model

**Disease:** Opioid Use Disorder (Psychiatric)
**Hypothesis ID:** `ibogaine_kappa_biased_agonism_model`
**Hypothesis Label:** Noribogaine G-protein-biased kappa-opioid agonism model
**Status in KB:** EMERGING
**Search date:** 2026-08-28 · 35 papers reviewed · 6 findings recorded across 5 iterations

---

## Summary

The hypothesis proposes that ibogaine's anti-opioid action is carried principally by the long-lived metabolite **noribogaine acting as a G-protein-biased kappa-opioid receptor (KOR) agonist**, with weak mu-opioid antagonism as a secondary contributor. Bias away from β-arrestin is invoked to explain why the compound lacks conventional kappa-agonist dysphoria, and functional inhibition of dynorphin-driven β-arrestin signalling is invoked to explain relief of the hyperkatifeia/anti-reward state. After a focused search of the primary literature, the verdict is **PARTIALLY SUPPORTED, with the central causal claim UNRESOLVED.**

The model decomposes into three claims of very different strength. First, "noribogaine is a G-protein-biased KOR agonist with weak mu antagonism" is **well established in vitro and independently replicated** — this is the model's strongest pillar. Second, "kappa agonism is *sufficient* to produce the durable anti-opioid phenotype" is **supported in rodents** by engineered iboga analogs (oxa-noribogaine) that are potent selective KOR agonists, durably suppress opioid intake, reverse opioid-induced hyperalgesia, and shed cardiac liability. Third — and decisively — "kappa agonism is *necessary* for native ibogaine's effect" is **untested**: no selective kappa-antagonist (norBNI) reversal experiment or *Oprk1*-knockout test of ibogaine's suppression of opioid self-administration was found. This is the load-bearing missing edge.

Three caveats keep the model from confirmation. (1) A **direction-of-effect paradox**: the anti-reward/anhedonia (hyperkatifeia) state the model claims to relieve is precisely the validated clinical indication for KOR *antagonists* (aticaprant, navacaprant), and ibogaine produces a durable *antidepressant* effect in humans that is hard to reconcile with net KOR agonism. (2) **Micromolar potency and CYP2D6-gated exposure** make efficacy contingent on brain concentrations actually reached. (3) The anti-opioid phenotype is **equally reproduced by at least three kappa-independent routes** (α3β4 nicotinic antagonism, VTA GDNF induction, 5-HT2A/neuroplasticity), one of which (GDNF) carries the loss-of-function evidence the kappa model lacks. The single most informative next experiment is a norBNI or *Oprk1*-knockout reversal test of ibogaine in opioid self-administration.

---

## Key Findings

### F001 — Noribogaine's biased kappa pharmacology is genuine, but micromolar and metabolite-dependent

The foundational pharmacology of the model is solid and replicated. Maillet and colleagues ([PMID: 26302653](https://pubmed.ncbi.nlm.nih.gov/26302653/)) characterized noribogaine as a **G-protein-biased KOR agonist, ~75% as efficacious as dynorphin A** at stimulating GDP–GTP exchange (EC50 ≈ 9 μM), yet only ~12% as efficacious at recruiting β-arrestin. Critically, noribogaine **functionally inhibits dynorphin-induced KOR β-arrestin recruitment** (IC50 ≈ 1 μM) — the exact molecular event the seed hypothesis invokes to explain relief of the dynorphin-driven hyperkatifeia state — and is a **weak mu antagonist** (functional Ke ≈ 20 μM at both G-protein and β-arrestin pathways).

The mu characterization was independently reinforced by Antonio/Zanda et al. ([PMID: 24204784](https://pubmed.ncbi.nlm.nih.gov/24204784/)): ibogaine, noribogaine, and 18-MC are **mu-opioid receptor antagonists** (functional Ke ~3 μM for ibogaine to ~13 μM for noribogaine and 18-MC), not agonists. This matters mechanistically because it argues **against** an opioid-substitution explanation for withdrawal relief — if the compounds antagonize mu, withdrawal relief cannot be a buprenorphine/methadone-style agonist substitution.

Two further pieces anchor the assignment of the opioid pharmacology to the metabolite. Higgins/Mash 1995 ([PMID: 7796150](https://pubmed.ncbi.nlm.nih.gov/7796150/)) found **noribogaine has higher affinity than ibogaine for all opioid receptors**, and the clinical PK study of Knuijver et al. ([PMID: 38519421](https://pubmed.ncbi.nlm.nih.gov/38519421/)) is consistent with brain noribogaine only just reaching the low-micromolar range after therapeutic dosing, with wide CYP2D6-dependent variability. Because the KOR EC50 (~9 μM) and mu Ke (~20 μM) sit at or above achievable concentrations, **the model is exposure-limited** — whether kappa engagement is even pharmacologically meaningful depends on CYP2D6 metabolizer status, converting exposure variability from a safety concern into a mechanistically load-bearing variable.

### F002 — Strong, loss-of-function-validated competing mechanisms exist that need no kappa agonism

The single most damaging class of evidence for a *kappa-necessary* model is the existence of **kappa-independent mechanisms that reproduce the anti-addictive phenotype**, at least one validated by loss of function.

**α3β4 nicotinic antagonism.** 18-methoxycoronaridine (18-MC), a de-cardiotoxified iboga congener, reduces self-administration of morphine, methamphetamine, and nicotine, and its anti-addictive potency **correlates with α3β4 nicotinic acetylcholine receptor inhibition** while its opioid activity is low ([PMID: 15178360](https://pubmed.ncbi.nlm.nih.gov/15178360/); [PMID: 12801235](https://pubmed.ncbi.nlm.nih.gov/12801235/); [PMID: 30216039](https://pubmed.ncbi.nlm.nih.gov/30216039/)). SAR work explicitly found "opioid activities were relatively low, and the α3β4 nicotinic acetylcholine receptor activities correlated with in vivo antiaddictive activities."

**VTA GDNF induction (loss-of-function validated).** He et al. 2005 ([PMID: 15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/)) showed ibogaine reduces ethanol self-administration by inducing glial cell line-derived neurotrophic factor in the ventral tegmental area; the effect is **mimicked by intra-VTA GDNF microinjection and blocked by intra-VTA anti-GDNF neutralizing antibodies**. This is the gold-standard necessity+sufficiency design the kappa hypothesis conspicuously lacks, and it points to a distinct mechanism.

Supporting the polypharmacology picture, Wei et al. 1998 ([PMID: 9685673](https://pubmed.ncbi.nlm.nih.gov/9685673/)) showed iboga alkaloids differ markedly in serotonergic effects (ibogaine causes large 5-HT increases, 18-MC none) yet share anti-addictive claims — arguing 5-HT is not essential and cautioning against single-receptor attributions. Litjens & Brunt 2016 ([PMID: 26807959](https://pubmed.ncbi.nlm.nih.gov/26807959/)) catalog micromolar interactions across NMDA, κ/μ-opioid, sigma-2, nicotinic, serotonin, and dopamine systems — a genuinely polypharmacological profile in which kappa is one node among many. Because multiple parallel routes converge on the same behavioral endpoint, demonstrating that kappa agonism is *sufficient* cannot establish that it is *necessary* for native ibogaine.

### F003 — Human clinical evidence: ibogaine relieves withdrawal, drug use, AND depression — the antidepressant effect sits awkwardly with a kappa-agonist model

Two uncontrolled human datasets anchor the clinical phenotype. Alper et al. 1999 ([PMID: 10506904](https://pubmed.ncbi.nlm.nih.gov/10506904/)) reported an open-label case series (n=33) in which **resolution of opioid withdrawal signs without further drug-seeking occurred within 24 h in 25/33 patients**, sustained to 72 h — with one fatality. Noller et al. 2018 ([PMID: 28402682](https://pubmed.ncbi.nlm.nih.gov/28402682/)) followed n=14 patients in a 12-month observational study of legal ibogaine treatment for opioid dependence and found a significant reduction in ASI-Lite drug-use composite (p=0.002), a significant acute reduction in Subjective Opioid Withdrawal Scale (p=0.015), and — importantly — a **significant, sustained reduction in Beck Depression Inventory-II from baseline to 12 months (p<0.001)**, again with one death during treatment.

The durable *antidepressant* signal is the crux of the tension. If the therapeutic mechanism were net KOR agonism, one would expect a pro-dysphoric tendency (see F004/F006), not a sustained antidepressant effect. The model reconciles this via **bias away from β-arrestin** (avoiding dysphoria) and **functional inhibition of dynorphin-driven β-arrestin signalling** (net anti-hyperkatifeia). That is internally coherent, but it is an inference, not a demonstration — no human study measured KOR engagement, dynorphin tone, or bias-dependent signalling in treated patients. Both datasets are also small, uncontrolled/observational, and carry treatment-associated mortality.

### F004 — Direction-of-effect paradox: hyperkatifeia relief is the validated indication for kappa ANTAGONISTS

The dynorphin/KOR system is a well-established driver of stress-induced dysphoria and pro-addictive behavior (Bruchas, Land & Chavkin 2010, [PMID: 19716811](https://pubmed.ncbi.nlm.nih.gov/19716811/): "activation of the dynorphin/kappa opioid receptor (KOR) system is likely to play a major role in the pro-addictive effects of stress"). The clinically validated way to relieve the resulting anti-reward/anhedonia state is **KOR antagonism, not agonism**:

- Aticaprant (a KOR antagonist) produced a **significant MADRS improvement vs placebo** in a phase 2 MDD trial, with a larger benefit in the high-anhedonia subgroup ([PMID: 38649428](https://pubmed.ncbi.nlm.nih.gov/38649428/); effect sizes ~0.23–0.36).
- A systematic review supports aticaprant and navacaprant as mechanistically novel antidepressants targeting anhedonia ([PMID: 39019223](https://pubmed.ncbi.nlm.nih.gov/39019223/)).
- Aticaprant reverses chronic-stress anhedonia in mice ([PMID: 32894343](https://pubmed.ncbi.nlm.nih.gov/32894343/)).

The seed hypothesis proposes a G-protein-biased KOR **agonist** (noribogaine) to relieve the same hyperkatifeia state — **the opposite pharmacological direction** from the validated antidepressant class. The model's defense is that noribogaine's functional inhibition of dynorphin-driven β-arrestin signalling (F001) makes it behave, in the pathological high-dynorphin state, more like a partial antagonist/normalizer than a classical agonist. This is a plausible, testable reconciliation, but it is currently a hypothesis layered on a hypothesis. The polarity mismatch is the single strongest conceptual argument against the model as literally stated.

### F005 — A 5-HT2A/neuroplasticity (psychoplastogen) competitor, and cardiac liability is ibogaine/hERG-driven

Cameron et al. 2021 ([PMID: 33299186](https://pubmed.ncbi.nlm.nih.gov/33299186/)) introduced tabernanthalog (TBG), a **non-hallucinogenic ibogaine analog** that promotes neural plasticity and reduces alcohol- and heroin-seeking — attributing iboga's anti-addictive effect to a **5-HT2A/neuroplasticity (psychoplastogen)** mechanism distinct from opioid receptors. A recent conceptual synthesis ([PMID: 41424776](https://pubmed.ncbi.nlm.nih.gov/41424776/)) similarly frames ibogaine's action as GDNF induction plus glutamate/dopamine modulation and reopened plasticity restoring reward-system fidelity — with kappa as, at most, one contributor.

Separately, the cardiac-safety argument that motivates oxa-iboga engineering is **ibogaine/parent-driven**: Knuijver et al. 2024 ([PMID: 38519421](https://pubmed.ncbi.nlm.nih.gov/38519421/)) concluded QTc prolongation and cerebellar effects are "most likely more driven by ibogaine rather than noribogaine," and ibogaine clearance is strongly CYP2D6-dependent; Litjens & Brunt attribute QT risk to hERG channel blockade. This supports oxa-iboga's *separability* argument (keep kappa agonism, drop hERG liability) but is orthogonal to whether native ibogaine works *through* kappa. The strongest positive evidence for the model — oxa-noribogaine ([PMID: 39304653](https://pubmed.ncbi.nlm.nih.gov/39304653/)) — is a **sufficiency** result: potent KOR-agonist analogs induce "long-lasting suppression of morphine, heroin, and fentanyl intake after a single dose... reversal of persistent opioid-induced hyperalgesia, and suppression of opioid drug seeking," and lack proarrhythmia in human cardiomyocytes. But the authors note these are "mechanistically distinct" with "atypical behavioral features compared to standard kappa opioid agonists," and the study does not show ibogaine requires kappa.

### F006 — Human OPRK1/PDYN genetics validate KOR as an OUD node but deepen the polarity tension; no ibogaine-response pharmacogenomics exists

Human genetics implicate the dynorphin/KOR system in substance-use disorder risk, validating KOR as an OUD-relevant node while repeatedly labelling KOR *activation* as pro-addictive/pro-dysphoric:

- Yuferov/Kreek 2022 ([PMID: 34843875](https://pubmed.ncbi.nlm.nih.gov/34843875/)): OPRK1 intron-2 SNPs (a glucocorticoid-responsive enhancer region) associate with opioid dependence in an African-American cohort (n=577); the paper restates that "activation of the dynorphin/KOR system is also thought to have a role in the pro-addictive effects of stress."
- Nagaya 2018 ([PMID: 28656735](https://pubmed.ncbi.nlm.nih.gov/28656735/)): OPRD1 rs1042114 strongly associated with opiate addiction (p=0.0001); OPRK1 rs702764 was not; PDYN rs910080 was (p=0.0217).
- Karpyak 2013 ([PMID: 23101464](https://pubmed.ncbi.nlm.nih.gov/23101464/)): a PDYN haplotype associated with alcohol dependence (p=0.0008) and negative-emotion craving; the paper states plainly that "synthetic κ-opioid receptor (KOR) agonists induce dysphoric and pro-depressive effects."
- Özkan-Kotiloğlu 2023 ([PMID: 37177778](https://pubmed.ncbi.nlm.nih.gov/37177778/)): OPRK1 rs6473797 associated with AUD risk; rs963549 with depressive-symptom intensity.

Crucially, **no study linking OPRK1/PDYN genotype (or CYP2D6 metabolizer status) to ibogaine/noribogaine or oxa-iboga treatment response was found.** This is a concrete source/data absence: the pharmacogenomic edge that would connect the validated KOR node to ibogaine response is entirely unpopulated.

---

## Mechanistic Model / Interpretation

### Hypothesized causal chain and where the literature is strong vs. inferred

```
Ibogaine (oral, therapeutic dose)
   │  CYP2D6-dependent metabolism            ← STRONG (PMID:38519421); rate-limiting, variable
   ▼
Noribogaine accumulates (long-lived; higher opioid affinity than parent)
   │  must reach µM brain conc.              ← EXPOSURE GAP: near-EC50, CYP2D6-gated
   ▼
G-protein-biased KOR agonism (EC50 ~9 µM)
 + functional inhibition of dynorphin→β-arrestin (IC50 ~1 µM)
 + weak mu antagonism (Ke ~20 µM)           ← STRONG in vitro (PMID:26302653; repl. 24204784)
   ▼
Net damping of maladaptive dynorphin/KOR anti-reward signalling
   │  bias avoids dysphoria                  ← CONTESTED premise (PMID:35513117); POLARITY PARADOX (F004)
   ▼
Relief of hyperkatifeia; ↓ opioid-induced hyperalgesia; ↓ opioid self-administration
   │  KOR necessity                          ← MISSING EDGE: no norBNI/Oprk1-KO test found
   ▼
↓ withdrawal, ↓ drug use, ↓ depression (human, uncontrolled)
                                             ← WEAK: PMID:10506904, 28402682 (no mechanistic assay)
```

| Causal step | Status | Support |
|---|---|---|
| Ibogaine → noribogaine (CYP2D6) | **Established** | PMID:38519421, 26807959 |
| Noribogaine carries opioid pharmacology | **Established** | PMID:7796150 |
| Biased KOR agonism + weak mu antagonism | **Established in vitro** | PMID:26302653; repl. 24204784 |
| Inhibits dynorphin-driven β-arrestin | **Established in vitro** | PMID:26302653 |
| Brain noribogaine reaches KOR-active conc. | **Weak / exposure-limited** | PMID:38519421 |
| **KOR agonism *necessary* for ibogaine's effect** | **UNTESTED (missing edge)** | — |
| KOR agonism *sufficient* for phenotype | **Supported (rodent)** | PMID:39304653 |
| Biased agonism relieves (not worsens) hyperkatifeia | **Contested** | vs PMID:38649428, 19716811, 23101464 |
| Human clinical benefit | **Weak (uncontrolled)** | PMID:10506904, 28402682 |

Every biochemical step *upstream* of receptor engagement is well supported, but the **single edge that would make the model causal — "KOR engagement is required for the behavioral effect" — is entirely inferred**, and the step immediately downstream runs against the validated pharmacology of the KOR-antagonist antidepressant class.

### Competing-mechanism map

```
                    ANTI-OPIOID / ANTI-ADDICTIVE PHENOTYPE
                    (↓ self-admin, ↓ withdrawal, ↓ seeking)
                         ▲     ▲     ▲     ▲
      ┌──────────────────┘     │     │     └──────────────────┐
Biased KOR agonism    α3β4 nicotinic   VTA GDNF induction   5-HT2A / neuroplasticity
(seed hypothesis)     antagonism       (He 2005)            (tabernanthalog)
NECESSITY: untested   (18-MC)          NECESSITY:           NECESSITY: analog
SUFFICIENCY: oxa-     NECESSITY:       LOSS-OF-FUNCTION     reproduces effect
iboga (39304653)      potency-corr.    VALIDATED (anti-     (33299186)
                      (15178360)       GDNF antibody)
```

Only the GDNF route currently carries loss-of-function evidence — a competitor with the causal design the seed hypothesis lacks. The most incisive reinterpretation of the *same* molecular data is a **KOR-signalling-normalization model**: noribogaine's measured inhibition of dynorphin-driven β-arrestin recruitment could make it act, in the high-dynorphin withdrawal/stress state, more like a functional antagonist than a classical agonist — simultaneously explaining the anti-opioid effect *and* the antidepressant effect while dissolving the polarity paradox.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [26302653](https://pubmed.ncbi.nlm.nih.gov/26302653/) | In vitro | **Supports** | Noribogaine biased KOR agonism + weak mu antagonism | ~75% dynorphin-A G-protein efficacy (EC50 9 µM), ~12% β-arrestin; inhibits dynorphin β-arrestin (IC50 1 µM); mu Ke 20 µM | Molecular pharmacology | High for pharmacology; micromolar; heterologous |
| [24204784](https://pubmed.ncbi.nlm.nih.gov/24204784/) | In vitro | **Qualifies (mu)** | Iboga alkaloids at MOR | Ibogaine/noribogaine/18-MC are mu **antagonists** (Ke 3–13 µM) | Molecular pharmacology | High; independent replication |
| [7796150](https://pubmed.ncbi.nlm.nih.gov/7796150/) | In vitro | **Supports** | Metabolite carries opioid affinity | Noribogaine > ibogaine affinity at all opioid receptors | Radioligand binding | Moderate; binding only |
| [39304653](https://pubmed.ncbi.nlm.nih.gov/39304653/) | Model organism | **Supports (sufficiency)** | KOR agonism sufficient for durable effect | Oxa-noribogaine: durable ↓ morphine/heroin/fentanyl intake, ↓ hyperalgesia, no cardiac risk | Male rats, OUD models | High for sufficiency; male-only; doesn't test ibogaine necessity |
| [15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/) | Model organism | **Competing (LOF)** | VTA GDNF mediates effect | Mimicked by intra-VTA GDNF, blocked by anti-GDNF antibody | Rat ethanol SA | High; gold-standard causal design; alcohol not opioid |
| [15178360](https://pubmed.ncbi.nlm.nih.gov/15178360/) | Model organism | **Competing** | α3β4 nicotinic antagonism | 18-MC blocks multi-drug SA; low opioid activity | Rat, multiple drugs | Moderate-high; correlational target link |
| [12801235](https://pubmed.ncbi.nlm.nih.gov/12801235/) | In vitro/SAR | **Competing** | α3β4 potency ↔ efficacy | Opioid activity low; α3β4 correlates w/ in vivo efficacy | SAR series | Moderate; correlational |
| [30216039](https://pubmed.ncbi.nlm.nih.gov/30216039/) | Review | **Competing (review)** | Nicotinic basis of anti-opiate effect | nAChR actions may underlie anti-opiate effects; 18-MC retains efficacy | Orientation | Review-level |
| [9685673](https://pubmed.ncbi.nlm.nih.gov/9685673/) | Model organism | **Qualifies** | Is 5-HT essential? | Iboga alkaloids differ in 5-HT effects yet share anti-addiction | Rat microdialysis | Moderate; single-target caution |
| [26807959](https://pubmed.ncbi.nlm.nih.gov/26807959/) | Review | **Qualifies (review)** | Polypharmacology & toxicity | µM at NMDA, κ/µ, sigma-2 + nicotinic/5-HT/DA; hERG QT risk | Orientation | Review-level |
| [33299186](https://pubmed.ncbi.nlm.nih.gov/33299186/) | Model organism | **Competing** | 5-HT2A/neuroplasticity | Non-hallucinogenic TBG ↓ alcohol/heroin seeking | Rodent | Moderate-high; distinct mechanism |
| [10506904](https://pubmed.ncbi.nlm.nih.gov/10506904/) | Human clinical | **Supports (weak)** | Withdrawal relief | Withdrawal resolved w/o drug-seeking 25/33 within 24h | Case series, n=33 | Low; uncontrolled; 1 fatality |
| [28402682](https://pubmed.ncbi.nlm.nih.gov/28402682/) | Human clinical | **Supports + Qualifies** | Durable use/withdrawal/mood | ↓ use (p=0.002), ↓ withdrawal (p=0.015), ↓ BDI-II 12mo (p<0.001) | Observational, n=14 | Low; uncontrolled; antidepressant paradox; 1 death |
| [19716811](https://pubmed.ncbi.nlm.nih.gov/19716811/) | Review | **Tension (review)** | KOR activation pro-addictive | Dynorphin/KOR activation drives stress pro-addictive behavior | Orientation | Review; strong consensus |
| [38649428](https://pubmed.ncbi.nlm.nih.gov/38649428/) | Human clinical | **Tension** | KOR **antagonism** treats anhedonia | Aticaprant significant MADRS vs placebo, larger in high-anhedonia | Phase 2 MDD RCT | High; opposite polarity |
| [39019223](https://pubmed.ncbi.nlm.nih.gov/39019223/) | Review | **Tension (review)** | KOR antagonists for MDD | Aticaprant/navacaprant improve depression & anhedonia | Orientation | Review; phase 3 pending |
| [32894343](https://pubmed.ncbi.nlm.nih.gov/32894343/) | Model organism | **Tension** | KOR antagonism reverses anhedonia | Aticaprant reverses chronic-stress anhedonia | Male mice UCMS | Moderate-high; opposite polarity |
| [34843875](https://pubmed.ncbi.nlm.nih.gov/34843875/) | Human genetic | **Qualifies** | KOR/dynorphin is an OUD node | OPRK1 intron-2 SNPs assoc. opioid dependence (n=577) | African-American cohort | Moderate; activation pro-addictive |
| [28656735](https://pubmed.ncbi.nlm.nih.gov/28656735/) | Human genetic | **Qualifies** | Opioid-system genetics | OPRD1 rs1042114 (p=0.0001); OPRK1 rs702764 null; PDYN rs910080 (p=0.0217) | Malaysian Malay, n=1002 | Moderate; OPRK1 weak here |
| [23101464](https://pubmed.ncbi.nlm.nih.gov/23101464/) | Human genetic | **Tension** | PDYN & negative-affect craving | PDYN haplotype assoc. dependence (p=0.0008); "KOR agonists induce dysphoric/pro-depressive effects" | AUD cohort | Moderate; restates agonist-dysphoria |
| [37177778](https://pubmed.ncbi.nlm.nih.gov/37177778/) | Human genetic | **Qualifies** | OPRK1 variation & depression | OPRK1 rs6473797 ↔ AUD; rs963549 ↔ depressive intensity | Turkish males, n=201 | Moderate; AUD not OUD |
| [35513117](https://pubmed.ncbi.nlm.nih.gov/35513117/) | Model organism | **Qualifies** | Is G-protein bias the mechanism? | Biased agonist triazole 1.1 milder, but benefit "attributed to factors other than G-protein bias" | Rhesus monkeys | Moderate; questions bias framing |
| [39833376](https://pubmed.ncbi.nlm.nih.gov/39833376/) | Review (scoping) | **Qualifies** | Preclinical reproducibility | Most studies show iboga ↓ opioid SA, but 7 (incl. 3 ibogaine) showed no improvement; quality "unclear" | OUD preclinical | Review; documents failed replications |

---

## Limitations and Knowledge Gaps

Each gap states scope, why it matters, what was checked, and what would resolve it.

**G1 — The necessity edge is untested (load-bearing gap).** *Scope:* No study applies a selective KOR antagonist (norBNI) or *Oprk1* knockout to test whether ibogaine/noribogaine's suppression of opioid self-administration is abolished. *Why it matters:* This is the exact distinguishing test named in the seed YAML; without it only sufficiency (via analogs) is established. *Checked:* PubMed for ibogaine/noribogaine × kappa × antagonist/knockout/self-administration — none found; PMID:39304653 reports sufficiency only. *Resolution:* norBNI pretreatment and *Oprk1*⁻/⁻ reversal in rodent opioid self-administration.

**G2 — Direction-of-effect paradox unresolved.** *Scope:* Whether biased/partial KOR engagement is net anti-hyperkatifeic in vivo, given KOR *antagonists* are the validated anhedonia therapy. *Checked:* KOR-antagonist depression literature (PMID:38649428, 39019223, 32894343) and human genetics restating agonist dysphoria (PMID:19716811, 23101464). *Resolution:* In vivo ICSS thresholds, CPA, sucrose preference comparing noribogaine, a biased agonist, and a KOR antagonist under high-dynorphin states.

**G3 — Exposure/potency gap.** *Scope:* Whether therapeutic dosing yields brain noribogaine sufficient to engage KOR (EC50 ~9 µM). *Checked:* PK/PD study PMID:38519421 (near-micromolar, CYP2D6-variable). *Resolution:* Paired plasma/CSF or KOR-PET occupancy stratified by CYP2D6 genotype.

**G4 — No ibogaine-response pharmacogenomics (source/data absence).** *Scope:* No dataset links OPRK1/PDYN or CYP2D6 genotype to ibogaine/oxa-iboga response. *Checked:* Human OPRK1/PDYN genetics (PMID:34843875, 28656735, 23101464, 37177778) — none reference ibogaine. *Resolution:* Genotype-stratified outcomes in any ibogaine OUD cohort.

**G5 — No controlled human trials; no human mechanistic assays.** *Scope:* All human OUD evidence is uncontrolled/observational, small n, no receptor-level readouts. *Checked:* PMID:10506904 (n=33), 28402682 (n=14); scoping review PMID:39833376 notes most clinical evidence is observational. *Resolution:* RCTs with embedded mechanistic biomarkers.

**G6 — Sufficiency evidence is male-only and analog-based.** *Scope:* Oxa-noribogaine efficacy in male rats only; effects from re-engineered analogs, not parent. *Checked:* PMID:39304653. *Resolution:* Female cohorts and direct native-ibogaine perturbation.

**G7 — "G-protein bias as the causal feature" is itself contested.** *Scope:* Whether reduced side-effects of biased KOR agonists are actually due to bias. *Checked:* PMID:35513117 — biased triazole 1.1 milder effects "attributed to factors other than G-protein bias." *Resolution:* Kinetic/residence-time and mutant-receptor studies dissociating bias from other properties.

**G8 — Registry/omics absences (curation provenance).** *Scope:* PharmGKB, GWAS Catalog, ClinicalTrials.gov not directly queried. *Resolution:* Query PharmGKB for CYP2D6×ibogaine; ClinicalTrials.gov for oxa-iboga/noribogaine/ibogaine OUD trials.

---

## Alternative / Competing Models

| Model | Relationship to seed hypothesis | Evidence | Verdict |
|---|---|---|---|
| **α3β4 nicotinic antagonism (18-MC)** | Alternative / parallel (different receptor family) | PMID:15178360, 12801235, 30216039 | Strong parallel; potency correlates with target; low opioid activity |
| **VTA GDNF induction** | Alternative (plausible downstream convergence node) | PMID:15659598 (LOF), 41424776 | Strongest causal design of any competitor; validated in alcohol model |
| **5-HT2A / neuroplasticity (psychoplastogen)** | Alternative / parallel | PMID:33299186, 41424776 | Non-hallucinogenic analog reproduces effect without opioid receptors |
| **Mu-opioid antagonism** | Complementary (secondary within seed model) | PMID:26302653, 24204784 | Real but weak (Ke 20 µM); argues against substitution, not a primary driver |
| **KOR-signalling normalization / antagonism** | Competing reinterpretation of same node — opposite polarity | PMID:26302653 (β-arrestin inhibition), 38649428, 39019223, 32894343 | Reframes benefit as functional KOR-signalling dampening; better explains antidepressant effect |
| **NMDA antagonism** | Parallel legacy hypothesis | PMID:26807959 | µM NMDA affinity historically invoked; not independently favored |
| **Non-specific polypharmacology** | Umbrella alternative — no single edge necessary | PMID:26807959, 9685673 | Parsimonious given convergent phenotype |

These are not mutually exclusive: ibogaine is polypharmacological, and the effect is plausibly the sum of several µM-affinity actions, with noribogaine shifting the balance toward the opioid/kappa arm over time.

---

## Proposed Follow-up Experiments / Discriminating Tests (ranked by decisiveness)

1. **Kappa necessity test (most decisive).** *Oprk1*-KO/conditional-KO and norBNI pretreatment before ibogaine/noribogaine in rat opioid (heroin/fentanyl) self-administration + opioid-induced hyperalgesia; include both sexes. *If model holds:* anti-opioid effect abolished. *If preserved:* kappa dispensable for ibogaine — refutes necessity while leaving oxa-iboga sufficiency intact.
2. **Target-engagement / occupancy study.** KOR PET occupancy (e.g., [¹¹C]LY2795050) vs plasma/brain noribogaine across CYP2D6 phenotypes; correlate occupancy with behavioral suppression. Resolves the exposure-gating gap.
3. **Polarity test.** Compare oxa-noribogaine (biased KOR agonist) vs aticaprant (KOR antagonist) in ICSS and anhedonia assays after chronic opioid/withdrawal. Determines whether anti-reward relief is agonist- or antagonist-like.
4. **Mechanism-dissection panel.** In matched OUD models, compare oxa-noribogaine (kappa), 18-MC (α3β4), tabernanthalog (5-HT2A) ± their respective antagonists ± anti-GDNF; measure VTA GDNF. Partitions the convergent phenotype among routes.
5. **CYP2D6-stratified human PK/PD RCT.** Genotype-stratified dosing with noribogaine exposure, KOR pharmacodynamic biomarkers (e.g., prolactin), and withdrawal/anhedonia scales.
6. **Pharmacogenomic association.** Test OPRK1/PDYN and CYP2D6 variants against ibogaine/oxa-iboga response in any available cohort/registry (closes G4).

---

## Curation Leads (require curator verification)

**Candidate status:** Retain **EMERGING**; annotate that the model's **sufficiency** claim is supported while its **necessity** claim is untested; flag the direction-of-effect paradox prominently; add restriction that behavioral kappa evidence is male-rat and analog-based.

**Candidate evidence references + snippets to verify:**
- PMID:26302653 — "noribogaine was a G-protein biased kappa agonist 75% as efficacious as dynorphin A at stimulating GDP-GTP exchange" (SUPPORT, IN_VITRO; already in KB).
- PMID:24204784 — "ibogaine, noribogaine and 18-MC were MOR antagonists with functional Ke values ranging from 3 uM (ibogaine) to 13 uM (noribogaine and 18MC)" (QUALIFIES mu claim, IN_VITRO; new).
- PMID:15659598 — "the ibogaine-mediated decrease in ethanol self-administration was mimicked by intra-VTA microinjection of GDNF and was reduced by intra-VTA delivery of anti-GDNF neutralizing antibodies" (COMPETING, MODEL_ORGANISM, loss-of-function; new).
- PMID:15178360 — "These data are consistent with the importance of nicotinic alpha3beta4 receptors as a therapeutic target to modulate drug seeking" (COMPETING, MODEL_ORGANISM; new).
- PMID:33299186 — "The psychedelic alkaloid ibogaine has anti-addictive properties in both humans and animals" (COMPETING context, 5-HT2A/plasticity; new).
- PMID:28402682 — "Reductions in BDI-II scores from baseline to 12-month follow-up were also significant (p < 0.001)" (SUPPORT + QUALIFIES; antidepressant paradox; new).
- PMID:38649428 — "Improvement ... in MADRS total score at week 6 for aticaprant was significant versus placebo" (COMPETING/direction; new).
- PMID:23101464 — "Synthetic κ-opioid receptor (KOR) agonists induce dysphoric and pro-depressive effects" (tension against KOR-agonist therapy; new).
- PMID:38519421 — "Ibogaine cardiac side effects (QTc time) and cerebellar effects are most likely more driven by ibogaine rather than noribogaine" (QUALIFIES; exposure/CYP2D6; new).
- PMID:39833376 — "seven studies ... showed no improvement over controls" (QUALIFIES/negative replications, REVIEW; new).

**Candidate pathophysiology nodes/edges:**
- Node: `noribogaine` —biased_agonist→ `KOR (OPRK1)` [G-protein pathway] (established, in vitro).
- Edge: `noribogaine` —functional_antagonist→ `dynorphin/KOR β-arrestin recruitment` (in vitro; label UNCONFIRMED in vivo).
- Edge: `KOR engagement` → `↓ opioid self-administration` — mark **UNCONFIRMED (missing perturbation evidence)**.
- Competing edges: `ibogaine`→`VTA GDNF`→↓drug SA (LOF-validated, alcohol); `18-MC`⊣`α3β4 nAChR`→↓drug SA; `tabernanthalog`→`5-HT2A`→neuroplasticity→↓seeking.
- Gating node: `CYP2D6 genotype`→`noribogaine exposure`→(gates) target engagement.

**Candidate ontology terms:** kappa opioid receptor (OPRK1); prodynorphin (PDYN); β-arrestin-2 (ARRB2); GPCR signaling pathway (GO:0007186); α3β4 nicotinic receptor (CHRNA3/CHRNB4); GDNF/RET signaling (GO:0035860); serotonin 5-HT2A receptor (HTR2A); CYP2D6; ventral tegmental area; nucleus accumbens; medial habenula; "drug self-administration"; "hyperalgesia"; "hyperkatifeia/negative affect".

**Candidate knowledge_gaps / discussion prompts:** (1) "No norBNI/*Oprk1*-knockout test of ibogaine's anti-opioid effect exists — kappa necessity unproven." (2) "Direction-of-effect conflict with KOR-antagonist antidepressant class (aticaprant/navacaprant)." (3) "In vivo KOR occupancy at therapeutic human noribogaine exposure unmeasured." (4) "Negative/failed preclinical replications exist (PMID:39833376)." (5) "No OPRK1/PDYN or CYP2D6 pharmacogenomic evidence for ibogaine response retrieved as of 2026-08-28."

---

## Limitations of this Search

Literature-only (no primary datasets analyzed); targeted pharmacogenomic/registry sources (PharmGKB, GWAS Catalog, ClinicalTrials.gov) were not directly queried and are listed as curation to-dos rather than confirmed absences; several key papers were available only as abstracts. The judgment reflects primary in vitro, model-organism, human clinical, and human genetic studies; reviews are labeled as review-level orientation.

---

*Report generated 2026-08-28 from a 5-iteration hypothesis search (35 papers reviewed, 6 findings recorded).*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)