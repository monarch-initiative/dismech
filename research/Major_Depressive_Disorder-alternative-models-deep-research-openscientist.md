---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T15:49:53.701315'
end_time: '2026-10-20T16:13:37.658405'
duration_seconds: 1423.96
template_file: templates/disease_alternative_models_research.md
template_sha: "fd383b2d1a33daa300c57674e5947cf02e77e337"
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 16
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Major_Depressive_Disorder-alternative-models-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Major_Depressive_Disorder-alternative-models-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Alternative Model Discovery Template

## Target Disease
- **Disease Name:** Major Depressive Disorder
- **MONDO ID:** MONDO:0002009

## Scope — Read This First

This is **not** a request for a general account of this disease. Its pathophysiology and clinical
features are already curated. The single question is narrow:

> **Which model systems, beyond the ones already curated, could be used to study the mechanisms
> this disease's pathograph records — and which specific pathograph nodes could each one
> legitimately support?**

What counts as an alternative model for this run:

Any model system not already curated for this entry: other mammalian species, non-mammalian vertebrates, invertebrates, and non-animal systems including iPSC-derived neurons, glia and co-cultures, brain and hippocampal organoids and assembloids, organ-chips, human post-mortem slice and explant culture, and primary cultures. Mouse and C. elegans models that are already curated are out of scope, but a *different* mouse or C. elegans model that reaches an unmodelled node is in scope. Say which schema block each candidate belongs in.

A report that returns models already listed below, or that proposes a model without naming the
pathograph node it serves, has failed this brief.

## What Is Already Curated — Do Not Re-Derive Any Of It

Animal models already curated:

- **tph-1 serotonin-null C. elegans** (Caenorhabditis elegans; PMID:17141627), clade: invertebrate
    - linked to: Monoamine Deficiency
- **daf-2 insulin-receptor loss-of-function immobility C. elegans** (Caenorhabditis elegans; PMID:29230398), clade: invertebrate
    - linked to: Reference Point Dysregulation
- **Serotonergic-neuron p38alpha MAPK conditional knockout mouse under social defeat** (Mouse; PMID:21835346), clade: mammal
    - linked to: Monoamine Deficiency
- **Astrocyte-specific Fgf13 knockout and overexpression mouse under chronic stress** (Mouse; PMID:42421017), clade: mammal
    - linked to: Neuroinflammation
- **Gsdmd, Casp1 and astrocytic Nlrp3 knockout mice under chronic mild stress** (Mouse; PMID:34877938), clade: mammal
    - linked to: Neuroinflammation
- **Microglial P2rx7 and Il6 and astrocytic Il6ra knockdown mice under chronic social defeat stress** (Mouse; PMID:39888279), clade: mammal
    - linked to: Neuroinflammation

Non-animal experimental models already curated: none. This entry has no `experimental_models` block, so organoid, organ-chip, slice and iPSC systems are an open field rather than a duplicate.

Do not restate, re-justify or re-report these. Do not report that the existing models cluster in
some taxon or system — that is the premise of the question, not a finding.

## The Mechanism Nodes To Map Against

Any model you propose must be mapped to one or more of these nodes **by name**, exactly as
written. The right-hand column says whether any curated model is already linked to that node; a
node marked **no** is where an alternative model has the most to add, and several such nodes are
usually the point of the exercise.

| # | Node | Scale | Already modelled |
|---|---|---|---|
| 1 | Monoamine Deficiency | TISSUE | yes |
| 2 | Excitation-Inhibition Imbalance | **not stated** | **no** |
| 3 | HPA Axis Dysregulation | **not stated** | **no** |
| 4 | Neuroplasticity Deficits | **not stated** | **no** |
| 5 | Neuroinflammation | **not stated** | yes |
| 6 | Mitochondrial Dysfunction | **not stated** | **no** |
| 7 | Reference Point Dysregulation | **not stated** | yes |
| 8 | Oligodendrocyte Dysfunction and Demyelination | **not stated** | **no** |
| 9 | Stalled Adult Hippocampal Neurogenesis | CELLULAR | **no** |
| 10 | Neurogenic Niche Interferon Signaling Activation | MOLECULAR | **no** |
| 11 | Stress-Responsive Transcription Factor Reprogramming | MOLECULAR | **no** |
| 12 | PENK+ GABAergic Interneuron Activation | CELLULAR | **no** |

Nodes of greatest interest for this run:

- PENK+ GABAergic Interneuron Activation
- Neurogenic Niche Interferon Signaling Activation
- Stress-Responsive Transcription Factor Reprogramming
- Oligodendrocyte Dysfunction and Demyelination
- Neuroinflammation

Of these, only Neuroinflammation currently has any model linked to it. The other four have
none, so for them any defensible candidate is an addition rather than a competitor.

Where a node's scale is shown as **not stated**, treat the node's own description as the
authority on what level of organisation it sits at, and say in your answer which level you took
it to be.

## The Substitution Problem — Address It Directly, Do Not Evade It

A model is only useful here if it can host the mechanism the node describes. State plainly, for
every candidate, what the model cannot carry.

Three of the five focus nodes were defined from human post-mortem hippocampus — single-nucleus
transcriptomics and chromatin accessibility — rather than from an animal experiment. The PENK+
GABAergic population is described as not previously reported in the human hippocampus. So the
substitution question here is not whether another taxon shares a mammalian structure, but
whether any model system can host a mechanism first observed in human tissue.

For each candidate, state specifically:

- Whether the cell population or regulatory module in question **exists** in that system. For
  the PENK+ node, say whether a homologous population has been identified there at all, and on
  what evidence. A model that lacks the cell type cannot recapitulate the node.
- Whether the transcription factors named in the node (KLF9, KLF15, EGR1 and relatives) have
  orthologs with conserved glucocorticoid or stress responsiveness in that system.
- For interferon signalling, whether the type I interferon pathway is conserved and whether the
  neurogenic niche itself exists — adult hippocampal neurogenesis is contested in humans and
  absent or very different in several candidate systems, which constrains the node directly.
- For oligodendrocyte and myelin nodes, whether the system myelinates at all. Several otherwise
  attractive invertebrate systems do not.
- Whether the readout is the human-defined molecular signature or a behavioural proxy. A
  despair-like behavioural assay is not evidence about a transcriptional module, and conflating
  the two is the most common failure in this literature.

Therefore, for **every** model you propose, state which of these it is:

- **(a) Recapitulates** the node: the same lesion in the same kind of system, or through a
  conserved mechanism that has been shown to operate there.
- **(b) Perturbs** the node: the manipulation acts on the molecular or cellular step the node
  names, without reproducing the node's full outcome.
- **(c) Informative by analogy only**: the model speaks to the biology, but the node's defining
  feature is absent from that system. Say exactly what is absent.
- **(d) Fails to recapitulate**: the model has been tested against this biology and does not
  reproduce it. A documented negative is a valuable result — report it as one.

Classification (c) is an honest answer and is preferred over stretching a model into (a). A short
report that correctly rules most candidates out is more useful than a long one that overstates
their fit.

## Systems To Cover

Cover each of the following. Say explicitly where a system has nothing to offer — an empty system
is a useful result, not a gap in the report.

- **Human iPSC-derived systems.** iPSC-derived GABAergic interneurons, oligodendrocyte
  progenitors and myelinating co-cultures, microglia-like cells, astrocytes. Patient-derived
  lines from people with MDD, and glucocorticoid or cytokine challenge of them.
- **Brain organoids and assembloids.** Hippocampal or dorsal-forebrain organoids, organoids with
  integrated microglia, and any organoid work on interferon signalling or myelination. State
  whether the relevant cell type arises.
- **Human post-mortem and surgical tissue.** Slice and explant culture, and any system that
  allows perturbation of human hippocampal tissue rather than observation only.
- **Organ-chips and engineered systems.** Blood-brain-barrier and neuroinflammation chips,
  especially any that model cytokine entry or microglial activation.
- **Non-mammalian vertebrates.** Zebrafish for microglial neuroinflammation, myelin and
  oligodendrocyte biology (where it is a strong genetic model), type I interferon signalling,
  cortisol stress-axis manipulation, and adult neurogenesis, which is extensive in teleosts.
  Medaka and Xenopus where relevant.
- **Invertebrates beyond the curated C. elegans models.** Drosophila stress, sleep and glial
  models; state explicitly where the absence of myelin or of a given cell type rules a node out.
- **Other mammals not already curated.** Rat chronic unpredictable stress, tree shrew, non-human
  primate chronic social stress, and the cuprizone and lysolecithin demyelination models, which
  are mammalian but are not curated on this entry.
- **Human experimental and iatrogenic models.** Interferon-alpha therapy as an induced model of
  inflammation-associated depression, and endotoxin or vaccine challenge studies in volunteers.
  These are human and not animal models; say which block they would belong in, if any.
- **Opioid peptide systems for the PENK node.** Proenkephalin and enkephalin manipulation in any
  system, and whether a PENK-expressing medium-spiny-neuron-like population has been described
  outside human hippocampus.
- **Glucocorticoid-responsive transcription factor systems.** KLF9, KLF15 and EGR1 reporter and
  knockout systems in any model, including in vitro, and whether their stress responsiveness is
  conserved.

## Output Required Per Candidate Model

- The system: species with scientific name where it is an organism, or the platform (organoid,
  organ-chip, iPSC-derived culture, slice, explant, cell line, in silico) where it is not
- Category: genetic model, controlled exposure or perturbation model, observational study, or
  engineered in vitro system
- A short description of what the model is and what it shows
- The pathograph node or nodes it maps to, named exactly as listed above
- Its classification as (a), (b), (c) or (d), with the reason
- Whether it would be curated as an `AnimalModel` (a whole organism) or an `ExperimentalModel`
  (organoid, organ-chip, cell line, iPSC-derived or primary culture) — these are separate blocks
  in the schema and a model proposed for the wrong one creates work
- The primary publication as a **PMID**
- At least one **exact verbatim quote** from the abstract or text supporting the key claim, with
  the article's exact title. Quotes are machine-validated against the source after this report is
  returned: a paraphrase presented as a quote, or a PMID that does not resolve, is a hard failure
- What the model does **not** show, and the limitation that constrains it

## Evidence Discipline

- Every PMID must resolve and must be the paper you mean. Give its exact title.
- Never present a paraphrase as a quote.
- Do not claim a model or a finding does not exist on the strength of an unsuccessful search. Say
  what you searched and what you found.
- Where a mechanism is genuinely not conserved in, or reproducible by, a candidate system, say so
  plainly rather than qualifying it into apparent usefulness.
- Distinguish an observational or correlational finding from a controlled manipulation, and say
  which any given citation is.


## Output

# Alternative Model Systems for the Major Depressive Disorder Pathograph

**Disease:** Major Depressive Disorder (MONDO:0002009)
**Brief:** Identify model systems — beyond the six already curated — that could legitimately
support specific, named pathograph nodes, and classify each by whether it recapitulates,
perturbs, is informative by analogy only, or fails to recapitulate the node it is mapped to.

---

## Summary

Beyond the six curated *C. elegans* and mouse models, a large field of uncurated systems can
legitimately support MDD pathograph nodes — but their value is sharply **stratified by node**,
and the most interesting focus nodes are precisely the ones that resist substitution. The
strongest, cleanest additions are for the **Oligodendrocyte Dysfunction and Demyelination** node
(cuprizone and lysolecithin mice, genetically tractable larval and `mbp:NTR` zebrafish, and human
iPSC myelinating co-cultures) and for the **Neuroinflammation** node (human iPSC microglia,
microglia-containing cerebral organoids, BBB-on-chip and neurovascular-unit platforms, adult
chronic-stress zebrafish, and human IFN-α therapy / LPS endotoxin challenge). For **HPA Axis
Dysregulation** the zebrafish glucocorticoid-receptor mutant and GRE reporter line, the tree
shrew, and the cynomolgus monkey are all defensible, uncurated candidates. For **Stress-Responsive
Transcription Factor Reprogramming**, the glucocorticoid-responsiveness of KLF9, KLF15 and EGR1 is
conserved all the way to *Xenopus* and reproducible in rodent and in-vitro reporter systems, so
these systems can *perturb* the transcriptional step the node names.

The three focus nodes that were defined from **human post-mortem hippocampus** — PENK+ GABAergic
Interneuron Activation, Neurogenic Niche Interferon Signaling Activation, and the transcription-
factor reprogramming module — behave very differently under substitution. Here the question is not
whether another taxon shares a mammalian structure, but whether any model can host a mechanism
first *observed in human tissue*. For these, most candidate systems are honestly classified as
**(b) perturbs** (they reproduce a molecular or cellular step) or **(c) informative by analogy
only** (the defining feature is absent). In particular, **the PENK+ GABAergic hippocampal
interneuron node has no model that recapitulates it**: an enkephalinergic GABAergic cell type
exists in mammalian neocortex and as striatal medium spiny neurons, but the specific hippocampal
population the node names — described as not previously reported in the human hippocampus — has not
been identified in any model system.

The honest bottom line: **a short report that correctly rules candidates out is more useful than a
long one that overstates them.** Drosophila and additional *C. elegans* models are empty for all
five focus nodes (they do not myelinate and lack the relevant cell types); teleost adult
neurogenesis is the opposite of the "stalled human" phenotype and so is analogy-only for the
neurogenesis node; and the PENK+ hippocampal interneuron remains genuinely unsubstitutable. The
strongest non-mouse additions cluster where the biology is evolutionarily conserved (myelin,
type I interferon, the glucocorticoid axis, KLF/EGR transcription factors) and the human-defined
single-nucleus modules remain only partially addressable.

---

## Key Findings

### Finding 1 — HPA Axis Dysregulation: the zebrafish glucocorticoid-receptor mutant is a strong, uncurated AnimalModel

The glucocorticoid-receptor (`gr`) loss-of-function zebrafish (*Danio rerio*) generated by Ziv et
al. is an adult-viable mutant in which negative feedback on the stress response is abolished:
cortisol is elevated but cannot signal through GR, producing freezing, reduced exploration and
failure to habituate — behaviours reversed by fluoxetine. Teleosts possess a conserved
hypothalamic–pituitary–interrenal (HPI) cortisol axis and a GR orthologue, so this model
**(a) recapitulates** the HPA Axis Dysregulation node at the level of disrupted glucocorticoid
feedback. A companion transgenic GRE-reporter line (SR4G) provides single-cell GR-activity readout
throughout the brain, enabling mechanistic perturbation rather than observation alone.

This would be curated as an **AnimalModel**. Its limitation is important and must be stated
plainly: fish use cortisol via an interrenal (HPI) axis rather than an adrenal HPA axis, lack a
laminated mammalian hippocampus, and the readout is behavioural/endocrine — **not** the human
single-nucleus RNA-seq transcriptional modules that define the hippocampus-derived focus nodes.
The model carries the stress-axis lesion but not the human hippocampal molecular signature.

> *"Dysregulation of the stress axis is a hallmark of major depression in human patients."* and
> *"We identified an adult-viable zebrafish mutant in which the negative feedback on the stress
> response is disrupted, due to abolition of all transcriptional activity of GR."*
> — *An affective disorder in zebrafish with mutation of the glucocorticoid receptor*,
> [PMID: 22641177](https://pubmed.ncbi.nlm.nih.gov/22641177/)

### Finding 2 — Stress-Responsive Transcription Factor Reprogramming: KLF9/KLF15/EGR1 are conserved, directly perturbable glucocorticoid targets

Node 11 (Stress-Responsive Transcription Factor Reprogramming, which I take to be a **MOLECULAR**
node per its description) names KLF9, KLF15, EGR1 and relatives. Multiple uncurated systems can
**(b) perturb** this node by reproducing the glucocorticoid → KLF/EGR transcriptional step:

- **Mouse hippocampus and the HT-22 hippocampal cell line** (Bagamasbad et al.): corticosterone
  directly induces *Klf9* via two GR/MR response elements, and the −5.3 kb GRE/MRE is largely
  conserved across tetrapods. The induction is protein-synthesis-independent, establishing KLF9 as
  a *direct* glucocorticoid-response gene. HT-22 would be an **ExperimentalModel**; the mouse an
  **AnimalModel**.
- **Rat hippocampus** (Kennedy et al.): genome-wide ChIP-seq maps KLF-family members as MR/GR
  targets after acute stress — an **AnimalModel**.
- **Xenopus tropicalis** GR-knockout tadpoles: corticosterone induction of *klf9* is completely
  abrogated, and the *Xenopus* XLK-WG cell line shows CORT-induced *klf9* via a synergy module
  whose AHRE cluster is positionally conserved in the human genome — **AnimalModel** (whole tadpole)
  and **ExperimentalModel** (XLK-WG line).
- **EGR1 systems**: in neuronal BZ cells and primary neurons, GR physically interacts with an EGR1
  response element to repress BDNF exon IV (linking node 11 to **Neuroplasticity Deficits**); in
  PC12 cells dexamethasone blunts IL-6-induced *Egr1*/*c-Fos*. Both **ExperimentalModels**.

The shared limitation: none reconstitutes the human hippocampal multi-cell module or the PENK+
interneuron context in which the module was defined, and the *Xenopus* readout is metamorphosis,
not mood.

> *"The CORT induction of Klf9 was resistant to protein synthesis inhibition, suggesting that Klf9
> is a direct CORT-response gene."* and *"The -5.3-kb GRE/MRE is largely conserved across
> tetrapods"* — *Molecular basis for glucocorticoid induction of the Kruppel-like factor 9 gene in
> hippocampal neurons*, [PMID: 22962255](https://pubmed.ncbi.nlm.nih.gov/22962255/)

> *"Induction by exogenous corticosterone (CORT, the frog stress hormone) of the CORT response
> genes, klf9 ... was completely abrogated in GRKO tadpoles."* — *Glucocorticoid receptor is
> required for survival through metamorphosis in the frog Xenopus tropicalis*,
> [PMID: 32032606](https://pubmed.ncbi.nlm.nih.gov/32032606/)

> *"both GR and EGR1 bind to this promoter sequence in a glucocorticoid-dependent manner"* —
> *Crosstalk Between Glucocorticoid Receptor and Early-growth Response Protein 1 Accounts for
> Repression of Brain-derived Neurotrophic Factor Transcript 4 Expression*,
> [PMID: 30578973](https://pubmed.ncbi.nlm.nih.gov/30578973/)

### Finding 3 — Oligodendrocyte Dysfunction and Demyelination: three complementary uncurated models, with invertebrates ruled out

This node (which I take to be **CELLULAR/TISSUE** level per its description) has the richest set of
defensible, uncurated additions:

1. **Cuprizone mouse** (**AnimalModel**): the copper chelator causes corpus-callosum
   demyelination accompanied by anxiety- and depression-like behaviour. Classification
   **(a) recapitulates** the demyelination lesion — but the readout couples a behavioural proxy to
   myelin loss, which must not be conflated with the human transcriptional signature.
2. **Larval zebrafish** (**AnimalModel**): genetically tractable, live-imageable CNS myelination;
   the `Tg(mbp:mCherry-NTR)` line enables inducible, reversible demyelination/remyelination.
   Classification **(a) recapitulates** oligodendrocyte biology at single-cell resolution.
3. **Human iPSC neuron–oligodendrocyte co-culture** (**ExperimentalModel**): human O4+
   oligodendrocytes myelinate axons in vitro. Classification **(b) perturbs / recapitulates**
   human myelination but lacks the in-vivo stress/HPA context.

Critically, **invertebrates (Drosophila, C. elegans) are ruled out for this node** — they do not
myelinate, so no manipulation in them can host the mechanism. This is a clean negative and a useful
result. A lysolecithin/LPC focal demyelination mouse is a further mammalian **AnimalModel** not
curated on this entry.

> *"As a model organism, larval zebrafish have been extensively employed to investigate the
> molecular and cellular basis of CNS myelination, because of their genetic tractability and
> suitability for non-invasive live cell imaging."* — *CNS Hypomyelination Disrupts Axonal
> Conduction and Behavior in Larval Zebrafish*,
> [PMID: 34544838](https://pubmed.ncbi.nlm.nih.gov/34544838/)

> *"Neurons form synaptic connections and transmit signals, while oligodendrocytes, including
> oligodendrocyte precursor cells (OPCs) and their derivatives, are vital for central nervous
> system maintenance and myelination."* — *Human iPSC-Derived Neuron and Oligodendrocyte
> Co-culture as a Small-Molecule Screening Assay for Myelination*,
> [PMID: 40364981](https://pubmed.ncbi.nlm.nih.gov/40364981/)

### Finding 4 — Neurogenic Niche Interferon Signaling + Stalled Adult Hippocampal Neurogenesis: mechanistically hostable, but the niche is human-hippocampus-defined

Node 10 (Neurogenic Niche Interferon Signaling Activation, **MOLECULAR**) and node 9 (Stalled Adult
Hippocampal Neurogenesis, **CELLULAR**) have no curated model. The candidates split cleanly:

- **Mouse adult neural stem cells**: primed quiescent NSCs carry an intrinsic interferon-response
  signature, and aging niche-derived inflammatory signals impose quiescence. These show the type I
  interferon pathway operating in the mammalian neurogenic niche to restrain neurogenesis —
  classification **(b) perturbs** node 10 and **(a) recapitulates** the stalled-neurogenesis
  phenotype — but in the SVZ rather than the human hippocampal niche defined by snRNA-seq. Curated
  as **AnimalModel** / primary culture.
- **Teleost fish (zebrafish, killifish)**: constitutive adult neurogenesis across many niches —
  classification **(c) informative by analogy only** for node 9. Fish have no hippocampus (they use
  pallium) and robust lifelong neurogenesis, the *opposite* of the contested, low-rate human
  hippocampal phenotype, so they cannot reproduce the "stalled human" condition. However, type I
  interferon is vertebrate-conserved in teleosts (confirmed in zebrafish via FTR33 regulation of
  type I IFN/ISGs), so fish can host node 10 *mechanistically* but not in a hippocampal context.

> *"Primed quiescent NSCs (p-qNSCs) are defined by high levels of LRIG1 and CD9, as well as an
> interferon response signature"* — *LRIG1 is a gatekeeper to exit from quiescence in adult neural
> stem cells*, [PMID: 33972529](https://pubmed.ncbi.nlm.nih.gov/33972529/)

> *"zebrafish exhibit constitutive neurogenesis across multiple stem cell niches that provide new
> neurons to every major brain division"* — *The role of neuro-epithelial-like and radial-glial
> stem and progenitor cells in development, plasticity, and repair*,
> [PMID: 29902500](https://pubmed.ncbi.nlm.nih.gov/29902500/)

### Finding 5 — PENK+ GABAergic Interneuron Activation: no model recapitulates; homologous cell types exist but not the hippocampal population

Node 12 (**CELLULAR**) describes a PENK+ GABAergic interneuron population explicitly "not
previously reported in the human hippocampus." Searching for proenkephalin/enkephalin GABAergic
hippocampal populations, I found that enkephalinergic GABAergic interneurons are well documented in
rodent **neocortex** (a VIP+/enkephalin+ mu-opioid-sensitive interneuron class; preproenkephalin-
immunoreactive GABAergic cortical interneurons) and as **striatal medium spiny neurons** (a
GABAergic projection-neuron population expressing proenkephalin). These establish that a homologous
PENK+/GABAergic cell *type* exists in mammals — but in neocortex and striatum, not the hippocampal
interneuron population the node names.

Human iPSC-derived MGE/LHX6+ GABAergic interneurons (**ExperimentalModel**) can generate diverse
neuropeptide+ interneuron subtypes but no study has demonstrated the specific hippocampal PENK+
population. **Classification (c) informative by analogy only**: the enkephalinergic GABAergic
module exists and can be perturbed (opioid/enkephalin manipulation), but the node's defining
hippocampal population has not been identified in any model system. This is the single node where
no candidate reaches **(a)**, and that is the honest answer.

> *"mu-opioid receptor-immunoreactive neurons very frequently exhibited preproenkephalin
> immunoreactivity"* — *A group of cortical interneurons expressing mu-opioid receptor-like
> immunoreactivity: a double immunofluorescence study in the rat cerebral cortex*,
> [PMID: 10854753](https://pubmed.ncbi.nlm.nih.gov/10854753/)

> *"layers II-V cells expressing vasoactive intestinal peptide and enkephalin (Enk)"* —
> *Extensive overlap of mu-opioid and nicotinic sensitivity in cortical interneurons*,
> [PMID: 17068095](https://pubmed.ncbi.nlm.nih.gov/17068095/)

> *"In the neostriatum, the proenkephalin gene is expressed in medium spiny GABA neurons, which
> project to the globus pallidus."* — *Intrinsic GABA neurons inhibit proenkephalin gene expression
> in slice cultures of rat neostriatum*,
> [PMID: 11982623](https://pubmed.ncbi.nlm.nih.gov/11982623/)

### Finding 6 — Neuroinflammation: human iPSC microglia, microglia-in-organoids, BBB-chips, and human IFN-α/LPS challenge add non-mouse models

The Neuroinflammation node is curated only with mouse models. Uncurated additions span three
schema situations:

- **Human iPSC-derived microglia-like cells** (**ExperimentalModel**): mount stimulus-specific
  inflammatory responses to TNF-α, IFN-γ, LPS and Poly(I:C) — **(a) recapitulates** human
  microglial activation. Type-I-interferon signalling drives microglial dysfunction/senescence in
  iPSC models, directly bridging to node 10.
- **Microglia-containing cerebral organoids** (**ExperimentalModel**): respond to inflammatory
  stimuli including IFN-γ — **(a/b)**, the relevant immune cell type is present and arises.
- **Human BBB-on-chip / neurovascular-unit chips** (**ExperimentalModel**): model cytokine
  (TNF-α/LPS)-driven barrier disruption and immune-cell migration — **(b) perturbs** the
  cytokine-entry/BBB step.
- **Human IFN-α therapy** (for hepatitis C) and **low-dose LPS endotoxin challenge** in volunteers:
  these are **human experimental/iatrogenic models**, not animal or in-vitro models. They would
  *not* fit the AnimalModel block, and as controlled-exposure/observational human data they do not
  map onto either the AnimalModel or ExperimentalModel block cleanly — they are human induced
  models of inflammation-associated depression.
- **Adult zebrafish chronic unpredictable stress** (**AnimalModel**): couples depression-like
  behaviour to microglial/astroglial neuroinflammation markers, cortisol and serotonin turnover —
  a non-mouse addition for this node and for HPA Axis Dysregulation.

> *"MGLCs displayed distinct morphologies and produced stimulus- and time-dependent cytokine
> secretion profiles upon exposure to diverse inflammatory stimuli, including pro-inflammatory
> cytokines (TNFα, interferon-γ) and agonists of the Toll-like receptors"* — *Differential
> Responses of Human iPSC-Derived Microglia to Stimulation with Diverse Inflammogens*,
> [PMID: 41227333](https://pubmed.ncbi.nlm.nih.gov/41227333/)

> *"Cytokine treatment with Interferon-alpha (IFN-α) represents a clinical model of immune
> associated depression"* — *Influence of gender on cytokine induced depression and treatment*,
> [PMID: 34171555](https://pubmed.ncbi.nlm.nih.gov/34171555/)

### Finding 7 — Patient-derived and defined-genetic human in-vitro systems close the non-focus-node gaps (E-I imbalance, mitochondrial, neuroplasticity)

Several uncurated human in-vitro systems address nodes that had no models:

- **Patient-derived SSRI-resistant MDD iPSC serotonergic neurons** (**ExperimentalModel**): show
  altered neurite growth/morphology downstream of lowered Protocadherin alpha genes — maps to
  **Neuroplasticity Deficits** (and Monoamine Deficiency); **(a)** for a human patient-derived MDD
  readout.
- **DISC1-mutant iPSC glutamatergic/GABAergic co-cultures** (**ExperimentalModel**): show aberrant
  GABAergic synapse densities — maps to **Excitation-Inhibition Imbalance** (node 2, scale **not
  stated**; I take it to be CELLULAR/circuit level); **(b)**.
- **TSPO-knockout hiPSC neurons/NPCs/astrocytes** (**ExperimentalModel**): reduced mitochondrial
  respiration and glycolysis — maps to **Mitochondrial Dysfunction** (node 6); **(b)**.
- **Perturbable adult human organotypic slice cultures** and **fetal human organotypic cortical
  cultures with shRNA knockdown** (**ExperimentalModel**): fill the previously empty human
  post-mortem/surgical-tissue category and allow genetic perturbation of human tissue affecting
  E-I / circuit function.

> *"NR patient-derived serotonergic neurons exhibited altered neurite growth and morphology
> downstream of lowered expression of key Protocadherin alpha genes as compared to healthy controls
> and Rs."* — *Altered serotonergic circuitry in SSRI-resistant major depressive disorder
> patient-derived neurons*, [PMID: 30903001](https://pubmed.ncbi.nlm.nih.gov/30903001/)

> *"Human organotypic slice cultures provide experimental access to adult human neuronal circuits
> ex vivo"* — *Adaptive Network Stabilization Despite Profound Structural Reorganization in Human
> Organotypic Cultures*, [PMID: 42750245](https://pubmed.ncbi.nlm.nih.gov/42750245/)

> *"STXBP1 knockdown disrupted spontaneous subplate neuronal network activity observed by calcium
> imaging at 14 days in vitro, reducing signal amplitude and synchronicity, indicating impaired
> early circuit function."* — *Human brain slice culture model of STXBP1 encephalopathy reveals
> disruption of neuronal network activity and changes in gene expression*,
> [PMID: 42214744](https://pubmed.ncbi.nlm.nih.gov/42214744/)

---

## Candidate Model Inventory (consolidated)

The table below consolidates every proposed candidate with its node mapping, classification, schema
block, primary PMID, and the key limitation that constrains it.

| System (species / platform) | Category | Node(s) mapped | Class | Schema block | PMID |
|---|---|---|---|---|---|
| *Danio rerio* `gr` mutant + SR4G GRE reporter | Genetic | HPA Axis Dysregulation | (a) | AnimalModel | [22641177](https://pubmed.ncbi.nlm.nih.gov/22641177/), [24679220](https://pubmed.ncbi.nlm.nih.gov/24679220/) |
| Mouse HT-22 line / mouse hippocampus (CORT→Klf9) | Perturbation | Stress-Responsive TF Reprogramming | (b) | ExperimentalModel / AnimalModel | [22962255](https://pubmed.ncbi.nlm.nih.gov/22962255/) |
| Rat hippocampus MR/GR ChIP-seq (KLFs) | Perturbation | Stress-Responsive TF Reprogramming | (b) | AnimalModel | [36942087](https://pubmed.ncbi.nlm.nih.gov/36942087/) |
| *Xenopus tropicalis* GR-KO tadpole; XLK-WG line | Genetic / Perturbation | Stress-Responsive TF Reprogramming | (b) | AnimalModel / ExperimentalModel | [32032606](https://pubmed.ncbi.nlm.nih.gov/32032606/), [35172007](https://pubmed.ncbi.nlm.nih.gov/35172007/) |
| BZ cells / PC12 (GR–EGR1, Egr1/c-Fos) | Perturbation | Stress-Responsive TF Reprogramming; Neuroplasticity | (b) | ExperimentalModel | [30578973](https://pubmed.ncbi.nlm.nih.gov/30578973/), [33454999](https://pubmed.ncbi.nlm.nih.gov/33454999/) |
| Cuprizone mouse | Controlled exposure | Oligodendrocyte Dysfunction & Demyelination | (a) | AnimalModel | [38394854](https://pubmed.ncbi.nlm.nih.gov/38394854/) |
| Larval zebrafish; `mbp:NTR` ablation line | Genetic | Oligodendrocyte Dysfunction & Demyelination | (a) | AnimalModel | [34544838](https://pubmed.ncbi.nlm.nih.gov/34544838/), [30820902](https://pubmed.ncbi.nlm.nih.gov/30820902/) |
| Human iPSC neuron–oligodendrocyte co-culture | Engineered in vitro | Oligodendrocyte Dysfunction & Demyelination | (b) | ExperimentalModel | [40364981](https://pubmed.ncbi.nlm.nih.gov/40364981/) |
| Mouse adult NSCs (IFN-response, quiescence) | Observational / Perturbation | Neurogenic Niche IFN Signaling; Stalled Neurogenesis | (b)/(a) | AnimalModel / primary culture | [33972529](https://pubmed.ncbi.nlm.nih.gov/33972529/), [30827680](https://pubmed.ncbi.nlm.nih.gov/30827680/) |
| Teleost (zebrafish/killifish) adult neurogenesis | Observational | Stalled Adult Hippocampal Neurogenesis | (c) | AnimalModel | [29902500](https://pubmed.ncbi.nlm.nih.gov/29902500/) |
| Zebrafish type I IFN (FTR33/ISGs) | Genetic | Neurogenic Niche IFN Signaling | (b) | AnimalModel | [36801427](https://pubmed.ncbi.nlm.nih.gov/36801427/) |
| Rodent neocortical enkephalin+ GABAergic interneurons | Observational | PENK+ GABAergic Interneuron Activation | (c) | AnimalModel / ex-vivo | [10854753](https://pubmed.ncbi.nlm.nih.gov/10854753/), [17068095](https://pubmed.ncbi.nlm.nih.gov/17068095/) |
| Rat striatal MSN slice culture (PENK+ GABA) | Engineered in vitro | PENK+ GABAergic Interneuron Activation | (c) | ExperimentalModel | [11982623](https://pubmed.ncbi.nlm.nih.gov/11982623/) |
| iPSC MGE/LHX6+ GABAergic interneurons | Engineered in vitro | PENK+ GABAergic Interneuron Activation | (c) | ExperimentalModel | [35269475](https://pubmed.ncbi.nlm.nih.gov/35269475/), [30559206](https://pubmed.ncbi.nlm.nih.gov/30559206/) |
| Human iPSC microglia-like cells | Engineered in vitro | Neuroinflammation; Neurogenic Niche IFN | (a) | ExperimentalModel | [41227333](https://pubmed.ncbi.nlm.nih.gov/41227333/), [35803230](https://pubmed.ncbi.nlm.nih.gov/35803230/) |
| Microglia-containing cerebral organoids | Engineered in vitro | Neuroinflammation | (a/b) | ExperimentalModel | [39500415](https://pubmed.ncbi.nlm.nih.gov/39500415/) |
| Human BBB-on-chip / neurovascular-unit chip | Engineered in vitro | Neuroinflammation | (b) | ExperimentalModel | [37818458](https://pubmed.ncbi.nlm.nih.gov/37818458/), [42053998](https://pubmed.ncbi.nlm.nih.gov/42053998/) |
| Human IFN-α therapy | Controlled exposure (human) | Neuroinflammation | (a) | neither (human induced) | [34171555](https://pubmed.ncbi.nlm.nih.gov/34171555/) |
| Human LPS endotoxin challenge | Controlled exposure (human) | Neuroinflammation | (b) | neither (human induced) | [34673176](https://pubmed.ncbi.nlm.nih.gov/34673176/) |
| Adult zebrafish chronic unpredictable stress | Controlled exposure | Neuroinflammation; HPA Axis | (a/b) | AnimalModel | [40220038](https://pubmed.ncbi.nlm.nih.gov/40220038/) |
| Patient-derived SSRI-resistant MDD iPSC 5-HT neurons | Observational (patient) | Neuroplasticity Deficits; Monoamine Deficiency | (a) | ExperimentalModel | [30903001](https://pubmed.ncbi.nlm.nih.gov/30903001/) |
| DISC1-mutant iPSC glutamatergic/GABAergic co-culture | Genetic | Excitation-Inhibition Imbalance | (b) | ExperimentalModel | [38438989](https://pubmed.ncbi.nlm.nih.gov/38438989/) |
| TSPO-KO hiPSC neurons/NPCs/astrocytes | Genetic | Mitochondrial Dysfunction | (b) | ExperimentalModel | [39684592](https://pubmed.ncbi.nlm.nih.gov/39684592/) |
| Adult human organotypic slice culture | Engineered in vitro | Excitation-Inhibition Imbalance; Neuroplasticity | (b/c) | ExperimentalModel | [42750245](https://pubmed.ncbi.nlm.nih.gov/42750245/) |
| Fetal human organotypic cortical culture + shRNA | Engineered in vitro | Excitation-Inhibition Imbalance | (b) | ExperimentalModel | [42214744](https://pubmed.ncbi.nlm.nih.gov/42214744/) |
| Tree shrew chronic psychosocial stress | Controlled exposure | HPA Axis Dysregulation | (a) | AnimalModel | [15744220](https://pubmed.ncbi.nlm.nih.gov/15744220/) |
| Cynomolgus monkey natural/social-defeat depression | Observational | HPA Axis Dysregulation | (a/c) | AnimalModel | [41102858](https://pubmed.ncbi.nlm.nih.gov/41102858/) |

**Empty systems (useful negatives):** *Drosophila* and additional *C. elegans* models return
nothing for all five focus nodes — they do not myelinate (ruling out the oligodendrocyte node) and
lack the relevant GABAergic hippocampal interneuron and adult-hippocampal-neurogenesis biology.
Repeated literature searches for Drosophila myelin/glia models and for human hippocampal organoids
reproducing the PENK+ population returned no supporting papers; these are reported as search-limited
gaps, not proven absences.

---

## Mechanistic Model / Interpretation

The central interpretive problem is the **substitution gap** between evolutionarily conserved
biology and human-tissue-defined modules. The candidate landscape sorts into three tiers:

```
 TIER 1 — CONSERVED MECHANISM, STRONG SUBSTITUTION  (class a / strong b)
 ┌─────────────────────────────────────────────────────────────────────┐
 │  Myelin biology ........ cuprizone mouse, larval zebrafish, iPSC OL   │
 │  Glucocorticoid axis ... zebrafish gr mutant, tree shrew, primate     │
 │  KLF9/KLF15/EGR1 TFs .... mouse/rat/Xenopus/HT-22/PC12 reporters       │
 │  Microglial activation .. iPSC microglia, microglia-organoids, chips  │
 │  Type I interferon ...... zebrafish (FTR33), iPSC microglia           │
 └─────────────────────────────────────────────────────────────────────┘
          │ conserved pathway operates in the model system
          ▼
 TIER 2 — PERTURB THE STEP, NOT THE HUMAN MODULE  (class b)
 ┌─────────────────────────────────────────────────────────────────────┐
 │  Mitochondrial (TSPO-KO iPSC); E-I (DISC1 iPSC); human slices         │
 │  Neurogenic niche IFN in mouse SVZ (not human hippocampus)            │
 └─────────────────────────────────────────────────────────────────────┘
          │ molecular/cellular step reproduced; full node outcome not
          ▼
 TIER 3 — ANALOGY ONLY / UNSUBSTITUTABLE  (class c)
 ┌─────────────────────────────────────────────────────────────────────┐
 │  PENK+ hippocampal interneuron .. cell type absent from all models   │
 │  Stalled human neurogenesis ..... teleosts show the OPPOSITE         │
 └─────────────────────────────────────────────────────────────────────┘
```

The pattern is coherent: **where the node names a conserved molecule or pathway (myelin, cortisol/
GR, KLF/EGR, type I interferon, microglial cytokines), non-mouse and in-vitro systems substitute
well.** Where the node names a **human-tissue-defined cell population or niche state** (the PENK+
hippocampal interneuron; the stalled low-rate human hippocampal neurogenesis), substitution fails
or is analogy-only, because the defining feature either does not exist in the candidate (PENK+
hippocampal interneuron) or exists in an opposite form (teleost constitutive neurogenesis).

This is exactly what the brief predicted: three focus nodes were defined from human post-mortem
hippocampus by single-nucleus transcriptomics and chromatin accessibility, and the substitution
question for them is not taxonomic structure-sharing but whether any system can host a mechanism
first observed in human tissue. The answer is **partial** — the *molecular step* can be perturbed
in conserved systems, but the *integrated human module* cannot yet be reconstituted.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Study type |
|---|---|---|---|
| [22641177](https://pubmed.ncbi.nlm.nih.gov/22641177/) | *An affective disorder in zebrafish with mutation of the glucocorticoid receptor* | Supports zebrafish `gr` mutant → HPA node (a) | Controlled genetic manipulation |
| [22962255](https://pubmed.ncbi.nlm.nih.gov/22962255/) | *Molecular basis for glucocorticoid induction of Klf9...* | KLF9 direct, conserved GC target | Controlled in-vitro/in-vivo |
| [32032606](https://pubmed.ncbi.nlm.nih.gov/32032606/) | *Glucocorticoid receptor required for survival through metamorphosis...* | KLF9 GR-dependence conserved to Xenopus | Controlled genetic KO |
| [30578973](https://pubmed.ncbi.nlm.nih.gov/30578973/) | *Crosstalk Between GR and EGR1...BDNF Transcript 4* | Links EGR1 node to neuroplasticity | Controlled manipulation |
| [34544838](https://pubmed.ncbi.nlm.nih.gov/34544838/) | *CNS Hypomyelination...Larval Zebrafish* | Zebrafish myelin model (a) | Genetic / imaging |
| [40364981](https://pubmed.ncbi.nlm.nih.gov/40364981/) | *Human iPSC...Oligodendrocyte Co-culture...Myelination* | Human in-vitro myelination platform | Engineered in vitro |
| [33972529](https://pubmed.ncbi.nlm.nih.gov/33972529/) | *LRIG1 is a gatekeeper to exit from quiescence in adult NSCs* | IFN signature in neurogenic niche | Controlled / observational |
| [29902500](https://pubmed.ncbi.nlm.nih.gov/29902500/) | *Neuro-epithelial-like and radial-glial stem/progenitor cells...* | Teleost constitutive neurogenesis = analogy only | Review/observational |
| [10854753](https://pubmed.ncbi.nlm.nih.gov/10854753/) | *Cortical interneurons expressing mu-opioid...* | PENK+ GABA cell type in neocortex | Observational |
| [11982623](https://pubmed.ncbi.nlm.nih.gov/11982623/) | *Intrinsic GABA neurons inhibit proenkephalin...neostriatum* | PENK+ GABA MSN outside hippocampus | Controlled ex-vivo |
| [41227333](https://pubmed.ncbi.nlm.nih.gov/41227333/) | *Differential Responses of Human iPSC-Derived Microglia...* | Human microglia recapitulate inflammation | Controlled in vitro |
| [34171555](https://pubmed.ncbi.nlm.nih.gov/34171555/) | *Influence of gender on cytokine induced depression...* | IFN-α as human induced model | Observational (human) |
| [30903001](https://pubmed.ncbi.nlm.nih.gov/30903001/) | *Altered serotonergic circuitry in SSRI-resistant MDD...neurons* | Patient-derived iPSC neuroplasticity phenotype | Observational (patient) |
| [40220038](https://pubmed.ncbi.nlm.nih.gov/40220038/) | *Chronic stress...brain monoamines and affective behavior in zebrafish* | Non-mouse neuroinflammation/HPA model | Controlled exposure |
| [38438989](https://pubmed.ncbi.nlm.nih.gov/38438989/) | *DISC1 co-cultures reveal aberrant GABAergic phenotypes* | E-I imbalance in vitro | Controlled genetic |
| [39684592](https://pubmed.ncbi.nlm.nih.gov/39684592/) | *Human TSPO knockout neuronal model* | Mitochondrial node in vitro | Controlled genetic |
| [42214744](https://pubmed.ncbi.nlm.nih.gov/42214744/) | *Human brain slice culture model of STXBP1 encephalopathy* | Perturbable human tissue | Controlled genetic |

**Correlational vs. controlled:** The zebrafish `gr` mutant, Xenopus GR-KO, cuprizone exposure,
`mbp:NTR` ablation, DISC1 and TSPO knockouts, and STXBP1 knockdown are **controlled manipulations**.
The patient-derived iPSC serotonergic neuron phenotype, the cynomolgus natural-depression model,
the IFN-α therapy cohort and the neocortical/striatal PENK+ cell-type descriptions are
**observational/correlational** with respect to the MDD module.

---

## Limitations and Knowledge Gaps

1. **The PENK+ GABAergic hippocampal interneuron node is unsubstitutable.** No model recapitulates
   it. The homologous cell type exists in neocortex and striatum but the specific human hippocampal
   population has not been identified in any model, including human iPSC interneuron systems. This
   is the single most important negative result.

2. **Human-tissue-defined modules resist in-vitro reconstitution.** Conserved systems perturb the
   *molecular step* (KLF/EGR induction, type I interferon, microglial cytokines) but none
   reconstitutes the integrated human hippocampal multi-cell module or the chromatin-accessibility
   landscape from which nodes 10–12 were defined.

3. **Behavioural-proxy vs. molecular-signature conflation.** Several otherwise strong models
   (cuprizone mouse, chronic-stress zebrafish, tree shrew, cynomolgus) read out depression-like
   *behaviour*, which is not evidence about a transcriptional module. This distinction was enforced
   throughout but constrains how far these models can be claimed to "support" the human-defined
   focus nodes.

4. **Adult hippocampal neurogenesis is contested in humans and divergent across candidates.** Mouse
   NSC work is in the SVZ, not hippocampus; teleosts show the opposite (constitutive) phenotype. No
   model cleanly reproduces "stalled human hippocampal neurogenesis."

5. **Search-limited gaps, not proven absences.** Searches for Drosophila myelin/glia models and for
   human hippocampal organoids reproducing the PENK+ population returned no papers. These are
   reported as gaps in the available literature, not as demonstrated non-existence.

6. **Node-scale ambiguity.** Where node scales were stated as "not stated," I inferred the level
   from each node's description (E-I Imbalance → cellular/circuit; TF Reprogramming → molecular;
   Oligodendrocyte → cellular/tissue). Different scale assignments could change which models count
   as recapitulating.

---

## Proposed Follow-up Experiments / Actions

1. **Target the PENK+ hippocampal interneuron directly.** Perform single-nucleus RNA-seq on human
   hippocampal organoids/assembloids and on long-term human organotypic hippocampal slice cultures
   to test whether a PENK+ GABAergic interneuron population arises; this is the only path to moving
   node 12 from class (c) toward (b) or (a).

2. **Build a human iPSC "KLF9/KLF15/EGR1 glucocorticoid-reporter" line.** Combine GRE/KSM reporters
   with patient-derived MDD lines and glucocorticoid challenge to reconstitute the TF-reprogramming
   step in a human hippocampal-like context, bridging the conserved rodent/Xenopus evidence to the
   human module.

3. **Interferon challenge of microglia-containing hippocampal organoids.** Combine the
   microglia-in-organoid platform with type I interferon stimulation and neurogenic-niche readouts
   to test node 10 in a human neurogenic context rather than mouse SVZ.

4. **Couple a demyelination manipulation to transcriptional (not behavioural) readout.** Apply
   cuprizone/lysolecithin or `mbp:NTR` ablation and profile oligodendrocyte-lineage transcriptomes
   against the human hippocampal signature, decoupling the myelin lesion from the behavioural proxy.

5. **Curate the clear wins now.** The zebrafish `gr` mutant (AnimalModel → HPA), cuprizone mouse
   and larval zebrafish (AnimalModel → Oligodendrocyte), human iPSC microglia and microglia-organoids
   (ExperimentalModel → Neuroinflammation), and iPSC OL co-cultures (ExperimentalModel →
   Oligodendrocyte) are defensible additions that can be entered into the schema immediately, each
   with its stated limitation.

6. **Record the negatives.** Enter the Drosophila/*C. elegans* myelin exclusion and the
   PENK+ hippocampal-interneuron substitution failure as documented negative results, so future
   curation does not re-propose them.


## Artifacts

- [OpenScientist final report](Major_Depressive_Disorder-alternative-models-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Major_Depressive_Disorder-alternative-models-deep-research-openscientist_artifacts/final_report.pdf)