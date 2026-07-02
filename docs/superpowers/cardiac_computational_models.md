# Computational models of cardiac disease — landscape survey

_Provenance/reference document for dismech curation of `computational_models:`
blocks on cardiac disorder entries. Compiled July 2026. All PMIDs below were
verified against PubMed records or the publisher page; the four flagged as
"search-confirmed" were taken from search-result summaries with matching PubMed
links but not individually re-opened — double-check before hard-committing them
to a KB entry._

## Why this matters for dismech

Cardiac electrophysiology is the most model-rich subfield of physiology, and the
dismech schema already supports it: the top-level `computational_models:` slot
(`ComputationalModel` class) captures ODE/PDE and other in-silico models, with
`model_type: KINETIC` for ODE systems, `variables` (each `ModelVariable` with a
native `dataset_identifier`, `unit`, and ontology `mappings_list`), and
`ModelVariableDescriptor` thresholds/`severity_scale` that link a state-variable
value to an HP phenotype. Evidence uses `evidence_source: COMPUTATIONAL`. The
prior worked example was `CKD-Mineral_Bone_Disorder.yaml` (Peterson-Riggs ODE
model, `BIOMD0000000613`); `Long_QT_Syndrome.yaml` is now the first **cardiac**
worked example (ORd, CiPA IKr-dynamic ORd, ToR-ORd).

## Models organized by spatial scale

Cardiac modeling is canonically **multiscale**: ODEs describe subcellular fluxes
and single-cell membrane dynamics; those cell models become the *reaction* term
inside tissue/organ **reaction-diffusion PDEs**; continuum finite-element
mechanics (plus fluid-structure interaction for blood) closes the
electromechanical loop.

### Subcellular / organelle (ODE systems)

| Sub-system | What is modeled | Representative models |
|---|---|---|
| Mitochondrial bioenergetics | TCA cycle, oxidative phosphorylation, ATP/ADP, NADH, membrane potential, matrix Ca²⁺ | Cortassa–Aon–Marbán–Winslow–O'Rourke 2003; ECME extension (Cortassa 2006) |
| Ca²⁺ handling / SR | L-type Ca²⁺ current, RyR2 Ca²⁺-induced Ca²⁺ release, SERCA uptake, compartmental Ca²⁺ | Shannon–Bers 2004 (reference SR/Ca²⁺ framework) |
| Myofilament / contraction | Cross-bridge cycling, Ca²⁺–troponin binding, length/tension dependence | Rice et al. 2008; Land et al. (used with ToR-ORd) |

These ODE sub-models are usually *plugged into* a single-cell electrophysiology
model rather than run alone.

### Single-cell cardiomyocyte electrophysiology (Hodgkin–Huxley lineage)

Systems of ODEs for membrane potential + gating variables + ion concentrations:

- **Hodgkin–Huxley 1952** (squid axon) — mathematical template, not cardiac.
- **Noble 1962** — first cardiac model (Purkinje fibre).
- **Beeler–Reuter 1977** — first mammalian ventricular AP.
- **Luo–Rudy I (1991) / II dynamic (1994)** — guinea-pig ventricle; 1990s workhorse.
- **Courtemanche 1998 / Nygren 1998** — foundational human *atrial* cell models (AF substrate).
- **Shannon–Bers 2004** — rabbit ventricle, gold-standard Ca²⁺ handling.
- **ten Tusscher 2004 / ten Tusscher–Panfilov 2006** — first widely adopted *human* ventricular models, efficient enough for tissue/organ use.
- **Grandi–Pasqualini–Bers 2010** — human ventricular AP + Ca²⁺ transient; strong for CaMKII / heart-failure remodeling.
- **O'Hara–Rudy "ORd" 2011** — modern reference human ventricular model; CiPA consensus model.
- **ToR-ORd (Tomek et al. 2019)** — ORd refinement (corrected reversal potentials, reformulated I_CaL, replaced hERG), validated in disease and drug block, cell-to-ECG.
- **Paci et al. hiPSC-CM models (2013 →)** — human iPSC-derived cardiomyocyte models (the main in-vitro human platform).

Key ventricular currents: I_Na, I_CaL, I_Kr (hERG — central to drug safety),
I_Ks, I_K1, I_to, I_NaCa, I_NaK, plus SR fluxes and CaMKII regulation.

### Tissue / organ (reaction-diffusion PDEs)

- **Monodomain** — single reaction-diffusion PDE (cell ionic model = reaction term + diffusion term); cheaper, assumes equal anisotropy ratios.
- **Bidomain** — coupled intra/extracellular PDE pair; required for defibrillation, external stimulation, ECG/body-surface potentials, unequal anisotropy.
- **Whole-heart / organ** — 3D geometries + fiber orientation for arrhythmia mechanism, ablation planning, in-silico drug trials (reviewed in Clayton 2011).

### Mechanics / finite-element and fluid-structure

- Nonlinear anisotropic hyperelastic constitutive laws (Guccione, Holzapfel–Ogden) + active tension → electromechanical whole-heart models.
- Fluid-structure interaction couples deforming myocardium/valves to intracavitary blood flow (Navier–Stokes). Basis of "cardiac digital twin" pipelines.

## Mapping model types to diseases (and candidate dismech entries)

| Disease | Typical modeling approach | dismech entry |
|---|---|---|
| Long QT syndrome | Ventricular ODE (ORd/ToR-ORd/Grandi) with I_Kr↓ (LQT2), I_Ks↓ (LQT1), late I_Na↑ (LQT3) → APD↑ → EADs | `Long_QT_Syndrome` ✅ (done) |
| Drug-induced TdP | CiPA IKr-dynamic ORd + multi-channel pharmacology → qNet | `Long_QT_Syndrome` ✅, `Torsade_De_Pointes_Syndrome_With_Short_Coupling_Interval` |
| Brugada syndrome | Ventricular cell + tissue, reduced I_Na (SCN5A) / altered I_to, transmural heterogeneity | `Brugada_Syndrome` |
| Short QT syndrome | Ventricular ODE with gain-of-function K⁺ currents → APD↓ | `Short_QT_Syndrome` |
| CPVT | Ca²⁺-handling models (Shannon–Bers/Grandi) with RyR2/CASQ2 leak → DADs | `RYR2_CPVT` |
| Atrial fibrillation | Courtemanche/Nygren atrial cell → 2D/3D tissue; rotor/ablation studies | `Atrial_Fibrillation`, `Familial_Atrial_Fibrillation` |
| HCM / DCM | Electromechanical FEM + cell remodeling (ToR-ORd validated in HCM) | `Hypertrophic_Cardiomyopathy`, `Dilated_Cardiomyopathy` |
| Heart failure | Cell remodeling (Grandi/Shannon–Bers) + organ electromechanics | `Heart_Failure` |
| MI / ischemia | Tissue reaction-diffusion with regional hyperkalemia/acidosis, scar geometry | `Myocardial_Infarction` |

### The CiPA initiative

CiPA (Comprehensive in vitro Proarrhythmia Assay; FDA/HESI/CSRC) replaces the
hERG-plus-QT paradigm with mechanistic in-vitro ion-channel data + an in-silico
cell model + hiPSC-CM confirmation. The consensus in-silico model is the ORd
model with a **Markov IKr model capturing dynamic drug–hERG binding**
("IKr-dynamic ORd"), optimized in Dutta 2017; the **qNet** metric stratifies
high/intermediate/low TdP risk.

## Repositories, databases, and software

| Resource | What it is | Identifiers | Landmark |
|---|---|---|---|
| CellML / Physiome Model Repository (PMR2) | Curated CellML cell/tissue models; hosts nearly all named cardiac cell models | `models.cellml.org/e/<id>` exposures (ORd = `e/71`, ToR-ORd = `e/5f1`) | Yu 2011 (PMID:21216774) |
| BioModels | EBI repository (mostly SBML) | `BIOMD0000000xxx` (curated) | Malik-Sheriff 2020 (PMID:31701150) |
| openCARP | Open-source cardiac EP simulator (mono/bidomain); successor to CARP | opencarp.org | Plank 2021 (PMID:34171774) |
| Chaste | C++ library for cardiac EP; strong CellML integration | github.com/Chaste | Mirams 2013 (PMID:23516352) |
| FDA/CiPA | Reference implementation of the IKr-dynamic ORd + qNet pipeline | github.com/FDA/CiPA | Dutta 2017 (PMID:28878692) |
| ToR-ORd | Model code (MATLAB + CellML), validation pipeline | github.com/jtmff/torord | Tomek 2019 (PMID:31868580) |
| Cardiac Atlas Project | Imaging + statistical shape/motion atlases of normal/pathological hearts | cardiacatlas.org | Fonseca 2011 (PMID:21737439) |

**Identifier conventions:** BioModels `BIOMD0000000###`; Physiome/CellML
human-readable exposure URIs (`models.cellml.org/e/<id>`). dismech's schema
declares a `biomodels:` prefix; there is no `physiome:`/`cellml:` prefix yet, so
CellML models are referenced by full `repository_url`.

## Landmark papers with verified PMIDs

### Single-cell electrophysiology lineage

| Model | Citation | PMID |
|---|---|---|
| Noble Purkinje | Noble D. J Physiol. 1962;160(2):317–352. | 14480151 |
| Beeler–Reuter | Beeler GW, Reuter H. J Physiol. 1977;268(1):177–210. | 874889 |
| Luo–Rudy I | Luo CH, Rudy Y. Circ Res. 1991;68(6):1501–1526. | 1709839 |
| Luo–Rudy II (dynamic) | Luo CH, Rudy Y. Circ Res. 1994;74(6):1071–1096. | 7514509 |
| Human atrial (Courtemanche) | Courtemanche M, Ramirez RJ, Nattel S. Am J Physiol. 1998;275(1):H301–H321. | 9688927 (search-confirmed) |
| Human atrial (Nygren) | Nygren A, et al. Circ Res. 1998;82(1):63–81. | 9440706 (search-confirmed) |
| Shannon–Bers Ca²⁺ | Shannon TR, et al. Biophys J. 2004;87(5):3351–3371. | 15347581 |
| ten Tusscher 2004 | ten Tusscher KHWJ, et al. Am J Physiol Heart Circ Physiol. 2004;286(4):H1573–H1589. | 14656705 |
| ten Tusscher–Panfilov 2006 | Am J Physiol Heart Circ Physiol. 2006;291(3):H1088–H1100. | 16565318 |
| ten Tusscher 2006 (efficient) | Phys Med Biol. 2006;51(23):6141–6156. | 17110776 |
| Grandi–Pasqualini–Bers | J Mol Cell Cardiol. 2010;48(1):112–121. | 19835882 |
| **O'Hara–Rudy (ORd)** | O'Hara T, Virág L, Varró A, Rudy Y. PLoS Comput Biol. 2011;7(5):e1002061. | **21637795** |
| **ToR-ORd** | Tomek J, et al. eLife. 2019;8:e48890. | **31868580** |

### hiPSC-CM models (Paci)

| Citation | PMID |
|---|---|
| Paci M, et al. Ann Biomed Eng. 2013;41(11):2334–2348. | 23722932 |
| Paci M, et al. Biophys J. 2020;118(10):2596–2611. (all-optical) | 32298635 (search-confirmed) |

### CiPA / drug-induced arrhythmia

| Citation | PMID |
|---|---|
| Sager PT, et al. Am Heart J. 2014;167(3):292–300. (CiPA rationale) | 24576511 |
| Colatsky T, et al. J Pharmacol Toxicol Methods. 2016;81:15–20. (CiPA update) | 27282641 |
| **Dutta S, et al. Front Physiol. 2017;8:616.** (IKr-dynamic ORd optimization) | **28878692** (corrigendum = 29230183) |

### Tissue/organ methods and review

| Citation | PMID |
|---|---|
| Clayton RH, et al. Prog Biophys Mol Biol. 2011;104(1–3):22–48. (mono/bidomain review) | 20553746 |

### Mitochondrial cardiac bioenergetics (Cortassa / O'Rourke)

| Citation | PMID |
|---|---|
| Cortassa S, et al. Biophys J. 2003;84(4):2734–2755. | 12668482 |
| Cortassa S, et al. Biophys J. 2006;91(4):1564–1589. (ECME) | 16679365 |
| Wei AC, et al. Biophys J. 2009;96(9):3510–3524. | 19289071 (search-confirmed) |

## Curation notes / how to extend

- Use `model_type: KINETIC` for ODE cell models; `PHYSIOLOGICAL` or
  `DIGITAL_TWIN` for organ/whole-heart PDE and electromechanical models. There is
  no dedicated "PDE" enum value.
- Map state-variable outputs to HP phenotypes via `ModelVariableDescriptor`
  thresholds. Treat thresholds as **model-calibrated illustrations, not clinical
  reference values** (e.g. APD90 is the cellular correlate of the QT interval,
  not a direct QT measurement) and say so in the variable/mapping `description`,
  exactly as the CKD-MBD entry does.
- All model evidence uses `evidence_source: COMPUTATIONAL` with an exact-quote
  snippet from the model paper's abstract; validate with the standard reference
  and term validators before committing.
- Next candidates in priority order: `RYR2_CPVT` (Shannon–Bers/Grandi Ca²⁺-leak
  DAD models), `Atrial_Fibrillation` (Courtemanche), `Brugada_Syndrome`
  (reduced-I_Na tissue models), `Hypertrophic_Cardiomyopathy` (ToR-ORd, validated
  in HCM), `Heart_Failure` (Grandi remodeling).
