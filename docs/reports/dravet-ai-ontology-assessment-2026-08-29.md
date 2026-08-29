# The DSF-funded AI-powered Dravet Syndrome Ontology: assessment and relevance to dismech (2026-08-29)

**Subject.** *Development of an AI-powered Dravet Syndrome Ontology* — a Dravet Syndrome
Foundation (DSF) Special Collaborative Research Project, $240,000 over 2 years, announced
2023-03-03. PIs: **Satya S. Sahoo** (Case Western Reserve University) and **Jeffrey
Buchhalter** (University of Calgary).
[Grant page](https://dravetfoundation.org/development-of-an-ai-powered-dravet-syndrome-ontology/) ·
[announcement](https://dravetfoundation.org/dsf-supports-the-development-of-an-ai-powered-dravet-ontology/).

**Why this document exists.** The grant page is a one-paragraph summary, but the project has
since published. This note reads the *outputs* rather than the blurb, and asks one question:
what does an expert-curated Dravet OWL ontology change for dismech, which already holds a
2,800-line `Dravet_syndrome` entry?

**Bottom line.** The two resources are **complementary, not competing, and the boundary is
clean**: they are building a *terminology* (an OWL class hierarchy of DS concepts, released
on BioPortal, used to condition LLM prompts); dismech is an *assertional* KB (evidence-anchored
causal claims about a named disease). Their ontology is a candidate **term source** for
dismech's epilepsy entries in the way HP and MONDO already are. It is not a source of
mechanism claims, and nothing in it substitutes for a verified snippet.

The one place the two projects genuinely converge is the **preclinical-model ↔ human
mapping**, which is the explicit motivation of the grant ("determine where there is
similarities and differences between model systems and humans") and the payload of their
2025 drug-efficacy paper. dismech has first-class schema for exactly that
(`animal_models[].modeled_mechanisms`, `fidelity`, `FAILS_TO_RECAPITULATE`,
`HUMAN_MODEL_MISMATCH`) — and dismech's own Dravet entry does not use it (§4).

Nothing here modifies a KB entry, schema file, or cache.

---

## 1. What the grant proposed

From the DSF pages, verbatim in substance:

- DS has abundant data across model organisms and humans, in repositories and literature,
  and existing integration methods "are limited in scale and functionality."
- The team had already combined an **epilepsy ontology with machine learning to classify
  epilepsy neuropathology data** at high accuracy — the cited precedent (§2.1).
- The proposal: **extend that epilepsy ontology for Dravet syndrome**, so ML can
  automatically index clinical literature and support analysis of basic-science data.
- The 2023 announcement adds the design intent: the DS ontology "would build off of the
  existing Epilepsy Ontology previously developed by Dr. Sahoo," adding DS-specific terms
  **plus terms from animal and cell models**, built with a working group of DS basic
  scientists and clinicians, and released publicly.

Buchhalter's stated interest is SUDEP — which matters, because SUDEP is where dismech's
Dravet entry is deepest (§4).

## 2. What actually shipped

### 2.1 The precedent: EpSO + ML on neuropathology

The "epilepsy ontology" of the grant text is Sahoo's **Epilepsy and Seizure Ontology
(EpSO)**, an OWL application ontology built on a four-dimensional epilepsy classification
aligned to ILAE terminology and NINDS common data elements
([PMID:23686934](https://pubmed.ncbi.nlm.nih.gov/23686934/), *JAMIA* 2014,
[doi:10.1136/amiajnl-2013-001696](https://doi.org/10.1136/amiajnl-2013-001696)).

The neuropathology result the grant leans on is
[PMID:36371527](https://pubmed.ncbi.nlm.nih.gov/36371527/) (*Sci Rep* 2022,
[doi:10.1038/s41598-022-23101-3](https://doi.org/10.1038/s41598-022-23101-3)): 312 epilepsy
surgery patients from the German Neuropathology Reference Center, with diagnosis, microscopy,
immunohistochemistry, anatomy, etiology and imaging findings modeled in EpSO and used as
engineered features. Reported effect: substantially improved diagnostic accuracy and a large
runtime reduction versus non-ontology features.

**Naming caution.** "The Epilepsy Ontology" also names a *different*, community-built
artifact from a different group ([PMID:37016683](https://pubmed.ncbi.nlm.nih.gov/37016683/),
*Bioinformatics Advances* 2023). The DSF page's unqualified "epilepsy ontology" means EpSO.
Do not conflate them when citing.

### 2.2 The DS ontology itself

[PMID:42428123](https://pubmed.ncbi.nlm.nih.gov/42428123/) — Golnari P, Prantzalos K,
Upadhyaya DP, Buchhalter J, Sahoo SS. *Developing a Specialized Dravet Syndrome Ontology for
Rare Disease Informatics and AI Applications.* medRxiv, 2026-07-04
([doi:10.64898/2026.07.01.26357055](https://doi.org/10.64898/2026.07.01.26357055),
PMC13345437).

What the abstract states:

- The DS ontology is an **expert-guided specialization of the previously published epilepsy
  ontology**, curated in OWL.
- Scope was set by a **scientific advisory board** with structured review meetings and
  iterative curation.
- DS content was reorganized across **nine major domains** — seizures, development, behavior,
  SUDEP/autonomic risk, genetics, comorbidities, electrophysiology, pharmacology, and drug
  responsiveness.
- It grew the **publicly released BioPortal version** beyond the pre-extension baseline.
- Evaluation was by expert-guided curation plus **downstream task-based reuse**: two published
  ontology-enabled LLM studies, and an in-progress DS knowledge graph and AI assistant.

The abstract does not give class counts, an IRI, or a licence, and I did not retrieve the
full text or the BioPortal record (§6).

### 2.3 The downstream LLM studies

[PMID:40311258](https://pubmed.ncbi.nlm.nih.gov/40311258/) — *Ontology accelerates few-shot
learning capability of large language model: A study in extraction of drug efficacy in a rare
pediatric epilepsy.* *Int J Med Inform* 2025;201:105942
([doi:10.1016/j.ijmedinf.2025.105942](https://doi.org/10.1016/j.ijmedinf.2025.105942)).

This is the one to read. It is also the one with the largest dismech-shaped author list —
DSF staff (Hood, Meskis) alongside Isom, Wilcox, Parent, Lal, Lhatoo, Wirrell, Knupp,
Sullivan, and Fureman.

- **The benchmark is a preclinical-model ↔ human efficacy table**: 17 antiseizure medications
  tested *both* in DS preclinical models and in DS patients.
- Method: ontology-augmented **phased in-context learning** over 4,935 full-text DS articles.
- Result: with the DS ontology in the prompt, Gemini 1.0 Pro reproduced the benchmark at
  reported 100% accuracy from **two** in-context examples.
- Extension: 7 further seizure-reducing drugs, analyzed to **identify knowledge gaps for
  designing new experiments**.

[PMID:40775940](https://pubmed.ncbi.nlm.nih.gov/40775940/) (*Stud Health Technol Inform*
2025) is the companion methods note on using ontologies to embed expert input into LLMs.

The "identify where key information is missing" framing in the DSF announcement is therefore
implemented, and it is implemented at the drug × model-system × human-outcome grain.

## 3. How this relates to dismech

The projects answer different questions, and the difference is the usual terminology /
assertion split:

| | DS ontology (CWRU) | dismech |
|---|---|---|
| Primary artifact | OWL class hierarchy, released on BioPortal | LinkML-validated YAML entries, one per disease |
| What a node is | a **class** — a kind of seizure, drug, comorbidity | a **claim** — a mechanism node in a named disease's pathograph |
| What an edge is | a subsumption or object-property axiom | a causal assertion with directness and evidence |
| Evidence | not the artifact's job | required: PMID + exact verified snippet + `evidence_source` |
| Scope | epilepsy/DS, deep | 2,476 diseases, cross-domain |
| Consumption | conditions LLM prompts; features for ML | rendered pages, KGX/CX2 export, pathographs |

Three practical consequences:

1. **It is a term-source candidate, not a content source.** If DS-specific concepts that
   HP/MONDO/GO lack are given stable IRIs there, that is the kind of gap dismech's ontology
   contract cares about. It would need an OAK adapter and a `cache/enums/` membership cache
   before any binding, and per `.claude/skills/dismech-terms`, *no term beats a bad one* —
   a BioPortal-only application ontology is a weaker anchor than an OBO-library term and
   should not displace one that already fits.
2. **Their drug-efficacy benchmark is directly comparable to dismech treatment records.**
   17 ASMs with paired preclinical and human outcomes is precisely a `treatments[]` ×
   `animal_models[].modeled_mechanisms` join. Their table is a cross-check on ours, in both
   directions.
3. **Their gap analysis and dismech's `discussions` do the same job by different means** —
   theirs by LLM extraction over 4,935 papers, ours by curator-written `KNOWLEDGE_GAP` /
   `HUMAN_MODEL_MISMATCH` records anchored to specific pathograph nodes. Ours are auditable
   and node-anchored; theirs have recall we cannot match by hand.

## 4. What dismech's Dravet entry holds, and what this exposes

`kb/disorders/Dravet_syndrome.yaml` (2,801 lines, created 2025-12-04) currently carries:

- `disease_term` MONDO:0100135, an ORPHA:33069 `external_assertions` record
- 5 pathophysiology nodes: SCN1A Gene Mutation → Neuronal Hyperexcitability, plus
  Postictal Serotonergic Neuron Dysfunction, Impaired CO2 Chemoreception and Postictal
  Hypoventilation, Astrocyte Dysregulation
- 2 `mechanistic_hypotheses`: a `CANONICAL` seizure-burden model of SUDEP risk and an
  `EMERGING` serotonergic chemoreflex-failure model
- 50 phenotypes, 11 genetic records, 11 treatments (incl. zorevunersen/STK-001 with full
  `aso_details`, and ETX101 gene therapy), 5 `discussions`, 4 datasets

That is a strong SUDEP-side entry — which is notable given Buchhalter's SUDEP focus, and it
already covers the serotonergic/chemoreception axis their nine-domain "SUDEP/autonomic risk"
bucket names.

Reading their nine domains against the file exposes five concrete, low-argument gaps:

| Gap | Detail |
|---|---|
| **No `animal_models:` block at all** | The entry carries a `HUMAN_MODEL_MISMATCH` discussion *about* `Scn1a+/-` background dependence, but no model record for the mouse it discusses. 539 of 2,476 dismech disorders have `animal_models`; the flagship DS entry is not one of them. This is the single largest gap, and it is the exact axis the grant is about. |
| **No `experimental_models:`** | Three of the four cited datasets are iPSC/organoid (`geo:GSE256142`, `geo:GSE111436`, `geo:GSE274660`) — the NAM systems are cited as data but not modeled as systems. |
| **`progression` has one phase** | Only `Onset`. The canonical DS course (febrile/diagnostic stage → worsening stage → stabilization/plateau) is not represented, and their "development" domain is built on it. |
| **5 of 11 treatments lack `therapeutic_modality`** | `Antiepileptic Medications`, `Supportive Therapies`, `Cannabidiol`, `Fenfluramine`, `Stiripentol`. Cannabidiol, fenfluramine and stiripentol are the three DS-approved agents, so these are the records their pharmacology and drug-responsiveness domains would key on. |
| **No structured epilepsy-syndrome classification** | `classifications` holds only Harrison's chapters. ILAE syndrome classification appears only as free text, in 23 KB files (21 of them disorders), and has no dedicated `classifications` slot. EpSO is built on the ILAE axes, so this is where their structure is most obviously ahead of ours. |

## 5. Recommendations

Ranked, and none of them urgent:

1. **Curate `animal_models` for `Dravet_syndrome`.** The `Scn1a+/-` mouse, the *scn1lab*
   zebrafish, and the conditional interneuron-specific knockouts, each with
   `modeled_mechanisms` links to the existing pathophysiology nodes, explicit `fidelity`, and
   `limitations`. The existing `HUMAN_MODEL_MISMATCH` discussion gives the honest fidelity
   language for free. This is worth doing on its own merits and makes any later comparison
   against their benchmark mechanical rather than manual.
2. **Cross-check the 17-ASM benchmark against dismech treatments** once the full text is in
   hand. Agreement is reassuring; disagreement is a finding for either side.
3. **Fill the five missing `therapeutic_modality` values** and extend `progression` to the
   three-stage course. Both are small, both are independently correct.
4. **Watch for the BioPortal release and the promised knowledge graph.** If the KG is
   published in a graph format, a node-level comparison against dismech's DS pathograph is a
   genuinely informative exercise — and the closest external analogue to the PhysioMap
   comparison in `docs/reports/physiomap-assessment-2026-08-23.md`.
5. **Do not open an ILAE `classifications` slot on the strength of this alone.** It is a
   schema addition with KB-wide consequences across 79 epilepsy-family entries; it belongs in
   `docs/explanation/design-decisions.md` as a proposal, not in a report's recommendation
   list.

Contact is plausible and cheap: DSF staff are co-authors on the IJMI paper, the resource is
explicitly meant to be publicly available, and dismech has DS content they would have had to
extract.

## 6. What I did not verify

- **The full text of the medRxiv preprint.** All §2.2 claims are from the abstract. Class
  counts, IRIs, licence, and the BioPortal acronym are unread.
- **The BioPortal record.** The BioPortal API requires a key; I did not query it, and I make
  no claim about which acronym the DS ontology is released under or whether EpSO and the DS
  extension are separate submissions.
- **The IJMI full text**, including the composition of the 17-ASM benchmark and the identity
  of the 7 extension drugs. The §5 item 2 cross-check is therefore proposed, not done.
- **Project status.** The DSF pages date the award to March 2023 for two years; the 2026
  preprint and a reported AES 2025 presentation indicate the work continued past that window.
  I did not establish current funding status.
- **Nothing in this note is evidence.** No claim here has been through
  `just validate-references`, and none of it should be copied into a KB `snippet:` without
  going through the normal reference workflow.
