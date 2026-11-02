---
title: 'Skin Sensitization AOP: Assays, Key Events, and Where dismech Disagrees'
status: IN_PROGRESS
description: >-
  The published assay-to-Key-Event mapping for AOP 40 (covalent protein binding
  leading to skin sensitisation), read off Aleksic et al. 2024 with a verified snippet
  behind every row — and a first worked case of dismech's own corpus bearing on an
  AOP-Wiki Key Event assignment that the review article itself flags as uncertain.
tags: [FRAMEWORK_ALIGNMENT, EVIDENCE, EXTERNAL_COLLABORATION, ENVIRONMENTAL_EXPOSURE]
diseases:
  - Contact_Dermatitis
  - Atopic_Dermatitis
  - Autoimmune_Pancreatitis
  - Bacterial_Vaginosis
  - Chlamydia_Pneumoniae_Pneumonia
  - Chorioamnionitis
  - Clostridioides_difficile_Infection
  - Familial_Pityriasis_Rubra_Pilaris
  - G6PC3_Deficiency
  - Pyoderma_Gangrenosum
  - SAPHO_Syndrome
  - Scabies
  - Shigellosis
  - Spotted_Fever_Rickettsiosis
  - Subacute_Inflammatory_Demyelinating_Polyneuropathy
---

# Skin Sensitization AOP: Assays, Key Events, and Where dismech Disagrees

## Scope

This page carries the AOP 40 use case out of
[AOP_EMOD_ALIGNMENT](AOP_EMOD_ALIGNMENT.md), where it began as a third pilot
alongside the lead and liver-fibrosis cases. It outgrew that page for a reason worth
stating: the other two pilots ask whether dismech content *can be aligned to* an AOP.
This one found a place where dismech content **bears on whether an AOP's own Key Event
assignment is right**, which is a different and more useful relationship. The alignment
project keeps the schema questions; this page keeps the worked case.

The target is [AOP 40](https://aopwiki.org/aops/40), *Covalent Protein binding leading to
Skin Sensitisation*. Unlike the other two pilots it enters from a **review article**, and
it is the only case where the assay-to-Key-Event mapping is already published: Aleksic M,
Rajagopal R, de-Ávila R, Spriggs S, Gilmour N. *The skin sensitization adverse outcome
pathway: exploring the role of mechanistic understanding for higher tier risk assessment.*
Crit Rev Toxicol 2024;54(2):69–91
([PMID:38385441](https://pubmed.ncbi.nlm.nih.gov/38385441/),
doi:[10.1080/10408444.2024.2308816](https://doi.org/10.1080/10408444.2024.2308816)).
Open access under CC BY-NC-ND.

Structurally it is the **inverse** of the liver fibrosis case: there, one
microphysiological system instrumented several Key Events of one AOP; here, a whole OECD
test-guideline battery exists in which each guideline is aligned to a *single* Key Event,
and the integration happens in a layer above the assays.

## How to read the snippets

Snippets are verbatim substrings of the article's PDF text layer, with three normalizations
and no others: line-break hyphenation rejoined, the superscript `TM` left inline as the text
layer emits it (`KeratinoSens TM`, `GARD TM skin`), and — where marked ‡ — the running
header and page number removed where a sentence crosses the page 3/4 break. The space in
`OECD TG 442 C` is the article's own. These have **not** been put through dismech's
reference validator, because AOP-Wiki aside, this article's full text is not in the
reference cache: `references_cache/PMID_38385441.md` and
`references_cache/DOI_10.1080_10408444.2024.2308816.md` both hold abstract-only records
(`content_type: unavailable` on the DOI record), and the publisher refuses automated
fetches. Treat them as transcribed, not machine-verified.

## Key Events against the assays aligned to them

Key Event titles and identifiers are AOP-Wiki's, read from the 2026-10-03 bulk XML export;
the article itself uses only `KE1`–`KE4` and does not cite AOP-Wiki identifiers, so the
first two columns are a join, not a quotation.

| KE | Event (AOP-Wiki) | Assays / methods | OECD TG | Snippet supporting the mapping |
|---|---|---|---|---|
| KE1 *(MIE)* | [396](https://aopwiki.org/events/396) Covalent Binding, Protein | DPRA, ADRA, kDPRA | 442C | "OECD TG 442 C describes the direct peptide reactivity assay (DPRA), amino acid derivative reactivity assay (ADRA) and the kinetic DPRA (kDPRA), which are test methods addressing KE1 (the binding of haptens to proteins in the skin" ‡ |
| KE2 | [826](https://aopwiki.org/events/826) Activation, Keratinocytes | KeratinoSens™, LuSens | 442D | "OECD TG 442D describes the KeratinoSens TM and LuSens methods which address KE2 (the activation of keratinocytes" |
| KE3 | [398](https://aopwiki.org/events/398) Activation, Dendritic Cells | h-CLAT, U-SENS™, IL-8 Luc assay, GARD™skin | 442E | "OECD TG 442E describes the Human Cell Line Activation test (hCLAT), U937 cell line activation Test (USens TM ), Interleukin-8 Reporter Gene Assay (IL 8 Luc assay) and Genomic Allergen Rapid Detection (GARD TM ) for assessment of skin sensitizers (GARD TM skin) which are test methods addressing KE3 (the activation of dendritic cells (DCs))" |
| KE4 | [272](https://aopwiki.org/events/272) Activation/Proliferation, T-cells | mouse LLNA and its variants | 429, 442A, 442B | "The LLNA, in fact, addresses KE4, measuring T cell proliferation in treated mice rather than established sensitization." |
| AO | [827](https://aopwiki.org/events/827) sensitisation, skin | none aligned; patch testing is diagnostic | — | "ACD is diagnosed by specialist dermatological investigations involving patch testing to identify the allergen to which an individual is allergic and enable allergen avoidance." |

**Every validated guideline assay is aligned to exactly one Key Event, and two of the five
Events have no validated non-animal assay at all.** The second clause is the article's own
emphasis, stated twice:

> Currently, there are no NAMs addressing KE4 (the activation and proliferation of a T cell
> response), which are sufficiently progressed for implementation in OECD TG or for use in a
> Next Generation Risk Assessment (NGRA)

> It remains difficult to envisage robust, sensitive, and reproducible assays addressing
> this KE in vitro in the near future.

### Methods that sit beside the battery

Named in the article, aligned to a Key Event's biology but not carrying a guideline.

| Method | Nearest KE | Status in the article | Snippet |
|---|---|---|---|
| Peroxidase Peptide Reactivity Assay (PPRA) | KE1 | reactivity assay adapted to activate pro-haptens; not in TG 442C | "adaptations to existing reactivity assays, aiming to incorporate "activation" of nonelectrophilic chemicals to their electrophilic metabolites which then bind to the model nucleophiles (e.g. Peroxidase Peptide Reactivity Assay (PPRA)" |
| DEREK Nexus, OECD QSAR Toolbox, TIMES, ToxTree | KE1 | *in silico*, chemistry and mechanistic domain | "several in silico tools, providing useful information on chemistry and mechanistic domain of sensitizers (e.g. DEREK Nexus, OECD QSAR Toolbox, TIMES, ToxTree)" |
| SenCeeTox®, SENS-IS, EpiSensA, VITOSENS | KE2 | transcriptional biomarker signatures | "Genes downstream of the Nrf2 pathway and other cellular stress markers have been evaluated as signatures for sensitizer-induced transcriptional changes in novel in vitro assays, such as SenCeeTox V R , SENS-IS, EpiSensA, and VITOSENS" |
| Buehler test, Guinea pig maximization Test (GPMT) | — | *in vivo* evidence; **no KE assigned** | "In vivo evidence (red box) comes from mouse local lymph node assay (LLNA) (OECD 2010a ) and its variants (OECD 2010b , 2018 ) and Buehler and Guinea pig maximization Test (GPMT) (OECD 2022b )." |

## One assay is aligned to a Key Event its biology does not match

Worth carrying out of the table, because it is a documented misalignment rather than a
clean row, and it is the kind of thing a KE cross-reference would have to be able to record:

> Interestingly, the IL 8 assay, which is the only OECD validated cytokine assay (Watanabe
> et al. 2007 ; Sand et al. 2018 ) was developed as a marker for APC activation (KE3) rather
> than keratinocyte inflammation (KE2), possibly due to the cell type used in the assay

The article generalizes the same caution across all of TG 442E — "While read outs from all
these assays have been aligned to KE3, some of these assays are also representative of the
events leading up to KE3." So KE3 alignment for this battery is an *assignment*, not a
measurement boundary.

## Models and approaches spanning more than one Key Event

The article treats single-assay-to-single-KE alignment as the floor, not the usable unit:

> With the exception of the GARD TM skin assay in certain circumstances (JRC EC 2021 ),
> these NAMs should not be used alone for hazard and potency categorization, but the output
> should be combined with information from other NAMs within a DA.

Two different kinds of thing span several Key Events, and they are worth keeping apart.

**An assay that itself reads out several Key Events.** This is the only place the article
uses the phrase:

> SENS-IS and GARDskin TM dose response assays (Cottrez et al. 2015 , 2016 ; Gradin et al.
> 2021 ), which cover multiple KEs, show some promise in providing more quantitative skin
> sensitizing potency assessment by predicting a skin sensitization class
> (strong/moderate/weak/non-sensitizing). However, it remains to be seen how these can be
> utilized in risk assessment.

**A defined approach (DA) that integrates outputs from assays aligned to different Key
Events.** These are multi-KE by construction rather than by readout.

| Model / approach | What the article says it does | Snippet |
|---|---|---|
| **SARA model** (Skin Allergy Risk Assessment) | derives a human-relevant point of departure with quantified uncertainty; adapted with NICEATM for UN GHS classification; separately incorporates clinical contact-allergy experience | "The SARA model allows derivation of a human relevant point of departure with quantifiable uncertainty and a risk metric for use in quantitative risk assessment (Reynolds et al. 2019 ) and has recently been adapted in collaboration with NICEATM to address UN GHS classification" · "clinical experience and established trends in contact allergy have been used within the SARA model DA to enable a prediction of the risk of induction of skin sensitization to a given exposure arising from a consumer product" |
| Bayesian Integrated Testing Strategy (ITS) | listed as an additional DA (Jaworska et al. 2013) | "Additional DAs include Bayesian Integrated Testing Strategy (ITS) (Jaworska et al. 2013 ), Artificial Neural Network (Tsujita-Inoue et al. 2015 ) and a series of linear regression models" |
| Artificial Neural Network | additional DA (Tsujita-Inoue et al. 2015) | as above |
| Linear regression models | additional DAs (Natsch and Gerberick 2022a, 2022b; Natsch 2023) | as above |
| The three DAs in OECD guideline 497 | integrate individual assay data for classification; **the article does not name them** | "Three DAs are currently included in the OECD guideline 497 (OECD 2023a ) which allow data from the individual assays to be integrated for chemical classification" |
| Quantitative AOP models (qAOP) | the forward-looking multi-KE integration layer | "Utilization of the quantitative data of KEs and additional elements of AOPs may ultimately be achieved through quantitative AOP models (qAOP) (Zgheib et al. 2019 ; Spinu et al. 2020 ), which may help us avoid the linear interpolation of the quantitative outputs of the KEs in the AOP" |

Three things this table deliberately does not say.

- **"SARA-ICE" is not the article's name for it.** The article says "SARA model" throughout
  and describes the NICEATM collaboration as an adaptation addressing UN GHS classification,
  citing a manuscript in preparation (Reynolds et al. 2023). It never writes the
  string `SARA-ICE`. If that name is wanted here it needs its own source.
- **No DA's Key Event inputs are enumerated.** The article says DAs combine outputs from
  assays that are each aligned to a Key Event, which makes them multi-KE, but it does not
  state which assays feed SARA, the Bayesian ITS, the ANN, or the regression models.
  Writing a per-model KE list from this source alone would be invention.
- **The three OECD 497 DAs are unnamed in the article.** Their identities (the 2o3 and
  ITS-style approaches) are not quotable from here.

## Where the article's own KE4 mapping lives

The LLNA-to-KE4 mapping in the table above is stated only in the Figure 2 caption, with a
correction attached ("rather than established sensitization"). The body text says just that
the LLNA is the sole validated assay measuring T cell proliferation, without naming a Key
Event. Anyone reusing that row should know the alignment rests on a caption.

No assay is aligned to the adverse outcome anywhere in the article. Patch testing appears
only as **diagnosis of ACD in patients**, which is a different claim from an assay
instrumenting a Key Event.
## What does dismech tell us about IL-8?

The misalignment above is stated in the article as a suspicion — the assay "was developed
as a marker for APC activation (KE3) rather than keratinocyte inflammation (KE2), possibly
due to the cell type used in the assay." AOP 40 nonetheless has the whole of TG 442E,
IL-8 Luc included, aligned to KE3. dismech holds an independent body of curated IL-8
mechanism, assembled from disease literature by curators who were not looking at AOP 40,
and it can be asked what cell it thinks produces IL-8 and what it thinks follows.

**No dismech pathophysiology node places IL-8 production in a dendritic cell.** Across
every node in `kb/` whose annotations or causal edges carry IL-8, the bound `cell_types`
are:

| Cell bound on the node | Entries |
|---|---|
| keratinocyte | Atopic_Dermatitis, Familial_Pityriasis_Rubra_Pilaris (two nodes), Scabies |
| other epithelium | Bacterial_Vaginosis (vaginal squamous), Chlamydia_Pneumoniae_Pneumonia (respiratory) |
| microvascular endothelial cell | Spotted_Fever_Rickettsiosis |
| T-helper 17 / T-helper 1 cell | Pyoderma_Gangrenosum, SAPHO_Syndrome (with macrophage) |
| neutrophil | G6PC3_Deficiency |
| none bound | Autoimmune_Pancreatitis (ductal epithelium, stated in prose), Chorioamnionitis, Clostridioides_difficile_Infection |

Keratinocyte is the most frequent single answer and the dendritic cell does not appear at
all. That is not a refutation of the KE3 alignment — a cell line's readout is a property
of the assay, not of the disease literature — but it is independent corroboration of the
article's own doubt, from a corpus with no stake in the question.

**Every IL-8 causal edge in dismech ends in neutrophil recruitment.** Nine entries, each
curated separately:

| Entry | Edge carrying IL-8 |
|---|---|
| Autoimmune_Pancreatitis | Increased Ductal Interleukin-8 Expression → Neutrophilic Duct Infiltration |
| Chorioamnionitis | Proinflammatory Cytokine and Chemokine Production → Neutrophil Chemotaxis into the Chorioamniotic Membranes |
| Clostridioides_difficile_Infection | Toxin Production (TcdA/TcdB) → Neutrophil Recruitment and Inflammation |
| Pyoderma_Gangrenosum | Th17/Th1-Skewed Cytokine Amplification → Neutrophil Recruitment to the Dermis |
| Chlamydia_Pneumoniae_Pneumonia | Respiratory Epithelial Cytadherence and IL-8 Signaling → Apoptotic Neutrophil Macrophage Transfer |
| Bacterial_Vaginosis | Vaginolysin-Mediated Epithelial Pore Formation → Epithelial Barrier Disruption and Mucosal Immune Activation |
| Scabies | Keratinocyte and Fibroblast Cytokine Response → Dermal Leukocyte and Granulocyte Infiltration |
| G6PC3_Deficiency | Neutrophil functional defects → Crohn disease |
| Atopic_Dermatitis | TOPK-STAT3 Signaling Axis → Type 2 Immune Response; → Secondary Inflammatory Amplification |

Atopic_Dermatitis is the sole partial exception: it routes IL-8 into Th2 polarization and
IgE alongside IL-6 and IL-33 rather than to neutrophils. Nothing in the corpus routes
IL-8 to dendritic-cell activation, which is the Key Event the assay reading it out is
aligned to.

### What this says to AOP-Wiki, and what it does not

The useful claim is narrow and worth keeping narrow. dismech cannot say which Key Event an
assay should be aligned to; that is a judgement about what a cell line reports under a test
guideline. What it can say is **what the disease literature holds about the biology the
assay is named for** — and here that answer points at keratinocyte and epithelial
production feeding neutrophil recruitment, which is the KE2 compartment and its immediate
consequence, not dendritic-cell activation.

Two things follow that are worth putting to the AOP 40 authors:

- **KE 826 (Activation, Keratinocytes) has a `measurement-methodology` field, and the IL-8
  Luc assay is not in it.** If the assay's readout is in part a KE2 marker, as the review
  states, the methodology text on the Key Event is where that belongs — independently of
  which guideline the assay sits in.
- **The misalignment is a property of the edge, not of either node.** Recording it needs a
  place to say "this assay is aligned to KE3 and its readout is a KE2 marker." Neither
  AOP-Wiki's Key Event records nor dismech's node annotations can currently hold that
  sentence, which is the same gap
  [question 1](AOP_EMOD_ALIGNMENT.md#1-should-a-pathophysiology-node-be-able-to-carry-a-key-event-cross-reference)
  is about, reached from the opposite direction.

### Three caveats on the dismech side

- **The queryable signal is far thinner than the corpus mentions.** IL-8 appears in 267
  strings across 77 files in `kb/`, but only **six** of those are ontology-grounded
  descriptor bindings; 53 are evidence snippets and 50 are node descriptions. The finding
  above comes from reading prose, not from a query that could be re-run as a gate.
- **Increase is encoded three incompatible ways.** SAPHO_Syndrome and
  Spotted_Fever_Rickettsiosis bind `GO:0032637` *interleukin-8 production* with
  `modifier: INCREASED`; Chlamydia_Pneumoniae_Pneumonia binds `GO:0032757` *positive
  regulation of interleukin-8 production* with no modifier; Autoimmune_Pancreatitis states
  it in the node **name** alone, binding no process descriptor at all. All three assert the
  same thing. A filter on `modifier: INCREASED` finds two of them, a filter on the GO term
  finds one, and nothing short of reading node names finds the third.
- **The strongest-looking row is the most carefully hedged.** Autoimmune_Pancreatitis is
  the only node in `kb/` named for increased IL-8 expression, and its curator recorded
  `causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES`, `directness: INDIRECT`, and an
  explanation stating that the evidence is differential qPCR between AIP subtypes and "was
  not a chemotaxis or IL-8 blockade experiment." Do not cite it as demonstrated causation.
  Subacute_Inflammatory_Demyelinating_Polyneuropathy is hedged the same way: CSF IL-8 as a
  biomarker of blood-nerve barrier dysfunction, with the node description saying outright
  that the evidence is from GBS and CIDP and is "not SIDP-specific."

## What this case adds to the alignment project

- **The AO row reproduces the endpoint gap from both earlier pilots.** AOP 40's adverse
  outcome has no assay in the article and no dismech mechanism node; `Contact_Dermatitis`
  is the disease entry, not an organ-scale event. That is now three use cases in which the
  terminal Event is the one with nothing to attach to.
- **It is the first case where the MIE is instrumented.** The lead and liver pilots both
  found the molecular initiating event unmapped and unmeasured. Here KE1 is the most
  thoroughly assayed Event of the five, with three guideline methods plus PPRA and four
  *in silico* tools — so the absence of a node for the chemical's initiating interaction is
  a gap on the dismech side specifically, not a general property of how AOPs get measured.
- **It supplies a test for any future Key Event cross-reference slot.** A slot that can
  record "this node corresponds to KE3" must also be able to record the IL-8 case, where
  the assay's own biology sits at KE2 and the alignment is at KE3. A plain identifier
  cannot.
- **It is the first case running in the other direction.** The lead and liver pilots ask
  what an AOP can contribute to dismech. The IL-8 section asks what dismech's corpus says
  about a Key Event assignment the AOP's own review article flags as uncertain, and gets a
  usable answer. That is a second, separate reason to keep curating against AOPs, and it is
  the one that gives the collaboration something to send back upstream.

## Next steps

- [ ] Put the IL-8 KE2/KE3 question to the AOP 40 authors, together with the
      `measurement-methodology` observation on KE 826.
- [ ] Decide whether the three encodings of increased IL-8 in `kb/` should be normalised,
      and if so to which one. This is a corpus-wide question about `modifier` versus
      `positive regulation of` GO terms, not specific to IL-8.
- [ ] Check whether the same KE2/KE3 reading holds for the other TG 442E assays, which the
      article says are "also representative of the events leading up to KE3."
