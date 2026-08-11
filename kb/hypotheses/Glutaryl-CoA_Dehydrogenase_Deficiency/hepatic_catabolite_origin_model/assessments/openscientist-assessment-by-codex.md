# Hepatic catabolite-origin report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Executive judgment

The report chooses the right overall category. Liver-directed interventions in
the severe GA1 mouse model provide strong evidence that hepatic lysine
catabolism can materially affect brain metabolite burden and neurological
outcome. They do not establish that the liver is the predominant source in
patients, identify which molecular species crosses the blood-brain barrier, or
quantify hepatic versus intracerebral contributions.

The report is unusually useful in recognizing a likely dual-compartment model,
but several of its mechanistic details are not reliable:

- it assigns GCDH a reaction on free glutaric acid that the enzyme does not
  catalyze;
- it calls hepatic production “quantitatively major” despite acknowledging
  that source partitioning has never been performed;
- it treats a global `Aass` knockout as compartment-specific evidence;
- it says no in-vivo BBB transport study exists, missing a directly relevant
  2008 radiotracer experiment;
- it turns structural BBB injury into an asserted increase in catabolite
  influx despite contrary tracer evidence; and
- it supplies several ontology identifiers for unrelated entities.

The defensible conclusion is partial support for a significant *mouse hepatic
contribution*, with source predominance and human translation unresolved.

## What is supported

### Liver perturbation changes brain outcome in mice

The central evidence is strong within its experimental scope.
[PMID:37075130](https://pubmed.ncbi.nlm.nih.gov/37075130/) used several
complementary interventions:

- healthy hepatocyte repopulation protected global `Gcdh`-knockout mice;
- diseased hepatocytes restored brain accumulation and lethality in
  `Gcdh/Aass` double-knockout recipients;
- liver-specific AAV-`Gcdh` reduced brain metabolites and pathology; and
- liver-directed `Aass` editing protected against high-protein-diet lethality.

These experiments show that the liver can causally modulate the brain phenotype
in this mouse system. The transported species was not identified, and all
results come from one publication and research program.

### A dual-compartment synthesis is plausible

Cultured `Gcdh`-deficient astrocytes can produce and release GA and 3-OHGA from
lysine
([PMID:25968119](https://pubmed.ncbi.nlm.nih.gov/25968119/)), while the liver
experiments show a peripheral contribution. Earlier hepatic-only knockout and
peripheral-loading work found low brain accumulation
([PMID:16573641](https://pubmed.ncbi.nlm.nih.gov/16573641/)). Together these
data fit a dual-source model better than either exclusive source.

They do not yet identify the fraction contributed by each source under basal
conditions, catabolic crisis, or human disease.

## Major corrections

### 1. The proposed free-GA clearance reaction is biochemically wrong

The report says intact brain GCDH can convert peripherally entering GA to
crotonyl-CoA. GCDH acts on **glutaryl-CoA**, not free glutaric acid. The classic
enzyme assay explicitly measures conversion of glutaryl-CoA
([PMID:3182847](https://pubmed.ncbi.nlm.nih.gov/3182847/)).

Brain GCDH status remains an important difference between the Sauer and Barzi
designs, but it does not establish the report's stated free-GA detoxification
reaction. The Barzi paper itself says the actual molecule crossing the BBB
still needs to be identified.

### 2. “Quantitatively major” is unsupported

Neither the liver-intervention study nor the global `Aass` knockout performs
isotope tracing or tissue-specific source partitioning. Global `Aass` deletion
reduced GA in brain and liver
([PMID:32567100](https://pubmed.ncbi.nlm.nih.gov/32567100/)), but that design
cannot determine whether the lower brain pool arose locally, from reduced
hepatic supply, or both.

The experiments establish a hepatic contribution. They do not establish
predominance.

### 3. A directly relevant in-vivo transport study was missed

The report states that no in-vivo BBB transport experiment for GA or 3-OHGA
exists. In 2008, investigators injected radiolabeled 3-OHGA into wild-type and
`Gcdh`-knockout mice and measured tissue distribution both at baseline and
during a high-protein-diet encephalopathic crisis
([PMID:18348873](https://pubmed.ncbi.nlm.nih.gov/18348873/)). Brain recovery
was low and decreased rather than increased during crisis.

That result does not explain the later liver-transplant experiments; they may
involve another transported metabolite or precursor. It does directly disprove
the report's claimed literature gap and constrains its crisis-permeability
story.

### 4. BBB breakdown is not evidence of increased 3-OHGA influx

The vascular study
([PMID:24468193](https://pubmed.ncbi.nlm.nih.gov/24468193/)) documented
capillary occlusion and tight-junction disruption. It did not trace hepatic
metabolites into brain. The direct radiotracer study found limited 3-OHGA entry
during a diet-induced crisis. Structural injury and molecular influx therefore
must not be treated as interchangeable observations.

### 5. Arginine evidence does not localize the metabolite source

The 12-child lysine-free, arginine-rich formula study used historical controls
and changed several variables at once, including dietary and plasma lysine,
arginine, gastrointestinal transport, modeled cerebral influx, and
hospitalization frequency
([PMID:21820344](https://pubmed.ncbi.nlm.nih.gov/21820344/)). The mouse work
also proposed competition at both the BBB and mitochondrial carriers
([PMID:20923787](https://pubmed.ncbi.nlm.nih.gov/20923787/)).

These studies support lysine-flux reduction and are compatible with local brain
production. They do not independently quantify or confirm compartmental
origin.

### 6. The ontology block contains multiple wrong identifiers

- `MONDO:0009280` is monosodium glutamate sensitivity; GA1 is
  `MONDO:0009281`.
- `GO:0019470` is trans-4-hydroxy-L-proline catabolism, not lysine catabolism.
- `GO:0033512` is obsolete and denotes lysine catabolism via L-saccharopine,
  not the report's pipecolic-acid label.
- `GO:0015804` is neutral-amino-acid transport, not the cationic lysine/arginine
  transport discussed here.
- `CL:0002543` is vein endothelial cell, not brain capillary endothelial cell.

None should be copied from the report without remapping.

## Curation implications

Keep `hepatic_catabolite_origin_model` as `EMERGING`, but narrow its description
from “predominant hepatic generation” to a significant hepatic contribution in
mouse models. Represent the exact transported species and quantitative
liver-versus-brain fractions as unresolved.

The current disorder YAML already repeats the provider's “predominant hepatic”
description and encodes systemic transport as a known-intermediate causal edge,
even though the Barzi study leaves the transported species unknown. It also
uses a sentence describing the historical intracerebral view as if it were
supporting experimental evidence. Those are separate disease-curation
follow-ups; this assessment-only PR does not edit the disease YAML or reference
cache.

## Most discriminating next evidence

The cleanest experiment combines tissue-specific `Aass` or `Gcdh`
perturbations with stable-isotope tracing that can distinguish a liver-derived
species from brain-local synthesis. It should measure labeled precursors and
products in plasma, liver, CSF, and brain at baseline and during high-protein
stress. Independent replication in a second model and eventual paired human
plasma/CSF data are needed before extrapolating source predominance to patients.
