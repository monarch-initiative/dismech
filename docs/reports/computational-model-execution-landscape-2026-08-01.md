# Computational Model Execution: State of the Art (2026-08-01)

**Scope.** Two questions: (1) what is in the dismech `computational_models` index today, and
(2) what does it currently take to actually *run* these models — is there an uber-framework,
and what needs HPC?

Companion documents: [`explanation/computational-models.md`](../explanation/computational-models.md)
(the in-repo `dismech-perturb` runner), and the new **Computational Models Browser**
(`app/models/index.html`, built by `just gen-models-data`).

---

## 1. What dismech actually indexes

42 models across 15 entries (14 disorders + 1 mechanism module), as of this report.

| `model_type` | Count | Representative entries |
|---|---:|---|
| `GENOME_SCALE_METABOLIC` | 16 | Recon3D+PAH KO (PKU), Harvey WBM, AGORA2, MICOM |
| `KINETIC` (ODE) | 9 | Topp beta-cell (BIOMD0000000341), Peterson-Riggs Ca/bone (BIOMD0000000613), ToR-ORd myocyte, urate homeostasis, HPT axis |
| `AGENT_BASED` | 5 | PDAC CAF-invasion + immunotherapy PhysiCell, tumor-immune PhysiCell, α-synuclein prion-like spreading |
| `PHYSIOLOGICAL` (PBPK/organ) | 5 | GLP-1 RA PBPK, CKD-MBD multiscale, mucociliary CFD, basal-ganglia spiking network |
| `MACHINE_LEARNING` | 3 | drexml drug repurposing, FA episignature classifier, FA core-complex structure |
| `FLUX_BALANCE_ANALYSIS` | 1 | Multi-compartment PKU FBA |
| `BOOLEAN_NETWORK` | 1 | FA/BRCA pathway Boolean model |
| unclassified | 2 | (Fanconi anemia entries missing `model_type`) |

**Formats and software are thinly populated**: only 13/42 record a `model_format` (7 SBML,
2 CellML, 4 PhysiCell `C++/XML/CSV`) and 16/42 a `model_software` (COBRApy 5, PhysiCell 4,
COPASI 3, Antimony/tellurium 2). Twenty-two have no `repository_url` at all. **Nothing in the
KB is annotated with Antimony as an exchange format** — Antimony appears only as
`model_software: Antimony/tellurium` on the two models dismech authored itself; those are
*stored* as SBML (`models/*.ant` is the human-editable source, `models/*.xml` the artifact
that is actually loaded).

Four models are **runnable in-repo today** via `dismech-perturb` — `urate_homeostasis`,
`hpt_feedback_axis`, `BIOMD0000000341`, `BIOMD0000000613` — each with a
`models/<model_id>.config.yaml` mapping gene perturbations onto model parameters. The other 38
are literature references. The models browser exposes this as the **Runnable In-Repo** facet;
it is the single most useful signal in the index.

There are **no constraint-based models with an executable in-repo path**, despite metabolic
models being the largest category. That is the widest gap between what dismech catalogues and
what it can run.

---

## 2. Is there an uber-framework?

**Short answer: yes for biochemical-network models, no for anything else.**

Note on terminology, since it comes up: the constraint-based ecosystem is **COBRA**
(COnstraint-Based Reconstruction and Analysis) — unrelated to CORBA, the 1990s distributed-object
middleware.

### 2.1 The COMBINE standards stack — the closest thing to an uber-framework

The COMBINE community maintains a layered stack that genuinely does decouple *model* from
*simulation* from *engine*:

- **SBML** — the model (reactions, species, parameters). Also **SBML-qual** for logical/Boolean
  models, **SBML-fbc** for constraint-based models, **CellML** for the Physiome/electrophysiology
  side, **NeuroML** for neuronal models, **BNGL/Kappa** for rule-based models.
- **SED-ML** — the *simulation experiment*: which model, which parameter changes, which
  algorithm, which time course, which outputs. This is the piece SBML deliberately omits, and
  its absence is exactly why "here is the SBML" does not reproduce a paper figure.
- **KiSAO** — an ontology of simulation algorithms, so "CVODE with these tolerances" is a
  machine-readable term rather than prose.
- **COMBINE/OMEX archive** — a ZIP of model + SED-ML + manifest + metadata; one file that is a
  complete, executable experiment.

**[BioSimulators](https://biosimulators.org/)** is the execution layer over that stack: a registry
of simulation engines, each packaged as a Docker image behind a *uniform command-line interface*
that takes an OMEX archive in and writes results out. Pulling the registry API today gives
**54 registered engines**:

| Modeling framework | Engines | Examples |
|---|---:|---|
| Continuous / ODE (SBO:0000293) | 23 | COPASI, tellurium, AMICI, VCell, libSBMLSim, PySCeS |
| Flux balance (SBO:0000624) | 14 | COBRApy, COBRA Toolbox, CBMPy, RAVEN, OptFlux, MASSpy |
| Stochastic / discrete (SBO:0000295) | 12 | GillesPy2, BioNetGen, iBioSim, E-Cell 4 |
| Logical / Boolean (SBO:0000547) | 6 | GINsim, MaBoSS, BoolNet, boolSim, Cell Collective |
| Spatial continuous / particle | ~8 | Morpheus, Smoldyn, MCell, VCell, SimVascular |

32 of the 54 accept SBML. **[runBioSimulations](https://run.biosimulations.org/)** is the hosted
front end — you upload an OMEX archive and it executes it on their infrastructure, no local
install. This is the answer to "can I just run this model?" for anything SBML/CellML-shaped.

**What is conspicuously absent from that list: PhysiCell, openCARP, Chaste.** Multicellular
agent-based simulation and whole-organ electrophysiology are outside the COMBINE stack entirely.
That is not an oversight in the registry — it reflects that these domains have no equivalent
declarative model-exchange standard, so there is nothing for a uniform runner to consume.

### 2.2 Composition across frameworks — Vivarium

[**Vivarium**](https://vivarium-collective.github.io/) (Agmon et al., *Bioinformatics* 2022) is
the serious attempt at the next layer up: an engine for wiring *heterogeneous* simulators into one
composite model, with explicit ports and a shared state store. Its `BiosimulatorProcess` wrapper
turns any BioSimulators engine into a Vivarium process, so e.g. an ODE model and an FBA model can
be co-simulated (`ODE_FBA`) with the ODE supplying fluxes as FBA bounds. The associated
"Compositional Systems Biology" programme (arXiv 2408.00942) is the current articulation of where
this is going.

Vivarium is the right conceptual model for what dismech's pathographs imply — a molecular ODE node
feeding a cellular Boolean node feeding a tissue-scale ABM. It is also, realistically, a research
framework rather than a turnkey product; composing two models still requires writing the coupling
by hand.

### 2.3 Per-domain silos that are each mature on their own terms

| Domain | Ecosystem | Run it how |
|---|---|---|
| ODE / kinetic | tellurium + libRoadRunner, COPASI/BasiCO, AMICI, PySCeS | `pip install`, seconds on a laptop |
| Constraint-based | **COBRA**: COBRApy (Python), COBRA Toolbox (MATLAB), plus MICOM, pymgpipe for communities | `pip install cobra`; needs an LP solver |
| Logical / Boolean | **CoLoMoTo** — 20 tools (GINsim, bioLQM, MaBoSS, Pint, BNS) in one Docker image + Jupyter notebook | `docker run colomoto/colomoto-docker` |
| Multicellular ABM | PhysiCell (C++/OpenMP), Morpheus, Chaste, CompuCell3D; FLAME GPU 2 for GPU | compile from source; XML config |
| Cardiac EP | openCARP, MonoAlg3D | HPC/GPU, see §3 |
| PBPK | Open Systems Pharmacology (PK-Sim/MoBi, GPLv2); Simcyp/GastroPlus commercial | desktop GUI; **no common exchange format until recently** |
| Single-cell ML | scGPT, Geneformer, UCE, TranscriptFormer, Arc STATE | GPU inference; HuggingFace-style weights |

The recurring pattern: **each silo has a good runner; there is no runner that spans silos.** The
COMBINE stack unifies the biochemical-network silos (ODE + FBA + Boolean + stochastic); Vivarium
tries to unify above that; ABM, cardiac EP, PBPK and ML each sit outside with their own
conventions.

Worth flagging as a genuinely recent development: the PARC **FAIR PBK standard** (2026) adopts SBML
as the exchange format for PBPK models with PBPKO annotation — the first credible attempt to pull
the PBPK silo into the COMBINE stack.

### 2.4 The reproducibility reality check

[Verification and reproducible curation of the BioModels repository](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013239)
(PLOS Comp Biol, 2025) is the sobering data point. BioModels holds ~1,100 manually curated models,
but **only about half of entries contained SED-ML files**, and those that did reflected whatever
SED-ML version was current at deposition. The paper builds a testable pipeline that pushes
SBML+SED-ML through five wrapped simulators and diffs the results — which is to say, executability
of a curated public model is still something you have to *verify*, not assume.

Both BioModels entries dismech cites (BIOMD0000000341, BIOMD0000000613) are curated and do run —
they are the two that `dismech-perturb` executes today.

---

## 3. What actually needs HPC

The honest split is roughly three tiers.

### Tier 1 — laptop, seconds (most of what dismech indexes)

- **ODE/kinetic models.** A BioModels-scale ODE system integrates in milliseconds. All four
  runnable dismech models are here. Parameter scans of thousands of conditions are still laptop
  work.
- **Single-organism FBA.** Recon3D (~10k reactions, ~6k constraints) solves in **0.1–1.0 s** per
  LP with a good solver. Gene-deletion screens over every gene in the model are minutes.
- **Boolean networks.** Attractor computation on the FA/BRCA-scale networks is trivial; the
  CoLoMoTo Docker image runs the whole toolchain interactively.

The practical constraint at this tier is not compute, it is the **LP solver license**. GLPK and
COIN-OR are free but slow enough that benchmark studies moved them to an 8-core/16 GB cluster;
Gurobi and CPLEX are dramatically faster and are what the COBRA and MICOM documentation actually
recommends. Both offer free academic licenses. This is a licensing/packaging problem, not a
hardware problem.

### Tier 2 — workstation to single HPC node

- **PhysiCell agent-based models** (4 of dismech's 5 ABM entries). OpenMP shared-memory parallel;
  scales roughly linearly in cell count. **10⁵–10⁶ cells is feasible on a quad-core desktop**;
  millions of cells needs a single HPC node. The PDAC models dismech cites are well inside desktop
  range. GPU ports (PhysiCell_GPU via OpenACC, FLAME GPU 2, Gell) report up to ~150× over multicore
  PhysiCell but are not the mainline.
- **Whole-body metabolic models (Harvey/Harvetta).** >80,000 reactions across 26 organs — large
  enough that *the authors do not distribute them as SBML* ("SBML format would be too large"); they
  ship as MATLAB `.mat` with the PSCM Toolbox extension to the COBRA Toolbox. LP is O(n³)-ish in
  practice, so an 8× larger model is ~8× the work per doubling. Single personalised WBM solves in
  minutes on a workstation with a commercial solver; the cost is **MATLAB + Gurobi/CPLEX**, not
  cores.
- **Community microbiome models (MICOM, AGORA2).** Per-sample community FBA is comparable to
  single-species FBA. The scaling axis is *number of samples* — an embarrassingly parallel sweep
  over a metagenomic cohort, which is a job-array problem, not a tightly-coupled HPC problem.

### Tier 3 — genuinely needs HPC/GPU

- **Whole-heart electrophysiology digital twins.** This is the one unambiguous HPC case. MonoAlg3D
  (2025) reports **10.94× speedup on GPU over CPU**, and scaling to **512 simulations across 128
  compute nodes**; a coarse biventricular mesh runs in <24 min, a fine mesh in **303 min**.
  openCARP is the standard finite-element framework here. dismech's Long QT entry cites ToR-ORd,
  which is a *single-cell* myocyte model (CellML, tier 1) — the tissue/organ escalation is where
  the cost appears.
- **CFD / continuum mechanics.** The Primary Ciliary Dyskinesia mucociliary-clearance model is an
  in-house immersed-boundary solver; this class is HPC-bound and, notably, has no repository and no
  standard format.
- **Single-cell foundation models.** scGPT (~33M cells), Geneformer (~30M, extended to 95M), Arc
  Institute's STATE (167M observational + >100M perturbational cells). **Training is large-cluster
  GPU work; inference is single-GPU.** For dismech's purposes only inference matters — running an
  in-silico perturbation against a released checkpoint is a single-GPU or even CPU-with-patience
  task. VCBench (2026) benchmarks Geneformer, scGPT, UCE, TranscriptFormer and Arc STATE across
  seven capability dimensions, and the recurring finding across independent benchmarks is that
  these models still struggle to beat simple linear baselines on perturbation prediction — worth
  keeping in mind before treating them as an oracle.

**Summary:** of the 42 models dismech indexes, roughly 30 are tier 1, ~10 are tier 2, and 2–3 are
tier 3. The framing "do these need HPC?" mostly resolves to **no** — the binding constraints are
solver licenses, MATLAB dependencies, missing format annotations, and models that were never
deposited anywhere.

---

## 4. Implications for dismech

Ordered by effort-to-value:

1. **Backfill `model_format` / `model_software` / `repository_url`.** 29/42 models have no format
   recorded and 22/42 no repository. These are the fields the new browser facets on, and they are
   the fields that decide whether a model is runnable at all. Cheap, mechanical, high value.
2. **Record a BioSimulators-compatible execution hint.** For any SBML/CellML model, note the
   BioModels/Physiome ID and whether an OMEX/SED-ML archive exists. That single fact is the
   difference between "cited" and "one `docker run` from reproducible".

   *Done for the four runnable models* (2026-08-01): `just sedml-export` emits SED-ML L1V3 +
   COMBINE archives from the `models/*.config.yaml` scenario definitions — see
   [Exporting Scenarios as SED-ML / COMBINE Archives](../explanation/computational-models.md).
   Three of the four export (43 scenarios); the CKD-MBD model does not, because its coupled
   base+extension co-simulation with inter-step Hill feedback has no SED-ML equivalent — a
   concrete instance of the §2.2 composition gap that Vivarium, not SED-ML, is the answer to.

   Run results are now persisted too: `just gen-model-results` writes
   `exports/model_runs/<model_id>.json` — per scenario, the final observable values, fold change
   vs baseline, and the HP phenotypes the curated thresholds activate — and the disorder pages
   render it. All four runnable models produce results (54 scenarios, 42 activating a phenotype),
   including the CKD-MBD model that SED-ML cannot express: dismech-perturb runs the coupled
   co-simulation natively, which is precisely why the artifact is worth keeping.
3. **Add a COBRApy execution path alongside `dismech-perturb`.** Metabolic models are dismech's
   largest category with zero runnable entries. The PKU Recon3D+PAH-knockout case is the obvious
   pilot: `cobra.io.read_sbml_model` → knock out PAH → FBA → read the phenylalanine flux, mapping
   onto the existing `ModelVariable`/`threshold`/`severity_scale` machinery exactly as the ODE path
   does. No new schema needed.
4. **Treat `model_type: MACHINE_LEARNING` as a distinct execution class.** It shares no
   infrastructure with the mechanistic models; the `FOUNDATION_MODEL` and `PERTURBATION_PREDICTION`
   enum values already exist and should be used instead of the generic `MACHINE_LEARNING` where
   they apply.
5. **Consider Vivarium as the long-term target for pathograph-coupled simulation**, but not as a
   near-term dependency. The composition problem dismech's multi-scale pathographs pose is exactly
   the one Vivarium models — it is just not yet a turnkey runner.

---

## Sources

- [BioSimulators registry](https://biosimulators.org/) and [`api.biosimulators.org/simulators/latest`](https://api.biosimulators.org/simulators/latest) (54 engines, queried 2026-08-01)
- [BioSimulators: a central registry of simulation engines and services](https://academic.oup.com/nar/article/50/W1/W108/6582178), *NAR* 2022
- [BioSimulations / BioSimulators documentation](https://docs.biosimulations.org/)
- [Verification and reproducible curation of the BioModels repository](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013239), *PLOS Comp Biol* 2025
- [Vivarium: an interface and engine for integrative multiscale modeling](https://academic.oup.com/bioinformatics/article/38/7/1972/6522109), *Bioinformatics* 2022; [Vivarium Collective](https://vivarium-collective.github.io/); [Prelude to a Compositional Systems Biology](https://arxiv.org/html/2408.00942v1)
- [Reproducible Boolean model analyses with the CoLoMoTo software suite](https://royalsocietypublishing.org/rsfs/article/15/3/20250002/235797/Reproducible-Boolean-model-analyses-and), *Interface Focus* 2025 (20 tools, Docker)
- [PhysiCell: an open source physics-based cell simulator](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1005991), *PLOS Comp Biol* 2018 (OpenMP scaling, 10⁵–10⁶ cells desktop)
- [An agent-based model for cell microenvironment simulation using FLAMEGPU2](https://www.sciencedirect.com/science/article/pii/S0010482524009168) (GPU ABM)
- [Personalized whole-body models integrate metabolism, physiology, and the gut microbiome](https://pubmed.ncbi.nlm.nih.gov/32463598/) (Harvey/Harvetta, >80k reactions); [PSCM Toolbox](https://opencobra.github.io/cobratoolbox/stable/modules/analysis/wholeBody/PSCMToolbox/index.html)
- [A benchmark of optimization solvers for genome-scale metabolic modeling](https://pmc.ncbi.nlm.nih.gov/articles/PMC10878033/) (Recon3D 0.1–1.0 s per LP; GLPK/COIN-OR cluster runs)
- [COBRApy](https://opencobra.github.io/cobrapy/); [MICOM](https://www.biorxiv.org/content/10.1101/361907v3.full)
- [Toward cardiac electrophysiology digital twins with an efficient open source scalable solver on GPU clusters](https://www.nature.com/articles/s41598-025-33709-w), *Sci Rep* 2025 (MonoAlg3D: 10.94× GPU speedup, 512 sims / 128 nodes, 303 min fine mesh)
- [Open Systems Pharmacology / PK-Sim](https://www.open-systems-pharmacology.org/); [An exchange standard for FAIR PBK models in chemical risk assessment](https://www.sciencedirect.com/science/article/pii/S2468111326000277) (PARC, SBML + PBPKO)
- [VCBench: A Multi-Dimensional Benchmark for Single-Cell Foundation Models](https://www.biorxiv.org/content/10.64898/2026.06.18.733146v1); [Arc Institute Virtual Cell Initiative / STATE](https://arcinstitute.org/virtual-cell-initiative)
- [BiSDL: a modeling language for multicellular synthetic biological systems](https://pmc.ncbi.nlm.nih.gov/articles/PMC11046772/) (on SBML/SED-ML scope limits for multi-level models)
