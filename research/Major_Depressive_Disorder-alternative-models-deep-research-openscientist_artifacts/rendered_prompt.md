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
