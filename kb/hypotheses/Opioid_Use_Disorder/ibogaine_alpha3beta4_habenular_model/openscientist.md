---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T04:02:18.453424'
end_time: '2026-08-28T04:27:44.704881'
duration_seconds: 1526.25
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Opioid Use Disorder
  category: Psychiatric
  hypothesis_group_id: ibogaine_alpha3beta4_habenular_model
  hypothesis_label: Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular
    pathway
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: ibogaine_alpha3beta4_habenular_model\nhypothesis_label:\
    \ Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway\nstatus:\
    \ EMERGING\ndescription: 'Proposes that iboga alkaloids reduce opioid self-administration\
    \ by noncompetitively blocking\n  alpha3beta4 nicotinic acetylcholine receptors,\
    \ which are concentrated in the medial habenula and interpeduncular\n  nucleus\
    \ rather than in the mesolimbic pathway, and thereby damping the sensitized accumbal\
    \ dopamine\n  response to repeated opioid exposure. The site specificity is the\
    \ model''s strength: local infusion\n  into the medial habenula or interpeduncular\
    \ nucleus reduces morphine self-administration while the same\n  infusion into\
    \ the ventral tegmental area does not, and the effect spares responding for a\
    \ non-drug reinforcer.\n  Its weakness for ibogaine specifically is that the supporting\
    \ in vivo work uses the congener 18-MC,\n  which does not reproduce ibogaine''s\
    \ neurotrophic actions, while noribogaine is a comparatively weak\n  alpha3beta4\
    \ blocker.'\nnotes: 'Distinguishing test: this model and the GDNF model predict\
    \ opposite outcomes for a local-infusion\n  dissociation - intra-habenular ibogaine\
    \ should suffice if the nicotinic route carries the effect, intra-VTA\n  ibogaine\
    \ if the neurotrophic route does. The two are not mutually exclusive and may account\
    \ for different\n  time courses, with nicotinic blockade acting during drug exposure\
    \ and neurotrophic remodelling accounting\n  for persistence.'\nevidence:\n- reference:\
    \ PMID:16626688\n  reference_title: 18-Methoxycoronaridine acts in the medial\
    \ habenula and/or interpeduncular nucleus to\n    decrease morphine self-administration\
    \ in rats.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n  snippet:\
    \ Local administration of 18-MC into either the medial habenula or the interpeduncular\
    \ area decreased\n    morphine self-administration while having no effect on responding\
    \ for a non-drug reinforcer (sucrose)\n  explanation: Localizes the anti-opioid\
    \ effect to the habenulo-interpeduncular pathway and shows it is\n    not general\
    \ response suppression.\n- reference: PMID:16626688\n  reference_title: 18-Methoxycoronaridine\
    \ acts in the medial habenula and/or interpeduncular nucleus to\n    decrease\
    \ morphine self-administration in rats.\n  supports: SUPPORT\n  evidence_source:\
    \ MODEL_ORGANISM\n  snippet: Local administration of 18-MC into the ventral tegmental\
    \ area had no effect on morphine self-administration\n  explanation: Negative\
    \ control that separates this model's site of action from the VTA site invoked\
    \ by\n    the GDNF model.\n- reference: PMID:17447255\n  reference_title: 18-MC\
    \ acts in the medial habenula and interpeduncular nucleus to attenuate dopamine\n\
    \    sensitization to morphine in the nucleus accumbens.\n  supports: SUPPORT\n\
    \  evidence_source: MODEL_ORGANISM\n  snippet: 18-MC had no effect on the dopamine\
    \ response to acute morphine\n  explanation: Restricts the proposed mechanism\
    \ to sensitized rather than acute mesolimbic dopamine signalling,\n    which is\
    \ the state relevant to established dependence.\n- reference: PMID:26022277\n\
    \  reference_title: Coronaridine congeners inhibit human \u03B13\u03B24 nicotinic\
    \ acetylcholine receptors by interacting\n    with luminal and non-luminal sites.\n\
    \  supports: PARTIAL\n  evidence_source: IN_VITRO\n  snippet: coronaridine congeners\
    \ noncompetitively inhibit h\u03B13\u03B24 AChRs\n  explanation: Supplies the\
    \ receptor-level mechanism, while the reported potency ordering places noribogaine\n\
    \    well below ibogaine and 18-MC, qualifying the model's applicability to the\
    \ long-lived metabolite.\n- reference: PMID:21040239\n  reference_title: Noribogaine,\
    \ but not 18-MC, exhibits similar actions as ibogaine on GDNF expression\n   \
    \ and ethanol self-administration.\n  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: our results suggest that noribogaine and 18-MC have different mechanisms\
    \ and sites of action\n  explanation: Explicit statement that the congener used\
    \ for most in vivo alpha3beta4 work does not share\n    ibogaine's route, limiting\
    \ transfer of this model to ibogaine."
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
citation_count: 19
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
- **Hypothesis ID:** ibogaine_alpha3beta4_habenular_model
- **Hypothesis Label:** Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: ibogaine_alpha3beta4_habenular_model
hypothesis_label: Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway
status: EMERGING
description: 'Proposes that iboga alkaloids reduce opioid self-administration by noncompetitively blocking
  alpha3beta4 nicotinic acetylcholine receptors, which are concentrated in the medial habenula and interpeduncular
  nucleus rather than in the mesolimbic pathway, and thereby damping the sensitized accumbal dopamine
  response to repeated opioid exposure. The site specificity is the model''s strength: local infusion
  into the medial habenula or interpeduncular nucleus reduces morphine self-administration while the same
  infusion into the ventral tegmental area does not, and the effect spares responding for a non-drug reinforcer.
  Its weakness for ibogaine specifically is that the supporting in vivo work uses the congener 18-MC,
  which does not reproduce ibogaine''s neurotrophic actions, while noribogaine is a comparatively weak
  alpha3beta4 blocker.'
notes: 'Distinguishing test: this model and the GDNF model predict opposite outcomes for a local-infusion
  dissociation - intra-habenular ibogaine should suffice if the nicotinic route carries the effect, intra-VTA
  ibogaine if the neurotrophic route does. The two are not mutually exclusive and may account for different
  time courses, with nicotinic blockade acting during drug exposure and neurotrophic remodelling accounting
  for persistence.'
evidence:
- reference: PMID:16626688
  reference_title: 18-Methoxycoronaridine acts in the medial habenula and/or interpeduncular nucleus to
    decrease morphine self-administration in rats.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Local administration of 18-MC into either the medial habenula or the interpeduncular area decreased
    morphine self-administration while having no effect on responding for a non-drug reinforcer (sucrose)
  explanation: Localizes the anti-opioid effect to the habenulo-interpeduncular pathway and shows it is
    not general response suppression.
- reference: PMID:16626688
  reference_title: 18-Methoxycoronaridine acts in the medial habenula and/or interpeduncular nucleus to
    decrease morphine self-administration in rats.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Local administration of 18-MC into the ventral tegmental area had no effect on morphine self-administration
  explanation: Negative control that separates this model's site of action from the VTA site invoked by
    the GDNF model.
- reference: PMID:17447255
  reference_title: 18-MC acts in the medial habenula and interpeduncular nucleus to attenuate dopamine
    sensitization to morphine in the nucleus accumbens.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: 18-MC had no effect on the dopamine response to acute morphine
  explanation: Restricts the proposed mechanism to sensitized rather than acute mesolimbic dopamine signalling,
    which is the state relevant to established dependence.
- reference: PMID:26022277
  reference_title: Coronaridine congeners inhibit human α3β4 nicotinic acetylcholine receptors by interacting
    with luminal and non-luminal sites.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: coronaridine congeners noncompetitively inhibit hα3β4 AChRs
  explanation: Supplies the receptor-level mechanism, while the reported potency ordering places noribogaine
    well below ibogaine and 18-MC, qualifying the model's applicability to the long-lived metabolite.
- reference: PMID:21040239
  reference_title: Noribogaine, but not 18-MC, exhibits similar actions as ibogaine on GDNF expression
    and ethanol self-administration.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: our results suggest that noribogaine and 18-MC have different mechanisms and sites of action
  explanation: Explicit statement that the congener used for most in vivo alpha3beta4 work does not share
    ibogaine's route, limiting transfer of this model to ibogaine.
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

# Mechanistic Hypothesis Search — Final Report

## Hypothesis: Alpha3beta4 nicotinic blockade in the habenulo-interpeduncular pathway (`ibogaine_alpha3beta4_habenular_model`)
### Disease: Opioid Use Disorder (Psychiatric) — KB status: EMERGING

---

## Executive Judgment

**Verdict: Partially supported — and best re-scoped as a congener-specific (18-MC-anchored) mechanism rather than an established explanation for ibogaine.**

The seed hypothesis proposes that iboga alkaloids reduce opioid self-administration by non-competitively blocking α3β4 nicotinic acetylcholine receptors (nAChRs) concentrated in the **medial habenula (MHb)** and **interpeduncular nucleus (IPN)** — not in the mesolimbic pathway — thereby damping the sensitized accumbal dopamine response to repeated opioids. Our search finds that the **receptor-level and site-specific premises are solid, but the transfer to ibogaine itself is unproven and actively contested.**

Three pillars support the model. First, a clean **local-infusion dissociation**: 18-methoxycoronaridine (18-MC) infused into the MHb or IPN — but not the VTA — reduces morphine self-administration and blocks the *sensitized* (not acute) accumbal dopamine response, while sparing responding for a non-drug reinforcer ([PMID:16626688](https://pubmed.ncbi.nlm.nih.gov/16626688/); [PMID:17447255](https://pubmed.ncbi.nlm.nih.gov/17447255/)). Second, an established **receptor mechanism**: coronaridine congeners are non-competitive α3β4 antagonists ([PMID:26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/)). Third — the strongest generalization beyond iboga drugs — **human and mouse genetics** causally tie the CHRNA5/A3/B4 (α3β4*) cluster to opioid dependence and withdrawal, and chemically distinct selective α3β4 antagonists (α-conotoxin AuIB, AT-1001) reproduce anti-withdrawal effects ([PMID:24750073](https://pubmed.ncbi.nlm.nih.gov/24750073/); [PMID:20485328](https://pubmed.ncbi.nlm.nih.gov/20485328/)).

The critical caveats are equally clear. The discovering laboratory attributed **ibogaine's own** anti-opioid self-administration effect to **kappa-opioid agonism plus NMDA antagonism**, actions that 18-MC largely lacks ([PMID:9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/); [PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/)). Unlike 18-MC, **ibogaine is not reinforcer-selective** (it also suppresses a non-drug reinforcer), weakening the transfer of the model's hallmark selectivity claim. **Noribogaine**, ibogaine's long-lived active metabolite, is the *weakest* α3β4 blocker of the congener series (~7× weaker than ibogaine) and works via a **competing GDNF/VTA neurotrophic route** that 18-MC does not engage ([PMID:26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/); [PMID:21040239](https://pubmed.ncbi.nlm.nih.gov/21040239/)). Finally, the model's clinical arm is an **explicit data gap**: no published human efficacy trial of 18-MC (or any selective α3β4 antagonist) for OUD exists as of the search date. The hypothesis should remain **EMERGING**, with an explicit annotation that the in vivo evidence is congener-specific to 18-MC.

---

## Key Findings

### F001 — Site-specific habenulo-interpeduncular localization of 18-MC's anti-morphine effect (SUPPORTS)

The keystone experimental support is a local-infusion dissociation. Glick et al. 2006 ([PMID:16626688](https://pubmed.ncbi.nlm.nih.gov/16626688/)) demonstrated that intracerebral 18-MC infused directly into the **medial habenula** or **interpeduncular nucleus** decreased morphine self-administration in rats, with *no effect on sucrose responding*, whereas the identical infusion into the **ventral tegmental area (VTA)** had no effect. The verified abstract snippet states: *"Local administration of 18-MC into either the medial habenula or the interpeduncular area decreased morphine self-administration while having no effect on responding for a non-drug reinforcer (sucrose),"* and separately, *"Local administration of 18-MC into the ventral tegmental area had no effect on morphine self-administration."*

This is a **positive, anatomically resolved dissociation** — the highest-value evidence class for a site-specificity claim. It simultaneously (a) localizes the anti-opioid effect to the habenulo-interpeduncular pathway, (b) shows reinforcer selectivity (not general response suppression), and (c) provides a negative VTA control that distinguishes this model from the competing GDNF/VTA neurotrophic route. The effect was reproduced by other α3β4 antagonists (mecamylamine, α-conotoxin AuIB), strengthening the causal attribution to the receptor rather than to an idiosyncratic property of 18-MC. A companion study ([PMID:17447255](https://pubmed.ncbi.nlm.nih.gov/17447255/)) showed that intra-MHb or intra-IPN 18-MC **blocked the sensitized accumbal dopamine response to repeated morphine** but had *"no effect on the dopamine response to acute morphine,"* restricting the mechanism to the sensitized state relevant to established dependence.

### F002 — Receptor-level non-competitive α3β4 block established, but noribogaine is the weakest congener (QUALIFIES)

Arias et al. 2015 ([PMID:26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/)) established the receptor mechanism: coronaridine congeners **non-competitively inhibit human α3β4 nAChRs** by interacting with luminal and non-luminal sites. Critically, the potency ordering places the therapeutically relevant metabolite last. The verified IC₅₀ sequence is: ibogamine (0.62 µM) ≈ catharanthine (0.68) > **ibogaine (0.95)** > **18-MC (1.47)** > voacangine (2.28) > 18-methylaminocoronaridine (2.62) ≈ 18-hydroxycoronaridine (2.81) > **noribogaine (6.82 µM)**.

Noribogaine — the long-lived active metabolite that dominates ibogaine's pharmacology hours after dosing — is therefore **~7-fold weaker than ibogaine and ~4.6-fold weaker than 18-MC** at the target receptor. This is a direct quantitative qualifier: the model's molecular engine is real, but the congener most relevant to ibogaine's persistent clinical effects is the least potent at driving it.

### F003 — Competing GDNF/VTA neurotrophic route dissociates from 18-MC (LIMITS TRANSFER)

Carnicella et al. 2010 ([PMID:21040239](https://pubmed.ncbi.nlm.nih.gov/21040239/)) provides the sharpest dissociation between the two candidate mechanisms. Noribogaine, like ibogaine, induced GDNF mRNA in SH-SY5Y cells, and **intra-VTA noribogaine** decreased alcohol self-administration — whereas 18-MC did neither. The verified conclusion: *"noribogaine, but not 18-MC, in the VTA decreases responding for alcohol. Together, our results suggest that noribogaine and 18-MC have different mechanisms and sites of action."* This is corroborated by He et al. 2005 ([PMID:15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/)): *"Microinjection of ibogaine into the ventral tegmental area (VTA), but not the substantia nigra, reduced self-administration of ethanol,"* and by Carnicella et al. 2008 ([PMID:18541917](https://pubmed.ncbi.nlm.nih.gov/18541917/)), showing intra-VTA GDNF is a fast-acting, MAPK-dependent suppressor of alcohol self-administration.

The upshot: the congener used for essentially all habenular α3β4 in vivo work (**18-MC**) is precisely the one that does *not* share ibogaine's / noribogaine's VTA-localized neurotrophic route. The two models predict **opposite outcomes** for a local-infusion dissociation — intra-habenular ibogaine should suffice if the nicotinic route carries the effect; intra-VTA ibogaine if the neurotrophic route does. This distinguishing test has not been performed for ibogaine.

### F004 — The medial habenula regulates opioid withdrawal/aversion — but via MOR, not proven α3β4 (PARALLEL MECHANISM)

Independent circuit work confirms the habenula is genuinely central to opioid-related aversion and withdrawal, but attributes the causality to **mu-opioid receptors (MOR)** in habenular neurons rather than to α3β4 channel block. Boulos et al. 2020 ([PMID:31005059](https://pubmed.ncbi.nlm.nih.gov/31005059/)) showed conditional deletion of MOR in *chrnb4* (β4-subunit) MHb neurons reduced naloxone conditioned place aversion and attenuated physical withdrawal, with the verified finding that *"physical signs of withdrawal precipitated by either MOR (naloxone) or nicotinic receptor (mecamylamine) blockade were attenuated."* Ozdemir et al. 2026 ([PMID:42217817](https://pubmed.ncbi.nlm.nih.gov/42217817/)) found *"Silencing Hb-MOR neurons abolished these effects and alleviated somatic withdrawal signs."* Liang et al. 2024 ([PMID:39270652](https://pubmed.ncbi.nlm.nih.gov/39270652/)) identified an IPN(GABA)→nucleus incertus circuit that amplifies aversion related to opioid withdrawal.

This is a **parallel/competing habenular mechanism**: it validates the anatomical locus but relocates the molecular driver from the α3β4 ion channel to the MOR expressed on the same β4-defined neuronal population. It raises the possibility that 18-MC's habenular effects are partly mediated through, or convergent with, MOR-expressing circuitry rather than pure nicotinic antagonism.

### F005 — Human + mouse genetics link α3β4* causally to morphine dependence/withdrawal (GENERALIZES BEYOND IBOGA)

The receptor premise is anchored well beyond iboga pharmacology. Muldoon et al. 2014 ([PMID:24750073](https://pubmed.ncbi.nlm.nih.gov/24750073/)) showed mice overexpressing the CHRNA5/A3/B4 cluster had increased somatic morphine-withdrawal signs; α5 and β4 knockouts had decreased signs; and selective α3β4* antagonists **α-conotoxin AuIB and AT-1001** attenuated somatic morphine withdrawal dose-dependently (*"selective α3β4* nACh receptor antagonists, α-conotoxin AuIB and AT-1001, attenuated somatic signs of morphine withdrawal in a dose-related manner"*). Two human datasets showed *"a protective role for variants in the CHRNA3 gene... in opioid dependence and withdrawal."* Sherva et al. 2010 ([PMID:20485328](https://pubmed.ncbi.nlm.nih.gov/20485328/)) independently associated the 15q25 CHRNA5/A3/B4 cluster with opioid dependence phenotypes.

This finding does the heavy lifting for the *receptor* leg of the hypothesis, using chemically distinct tools and human genetics that owe nothing to iboga alkaloids. It converts "α3β4 is a plausible target" into "α3β4 is causally implicated in opioid dependence/withdrawal."

### F006 — Selective α3β4 antagonist AT-1001 generalizes via a non-mesolimbic route — but opioid self-administration untested (SUPPORTS with GAP)

Toll et al. 2012 ([PMID:22278092](https://pubmed.ncbi.nlm.nih.gov/22278092/)) characterized AT-1001, a high-affinity (Ki < 10 nM), selective α3β4 antagonist (>90-fold over α4β2/α7), which *"potently and dose-dependently blocks nicotine self-administration in rats, without affecting food responding,"* and *"inhibits nicotine-induced [³H]dopamine release poorly and at significantly higher concentrations compared with mecamylamine and conotoxin MII"* — implying an **indirect, non-mesolimbic** locus consistent with a habenular site. AT-1001/AT-1012 also attenuate cocaine CPP and sensitization ([PMID:26256075](https://pubmed.ncbi.nlm.nih.gov/26256075/)), and AT-1001 reduces alcohol seeking under yohimbine stress ([PMID:25689019](https://pubmed.ncbi.nlm.nih.gov/25689019/)). **A dedicated opioid self-administration study with AT-1001 was not found** — a concrete, tractable gap.

### F007 — Within-drug competing mechanism: ibogaine's anti-opioid effect attributed to kappa/NMDA, and ibogaine is NOT reinforcer-selective (COMPETING)

This is the finding that most limits transfer of the model to ibogaine. Glick & Maisonneuve 1998 ([PMID:9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/)) concluded that *"kappa agonist and NMDA antagonist actions contribute to ibogaine's effects on opioid and stimulant self-administration."* Glick et al. 2000 ([PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/)) noted that *"unlike ibogaine, 18-MC does not affect responding for a nondrug reinforcer (water)"* — meaning **ibogaine DOES suppress a non-drug reinforcer** — and that *"18-MC has much lower affinities than ibogaine for NMDA and sigma-2 receptors, sodium channels, and the 5-HT transporter,"* while both share similar kappa and nicotinic affinities. The model's signature reinforcer-selectivity is thus a property of 18-MC, not ibogaine; and the parent lab's own attribution of ibogaine's anti-opioid effect points away from α3β4 toward kappa/NMDA.

### F008 — Both ibogaine and 18-MC reduce morphine SA and block accumbal dopamine; 18-MC lowers reinforcing efficacy (SUPPORTS phenotype)

Maisonneuve & Glick 1999 ([PMID:10556676](https://pubmed.ncbi.nlm.nih.gov/10556676/)) showed 18-MC produced *"a downward shift in the entire morphine dose-response curve without any displacement to the left or right"* — reducing reinforcing *efficacy* without altering potency, exactly the behavioral phenotype the model claims to explain. Glick et al. 2000 ([PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/)) confirmed *"Both ibogaine and 18-MC block morphine-induced and nicotine-induced dopamine release in the nucleus accumbens."* The downstream dopaminergic phenomenon is robust for both compounds; the dispute is over the upstream molecular cause.

### F009 — Source/data absence: no human clinical efficacy trial of 18-MC for OUD (DATA GAP)

Systematic PubMed searches returned **zero** human 18-MC efficacy or phase-1 addiction trials. The only recent human-facing 18-MC work ([PMID:42038284](https://pubmed.ncbi.nlm.nih.gov/42038284/)) targets **leishmaniasis**, reporting a *"safety profile compatible with first-in-human evaluation"* for that unrelated indication. The model's clinical arm is therefore an explicit, curation-relevant data absence as of August 2026.

---

## Mechanistic Model / Interpretation

### The causal chain implied by the hypothesis

```
 Iboga alkaloid (18-MC / ibogaine)
            │
            ▼  [STRONG in vitro: PMID 26022277]
 Non-competitive block of α3β4 nAChRs
            │
            ▼  [STRONG anatomy: receptors enriched in MHb & IPN, sparse in mesolimbic]
 Reduced α3β4 signalling in medial habenula / interpeduncular nucleus
            │
            ▼  [STRONG for 18-MC: PMID 16626688, 17447255 — intra-MHb/IPN works, intra-VTA does not]
 Damped habenulo-interpeduncular modulation of mesolimbic DA
            │
            ▼  [STRONG for 18-MC: blocks SENSITIZED (not acute) accumbal DA to repeated morphine]
 Reduced sensitized dopamine response in nucleus accumbens
            │
            ▼  [STRONG phenotype: PMID 10556676 downward DR-curve shift; reinforcer-selective for 18-MC]
 Reduced reinforcing efficacy of morphine → ↓ opioid self-administration
            │
            ▼  [ABSENT: no human 18-MC OUD trial — PMID 42038284 only leishmaniasis]
 Reduced opioid use / relapse in patients   ◀── UNTESTED IN HUMANS
```

### Where the literature is strong vs. inferred vs. missing

| Causal link | Evidence status | Key support / challenge |
|---|---|---|
| Iboga alkaloids block α3β4 non-competitively | **Established** | [PMID:26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/) — but noribogaine weakest |
| α3β4 causally involved in opioid dependence/withdrawal | **Established** | [PMID:24750073](https://pubmed.ncbi.nlm.nih.gov/24750073/), [PMID:20485328](https://pubmed.ncbi.nlm.nih.gov/20485328/) (human + mouse) |
| Site of action = MHb/IPN, not VTA (**for 18-MC**) | **Established for 18-MC** | [PMID:16626688](https://pubmed.ncbi.nlm.nih.gov/16626688/), [PMID:17447255](https://pubmed.ncbi.nlm.nih.gov/17447255/) |
| Effect restricted to *sensitized* accumbal DA | **Established for 18-MC** | [PMID:17447255](https://pubmed.ncbi.nlm.nih.gov/17447255/) |
| Reinforcer-selective (spares non-drug reward) | **True for 18-MC, FALSE for ibogaine** | [PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/) |
| Same site of action = ibogaine | **Inferred / contradicted** | Ibogaine acts via VTA-GDNF ([PMID:15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/)) and kappa/NMDA ([PMID:9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/)) |
| Habenular locus drives opioid aversion/withdrawal | **Established, but via MOR** | [PMID:31005059](https://pubmed.ncbi.nlm.nih.gov/31005059/), [PMID:42217817](https://pubmed.ncbi.nlm.nih.gov/42217817/) |
| Translates to human OUD efficacy | **Missing** | No trial; [PMID:42038284](https://pubmed.ncbi.nlm.nih.gov/42038284/) only leishmaniasis |

**Synthesis.** The model is internally coherent and, for **18-MC**, well-supported at every preclinical link from receptor to behavior. Its weakness is entirely at the *identity* of the active agent and the *transfer to ibogaine*. Ibogaine and its metabolite noribogaine reach the same behavioral endpoint (↓ morphine self-administration, ↓ accumbal dopamine) but appear to do so through at least two additional, better-supported routes for those specific molecules: (1) VTA-localized GDNF neurotrophic remodelling, and (2) kappa-opioid agonism + NMDA antagonism. These are **not mutually exclusive** with the nicotinic route and may operate on different time courses — nicotinic blockade during drug exposure, neurotrophic remodelling accounting for persistence — but the seed hypothesis is, on current evidence, most accurately labeled a **model of 18-MC's anti-opioid action**, not ibogaine's.

---

## Evidence Matrix

| Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Context/subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| [16626688](https://pubmed.ncbi.nlm.nih.gov/16626688/) | Model organism (rat) | **Supports** | Site of 18-MC anti-morphine effect = MHb/IPN not VTA | Intra-MHb/IPN ↓ morphine SA, spares sucrose; intra-VTA no effect | Morphine SA, established exposure | High for 18-MC; single lab; no ibogaine arm |
| [17447255](https://pubmed.ncbi.nlm.nih.gov/17447255/) | Model organism (rat) | **Supports** | 18-MC blocks sensitized (not acute) accumbal DA | Intra-MHb/IPN blocks sensitized DA; no effect on acute | Repeated morphine sensitization | High for 18-MC; congener-specific |
| [26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/) | In vitro (human nAChR) | **Qualifies** | Non-competitive α3β4 block; potency order | Noribogaine (6.82 µM) ≫ weaker than ibogaine (0.95) / 18-MC (1.47) | Receptor pharmacology | High; metabolite is weakest blocker |
| [21040239](https://pubmed.ncbi.nlm.nih.gov/21040239/) | Model organism (rat) + cell | **Competing/limits** | Noribogaine vs 18-MC mechanism | Noribogaine (not 18-MC) → GDNF + intra-VTA effect | Ethanol SA; extrapolated | High; dissociates congeners |
| [15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/) | Model organism (rat) | **Competing** | Ibogaine acts via VTA-GDNF | Intra-VTA (not SN) ibogaine ↓ ethanol SA; GDNF-dependent | Alcohol; ibogaine parent | High for alcohol; opioid extrapolation |
| [18541917](https://pubmed.ncbi.nlm.nih.gov/18541917/) | Model organism (rat) | **Competing** | VTA-GDNF sufficient, MAPK-dependent | Intra-VTA GDNF rapidly ↓ ethanol SA & relapse | Alcohol | High; not opioid-tested |
| [24750073](https://pubmed.ncbi.nlm.nih.gov/24750073/) | Human genetic + mouse | **Supports (receptor)** | α3β4* causally mediates morphine dependence | KO/overexpression + AuIB/AT-1001 modulate withdrawal; CHRNA3 protective in humans | Morphine dependence/withdrawal | High; generalizes beyond iboga |
| [20485328](https://pubmed.ncbi.nlm.nih.gov/20485328/) | Human genetic | **Supports (receptor)** | CHRNA5/A3/B4 cluster ↔ opioid dependence | 15q25 variants associated with opioid dependence | Human OUD/polysubstance | Moderate; association not causal |
| [22278092](https://pubmed.ncbi.nlm.nih.gov/22278092/) | Model organism (rat) | **Supports (indirect)** | Selective α3β4 antagonism, non-mesolimbic locus | AT-1001 ↓ nicotine SA, spares food; poor NAc DA inhibition | Nicotine SA | High for nicotine; **opioid SA untested** |
| [26256075](https://pubmed.ncbi.nlm.nih.gov/26256075/) | Model organism (mouse) | **Supports (generalizes)** | α3β4 antagonists affect drug reward | AT-1001/1012 ↓ cocaine CPP & sensitization | Cocaine | Moderate; not opioid |
| [9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/) | Model organism (rat) review | **Competing** | Ibogaine anti-opioid effect = kappa/NMDA | Kappa agonism + NMDA antagonism drive ibogaine's SA effects | Opioid/stimulant SA | High; from originating lab |
| [11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/) | Model organism (rat) | **Competing/qualifies** | Ibogaine vs 18-MC selectivity & targets | Ibogaine (not 18-MC) suppresses non-drug reinforcer; differing receptor affinities | Morphine/nicotine | High; undermines selectivity transfer |
| [10556676](https://pubmed.ncbi.nlm.nih.gov/10556676/) | Model organism (rat) | **Supports (phenotype)** | 18-MC lowers reinforcing efficacy | Downward shift of morphine dose-response curve | Morphine SA | High; behavioral endpoint |
| [31005059](https://pubmed.ncbi.nlm.nih.gov/31005059/) | Model organism (mouse) | **Parallel/competing** | Habenular locus of opioid aversion | MHb β4-neuron MOR deletion ↓ naloxone aversion/withdrawal | Opioid withdrawal | High; MOR not α3β4 channel |
| [42217817](https://pubmed.ncbi.nlm.nih.gov/42217817/) | Model organism (mouse) | **Parallel/competing** | Hb-MOR neurons drive withdrawal | Silencing Hb-MOR neurons abolishes aversion, eases withdrawal | Opioid withdrawal | High; MOR-centric |
| [39270652](https://pubmed.ncbi.nlm.nih.gov/39270652/) | Model organism (mouse) | **Parallel** | IPN→NI circuit amplifies aversion | IPN(GABA)→nucleus incertus amplifies opioid-withdrawal aversion | Opioid withdrawal/relapse | Moderate; circuit-level |
| [42038284](https://pubmed.ncbi.nlm.nih.gov/42038284/) | Translational (primate/rodent) | **Data absence** | 18-MC human readiness (wrong indication) | 18-MC PK/safety "compatible with first-in-human" — for leishmaniasis | Not OUD | Confirms no OUD trial |
| [42117212](https://pubmed.ncbi.nlm.nih.gov/42117212/) | Review (human RCTs) | **Context** | Ibogaine/noribogaine clinical status | Only 3 RCTs; noribogaine QTc prolongation, non-significant withdrawal reduction | Human OUD/cocaine | Review-level; no α3β4 evidence |

---

## Knowledge Gaps

**G1 — No intra-habenular or intra-VTA infusion of ibogaine (the decisive dissociation).**
*Scope:* The single test that would separate the α3β4-habenular model from the GDNF-VTA model for ibogaine itself. *Why it matters:* All habenular localization uses 18-MC; all VTA/GDNF localization uses ibogaine/noribogaine. The models predict opposite outcomes. *What was checked:* Literature search found no intra-MHb/IPN ibogaine self-administration study. *Resolution:* Intracerebral ibogaine into MHb/IPN vs VTA in a morphine SA paradigm.

**G2 — No opioid self-administration study with a selective α3β4 antagonist (AT-1001).**
*Scope:* AT-1001 reproduces reinforcer-selective suppression for nicotine and cocaine, and attenuates morphine *withdrawal*, but was never tested on **opioid self-administration**. *Why it matters:* Would confirm the α3β4-mediated behavioral effect using a tool free of iboga confounds. *What was checked:* Searches for AT-1001 + opioid/morphine self-administration returned none. *Resolution:* AT-1001 dose-response on morphine/heroin SA with a food control.

**G3 — Habenular α3β4 channel block vs MOR: which drives the effect?**
*Scope:* Boulos 2020 and Ozdemir 2026 show MHb MOR (on β4-defined neurons) drives opioid withdrawal/aversion. *Why it matters:* 18-MC's habenular effect may act through, or converge on, MOR-expressing circuitry rather than pure α3β4 antagonism. *What was checked:* Two independent circuit studies. *Resolution:* Test 18-MC in MHb-MOR conditional-KO mice; if the effect persists, α3β4 is the driver.

**G4 — Noribogaine potency mismatch.**
*Scope:* Noribogaine is the weakest α3β4 blocker (6.82 µM) yet dominates ibogaine's late pharmacokinetics. *Why it matters:* If the anti-opioid effect persists after ibogaine clears (when noribogaine predominates), α3β4 block is an unlikely sole mechanism. *What was checked:* [PMID:26022277](https://pubmed.ncbi.nlm.nih.gov/26022277/) potency series. *Resolution:* Correlate time course of anti-opioid effect with noribogaine plasma/brain levels and α3β4 occupancy.

**G5 — No human clinical efficacy trial of 18-MC or a selective α3β4 antagonist for OUD.**
*Scope:* Source/data absence as of Aug 2026. *Why it matters:* The clinical arm of the causal chain is untested; existing human ibogaine/noribogaine RCTs cannot isolate α3β4. *What was checked:* PubMed for 18-MC human trials returned only a leishmaniasis study ([PMID:42038284](https://pubmed.ncbi.nlm.nih.gov/42038284/)). *Resolution:* Phase-1/2 OUD trial of an α3β4-selective agent.

**G6 — Ibogaine reinforcer non-selectivity is unexplained mechanistically.**
*Scope:* Ibogaine suppresses non-drug reinforcers; 18-MC does not. *Why it matters:* Suggests ibogaine's additional NMDA/sigma/5-HT actions add non-selective suppression not captured by the model. *What was checked:* [PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/). *Resolution:* Component-resolution studies pairing selective antagonists.

---

## Alternative Models

1. **GDNF / VTA neurotrophic remodelling (competing, and the primary alternative for ibogaine).** Ibogaine and noribogaine induce GDNF and act in the VTA to reduce drug self-administration; 18-MC does neither ([PMID:15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/), [PMID:18541917](https://pubmed.ncbi.nlm.nih.gov/18541917/), [PMID:21040239](https://pubmed.ncbi.nlm.nih.gov/21040239/)). This is a *parallel-and-competing* mechanism operating at a different anatomical site, plausibly accounting for the **persistence** of ibogaine's effects, while nicotinic blockade would act **during** drug exposure. Not mutually exclusive with the seed model, but better supported for ibogaine specifically.

2. **Kappa-opioid agonism + NMDA antagonism (within-drug competing).** The originating lab attributes ibogaine's anti-opioid self-administration effect to these actions, which 18-MC largely lacks ([PMID:9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/), [PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/)). A direct alternative to α3β4 for the parent compound.

3. **Habenular MOR circuit (parallel).** MHb/Hb MOR neurons causally drive opioid withdrawal and aversion ([PMID:31005059](https://pubmed.ncbi.nlm.nih.gov/31005059/), [PMID:42217817](https://pubmed.ncbi.nlm.nih.gov/42217817/)); an IPN→nucleus incertus circuit amplifies withdrawal aversion ([PMID:39270652](https://pubmed.ncbi.nlm.nih.gov/39270652/)). Same anatomy, different molecular driver — potentially convergent with the α3β4 effect.

4. **5-HT2A psychoplastogen route (parallel, for next-generation analogues).** Non-hallucinogenic ibogaine analogues (e.g., tabernanthalog) show anti-addictive effects attributed to psychoplasticity ([PMID:33299186](https://pubmed.ncbi.nlm.nih.gov/33299186/)), an alternative for the analogue class rather than the seed compound.

---

## Discriminating Tests

| Test | Design | Expected under α3β4-habenular model | Expected under competing model |
|---|---|---|---|
| **Intracerebral ibogaine dissociation** | Infuse ibogaine into MHb/IPN vs VTA; measure morphine SA | Intra-MHb/IPN suffices; VTA no effect | Intra-VTA suffices (GDNF); MHb/IPN no effect |
| **AT-1001 on opioid SA** | Selective α3β4 antagonist dose-response on heroin/morphine SA + food control | Reinforcer-selective ↓ opioid SA | No effect if habenular α3β4 not sufficient for opioids |
| **18-MC in MHb-MOR cKO** | 18-MC anti-morphine effect in β4-neuron MOR knockouts | Effect persists (α3β4-driven) | Effect lost (MOR-convergent) |
| **Time-course vs noribogaine** | Correlate persistence of anti-opioid effect with noribogaine levels & α3β4 occupancy | Effect tracks α3β4 occupancy | Effect outlasts occupancy → GDNF/remodelling |
| **Human trial** | Phase-1/2 OUD trial of α3β4-selective agent | ↓ craving/withdrawal without QTc risk | Null → mechanism not clinically sufficient |

---

## Curation Leads (require curator verification)

- **Status:** Retain **EMERGING**. Add an explicit annotation: *"In vivo evidence is congener-specific to 18-MC; transfer to ibogaine is inferred, not demonstrated, and is contested by kappa/NMDA and GDNF/VTA models."*
- **Candidate supporting evidence (verify snippets):**
  - [PMID:24750073](https://pubmed.ncbi.nlm.nih.gov/24750073/) — *"selective α3β4* nACh receptor antagonists, α-conotoxin AuIB and AT-1001, attenuated somatic signs of morphine withdrawal in a dose-related manner"* + *"two human datasets revealed a protective role for variants in the CHRNA3 gene... in opioid dependence and withdrawal."* (Human + mouse causal support for the receptor premise.)
  - [PMID:20485328](https://pubmed.ncbi.nlm.nih.gov/20485328/) — human association of CHRNA5/A3/B4 with opioid dependence.
  - [PMID:22278092](https://pubmed.ncbi.nlm.nih.gov/22278092/) — selective α3β4 antagonist, reinforcer-selective, non-mesolimbic locus.
  - [PMID:10556676](https://pubmed.ncbi.nlm.nih.gov/10556676/) — *"downward shift in the entire morphine dose-response curve"* (reinforcing-efficacy phenotype).
- **Candidate competing/qualifying evidence:**
  - [PMID:9668680](https://pubmed.ncbi.nlm.nih.gov/9668680/) — kappa/NMDA attribution for ibogaine.
  - [PMID:11085336](https://pubmed.ncbi.nlm.nih.gov/11085336/) — ibogaine not reinforcer-selective.
  - [PMID:15659598](https://pubmed.ncbi.nlm.nih.gov/15659598/), [PMID:18541917](https://pubmed.ncbi.nlm.nih.gov/18541917/) — GDNF/VTA competing route.
  - [PMID:31005059](https://pubmed.ncbi.nlm.nih.gov/31005059/), [PMID:42217817](https://pubmed.ncbi.nlm.nih.gov/42217817/) — habenular MOR parallel mechanism.
- **Candidate pathophysiology nodes/edges:** `MHb α3β4 nAChR → habenulo-interpeduncular signalling → sensitized NAc dopamine → opioid reinforcing efficacy`; add competing edges `VTA GDNF → mesolimbic remodelling` and `MHb MOR neuron → opioid withdrawal/aversion`.
- **Candidate ontology terms:** medial habenula (UBERON:0001905), interpeduncular nucleus (UBERON:0002743), CHRNA3/CHRNB4/CHRNA5, nucleus accumbens (UBERON:0001882), ventral tegmental area (UBERON:0001943); processes: nicotinic acetylcholine receptor signalling, behavioral response to opioids, dopamine secretion.
- **Candidate knowledge_gaps entries:** (a) no intra-habenular ibogaine dissociation; (b) no opioid SA test with a selective α3β4 antagonist; (c) noribogaine potency mismatch; (d) no human 18-MC/α3β4 OUD trial (source absence, Aug 2026); (e) unresolved α3β4-channel-vs-habenular-MOR causal driver.

---

## Limitations

- Nearly all site-specific in vivo evidence originates from a **single laboratory** (Glick/Maisonneuve) and uses **18-MC**, not ibogaine.
- Several supporting studies use **nicotine, cocaine, or alcohol** self-administration and extrapolate to opioids.
- Human evidence for the receptor is **genetic-association** level; no human interventional data isolate α3β4.
- The competing GDNF and MOR mechanisms are strongly supported for **alcohol** and **withdrawal** respectively, and their opioid-self-administration relevance is partly inferred.

---

## Proposed Follow-up Experiments / Actions

1. **Run the decisive intracerebral ibogaine dissociation (G1):** intra-MHb/IPN vs intra-VTA ibogaine in rat morphine self-administration. Directly adjudicates seed vs GDNF model for the parent compound.
2. **Test AT-1001 (and α-conotoxin AuIB) on opioid self-administration (G2):** close the single largest tool gap; a positive, reinforcer-selective result would establish the α3β4 behavioral effect independent of iboga chemistry.
3. **Dissect α3β4-channel vs habenular-MOR (G3):** apply 18-MC in MHb-MOR conditional knockouts to determine whether the anti-morphine effect survives loss of MOR.
4. **Pharmacokinetic-behavioral coupling (G4):** correlate the persistence of the anti-opioid effect with noribogaine brain levels and estimated α3β4 occupancy to test whether the weak-blocker metabolite can plausibly carry the effect.
5. **Advance a clinical arm (G5):** given the absence of any human 18-MC/α3β4 OUD trial, prioritize a phase-1/2 study of an α3β4-selective, non-cardiotoxic agent, with CYP2D6 genotyping and QTc monitoring informed by the ibogaine cardiac-safety literature.
6. **Curation action:** keep status EMERGING, annotate as congener-specific to 18-MC, and register the five knowledge gaps above as explicit `knowledge_gaps` entries.

---

*Report generated from 5 completed iterations, 9 verified findings, and 41 reviewed papers.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)