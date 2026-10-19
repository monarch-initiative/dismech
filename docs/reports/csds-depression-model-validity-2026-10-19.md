# Chronic social defeat stress as a model of major depressive disorder

Written 2026-10-19 for issue
[#14274](https://github.com/monarch-initiative/dismech/issues/14274), area 3 of
[#13754](https://github.com/monarch-initiative/dismech/issues/13754). It answers
the four questions that issue asks about chronic social defeat stress (CSDS)
and recommends how a CSDS model record should be linked into
`kb/disorders/Major_Depressive_Disorder.yaml`.

No model record is added here. `AnimalModel` cannot yet record a procedure
applied to a wild-type animal; that waits on
[#13768](https://github.com/monarch-initiative/dismech/issues/13768).

**Sources.** Two passes were combined: a reading of the leads named in the
issue and the standard CSDS papers, and an OpenScientist deep-research report
(`research/model_validity/Major_Depressive_Disorder-model-validity-chronic_social_defeat_stress-deep-research-openscientist.md`).
Every quotation below is an exact substring of the cached file
`references_cache/PMID_<id>.md` for the PMID that follows it. Most caches hold
only the abstract; the table at the end says which.

## Summary

- **CSDS models stress-induced social avoidance and anhedonia-like behaviour,
  not depressed mood.** Its strongest validity argument is pharmacological:
  social avoidance reverses with chronic but not acute antidepressants, and
  within a day with ketamine or psilocybin. Its construct validity is disputed:
  both susceptible and resilient mice become anxious, several sources say the
  paradigm models PTSD as much as depression, and one review of 318 reports
  says the protocol has limited ecological validity.
- **The susceptible/resilient split is presented as a model of human
  vulnerability, but no source tests it as one in people.** What has been
  tested is narrower: six molecules or programs that mark susceptible mice are
  also altered in patients with MDD compared with controls.
- **CSDS findings bear on ten of the twelve mechanism nodes, but often in a
  different direction or form from the node.** The monoamine findings do not
  fit the Monoamine Deficiency node (they are mixed in direction, and VTA
  dopamine firing increases), the enkephalin finding runs opposite to the PENK+
  interneuron node, and the neurogenesis suppression is transient rather than
  stalled.
  There is no CSDS evidence for Reference Point Dysregulation or Neurogenic
  Niche Interferon Signaling Activation.
- **The blood-brain barrier finding is the strongest case for a new node**:
  it is specific to susceptible mice and has the same change in patient
  postmortem tissue. Circuit findings, including the lateral habenula, are
  better recorded as a knowledge gap for now.
- **Standard CSDS cannot be run in females**, and 95% of 318 reviewed defeat
  reports studied males. Four female adaptations exist and disagree about
  whether the female phenotype matches the male one.

## 1. What CSDS models, and what it does not

**Protocol.** An experimental C57BL/6J mouse is defeated daily by a larger
aggressor: "C57BL/6J mice that are repeatedly subjected to bouts of social
defeat by a larger and aggressive CD-1 mouse results in the development of a
clear depressive-like syndrome, characterized by enduring deficits in social
interactions" (PMID:21799487). "This sequence is repeated for 10 days, with a
novel opponent each day" (PMID:31584111). The primary readout is a ratio of
time spent near a caged novel mouse: "The social interaction ratio (SI ratio)
is obtained by dividing the time spent in the interaction zone when the target
is present by the time spent in the interaction zone when the target is
absent" (PMID:21799487).

**Face validity.** Reviews list several readouts that resemble human symptoms:
"Defeat produces specific behaviors resembling the signs and symptoms of humans
with affective disorders, such as anhedonia, social avoidance, despair and
anxiety" (PMID:26475995). One review calls it "an ethologically valid rodent
model that exhibits long-term physiological and behavioral phenotypes similar
to depression and anxiety" (PMID:33090813).

Different readouts depend on different mechanisms, so "depression-like" is not
one phenotype. Prefrontal NPAS4 "is required in this brain region for
CSDS-induced changes in sucrose preference and natural reward motivation in
the mice", but "NPAS4 is not required for CSDS-induced social avoidance or
anxiety-like behavior" (PMID:36780219).

**Construct validity.** The argument is that social stress is a cause of human
depression, and that the mouse response depends on reward-circuit plasticity:
"BDNF is required for the development of this experience-dependent social
aversion" (PMID:16469931). Hammels and colleagues claim "the social defeat
paradigm has been shown to have etiological, predictive and face validity"
(PMID:26475995). Lyons and colleagues, reviewing 318 reports, dispute the
ecological part of that claim: "Elements of limited ecological validity include
frequent and repeated exposure to defeat stressors without opportunities to
avoid or escape from unfamiliar conspecifics that are pre-screened and selected
for aggressive behavior" (PMID:36608919).

**Predictive validity** is the model's strongest claim:

- "Mice experiencing repeated aggression develop a long-lasting aversion to
  social contact, which can be normalized by chronic, but not acute,
  administration of antidepressant" (PMID:16469931). The protocol paper calls
  this "a pharmacological validity not often seen in other stress models that
  tend to respond equally to both acute and chronic antidepressant treatments"
  (PMID:21799487).
- The model separates slow from rapid-acting drugs: "Fluoxetine showed no
  significant effects 24 h after a single dose or following 7 days of repeated
  administration; antidepressant-like effects only appeared after 14 days of
  continuous treatment. In contrast, a single dose of either ketamine or
  psilocybin significantly reversed social avoidance behavior at 24 h"
  (PMID:41290975).
- Ketamine's effect is partial: "High, but not low, doses of ketamine
  administered after completion of the CSDS regimen attenuated social avoidance
  in defeated mice, although this effect was transient" (PMID:24495460), and
  "acute administration of ketamine fails to attenuate CSDS-induced anhedonia
  despite reducing other depression-related behavioral abnormalities"
  (PMID:24495460).
- Only some susceptible mice respond, as in patients: "Each treatment reversed
  social interaction deficits in approximately 50% of susceptible mice—similar
  to previous studies" (PMID:27569543).

**What is disputed, and by whom.**

- *Anxiety rather than depression.* Donahue and colleagues report the competing
  reading: "it has been proposed that CSDS-triggered behaviors have their basis
  in anxiety (17,18), and what is often interpreted as anhedonia in sucrose
  preference tests may actually reflect anxiety-enhanced neophobia"
  (PMID:24495460). The protocol paper itself reports that anxiety does not
  separate the groups: "both susceptible and resilient mice show increased
  anxiety-like behavior, as measured by the elevated plus maze, stress-induced
  polydipsia and increased corticosterone release in response to a swim
  stress" (PMID:21799487).
- *PTSD and other disorders.* Hammels and colleagues say the defeat model "may
  mimic cardinal features of a multitude of psychiatric disorders including
  depression, post-traumatic stress disorder and schizophrenia"
  (PMID:26475995). Browne and colleagues point out that the drug response used
  as predictive validity for depression fits PTSD just as well: avoidance "can
  be reversed by 28 days of treatment with selective serotonin reuptake
  inhibitors, the only pharmaceutical class approved by the U.S. Food and Drug
  Administration for treating post-traumatic stress disorder" (PMID:29020387).
- *Readouts.* Donahue and colleagues note that "In many behavioral assays, it
  can be difficult to determine if these adaptations reflect core signs of
  depression" (PMID:24495460). CSDS studies often add the forced swim test,
  which Molendijk and de Kloet reject as a depression readout: "The forced swim
  test (FST) for rodents does not model despair or helplessness"
  (PMID:30738104). Commons and colleagues agree independently: "The FST provides
  little construct- or face-validity to support an interpretation as
  "depression-like" behavior" (PMID:28287253).
- *Symptoms no rodent model can show.* Planchez and colleagues, writing about
  rodent models in general: "some symptoms observed in humans, such as feelings
  of worthlessness or excessive guilt or recurrent thoughts of death, suicidal
  ideation or a suicide attempt cannot be observed in animals such as rodents"
  (PMID:31584111).

No source found critiques the social interaction ratio itself as a readout.
The disputes are about what the behaviour means, not whether it is measured
reliably.

**A misattribution risk.** Planchez and colleagues write that a model "mimics a
trauma, and therefore, it should instead be considered as a model of
post-traumatic stress disorder" (PMID:31584111). That sentence is about the
predator-exposure model, not CSDS, and should not be cited for CSDS.

## 2. Susceptible versus resilient

**Origin and framing.** Krishnan and colleagues introduced the split: "an
inbred population of mice subjected to social defeat can be separated into
susceptible and unsusceptible subpopulations" (PMID:17956738). They frame it
through human resilience: "most individuals exposed to adversity maintain
normal psychological functioning" (PMID:17956738). Wang and colleagues say CSDS
"can imitate individual differences in stress responses in humans"
(PMID:33090813).

So the split is presented as a model of human vulnerability. **None of the
sources tests it as one.** Every human comparison found compares patients who
already have MDD with controls. None follows people before illness to ask
whether a susceptibility marker predicts who becomes ill.

**Tested in human tissue or blood (patient versus control):**

| Susceptible-mouse finding | Human finding | Source |
|---|---|---|
| "IL-6 was most highly up-regulated only in mice that ultimately developed a susceptible behavioral phenotype" | "We confirmed a similar elevation of serum IL-6 in two separate cohorts of patients with treatment-resistant major depressive disorder." | PMID:25331895 |
| "reduced expression of the endothelial cell tight junction protein claudin-5 (Cldn5) and abnormal blood vessel morphology in nucleus accumbens (NAc) of stress-susceptible but not resilient mice" | "CLDN5 expression was also decreased in NAc of depressed patients." | PMID:29184215 |
| "a sustained reduction in RAS-related C3 botulinum toxin substrate 1 (Rac1) expression after chronic social defeat stress" | "We found a similar repressive chromatin state surrounding the RAC1 promoter in the NAc of subjects with depression, which corresponded with reduced RAC1 transcription." | PMID:23416703 |
| Prefrontal oligodendrocyte loss and hypomyelination after repeated defeat | "Analysis of single-nucleus transcriptomic data from MDD patients revealed oligodendroglial-lineage dysregulation and the presence of immune-oligodendrocytes (Im-OL)"; "Im-OL were also identified in mice after RSDS" | PMID:35301426 |
| Serum ULK1 in susceptible mice | "serum ULK1 levels are decreased in both patients with depression and mice susceptible to chronic social-defeat stress" | PMID:42714059 |
| Transcriptional networks in prefrontal cortex and nucleus accumbens | "chronic social defeat stress and adult social isolation better reproduce gene networks characteristic of human MDD" | PMID:32169281 |

The transcriptional overlap holds at the network level but is weak gene by
gene: Scarpa and colleagues report overlap of "5.2% in CSDS susceptible mice
(18/344; 16 common, 2 opposite)" in one comparison (PMID:32169281). Bagot and
colleagues compare their CSDS gene modules with published human lists after
the fact, which is weaker still: "we see overlap between MB genes and those
identified as showing altered expression in depressed humans" (PMID:27181059).

**Proposed for humans, tested only in mice:**

- Hodes and colleagues found "individual differences in IL-6 levels from ex
  vivo stimulated leukocytes that predict susceptibility versus resilience to a
  subsequent stressor" (PMID:25331895). The prediction before stress was shown
  in mice only.
- Hultman and colleagues found an electrical network that "is also enhanced in
  three independent models of MDD vulnerability" and "is biologically distinct
  from the networks that encode dysfunction after stress" (PMID:29502969). The
  cohort is male mice, and no human data were collected.

**Recommendation.** Treat the claim that the split models human vulnerability
as a proposal. Record it as a `HUMAN_MODEL_MISMATCH` discussion rather than as
fidelity on a model link: the mouse evidence exists, and its translation to
people is what is open. A prospective human study that measures one of the
markers above before illness would settle it.

## 3. Which MDD mechanism nodes CSDS findings bear on

| Node | CSDS finding | Fit to the node | Human link | Source |
|---|---|---|---|---|
| Neuroinflammation | Peripheral IL-6 rises in susceptible mice; claudin-5 loss is "promoting peripheral IL-6 passage across the BBB and depression" | Same direction; susceptible only | Serum IL-6, NAc CLDN5 | PMID:25331895, PMID:29184215 |
| Stress-Responsive Transcription Factor Reprogramming | "ΔFosB is selectively induced in D1-MSNs in the NAc of resilient mice, and in D2-MSNs of susceptible mice" | Fits, but the same factor marks resilience or susceptibility by cell type | Network overlap | PMID:28462942, PMID:24623766, PMID:27181059, PMID:32169281 |
| Neuroplasticity Deficits | Rac1 falls in the NAc after CSDS; across chronic stress models generally, spines are lost in hippocampus and prefrontal cortex but gained in amygdala and NAc | Region-dependent; mesolimbic BDNF *promotes* susceptibility, opposite to the node's deficit framing | NAc RAC1 | PMID:23416703, PMID:26881133, PMID:16469931 |
| Oligodendrocyte Dysfunction and Demyelination | "severe hypomyelination in the prefrontal cortex" | Same direction; microglia act upstream | Patient Im-OL | PMID:35301426, PMID:39719686 |
| Mitochondrial Dysfunction | "alterations of mitochondrial functions are common between human MDD and every mouse model in both mPFC and NAc" | Direction not given; the female NAc proteome reports reduced oxidative phosphorylation proteins | Shared with patient tissue | PMID:32169281, PMID:42614171 |
| HPA Axis Dysregulation | "All stressed animals, regardless of the coping strategy, presented higher plasma corticosterone levels" (18-day defeat in OF1 mice); in standard CSDS, swim-stress corticosterone rises in both susceptible and resilient mice; mice split by active versus passive coping show "marked phenotype-dependent differences in glucocorticoid-responsive transcriptional programs" | Raised, but in resilient mice too, so it does not track the phenotype; glucocorticoid sensitivity differs by coping style | None | PMID:38688411, PMID:21799487, PMID:42511784 |
| Excitation-Inhibition Imbalance | Synaptic ratios in the prefrontal cortex change differently in susceptible and resilient mice, depending on IL-6 trans-signaling; ventral hippocampal parvalbumin interneuron activity promotes susceptibility | Fits, susceptibility-dependent | None | PMID:31301368, PMID:42593738 |
| Stalled Adult Hippocampal Neurogenesis | "Chronic stress, such as repeated social defeat, suppresses cell proliferation during and immediately after stress; however, this effect is transient" | Suppressed, not stalled | None | PMID:36030966, PMID:31542427 |
| Monoamine Deficiency | After an 18-day defeat variant in OF1 mice, prefrontal dopamine and 5-HIAA fall but serotonin rises, with no change in hippocampus; "Phasic firing of the neurons, which is well known to encode reward signals, is upregulated by repeated social-defeat stress" | Mixed direction; VTA dopamine firing *increases* in susceptible mice | None | PMID:38688411, PMID:23235832 |
| PENK+ GABAergic Interneuron Activation | "Compared to controls, susceptible animals showed reduced enkephalin levels in the NAc", while proenkephalin mRNA is unchanged | Opposite direction, and in NAc rather than in an interneuron population | None | PMID:31132785 |
| Reference Point Dysregulation | None found | — | — | — |
| Neurogenic Niche Interferon Signaling Activation | None found. The nearest evidence is from restraint stress, not CSDS, and shows *decreased* STING pathway components | No CSDS evidence | — | PMID:35470042 |

**Findings with no existing node:**

- **Blood-brain barrier / neurovascular integrity** (PMID:29184215). This is the
  strongest case for a new node: a mouse mechanism, a susceptible-only
  phenotype, and the same change in patient postmortem tissue. A
  cross-paradigm meta-analysis of six CSDS and chronic unpredictable stress
  datasets also finds "downregulation of glia/myelin and vascular pathways"
  in the prefrontal cortex (PMID:41566898). The MDD entry already names a
  neurovascular, blood-brain-barrier route in one discussion and a claudin-5
  readout in a proposed experiment, so a node would give those an anchor.
- **Circuit-level findings.** Three are reported:
  - In Hultman's network, "Activity patterns in this network originate in
    prefrontal cortex and ventral striatum, relay through amygdala and ventral
    tegmental area, and converge in ventral hippocampus" (PMID:29502969).
  - Chaudhury and colleagues found that "phasic activation of VTA neurons
    projecting to the nucleus accumbens (NAc), but not to the medial prefrontal
    cortex (mPFC), induced susceptibility" (PMID:23235832).
  - Li and Ning found "elevated spontaneous neuronal activity in the LHb,
    robust hyperconnectivity between the LHb and dorsal anterior cingulate
    cortex" in susceptible mice (PMID:42874279).

  The OpenScientist report proposes a lateral habenula node, citing serum ULK1
  as human support. This report does not recommend one yet. The habenula fMRI
  study is a single 2026 study in male mice, and serum ULK1 is a blood marker
  rather than a measure of habenula activity. Hultman's network is a
  vulnerability trait that its authors say is distinct from the disease state.
  A `KNOWLEDGE_GAP` discussion naming the circuit question fits better.
- **Glycemic shift** (PMID:42633587): "this stress-induced hyperglycemic
  response was abolished in C57BL/6N and C57BL/6J mice, whereas BALB/c mice
  showed stress-induced hypoglycemia". This is a single study comparing
  strains rather than susceptible and resilient mice. It does not warrant a
  node.

## 4. Sex

**Why standard CSDS fails in females.** "An important limitation of RSDS
studies to date is that they have been conducted exclusively in male mice due
to the difficulty of initiating attack behavior directed toward female mice"
(PMID:28993631). The protocol paper does not mention females (PMID:21799487).
The bias persists: "Most of the 318 reviewed reports (95%) focus on males"
(PMID:36608919).

**Adaptations, and how their results compare with males:**

| Method | Result compared with males | Source |
|---|---|---|
| Male odorants applied to females so male residents attack them | "This method produces comparable results to those obtained in male mice" | PMID:29090682 |
| Chemogenetic activation of the aggressor's ventromedial hypothalamus so it attacks females | "These patterns of behavioral abnormalities closely resemble susceptibility and resilience in male mice after RSDS" | PMID:28993631 |
| Aggressive female residents defeat female intruders | "significant features of the defeated female phenotype are distinct from males"; defeated females showed vigilance "though the duration of time spent in a predefined social interaction zone was comparable between groups" | PMID:31255250 |
| Females witness a male being defeated (vicarious stress) | Females develop reduced sucrose preference, which "appears to be sex dependent, since previous work suggests that ES-male c57BL/6 mice do not develop a decrease in preference for sucrose 24 h after VDS" | PMID:28888327 |
| Aggressive parous females defeat females (femCSDS) | Proteomic study; no male comparison | PMID:42614171 |

The adaptations disagree. The two that make males attack females report a
male-like phenotype. The female-aggressor model finds that time in the
interaction zone does not change, so a female cohort scored by the male
readout would look resilient. The vicarious model applies emotional rather
than physical stress, a different construct. Where the molecular response has
been compared, it differs: "there are sex-specific differences in peripheral
immune responses and differential gene regulation in the prefrontal cortex to
chronic stress and to the treatment" (PMID:32918293).

The femCSDS authors criticise the first two methods, which "relied on
artificial triggers like applying male urine to females or using optogenetic
stimulation which risk introducing confounding hormonal and sensory variables"
(PMID:42614171). (Takahashi and colleagues used chemogenetic, not optogenetic,
activation.) A systematic review argues against defeat for females altogether:
"social defeat stress model does not fit the social nature of females"
(PMID:30196085).

**Does it limit the model?** Yes, and several sources say so. "The risk of
developing stress related disorders such as depression is two times higher in
women than in men" (PMID:30196085). One review states that "a historical
weakness of rodent social stress models has been an under-representation of
studies in females" (PMID:34532840), and another that CSDS "is limited to the
study of male mice" (PMID:26881133). The human comparison in question 2 relies
on male CSDS cohorts: "Only our human and CVS cohorts included females. This
may, unfortunately, limit our interpretation of the data" (PMID:32169281). The
CSDS cohorts behind the blood-brain barrier, dopamine, network and habenula
findings above are male (PMID:29184215, PMID:23235832, PMID:29502969,
PMID:42874279).

## Recommendations for model records

These apply once #13768 gives `AnimalModel` a perturbation slot.

**One record for standard CSDS**, male C57BL/6J defeated by CD-1 aggressors,
with PMID:21799487 as the protocol reference:

| Target node | relationship | fidelity | Divergences beyond the defaults below |
|---|---|---|---|
| Neuroinflammation | `PARTIALLY_RECAPITULATES` | `MODERATE` | — |
| Oligodendrocyte Dysfunction and Demyelination | `PARTIALLY_RECAPITULATES` | `MODERATE` | — |
| Stress-Responsive Transcription Factor Reprogramming | `PARTIALLY_RECAPITULATES` | `MODERATE` | `CONTESTED_ASSUMPTION` (the node assumes one direction of reprogramming; ΔFosB marks resilience in D1 neurons and susceptibility in D2 neurons) |
| Neuroplasticity Deficits | `PARTIALLY_RECAPITULATES` | `LOW` | `CONTESTED_ASSUMPTION` (direction differs by region; mesolimbic BDNF promotes susceptibility) |
| Excitation-Inhibition Imbalance | `PARTIALLY_RECAPITULATES` | `LOW` | — |
| HPA Axis Dysregulation | `PARTIALLY_RECAPITULATES` | `LOW` | `CONTESTED_ASSUMPTION` (corticosterone rises in resilient mice too) |
| Stalled Adult Hippocampal Neurogenesis | `PARTIALLY_RECAPITULATES` | `LOW` | `TEMPORAL_SCOPE` (suppression is transient) |
| Mitochondrial Dysfunction | `MEASURES` | `LOW` | `PROXY_QUANTITY` (pathway overlap stands in for measured mitochondrial function) |

Every link should also carry four default divergences:

- `SPECIES_MISMATCH`: every finding is from mice, most of them from the
  standard C57BL/6J protocol.
- `PROXY_QUANTITY`: social avoidance and sucrose preference stand in for
  depressed mood and anhedonia.
- `CONTESTED_ASSUMPTION`: the anxiety and PTSD readings in question 1.
- `POPULATION_MISMATCH`: male-only cohorts.

Readouts should be the social interaction ratio and sucrose preference, not the
forced swim test.

**Do not link as `RECAPITULATES`:**

- Monoamine Deficiency: the changes are mixed in direction and VTA dopamine
  firing increases (PMID:38688411, PMID:23235832).
- PENK+ GABAergic Interneuron Activation: enkephalin falls in susceptible mice
  (PMID:31132785).

Either leave these out, or use `FAILS_TO_RECAPITULATE` with `limitations` and
evidence. Do not link Reference Point Dysregulation or Neurogenic Niche
Interferon Signaling Activation at all; there is no CSDS evidence for either.

**Female adaptations** should be separate records, one per method. They use
different aggressors and, in the female-aggressor model, a different readout,
so results from one do not stand in for another.

**New node.** Propose a blood-brain barrier / neurovascular integrity node
upstream of Neuroinflammation, citing PMID:29184215 for both the mouse and the
human postmortem findings. It needs its own curation PR with evidence and
causal edges.

**Discussions.**

- A `HUMAN_MODEL_MISMATCH` discussion on whether the susceptible/resilient split
  predicts human vulnerability (question 2).
- A `KNOWLEDGE_GAP` on circuit-level vulnerability, covering Hultman, Chaudhury
  and the lateral habenula.

## How the OpenScientist report was used

The report was generated with a new template,
`templates/disease_model_validity_research.md`, through the recipe
`just research-model-validity`. Its reference validation resolved all 30
references it cited, and every quotation it attributes to an abstract was
checked against the cache files written by that validation.
`just preflight-dr` returns SKIP for it, because MONDO records no causal gene
for MDD; the report is about CSDS and MDD throughout, so name confusion is not
a concern.

It added most of what this report says about the oligodendrocyte,
neurogenesis, PENK, excitation-inhibition and habenula findings, and the
ecological-validity and 95%-male census. Points where this report departs from
it:

- It treats PMID:35470042 as the interferon-node evidence. That study used
  restraint stress, not CSDS.
- It cites the bioRxiv preprint of the cross-paradigm meta-analysis
  (PMID:41278963). This report cites the published version (PMID:41566898).
- It recommends a lateral habenula node. This report recommends a knowledge
  gap instead, for the reasons in question 3.
- It says several mechanisms have been replicated "in human depressed
  postmortem tissue or patient blood". This report agrees, but notes that all
  of these are patient-versus-control comparisons and none tests the
  susceptible/resilient split itself.

## References

All are cached in `references_cache/`.

| PMID | First author, year | Cache holds |
|---|---|---|
| 16469931 | Berton 2006 | abstract |
| 17956738 | Krishnan 2007 | abstract |
| 21799487 | Golden 2011 | full text |
| 23235832 | Chaudhury 2013 | full text |
| 23416703 | Golden 2013 | abstract |
| 24495460 | Donahue 2014 | full text |
| 24623766 | Vialou 2014 | abstract |
| 25331895 | Hodes 2014 | abstract |
| 26475995 | Hammels 2015 | abstract |
| 26881133 | Qiao 2016 | abstract |
| 27181059 | Bagot 2016 | full text |
| 27569543 | Bagot 2017 | full text |
| 28287253 | Commons 2017 | full text |
| 28462942 | Hamilton 2018 | abstract |
| 28888327 | Iñiguez 2018 | full text |
| 28993631 | Takahashi 2017 | full text |
| 29020387 | Browne 2018 | abstract |
| 29090682 | Harris 2018 | abstract |
| 29184215 | Menard 2017 | full text |
| 29502969 | Hultman 2018 | full text |
| 30196085 | Goñi-Balentziaga 2018 | abstract |
| 30738104 | Molendijk 2019 | abstract |
| 31132785 | Nam 2019 | abstract |
| 31255250 | Newman 2019 | full text |
| 31301368 | Esquivel-Rendón 2019 | abstract |
| 31542427 | Jiang 2019 | abstract |
| 31584111 | Planchez 2019 | full text |
| 32169281 | Scarpa 2020 | full text |
| 32918293 | Deonaraine 2020 | abstract |
| 33090813 | Wang 2021 | abstract |
| 34532840 | Kuske 2022 | abstract |
| 35301426 | Kokkosis 2022 | abstract |
| 35470042 | Duan 2022 | abstract |
| 36030966 | Segi-Nishida 2025 | abstract |
| 36608919 | Lyons 2023 | abstract |
| 36780219 | Hughes 2023 | abstract |
| 38688411 | Díez-Solinska 2024 | abstract |
| 39719686 | Madeira 2025 | abstract |
| 41278963 | Xiong 2025 (preprint) | abstract |
| 41290975 | Domżalska 2025 | abstract |
| 41566898 | Xiong 2026 | full text |
| 42511784 | Ritter 2026 | full text |
| 42593738 | Santos-Silva 2026 | full text |
| 42614171 | Patel 2026 | full text |
| 42633587 | Qiu 2026 | full text |
| 42714059 | Wang 2026 | abstract |
| 42874279 | Li 2026 | abstract |
