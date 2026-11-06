---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T17:14:57.526588'
end_time: '2026-10-23T17:27:39.770587'
duration_seconds: 762.24
template_file: templates/disease_phenotype_wiring_research.md
template_sha: "e4c8898a5d741502b1868031e5dbb9e7ad91d698"
template_variables:
  disease_name: Dementia with Lewy Bodies
  mondo_id: MONDO:0007488
  mechanism_nodes: 1. Alpha-Synuclein Aggregation and Lewy Body Formation (cortical,
    limbic and brainstem Lewy bodies and Lewy neurites); 2. Autophagy-Lysosome Dysfunction
    (GBA1-linked impaired clearance of alpha-synuclein); 3. Neuronal Death (cortical
    and limbic neuronal loss)
  phenotype_names: Recurrent complex visual hallucinations; Visual misperceptions,
    illusions and passage/presence hallucinations (early); Delusions and misidentification
    syndromes (e.g. Capgras); Fluctuating cognition and alertness; Excessive daytime
    somnolence; Dementia with early attention, executive and visuospatial deficits
    and relatively spared early memory; Later amnestic decline; REM sleep behavior
    disorder; Hyposmia; Constipation; Orthostatic hypotension and syncope; Urinary
    dysfunction; Parkinsonism (bradykinesia, rigidity; rest tremor less common than
    in Parkinson disease); Postural instability, gait disturbance and falls; Dysphagia
    and aspiration pneumonia (late); Severe antipsychotic (neuroleptic) sensitivity;
    Depression; Anxiety; Apathy; Reduced striatal dopamine transporter uptake on SPECT/PET;
    Reduced cardiac 123I-MIBG uptake; Occipital hypometabolism and cingulate island
    sign; Posterior slow-wave EEG activity
  established_axis: Misfolded alpha-synuclein aggregates into Lewy bodies and Lewy
    neurites, spreading through brainstem, limbic and neocortical regions, accompanied
    in many cases by amyloid-beta and tau co-pathology, with GBA1, APOE e4 and SNCA
    as genetic risk loci. Do not re-survey the aggregation biology itself.
  priority_hubs: '(a) DISEASE STAGING AND PROGRESSION: the order in which phenotypes
    appear. Report the prodromal phase (isolated REM sleep behavior disorder, hyposmia,
    constipation, orthostatic hypotension, depression/anxiety, often years to decades
    before dementia), the MCI-with-Lewy-bodies phase (attention/executive/visuospatial-predominant),
    and established dementia, then late-stage features (falls, dysphagia, aspiration,
    worsening parkinsonism, amnestic decline). For each phase give primary longitudinal
    human data (phenoconversion cohorts from isolated RBD, prodromal DLB research
    criteria by McKeith 2020, clinicopathological series) with timing estimates. State
    which anatomical pathology (peripheral autonomic/olfactory/lower brainstem versus
    limbic versus neocortical Lewy stage, and contribution of AD co-pathology) is
    believed to underlie each phase, and whether body-first versus brain-first spread
    models are relevant. (b) CHOLINERGIC HUB: nucleus basalis of Meynert / basal forebrain
    cholinergic degeneration and the cortical cholinergic deficit as a driver of fluctuations,
    attention deficits and visual hallucinations, including cholinesterase-inhibitor
    response as interventional evidence. (c) VISUAL HALLUCINATION CIRCUITRY: ventral
    visual stream / occipitotemporal Lewy pathology, occipital hypometabolism, attentional/default-mode
    network models, cholinergic loss, and amygdala/temporal Lewy density correlations.
    (d) DOPAMINERGIC HUB: nigrostriatal degeneration as cause of parkinsonism and
    DAT imaging abnormality, its timing relative to dementia, the D2-receptor basis
    of neuroleptic sensitivity, and the contribution of non-dopaminergic (cholinergic/PPN,
    cortical) lesions to gait and falls. (e) BRAINSTEM AND AUTONOMIC HUB: pontine
    sublaterodorsal/magnocellular lesions behind RBD, locus coeruleus noradrenergic
    loss, cardiac sympathetic denervation (MIBG), enteric/vagal pathology behind constipation,
    and olfactory bulb pathology behind hyposmia.'
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-5-5
  num_turns: 94
  total_cost_usd: 4.8892500000000005
  session_id: a5cdc15b-638d-43b6-a0a1-9a84a52f5542
  stop_reason: end_turn
  permission_denials: 8
  denied_tools:
  - Bash
  assistant_text_blocks: 9
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 42
  on_topic: 25
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002367
    reported_labels:
    - closest cached term; no "visual illusion" HP term is cached, so look one up
      before binding
    ontology_label: Visual hallucination
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Dementia with Lewy Bodies
- **MONDO ID:** MONDO:0007488 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Alpha-Synuclein Aggregation and Lewy Body Formation (cortical, limbic and brainstem Lewy bodies and Lewy neurites); 2. Autophagy-Lysosome Dysfunction (GBA1-linked impaired clearance of alpha-synuclein); 3. Neuronal Death (cortical and limbic neuronal loss)

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Recurrent complex visual hallucinations; Visual misperceptions, illusions and passage/presence hallucinations (early); Delusions and misidentification syndromes (e.g. Capgras); Fluctuating cognition and alertness; Excessive daytime somnolence; Dementia with early attention, executive and visuospatial deficits and relatively spared early memory; Later amnestic decline; REM sleep behavior disorder; Hyposmia; Constipation; Orthostatic hypotension and syncope; Urinary dysfunction; Parkinsonism (bradykinesia, rigidity; rest tremor less common than in Parkinson disease); Postural instability, gait disturbance and falls; Dysphagia and aspiration pneumonia (late); Severe antipsychotic (neuroleptic) sensitivity; Depression; Anxiety; Apathy; Reduced striatal dopamine transporter uptake on SPECT/PET; Reduced cardiac 123I-MIBG uptake; Occipital hypometabolism and cingulate island sign; Posterior slow-wave EEG activity

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Misfolded alpha-synuclein aggregates into Lewy bodies and Lewy neurites, spreading through brainstem, limbic and neocortical regions, accompanied in many cases by amyloid-beta and tau co-pathology, with GBA1, APOE e4 and SNCA as genetic risk loci. Do not re-survey the aggregation biology itself.

## Research Objective

The missing layer is the **causal wiring between the mechanism nodes and the
clinical phenotypes**: which pathophysiological process produces which clinical
manifestation, through what intermediates. For **each phenotype listed above**,
report:

1. **The mechanistic chain** from the established disease process to that
   phenotype, as an ordered sequence of steps, one per line, with explicit
   causal verbs ("leads to", "results in"). Start each chain from whichever of
   the existing mechanism nodes is the true proximal upstream step.
2. **Missing intermediate processes**: where the chain passes through a
   process that is NOT in the mechanism node list above (for example a
   malabsorption step, a distinct autoantibody specificity, a clonal expansion
   step), name it explicitly and flag it as a proposed new node.
3. **Primary human evidence** for each causal step: PMIDs with exact quotes
   from the abstracts. Prefer human clinical and interventional studies
   (dietary-withdrawal reversal counts as interventional evidence for a causal
   link). Distinguish evidence source types: human clinical, model organism,
   in vitro, computational.
4. **An evidence grade for the chain as a whole**, one of:
   - ESTABLISHED — causal chain demonstrated in humans, widely accepted
   - SUPPORTED — plausible chain with direct human evidence for most steps
   - PROPOSED — hypothesis in the literature, key steps not demonstrated
   - NOT_ESTABLISHED — the association is documented but no mechanistic chain
     has been demonstrated; competing explanations remain open
5. **Non-causal alternatives** where they are live: if the phenotype may be
   associated through shared genetic background (for example shared HLA
   haplotypes), coincident autoimmunity, or ascertainment rather than through
   downstream causation, say so explicitly.

**Honesty requirement:** "NOT_ESTABLISHED, mechanism unknown" is a correct and
valuable answer. Do NOT manufacture a mechanistic chain to satisfy the request.
A phenotype with no settled mechanism should be reported as exactly that, with
the competing hypotheses named and graded. It is expected that several
phenotypes in the list will end up NOT_ESTABLISHED.

## Priority Hubs

The following convergence hubs are anticipated to route several phenotypes and
must NOT be given shallow treatment. For each, report the full mechanistic
detail and per-branch citations:

(a) DISEASE STAGING AND PROGRESSION: the order in which phenotypes appear. Report the prodromal phase (isolated REM sleep behavior disorder, hyposmia, constipation, orthostatic hypotension, depression/anxiety, often years to decades before dementia), the MCI-with-Lewy-bodies phase (attention/executive/visuospatial-predominant), and established dementia, then late-stage features (falls, dysphagia, aspiration, worsening parkinsonism, amnestic decline). For each phase give primary longitudinal human data (phenoconversion cohorts from isolated RBD, prodromal DLB research criteria by McKeith 2020, clinicopathological series) with timing estimates. State which anatomical pathology (peripheral autonomic/olfactory/lower brainstem versus limbic versus neocortical Lewy stage, and contribution of AD co-pathology) is believed to underlie each phase, and whether body-first versus brain-first spread models are relevant. (b) CHOLINERGIC HUB: nucleus basalis of Meynert / basal forebrain cholinergic degeneration and the cortical cholinergic deficit as a driver of fluctuations, attention deficits and visual hallucinations, including cholinesterase-inhibitor response as interventional evidence. (c) VISUAL HALLUCINATION CIRCUITRY: ventral visual stream / occipitotemporal Lewy pathology, occipital hypometabolism, attentional/default-mode network models, cholinergic loss, and amygdala/temporal Lewy density correlations. (d) DOPAMINERGIC HUB: nigrostriatal degeneration as cause of parkinsonism and DAT imaging abnormality, its timing relative to dementia, the D2-receptor basis of neuroleptic sensitivity, and the contribution of non-dopaminergic (cholinergic/PPN, cortical) lesions to gait and falls. (e) BRAINSTEM AND AUTONOMIC HUB: pontine sublaterodorsal/magnocellular lesions behind RBD, locus coeruleus noradrenergic loss, cardiac sympathetic denervation (MIBG), enteric/vagal pathology behind constipation, and olfactory bulb pathology behind hyposmia.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as listed
  above, containing: the numbered causal chain, the evidence grade, PMIDs with
  exact abstract quotes per step, and suggested ontology terms (GO for
  biological processes, CL for cell types, HP for the phenotype itself).
- A final section titled **Proposed New Mechanism Nodes** listing every
  intermediate process flagged in item 2, each with: a suggested node name, its
  upstream node (from the existing list or another proposed node), its
  downstream phenotypes, and the strongest single citation for its causal
  placement.
- A final section titled **Unwired Phenotypes** listing every phenotype graded
  NOT_ESTABLISHED, with one sentence each on what evidence would settle it.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make


## Output

I'm looking for DLB papers already in the local reference cache so I can quote their abstracts exactly. I'll then fill the gaps from PubMed.

Now gathering PMIDs for the cholinergic, imaging, autonomic and staging papers.

Fetching the next batch of abstracts locally, then searching the remaining hubs (amnestic co-pathology, falls, EEG, dysphagia, urinary).

Still collecting sources (on DAT/nigral loss, tau co-pathology, fluctuations and the thalamus). A few more searches, and then I'll write the report.

Reading the cached abstracts now so every quote is exact.

Retrying the MIBG multicentre study and searching for prodromal-timing and RBD-autopsy series.

Last batch of abstracts to read, then I'll write the report.

Checking suggested ontology terms against the repo's term caches instead of writing CURIEs from memory.

# Mechanism-to-phenotype wiring for Dementia with Lewy Bodies (MONDO:0007488)

## Scope and method

This report traces the causal chain from the three curated mechanism nodes to each of the 23 phenotypes in the entry. The nodes are:

- **N1** Alpha-Synuclein Aggregation and Lewy Body Formation
- **N2** Autophagy-Lysosome Dysfunction
- **N3** Neuronal Death

Every quote below was copied from the abstract (or, where marked, the full text) of a reference cached locally with `just fetch-reference`. None was paraphrased from memory. The caches are in `references_cache/`, are not yet committed, and include 40 newly fetched files.

HP, CL and GO identifiers were checked against `cache/*/terms.csv`. Where no cached term exists, the report says so rather than giving an ID.

### Overall picture

- **N2 is never the proximal upstream node.** No phenotype-level evidence reaches from GBA1/lysosomal dysfunction to a specific clinical feature without passing through N1. N2 should feed N1 only.
- **N3 is too coarse to wire most phenotypes.** Almost every chain passes through a *neurotransmitter-system-specific* loss. Those losses are the missing intermediate nodes (cholinergic, nigrostriatal dopaminergic, noradrenergic/cardiac sympathetic, olfactory, brainstem REM-atonia circuitry, temporal-limbic Lewy pathology, AD co-pathology).
- **Grade totals:** ESTABLISHED 2; SUPPORTED 8; PROPOSED 6; NOT_ESTABLISHED 7.

---

## Priority Hub (a): Staging and progression

**Prodromal phase (years to decades).**
- Postuma 2019 (PMID:30789229, 1,280 isolated RBD patients, 24 centres): "The overall conversion rate from iRBD to an overt neurodegenerative syndrome was 6.3% per year, with 73.5% converting after 12-year follow-up."
- Postuma 2019, full text: "153 (43.5%) developed dementia first".
- In the same cohort, the conversion predictors were "olfactory deficit (HR = 2.62), mild cognitive impairment (HR = 1.91-2.37), erectile dysfunction (HR = 2.13) … constipation (HR = 1.67)". Conversely, "There was no significant predictive value of sex, daytime somnolence, insomnia, restless legs syndrome, sleep apnoea, urinary dysfunction, orthostatic symptoms, depression, anxiety".
- Boeve 2013 autopsy series (PMID:23474058): "RBD preceded the onset of cognitive impairment, parkinsonism, or autonomic dysfunction in 87 (51%) patients by 10±12 (range, 1-61) years." Also: "Among the neurodegenerative disorders associated with RBD (n=170), 160 (94%) were synucleinopathies."
- Fujishiro 2013 (PMID:23909972, 90 patients with probable DLB, retrospective): "LB-related symptoms were present in 79 of 90 patients (87.8%) with probable DLB before or at the time of memory loss onset. These symptoms preceded the onset of memory loss between 1.2 and 9.3 years."
- Fujishiro 2012 (PMID:22722638): "DLB patients exhibited a significantly higher prevalence of olfactory dysfunction, constipation, increased saliva and signs of rapid eye movement sleep behavior disorder at the onset of memory loss than AD patients and normal controls."

**MCI with Lewy bodies (MCI-LB).**
- McKeith 2020 research criteria (PMID:32241955): "The prodromal phase of dementia with Lewy bodies (DLB) includes (1) mild cognitive impairment (MCI), (2) delirium-onset, and (3) psychiatric-onset presentations." The authors "propose operationalized diagnostic criteria for probable and possible mild cognitive impairment with Lewy bodies".
- Joza 2024 (PMID:37461299, 754 isolated-RBD participants): "Reduced attention and executive function, particularly performance on the Trail Making Test Part B, were the strongest identifiers of early DLB." Also: "In phenoconverters, the onset of cognitive decline began up to 10 years prior to phenoconversion."

**Established and late phases.**
- AD co-pathology shifts and accelerates the course. Kraybill 2005 (PMID:15985574): "Patients with AD/LBP had the most rapid rate of cognitive decline."
- Late features (falls, dysphagia, worsening parkinsonism) have no longitudinal staging data in the abstracts retrieved. See the individual phenotypes below.

**Anatomical substrate per phase.**
- *Peripheral and lower-brainstem pathology.* Beach 2010 (PMID:20306269): "The greatest densities and frequencies of PASH occurred in the spinal cord, followed by the paraspinal sympathetic ganglia, the vagus nerve, the gastrointestinal tract and endocrine organs." And: "Spinal cord and peripheral PASH was most common in subjects with PD and DLB, where it appears likely that it is universally widespread."
- *Olfactory bulb.* Beach 2009 (PMID:18982334): "Involvement of the olfactory bulb by Lewy-type alpha-synucleinopathy (LTS) is known to occur at an early stage".
- *Clinical expression scales with neocortical Lewy extent.* Tiraboschi 2015 (PMID:25552579): "The likelihood of occurrence of the DLB clinical syndrome is positively related to the extent of Lewy body pathology and negatively related to the severity of Alzheimer neuritic pathology, while β-amyloid load has no effect."

**Body-first versus brain-first.**
- Horsager 2020 (PMID:32830221; Parkinson disease, not DLB): "The combined iRBD and PDRBD+ patient data were compatible with a body-first trajectory, characterized by initial loss of cardiac MIBG signal and 11C-colonic donepezil signal followed by loss of putaminal FDOPA uptake."
- Borghammer 2021 (PMID:34763110, post-mortem) describes "a caudo-rostral pattern" and "an amygdala-centered pattern with the most abundant pathology in the 'center of the brain', including the amygdala, entorhinal cortex, and substantia nigra".
- **Relevance to DLB is PROPOSED.** The model was built and tested mainly in Parkinson disease. Postuma 2019 (full text) leaves the dementia-first versus parkinsonism-first split unresolved: "It is unclear whether the conversion to dementia versus parkinsonism first is related to a different 'top-down' synuclein spread … or to effects of co-morbid pathology".
- **Proposed node:** "Lewy Pathology Spread Trajectory (body-first / brain-first)". This is better held in `progression:` or `mechanistic_hypotheses` than as a pathophysiology node.

---

## Priority Hubs (b)–(e): Shared intermediates

**(b) Cholinergic hub**
- Tiraboschi 2000 (PMID:10668703): "Marked losses in midfrontal ChAT activity occur in diseases with LB, independent of coexistent AD changes."
- Schumacher 2022 (PMID:34605858): "Patients who have dementia with Lewy bodies and Alzheimer's disease show early degeneration of the cholinergic nucleus basalis of Meynert." Same study: "EEG slowing in the patient groups as assessed by a decrease in dominant frequency was associated with smaller nucleus basalis of Meynert volumes".
- **Interventional evidence.**
  - McKeith 2000, rivastigmine RCT (PMID:11145488): "Patients taking rivastigmine were significantly less apathetic and anxious, and had fewer delusions and hallucinations while on treatment than controls." It also reported benefit "particularly on tasks with a substantial attentional component", and "After drug discontinuation differences between rivastigmine and placebo tended to disappear."
  - Mori 2012, donepezil RCT (PMID:22829268): "Donepezil at 5 and 10mg/day produces significant cognitive, behavioral, and global improvements".

**(c) Visual hallucination circuitry.** See the phenotype entry below.

**(d) Dopaminergic hub**
- Colloby 2012 (PMID:22961551): "In all striatal regions, image uptake was associated with nigral dopaminergic neuronal density (P ≤ 0.04) but not α-synuclein (P ≥ 0.46), tau (P ≥ 0.18) or amyloid β (P ≥ 0.22) burden."

**(e) Brainstem and autonomic hub**
- RBD: Boeve 2007 framework; Ehrminger 2016 locus coeruleus/subcoeruleus MRI.
- Cardiac sympathetic denervation: Orimo 2005.
- Vagal and GI pathology: Beach 2010.
- Olfactory bulb: Beach 2009.
- These are detailed under the individual phenotypes.

---

## Per-phenotype wiring

### Recurrent complex visual hallucinations
**Chain**
1. N1 (temporal-limbic Lewy pathology in amygdala, parahippocampal and inferior temporal cortex) leads to ventral visual-stream and limbic dysfunction.
2. N1 leads to basal forebrain cholinergic degeneration, which results in cortical cholinergic and α7-nicotinic deficit **[proposed node: Cortical Cholinergic Deficit]**.
3. Steps 1 and 2 converge with occipital/parietal hypofunction and result in visual hallucinations.

**Grade: SUPPORTED**

**Evidence**
- *Step 1.* Harding 2002 (PMID:11844739; human clinicopathological, n=63): "Cases with well-formed visual hallucinations had high densities of LB in the amygdala and parahippocampus, with early hallucinations relating to higher densities in parahippocampal and inferior temporal cortices."
- *Step 2.* Ballard 2002 (PMID:11796155; human post-mortem): "Visual hallucinations and delusional misidentification were associated with lower [(125)I]alpha bungarotoxin binding in areas 36 and 20 (P<.05)".
- *Step 2, interventional.* PMID:11145488: patients "had fewer delusions and hallucinations while on treatment than controls".
- *Step 3.* Nagahama 2010 (PMID:19920063; human SPECT): "Visual hallucinations were related to dysfunction of the parietal and occipital association cortices".
- *Modifier.* Merdes 2003 (PMID:12771246): "The low Braak stage (0 to 2, n = 24) subjects had a higher frequency of visual hallucinations (65%) than did subjects with DLB with higher (3 to 6, n = 66) Braak stages (33%, p = 0.008)".

**Non-causal alternative.** Pedunculopontine cholinergic loss is not supported in DLB. Hepp 2013 (PMID:24226265): "The mean cell density in DLB patients was not significantly reduced compared with that in controls."

**Terms:** HP:0002367 Visual hallucination; CL:0000108 cholinergic neuron; GO:0007601 visual perception.

### Visual misperceptions, illusions and passage/presence hallucinations (early)
**Chain**
1. N1 leads to cortical cholinergic deficit (arousal/attention) together with visuoperceptual cortical dysfunction.
2. This results in pareidolic and illusory misperception, which marks susceptibility to visual hallucinations.

**Grade: PROPOSED**

**Evidence**
- Uchiyama 2012 (PMID:22649179; human clinical): "pareidolias do not reflect visual hallucinations themselves but may reflect susceptibility to visual hallucinations." The causal clause is the authors' inference: "Arousal and attentional deficits mediated by abnormal cholinergic mechanisms and visuoperceptual dysfunctions are likely to contribute".
- Presence hallucinations: Nagahama (PMID:19920063) found "visual hallucination of person and feeling of presence … were related to hypoperfusion in the left ventral occipital gyrus and bilateral parietal areas."

**Terms:** HP:0002367 (closest cached term; no "visual illusion" HP term is cached, so look one up before binding).

### Delusions and misidentification syndromes (e.g. Capgras)
**Chain**
1. N1 leads to limbic-paralimbic dysfunction (hippocampus, insula, ventral striatum).
2. In parallel, N1 leads to cortical α7-nicotinic/cholinergic loss.
3. Both result in misidentification syndromes.

**Grade: PROPOSED** (correlational; there is no lesion-level or interventional proof specific to misidentification)

**Evidence**
- Nagahama 2010 (PMID:19920063): "misidentifications were related to dysfunction of the limbic-paralimbic structures and delusions were related to dysfunction of the frontal cortices."
- PMID:11796155: "Loss of cortical alpha 7 nicotinic receptors may contribute to hallucinations and delusional misidentification in DLB".
- Rivastigmine reduced delusions (PMID:11145488).

**Terms:** HP:0000746 Delusion. No Capgras HP term is cached.

### Fluctuating cognition and alertness
**Chain**
1. N1 leads to basal forebrain cholinergic degeneration **[Cortical Cholinergic Deficit]**.
2. In parallel, N1 leads to thalamic microstructural and cholinergic imbalance **[proposed node: Thalamocortical Arousal Network Dysfunction]**.
3. These result in posterior EEG slowing and variability, and in fluctuating attention and arousal.

**Grade: PROPOSED**

**Evidence**
- Fluctuations are not explained by regional Lewy body density. Harding 2002 (PMID:11844739): "There was no association across groups between any neuropathological variable and the presence or absence of fluctuating cognition."
- Delli Pizzi 2015 (PMID:25260701; MRI/MRS, n=16 DLB): the thalamic choline signal "correlated with severity and frequency of flCog"; "We posit that microstructural thalamic damage and cholinergic imbalance may be central to the etiology of flCog".
- Bonanni 2008 (PMID:18202105): "in those with DLB and PDD, the degree to which residual alpha and 5.6-7.9 bands appeared was related to the presence and severity of cognitive fluctuations."
- Interventional evidence is indirect: the attentional benefit of rivastigmine (PMID:11145488).

**Terms:** HP:0000736 Short attention span is the closest cached term; there is no cached term for fluctuating cognition.

### Excessive daytime somnolence
**Chain**
1. N1 (Lewy pathology involving hypothalamic hypocretin/orexin neurons) leads to reduced hypocretin signalling **[proposed node: Hypocretin/Orexin Deficiency]**.
2. This results in hypersomnolence.

**Grade: PROPOSED**

**Evidence**
- Lessig 2010 (PMID:20531237; human autopsy, n=21 DLB): "we show reduced neocortical hypocretin immunoreactivity in dementia with Lewy bodies patients correlating with hypersomnolence and alpha-synuclein levels."
- *Counter-evidence (PDD, not DLB).* Compta 2009 (PMID:19858078): CSF hypocretin-1 levels "were similar among groups … and unrelated to either epworth sleepiness scale or mini-mental state examination."
- *Not a prodromal predictor.* Postuma 2019 found no predictive value for "daytime somnolence".

**Competing explanations:** nocturnal sleep fragmentation; RBD; medication; the cholinergic and arousal hub.

**Terms:** HP:0001262 Excessive daytime somnolence; CL:0011109 hypocretin-secreting neuron; GO:0030431 sleep.

### Dementia with early attention, executive and visuospatial deficits and relatively spared early memory
**Chain**
1. N1 (limbic and neocortical Lewy pathology plus basal forebrain involvement) leads to frontal cholinergic loss independent of AD **[Cortical Cholinergic Deficit]**.
2. Together with N3 cortical dysfunction, this results in an attention/executive/visuospatial-predominant profile.
3. Medial temporal lobe tangle burden is low, so memory is relatively spared.

**Grade: SUPPORTED**

**Evidence**
- PMID:10668703: "A greater midfrontal, as opposed to hippocampal, cholinergic deficit may differentiate LBV from AD."
- Kraybill 2005 (PMID:15985574; autopsy-verified): "LBP patients were more impaired than AD patients on executive function (Trail Making Test Part B; p < 0.05) and attention tasks".
- PMID:34605858: increased diffusivity of the nucleus basalis lateral pathway "was related to more impaired global cognition (β = -0.22, P = 0.06) and worse performance on an attention task (β = 0.30, P = 0.03)".
- Interventional: Mori 2012 (PMID:22829268) donepezil improved MMSE.
- Prodromal timing: Joza 2024 (PMID:37461299), quoted above.

**Terms:** HP:0000726 Dementia; HP:0033051 Impaired executive functioning; HP:0010794 Impaired visuospatial constructive cognition; GO:0050890 cognition.

### Later amnestic decline
**Chain**
1. AD co-pathology **[proposed node: Concomitant Alzheimer Neurofibrillary Pathology]** leads to medial temporal tangle-driven degeneration.
2. This results in an amnestic deficit and faster decline.

**Grade: SUPPORTED**

**Evidence**
- PMID:15985574: "patients with Alzheimer disease (AD) alone and AD/Lewy body pathology (LBP) had more severe memory impairment than patients with LBP."
- McKeith 2017 (PMID:28592453, full text): the hippocampus "is strongly correlated at autopsy with tangle rather than plaque or LB-related pathology", and "MTL atrophy in DLB may, however, signal substantial additional AD neuropathologic change, and predict a more rapid clinical course."
- PMID:37461299: "Decline in episodic memory best distinguished dementia-first from parkinsonism-first phenoconversion."

**Non-causal alternative.** Amnestic decline in late disease may also reflect the spread of Lewy pathology itself. The two cannot be cleanly separated in these data.

**Terms:** HP:0002354 Memory impairment; GO:0007611 learning or memory.

### REM sleep behavior disorder
**Chain**
1. N1 (lower-brainstem Lewy pathology) leads to degeneration of the pontine coeruleus/subcoeruleus (sublaterodorsal-equivalent) REM-atonia circuitry **[proposed node: Brainstem REM-Atonia Circuit Degeneration]**.
2. This results in loss of REM atonia.
3. Loss of REM atonia results in dream enactment.

**Grade: SUPPORTED** (the anatomical framework comes from animal work; human evidence is imaging and clinicopathological)

**Evidence**
- Boeve 2007 (PMID:17412731; review drawing on rat and cat data): "The structure in man analogous to the subcoeruleus region in cat and sublaterodorsal nucleus in rat is proposed as the nucleus (and its associated efferent and afferent pathways) crucial to RBD pathophysiology."
- Ehrminger 2016 (PMID:26920675; human neuromelanin MRI): "reduced signal intensity was identified in the locus coeruleus/subcoeruleus complex of the patients with idiopathic rapid eye movement sleep behaviour."
- Boeve 2013 (PMID:23474058): 94% of RBD-associated neurodegeneration was synucleinopathy.
- Ferman 2011 (PMID:21849645): "RBD increased the odds by 6-fold" of autopsy-confirmed DLB.

**Terms:** HP:5200291 REM sleep behavior disorder; CL:0008025 noradrenergic neuron (locus coeruleus component only).

### Hyposmia
**Chain**
1. N1 in the olfactory bulb and anterior olfactory structures leads to olfactory pathway dysfunction **[proposed node: Olfactory Bulb Synucleinopathy]**.
2. This results in hyposmia.

**Grade: SUPPORTED** for the lesion and the timing. The lesion-to-test link is not quantified in DLB in these abstracts.

**Evidence**
- PMID:18982334: olfactory bulb synucleinopathy in "DLB 34/1" positive/negative; "97 and 91% for DLB versus elderly control".
- PMID:22722638: higher prevalence of olfactory dysfunction at memory-loss onset.
- PMID:30789229: olfactory deficit predicts phenoconversion (HR 2.62).

**Terms:** HP:0004409 Hyposmia; GO:0007608 sensory perception of smell.

### Constipation
**Chain**
1. N1 in the enteric nervous system, vagus nerve and dorsal motor nucleus of the vagus **[proposed node: Enteric and Vagal Synucleinopathy]**.
2. This leads to colonic parasympathetic denervation and dysmotility.
3. Dysmotility results in constipation.

**Grade: PROPOSED** for DLB. The lesions are documented, but no DLB abstract links lesion burden to constipation.

**Evidence**
- PMID:20306269 describes pathology in "the vagus nerve, the gastrointestinal tract".
- In Parkinson disease, Horsager 2020 (PMID:32830221) found RBD-positive patients had "enlarged colon volumes (P < 0.001, ANOVA) and delayed colonic transit times", alongside reduced colonic donepezil PET signal.
- Prodromal occurrence: PMID:22722638; PMID:30789229 (HR 1.67).

**Non-causal alternatives:** immobility, medication (anticholinergics), diet.

**Terms:** HP:0002019 Constipation; CL:0007011 enteric neuron.

### Orthostatic hypotension and syncope
**Chain**
1. N1 in the paraspinal sympathetic ganglia, intermediolateral spinal cord and postganglionic cardiac/vascular sympathetic fibres.
2. This leads to distal-first sympathetic noradrenergic denervation **[proposed node: Peripheral Sympathetic Noradrenergic Denervation]**.
3. Denervation results in failure of adrenergic vasoconstriction, then orthostatic hypotension, then syncope.

**Grade: SUPPORTED**

**Evidence**
- PMID:20306269: pathology is dense in "spinal cord, followed by the paraspinal sympathetic ganglia".
- Thaisetthawatkul 2004 (PMID:15159482; human autonomic testing): "orthostatic hypotension occurred in 10/20 DLB"; "Autonomic dysfunction is frequent in dementia with Lewy bodies and the severity is intermediate between that of multiple system atrophy and Parkinson disease."
- Postuma 2019 found no prodromal predictive value for "orthostatic symptoms". The causal chain is not proven at the level of individual patients.

**Note.** McKeith 2017 says "Transient episodes of unresponsiveness may represent an extreme form of cognitive fluctuation, difficult to distinguish from true syncope". Some reported "syncope" may therefore belong to the fluctuation branch rather than this one.

**Terms:** HP:0001278 Orthostatic hypotension; HP:0001279 Syncope; CL:0011103 sympathetic neuron; GO:0008217 regulation of blood pressure.

### Urinary dysfunction
**Chain (hypothesised)**
1. N1 leads to loss of the central inhibitory control of micturition (pontine/basal ganglia/frontal).
2. This leads to detrusor overactivity.
3. Detrusor overactivity results in urgency and urge incontinence.

**Grade: NOT_ESTABLISHED**

**Evidence**
- Ransmayr 2008 (PMID:18209204): "detrusor overactivity in 92% of the patients with DLB". The study establishes the urodynamic phenotype only, not its lesion.
- Not predictive of phenoconversion (PMID:30789229).

**Competing explanations:** prostatic disease, frontal dementia-related incontinence, medication.

**Terms:** HP:0000012 Urinary urgency; HP:0000020 Urinary incontinence.

### Parkinsonism (bradykinesia, rigidity; rest tremor less common than in Parkinson disease)
**Chain**
1. N1 in the substantia nigra pars compacta leads to N3 (dopaminergic neuron loss) **[proposed node: Nigrostriatal Dopaminergic Degeneration]**.
2. This leads to striatal dopamine and transporter loss.
3. Dopamine loss results in bradykinesia and rigidity.

**Grade: ESTABLISHED** (for the core chain)

**Evidence**
- Piggott 1999 (PMID:10430831; post-mortem): "In the caudal putamen, dopamine was reduced by 72% in DLB", with "the loss of substantia nigra neurons (49%)".
- McKeith 2017 recommends recording nigral neuron loss "to subclassify cases into those likely or not to have parkinsonism (DLB-P and DLB-no P)".
- Why levodopa response is poorer is PROPOSED: Piggott describes compensatory dopamine turnover "absent in DLB".

**Terms:** HP:0001300 Parkinsonism; HP:0002067 Bradykinesia; HP:0002063 Rigidity; CL:0000700 dopaminergic neuron.

### Postural instability, gait disturbance and falls
**Chain (hypothesised)**
1. Nigrostriatal loss plus cortical cholinergic and attentional deficits plus orthostatic hypotension and neuroleptic exposure lead to falls.

**Grade: NOT_ESTABLISHED** for DLB

**Evidence**
- The cholinergic–attention–falls link comes from Parkinson disease. PMID:21898597 (review): "It is therefore feasible that cognition (namely, attention), visual hallucinations, falls, and gait are subserved by acetylcholine".
- **Against simple extrapolation:** pedunculopontine cholinergic neurons were not significantly reduced in DLB (PMID:24226265).
- McKeith 2017 lists fall-risk management but gives no mechanism.

**Terms:** HP:0002172 Postural instability; HP:0001288 Gait disturbance; HP:0002527 Falls.

### Dysphagia and aspiration pneumonia (late)
**Chain (hypothesised)**
1. N1 in the dorsal motor nucleus of the vagus and brainstem swallowing network, plus nigrostriatal loss and cognitive decline.
2. These lead to pharyngeal-phase dysfunction.
3. Pharyngeal dysfunction results in aspiration.

**Grade: NOT_ESTABLISHED**

**Evidence**
- Londos 2013 (PMID:24099488): "Twenty-four (92%) of these had a documented swallowing dysfunction on VFSE. Eighty-eight percent suffered from pharyngeal dysfunction." The vagal-nucleus mechanism appears only as background in the full text and is not demonstrated.

**Terms:** HP:0002015 Dysphagia; HP:0011951 Aspiration pneumonia.

### Severe antipsychotic (neuroleptic) sensitivity
**Chain**
1. N3 nigrostriatal loss leads to striatal dopamine depletion.
2. D2 receptors fail to show the compensatory upregulation seen in Parkinson disease **[part of Nigrostriatal Dopaminergic Degeneration]**.
3. D2 blockade on this reduced reserve results in severe extrapyramidal and sensitivity reactions.

**Grade: PROPOSED.** The clinical phenomenon is established; the receptor mechanism is post-mortem inference.

**Evidence**
- PMID:10430831: "[(3)H]raclopride binding to D2 receptors was significantly reduced in the caudal putamen (17%) compared with controls, and was significantly lower than in Parkinson's disease at all levels." Also: "These differences … may explain some characteristics of the extrapyramidal features of DLB and its limited response to L-dopa and severe neuroleptic sensitivity."
- McKeith 1992 (PMID:1356550): "16 (80%) patients with Lewy body type dementia received neuroleptics, 13 (81%) of whom reacted adversely; in seven (54%) the reactions were severe."

**Terms:** none cached; look up an HP drug-sensitivity term before binding.

### Depression
**Grade: NOT_ESTABLISHED.** It is a prodromal feature but has no demonstrated lesion chain.
- PMID:23909972 lists depression among LB-related symptoms that precede memory loss. One patient "converted to probable DLB with the development of parkinsonism 2 years after major depression was diagnosed."
- Not predictive of iRBD conversion (PMID:30789229).
- Candidate mechanisms (locus coeruleus and raphe monoaminergic loss) are not evidenced in the abstracts retrieved.
- **Non-causal alternatives:** reactive depression; shared ascertainment in memory clinics.

**Terms:** HP:0000716 Depression.

### Anxiety
**Grade: NOT_ESTABLISHED**
- Rivastigmine reduced anxiety (PMID:11145488), but McKeith 2017 notes "anxiety and agitation are sometimes driven by psychosis", so this effect may be secondary.
- Not predictive of iRBD conversion (PMID:30789229).

**Terms:** HP:0000739 Anxiety.

### Apathy
**Grade: NOT_ESTABLISHED** (a cholinergic contribution is PROPOSED)
- Interventional hint only: patients on rivastigmine "were significantly less apathetic" (PMID:11145488). No lesion study was retrieved.

**Terms:** HP:0000741 Apathy.

### Reduced striatal dopamine transporter uptake on SPECT/PET
**Chain**
1. N1 leads to N3 (nigral dopaminergic neuron loss).
2. Loss of nigrostriatal terminals results in reduced DAT binding.

**Grade: ESTABLISHED**

**Evidence**
- PMID:22961551, quoted under hub (d): uptake tracks nigral neuronal density, not lesion burden.
- Walker 2007 (PMID:17353255): "The sensitivity of the FP-CIT scan for the diagnosis of DLB was 88% and specificity was 100%."
- Normal scans occur with minimal brainstem involvement (McKeith 2017).

**Terms:** GO:0051583 dopamine uptake involved in synaptic transmission; CL:0000700.

### Reduced cardiac 123I-MIBG uptake
**Chain**
1. N1 in cardiac postganglionic sympathetic axons leads to distal axonal degeneration, which precedes loss of ganglion neurons **[Peripheral Sympathetic Noradrenergic Denervation]**.
2. This results in reduced MIBG uptake.

**Grade: ESTABLISHED**

**Evidence**
- Orimo 2005 (PMID:15933869): "Decreased cardiac uptake of MIBG in Lewy body disease reflects actual cardiac sympathetic denervation, which precedes the neuronal loss in the sympathetic ganglia."
- Yoshita 2015 (PMID:25793585): "sensitivity was 68.9% and the specificity was 89.1%".

**Terms:** CL:0011103 sympathetic neuron; GO:0048243 norepinephrine secretion.

### Occipital hypometabolism and cingulate island sign
**Chain**
1. N1 and cortical cholinergic denervation lead to occipital and visual-association hypometabolism.
2. Low medial temporal / posterior cingulate tangle load (absence of AD co-pathology) means relative posterior cingulate preservation, i.e. the cingulate island sign.

**Grade: SUPPORTED**

**Evidence**
- Graff-Radford 2014 (PMID:25056580): "CIS on FDG-PET is not associated with fibrillar β-amyloid deposition but indicates lower Braak NFT stage in patients with DLB."
- Lim 2009 (PMID:19759102): "hypometabolism in the lateral occipital cortex had the highest sensitivity (88%), but relative preservation of the mid or posterior cingulate gyrus (cingulate island sign) had the highest specificity (100%)."
- McKeith 2017 (full text): "FDG-PET occipital hypometabolism correlates with visual cortex neuropathology in DLB".
- Whether the occipital deficit is cholinergic or primary-synaptic remains open.

**Terms:** none cached; look up an HP neuroimaging-abnormality term before binding.

### Posterior slow-wave EEG activity
**Chain**
1. N1 leads to nucleus basalis degeneration **[Cortical Cholinergic Deficit]**.
2. This results in slowing of the dominant posterior rhythm.

**Grade: SUPPORTED**

**Evidence**
- PMID:34605858: "EEG slowing … was associated with smaller nucleus basalis of Meynert volumes (β = 0.22, P = 0.02)".
- PMID:18202105: "Dominant frequencies were 8.3 +/- 0.6 Hz for the AD group and 7.4 +/- 1.6 Hz for the DLB group".

**Terms:** HP:0010845 EEG with generalized slow activity (closest cached term; the finding is posterior, not generalized).

---

## Proposed New Mechanism Nodes

| Suggested node | Upstream | Downstream phenotypes | Strongest citation |
|---|---|---|---|
| Cortical Cholinergic Deficit (basal forebrain / nucleus basalis degeneration) | N1 → N3 | Visual hallucinations; misperceptions; delusions/misidentification; fluctuations; attention/executive dementia; posterior EEG slowing; occipital hypometabolism; apathy (proposed) | PMID:10668703 (with interventional PMID:11145488) |
| Temporal-Limbic Lewy Body Burden (amygdala, parahippocampal, inferior temporal) | N1 | Visual hallucinations; misidentification | PMID:11844739 |
| Thalamocortical Arousal Network Dysfunction | Cortical Cholinergic Deficit; N1 | Fluctuating cognition; EDS (partly) | PMID:25260701 |
| Nigrostriatal Dopaminergic Degeneration (with absent D2 compensation) | N1 → N3 | Parkinsonism; reduced DAT uptake; neuroleptic sensitivity; falls (contributory) | PMID:22961551; PMID:10430831 |
| Brainstem REM-Atonia Circuit Degeneration (coeruleus/subcoeruleus) | N1 | REM sleep behavior disorder | PMID:26920675 |
| Peripheral Sympathetic Noradrenergic Denervation | N1 | Reduced MIBG uptake; orthostatic hypotension and syncope | PMID:15933869 |
| Enteric and Vagal Synucleinopathy | N1 | Constipation; dysphagia (proposed) | PMID:20306269 |
| Olfactory Bulb Synucleinopathy | N1 | Hyposmia | PMID:18982334 |
| Hypocretin/Orexin Deficiency | N1 | Excessive daytime somnolence | PMID:20531237 |
| Concomitant Alzheimer Neurofibrillary Pathology | Separate co-pathology; not downstream of N1 | Later amnestic decline; low cingulate island ratio; fewer hallucinations | PMID:15985574; PMID:25056580 |
| Lewy Pathology Spread Trajectory (body-first / brain-first) | N1 | Prodromal ordering (RBD, autonomic, hyposmia before dementia) | PMID:32830221 (Parkinson disease cohort) |

N2 should connect only as N2 → N1. No phenotype-level evidence bypasses aggregation.

## Unwired Phenotypes (NOT_ESTABLISHED)

- **Urinary dysfunction.** Settled by a urodynamic-clinicopathological study relating detrusor overactivity to pontine/frontal Lewy burden or dopaminergic loss in DLB.
- **Postural instability, gait disturbance and falls.** Settled by DLB cholinergic (VAChT/PET) and nigral imaging correlated with prospectively recorded falls. PMID:24226265 argues against assuming the Parkinson disease pedunculopontine mechanism.
- **Dysphagia and aspiration pneumonia.** Settled by autopsy correlation of dorsal-vagal/nucleus-ambiguus Lewy burden with videofluoroscopic findings.
- **Depression.** Settled by locus coeruleus/raphe neuromelanin or serotonergic imaging related to prospective depression ratings in prodromal DLB.
- **Anxiety.** Settled by studies separating psychosis-driven from primary anxiety, plus monoaminergic or amygdala lesion correlation.
- **Apathy.** Settled by a cholinergic or frontostriatal lesion study, or a trial with apathy as the primary endpoint (the rivastigmine signal is secondary).
- **Severe antipsychotic sensitivity (mechanism only).** Settled by in vivo D2 PET in DLB with documented sensitivity reactions. This is graded PROPOSED above, but its receptor chain rests on one post-mortem series.

## Notes for curation

- About 40 reference files were added to `references_cache/` by `just fetch-reference` and are **uncommitted**. Stage only those you cite.
- Several quotes come from full text rather than the abstract: PMID:30789229 (the dementia-first counts and the top-down spread passage), PMID:28592453 (the tangle, MTL atrophy, occipital FDG and syncope passages), and PMID:24099488. Run `just count-verified-snippets` before using them.
- Parkinson-derived evidence (PMIDs 32830221, 19858078, 21898597) should carry `directness: INDIRECT` if it is cited for DLB.
- No HP term is cached for fluctuating cognition, Capgras/misidentification, visual illusion, neuroleptic sensitivity, or the imaging findings. Look each one up rather than reusing the IDs above.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 42 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002367` (2 mentions) - the report calls it "closest cached term; no "visual illusion" HP term is cached, so look one up before binding"; HP calls it **Visual hallucination**