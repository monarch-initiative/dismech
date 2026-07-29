# Digital Twins for Disease: State of the Art

_Compiled 2026-07-29. A landscape survey of patient- and disease-level digital twins:
what they are, which mathematical formalisms are actually used, how far each clinical
domain has got, what regulators have accepted, and where the field is blocked. A short
closing section considers where a curated mechanism knowledge base such as dismech fits._

**Verification note.** Claims traceable to a primary paper, a regulatory document, or a
project's own publication are cited inline. Claims drawn only from secondary summaries
(news items, vendor pages, conference abstracts) are marked as such — several widely
repeated digital-twin numbers circulate without a peer-reviewed source, and this report
tries not to launder them.

---

## 1. What a "disease digital twin" is — and how loosely the term is used

The term arrived in medicine from aerospace and manufacturing, where a digital twin is a
simulation of a *specific physical artifact*, kept synchronized with that artifact by a
live data feed, used to predict its future and to test interventions before they are
applied. Transplanting that definition to a patient implies three commitments:

1. **A physical entity** — this patient, not a cohort.
2. **A virtual counterpart** — a computable model whose parameters are individualized.
3. **A living connection** — data flowing in, predictions flowing out, and the model
   being *updated* as the patient changes.

The US National Academies (NASEM) formalization used across the health literature adds
that a digital twin must be personalized, dynamically updated, and predictive in a way
that informs decisions. It is worth stating plainly how rarely published work meets that
bar. A 2025 scoping review in *npj Digital Medicine* screened the 2017–July 2024
literature and found **149 studies** claiming human digital twins, of which **18
(12.1%)** fully satisfied the NASEM criteria
([Tudor et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484800/)). The remainder
distributed across weaker constructs:

| Construct | Studies | % | What it actually is |
|---|---:|---:|---|
| Personalized digital model, no decision support | 56 | 37.6 | A model fitted to one patient; nothing acts on it |
| Personalized digital model, one-time decision support | 31 | 20.8 | Individualized, used once, never updated |
| Digital twin (human-in-the-loop) | 17 | 11.4 | Updated via a clinician-mediated loop |
| Virtual patient cohort | 15 | 10.1 | Synthetic population, not tied to any individual |
| General digital model | 15 | 10.1 | Not individualized at all |
| Digital shadow | 14 | 9.4 | Data mirror with no predictive model |
| Traditional digital twin (automatic update) | 1 | 0.7 | Closed loop without a human in it |

A useful working vocabulary, borrowed from the respiratory-twin literature
([Bhattacharya et al., *Eur Respir Rev* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653195/)),
splits the field into **monitoring twins** (cyber-physical systems: sensors, streaming
state estimation, alerting) and **simulation twins** (mechanistic models run forward to
answer counterfactual questions). Most commercial products are monitoring twins wearing
simulation-twin language; most academic mechanistic work is a simulation twin missing the
live connection. Genuinely closed-loop mechanistic twins are rare.

Two consequences matter for anyone reading this literature:

- **Ladder, not binary.** "Digital model → digital shadow → digital twin" is a maturity
  ladder, and honest papers say where they sit on it. The 2024 *npj Digital Medicine*
  scoping review of digital twins for health
  ([Katsoulakis et al. 2024](https://www.nature.com/articles/s41746-024-01073-0)) makes the
  same point via its "individualized, interconnected, interactive, informative, impactful"
  criteria.
- **The validation deficit is structural, not incidental.** In that 149-study corpus,
  **two studies** mentioned verification, validation and uncertainty quantification
  (VVUQ) at all. A field whose central claim is counterfactual prediction has almost no
  published practice of checking counterfactual predictions.

---

## 2. The modeling toolbox

There is no single digital-twin formalism. Real systems are assemblies, and the choice of
formalism is driven by *what is observable*, *what timescale matters*, and *whether the
question is "what will happen" or "what if I intervene"*.

### 2.1 Continuous mechanistic models (ODE / DAE)

Ordinary differential equations remain the workhorse: state variables are concentrations,
volumes, pressures, cell counts; parameters are rates and capacities with physical meaning.

- **Physiological / whole-body models.** HumMod is the canonical integrative human
  physiology simulator — roughly **5,000 variables** spanning cardiovascular, respiratory,
  renal, neural, endocrine, muscle and metabolic physiology, assembled from published
  empirical relations
  ([Hester et al., *Front Physiol* 2011](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2011.00012/full)).
  Its lineage runs back to Guyton's circulatory model and forward into the
  [Physiome Project](https://www.embs.org/pulse/articles/virtual-physiological-human/),
  launched by IUPS in 1997 explicitly to build modular, reproducible, multiscale
  physiology. Notably, decades on, there is still no comprehensive model integrating
  across all organ systems — the "physiome" remains aspirational.
- **Quantitative systems pharmacology (QSP).** Disease-plus-drug ODE models built to
  answer dose, schedule and combination questions. QSP has become a routine part of
  model-informed drug development, with a steady rise in FDA submissions over the past
  decade, used to inform dose selection and justify trial design. The hard technical
  problem in QSP is not the equations but **virtual population generation** — sampling
  parameter vectors that are individually plausible and collectively reproduce observed
  clinical distributions. In oncology this collides with endpoint structure: linking
  simulated tumor size to time-to-event endpoints such as PFS, with censoring, is an
  active methodological problem
  ([Braniff et al., *CPT:PSP* 2025](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/psp4.13270)).
- **PBPK.** Physiologically based pharmacokinetics is the most regulatorily mature
  mechanistic modeling in medicine, though it models the *drug in the body* rather than
  the disease. Simcyp dominates FDA PBPK submissions (~80% of them, with GastroPlus ~5%
  and PK-Sim ~3%), and enzyme-mediated drug–drug interaction is by far the largest use
  case (~60–75% of applications)
  ([review](https://www.mdpi.com/1999-4923/17/11/1413)). PBPK matters here as an existence
  proof: mechanistic simulation *can* substitute for clinical study when the context of
  use is narrow and the model's chain of evidence from in vitro parameters to clinical
  prediction is complete.
- **Metabolic / endocrine twins.** The UVA/Padova type 1 diabetes simulator is the single
  most consequential disease ODE model in regulatory history: accepted by FDA in January
  2008 as a **substitute for animal trials** for closed-loop insulin control algorithms
  and deposited as Device Master File 1521, with a virtual cohort of 300 in silico
  subjects (100 adults, 100 adolescents, 100 children), revised and resubmitted in 2013
  ([Man et al., *J Diabetes Sci Technol*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4454102/);
  [retrospective](https://pmc.ncbi.nlm.nih.gov/articles/PMC10658679/)).

### 2.2 Spatial continuum models (PDE, FEM, CFD)

When geometry matters, the model becomes a partial differential equation on a
patient-specific mesh derived from imaging.

- **Cardiac electrophysiology** is the deepest example. Single-cell ODE membrane models
  become the reaction term of a monodomain/bidomain reaction–diffusion PDE on a mesh
  segmented from late-gadolinium-enhancement MRI. [openCARP](https://www.sciencedirect.com/science/article/abs/pii/S0169260721002972)
  is the community simulation environment for this, paired with the `carputils` pipeline
  framework for reproducibility.
- **Tumor growth.** Mechanically coupled reaction–diffusion models — a diffusion term for
  tumor cell movement, a reaction term for proliferation and death, coupled to tissue
  mechanics — calibrated on early-treatment MRI to forecast response to neoadjuvant
  chemotherapy
  ([Weis et al., *Cancer Res* 2015](https://aacrjournals.org/cancerres/article/75/22/4697/662361/Predicting-the-Response-of-Breast-Cancer-to);
  reviewed in [Lorenzo et al., *Annu Rev Biomed Eng*](https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-081623-025834)).
  This is one of the few places where a mechanistic model is fitted on data from *within*
  a treatment course and used to predict that same patient's endpoint.
- **Structural / biomechanical.** CT-to-finite-element workflows for bone strength are
  clinically deployed: Biomechanical Computed Tomography is FDA-cleared and used for
  opportunistic osteoporosis diagnosis from existing CT, and the Bologna group has
  published a full ASME V&V 40 credibility assessment of its own BCT solution
  ([Aldieri et al., *Comput Methods Programs Biomed* 2023](https://www.sciencedirect.com/science/article/pii/S0169260723003930)).
  In outcome terms, FE-derived strength predicts incident fracture about as well as DXA
  areal BMD ([review](https://pubmed.ncbi.nlm.nih.gov/34931294/)) — an honest reminder
  that mechanistic sophistication does not automatically buy predictive gain.
- **Fluid and electromechanics.** The
  [SIMULIA Living Heart](https://www.3ds.com/products/simulia/life-sciences-healthcare/living-heart-model)
  four-chamber model couples electrical, structural and fluid physics; Dassault has run a
  multi-year collaborative research agreement with FDA on using virtual patient cohorts as
  digital evidence for cardiovascular device submissions (project reporting is largely
  vendor- and trade-press-sourced; treat specific efficiency claims cautiously).
- **Respiratory.** Reduced pressure–volume and gas-exchange models, 3D CFD on
  patient-specific airway geometry, poroelastic tissue deformation, and long-timescale
  remodeling models all exist — but as components, not twins.

### 2.3 Agent-based and discrete-cell models

Agent-based models (ABMs) give each cell rules and let tissue-level behavior emerge. They
are the natural formalism where **spatial structure and stochasticity drive the outcome**
and where cell-to-cell heterogeneity is the phenomenon rather than noise.

- [PhysiCell](https://pmc.ncbi.nlm.nih.gov/articles/PMC10616087/) is the widely used
  open-source 3-D multicellular agent framework; **PhysiBoSS** couples it to intracellular
  Boolean signaling (see §2.4), giving genuinely two-scale agents.
- Immunology and infection are the heartland: TB granuloma ABMs explain differential
  bacterial control by spatial layering and 3-D motility
  ([Michael et al., *PLOS Comput Biol* 2024](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1012266));
  HostSim tracks multiple granulomas with blood and lymph-node compartments; ABMs of acute
  inflammation have a two-decade translational-systems-biology lineage; PhysiBoSS-COVID
  modeled SARS-CoV-2 signaling in a multicellular context.
- A multiscale ABM of immune surveillance in micrometastases has been framed explicitly as
  groundwork for cancer patient digital twins
  ([PMC11614875](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11614875/)).

ABMs pay for their expressiveness with calibration cost: they are stochastic, expensive,
have many weakly-identifiable rule parameters, and require ensemble runs for any
uncertainty statement. Nearly all disease ABMs are population- or cohort-calibrated, not
patient-personalized.

### 2.4 Logical, qualitative and symbolic models

When kinetic parameters are unknown — the normal condition in signaling and gene
regulation — discrete formalisms buy mechanism without demanding rate constants.

- **Boolean / multivalued networks.** Nodes are active/inactive; dynamics come from update
  rules. `MaBoSS` simulates Boolean models stochastically in continuous time, and the
  `PROFILE` method personalizes them by using patient omics to set initial states, fix
  nodes, or bias transition rates — demonstrated on TCGA patients and cell lines to derive
  individualized drug-response simulations
  ([Béal et al., *eLife* 2021](https://elifesciences.org/articles/72626)). This is one of
  the cleanest existing routes from a *knowledge-derived network* to a *patient-specific
  simulation*, and it needs no rate constants.
- **Curated causal graph formalisms.** Two are worth naming because they sit exactly at
  the boundary between knowledge representation and simulation:
  - **GO-CAM** (Gene Ontology Causal Activity Models) links gene-product molecular
    activities into causal flows, and has been shown to distinguish phenotypes arising
    from mutations at different points in a pathway
    ([Thomas et al., *Genetics* 2023](https://academic.oup.com/genetics/article/225/2/iyad152/7242464)).
    Reactome's process-description pathways can be converted into GO-CAMs.
  - **Adverse Outcome Pathways (AOPs)**, from regulatory toxicology, chain a molecular
    initiating event through measurable key events to an adverse outcome. Qualitative AOPs
    give causal architecture without dose–time quantification; **quantitative AOPs** add
    response–response functions, often via Bayesian networks, converting a curated causal
    chain into a predictive model
    ([qAOP review](https://www.researchgate.net/publication/341461985_Quantitative_adverse_outcome_pathway_qAOP_models_for_toxicity_prediction)).
    AOPs are the closest existing precedent for "a curated mechanism graph that a
    regulator will actually reason over."
- **Constraint-based metabolic models.** Genome-scale metabolic reconstructions with flux
  balance analysis are stoichiometry-only, need no kinetics, and scale to whole-organism
  metabolism — well suited to inborn errors of metabolism and to tumor metabolic
  rewiring, and directly personalizable by integrating patient expression data.

### 2.5 Statistical and generative models

The fastest-moving and least mechanistic branch.

- **Generative disease-trajectory models.** `Delphi-2M` adapts a GPT architecture to
  health histories: trained on ~0.4M UK Biobank participants, externally validated on
  ~1.9M Danish individuals, predicting rates of **more than 1,000 diseases** conditional
  on past history, and — because it is generative — able to sample synthetic 20-year
  trajectories
  ([Shmatko et al., *Nature* 2025](https://www.nature.com/articles/s41586-025-09529-3)).
  Its error profile is instructive: strongest for conditions with predictable courses
  (some cancers, myocardial infarction), weakest for psychiatric disorders, pregnancy
  complications, and rare diseases. That is exactly the region where mechanism, not
  epidemiological pattern, carries the information.
- **Prognostic "digital twins" for trials.** Unlearn.ai's approach generates a model-based
  forecast of each enrolled participant's control-arm trajectory and uses it as a
  prognostic covariate (PROCOVA). The EMA qualified PROCOVA as an acceptable statistical
  approach for primary analysis of Phase 2/3 trials with continuous endpoints in 2022, and
  retrospective Alzheimer analyses report control-arm reductions in the tens of percent
  ([Wang et al., *Alz Dement TRCI* 2025](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/trc2.70181)).
  These are *statistical* twins — unbiased treatment-effect estimation is guaranteed by
  the covariate-adjustment framing even if the twin model is biased — and they answer
  "how would this patient have progressed untreated," not "why."
- **Graph and causal ML.** Graph neural networks over comorbidity/diagnosis graphs, and
  knowledge-graph-driven causal twins for chronic disease progression, are an active area;
  reported external-validation gains over recurrent and mechanistic baselines exist but
  are mostly in preprints and non-indexed venues, so treat effect sizes as provisional.

### 2.6 Hybrid / scientific-ML

The consensus direction of travel. Mechanistic structure constrains a flexible learner;
the learner absorbs what the mechanism does not capture.

- **Physics-informed neural networks (PINNs)** encode governing equations as loss terms —
  useful when data are sparse but physics is known
  ([narrative review for physiological signals](https://iopscience.iop.org/article/10.1088/1361-6579/adf1d3)).
- **Neural ODEs** replace fixed rate laws with learned derivative functions, letting a
  compartmental model adapt to individual physiology — applied to glucose dynamics where
  population-level parameterizations cannot track individual variability.
- **Surrogates / emulators.** Because credible twins need thousands of runs for uncertainty
  quantification and virtual-population inference, emulation of expensive mechanistic
  models is becoming standard practice — including in immuno-oncology QSP.
- **Data assimilation.** Kalman-family and particle filters keep a mechanistic model
  synchronized with streaming measurements. This is the piece that turns a simulation into
  an actual *twin*, and its absence is why so much of the literature is stuck one rung
  down the ladder.

### 2.7 Choosing a formalism

| Formalism | Needs | Gives | Individualization route | Main weakness |
|---|---|---|---|---|
| ODE / QSP / PBPK | Rate constants, structure | Continuous dynamics, dose–response, intervenable | Parameter estimation, virtual populations | Parameters often unidentifiable from clinical data |
| PDE / FEM / CFD | Imaging geometry, material properties | Spatial, biophysically grounded | Patient mesh + measured properties | Cost; needs imaging; narrow scope per model |
| ABM | Cell rules, spatial setup | Emergence, heterogeneity, stochasticity | Rarely personalized in practice | Calibration and compute cost |
| Boolean / logical | Network topology only | Qualitative mechanism, drug logic | Omics-driven node fixing (PROFILE) | No timescales, no magnitudes |
| Constraint-based (FBA) | Stoichiometry, gene–reaction rules | Whole-metabolism flux states | Expression integration | Steady-state only; no regulation dynamics |
| Statistical / generative | Large longitudinal cohorts | Broad disease coverage, calibrated risk | Native (conditions on history) | Associational; poor on rare disease; weak counterfactuals |
| Hybrid / SciML | Both of the above | Data efficiency + flexibility | Both routes | Credibility assessment is unsettled |

Four capabilities are worth naming as the actual design targets, since they separate a twin
from a predictor: **explainability** (structure interpretable in biological terms),
**intervenability** (you can simulate a therapy, not just forecast), **learnability** (the
model updates as trajectories accrue), and **diversability** (parameter uncertainty yields
ensembles rather than point predictions)
([Frontiers, multi-scale DT review 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1753906/full)).

---

## 3. Which parts of disease space are actually covered

This is the question most reviews dodge. The distribution is extremely uneven, and it is
driven almost entirely by **whether the dominant mechanism is measurable at the bedside
and expressible in a physics-like formalism** — not by disease burden.

From the same 149-study corpus
([Tudor et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484800/)):

| Domain | Studies | % |
|---|---:|---:|
| Cardiac | 43 | 28.9 |
| Metabolic (13 of them diabetes) | 19 | 12.8 |
| Musculoskeletal (13 skeletal-specific) | 18 | 12.1 |
| Cancer | 11 | 7.4 |
| Whole body | 10 | 6.7 |
| Respiratory | 9 | 6.0 |
| Neurological | 6 | 4.0 |
| Hepatic | 5 | 3.4 |
| Immune | 5 | 3.4 |

Modeling approach in that corpus: **empirical 64 (43.0%), mechanistic 47 (31.6%), hybrid
38 (25.5%)** — and among the NASEM-compliant twins specifically, empirical approaches
dominated (61.1%), because dynamic updating is far easier with a data-driven model than
with a stiff mechanistic one. Half the studies (74; 49.7%) used imaging; 61.1% used
clinical-grade sensors, while NASEM-compliant twins leaned toward consumer-grade sensors
(55.6%), reflecting what continuous monitoring actually requires.

### Domain-by-domain maturity

**Cardiac electrophysiology — the most mature.** Heart digital twins are built from 3-D
LGE-MRI, simulate all inducible VT circuits, and propose ablation targets. Published
validation shows electrogram abnormalities significantly enriched at twin-predicted sites
versus non-predicted sites (468/1029, 45.5% vs 519/1611, 32.2%; *P*<0.001) in an 18-patient
cohort
([*Circulation* 2025](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.070526);
companion in [*Circ Arrhythm Electrophysiol*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313252/)).
The **TWIN-VT** study (NCT03536052) is an FDA investigational-device-exemption trial
prospectively testing twin-guided ischemic VT ablation — single-institution, 10 subjects.
A Johns Hopkins release in April 2026 reported complete procedural success in those 10
participants; that headline currently rests on an institutional communication rather than a
peer-reviewed primary report, and should be read as promising rather than established.
Separately, cardiac twins are used for **virtual drug testing**, personalizing
repolarization from 12-lead ECG plus MRI.

**Epilepsy — the most ambitious neurological attempt.** The Virtual Epileptic Patient
builds a personalized whole-brain network model (neural-mass dynamics on a subject's
structural connectome) and infers the epileptogenic zone. Retrospectively, in 53 patients
with drug-resistant focal epilepsy, VEP reproduced clinically defined epileptogenic zones
with mean precision 0.613 and mean distance 5.6 mm, with a low false-discovery rate (0.028)
among patients who became seizure-free
([review](https://www.sciencedirect.com/science/article/abs/pii/S147444222300008X)).
**EPINOV** (2019–2024) randomized **356 patients across 11 French hospitals** to surgical
planning with or without VEP predictions — the largest randomized test of a mechanistic
disease twin to date. Preliminary results were presented at the EBRAINS Summit 2025;
a full primary-outcome publication was not locatable as of this survey, so the trial should
be described as completed-and-reporting, not as a positive result. The successor
**Virtual Brain Twin** project extends the approach beyond epilepsy surgery.

**Diabetes and metabolism — the most clinically deployed, in two very different senses.**
The mechanistic branch (UVA/Padova, §2.1) is a regulatory landmark and underpins artificial
pancreas development. The commercial branch is exemplified by Twin Health's "Whole Body
Digital Twin" for type 2 diabetes: CGM plus wearables plus labs driving individualized
dietary and lifestyle guidance, with an RCT reporting large HbA1c reductions and high
remission rates at 6, 12 and 18 months
([ADA 2024 abstract](https://diabetesjournals.org/diabetes/article/73/Supplement_1/20-OR/154875/20-OR-Digital-Twin-DT-Technology-in-Type-2);
[1-year real-world](https://www.nature.com/articles/s41598-024-76584-7)). Two caveats
belong in any honest account: the intervention bundles an intensive behavioral program with
the model, so the twin's incremental contribution is not isolated; and much of the
mechanistic framing is proprietary. It is the clearest case of a "twin" whose demonstrated
value is real but whose *mechanistic* content is unverifiable externally.

**Oncology — high investment, structurally hard.** The NCI–DOE Cancer Patient Digital Twin
initiative (2020, building on JDACS4C from 2016) established the vision and the
[collaboration roadmap](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2022.1007784/full).
Real progress clusters in image-driven mechanistic forecasting of treatment response (§2.2),
QSP-based immuno-oncology virtual patients (e.g. immunogenomic-data-guided virtual patients
predicting NSCLC response to PD-L1 inhibition,
[*npj Precision Oncology* 2023](https://www.nature.com/articles/s41698-023-00405-9)), and
adaptive radiotherapy. The obstruction is intrinsic: tumor evolution is stochastic, the
relevant state (subclonal architecture, immune microenvironment) is sampled sparsely and
destructively, and the endpoints are time-to-event.

**Immunology and infection — the largest recognized gap, with a roadmap.** The immune
digital twin roadmap ([Laubenbacher et al., *npj Digital Medicine* 2022](https://www.nature.com/articles/s41746-022-00610-z))
proposes a four-stage process — (1) fix a concrete clinical use case and build a generic
template model; (2) personalize it with patient immune data; (3) test it and quantify
parametric, structural, algorithmic and observational uncertainty; (4) improve it
continuously — and explicitly endorses formalism pluralism (ODEs for physiology/PK, ABMs
for cell-level spatial dynamics, Boolean models for signaling and gene regulation, ML for
imaging, hybrids where mechanism is unmapped). Its two most sobering statements are that
**many relevant immune parameters simply cannot be measured in a living patient**, so use-case
selection determines feasibility; and that the effort is comparable in cost and complexity
to the $1.8B Cancer Moonshot — with team-science infrastructure, not mathematics, named as
the hardest part. The RDA Building Immune Digital Twins working group (100+ experts, 22
countries) is the current community vehicle.

**Musculoskeletal — narrow but genuinely translated.** CT-to-FE bone strength (§2.2) is the
clearest case of a mechanistic patient-specific model in routine clinical use with a
formal credibility assessment behind it.

**Respiratory — conceptual.** A review of chronic lung disease twins found that only **6 of
80** systems claiming to be digital twins addressed respiratory disease at all, and that
**none** of the included articles met all digital-twin requirements. Asthma, COPD and IPF
twins remain largely proposals; the components (spirometry/oximetry/smart-inhaler streams,
CFD on airway geometry, ML exacerbation prediction) exist unassembled.

**Hepatic and renal — early, promising.** MASLD/MAFLD is an active target, combining
mechanistic progression models with AI (e.g. the ARTEMIs effort; a clinical study,
NCT07430501, is registered). AKI trajectory forecasting with organ-structured latent state
is emerging in preprint form.

**Critical care — the best fit for the twin concept, the worst fit for mechanism.** ICU
patients are densely instrumented and change fast, which is exactly what data assimilation
wants. But sepsis spans cardiovascular, immune, metabolic and microvascular dynamics
simultaneously, and the informed view is that progress will come from **targeted
sub-models** (fluid responsiveness, vasopressor response) rather than whole-syndrome twins.
Mechanism-based critical-illness twins have so far mostly been used to *generate synthetic
data* rather than to guide care.

**Rare and Mendelian disease — the structural hole.** A critical appraisal of in silico
rare-disease technologies
([*npj Digital Medicine* 2025](https://www.nature.com/articles/s41746-025-02068-1)) and a
pediatric-rare-disease twin perspective
([*CPT:PSP* 2026](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/psp4.70234)) converge
on the same diagnosis: small cohorts, heterogeneous phenotypes, incomplete modality
coverage, and evolving endpoints defeat conventional evidence pathways; genotype-to-phenotype
translation remains unable to predict individual trajectories; and most rare diseases have
no coupled multi-omics data at all. This is precisely where mechanistic and
knowledge-driven models should have the comparative advantage — the mechanism is often
*known* (a specific enzyme deficiency, a specific channel defect) even when the cohort is
tiny — and where generative EHR models are weakest.

### The shape of the coverage gap

Put the two distributions side by side. `Delphi-2M` spans **>1,000 disease codes** but
purely associationally. Mechanistic twins span perhaps a few dozen diseases with real
depth, concentrated in cardiac EP, diabetes, bone, and a handful of tumor types. Between
them sits the great majority of the roughly 10,000 recognized human diseases, for which
there exists neither a fitted mechanistic model nor enough longitudinal data to learn one:
most Mendelian disease, most immune-mediated disease, most neurodegeneration, most
psychiatric illness. The binding constraint there is **not compute and not data volume** —
it is that nobody has written down the mechanism in a computable, reusable, evidence-linked
form.

---

## 4. Standards, infrastructure, and reproducibility

A twin field without model exchange standards would be a collection of unrepeatable
one-offs. The systems-biology community solved a version of this problem already:

- **SBML** for model structure, **CellML** for modular physiological models, **SED-ML**
  for simulation experiment description (what to run to reproduce a specific figure),
  **SBGN** for visual notation, and **OMEX/COMBINE archives** to bundle them
  ([overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC10435326/)).
- **BioModels** holds nearly **1,100 manually curated models** (as of May 2025), curated
  so that they reproduce their published results, with recent work systematizing that
  verification ([*PLOS Comput Biol* 2025](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013239)).
  The **Physiome Model Repository** plays the analogous role for CellML.
- **Europe's Virtual Human Twin.** The EDITH Coordination and Support Action closed in
  October 2025 with a [Roadmap for the European Virtual Human Twin](https://www.edith-csa.eu/roadmap/)
  plus a policy brief, and a proof-of-concept federated cloud repository and simulation
  platform. This is currently the most concrete institutional attempt to build shared twin
  infrastructure rather than individual twins.

The gap in this stack is telling: there are mature standards for **models** and mature
standards for **clinical data** (OMOP, FHIR), but no widely adopted standard for the
**mechanistic claim layer in between** — the curated, evidence-attributed statement that
"this perturbation causes that process in this cell type, and here is the paper." GO-CAM
and AOP-Wiki are the nearest things, each scoped to its own community.

---

## 5. Personalization, credibility, and regulation

### Personalization is an inference problem, not a data-plumbing problem

Building a twin from a template model means solving an inverse problem: infer parameters
from sparse, noisy, indirect measurements. The recurring difficulties are consistent across
domains:

- **Identifiability.** Many mechanistic parameters cannot be uniquely determined from
  clinically obtainable measurements. Different parameter vectors reproduce the same
  observations and diverge under intervention — which is fatal precisely for the
  counterfactual questions twins are built to answer.
- **Unobservability.** The states that matter most are frequently the ones you cannot
  measure in a living person (tissue-level immune cell states, subclonal composition,
  intracellular signaling flux).
- **Uncertainty propagation across scales.** Error at the molecular layer amplifies upward;
  without uncertainty quantification a multiscale twin produces confident nonsense.
- **Cross-scale coupling.** How a molecular event changes an organ-level phenotype is
  usually the least formalized part of a multiscale model — often a hand-tuned coupling
  term standing in for unknown biology.
- **Computational tractability** for real-time bedside updating, which is why emulation
  and surrogate modeling have become load-bearing.

### Credibility frameworks

The regulatory apparatus for mechanistic simulation is more developed than most clinicians
realize:

- **ASME V&V 40** defines credibility as trust in a model's predictive capability *for a
  stated context of use*, and requires VVUQ effort proportional to **model risk** — the
  product of the model's influence on the decision and the consequence of that decision
  being wrong. Context of use is the pivotal concept: a model is never "validated" in
  general.
- **FDA final guidance**, "Assessing the Credibility of Computational Modeling and
  Simulation in Medical Device Submissions," issued **16 November 2023**
  ([Federal Register](https://www.federalregister.gov/documents/2023/11/17/2023-25470/assessing-the-credibility-of-computational-modeling-and-simulation-in-medical-device-submissions);
  [document](https://www.fda.gov/media/154985/download)), builds on V&V 40 and enumerates
  credibility evidence categories spanning code and calculation verification, model
  plausibility, calibration, bench and in vivo comparison, population-level validation,
  emergent behavior, and documentation/traceability.
- **Good Simulation Practice.** The Avicenna Alliance / VPH Institute / In Silico World
  book *Toward Good Simulation Practice* (23 February 2024, 144 contributing experts,
  >50,000 downloads by December 2025) proposes GSP as a peer of GLP/GCP/GMP for
  computational evidence
  ([Avicenna Alliance](https://www.avicenna-alliance.com/publications/toward-good-simulation-practice-best-practices-for-the-use-of-computational-modelling-and-simulation.html)).

### Where simulation has actually been accepted

| Instance | Regulator | Status |
|---|---|---|
| UVA/Padova T1D simulator | FDA | Accepted 2008 as substitute for animal trials in closed-loop algorithm testing; Device Master File 1521 |
| PBPK (Simcyp and others) | FDA/EMA | Routine in submissions; DDI predictions can support labeling |
| PROCOVA prognostic twins | EMA | Qualified 2022 as acceptable primary-analysis approach (Phase 2/3, continuous endpoints) |
| CT-to-FE bone strength (BCT) | FDA | Cleared; clinical indication for opportunistic osteoporosis diagnosis |
| Heart digital twin VT ablation guidance | FDA | IDE trial (TWIN-VT, NCT03536052), 10 subjects |
| Living Heart virtual cohorts | FDA | Collaborative research agreement toward device digital evidence |

The pattern is unmistakable: acceptance follows **narrow context of use plus a complete
evidence chain**, never model comprehensiveness. Nothing on that list is a whole-patient
twin.

---

## 6. What is genuinely blocking progress

1. **The mechanism-representation bottleneck.** Most published "digital twins" are
   phenomenological — they fit observed phenomena rather than encoding underlying
   mechanism — which leaves a real gap when the goal is to bridge biological scales.
   Every mechanistic twin still begins with a human reading literature and hand-writing a
   model. There is no reusable, machine-readable, evidence-attributed substrate of disease
   mechanism to build from, so each new disease starts near zero. This is the single most
   under-discussed constraint, and the one least amenable to more compute.
2. **Identifiability and unobservability** (§5) — structural, not a data-collection
   problem.
3. **Validation of counterfactuals.** Predictive accuracy on observed trajectories does not
   establish that a model gets *interventions* right, yet that is the claim. Validation
   needs to target counterfactual fidelity and treatment-response simulation, and almost
   nobody does this. Two of 149 studies mentioned VVUQ.
4. **Complex-systems limits.** Emergence, nonlinearity, and individual-versus-population
   inference impose limits that no amount of data removes; the honest framing is bounded
   prediction horizons with quantified uncertainty, not "simulate the patient."
5. **Regulatory fit for learning systems.** V&V 40 and the FDA framework assume a *fixed*
   model with a *fixed* context of use. A twin that updates itself continuously is a
   regulatory object nobody has fully specified.
6. **Definitional inflation.** When 88% of self-described twins are not twins, evidence
   synthesis becomes impossible and the label loses information.
7. **Ethics, privacy, equity.** Consent for a model that outlives its update window and
   generates predictions the subject never contemplated is not addressed by conventional
   one-time consent; a real risk exists of stratification between the "digitally twinned"
   and the digitally excluded, given cost and literacy barriers; and governance is
   fragmented across jurisdictions.

---

## 7. Where the field is heading

- **Hybrid by default.** Pure mechanistic models cannot absorb clinical heterogeneity;
  pure ML cannot answer intervention questions. Mechanistic scaffold plus learned
  residual, with surrogates for tractability, is the emerging consensus architecture.
- **Foundation models as components, not twins.** Generative trajectory models
  (Delphi-2M-class) give unmatched breadth of disease coverage and calibrated risk; they
  are best understood as a prior or an outer layer over mechanistic modules, not a
  replacement. LLM-orchestrated and "world model" framings are appearing rapidly, largely
  in preprints; the interesting near-term use is agentic *assembly and calibration* of
  mechanistic models rather than the LLM being the twin.
- **Federation over centralization.** EDITH's federated repository and simulation platform
  reflects the reality that the data will not move.
- **Population and health-system twins** alongside patient twins, for capacity planning and
  prevention policy.
- **Twins as trial instruments** — synthetic control arms, sample-size reduction, in silico
  device evaluation — will likely deliver regulatory-grade value before bedside twins do,
  because the context of use is narrower and the comparator is a statistic rather than a
  patient.

The realistic near-term picture is not one twin per patient. It is **a library of
credible, narrow, composable disease modules**, each validated for a stated context of
use, assembled per patient as the question demands — which makes the reusable mechanism
substrate (§6.1) the rate-limiting asset.

---

## 8. Where dismech could contribute

dismech is a curated, evidence-linked knowledge base of disease pathophysiology: currently
1,635 disorder entries, 118 mechanism modules, 48 groupings and 17 comorbidity entries,
with pathophysiology represented as named nodes carrying ontology-bound cell types,
biological processes and molecular functions, explicit `downstream` causal edges, a
`biological_scale` tag (MOLECULAR / CELLULAR / TISSUE / ORGANISM), and per-claim evidence
whose snippets are mechanically validated against cached source abstracts.

That is, structurally, a **qualitative causal mechanism graph with provenance** — the same
class of object as GO-CAM and the AOP framework, but organized by disease and at
substantially broader disease coverage. Reading §3 and §6.1 together suggests where that is
worth something.

**1. Supplying the model-building substrate for the long tail.**
The coverage gap is not in cardiac EP; it is in the thousands of diseases where mechanism
is *known* but never written down computably. dismech already spans a large slice of that
tail, including the Mendelian and immune-mediated disease where generative EHR models are
weakest (Delphi-2M's own worst-performing category) and where rare-disease appraisals
identify the genotype-to-phenotype gap. A dismech pathograph is not a simulation, but it is
most of the specification work for one: nodes, edges, directions, scales, and the citations
justifying each.

**2. Boolean/logical models as the natural first executable target.**
Of the formalisms in §2, discrete logical models are the closest to dismech's existing
content — they need topology and edge sign, not rate constants, which is exactly what a
pathograph has and exactly what it lacks. The `PROFILE`/`MaBoSS` pattern (personalize a
knowledge-derived Boolean network with patient omics) is a demonstrated route from curated
network to patient-specific drug-response simulation. A dismech module such as
`fibrotic_response` or `cellular_senescence`, with its trigger→consequence chain and
`modifier` directions, is a candidate for semi-automated export to a logical model with
evidence attached to every edge. Modules matter here more than individual disorders: they
are exactly the *reusable, composable* units §7 argues the field needs, and `conforms_to`
already records which diseases instantiate which conserved process — a ready-made map of
where one validated module could be reused across many diseases.

**3. The existing `computational_models` slot is the right hook, and it is underpopulated.**
The schema already has a `ComputationalModel` class (`model_type` covering
GENOME_SCALE_METABOLIC, FLUX_BALANCE_ANALYSIS, KINETIC, AGENT_BASED, BOOLEAN_NETWORK,
PHYSIOLOGICAL, DIGITAL_TWIN), with `repository_url`/`model_id`/`model_format` for BioModels
and SBML provenance, `ModelVariable` for state variables (native `dataset_identifier`, unit,
and ontology `mappings_list` to LOINC/CHEBI/HP), and `ModelVariableDescriptor` thresholds
with `severity_scale` linking a model variable's value to an HP phenotype at a given
severity. `CKD-Mineral_Bone_Disorder` (Peterson-Riggs calcium/bone ODE model,
`BIOMD0000000613`) and `Long_QT_Syndrome` (ORd family) are worked examples. But only **18
of 1,818 entries** carry a `computational_models` block. Closing that gap — systematically
linking existing published models in BioModels, the Physiome Model Repository and the
cardiac/metabolic literature to the diseases they model — would make dismech a usable index
from *disease* to *available executable model*, which as far as this survey found does not
currently exist in any organized form.

**4. Model-variable-to-phenotype mapping as a validation interface.**
The `ModelVariableDescriptor` threshold/`severity_scale` construct, plus the empirical
`reference_ranges` with `interpretation_bands` on `Biochemical` markers, together define
something the twin field needs and generally improvises: a curated mapping from *simulated
state variable* to *clinically recognized phenotype*, with the LOINC-coded normal interval
and the graded abnormality bands kept distinct from the model's activation thresholds. That
is the interface at which a simulation output can be scored against a phenotype-coded
patient record — i.e. at which counterfactual claims become checkable (§6.3).

**5. Mechanistic hypotheses and knowledge gaps as a model-risk annotation.**
dismech records `mechanistic_hypotheses` with status (canonical / alternative / emerging),
lets causal edges opt into hypothesis groups, and distinguishes `KNOWLEDGE_GAP` (evidence
absent) from `HUMAN_MODEL_MISMATCH` (evidence exists in a model system but human validity
is the open question). In V&V 40 terms this is per-edge information about **structural
uncertainty** — which parts of a mechanism graph are consensus and which are contested,
and which rest on animal or in vitro data that may not transfer. A twin assembled from
curated mechanism could inherit that annotation and propagate it into its uncertainty
statement, rather than presenting all edges as equally solid. The `evidence_source`
discipline (HUMAN_CLINICAL / MODEL_ORGANISM / IN_VITRO / COMPUTATIONAL) does similar work
at the level of individual claims.

**6. Benchmarking and interpreting learned models.**
A curated causal graph is a natural test set for mechanistic claims emitted by
data-driven pipelines — the framing already sketched in
`docs/causal-modeling-integration-plan.md` for causal gene-to-trait analyses. The same
applies to twin outputs: when a knowledge-graph or GNN-based twin asserts a mechanistic
pathway, dismech can say whether that pathway is curated, contested, or absent, and cite
why.

**Honest limits.** dismech is qualitative: no rate constants, no timescales, no
quantitative edge magnitudes, no patient-level data, and no simulation engine. It cannot
become a digital twin, and framing it as one would be exactly the definitional inflation
§6.6 criticizes. Its plausible role is narrower and more defensible — the **curated,
evidence-attributed, disease-indexed mechanism layer** that model builders currently
reconstruct by hand for every new disease, plus the index from disease to the executable
models that already exist. Whether that role is worth investing in is partly an empirical
question, and the cheapest test is small: take two or three modules with clean
trigger→consequence chains, export them to logical models, and see how much of the
specification work the pathograph actually removes.

---

## Sources

Primary literature and standards:

- [A scoping review of human digital twins in healthcare applications and usage patterns — *npj Digital Medicine* 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12484800/)
- [Digital twins for health: a scoping review — *npj Digital Medicine* 2024](https://www.nature.com/articles/s41746-024-01073-0)
- [Building digital twins of the human immune system: toward a roadmap — *npj Digital Medicine* 2022](https://www.nature.com/articles/s41746-022-00610-z)
- [Immune digital twins for complex human pathologies — *npj Systems Biology and Applications* 2024](https://www.nature.com/articles/s41540-024-00450-5)
- [Challenges and opportunities for digital twins in precision medicine from a complex systems perspective — *npj Digital Medicine* 2024](https://www.nature.com/articles/s41746-024-01402-3)
- [Advancing the frontier of rare disease modeling: a critical appraisal of in silico technologies — *npj Digital Medicine* 2025](https://www.nature.com/articles/s41746-025-02068-1)
- [The Potential of Digital Twins for Pediatric Rare Diseases — *CPT:PSP* 2026](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/psp4.70234)
- [Multi-scale digital twins for personalized medicine — *Frontiers in Digital Health* 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1753906/full)
- [Digital twins for chronic lung diseases — *European Respiratory Review* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11653195/)
- [Personalized Heart Digital Twins Detect Substrate Abnormalities in Scar-Dependent VT — *Circulation* 2025](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.070526)
- [Heart Digital Twins Predict Features of Invasive Reentrant Circuits and Ablation Lesions — *Circ Arrhythm Electrophysiol*](https://pmc.ncbi.nlm.nih.gov/articles/PMC12313252/)
- [The openCARP simulation environment for cardiac electrophysiology](https://www.sciencedirect.com/science/article/abs/pii/S0169260721002972)
- [Personalised virtual brain models in epilepsy — *Lancet Neurology*](https://www.sciencedirect.com/science/article/abs/pii/S147444222300008X)
- [Virtual brain twins: from basic neuroscience to clinical use — *National Science Review* 2024](https://academic.oup.com/nsr/article/11/5/nwae079/7616087)
- [The UVA/PADOVA Type 1 Diabetes Simulator: New Features](https://pmc.ncbi.nlm.nih.gov/articles/PMC4454102/)
- [Developing the UVA/Padova Type 1 Diabetes Simulator: Modeling, Validation, Refinements, and Utility](https://pmc.ncbi.nlm.nih.gov/articles/PMC10658679/)
- [Predicting the Response of Breast Cancer to Neoadjuvant Therapy Using a Mechanically Coupled Reaction–Diffusion Model — *Cancer Research* 2015](https://aacrjournals.org/cancerres/article/75/22/4697/662361/Predicting-the-Response-of-Breast-Cancer-to)
- [Patient-Specific, Mechanistic Models of Tumor Growth Incorporating AI and Big Data — *Annu Rev Biomed Eng*](https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-081623-025834)
- [Patient-specific Boolean models of signalling networks guide personalised treatments — *eLife* 2021](https://elifesciences.org/articles/72626)
- [PhysiBoSS 2.0: sustainable integration of stochastic Boolean and agent-based modelling](https://pmc.ncbi.nlm.nih.gov/articles/PMC10616087/)
- [Agent-based model of TB granuloma structure and 3D movement — *PLOS Comput Biol* 2024](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1012266)
- [A multiscale model of immune surveillance in micrometastases and cancer patient digital twins](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11614875/)
- [Learning the natural history of human disease with generative transformers (Delphi-2M) — *Nature* 2025](https://www.nature.com/articles/s41586-025-09529-3)
- [Using AI-generated digital twins to boost clinical trial efficiency in Alzheimer's disease — *Alz Dement TRCI* 2025](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/trc2.70181)
- [An integrated QSP virtual population approach for calibration with oncology efficacy endpoints — *CPT:PSP* 2025](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/psp4.13270)
- [Immunogenomic data-guided virtual patients predicting NSCLC response to PD-L1 inhibition — *npj Precision Oncology* 2023](https://www.nature.com/articles/s41698-023-00405-9)
- [The Evolution and Future Directions of PBPK Modeling in FDA Regulatory Review](https://www.mdpi.com/1999-4923/17/11/1413)
- [HumMod: A Modeling Environment for the Simulation of Integrative Human Physiology — *Front Physiol* 2011](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2011.00012/full)
- [The Virtual Physiological Human — IEEE Pulse](https://www.embs.org/pulse/articles/virtual-physiological-human/)
- [Verification and reproducible curation of the BioModels repository — *PLOS Comput Biol* 2025](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013239)
- [Standards, Dissemination, and Best Practices in Systems Biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC10435326/)
- [Biochemical pathways represented by GO-CAMs identify distinct phenotypes resulting from mutations in pathways — *Genetics* 2023](https://academic.oup.com/genetics/article/225/2/iyad152/7242464)
- [Quantitative adverse outcome pathway (qAOP) models for toxicity prediction](https://www.researchgate.net/publication/341461985_Quantitative_adverse_outcome_pathway_qAOP_models_for_toxicity_prediction)
- [Credibility assessment of computational models according to ASME V&V 40: Bologna Biomechanical CT](https://www.sciencedirect.com/science/article/pii/S0169260723003930)
- [Finite Element Assessment of Bone Fragility from Clinical Images](https://pubmed.ncbi.nlm.nih.gov/34931294/)
- [Physics-informed neural networks for physiological signal processing and modeling: a narrative review](https://iopscience.iop.org/article/10.1088/1361-6579/adf1d3)
- [Digital twins as global learning health and disease models — *Genome Medicine* 2025](https://link.springer.com/article/10.1186/s13073-025-01435-7)
- [Exploring approaches for predictive cancer patient digital twins (NCI–DOE) — *Frontiers in Digital Health* 2022](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2022.1007784/full)
- [Building Digital Twins for Cardiovascular Health: From Principles to Clinical Impact — *JAHA*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11681439/)
- [Digital Twin (DT) Technology in Type 2 Diabetes Remission — 18-month RCT results, ADA 2024](https://diabetesjournals.org/diabetes/article/73/Supplement_1/20-OR/154875/20-OR-Digital-Twin-DT-Technology-in-Type-2)
- [One-year outcomes of a digital twin intervention for type 2 diabetes — *Scientific Reports* 2024](https://www.nature.com/articles/s41598-024-76584-7)

Regulatory and infrastructure documents:

- [FDA final guidance: Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions (16 Nov 2023)](https://www.fda.gov/media/154985/download) · [Federal Register notice](https://www.federalregister.gov/documents/2023/11/17/2023-25470/assessing-the-credibility-of-computational-modeling-and-simulation-in-medical-device-submissions)
- [Toward Good Simulation Practice — Avicenna Alliance / VPH Institute / In Silico World (Feb 2024)](https://www.avicenna-alliance.com/publications/toward-good-simulation-practice-best-practices-for-the-use-of-computational-modelling-and-simulation.html)
- [A Roadmap for the European Virtual Human Twin — EDITH CSA (Oct 2025)](https://www.edith-csa.eu/roadmap/) · [European VHT Initiative](https://digital-strategy.ec.europa.eu/en/policies/virtual-human-twins)
- [SIMULIA Living Heart Model](https://www.3ds.com/products/simulia/life-sciences-healthcare/living-heart-model)
- [Unlearn.ai — reflections on the EMA draft qualification opinion](https://www.unlearn.ai/blog/success-is-never-a-straight-line--reflecting-on-our-ema-draft-qualification-opinion)

Secondary / non-peer-reviewed sources used only where flagged as such in the text:

- [Digital twin hearts deliver 100% success in arrhythmia trial — Johns Hopkins Hub, Apr 2026](https://hub.jhu.edu/2026/04/01/digital-twin-hearts-arrhythmia-trial/)
- [EPINOV trial: impacts and lessons learned — EBRAINS Summit 2025](https://summit2025.ebrains.eu/programme/epinov-trial-impacts-and-lessons-learned)
- ['Immune digital twins' could simulate drug responses without risk — Medical Xpress, Oct 2025](https://medicalxpress.com/news/2025-10-immune-digital-twins-simulate-drug.html)
- [Predictive Persons: Privacy Law and Digital Twins — Petrie-Flom Center, Oct 2025](https://petrieflom.law.harvard.edu/2025/10/29/predictive-persons-privacy-law-and-digital-twins/)
