# hEDS: Comorbidities, Disease Trajectories, and Pathomechanisms — Literature Review

*Date: 2026-07-28. Scope: hypermobile Ehlers-Danlos syndrome (hEDS) and the closely
adjacent hypermobility spectrum disorders (HSD). Sources retrieved from PubMed;
every claim below is anchored to a PMID whose abstract was read directly.*

## Executive summary

1. **The comorbidity picture is well described but weakly mechanistically explained.**
   Every major review converges on the same multisystem cluster — chronic pain,
   fatigue, dysautonomia/POTS, disorders of gut–brain interaction (DGBI), mast cell
   activation, anxiety/neurodevelopmental conditions — but the 2025 AGA expert review
   states plainly that "experimental evidence of the biological mechanisms that explain
   relationships is limited and evolving" (PMID:40387691).
2. **The "trifecta" (hEDS + POTS + MCAS) is contested, not settled.** It is
   simultaneously the organising frame of the clinical literature *and* the target of a
   substantive skeptical review arguing the association is an artifact of overlapping
   subjective symptom pools (PMID:31267471). Any dismech curation must represent both
   positions.
3. **Objective physiological findings are stronger than the nosology.** The largest
   instrumented hEDS series (n=270) found reduced orthostatic cerebral blood flow
   velocity in 79%, POTS in 33%, and small fiber neuropathy in 64–82% (PMID:40843452) —
   these are measurements, not symptom checklists, and they are the most defensible
   mechanistic anchors currently available.
4. **Trajectory evidence is thin.** The only explicit natural-history staging model
   (hypermobility → pain → stiffness phases) rests on a 21-patient pilot from 2010
   (PMID:20140961). There is no large longitudinal cohort establishing directionality
   between hEDS and its comorbidities. Sequence claims should be curated as hypotheses.
5. **The first common-variant genetics arrived in 2025 and is still a preprint.** A GWAS
   meta-analysis (1,815 cases / 5,008 controls) reports two genome-wide significant loci
   and — importantly for comorbidity modeling — LD-score genetic correlations with
   ME/CFS, fibromyalgia, depression, anxiety, ASD, migraine, and GI disease
   (PMID:41001447). Preprint status must be flagged if used.

---

## 1. Comorbidities

### 1.1 The multisystem cluster

The Mayo/MUSC registry study is the largest systematic comorbidity dataset: 2,149
clinically diagnosed hEDS patients, self-reported survey, K-means clustering. It
identified **three distinct phenotypic clusters** and — a notable negative result —
concluded that **Beighton scores are unreliable for multimorbidity phenotyping**
(PMID:38779137). This matters for dismech: joint-laxity severity does not index
multisystem burden, so a comorbidity model keyed on hypermobility score would be
mis-specified.

Caveats: cross-sectional, self-reported, registry-recruited (ascertainment bias toward
severely affected and highly engaged patients), and clinically — not genetically —
diagnosed.

### 1.2 Gastrointestinal (best-quantified comorbidity)

A systematic review reports GI symptom prevalences in HSD/hEDS versus non-HSD/hEDS
comparators (PMID:35750466):

| Symptom | HSD/hEDS | Comparator | p |
|---|---|---|---|
| Abdominal pain | 69% | 27% | <0.0001 |
| Constipation | 73% | 16% | <0.001 |
| Diarrhea | 47% | 9% | <0.001 |
| Postprandial fullness | 34% | 16% | 0.01 |

The dominant GI phenotype is **disorders of gut–brain interaction**, particularly
functional dyspepsia — not structural bowel disease. Proposed contributors: connective
tissue laxity and its functional consequences, autonomic dysfunction, medication effects,
and comorbid mental health disorders (PMID:35750466).

The 2025 AGA Clinical Practice Update adds two specific, testable GI observations
(PMID:40387691):
- **Pelvic floor dysfunction, especially rectal hyposensitivity**, is highly prevalent —
  it recommends anorectal manometry/balloon expulsion/defecography for lower GI symptoms.
- **Abnormal gastric emptying may be more common than in the general population**, in
  hEDS/HSD patients with comorbid POTS specifically.

It also advises **earlier celiac testing** in hEDS/HSD across GI presentations, not only
diarrhea — a concrete co-occurrence signal (celiac disease is already in `kb/disorders/`).

### 1.3 Dysautonomia / POTS

Reviews frame neurocardiovascular dysautonomia — chiefly POTS — as a core hEDS
comorbidity, and note that **POTS onset is often linked to a discrete precipitating
event: infection, trauma, surgery, or stress** (PMID:34766441). That is the closest thing
in this literature to a mechanistic trajectory trigger.

The instrumented Brigham series (270 hEDS patients vs 29 controls) is the strongest
objective dataset (PMID:40843452):

| Finding | Prevalence in hEDS |
|---|---|
| Reduced orthostatic cerebral blood flow velocity | 79% |
| Widespread but **mild** autonomic failure on testing | 90% |
| POTS on head-up tilt | 33% |
| Hypocapnic cerebral hypoperfusion | 22% |
| Orthostatic cerebral hypoperfusion syndrome | 18% |
| Neurogenic orthostatic hypotension | 9% |
| Small fiber neuropathy (structural criteria) | 64% |
| Small fiber neuropathy (structural + functional) | 82% |

Two things stand out. First, **cerebral hypoperfusion is more prevalent than POTS
itself** — orthostatic symptoms in hEDS are not reducible to heart-rate criteria.
Second, **small fiber neuropathy at 64–82%** is a candidate unifying substrate linking
autonomic dysfunction, chronic pain, and GI dysmotility. The existing dismech hEDS entry
carries `Peripheral neuropathy` (HP:0009830) but not small fiber neuropathy specifically.

Caveat: tertiary autonomic-referral population; the control arm (n=29) is small.

### 1.4 Mast cell activation

This is the weakest link in the triad, and the literature is openly split.

**For:** A retrospective chart review (195 records) found MCAS in **31%** of the POTS+EDS
group versus **2%** of the non-POTS/EDS group, OR 32.46 (PMID:33980338).

**Against:** A systematic review of the hEDS–POTS–MCAS literature found that of 88+136
search combinations, only four (narrow) and nine (broad) papers were original research,
and **no paper resulted from combining search terms for all three conditions**. Its
conclusion: "current evidence is lacking on the existence of MCAS or hEDS as separate or
significant clinical entities," and the apparent association "stems from an overlapping
pool of vague, subjective symptoms" (PMID:31267471).

**Practice position:** The AGA update takes the middle road — clinicians should be aware
of the observed associations, but **universal POTS/MCAS testing in all hEDS/HSD patients
is not supported by current evidence** (PMID:40387691). It sets a concrete diagnostic
threshold: tryptase at baseline and 1–4 h post-flare, with an increase of **20% above
baseline plus 2 ng/mL** required to demonstrate mast cell activation.

**Mechanistic hypothesis:** A mechanobiology review proposes that reduced tissue
stiffness in EDS is itself the link to mast cell degranulation — i.e. the comorbidity is
a downstream consequence of the matrix defect rather than an independent disease
(PMID:35547807). This is a hypothesis, not a demonstrated pathway.

### 1.5 Chronic pain

Roughly **90% of EDS patients report some form of chronic pain**, often as one of the
first symptoms, and it is multifactorial: joint subluxations/dislocations, prior surgery,
muscle weakness, proprioceptive disorders, vertebral instability, plus generalized body
pain, headaches, GI pain, TMJ pain, dysmenorrhea, and vulvodynia (PMID:28186390).

Quantitative sensory testing supports **central pain facilitation** as a mechanism: 20
women with hEDS versus 20 matched controls showed reduced pressure pain thresholds and
significantly **increased temporal summation of pain**; exercise-induced hypoalgesia was
reduced at the quadriceps; conditioned pain modulation results were inconclusive
(PMID:35442549). A parallel adolescent feasibility study exists but is
methodology-focused and underpowered for prevalence claims (PMID:37316864).

### 1.6 Fatigue / ME-CFS

Chronic fatigue is a major driver of impaired quality of life, and there is explicit
symptom overlap with chronic fatigue syndrome — the review argues that **"a proportion of
those with CFS likely have EDS that has not been identified"** (PMID:28186393). Named
contributors: sleep disorders, chronic pain, deconditioning, cardiovascular autonomic
dysfunction, bowel and bladder dysfunction, psychological factors, nutritional
deficiencies. This is a *diagnostic-overlap* claim as much as a comorbidity claim, which
is exactly the confound that makes hEDS comorbidity curation hard.

### 1.7 Psychiatric and neurodevelopmental

The strongest and most replicated psychiatric association is **anxiety**; there is
growing but more limited evidence for depression, eating disorders, neurodevelopmental
disorders, and alcohol/tobacco misuse (PMID:28186381). The proposed mechanisms are
notably *not* purely psychological: genetic risk, autonomic dysfunction, **increased
exteroceptive and interoceptive sensitivity, decreased proprioception**, and neuroimaging
evidence of increased responsiveness in emotion-processing brain regions. The authors
name this the **"neuroconnective phenotype."**

For autism, a systematic review with prevalence meta-analysis (20 studies; 12 of 15
association studies significant) reports (PMID:40145613):
- Joint hypermobility in autistic individuals: **22.3%** overall, **31%** when clinically
  (not self-) assessed
- HSD/EDS in autistic samples: **27.9%** overall, **39%** when clinically assessed

### 1.8 Migraine

Migraine is described as one of the most common comorbidities of POTS, HSD, and MCAS, and
conversely these are prevalent in migraine patients with multisystem symptoms
(PMID:37847487). This is a review-level claim about a shared cluster rather than an
independent effect estimate.

### 1.9 Respiratory (under-recognized)

One case-control study estimated **twofold to threefold greater respiratory disease
burden** in EDS versus controls (PMID:34811894). Mechanistically distinct arms:
structural (pectus deformity, scoliosis, recurrent rib subluxation, tracheobronchomalacia),
functional aerodigestive (**inducible laryngeal obstruction misdiagnosed as asthma**,
with GE dysmotility/reflux contributing), inflammatory (costochondritis, bronchiectasis,
localized mast cell activation), and neurological (**craniocervical instability
dysregulating respiratory control pathways**).

---

## 2. Disease trajectories

### 2.1 The three-phase model — and its evidentiary weight

The only explicit natural-history staging in this literature comes from a **21-patient
pilot study** proposing three phases distinguished by dominant manifestations
(PMID:20140961):

1. **Hypermobility phase**
2. **Pain phase**
3. **Stiffness phase**

The same study identified Arnold-Chiari type I malformation, dolichocolon, and dysphonia
as additional, apparently uncommon findings. This model is widely cited and clinically
resonant, but n=21, single-center, and pre-dates the 2017 criteria — it should be curated
as a **hypothesis with EMERGING status**, not as an established progression.

### 2.2 What the current dismech entry says

`kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml` currently models progression as
"lifelong variable multisystem disorder" plus "recurrent instability and chronic symptom
burden," citing GeneReviews (PMID:20301456) on variable expression. That is defensible
and conservative — the literature does **not** support a fixed degenerative sequence — but
it omits the phase model and the trigger-event observation below.

### 2.3 Trigger events (the best-supported directional claim)

POTS onset in EDS/HSD "may be linked to an event such as infection, trauma, surgery, or
stress" (PMID:34766441). This is the clearest available statement of temporal ordering:
hEDS as a *susceptibility state*, with a discrete environmental precipitant converting it
into overt autonomic disease. It is a review assertion, not a cohort-derived hazard ratio.

### 2.4 Diagnostic delay as a trajectory feature

Recognition delay is repeatedly described: "for many, there is delay in clinicians
recognizing the nature of the symptoms, and recognizing EDS or HSD, leading to delays in
treatment" (PMID:34766441). This means **EHR-derived trajectories for hEDS are
systematically distorted** — the coded hEDS diagnosis typically post-dates the coded
comorbidity diagnoses. Any Disease-Trajectories/ICEES-style directional signal involving
hEDS should carry an explicit ascertainment-bias caveat; naive A-before-B inference will
report comorbidities as *causes* of hEDS.

### 2.5 What is missing

No large longitudinal cohort establishes directionality between hEDS and any comorbidity.
There is no published hEDS mortality or disability-progression study in this retrieved
set. Trajectory modeling in dismech should therefore be hypothesis-typed throughout.

---

## 3. Pathomechanisms

### 3.1 The central fact: no validated causal gene

hEDS is the only EDS subtype without a defined molecular cause; variability in symptom
spectrum, severity, and progression is attributed to age, sex, lifestyle, and expression
domains of connective-tissue genes across development and postnatal life (PMID:32629534).
Diagnosis remains clinical, by the 2017 criteria.

### 3.2 Matrix / cellular mechanisms (already partly in dismech)

The existing entry captures the strongest cell-level findings: ECM disorganization,
preferential αvβ3 integrin recruitment signaling through ILK to Snail1, high MMP9, and a
myofibroblast-like fibroblast transition (PMID:31409039, PMID:29587413). These are
patient-fibroblast findings — candidate mechanisms, not biomarkers.

### 3.3 The fascia-centered framework (new synthesis)

A 2025 narrative review proposes reframing hEDS/HSD as **disorders of pathological
fascial remodeling**, synthesizing transcriptomic, histological, and imaging findings:
abnormal fascial thickness, impaired interfascial gliding, myofibroblast activation,
tendon elongation, and altered tissue stiffness (PMID:40565051). Its appeal is that it
offers one substrate for symptoms otherwise treated as separate comorbidities — pain,
proprioceptive failure, autonomic involvement. It is a hypothesis-generating review, not
primary evidence, and shares authorship with the clinical-review community it summarizes.

### 3.4 Mechanobiology of the comorbidities

Reduced tissue elastic modulus and ultimate strength are documented across EDS tissues;
the proposal is that **the comorbidities themselves may be consequences of reduced tissue
stiffness**, with mast cell degranulation (hEDS/cEDS) and impaired wound healing as the
worked examples (PMID:35547807). This is the most explicit attempt in the literature to
derive comorbidity from the primary matrix defect rather than positing independent
diseases.

### 3.5 Neuro-immune / genetic mechanisms (2025, preprint)

The first hEDS GWAS meta-analysis (1,815 cases, 5,008 ancestry-matched controls,
6.2 M variants) reports (PMID:41001447):
- **Two genome-wide significant loci**, including a regulatory region near **ACKR3**
  (atypical chemokine receptor 3) on chromosome 2. Risk alleles colocalize with eQTLs in
  **tibial nerve**, alter enhancer activity, and generate an AHR transcription-factor
  regulatory site — implicating **neuroimmune and pain signaling**.
- Gene-based/TWAS hits including a **zinc transporter previously implicated in a rare
  form of EDS** and a gene involved in CNS development.
- **LD-score genetic correlations** between hEDS and joint hypermobility, **ME/CFS,
  fibromyalgia, depression, anxiety, ASD, migraine, and GI diseases.**

This last point is the single most important result for comorbidity curation: it is the
first evidence that the hEDS comorbidity cluster has **shared common-variant genetic
architecture**, rather than being purely a referral or symptom-overlap artifact — i.e.
direct counter-evidence to the skeptical position in §1.4.

**Status caveat: this is a medRxiv preprint (DOI 10.1101/2025.09.19.25336146).** Under
dismech evidence policy it should be cited only with explicit preprint flagging, and
comorbidity entries should not rest on it alone.

### 3.6 Convergent mechanistic model

Synthesizing the above, the defensible current model is a **three-layer convergence**:

```
Unresolved connective-tissue / fascial matrix defect
  (ECM disorganization, αvβ3-ILK-Snail1, MMP9, myofibroblast transition,
   reduced tissue stiffness, impaired interfascial gliding)
        |
        +--> joint instability, recurrent injury, proprioceptive failure
        |         |
        |         +--> nociceptive input --> central sensitization
        |                (increased temporal summation, reduced EIH)
        |
        +--> vascular/connective distensibility + small fiber neuropathy
        |         |
        |         +--> orthostatic cerebral hypoperfusion, POTS
        |                (precipitated by infection/trauma/surgery/stress)
        |
        +--> visceral laxity + autonomic dysregulation + pelvic floor dysfunction
        |         |
        |         +--> disorders of gut-brain interaction, dysmotility
        |
        +--> [hypothesized] altered matrix mechanics --> mast cell degranulation
                  |
                  +--> MCAS-like multisystem symptoms

Shared genetic layer (preprint): neuroimmune/pain-signaling common variants
  correlating hEDS with ME/CFS, fibromyalgia, migraine, anxiety, depression, ASD, GI
```

Every arrow above is `INDIRECT_UNKNOWN_INTERMEDIATES` or weaker. None is a demonstrated
causal pathway.

---

## 4. Implications for the dismech knowledge base

### 4.1 Gaps in the current hEDS entry

`kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml` (655 lines) is well-evidenced but
predates or omits:

| Gap | Supporting source |
|---|---|
| **Small fiber neuropathy** as a distinct phenotype (64–82%) | PMID:40843452 |
| **Orthostatic cerebral hypoperfusion** (79%) — more prevalent than POTS | PMID:40843452 |
| **Central sensitization** as a pathophysiology node (increased temporal summation) | PMID:35442549 |
| **Pelvic floor dysfunction / rectal hyposensitivity** | PMID:40387691 |
| Quantitative GI symptom frequencies (constipation 73%, abdominal pain 69%) | PMID:35750466 |
| **Three-phase natural history** as a `mechanistic_hypotheses` entry | PMID:20140961 |
| Fascial-remodeling mechanism branch | PMID:40565051 |
| Common-variant genetic architecture (preprint-flagged) | PMID:41001447 |
| Note that **Beighton score does not index multimorbidity** | PMID:38779137 |

### 4.2 Candidate `kb/comorbidities/` entries

Partner disorders already present in `kb/disorders/`, so these are curatable now:

| Pair | Directionality | Strongest evidence | Confidence |
|---|---|---|---|
| hEDS ↔ Postural Orthostatic Tachycardia Syndrome | `UNKNOWN` (hEDS is the susceptibility state; POTS onset event-triggered) | POTS 33% on tilt in n=270 (PMID:40843452); PMID:34766441 | **High** |
| hEDS ↔ Irritable Bowel Syndrome / DGBI | `UNKNOWN` | Symptom prevalence table, PMID:35750466; PMID:40387691 | **High** |
| hEDS ↔ Fibromyalgia | `UNKNOWN` | Central sensitization QST, PMID:35442549; genetic correlation, PMID:41001447 (preprint) | Moderate |
| hEDS ↔ ME/CFS | `UNKNOWN`, with explicit **diagnostic-overlap** caveat | PMID:28186393; PMID:41001447 (preprint) | Moderate |
| hEDS ↔ Autism Spectrum Disorder | `UNKNOWN` | Prevalence meta-analysis, PMID:40145613 | Moderate |
| hEDS ↔ Generalized Anxiety Disorder | `UNKNOWN` | PMID:28186381 ("neuroconnective phenotype") | Moderate |
| hEDS ↔ Migraine | `UNKNOWN` | PMID:37847487 (review-level) | Low–moderate |
| hEDS ↔ Celiac Disease | `UNKNOWN` | PMID:40387691 (earlier-testing recommendation) | Low |

**MCAS is not curatable as a comorbidity entry yet** — there is no MCAS disorder file in
`kb/disorders/` (only `Systemic_Mastocytosis` and `Maculopapular_Cutaneous_Mastocytosis`,
which are distinct clonal entities), and the association is actively contested
(PMID:31267471 vs PMID:33980338). If curated, it must carry both sides.

### 4.3 Curation guardrails specific to hEDS

1. **Directionality should default to `UNKNOWN`.** Diagnostic delay (§2.4) means EHR
   temporal ordering is systematically misleading for this disease.
2. **Every comorbidity entry needs a `discussions` block with `kind: KNOWLEDGE_GAP`**
   recording that mechanism evidence is "limited and evolving" (PMID:40387691).
3. **Ascertainment bias is the dominant confound.** The two largest datasets
   (PMID:38779137 registry, PMID:40843452 autonomic referral centre) both over-sample
   severely affected patients.
4. **Do not use Beighton score or hypermobility severity as a proxy for comorbidity
   burden** (PMID:38779137).
5. **The skeptical position must be represented,** not filtered out — PMID:31267471 is a
   peer-reviewed systematic review in a mainstream journal, and `supports: PARTIAL` or a
   `REFUTE`-typed evidence item is the honest encoding.

---

## Reference list

All references below were retrieved from PubMed and their abstracts read directly.

| PMID | Citation | DOI |
|---|---|---|
| 20140961 | Castori M, et al. Natural history and manifestations of the hypermobility type Ehlers-Danlos syndrome: a pilot study on 21 patients. *Am J Med Genet A* 2010;152A:556-64. | [10.1002/ajmg.a.33231](https://doi.org/10.1002/ajmg.a.33231) |
| 28186381 | Bulbena A, et al. Psychiatric and psychological aspects in the Ehlers-Danlos syndromes. *Am J Med Genet C* 2017;175:237-45. | [10.1002/ajmg.c.31544](https://doi.org/10.1002/ajmg.c.31544) |
| 28186390 | Chopra P, et al. Pain management in the Ehlers-Danlos syndromes. *Am J Med Genet C* 2017;175:212-19. | [10.1002/ajmg.c.31554](https://doi.org/10.1002/ajmg.c.31554) |
| 28186393 | Hakim A, et al. Chronic fatigue in Ehlers-Danlos syndrome-Hypermobile type. *Am J Med Genet C* 2017;175:175-80. | [10.1002/ajmg.c.31542](https://doi.org/10.1002/ajmg.c.31542) |
| 31267471 | Kucharik AH, Chang C. The Relationship Between hEDS, POTS, and MCAS. *Clin Rev Allergy Immunol* 2020;58:273-97. | [10.1007/s12016-019-08755-8](https://doi.org/10.1007/s12016-019-08755-8) |
| 32629534 | Gensemer C, et al. Hypermobile Ehlers-Danlos syndromes: Complex phenotypes, challenging diagnoses, and poorly understood causes. *Dev Dyn* 2021;250:318-44. | [10.1002/dvdy.220](https://doi.org/10.1002/dvdy.220) |
| 33980338 | Wang E, et al. The relationship between MCAS, POTS, and Ehlers-Danlos syndrome. *Allergy Asthma Proc* 2021;42:243-46. | [10.2500/aap.2021.42.210022](https://doi.org/10.2500/aap.2021.42.210022) |
| 34766441 | Mathias CJ, et al. Dysautonomia in the Ehlers-Danlos syndromes and hypermobility spectrum disorders. *Am J Med Genet C* 2021;187:510-19. | [10.1002/ajmg.c.31951](https://doi.org/10.1002/ajmg.c.31951) |
| 34811894 | Bascom R, et al. Respiratory manifestations in the Ehlers-Danlos syndromes. *Am J Med Genet C* 2021;187:533-48. | [10.1002/ajmg.c.31953](https://doi.org/10.1002/ajmg.c.31953) |
| 35442549 | De Wandele I, et al. Exploring pain mechanisms in hypermobile Ehlers-Danlos syndrome: A case-control study. *Eur J Pain* 2022;26:1355-67. | [10.1002/ejp.1956](https://doi.org/10.1002/ejp.1956) |
| 35547807 | Royer SP, Han SJ. Mechanobiology in the Comorbidities of Ehlers Danlos Syndrome. *Front Cell Dev Biol* 2022;10:874840. | [10.3389/fcell.2022.874840](https://doi.org/10.3389/fcell.2022.874840) |
| 35750466 | Thwaites PA, et al. Hypermobile Ehlers-Danlos syndrome and disorders of the gastrointestinal tract. *J Gastroenterol Hepatol* 2022;37:1693-1709. | [10.1111/jgh.15927](https://doi.org/10.1111/jgh.15927) |
| 35756986 | Buryk-Iggers S, et al. Exercise and Rehabilitation in People With Ehlers-Danlos Syndrome: A Systematic Review. *Arch Rehabil Res Clin Transl* 2022;4:100189. | [10.1016/j.arrct.2022.100189](https://doi.org/10.1016/j.arrct.2022.100189) |
| 37316864 | Schubert-Hjalmarsson E, et al. Central sensitization in adolescents with HSD or hEDS—a feasibility study. *Pilot Feasibility Stud* 2023;9:97. | [10.1186/s40814-023-01320-3](https://doi.org/10.1186/s40814-023-01320-3) |
| 37847487 | Blitshteyn S. Dysautonomia, Hypermobility Spectrum Disorders and Mast Cell Activation Syndrome as Migraine Comorbidities. *Curr Neurol Neurosci Rep* 2023;23:769-76. | [10.1007/s11910-023-01307-w](https://doi.org/10.1007/s11910-023-01307-w) |
| 38779137 | Petrucci T, et al. Phenotypic Clusters and Multimorbidity in Hypermobile Ehlers-Danlos Syndrome. *Mayo Clin Proc Innov Qual Outcomes* 2024;8:253-62. | [10.1016/j.mayocpiqo.2024.04.001](https://doi.org/10.1016/j.mayocpiqo.2024.04.001) |
| 40145613 | Baeza-Velasco C, et al. Autism in the context of joint hypermobility, HSD, and EDS: A systematic review and prevalence meta-analyses. *Autism* 2025;29:1939-58. | [10.1177/13623613251328059](https://doi.org/10.1177/13623613251328059) |
| 40387691 | Aziz Q, et al. AGA Clinical Practice Update on GI Manifestations and Autonomic or Immune Dysfunction in hEDS: Expert Review. *Clin Gastroenterol Hepatol* 2025;23:1291-1302. | [10.1016/j.cgh.2025.02.015](https://doi.org/10.1016/j.cgh.2025.02.015) |
| 40565051 | Wang TJ, et al. Fascial Pathophysiology in HSD and hEDS: A Review of Emerging Evidence. *Int J Mol Sci* 2025;26:5587. | [10.3390/ijms26125587](https://doi.org/10.3390/ijms26125587) |
| 40843452 | Novak P, et al. Hypermobile Ehlers-Danlos Syndrome: Cerebrovascular, Autonomic and Neuropathic Features. *Am J Med Open* 2025;14:100111. | [10.1016/j.ajmo.2025.100111](https://doi.org/10.1016/j.ajmo.2025.100111) |
| 41001447 | Petrucci-Nelson T, et al. Complex Genetics and Regulatory Drivers of hEDS: Insights from GWAS Meta-analysis. *medRxiv* 2025. **PREPRINT** | [10.1101/2025.09.19.25336146](https://doi.org/10.1101/2025.09.19.25336146) |

Already cited in the dismech hEDS entry and reused here: PMID:20301456 (GeneReviews),
PMID:31409039, PMID:29587413.

---

*Method: PubMed searches across hEDS comorbidity, dysautonomia/POTS, mast cell
activation, psychiatric/neurodevelopmental, GI, pain mechanism, natural history, and
pathogenesis axes. Abstracts were read directly for every cited PMID; no claim above is
sourced from a secondary summary. No evidence snippets have been committed to KB YAML
from this review — quoted figures must be re-verified against
`references_cache/` via `just fetch-reference` before use in an evidence item.*
