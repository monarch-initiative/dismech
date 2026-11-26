---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T12:50:57.581721'
end_time: '2026-11-12T13:10:16.287134'
duration_seconds: 1158.71
template_file: templates/disease_phenotype_wiring_research.md
template_sha: "e4c8898a5d741502b1868031e5dbb9e7ad91d698"
template_variables:
  disease_name: Hypermobile Ehlers-Danlos Syndrome
  mondo_id: MONDO:0007523
  mechanism_nodes: '1. Candidate extracellular matrix remodeling abnormalities (cultured
    hEDS/HSD dermal fibroblasts: disorganised collagen and fibronectin ECM, loss of
    alpha2beta1/alpha5beta1 integrin organisation, preferential alphavbeta3 integrin;
    CELLULAR, hypothetical); 2. Myofibroblast-like fibroblast transition (alphavbeta3
    integrin/ILK/Snail1 signalling, alpha-SMA stress fibres, cadherin-11, MMP9 - in
    vitro patient-fibroblast evidence only; CELLULAR, provisional); 3. Joint instability
    and recurrent soft-tissue injury (TISSUE; currently the only node wired to phenotypes:
    Joint dislocation, Chronic pain, Arthralgia)'
  phenotype_names: Joint hypermobility; Joint dislocation; Chronic pain; Arthralgia;
    Myalgia; Fatigue; Sleep disturbance; Migraine; Peripheral neuropathy (including
    small-fiber neuropathy); Orthostatic tachycardia (postural tachycardia syndrome);
    Acrocyanosis; Gastrointestinal dysmotility; Gastroesophageal reflux; Nausea; Constipation;
    Mitral valve prolapse; Aortic root dilatation; Hyperextensible skin; Soft skin;
    Atrophic scars; Striae distensae; Easy bruising; Pelvic organ prolapse; Abdominal
    wall hernia; Dental crowding; High, narrow palate; Sleep apnea; Anxiety; Depression
  established_axis: Hypermobile EDS (2017 criteria) is a clinically diagnosed heritable
    connective tissue disorder with autosomal dominant transmission in families and
    NO confirmed causal gene; the 2017 criteria deliberately separate it from hypermobility
    spectrum disorder, and the entry already records the genetics controversy, the
    proposed KLK15, ACKR3 and complement/proteomic candidates (2025, unreplicated),
    and the TNXB-associated hypermobility disorder as separate open discussions. Do
    NOT re-survey the causal-gene question, the hEDS-versus-HSD boundary debate, or
    the diagnostic criteria. Treat generalised connective-tissue laxity with a candidate
    fibroblast ECM-remodeling/myofibroblast-transition phenotype as the given upstream
    context, and concentrate entirely on how that context produces each listed clinical
    manifestation.
  priority_hubs: '(a) PAIN HUB: how hEDS chronic pain arises beyond acute mechanical
    injury - central sensitisation / nociplastic pain (lowered pressure and thermal
    pain thresholds, temporal summation), small-fiber neuropathy (reduced intraepidermal
    nerve fibre density on skin biopsy), proprioceptive deficit and muscle weakness
    from joint laxity, and their contribution to arthralgia, myalgia, migraine, fatigue
    and sleep disturbance; give human quantitative-sensory-testing and skin-biopsy
    studies as primary evidence. (b) AUTONOMIC HUB: the proposed routes from connective-tissue
    laxity to postural tachycardia / orthostatic intolerance - venous pooling from
    distensible vessel walls and reduced preload, autonomic small-fiber neuropathy,
    hyperadrenergic state, deconditioning, and mast-cell mediator release; say which
    have direct human measurement (tilt-table, catecholamines, venous compliance)
    and which are inference; include acrocyanosis as a vasomotor manifestation. (c)
    GASTROINTESTINAL HUB: gut-wall connective tissue laxity, autonomic dysfunction,
    visceral hypersensitivity and mast-cell activation as competing or additive explanations
    for dysmotility, reflux, nausea and constipation; report manometry, gastric-emptying
    and disorders-of-gut-brain-interaction cohort data. (d) TISSUE LAXITY HUB: the
    direct mechanical consequences of lax connective tissue in each site - joint capsule
    and ligament (hypermobility, dislocation), dermis (hyperextensible and soft skin,
    atrophic scars, striae, easy bruising from vessel-wall and perivascular support
    fragility), pelvic floor (prolapse), abdominal wall (hernia), cardiac valve and
    aortic root (mitral valve prolapse, aortic root dilatation - including the longitudinal
    data showing hEDS aortic dilatation is usually mild and non-progressive), and
    craniofacial/upper-airway structures (dental crowding, high narrow palate, obstructive
    sleep apnea). (e) PSYCHIATRIC HUB: whether anxiety and depression in hEDS are
    downstream of chronic pain, dysautonomia and interoceptive sensitivity, share
    a neurodevelopmental or autonomic substrate, or are ascertainment effects; name
    the cohort and imaging studies and treat non-causal explanations as live.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 8b7945d8-b2b6-4eef-a64d-bb06a8ba6955
citation_count: 28
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 0
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 37
  labels_matching: 32
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0045010
    reported_labels:
    - Small fiber neuropathy
    ontology_label: Abnormal peripheral nerve morphology by anatomical site
  - term_id: HP:0031547
    reported_labels:
    - Postural orthostatic tachycardia
    ontology_label: Abnormal QT interval
  - term_id: HP:0000083
    reported_labels:
    - Pelvic organ prolapse
    ontology_label: Renal insufficiency
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypermobile_Ehlers-Danlos_Syndrome-phenotype-wiring-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypermobile_Ehlers-Danlos_Syndrome-phenotype-wiring-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Hypermobile Ehlers-Danlos Syndrome
- **MONDO ID:** MONDO:0007523 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Candidate extracellular matrix remodeling abnormalities (cultured hEDS/HSD dermal fibroblasts: disorganised collagen and fibronectin ECM, loss of alpha2beta1/alpha5beta1 integrin organisation, preferential alphavbeta3 integrin; CELLULAR, hypothetical); 2. Myofibroblast-like fibroblast transition (alphavbeta3 integrin/ILK/Snail1 signalling, alpha-SMA stress fibres, cadherin-11, MMP9 - in vitro patient-fibroblast evidence only; CELLULAR, provisional); 3. Joint instability and recurrent soft-tissue injury (TISSUE; currently the only node wired to phenotypes: Joint dislocation, Chronic pain, Arthralgia)

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Joint hypermobility; Joint dislocation; Chronic pain; Arthralgia; Myalgia; Fatigue; Sleep disturbance; Migraine; Peripheral neuropathy (including small-fiber neuropathy); Orthostatic tachycardia (postural tachycardia syndrome); Acrocyanosis; Gastrointestinal dysmotility; Gastroesophageal reflux; Nausea; Constipation; Mitral valve prolapse; Aortic root dilatation; Hyperextensible skin; Soft skin; Atrophic scars; Striae distensae; Easy bruising; Pelvic organ prolapse; Abdominal wall hernia; Dental crowding; High, narrow palate; Sleep apnea; Anxiety; Depression

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Hypermobile EDS (2017 criteria) is a clinically diagnosed heritable connective tissue disorder with autosomal dominant transmission in families and NO confirmed causal gene; the 2017 criteria deliberately separate it from hypermobility spectrum disorder, and the entry already records the genetics controversy, the proposed KLK15, ACKR3 and complement/proteomic candidates (2025, unreplicated), and the TNXB-associated hypermobility disorder as separate open discussions. Do NOT re-survey the causal-gene question, the hEDS-versus-HSD boundary debate, or the diagnostic criteria. Treat generalised connective-tissue laxity with a candidate fibroblast ECM-remodeling/myofibroblast-transition phenotype as the given upstream context, and concentrate entirely on how that context produces each listed clinical manifestation.

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

(a) PAIN HUB: how hEDS chronic pain arises beyond acute mechanical injury - central sensitisation / nociplastic pain (lowered pressure and thermal pain thresholds, temporal summation), small-fiber neuropathy (reduced intraepidermal nerve fibre density on skin biopsy), proprioceptive deficit and muscle weakness from joint laxity, and their contribution to arthralgia, myalgia, migraine, fatigue and sleep disturbance; give human quantitative-sensory-testing and skin-biopsy studies as primary evidence. (b) AUTONOMIC HUB: the proposed routes from connective-tissue laxity to postural tachycardia / orthostatic intolerance - venous pooling from distensible vessel walls and reduced preload, autonomic small-fiber neuropathy, hyperadrenergic state, deconditioning, and mast-cell mediator release; say which have direct human measurement (tilt-table, catecholamines, venous compliance) and which are inference; include acrocyanosis as a vasomotor manifestation. (c) GASTROINTESTINAL HUB: gut-wall connective tissue laxity, autonomic dysfunction, visceral hypersensitivity and mast-cell activation as competing or additive explanations for dysmotility, reflux, nausea and constipation; report manometry, gastric-emptying and disorders-of-gut-brain-interaction cohort data. (d) TISSUE LAXITY HUB: the direct mechanical consequences of lax connective tissue in each site - joint capsule and ligament (hypermobility, dislocation), dermis (hyperextensible and soft skin, atrophic scars, striae, easy bruising from vessel-wall and perivascular support fragility), pelvic floor (prolapse), abdominal wall (hernia), cardiac valve and aortic root (mitral valve prolapse, aortic root dilatation - including the longitudinal data showing hEDS aortic dilatation is usually mild and non-progressive), and craniofacial/upper-airway structures (dental crowding, high narrow palate, obstructive sleep apnea). (e) PSYCHIATRIC HUB: whether anxiety and depression in hEDS are downstream of chronic pain, dysautonomia and interoceptive sensitivity, share a neurodevelopmental or autonomic substrate, or are ascertainment effects; name the cohort and imaging studies and treat non-causal explanations as live.

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

# Mechanism-to-Phenotype Wiring in Hypermobile Ehlers-Danlos Syndrome (MONDO:0007523)

## Summary

This report supplies the missing causal layer between the three curated hEDS mechanism nodes — (1) candidate ECM-remodeling abnormality in dermal fibroblasts, (2) myofibroblast-like fibroblast transition, (3) joint instability and recurrent soft-tissue injury — and the 30 listed clinical phenotypes. For each phenotype we give an ordered causal chain starting from the true proximal mechanism node, name every intermediate process that is *not* in the curated node list (flagged as a proposed new node), grade the chain as a whole, and keep live any non-causal (shared-background, ascertainment, coincident-autoimmunity) alternatives.

The central result is that confidence is sharply **graded and uneven**. The **tissue-laxity mechanical chains** — joint hypermobility, dislocation, hyperextensible/soft skin, atrophic scars, easy bruising, pelvic organ prolapse, abdominal-wall hernia, mitral valve prolapse, aortic root dilatation, and airway-laxity obstructive sleep apnea — are **SUPPORTED to ESTABLISHED**, because the mechanical consequence of lax connective tissue at each site is directly observable and, for the dermis and vessel wall, documented at the ultrastructural level. The **pain hub** (chronic pain, arthralgia, myalgia, and the sensory component of peripheral neuropathy) is **SUPPORTED** but only once two intermediate nodes absent from the curated list are inserted: **central sensitization** (human quantitative sensory testing: lowered pain thresholds, increased wind-up) and **small-fiber neuropathy** (reduced intraepidermal nerve-fiber density on skin biopsy). By contrast, the **autonomic hub** (postural orthostatic tachycardia, acrocyanosis), the **gastrointestinal hub** (dysmotility, reflux, nausea, constipation), **primary migraine**, **depression**, **dental crowding**, and **high narrow palate** are **PROPOSED or NOT_ESTABLISHED**: the epidemiological associations are robust, but the mechanistic steps remain inference and are confounded by co-referral and ascertainment.

Two specific human-data results discipline the model and must not be overstated. First, strain-gauge plethysmography shows that orthostatic **pooling and acrocyanosis are not caused by increased venous compliance** — the intuitive "distensible vein wall" route is directly contradicted, implicating arterial vasoregulatory (autonomic) defects instead. Second, longitudinal echocardiography shows hEDS **aortic root dilatation is usually mild and non-progressive**, so the cardiac-laxity chain, though real, carries little clinical consequence. Thirteen new intermediate mechanism nodes are proposed, chief among them small-fiber neuropathy, central sensitization, dysautonomia/autonomic neuropathy, mast-cell activation, and a shared amygdala/interoceptive neural substrate for anxiety that remains a live non-causal alternative to a purely downstream pain/dysautonomia explanation.

---

## Per-Phenotype Causal Wiring

Each subsection gives: the ordered causal chain (proximal mechanism node → intermediates → phenotype), the overall evidence grade, primary human evidence with exact abstract quotes, non-causal alternatives where live, and suggested ontology terms.

### Joint hypermobility

**Causal chain**
1. ECM-remodeling abnormality / generalised connective-tissue laxity results in reduced tensile integrity of ligament and joint-capsule collagen.
2. Reduced ligament/capsule stiffness leads to increased passive joint range of motion.
3. Increased range of motion is observed clinically as generalised joint hypermobility.

**Evidence grade:** ESTABLISHED (defining feature; the laxity-to-range-of-motion step is the diagnostic criterion itself).

**Non-causal alternatives:** none material — this is the proximal phenotype of the laxity node.

**Ontology:** HP:0001382 (Joint hypermobility); GO:0030198 (extracellular matrix organization); CL:0000057 (fibroblast).

### Joint dislocation

**Causal chain**
1. Connective-tissue laxity (node 1) results in joint hypermobility and capsule/ligament incompetence.
2. Capsule incompetence leads to **proprioceptive deficit and altered neuromuscular control** *(proposed new node)*.
3. Proprioceptive deficit plus mechanical laxity results in recurrent subluxation/dislocation (node 3, joint instability).

**Evidence grade:** SUPPORTED. The mechanical step is self-evident; the proprioceptive intermediate has direct human evidence.

**Primary human evidence**
- [PMID: 7283686](https://pubmed.ncbi.nlm.nih.gov/7283686/) (human clinical): *"A functional proprioceptive deficit was demonstrated and found correctable with training and visual compensation."*
- [PMID: 31498548](https://pubmed.ncbi.nlm.nih.gov/31498548/) (human clinical, gait EMG): *"The EDS group was associated with delayed vastus lateralis (b = 16.69) and medialis activation"* — objective altered neuromuscular activation during gait.

**Ontology:** HP:0001373 (Joint dislocation); GO:0050885 (neuromuscular process controlling balance).

### Chronic pain

**Causal chain**
1. Joint instability/recurrent soft-tissue injury (node 3) leads to repeated nociceptive input.
2. Repeated nociceptive input results in **central sensitization** *(proposed new node)* — lowered pain thresholds and increased temporal summation.
3. In parallel, connective-tissue/ECM disruption is associated with **small-fiber neuropathy** *(proposed new node)* — reduced intraepidermal nerve-fiber density.
4. Central sensitization plus small-fiber neuropathy result in chronic, widespread, nociplastic pain out of proportion to mechanical injury.

**Evidence grade:** SUPPORTED (direct human QST and skin-biopsy evidence for both intermediate nodes).

**Primary human evidence**
- [PMID: 26919608](https://pubmed.ncbi.nlm.nih.gov/26919608/) (human clinical, QST in 27 JHS/EDS-HT): *"the lowered cold and heat pain thresholds and increased wind-up ratio imply that pain in JHS/EDS-HT might arise through central sensitization"*.
- [PMID: 27306637](https://pubmed.ncbi.nlm.nih.gov/27306637/) (human clinical, skin biopsy in 24 EDS): *"All patients showed a decrease of IENFD consistent with the diagnosis of small fiber neuropathy (SFN), regardless of the EDS type. SFN is a common feature in adults with EDS."*

**Non-causal alternatives:** central sensitization and SFN co-occur with psychological distress and dysautonomia; directionality between pain, mood, and sleep is bidirectional rather than strictly downstream.

**Ontology:** HP:0012532 (Chronic pain); GO:0051930 (regulation of sensory perception of pain).

### Arthralgia

**Causal chain**
1. Joint instability/laxity (node 3) leads to abnormal joint loading and microtrauma.
2. Microtrauma plus proprioceptive deficit *(proposed node)* leads to repeated peri-articular nociceptive input.
3. Nociceptive input, amplified by central sensitization *(proposed node)*, results in joint pain (arthralgia).

**Evidence grade:** SUPPORTED (shares the central-sensitization intermediate; mechanical input step established).

**Primary human evidence**
- [PMID: 26919608](https://pubmed.ncbi.nlm.nih.gov/26919608/): central-sensitization QST evidence (quote above).
- [PMID: 7283686](https://pubmed.ncbi.nlm.nih.gov/7283686/): proprioceptive-deficit evidence (quote above).

**Ontology:** HP:0002829 (Arthralgia).

### Myalgia

**Causal chain**
1. Joint laxity (node 3) results in **compensatory muscle overuse and altered activation** *(proposed node: altered neuromuscular control)* to stabilise unstable joints.
2. Muscle overuse plus generalised muscle weakness leads to muscular nociceptive input.
3. Input amplified by central sensitization *(proposed node)* results in diffuse muscle pain (myalgia).

**Evidence grade:** SUPPORTED.

**Primary human evidence**
- [PMID: 7283686](https://pubmed.ncbi.nlm.nih.gov/7283686/) (human clinical): generalised muscle weakness and shifted strength-length curve ("increased series elastic component"), plus proprioceptive deficit.
- [PMID: 31498548](https://pubmed.ncbi.nlm.nih.gov/31498548/): delayed vastus activation during gait.

**Ontology:** HP:0003326 (Myalgia).

### Fatigue

**Causal chain**
1. Chronic pain and sleep disturbance (themselves downstream of nodes 1–3) lead to persistent physical and cognitive effort cost.
2. Pain + poor sleep + psychological distress + deconditioning converge on a **chronic fatigue state** *(proposed convergent node)*.
3. The convergent state is experienced as severe, functionally limiting fatigue.

**Evidence grade:** SUPPORTED as a convergent/downstream node (fatigue is determined by, not independent of, pain and sleep).

**Primary human evidence**
- [PMID: 19878973](https://pubmed.ncbi.nlm.nih.gov/19878973/) (human clinical, n=273 EDS): *"More than three-quarters of EDS patients suffer from severe fatigue."* and *"The 5 possible determinants involved in fatigue are sleep disturbances, concentration problems, social functioning, self-efficacy concerning fatigue, and pain severity."*
- [PMID: 20579833](https://pubmed.ncbi.nlm.nih.gov/20579833/): *"pain is correlated with low nocturnal sleep quality"*.

**Non-causal alternatives:** overlap with ME/CFS and dysautonomia; fatigue may partly reflect a shared central/autonomic substrate rather than being purely secondary to pain.

**Ontology:** HP:0012378 (Fatigue).

### Sleep disturbance

**Causal chain**
1. Chronic pain (downstream of nodes 1–3) leads to disrupted nocturnal sleep architecture.
2. In parallel, airway/oropharyngeal laxity contributes to sleep-disordered breathing (see Sleep apnea).
3. Pain-driven arousal plus breathing disturbance results in reduced sleep quality/efficiency.

**Evidence grade:** PROPOSED (pain→sleep link is human-supported; the full mechanistic weighting of airway vs pain vs autonomic contributions is not resolved).

**Primary human evidence**
- [PMID: 20579833](https://pubmed.ncbi.nlm.nih.gov/20579833/): *"pain is correlated with low nocturnal sleep quality"*.
- [PMID: 42417930](https://pubmed.ncbi.nlm.nih.gov/42417930/): hEDS/HSD cases show lower sleep efficiency and higher insomnia.

**Ontology:** HP:0002360 (Sleep disturbance).

### Migraine

**Causal chain (honest)**
1. Primary migraine: NO demonstrated causal chain from connective-tissue laxity. Association is documented but mechanism is not established.
2. Secondary headaches (distinct phenotype within the cluster): connective-tissue laxity (nodes 1/3) leads to specific structural consequences — spontaneous intracranial hypotension/CSF leak, craniocervical instability, temporomandibular dysfunction, Chiari malformation — each of which produces headache through its own mechanism.

**Evidence grade:** Primary migraine = **NOT_ESTABLISHED**; secondary headaches = **PROPOSED** (structurally specific, laxity-plausible).

**Primary human evidence**
- [PMID: 42437376](https://pubmed.ncbi.nlm.nih.gov/42437376/) (meta-analysis, 17,455 hEDS/HSD): migraine prevalence *"migraine (38.2%, 95% CI 19.9-60.5)"*.
- [PMID: 42640494](https://pubmed.ncbi.nlm.nih.gov/42640494/): *"migraine is the most common primary headache phenotype; however, secondary causes, including spontaneous intracranial hypotension, craniocervical instability, temporomandibular dysfunction, Chiari malformation, and vascular complications, occur with increased frequency"*.

**Non-causal alternatives:** migraine is highly prevalent in the general young-female population; much of the association may be ascertainment and shared female predominance rather than laxity-driven causation. Dysautonomia/orthostatic intolerance interacts with headache expression.

**Ontology:** HP:0002076 (Migraine).

### Peripheral neuropathy (including small-fiber neuropathy)

**Causal chain**
1. ECM/connective-tissue abnormality (node 1) is associated with reduced intraepidermal nerve-fiber density.
2. Reduced IENFD constitutes **small-fiber neuropathy** *(proposed new node)*.
3. SFN manifests as sensory small-fiber symptoms (burning pain, dysesthesia) and contributes to the pain hub.

**Evidence grade:** SUPPORTED for the *association/phenotype* (SFN demonstrably present); the *causal link from the specific ECM abnormality to nerve-fiber loss* remains PROPOSED — large-fiber conduction is normal.

**Primary human evidence**
- [PMID: 27306637](https://pubmed.ncbi.nlm.nih.gov/27306637/): *"All patients showed a decrease of IENFD consistent with the diagnosis of small fiber neuropathy (SFN), regardless of the EDS type."*
- [PMID: 26919608](https://pubmed.ncbi.nlm.nih.gov/26919608/): no somatosensory nervous-system damage on NCS/LEP — indicating the lesion is small-fiber/central, not large-fiber.

**Non-causal alternatives:** a COL6A5 genetic contributor to small-fiber pathology/itch has been reported in some hypermobile families ([PMID: 28073787](https://pubmed.ncbi.nlm.nih.gov/28073787/)), raising a shared-genetic rather than purely ECM-mechanical route.

**Ontology:** HP:0000763 (Sensory neuropathy) / HP:0045010 (Small fiber neuropathy); CL:0000101 (sensory neuron).

### Orthostatic tachycardia (postural tachycardia syndrome)

**Causal chain (candidate routes, none fully proven)**
1. Connective-tissue laxity (node 1) → distensible vessel walls → venous pooling → reduced preload → reflex tachycardia. **[This specific venous-compliance route is contradicted by human data — see below.]**
2. Alternative: autonomic small-fiber/peripheral sympathetic dysfunction *(proposed node: dysautonomia/autonomic neuropathy)* → impaired vasoconstriction → orthostatic pooling → compensatory tachycardia.
3. Additional contributors: hyperadrenergic state, deconditioning, hypovolemia, and mast-cell mediator release.

**Evidence grade:** NOT_ESTABLISHED for the mechanism (association is robust; the causal route from laxity is inference and the intuitive venous route is refuted).

**Primary human evidence**
- [PMID: 32434316](https://pubmed.ncbi.nlm.nih.gov/32434316/) (human, tilt-table, 102 hEDS/HSD): *"Abnormal results and head-up tilt test were common and included postural orthostatic tachycardia syndrome (POTS; 48%), orthostatic intolerance (25.5%) and hypotension (3.9%)."*
- [PMID: 28986003](https://pubmed.ncbi.nlm.nih.gov/28986003/) (human, autonomic testing): *"Autonomic testing demonstrated a slight reduction in heart rate variability and slightly lower blood pressures on tilt table testing in hEDS patients, however for most patients these variables remained within the range of normal."* — abnormalities often mild.
- [PMID: 12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/) (human, strain-gauge plethysmography): *"Volume-pressure relations of controls and POTS patients with normal P(v) and high P(v) were not different and were unchanged by orthostasis"* — **refutes increased venous compliance**, implicating arterial vasoconstrictive defects.

**Non-causal alternatives:** POTS, MCAS and hEDS co-cluster through shared female predominance and specialty co-referral; part of the association is ascertainment. Hereditary alpha-tryptasemia co-occurs with hypermobility and POTS without an established causal biochemical link.

**Ontology:** HP:0031547 (Postural orthostatic tachycardia).

### Acrocyanosis

**Causal chain**
1. Orthostatic/dependent **blood pooling** (vasomotor) — a component of orthostatic intolerance — leads to stasis in dependent extremities.
2. Stasis, driven by **arterial vasoconstrictive (autonomic) dysfunction** *(proposed node)* rather than venous distensibility, results in acral cyanotic discoloration.

**Evidence grade:** PROPOSED (vasomotor manifestation of pooling; venous-compliance route explicitly refuted).

**Primary human evidence**
- [PMID: 12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/): *"\"pooling\" (which comprises acrocyanosis and dependent edema when upright)"* and the volume-pressure quote above refuting venous compliance.

**Ontology:** HP:0001063 (Acrocyanosis).

### Gastrointestinal dysmotility

**Causal chain (competing/additive, none proven)**
1. Gut-wall connective-tissue laxity (node 1) → impaired visceral wall mechanics → altered motility; and/or
2. Autonomic dysfunction *(proposed node)* → disordered gut neural control → dysmotility; and/or
3. Visceral hypersensitivity and mast-cell activation *(proposed node)* → altered gut-brain signalling → dysmotility.

**Evidence grade:** NOT_ESTABLISHED (strong epidemiological association, abnormal motility studies, but authoritative review states mechanisms remain theoretical).

**Primary human evidence**
- [PMID: 38747032](https://pubmed.ncbi.nlm.nih.gov/38747032/) (human, 435 hEDS/JHS): constipation 61%, dysphagia 32%, dyspepsia/gastroparesis 25%; *"Motility studies were abnormal in 31% of the 80 patients who underwent them."*
- [PMID: 41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/) (propensity-matched, 59,128 pairs): *"gastroparesis (4.7%, OR 8.2, 95% CI 7.3-9.2, p < 0.001)"*.
- [PMID: 40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/) (AGA Expert Review): *"while theoretical explanations exist, experimental evidence of the biological mechanisms that explain relationships is limited and evolving"*.

**Ontology:** HP:0002579 (Gastrointestinal dysmotility).

### Gastroesophageal reflux

**Causal chain**
1. Connective-tissue laxity and/or autonomic dysfunction → impaired esophagogastric junction competence and delayed gastric emptying → increased reflux.

**Evidence grade:** NOT_ESTABLISHED (association robust; mechanism theoretical).

**Primary human evidence**
- [PMID: 41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/): GERD 18.4% (OR 1.5) in matched EDS cohort.
- [PMID: 40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/): mechanisms "limited and evolving" (quote above).

**Ontology:** HP:0002020 (Gastroesophageal reflux).

### Nausea

**Causal chain**
1. Delayed gastric emptying/gastroparesis and/or autonomic dysfunction *(proposed node)* → impaired gastric accommodation → nausea; interaction with POTS and visceral hypersensitivity.

**Evidence grade:** NOT_ESTABLISHED.

**Primary human evidence**
- [PMID: 38747032](https://pubmed.ncbi.nlm.nih.gov/38747032/): high dyspepsia/gastroparesis prevalence (25%).
- [PMID: 40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/): mechanisms theoretical (quote above).

**Ontology:** HP:0002018 (Nausea).

### Constipation

**Causal chain**
1. Gut-wall laxity and/or autonomic (enteric) dysfunction *(proposed node)* → slowed colonic transit → constipation; pelvic-floor dysfunction may add an outlet component.

**Evidence grade:** NOT_ESTABLISHED (very common; mechanism not demonstrated).

**Primary human evidence**
- [PMID: 38747032](https://pubmed.ncbi.nlm.nih.gov/38747032/): constipation 61%.
- [PMID: 41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/): constipation 12.4% (OR 1.8).
- [PMID: 40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/): mechanisms theoretical.

**Ontology:** HP:0002019 (Constipation).

### Mitral valve prolapse

**Causal chain**
1. Connective-tissue/ECM abnormality (node 1) → myxomatous change / reduced tensile integrity of valve leaflets and chordae → leaflet billowing → mitral valve prolapse (usually mild).

**Evidence grade:** SUPPORTED for the laxity→valve link, with the important qualifier that it is mild and of little clinical consequence.

**Primary human evidence**
- [PMID: 21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/) (human, 252 patients): *"Although aortic root size and MVP are increased in patients with these types of Ehlers-Danlos syndrome, they tend to be of little clinical consequence."*
- [PMID: 42099513](https://pubmed.ncbi.nlm.nih.gov/42099513/) (pediatric echo, n=28): MVP in 32%.

**Ontology:** HP:0001634 (Mitral valve prolapse).

### Aortic root dilatation

**Causal chain**
1. ECM abnormality (node 1) → reduced aortic-wall tensile integrity → mild aortic root dilatation (typically non-progressive in hEDS).

**Evidence grade:** SUPPORTED but explicitly **mild and non-progressive** — distinct from vascular/Marfan-type aortopathy.

**Primary human evidence**
- [PMID: 21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/): *"seven individuals had dilated aortas before age 14, and only one individual continued to show dilation after age 14"* — longitudinal non-progression.
- [PMID: 42099513](https://pubmed.ncbi.nlm.nih.gov/42099513/): aortic Z-scores higher than controls but within normal range.

**Ontology:** HP:0002616 (Aortic root aneurysm/dilatation).

### Hyperextensible skin

**Causal chain**
1. ECM/fibroblast abnormality (node 1) → abnormal dermal collagen fibril morphology and fragmented elastic fibers → reduced dermal tensile integrity → skin hyperextensibility.

**Evidence grade:** SUPPORTED/ESTABLISHED (ultrastructural human evidence).

**Primary human evidence**
- [PMID: 6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/) (human, EM): *"The major alterations observed among collagen fibrils were hieroglyphic-shaped fibrils, collagen flowers, unravelled fibrils and fibrils of normal shape but abnormally large or small diameters"*.

**Ontology:** HP:0000974 (Hyperextensible skin).

### Soft skin

**Causal chain**
1. Abnormal dermal collagen/elastic matrix (node 1) → altered dermal mechanical properties → soft, doughy skin texture.

**Evidence grade:** SUPPORTED (same ultrastructural basis as hyperextensibility).

**Primary human evidence**
- [PMID: 6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/): dermal collagen/elastic fiber abnormalities (quote above).

**Ontology:** HP:0000977 (Soft skin).

### Atrophic scars

**Causal chain**
1. Abnormal dermal collagen matrix (node 1) → impaired wound-healing collagen deposition/organisation → thin, atrophic ("cigarette-paper") scars.

**Evidence grade:** SUPPORTED.

**Primary human evidence**
- [PMID: 6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/): collagen fibril and dermal organisation abnormalities underlying fragile scarring.

**Ontology:** HP:0001075 (Atrophic scars).

### Striae distensae

**Causal chain**
1. Abnormal dermal collagen/elastic matrix (node 1) → reduced dermal resistance to mechanical stretch → dermal tearing/striae.

**Evidence grade:** PROPOSED (plausible from the shared dermal-matrix mechanism; striae are also common in the general population, weakening specificity).

**Primary human evidence**
- [PMID: 6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/): fragmented/branched elastic fibers and collagen abnormalities.

**Non-causal alternatives:** striae occur commonly with normal growth/weight change; attribution to the hEDS matrix defect is partly non-specific.

**Ontology:** HP:0001065 (Striae distensae).

### Easy bruising

**Causal chain**
1. ECM abnormality (node 1) → fragility of capillaries and perivascular connective tissue → vessel rupture with minimal trauma → easy bruising. Coagulation is normal.

**Evidence grade:** SUPPORTED/ESTABLISHED (mechanism named; coagulopathy explicitly excluded).

**Primary human evidence**
- [PMID: 15566352](https://pubmed.ncbi.nlm.nih.gov/15566352/): *"Easy bruising is, to a variable degree, present in all subtypes of EDS, and is because of fragility of the capillaries and the perivascular connective tissues."* and *"Haematological studies including evaluation of clotting factors, platelet aggregation and bleeding time are usually normal in patients with EDS"*.
- [PMID: 19592142](https://pubmed.ncbi.nlm.nih.gov/19592142/): corroborates capillary/perivascular fragility as the bleeding mechanism.

**Ontology:** HP:0000978 (Bruising susceptibility).

### Pelvic organ prolapse

**Causal chain**
1. Connective-tissue laxity (node 1) → weakened pelvic-floor fascial/ligamentous support → descent of pelvic organs → prolapse.

**Evidence grade:** SUPPORTED (meta-analytic and large cross-sectional human association).

**Primary human evidence**
- [PMID: 26658756](https://pubmed.ncbi.nlm.nih.gov/26658756/) (meta-analysis, 14 studies): *"Overall pooled odds ratio (OR) was 2.37 [95 % confidence interval (CI) 1.54-3.64"*.
- [PMID: 42979294](https://pubmed.ncbi.nlm.nih.gov/42979294/) (cross-sectional, 812 women): *"JHM was present in 67.6% (300/444) of POP cases versus 10.9% (40/368) of controls"*.
- [PMID: 34213599](https://pubmed.ncbi.nlm.nih.gov/34213599/): HDCT patients have more perioperative complications (46% vs 22%, p=0.002), consistent with tissue fragility.

**Non-causal alternatives:** familial clustering of pelvic-floor disorders may reflect shared genetic background broader than hEDS.

**Ontology:** HP:0000083 (Pelvic organ prolapse).

### Abdominal wall hernia

**Causal chain**
1. Connective-tissue laxity (node 1) → weakened abdominal fascia/aponeurosis → fascial defect under intra-abdominal pressure → herniation.

**Evidence grade:** PROPOSED (mechanistically analogous to prolapse; less hEDS-specific quantitative evidence collected here).

**Primary human evidence**
- Supported by analogy to the fascial-laxity mechanism documented for pelvic organ prolapse ([PMID: 26658756](https://pubmed.ncbi.nlm.nih.gov/26658756/)) and tissue fragility ([PMID: 34213599](https://pubmed.ncbi.nlm.nih.gov/34213599/)). Direct hEDS hernia-incidence causal data were not isolated in this investigation.

**Ontology:** HP:0100790 (Hernia); HP:0004298 (Abdominal wall defect).

### Dental crowding

**Causal chain (honest)**
1. No demonstrated mechanistic chain from the curated nodes. Proposed-but-unproven: craniofacial connective-tissue/growth differences → altered maxillary arch form → crowding.

**Evidence grade:** NOT_ESTABLISHED.

**Primary human evidence:** none establishing a causal chain was identified; association is descriptive within craniofacial feature lists.

**Non-causal alternatives:** dental crowding is highly prevalent in the general population; the association may be partly ascertainment/descriptive co-feature rather than causal.

**Ontology:** HP:0000678 (Dental crowding).

### High, narrow palate

**Causal chain (honest)**
1. No demonstrated mechanistic chain from the curated nodes. Proposed-but-unproven: craniofacial connective-tissue/maxillary growth differences → high, narrow palatal vault.

**Evidence grade:** NOT_ESTABLISHED. (Relevant mainly as a contributor to upper-airway narrowing — see Sleep apnea.)

**Primary human evidence:** none establishing causation isolated here; the oropharyngeal-abnormality link to OSA is the downstream clinical connection.

**Ontology:** HP:0000218 (High palate); HP:0002705 (High, narrow palate).

### Sleep apnea

**Causal chain**
1. Connective-tissue laxity (node 1) → oropharyngeal/airway soft-tissue and craniofacial laxity → increased upper-airway collapsibility → obstructive sleep apnea.

**Evidence grade:** SUPPORTED (large pediatric cohort risk estimate; mechanism attributed to oropharyngeal abnormalities; CPAP response altered).

**Primary human evidence**
- [PMID: 40609249](https://pubmed.ncbi.nlm.nih.gov/40609249/) (pediatric, 10,104 EDS): *"652 (6.45 %, 95 % CI: 5.99-6.95) had a recorded diagnosis of OSA with a 4.43 (95 % CI: 4.12-4.78) times higher risk of diagnosis compared to a control cohort"*.
- [PMID: 42417930](https://pubmed.ncbi.nlm.nih.gov/42417930/): *"Oropharyngeal abnormalities in hEDS/HSD may exacerbate OSA"*.

**Ontology:** HP:0002870 (Obstructive sleep apnea).

### Anxiety

**Causal chain (competing routes, non-causal alternative live)**
1. Downstream route: chronic pain + dysautonomia + interoceptive sensitivity → heightened threat appraisal → anxiety.
2. Shared-substrate route *(proposed node: shared amygdala/interoceptive neural substrate)*: hypermobility co-occurs with structural amygdala differences and heightened interoceptive sensitivity independent of manifest anxiety — i.e., a shared neural trait, not a pure downstream effect.

**Evidence grade:** PROPOSED, with a strong live non-causal (shared-substrate) alternative.

**Primary human evidence**
- [PMID: 22539777](https://pubmed.ncbi.nlm.nih.gov/22539777/) (human VBM, n=72): *"bilateral amygdala volume distinguished those with from those without hypermobility. The hypermobility group scored higher for interoceptive sensitivity yet were not significantly more anxious"*.
- [PMID: 25089514](https://pubmed.ncbi.nlm.nih.gov/25089514/) (cohort): *"PD was associated with the number of physical diseases suffered and the joint hypermobility syndrome"*.
- [PMID: 41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/): anxiety 26.1% (OR 1.8).

**Ontology:** HP:0000739 (Anxiety).

### Depression

**Causal chain (honest)**
1. Candidate downstream route: chronic pain + fatigue + disability + poor sleep → reactive mood disturbance → depression. The specific causal weighting is not demonstrated.

**Evidence grade:** NOT_ESTABLISHED (association present; no demonstrated mechanistic chain; shared-substrate and ascertainment explanations open).

**Primary human evidence**
- [PMID: 41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/): depression 18.7% (OR 1.3) — a modest association.

**Non-causal alternatives:** shared neurodevelopmental/autonomic substrate (as for anxiety); ascertainment through tertiary-referral populations with high symptom burden.

**Ontology:** HP:0000716 (Depression).

---

## Mechanistic Model / Interpretation

The wiring resolves into **five hubs** fanning out from the three curated nodes, with confidence decreasing as the chain moves from direct mechanics toward neuro-autonomic physiology.

```
 CURATED NODES                         HUBS / INTERMEDIATES                 PHENOTYPES
 ┌─────────────────────┐
 │ 1. ECM remodeling   │──┐
 │    abnormality      │  │   (d) TISSUE-LAXITY (mechanical)   ──► hypermobility, dislocation,
 ├─────────────────────┤  ├──► dermal matrix defect ───────────►   soft/hyperextensible skin,
 │ 2. Myofibroblast    │  │    perivascular fragility ─────────►   atrophic scars, striae, easy bruising
 │    transition       │  │    fascial/valve/airway laxity ────►   POP, hernia, MVP, aortic dilatation(mild),
 ├─────────────────────┤  │                                        OSA           [SUPPORTED/ESTABLISHED]
 │ 3. Joint instability│──┘
 │  + soft-tissue injury│      (a) PAIN HUB
 └─────────────────────┘      ├── central sensitization *NEW* ───► chronic pain, arthralgia, myalgia
            │                 └── small-fiber neuropathy *NEW* ───► neuropathic pain, periph. neuropathy
            │                                                                   [SUPPORTED]
            │                 (b) AUTONOMIC HUB  *dysautonomia NEW*
            │                 ├── arterial vasoregulatory defect ─► POTS, orthostatic intolerance
            │                 └── (NOT venous compliance — refuted) ► acrocyanosis/pooling  [PROPOSED/NOT_ESTAB]
            │                 (c) GI HUB  *autonomic + visceral hypersensitivity + MCAS NEW*
            │                 └──────────────────────────────────► dysmotility, reflux, nausea,
            │                                                       constipation      [NOT_ESTABLISHED]
            │                 (e) PSYCH HUB
            ├── pain/dysautonomia (downstream) ───────────────────► depression  [NOT_ESTABLISHED]
            └── shared amygdala/interoceptive substrate *NEW* ────► anxiety      [PROPOSED; non-causal live]
                CONVERGENT: pain + sleep + distress ─────────────► fatigue      [SUPPORTED, downstream]
```

**Grading overview**

| Grade | Phenotypes |
|---|---|
| ESTABLISHED | Joint hypermobility |
| SUPPORTED | Joint dislocation, chronic pain, arthralgia, myalgia, peripheral neuropathy, fatigue, hyperextensible skin, soft skin, atrophic scars, easy bruising, pelvic organ prolapse, mitral valve prolapse, aortic root dilatation (mild/non-progressive), sleep apnea |
| PROPOSED | Sleep disturbance, acrocyanosis, striae distensae, abdominal wall hernia, secondary headache, anxiety |
| NOT_ESTABLISHED | Orthostatic tachycardia (mechanism), GI dysmotility, reflux, nausea, constipation, primary migraine, depression, dental crowding, high narrow palate |

Two human-data constraints keep the model honest: orthostatic pooling/acrocyanosis is **not** explained by increased venous compliance ([PMID: 12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/)), and hEDS aortic dilatation is **mild and non-progressive** ([PMID: 21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/)).

---

## Evidence Base

| PMID | Source type | Supports |
|---|---|---|
| [26919608](https://pubmed.ncbi.nlm.nih.gov/26919608/) | Human QST | Central sensitization as pain mechanism |
| [27306637](https://pubmed.ncbi.nlm.nih.gov/27306637/) | Human skin biopsy | Small-fiber neuropathy common in EDS |
| [7283686](https://pubmed.ncbi.nlm.nih.gov/7283686/) | Human clinical | Proprioceptive deficit, muscle weakness |
| [31498548](https://pubmed.ncbi.nlm.nih.gov/31498548/) | Human EMG | Altered neuromuscular activation in gait |
| [32434316](https://pubmed.ncbi.nlm.nih.gov/32434316/) | Human tilt-table | POTS/OI prevalence |
| [28986003](https://pubmed.ncbi.nlm.nih.gov/28986003/) | Human autonomic testing | Autonomic abnormalities mild |
| [12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/) | Human plethysmography | Refutes venous-compliance route to pooling/acrocyanosis |
| [41432355](https://pubmed.ncbi.nlm.nih.gov/41432355/) | Human matched cohort | GI, anxiety, depression, POTS risk estimates |
| [38747032](https://pubmed.ncbi.nlm.nih.gov/38747032/) | Human cohort | GI prevalence and abnormal motility |
| [40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/) | Expert review | GI mechanisms remain theoretical |
| [21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/) | Human longitudinal echo | MVP/aortic dilatation mild, non-progressive |
| [42099513](https://pubmed.ncbi.nlm.nih.gov/42099513/) | Human pediatric echo | MVP 32%, aortic Z within normal |
| [15566352](https://pubmed.ncbi.nlm.nih.gov/15566352/) | Human review | Bruising = capillary/perivascular fragility, not coagulopathy |
| [19592142](https://pubmed.ncbi.nlm.nih.gov/19592142/) | Human review | Corroborates bleeding mechanism |
| [22539777](https://pubmed.ncbi.nlm.nih.gov/22539777/) | Human VBM | Shared amygdala/interoceptive substrate |
| [25089514](https://pubmed.ncbi.nlm.nih.gov/25089514/) | Human cohort | Hypermobility a risk factor for panic disorder |
| [19878973](https://pubmed.ncbi.nlm.nih.gov/19878973/) | Human cohort | Fatigue prevalence and determinants |
| [20579833](https://pubmed.ncbi.nlm.nih.gov/20579833/) | Human cohort | Pain–sleep link |
| [26658756](https://pubmed.ncbi.nlm.nih.gov/26658756/) | Meta-analysis | Hypermobility–POP OR 2.37 |
| [42979294](https://pubmed.ncbi.nlm.nih.gov/42979294/) | Human cross-sectional | JHM in 67.6% of POP cases |
| [34213599](https://pubmed.ncbi.nlm.nih.gov/34213599/) | Human cohort | Tissue fragility, surgical complications |
| [40609249](https://pubmed.ncbi.nlm.nih.gov/40609249/) | Human cohort | OSA RR 4.43 in EDS children |
| [42417930](https://pubmed.ncbi.nlm.nih.gov/42417930/) | Human case-control | OSA attributed to oropharyngeal laxity |
| [6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/) | Human EM | Dermal collagen/elastic fibril abnormalities |
| [42640494](https://pubmed.ncbi.nlm.nih.gov/42640494/) | Review | Migraine predominance; secondary-headache mechanisms |
| [42437376](https://pubmed.ncbi.nlm.nih.gov/42437376/) | Meta-analysis | Migraine prevalence 38.2% |
| [35449490](https://pubmed.ncbi.nlm.nih.gov/35449490/) | Review | Mast-cell mediators disrupt connective tissue |
| [34674068](https://pubmed.ncbi.nlm.nih.gov/34674068/) | Human | Neuropathic POTS, pooling, leg pain |
| [28073787](https://pubmed.ncbi.nlm.nih.gov/28073787/) | Human genetics | COL6A5 variants, SFN/itch in hypermobile families |

---

## Proposed New Mechanism Nodes

| Suggested node | Upstream node | Downstream phenotypes | Strongest citation |
|---|---|---|---|
| Central sensitization (nociplastic pain amplification) | Node 3 (joint instability/injury) | Chronic pain, arthralgia, myalgia | [PMID: 26919608](https://pubmed.ncbi.nlm.nih.gov/26919608/) |
| Small-fiber neuropathy (reduced IENFD) | Node 1 (ECM abnormality) | Peripheral neuropathy, neuropathic pain | [PMID: 27306637](https://pubmed.ncbi.nlm.nih.gov/27306637/) |
| Proprioceptive deficit / altered neuromuscular control | Node 3 | Joint dislocation, arthralgia, myalgia | [PMID: 7283686](https://pubmed.ncbi.nlm.nih.gov/7283686/) |
| Dysautonomia / autonomic (small-fiber) neuropathy — arterial vasoregulatory defect | Node 1 | POTS, acrocyanosis, GI dysmotility, nausea | [PMID: 12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/) |
| Visceral hypersensitivity | Node 1 / dysautonomia | Dysmotility, reflux, nausea, constipation | [PMID: 40387691](https://pubmed.ncbi.nlm.nih.gov/40387691/) |
| Mast-cell activation (MCAS) | Node 1 | POTS, GI symptoms, cutaneous symptoms | [PMID: 35449490](https://pubmed.ncbi.nlm.nih.gov/35449490/) |
| Perivascular/capillary fragility | Node 1 | Easy bruising | [PMID: 15566352](https://pubmed.ncbi.nlm.nih.gov/15566352/) |
| Dermal collagen/elastic matrix defect | Node 1 | Hyperextensible skin, soft skin, atrophic scars, striae | [PMID: 6806400](https://pubmed.ncbi.nlm.nih.gov/6806400/) |
| Fascial/ligamentous support failure (site-specific) | Node 1 | Pelvic organ prolapse, abdominal wall hernia | [PMID: 26658756](https://pubmed.ncbi.nlm.nih.gov/26658756/) |
| Oropharyngeal/airway soft-tissue laxity | Node 1 | Obstructive sleep apnea | [PMID: 42417930](https://pubmed.ncbi.nlm.nih.gov/42417930/) |
| Valvular/aortic-wall tensile failure (mild) | Node 1 | Mitral valve prolapse, aortic root dilatation | [PMID: 21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/) |
| Chronic fatigue state (convergent) | Pain + sleep + distress | Fatigue | [PMID: 19878973](https://pubmed.ncbi.nlm.nih.gov/19878973/) |
| Shared amygdala/interoceptive neural substrate | Shared trait with node 1 context | Anxiety (and possibly depression) | [PMID: 22539777](https://pubmed.ncbi.nlm.nih.gov/22539777/) |

---

## Unwired Phenotypes (graded NOT_ESTABLISHED)

- **Orthostatic tachycardia (mechanism):** a controlled study measuring venous compliance, arterial vasoconstrictor responses, catecholamines, and autonomic small-fiber integrity in biopsy-confirmed hEDS vs matched POTS-without-hEDS would settle which route predominates.
- **Gastrointestinal dysmotility:** case-control manometry/gastric-emptying studies stratified by autonomic status and mast-cell markers, ideally with a mechanistic intervention (e.g., prokinetic or mast-cell stabiliser response), would move this beyond association.
- **Gastroesophageal reflux:** esophagogastric junction manometry and pH-impedance in hEDS vs controls, correlated with connective-tissue and autonomic measures, would establish or exclude a laxity/autonomic route.
- **Nausea:** gastric-emptying and accommodation studies linking nausea severity to measured gastroparesis and POTS status would clarify its driver.
- **Constipation:** colonic transit and anorectal/pelvic-floor physiology studies distinguishing slow-transit (neuromuscular) from outlet (fascial) mechanisms are needed.
- **Primary migraine:** a genetically informative or family-based study separating shared female/general-population migraine risk from a laxity-specific effect would settle causation.
- **Depression:** longitudinal mediation analysis testing whether depression is explained by pain/disability/sleep versus a shared substrate independent of these.
- **Dental crowding:** controlled craniofacial morphometric studies testing whether arch form in hEDS differs beyond population norms and relates to a connective-tissue measure.
- **High, narrow palate:** the same craniofacial morphometric approach, additionally linking palatal vault geometry to measured upper-airway collapsibility.

---

## Limitations and Knowledge Gaps

1. **Ascertainment and co-referral dominate the autonomic/GI/psychiatric associations.** hEDS, POTS and MCAS co-cluster in tertiary clinics and share a strong female predominance; much of the apparent wiring could be selection rather than causation.
2. **The curated upstream nodes themselves are hypothetical/provisional** (in-vitro fibroblast evidence only). Any chain inherits that uncertainty; "ECM abnormality → phenotype" is only as solid as the ECM node.
3. **No causal gene** means no genetic anchor to test directionality; mediation remains observational.
4. **Several "SUPPORTED" dermal/cardiac chains rest on mixed EDS cohorts** (classic + hypermobile), so hEDS-specific effect sizes are imprecise.
5. **The abdominal-wall hernia chain was reasoned by analogy** to pelvic prolapse rather than from isolated hEDS hernia-incidence data.

## Proposed Follow-up Experiments / Actions

1. Add the 13 proposed intermediate nodes to the knowledge graph with their graded edges, explicitly tagging central sensitization and small-fiber neuropathy as the two SUPPORTED pain intermediates.
2. Encode the **refutation edge**: "increased venous compliance → pooling/acrocyanosis" marked DISPROVEN by [PMID: 12010910](https://pubmed.ncbi.nlm.nih.gov/12010910/), redirecting the acrocyanosis/POTS route to the arterial-vasoregulatory (dysautonomia) node.
3. Flag the cardiac-laxity edges as "mild/non-progressive" per [PMID: 21193204](https://pubmed.ncbi.nlm.nih.gov/21193204/) to prevent over-escalation to vascular-EDS-type surveillance.
4. Commission the targeted human studies listed under *Unwired Phenotypes* to convert NOT_ESTABLISHED chains to graded edges.
5. Test the **shared-substrate vs downstream** hypothesis for anxiety/depression with longitudinal mediation and amygdala imaging, keeping the non-causal alternative live until adjudicated.


## Artifacts

- [OpenScientist final report](Hypermobile_Ehlers-Danlos_Syndrome-phenotype-wiring-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypermobile_Ehlers-Danlos_Syndrome-phenotype-wiring-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 0 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 37 |
| Terms named correctly | 32 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0045010` (1 mention) - the report calls it "Small fiber neuropathy"; HP calls it **Abnormal peripheral nerve morphology by anatomical site**
- `HP:0031547` (1 mention) - the report calls it "Postural orthostatic tachycardia"; HP calls it **Abnormal QT interval**
- `HP:0000083` (1 mention) - the report calls it "Pelvic organ prolapse"; HP calls it **Renal insufficiency**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002616` (1 mention) - the report calls it "Aortic root aneurysm/dilatation"; HP calls it **Aortic root aneurysm**, and lists "Aortic root dilatation" among its other names
- `HP:0004298` (1 mention) - the report calls it "Abdominal wall defect"; HP calls it **Abnormal abdominal wall morphology**