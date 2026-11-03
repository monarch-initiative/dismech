---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-03T15:01:59.751908'
end_time: '2026-11-03T15:19:23.690463'
duration_seconds: 1043.94
template_file: templates/disease_alternative_models_research.md
template_sha: "fd383b2d1a33daa300c57674e5947cf02e77e337"
template_variables:
  disease_name: Noonan Syndrome
  mondo_id: MONDO:0018997
  model_scope: 'Any model system bearing on the RAF1/RAS-MAPK cardiac hypertrophy
    axis that this entry does not already curate: knock-in and transgenic mice carrying
    Noonan-associated RAF1, PTPN11, RIT1, SOS1 or LZTR1 alleles; other vertebrate
    models including zebrafish; human myocardial tissue slices, explants and resected
    surgical tissue; engineered heart tissue and cardiac organ-chips; and iPSC-cardiomyocyte
    systems other than the one already curated. Treated human patients are in scope
    as evidence for the mechanism, but say clearly that a case report is clinical
    evidence rather than a model system, and name which schema block each candidate
    belongs in (animal_models, experimental_models, or treatment evidence).'
  nodes_of_interest: '- RAF1 Kinase Hyperactivation

    - ERK Cascade Hyperactivation

    - Cardiomyocyte Hypertrophy

    - Cardiac Valve Morphogenesis Defects


    Cardiomyocyte Hypertrophy and ERK Cascade Hyperactivation already carry one linked
    model,

    a patient-derived RAF1 S257L iPSC-cardiomyocyte system. For those two, a candidate
    is a

    competitor or a corroborator rather than first coverage, so say what it adds that
    the

    iPSC system cannot show. RAF1 Kinase Hyperactivation and Cardiac Valve Morphogenesis

    Defects carry no linked model at all.'
  substitution_constraint: 'Two constraints, and the second is the one this use case
    exists for.


    First, the ordinary substitution question: an iPSC-cardiomyocyte monolayer has
    no

    haemodynamic load, no fibroblast or endothelial compartment and an immature

    maturation state, while a whole mouse has all of them and a non-human genome.
    For each

    candidate, state which compartments and loads it carries, and which of the four
    nodes it

    can and cannot observe directly. Where a candidate reports a node it cannot observe

    directly, say so explicitly: that is an upward extrapolation and must be recorded
    as one.


    Second, MEK inhibition runs in both directions here and the two claims must not
    be

    conflated. In this disease MEK inhibition is proposed as a treatment that reverses

    hypertrophy. In the curated module mek_inhibition_cardiac_mitochondrial_injury,
    the same

    pharmacology is a cause of cardiomyocyte injury, through loss of ERK-dependent

    mitochondrial STAT3 serine-727 phosphorylation, respiratory chain failure and
    reversible

    hypocontractility. For every model or patient report in which a MEK inhibitor
    was given,

    state: what was measured, over what duration, whether contractile or mitochondrial

    function was assessed at all, and whether the result bears on the therapeutic
    claim, on

    the toxicity claim, or on both. Report any evidence that the therapeutic window
    depends on

    timing of initiation, dose, or the presence of a RAS-MAPK-activating variant.
    Do not

    assume the two directions are reconciled in the literature; if they are not, say
    so.'
  systems_to_cover: "Cover each of these and say explicitly where the literature is\
    \ empty rather than filling a\ngap with a plausible candidate:\n\n- Knock-in mouse\
    \ models of Noonan-associated RAF1 alleles, and what MEK inhibition did in\n \
    \ them, including any dependence on when treatment was started.\n- Human myocardial\
    \ tissue slices, explants or resected surgical tissue from Noonan\n  patients,\
    \ and any contractility or calcium-handling readout.\n- Engineered heart tissue,\
    \ cardiac organ-chips and other loaded three-dimensional systems.\n- Zebrafish\
    \ and other non-mammalian vertebrate models of the RAS-MAPK cardiac phenotype.\n\
    - Treated patients: compassionate-use and off-label MEK-inhibitor reports, at\
    \ any age,\n  with the outcome measured and the follow-up duration.\n- Any model\
    \ bearing on Cardiac Valve Morphogenesis Defects, which is developmental and may\n\
    \  need an embryonic rather than a postnatal system."
  existing_models: "Animal models already curated:\n\n- **Chick neural tube electroporation\
    \ of PTPN11 variants** (Chicken; PPR:PPR1278294), clade: bird\n    - linked to:\
    \ Neural Crest Cell Developmental Dysregulation\n- **RIT1 mutant Noonan syndrome\
    \ mouse model** (Mouse; no publication recorded), clade: mammal\n- **Lztr1G245R/+\
    \ and Lztr1R409C/+ knock-in** (Mouse; no publication recorded), clade: mammal\n\
    - **Noonan syndrome-causing SHP2 mutant mouse model** (Mouse; no publication recorded),\
    \ clade: mammal\n\nNon-animal experimental models already curated:\n\n- **Noonan\
    \ syndrome cortical organoid model** (ORGANOID)\n    - linked to: Cortical Layer\
    \ Development Abnormalities\n- **Noonan syndrome iPSC-cardiomyocyte model** (IPSC_DERIVED_MODEL)\n\
    \    - linked to: Cardiomyocyte Hypertrophy, ERK Cascade Hyperactivation"
  mechanism_nodes: '| # | Node | Scale | Already modelled |

    |---|---|---|---|

    | 1 | SHP2 Gain-of-Function Activation | **not stated** | yes (computational_models)
    |

    | 2 | SOS-Family-Mediated RAS-GTP Loading | **not stated** | yes (computational_models)
    |

    | 3 | RAF1 Kinase Hyperactivation | **not stated** | **no** |

    | 4 | RIT1-Mediated RAF Recruitment | **not stated** | yes (computational_models)
    |

    | 5 | LZTR1-Mediated RAS Proteostasis Defect | **not stated** | yes (computational_models)
    |

    | 6 | Additional RAS-MAPK Signal-Amplifying Variants | **not stated** | **no**
    |

    | 7 | ERK Cascade Hyperactivation | **not stated** | yes (experimental_models)
    |

    | 8 | Growth Plate Chondrocyte Differentiation Defect | **not stated** | **no**
    |

    | 9 | Cortical Layer Development Abnormalities | **not stated** | yes (experimental_models)
    |

    | 10 | Lymphatic Structural Abnormalities | **not stated** | **no** |

    | 11 | Hematologic Dysregulation | **not stated** | **no** |

    | 12 | Cardiac Valve Morphogenesis Defects | **not stated** | **no** |

    | 13 | Congenital Cardiac Structural Defects | **not stated** | **no** |

    | 14 | RASopathy Neoplastic Predisposition | **not stated** | **no** |

    | 15 | Cardiomyocyte Hypertrophy | **not stated** | yes (experimental_models)
    |

    | 16 | Neural Crest Cell Developmental Dysregulation | CELLULAR | yes (animal_models)
    |'
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
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:24875294
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Noonan_Syndrome-alternative-models-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Noonan_Syndrome-alternative-models-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Alternative Model Discovery Template

## Target Disease
- **Disease Name:** Noonan Syndrome
- **MONDO ID:** MONDO:0018997

## Scope — Read This First

This is **not** a request for a general account of this disease. Its pathophysiology and clinical
features are already curated. The single question is narrow:

> **Which model systems, beyond the ones already curated, could be used to study the mechanisms
> this disease's pathograph records — and which specific pathograph nodes could each one
> legitimately support?**

What counts as an alternative model for this run:

Any model system bearing on the RAF1/RAS-MAPK cardiac hypertrophy axis that this entry does not already curate: knock-in and transgenic mice carrying Noonan-associated RAF1, PTPN11, RIT1, SOS1 or LZTR1 alleles; other vertebrate models including zebrafish; human myocardial tissue slices, explants and resected surgical tissue; engineered heart tissue and cardiac organ-chips; and iPSC-cardiomyocyte systems other than the one already curated. Treated human patients are in scope as evidence for the mechanism, but say clearly that a case report is clinical evidence rather than a model system, and name which schema block each candidate belongs in (animal_models, experimental_models, or treatment evidence).

A report that returns models already listed below, or that proposes a model without naming the
pathograph node it serves, has failed this brief.

## What Is Already Curated — Do Not Re-Derive Any Of It

Animal models already curated:

- **Chick neural tube electroporation of PTPN11 variants** (Chicken; PPR:PPR1278294), clade: bird
    - linked to: Neural Crest Cell Developmental Dysregulation
- **RIT1 mutant Noonan syndrome mouse model** (Mouse; no publication recorded), clade: mammal
- **Lztr1G245R/+ and Lztr1R409C/+ knock-in** (Mouse; no publication recorded), clade: mammal
- **Noonan syndrome-causing SHP2 mutant mouse model** (Mouse; no publication recorded), clade: mammal

Non-animal experimental models already curated:

- **Noonan syndrome cortical organoid model** (ORGANOID)
    - linked to: Cortical Layer Development Abnormalities
- **Noonan syndrome iPSC-cardiomyocyte model** (IPSC_DERIVED_MODEL)
    - linked to: Cardiomyocyte Hypertrophy, ERK Cascade Hyperactivation

Do not restate, re-justify or re-report these. Do not report that the existing models cluster in
some taxon or system — that is the premise of the question, not a finding.

## The Mechanism Nodes To Map Against

Any model you propose must be mapped to one or more of these nodes **by name**, exactly as
written. The right-hand column says whether any curated model is already linked to that node; a
node marked **no** is where an alternative model has the most to add, and several such nodes are
usually the point of the exercise.

| # | Node | Scale | Already modelled |
|---|---|---|---|
| 1 | SHP2 Gain-of-Function Activation | **not stated** | yes (computational_models) |
| 2 | SOS-Family-Mediated RAS-GTP Loading | **not stated** | yes (computational_models) |
| 3 | RAF1 Kinase Hyperactivation | **not stated** | **no** |
| 4 | RIT1-Mediated RAF Recruitment | **not stated** | yes (computational_models) |
| 5 | LZTR1-Mediated RAS Proteostasis Defect | **not stated** | yes (computational_models) |
| 6 | Additional RAS-MAPK Signal-Amplifying Variants | **not stated** | **no** |
| 7 | ERK Cascade Hyperactivation | **not stated** | yes (experimental_models) |
| 8 | Growth Plate Chondrocyte Differentiation Defect | **not stated** | **no** |
| 9 | Cortical Layer Development Abnormalities | **not stated** | yes (experimental_models) |
| 10 | Lymphatic Structural Abnormalities | **not stated** | **no** |
| 11 | Hematologic Dysregulation | **not stated** | **no** |
| 12 | Cardiac Valve Morphogenesis Defects | **not stated** | **no** |
| 13 | Congenital Cardiac Structural Defects | **not stated** | **no** |
| 14 | RASopathy Neoplastic Predisposition | **not stated** | **no** |
| 15 | Cardiomyocyte Hypertrophy | **not stated** | yes (experimental_models) |
| 16 | Neural Crest Cell Developmental Dysregulation | CELLULAR | yes (animal_models) |

Nodes of greatest interest for this run:

- RAF1 Kinase Hyperactivation
- ERK Cascade Hyperactivation
- Cardiomyocyte Hypertrophy
- Cardiac Valve Morphogenesis Defects

Cardiomyocyte Hypertrophy and ERK Cascade Hyperactivation already carry one linked model,
a patient-derived RAF1 S257L iPSC-cardiomyocyte system. For those two, a candidate is a
competitor or a corroborator rather than first coverage, so say what it adds that the
iPSC system cannot show. RAF1 Kinase Hyperactivation and Cardiac Valve Morphogenesis
Defects carry no linked model at all.

Where a node's scale is shown as **not stated**, treat the node's own description as the
authority on what level of organisation it sits at, and say in your answer which level you took
it to be.

## The Substitution Problem — Address It Directly, Do Not Evade It

A model is only useful here if it can host the mechanism the node describes. State plainly, for
every candidate, what the model cannot carry.

Two constraints, and the second is the one this use case exists for.

First, the ordinary substitution question: an iPSC-cardiomyocyte monolayer has no
haemodynamic load, no fibroblast or endothelial compartment and an immature
maturation state, while a whole mouse has all of them and a non-human genome. For each
candidate, state which compartments and loads it carries, and which of the four nodes it
can and cannot observe directly. Where a candidate reports a node it cannot observe
directly, say so explicitly: that is an upward extrapolation and must be recorded as one.

Second, MEK inhibition runs in both directions here and the two claims must not be
conflated. In this disease MEK inhibition is proposed as a treatment that reverses
hypertrophy. In the curated module mek_inhibition_cardiac_mitochondrial_injury, the same
pharmacology is a cause of cardiomyocyte injury, through loss of ERK-dependent
mitochondrial STAT3 serine-727 phosphorylation, respiratory chain failure and reversible
hypocontractility. For every model or patient report in which a MEK inhibitor was given,
state: what was measured, over what duration, whether contractile or mitochondrial
function was assessed at all, and whether the result bears on the therapeutic claim, on
the toxicity claim, or on both. Report any evidence that the therapeutic window depends on
timing of initiation, dose, or the presence of a RAS-MAPK-activating variant. Do not
assume the two directions are reconciled in the literature; if they are not, say so.

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

Cover each of these and say explicitly where the literature is empty rather than filling a
gap with a plausible candidate:

- Knock-in mouse models of Noonan-associated RAF1 alleles, and what MEK inhibition did in
  them, including any dependence on when treatment was started.
- Human myocardial tissue slices, explants or resected surgical tissue from Noonan
  patients, and any contractility or calcium-handling readout.
- Engineered heart tissue, cardiac organ-chips and other loaded three-dimensional systems.
- Zebrafish and other non-mammalian vertebrate models of the RAS-MAPK cardiac phenotype.
- Treated patients: compassionate-use and off-label MEK-inhibitor reports, at any age,
  with the outcome measured and the follow-up duration.
- Any model bearing on Cardiac Valve Morphogenesis Defects, which is developmental and may
  need an embryonic rather than a postnatal system.

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

# Alternative Model Discovery — Noonan Syndrome (MONDO:0018997)

## Summary

This report answers a narrow question: beyond the model systems already curated for Noonan syndrome (NS), which *other* published models could study the mechanisms recorded in this disease's pathograph, and which specific pathograph nodes can each legitimately support? The investigation deliberately prioritised the four nodes flagged as most interesting — **RAF1 Kinase Hyperactivation**, **ERK Cascade Hyperactivation**, **Cardiomyocyte Hypertrophy** and **Cardiac Valve Morphogenesis Defects** — while also covering the lymphatic, hematologic, neoplastic, congenital-cardiac-structural and growth-plate nodes, and checking each of the required systems (RAF1 knock-in mice, human myocardial tissue, engineered heart tissue/organ-chips, zebrafish, treated patients, and embryonic valve models).

The headline result is that the **two priority nodes with no curated model can both be filled by existing, published, whole-organism mouse models**. **RAF1 Kinase Hyperactivation** (together with ERK Cascade Hyperactivation and Cardiomyocyte Hypertrophy) is recapitulated by the **Raf1(L613V) knock-in mouse** ([PMID 21339642](https://pubmed.ncbi.nlm.nih.gov/21339642/)), which also demonstrates postnatal, MEK-reversible hypertrophy — but is, critically, a *documented negative* (class d) for valve morphogenesis. **Cardiac Valve Morphogenesis Defects** is recapitulated by the embryonic **Tie2-Cre Q79R-Shp2 endocardial-cushion mouse** ([PMID 19017799](https://pubmed.ncbi.nlm.nih.gov/19017799/)), in which ERK1 deletion completely rescues the cushion phenotype, establishing ERK1-dependent causality. These two models are complementary: the first is postnatal and the second embryonic, which matches the developmental scale of the valve node.

Two further results constrain the brief. First, the **loaded human cardiac systems** the use case most wants — human Noonan myocardial slices/explants with contractility or calcium-handling readouts, and RASopathy engineered heart tissue / organ-chips / cardiac organoids — were **not found in the literature searched**. This is the genuinely missing model class: the Cardiomyocyte Hypertrophy node is currently bracketed by a human-but-unloaded monolayer and a loaded-but-murine whole animal, with nothing carrying a human genome, haemodynamic load and multicellular compartments together. Second, the **two directions of MEK inhibition remain unreconciled**: every therapeutic case report measured echocardiographic wall thickness or outflow gradient, and **none measured mitochondrial or contractile function**, so none of them bears on the `mek_inhibition_cardiac_mitochondrial_injury` toxicity claim. The therapeutic claim and the toxicity claim are supported by disjoint evidence.

---

## Key Findings

### Finding 1 — Raf1(L613V) knock-in mouse fills RAF1 Kinase Hyperactivation, and is a documented negative for valve morphogenesis

The heterozygous **Raf1 L613V/+ knock-in mouse** recapitulates core NS features: short stature, craniofacial dysmorphia, hematologic abnormalities, and **eccentric cardiac hypertrophy** with aberrant reactivation of the fetal gene programme. Agonist-evoked MEK–ERK activation is enhanced across multiple cell types, and **postnatal** MEK inhibition (PD0325901) normalised the growth, facial and cardiac defects — establishing that MEK/ERK hyperactivation is causal for the hypertrophy and that benefit is obtainable with treatment started after birth.

As a whole organism, this model carries haemodynamic load, multicellular compartments (fibroblast, endothelial, myocyte) and an intact — though murine — genome. It is therefore classified **(a) recapitulates** for **RAF1 Kinase Hyperactivation**, **ERK Cascade Hyperactivation** and **Cardiomyocyte Hypertrophy**. It would be curated as an **AnimalModel**.

Crucially, the same paper reports that **valvuloseptal development was normal**. Against **Cardiac Valve Morphogenesis Defects** this model is therefore a **class (d) documented negative** — a valuable result, because it shows that a RAF1 kinase-activating allele sufficient to drive postnatal hypertrophy does *not*, on its own, reproduce the valve lesion. On the MEK two-direction question, the readouts here were growth, facial morphology, cardiac mass and gene expression; **contractile and mitochondrial (STAT3-S727) toxicity were not assessed**, so this model does not bear on the toxicity claim.

> *"Valvuloseptal development was normal, but L613V/+ mice exhibited eccentric cardiac hypertrophy and aberrant cardiac fetal gene expression, and decompensated following pressure overload."*
> — *MEK-ERK pathway modulation ameliorates disease phenotypes in a mouse model of Noonan syndrome associated with the Raf1(L613V) mutation* [PMID 21339642](https://pubmed.ncbi.nlm.nih.gov/21339642/)

> *"postnatal MEK inhibition normalized the growth, facial, and cardiac defects in L613V/+ mice"*
> — same source

**What it does not show:** it is murine (non-human genome); it does not reproduce the valve defect; and the MEK-inhibitor experiments did not test contractile or mitochondrial endpoints, so they inform only the therapeutic axis.

### Finding 2 — Tie2-Cre Q79R-Shp2 endocardial-cushion mouse fills the unmodelled Cardiac Valve Morphogenesis Defects node

Endocardial-specific overexpression of the NS-associated **Q79R-Shp2** allele (driven by Tie2-Cre) caused embryonic lethality by E14.5 with **significantly enlarged endocardial cushions** in the atrioventricular canal and outflow tract; wild-type Shp2 expressed at comparable levels did not. The phenotype was accompanied by increased ERK1/2 activation in cushion mesenchyme, and **genetic deletion of ERK1 completely rescued the cushion phenotype** (ERK2 reduction did not), pinning causality to ERK1.

This is an **embryonic developmental system** — the correct scale for a valve-morphogenesis node — and observes a lesion that neither the curated RAF1 S257L iPSC-cardiomyocyte nor the postnatal Raf1 L613V mouse (valve development normal) can show. It is classified **(a) recapitulates** for **Cardiac Valve Morphogenesis Defects** and **(b) perturbs** for **ERK Cascade Hyperactivation** at the cushion-mesenchyme level. It would be curated as an **AnimalModel**.

> *"mutant embryos showed significantly enlarged endocardial cushions in the atrioventricular canal and in the outflow tract"*
> — *Role of ERK1/2 signaling in congenital valve malformations in Noonan syndrome* [PMID 19017799](https://pubmed.ncbi.nlm.nih.gov/19017799/)

> *"Deletion of ERK1 completely rescued the endocardial cushion phenotype, whereas ERK2 protein reduction did not affect endocardial cushion size."*
> — same source

**What it does not show:** embryonic lethality precludes any postnatal or adult readout; it does not address hypertrophy progression, haemodynamic-load-dependent remodeling, or MEK-inhibitor treatment.

### Finding 3 — MEK-inhibitor case reports are clinical treatment evidence, and the two MEK directions remain unreconciled

Multiple off-label / compassionate-use case reports document that **trametinib reverses NS-associated hypertrophic cardiomyopathy (HCM)**. In a RIT1-related NS infant, treatment produced *complete remission of the cardiac hypertrophy and significant improvement of the pulmonary valve stenosis* ([PMID 36184070](https://pubmed.ncbi.nlm.nih.gov/36184070/)). Further reports cover a RAF1 p.Ser257Leu child ([PMID 42256976](https://pubmed.ncbi.nlm.nih.gov/42256976/)) and lymphatic presentations ([PMID 36140671](https://pubmed.ncbi.nlm.nih.gov/36140671/)). A 17-case review ([PMID 40041314](https://pubmed.ncbi.nlm.nih.gov/40041314/)) reported short-term symptomatic improvement in all cases, with three deaths presumably unrelated to trametinib and no long-term follow-up available.

These reports are **clinical evidence for the mechanism** — RAF1/RIT1/SOS-driven ERK hypertrophy, reversible by MEK inhibition — and belong in the **treatment-evidence block**, not in `animal_models` or `experimental_models`. A case report is a treated patient, not a model system.

Decisively for the substitution problem: every readout was **echocardiographic wall thickness or outflow gradient over weeks-to-months**; **none assessed mitochondrial function or ERK-dependent mitochondrial STAT3 Ser-727 contractile toxicity**. These reports therefore bear on the **therapeutic claim only** and do **not** reconcile with the `mek_inhibition_cardiac_mitochondrial_injury` toxicity claim. The two directions of MEK pharmacology are, in the literature searched, supported by disjoint datasets and remain unreconciled. On timing, benefit is reported with early-infancy initiation in a RAS-MAPK-variant-positive context.

> *"She received off-label treatment with the MEK-inhibitor trametinib which resulted in complete remission of the cardiac hypertrophy and a significant improvement of the pulmonary valve stenosis."*
> — *Succesful MEK-inhibition of severe hypertrophic cardiomyopathy in RIT1-related Noonan Syndrome* [PMID 36184070](https://pubmed.ncbi.nlm.nih.gov/36184070/)

> *"A short-term improvement of symptoms was reported in all cases, with three deaths presumably unrelated to trametinib."*
> — *Trametinib as a targeted treatment in cardiac and lymphatic presentations of Noonan syndrome* [PMID 40041314](https://pubmed.ncbi.nlm.nih.gov/40041314/)

### Finding 4 — FRET ERK-reporter zebrafish for ERK Cascade Hyperactivation and Additional RAS-MAPK Signal-Amplifying Variants

A transgenic **zebrafish (*Danio rerio*)** ERK biosensor (the "Teen" FRET reporter) expressing NS-causing **Shp2 (PTPN11) gain-of-function variants** permits live, in-vivo quantification of ERK hyperactivation during gastrulation — *before* morphological defects appear — and detects normalisation by low-dose MEK inhibitor ([PMID 38594640](https://pubmed.ncbi.nlm.nih.gov/38594640/)). A companion protocol uses transient zebrafish RASopathy models for rapid functional validation of candidate pathogenic RAS-MAPK variants ([PMID 40388378](https://pubmed.ncbi.nlm.nih.gov/40388378/)).

Compartments and load: a whole embryonic vertebrate organism, transparent, with a non-mammalian genome, but **no mature four-chamber heart, no haemodynamic afterload and no postnatal cardiomyocyte biology**. It is classified **(a) recapitulates / (b) perturbs** for **ERK Cascade Hyperactivation** (ERK directly measured in vivo, pharmacologically reversible) and **(b) perturbs** for **Additional RAS-MAPK Signal-Amplifying Variants** (the platform is purpose-built to validate new variants' ERK impact). For **Cardiomyocyte Hypertrophy** it is **class (c) informative by analogy only** — the defining mammalian postnatal hypertrophy phenotype is absent. It would be curated as an **AnimalModel**. What it adds over the curated iPSC-cardiomyocyte: **live, real-time, whole-organism ERK dynamics and drug-response timing** a fixed monolayer cannot show. The MEK-inhibitor readout here is ERK phosphorylation/morphology; contractile and mitochondrial toxicity were not assessed, so it bears on the therapeutic/target-engagement axis only.

> *"we can quantitatively trace back the modulation of ERK phosphorylation obtained by low-dose MEK inhibitor treatment to early development, before the onset of morphological defects"*
> — *Assessment of the FRET-based Teen sensor to monitor ERK activation changes preceding morphological defects in a RASopathy zebrafish model and phenotypic rescue by MEK inhibitor* [PMID 38594640](https://pubmed.ncbi.nlm.nih.gov/38594640/)

> *"Functional validation of the pathogenicity of these variants, essential for accurate diagnosis, requires fast and reliable protocols, preferably in vivo."*
> — *An Efficient Protocol to Assess ERK Activity Modulation in Early Zebrafish Noonan Syndrome Models via Live FRET Microscopy and Immunofluorescence* [PMID 40388378](https://pubmed.ncbi.nlm.nih.gov/40388378/)

### Finding 5 — The Growth Plate Chondrocyte Differentiation Defect node is poorly served: available chondrocyte models are loss-of-function, the opposite direction to Noonan

Chondrocyte-specific genetic models of the SHP2/ERK growth-plate axis in the literature are **loss-of-function**. Mosaic postnatal *Ptpn11* inactivation delays the terminal differentiation of chondrocytes and produces enchondroma-like lesions ([PMID 24875294](https://pubmed.ncbi.nlm.nih.gov/24875294/)); inducible *Shp2* chondrocyte knockout deforms orofacial cartilage with reduced ERK ([PMID 25919282](https://pubmed.ncbi.nlm.nih.gov/25919282/)); ERK1/2 deletion in hypertrophic chondrocytes expands the hypertrophic zone and shortens long bones ([PMID 25401279](https://pubmed.ncbi.nlm.nih.gov/25401279/)). All of these *reduce* SHP2/ERK signalling, whereas NS is caused by **gain-of-function** RAS-MAPK activation.

For the **Growth Plate Chondrocyte Differentiation Defect** node these are therefore **class (b/c)** — they perturb and illuminate the same chondrocyte ERK-maturation axis the node names, but they do **not** recapitulate the Noonan gain-of-function lesion (the defining GoF driver is absent or reversed). The nearest GoF evidence is organismal short stature in the Raf1 L613V mouse, which is whole-organism and not chondrocyte-resolved. A chondrocyte-specific *Noonan-GoF* growth-plate model was searched for ("Shp2/PTPN11/Ptpn11 chondrocyte growth plate Noonan short stature") and **not retrieved** — a genuine gap.

> *"We found that SHP2 depletion, or inhibition of the ERK1/2 pathway, delays the terminal differentiation of chondrocytes from the early-hypertrophic to the late-hypertrophic stage."*
> — *SHP2 regulates chondrocyte terminal differentiation, growth plate architecture and skeletal cell fates* [PMID 24875294](https://pubmed.ncbi.nlm.nih.gov/24875294/)

### Finding 6 — Confirmed-empty systems: human Noonan myocardial slices/explants and loaded RASopathy 3D cardiac models

Two targeted search campaigns returned no Noonan/RASopathy-specific study:

1. **Human Noonan myocardial tissue** — slices, explants or resected surgical tissue with contractility or calcium-handling readouts. Searches included "Noonan syndrome human cardiomyocyte myocardial biopsy explant calcium handling contractility", "Noonan syndrome myectomy myocardial tissue histology surgical specimen", and "Noonan syndrome myocardium histopathology disarray resected cardiac tissue".
2. **Loaded 3D cardiac systems** — "engineered heart tissue hiPSC cardiomyocyte hypertrophy MAPK RAS force contractility 3D" and "cardiac organoid RASopathy Noonan hypertrophy heart-on-chip".

This is a **reported-empty result, not a claim of non-existence**: no loaded, force-generating or native-tissue Noonan cardiac model was retrievable. The consequence is that the **Cardiomyocyte Hypertrophy node currently has no model that carries haemodynamic load *plus* a human genome *plus* multicellular (fibroblast/endothelial) compartments**. The curated RAF1 S257L iPSC-cardiomyocyte monolayer (human but unloaded) and the Raf1 L613V mouse (loaded but murine) bracket this gap. **An engineered heart tissue built from RASopathy iPSC-cardiomyocytes would be the missing ExperimentalModel** that adds auxotonic load and a force/contractility readout to a human-genome system — and would be the ideal platform to test the therapeutic-versus-toxicity question directly.

### Finding 7 — LEOPARD/PTPN11 iPSC-cardiomyocyte corroborates Cardiomyocyte Hypertrophy via a different gene; NS-Shp2 zebrafish covers Hematologic Dysregulation

Patient-derived **LEOPARD-syndrome iPSC-cardiomyocytes** (PTPN11 T468M) are larger, show greater sarcomeric organisation and preferential nuclear localisation of NFATC4 — a hypertrophic signature ([PMID 20535210](https://pubmed.ncbi.nlm.nih.gov/20535210/)). For **Cardiomyocyte Hypertrophy** this is **(a) recapitulates** at the cellular level, acting as a **corroborator** of the curated RAF1 S257L iPSC-cardiomyocyte but via a *different gene*, demonstrating genotype convergence onto the same cellular endpoint. It is an **ExperimentalModel**. Important caveat: LEOPARD PTPN11 alleles are **catalytically impaired** (not the classic Noonan gain-of-function), so it must **not** be curated under *SHP2 Gain-of-Function Activation*. Limitation: as a monolayer it has no haemodynamic load, no fibroblast/endothelial compartment and an immature state — it adds genotypic breadth, not a new compartment.

A CRISPR knock-in **Shp2 Noonan zebrafish** shows inflammatory transcriptional changes in hematopoietic stem and progenitor cells (HSPCs) and blood defects shared with JMML patients ([PMID 35535491](https://pubmed.ncbi.nlm.nih.gov/35535491/)). For **Hematologic Dysregulation** this is **(a) recapitulates**, as an **AnimalModel** (whole vertebrate with a transparent embryo enabling live haematopoiesis imaging). It does not model cardiac hypertrophy or valve morphogenesis.

> *"in vitro-derived cardiomyocytes from LEOPARD syndrome iPSCs are larger, have a higher degree of sarcomeric organization and preferential localization of NFATC4 in the nucleus"*
> — *Patient-specific induced pluripotent stem-cell-derived models of LEOPARD syndrome* [PMID 20535210](https://pubmed.ncbi.nlm.nih.gov/20535210/)

> *"we explored transcriptomes of HSPCs with SHP2 mutations derived from JMML patients and a novel NS zebrafish model"*
> — *Inflammatory response in hematopoietic stem and progenitor cells triggered by activating SHP2 mutations evokes blood defects* [PMID 35535491](https://pubmed.ncbi.nlm.nih.gov/35535491/)

### Finding 8 — Congenital Cardiac Structural Defects and RASopathy Neoplastic Predisposition: Ptpn11 D61G mouse (overlap-flagged) and distinct human JMML HSCs

The foundational **Ptpn11 D61G knock-in mouse** reproduces short stature, craniofacial abnormalities, **myeloproliferative disease**, and — in severely affected embryos — **multiple cardiac defects** with increased endocardial-cushion Erk activation ([PMID 15273746](https://pubmed.ncbi.nlm.nih.gov/15273746/)). This maps to **Congenital Cardiac Structural Defects** (class a), **RASopathy Neoplastic Predisposition** (class a, myeloproliferative/JMML-like), **Hematologic Dysregulation** and **ERK Cascade Hyperactivation**. It is a whole-organism **AnimalModel**.

**Overlap caveat:** this canonical "Noonan SHP2 mutant mouse" very likely corresponds to the already-curated generic *"Noonan syndrome-causing SHP2 mutant mouse model"* (which carries no publication and no node-links). If so it is **not a new candidate**, but its PMID and node-links (13, 14) are currently unrecorded and could be *attached to the existing entry* rather than re-curated.

A genuinely **distinct** model for the neoplastic/hematologic nodes is the **JMML patient-derived hematopoietic stem/progenitor cell culture** (**ExperimentalModel**), used to show activating-Shp2-driven proliferation and its pharmacologic reversal ([PMID 40640547](https://pubmed.ncbi.nlm.nih.gov/40640547/)) — **(a) recapitulates** the neoplastic/hematologic driver in human primary cells. Limitation: HSC cultures carry no cardiac compartment and no load.

> *"Severely affected Ptpn11(D61G/+) embryos ( approximately 50%) have multiple cardiac defects similar to those in mice lacking the Ras-GAP protein neurofibromin."*
> — *Mouse model of Noonan syndrome reveals cell type- and gene dosage-dependent effects of Ptpn11 mutation* [PMID 15273746](https://pubmed.ncbi.nlm.nih.gov/15273746/)

> *"SFX-01 also attenuated JMML human patient-derived hematopoietic stem cell proliferation that was linked to STAT1 signaling and decreased cyclin D1 expression, resulting in cell-cycle arrest"*
> — *SFX-01 is therapeutic against myeloproliferative disorders caused by activating mutations in Shp2* [PMID 40640547](https://pubmed.ncbi.nlm.nih.gov/40640547/)

### Finding 9 — Rit1 A57G mouse fills the unmodelled Lymphatic Structural Abnormalities node (overlap-flagged against the curated RIT1 mouse)

An embryonic phenotyping study of a Noonan-syndrome **Rit1 A57G knock-in mouse** found **cardiovascular and lymphatic abnormalities arising in the fetal period**, with MEK/ERK activation implicated as the cause of cardiac hypertrophy ([PMID 41388936](https://pubmed.ncbi.nlm.nih.gov/41388936/)). Node mapping: **Lymphatic Structural Abnormalities** (currently unmodelled) — **(a) recapitulates**, in a whole-organism **AnimalModel** with an intact lymphatic compartment; **Congenital Cardiac Structural Defects** and **Cardiomyocyte Hypertrophy** via MEK/ERK (class a/b); **ERK Cascade Hyperactivation**; **RIT1-Mediated RAF Recruitment**.

**Overlap caveat:** the already-curated *"RIT1 mutant Noonan syndrome mouse model"* (no publication recorded) may be the same Rit1 line; if so this is not a wholly new organism, but the **lymphatic node-link and the fetal-timing data are new and recordable**, and PMID 41388936 can be attached. What it does **not** show: it is an embryonic/fetal analysis, so it does not address postnatal hypertrophy progression, adult haemodynamic-load-dependent remodeling, or MEK-inhibitor treatment (no contractile/mitochondrial readout; does not bear on the toxicity claim). The MEK/ERK attribution to hypertrophy here is **observational/correlative**, not a pharmacologic manipulation.

> *"Rit1 mutation causes cardiovascular and lymphatic abnormalities in the fetal period, and that the activation of MEK/ERK is the potential pathogenesis of cardiac hypertrophy"*
> — *Phenotypic Analysis of Embryos in a Noonan Syndrome Model Mouse With the Rit1 A57G Mutation* [PMID 41388936](https://pubmed.ncbi.nlm.nih.gov/41388936/)

---

## Mechanistic Model / Interpretation

The candidate models tile the RAS-MAPK cardiac axis by **scale** and by **genome/compartment completeness**. The organising insight is that no single alternative model carries the whole mechanism: each covers a defined stretch of it.

```
   MOLECULAR  ──────────►  CELLULAR  ──────────►  TISSUE / ORGAN  ──────────►  WHOLE ORGANISM
   (variant → ERK)         (cardiomyocyte)        (loaded 3D, valve cushion)    (mouse, fish)

 Zebrafish FRET          LEOPARD PTPN11            [EMPTY: human EHT /          Raf1 L613V mouse
 ERK reporter            iPSC-CM (ExpModel)         engineered heart tissue,     (RAF1, ERK, hypertrophy;
 (Shp2, in vivo ERK;     corroborates             organ-chip, organoid)         valve NEGATIVE)
 variant validation)     hypertrophy                                            
                                                  Q79R-Shp2 Tie2-Cre            Rit1 A57G mouse
 Curated RAF1 S257L      Curated RAF1 S257L        endocardial cushion          (lymphatic + cardiac,
 iPSC-CM (ERK,           iPSC-CM (hypertrophy)     (VALVE, embryonic,           fetal)
 hypertrophy)                                      ERK1-dependent)              
                        JMML patient HSCs          Ptpn11 D61G mouse           Shp2 zebrafish
                        (neoplastic, human)        embryo cardiac defects       (hematologic)
                                                   (overlap w/ curated SHP2)
```

Two features of this map matter most:

1. **The valve node and the RAF1 node need different systems.** The RAF1 L613V mouse proves that a kinase-activating RAF1 allele drives postnatal hypertrophy *without* a valve defect (valvuloseptal development normal). The valve lesion instead requires an **embryonic, endocardial-compartment** perturbation (Q79R-Shp2), and is **ERK1-dependent**. So the pathograph's separation of *RAF1 Kinase Hyperactivation* from *Cardiac Valve Morphogenesis Defects* is mechanistically real, not an artefact — they are reached by different alleles in different compartments at different developmental windows.

2. **The missing model is the loaded human one.** Along the completeness axis, the Cardiomyocyte Hypertrophy node has a human-unloaded model (iPSC-CM) and a loaded-murine model (L613V mouse) but nothing with human genome + load + stromal compartments. This is exactly where the two MEK directions could be discriminated — a RASopathy engineered heart tissue is the one platform that could measure force/contractility under load *and* mitochondrial endpoints in a human-genome context.

### MEK inhibition — the two directions are not reconciled

| Direction | What the evidence is | What was measured | Duration | Contractile/mitochondrial function assessed? | Bears on |
|---|---|---|---|---|---|
| **Therapeutic** (reverses hypertrophy) | Patient case reports (36184070, 42256976, 40041314, 36140671); Raf1 L613V mouse (21339642) | Echo wall thickness, outflow gradient; mouse cardiac mass + gene expression | Weeks–months (patients); postnatal course (mouse) | **No** | Therapeutic claim only |
| **Toxic** (`mek_inhibition_cardiac_mitochondrial_injury`) | Curated module: loss of ERK-dependent mitochondrial STAT3 Ser-727, respiratory-chain failure, reversible hypocontractility | Mitochondrial respiration, contractility | — | Yes (by construction) | Toxicity claim only |

The therapeutic evidence and the toxicity evidence come from **non-overlapping measurements**. No therapeutic study in a RAS-MAPK-variant context measured mitochondrial or contractile function, and the toxicity module is not reported in a Noonan-variant-positive model. **The directions are therefore not reconciled in the literature searched**, and should not be presented as though they are. The therapeutic window's dependence on *timing* is suggested (benefit with postnatal/early-infancy initiation) but dose- and variant-dependence of the *toxic* direction in a Noonan background is untested.

---

## Evidence Base

| PMID | Title (abbreviated) | Model / evidence type | Node(s) served | Class |
|---|---|---|---|---|
| [21339642](https://pubmed.ncbi.nlm.nih.gov/21339642/) | *MEK-ERK modulation ... Raf1(L613V) mouse* | AnimalModel (genetic) | RAF1 Kinase Hyperactivation; ERK Cascade; Cardiomyocyte Hypertrophy / **valve = negative** | (a); **(d)** for valve |
| [19017799](https://pubmed.ncbi.nlm.nih.gov/19017799/) | *Role of ERK1/2 signaling in congenital valve malformations in NS* | AnimalModel (genetic, embryonic) | Cardiac Valve Morphogenesis Defects; ERK Cascade | (a); (b) |
| [38594640](https://pubmed.ncbi.nlm.nih.gov/38594640/) | *FRET-based Teen sensor ... RASopathy zebrafish* | AnimalModel (genetic/reporter) | ERK Cascade; Additional RAS-MAPK Variants; Cardiomyocyte Hypertrophy | (a)/(b); **(c)** for hypertrophy |
| [40388378](https://pubmed.ncbi.nlm.nih.gov/40388378/) | *Protocol to assess ERK ... zebrafish NS models* | AnimalModel platform | Additional RAS-MAPK Variants | (b) |
| [20535210](https://pubmed.ncbi.nlm.nih.gov/20535210/) | *iPSC-derived models of LEOPARD syndrome* | ExperimentalModel (iPSC-CM) | Cardiomyocyte Hypertrophy (corroborator, different gene) | (a) |
| [35535491](https://pubmed.ncbi.nlm.nih.gov/35535491/) | *Inflammatory response in HSPCs ... SHP2 mutations* | AnimalModel (zebrafish) | Hematologic Dysregulation | (a) |
| [15273746](https://pubmed.ncbi.nlm.nih.gov/15273746/) | *Mouse model of NS ... Ptpn11 mutation* | AnimalModel — **overlap w/ curated SHP2 mouse** | Congenital Cardiac Structural Defects; Neoplastic Predisposition; Hematologic | (a) |
| [40640547](https://pubmed.ncbi.nlm.nih.gov/40640547/) | *SFX-01 ... myeloproliferative disorders / Shp2* | ExperimentalModel (human JMML HSCs) | RASopathy Neoplastic Predisposition; Hematologic | (a) |
| [41388936](https://pubmed.ncbi.nlm.nih.gov/41388936/) | *Phenotypic Analysis ... Rit1 A57G mutation* | AnimalModel — **overlap w/ curated RIT1 mouse** | Lymphatic Structural Abnormalities; Congenital Cardiac; Cardiomyocyte Hypertrophy; RIT1-Mediated RAF Recruitment | (a)/(b) |
| [24875294](https://pubmed.ncbi.nlm.nih.gov/24875294/) | *SHP2 regulates chondrocyte terminal differentiation* | Genetic (chondrocyte, **LOF**) | Growth Plate Chondrocyte Differentiation Defect | (b)/(c) |
| [25919282](https://pubmed.ncbi.nlm.nih.gov/25919282/) | *SHP2-Deficiency in Chondrocytes ...* | Genetic (chondrocyte, LOF) | Growth Plate Chondrocyte Differentiation Defect | (b)/(c) |
| [25401279](https://pubmed.ncbi.nlm.nih.gov/25401279/) | *ERK1/2 regulate chondrocyte terminal differentiation* | Genetic (chondrocyte, LOF) | Growth Plate Chondrocyte Differentiation Defect | (b)/(c) |
| [36184070](https://pubmed.ncbi.nlm.nih.gov/36184070/) | *MEK-inhibition ... RIT1-related NS* | **Treatment evidence** (case report) | Therapeutic claim (RIT1) | — |
| [42256976](https://pubmed.ncbi.nlm.nih.gov/42256976/) | *Trametinib ... RAF1-Related NS (p.Ser257Leu)* | **Treatment evidence** (case report) | Therapeutic claim (RAF1) | — |
| [40041314](https://pubmed.ncbi.nlm.nih.gov/40041314/) | *Trametinib ... cardiac and lymphatic presentations of NS* | **Treatment evidence** (17-case review) | Therapeutic claim | — |
| [36140671](https://pubmed.ncbi.nlm.nih.gov/36140671/) | *Severe Lymphatic Disorder ... Trametinib ... SOS1* | **Treatment evidence** (case report) | Therapeutic claim (SOS1, lymphatic) | — |

**Schema-block assignment summary:** AnimalModels — 21339642, 19017799, 38594640/40388378, 35535491, 15273746 (overlap), 41388936 (overlap). ExperimentalModels — 20535210, 40640547. Treatment evidence (not models) — 36184070, 42256976, 40041314, 36140671.

---

## Limitations and Knowledge Gaps

1. **No loaded human cardiac model exists in the literature searched.** Human Noonan myocardial slices/explants/resected tissue with contractility or calcium readouts, and RASopathy engineered heart tissue / organ-chips / cardiac organoids, all returned empty. This is the single largest gap: the Cardiomyocyte Hypertrophy node has no model with human genome + haemodynamic load + stromal compartments.
2. **The two MEK directions are unreconciled.** No therapeutic study measured mitochondrial or contractile function; the toxicity module is not tested in a Noonan-variant background. Dose-, timing- and variant-dependence of the toxic direction is unknown.
3. **Two mouse candidates likely overlap curated entries.** Ptpn11 D61G (15273746) probably *is* the curated generic SHP2 mouse; Rit1 A57G (41388936) may *be* the curated RIT1 mouse. These should be treated as *attach PMID + new node-links* actions, not new curations.
4. **The Growth Plate node has no gain-of-function chondrocyte model.** All retrievable chondrocyte models are SHP2/ERK loss-of-function — mechanistically the opposite of Noonan — so they perturb but do not recapitulate the node.
5. **Model-specific scope limits:** the valve mouse is embryonic-lethal (no postnatal readout); the zebrafish has no mature heart (hypertrophy is class c only); iPSC-CM corroborators are unloaded monolayers (genotypic breadth, not a new compartment); case reports are clinical evidence, not models.
6. **Negative searches are reported as searches, not proofs of non-existence.** The empty-system claims reflect the queries listed in Finding 6, not an exhaustive census of all literature.

---

## Proposed Follow-up Experiments / Actions

1. **Build or find a RASopathy engineered heart tissue (EHT).** Construct an EHT from RAF1- or PTPN11-variant iPSC-cardiomyocytes with fibroblast/endothelial co-culture under auxotonic load. This is the missing **ExperimentalModel** for Cardiomyocyte Hypertrophy with a human genome and a force readout — and the ideal platform to measure contractility *and* mitochondrial endpoints under MEK inhibition, directly testing the therapeutic-versus-toxicity question.
2. **Measure mitochondrial/contractile endpoints in a therapeutic MEK-inhibition experiment.** In the Raf1 L613V mouse or a RASopathy EHT, assess ERK-dependent mitochondrial STAT3 Ser-727 phosphorylation, respiratory-chain function and contractility across doses and initiation timings, to reconcile the two MEK directions.
3. **Attach, don't re-curate, the overlap-flagged mice.** Record PMID 15273746 + node-links (Congenital Cardiac Structural Defects, Neoplastic Predisposition, Hematologic) against the curated SHP2 mouse; record PMID 41388936 + the new **Lymphatic Structural Abnormalities** link against the curated RIT1 mouse.
4. **Seek or generate a gain-of-function chondrocyte Noonan model.** A chondrocyte-specific NS-GoF allele (e.g., Ptpn11 D61G or Raf1 L613V under a chondrocyte Cre) would convert the Growth Plate node from "perturbed by LOF analogues" to "recapitulated".
5. **Curate the valve node to the Q79R-Shp2 embryonic mouse (PMID 19017799)** and record the Raf1 L613V mouse as the **documented negative (class d)** for the same node — a valuable explicit negative.
6. **Search the surgical-pathology literature** specifically (myectomy/explant biobanks) for Noonan HCM specimens with any functional readout, to confirm or close the human-tissue gap.

---

*Report generated from 5 completed investigation iterations; 10 confirmed findings; 33 papers reviewed. All PMIDs and verbatim quotes above were validated against source abstracts during the investigation.*


## Artifacts

- [OpenScientist final report](Noonan_Syndrome-alternative-models-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Noonan_Syndrome-alternative-models-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:24875294` (5 mentions) - SHP2 regulates chondrocyte terminal differentiation, growth plate architecture and skeletal cell fates.
  - shared terms: postnatal, shp2

Weighed against this report's own most characteristic terms: `model`, `noonan`, `cardiac`, `hypertrophy`, `mouse`, `raf1`, `defect`, `erk`, `curated`, `syndrome`, `node`, `cardiomyocyte`, `valve`, `mek`, `therapeutic`, `l613v`, `mitochondrial`, `postnatal`, `compartment`, `shp2`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.