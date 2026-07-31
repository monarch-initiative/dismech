# Assessment of the OpenScientist report

**Hypothesis:** Canonical Th1/IFN-gamma effector polarization
**Assessor:** Codex
**Verdict:** **PARTIALLY_SUPPORTED**

The report supports a real and important IFN-gamma/Th1 arm, and it correctly
rejects a Th1-exclusive account. Its strongest evidence comes from two small
human gastric-clone studies plus several complementary murine perturbations.
The report overstates these results when it moves from “important in a model”
to universal initiation, dominant human cell source, or direct genetic wiring.

## Evidence calibration

Human H+/K+-ATPase-reactive CD4 clones were frequently Th1-polarized and
cytotoxic
([PMID:11159878](https://pubmed.ncbi.nlm.nih.gov/11159878/),
[PMID:15763992](https://pubmed.ncbi.nlm.nih.gov/15763992/)). That is direct
human support, but it comes from a small number of selected clonal studies and
does not sample the complete infiltrate.

Anti-IFN-gamma reduced neonatal-thymectomy-model incidence from 69% to 16%;
calling this “abolished” is inaccurate
([PMID:8766575](https://pubmed.ncbi.nlm.nih.gov/8766575/)). A separate study
found that IFN-gamma-deficient or IL-17-deficient T cells could still initiate
mild gastritis, although both cytokines were needed for severe tissue
disruption. That study also located most IFN-gamma in CD8 cells in its
polyclonal mouse setting
([PMID:22777705](https://pubmed.ncbi.nlm.nih.gov/22777705/)). These are
model-dependent results, not a contradiction that can be erased by calling
IFN-gamma universally required for initiation.

Murine organoid and knockout work strongly supports direct epithelial effects
and a requirement for IFN-gamma in TxA23 atrophy/metaplasia
([PMID:30511397](https://pubmed.ncbi.nlm.nih.gov/30511397/)). IL-13/IL-4R-alpha
is a separable, required metaplastic arm
([PMID:34587523](https://pubmed.ncbi.nlm.nih.gov/34587523/)), but “independent
of IFN-gamma” is too broad because metaplasia was absent in the IFN-gamma
knockout trajectory.

The PTPN22 synthesis is an inference across two studies, not direct genetic
proof of gastric polarization. One associates a locus with pernicious anemia;
the other measures immune phenotypes in genotyped donors
([PMID:34145262](https://pubmed.ncbi.nlm.nih.gov/34145262/),
[PMID:23333624](https://pubmed.ncbi.nlm.nih.gov/23333624/)). The report also
misstates the GWAS p value as 1.91×10^-10 rather than 1.91×10^-24.

NK depletion in one model does not “rule out innate IFN-gamma sources”
([PMID:11905844](https://pubmed.ncbi.nlm.nih.gov/11905844/)). The ontology
candidate GO:0010656 is likewise wrong: it denotes negative regulation of
muscle-cell apoptosis, not epithelial-cell apoptotic process.

## Disease-YAML follow-up

This assessment does not edit `kb/disorders/Autoimmune_Gastritis.yaml`, but its
current notes repeat several conclusions that need a separate evidence pass:

- anti-IFN-gamma is said to prevent disease without the residual incidence and
  model conflict;
- the PA-associated PTPN22 variant is said to favor Th1 over Th17 in AIG;
- IL-13 is said to drive metaplasia independently;
- the intrinsic-factor/pernicious-anemia compartment is called
  Th17-dominant, although the cited 94% combines Th17 **or** Th1 clones.

The disease-level account should retain canonical IFN-gamma/Th1 involvement,
state the species and model for causal perturbations, and leave human cell-type
dominance and stage-specific polarization unresolved.
