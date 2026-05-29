---
title: "Pathographs: an integrative causal representation of disease mechanism for translational medicine"
target_journal: Nature Medicine (Perspective / Resource)
authors:
  - Christopher J. Mungall (LBNL, Monarch Initiative)
  - J. Harry Caufield (LBNL)
  - [co-authors TBD]
draft_status: working draft
---

## Abstract

The translational pipeline from a genetic variant or environmental exposure to
a clinical decision still depends on an implicit, expert-held model of *why* a
disease presents the way it does. That mechanistic model is rarely written
down in a form a clinician, a regulator, or an AI system can interrogate. It
is fragmented across review articles, pathway diagrams, drug labels, animal
studies, and increasingly across the outputs of new approach methodologies
(NAMs) such as organoids, iPSC-derived multicellular systems, and genome-wide
perturbation screens. The Disorder Mechanisms Knowledge Base (dismech) is a
community resource that captures this mechanistic layer as a **pathograph**:
an explicit, evidence-backed causal graph linking aetiology, pathophysiology,
phenotype, treatment, and the assays and datasets that support each claim.
Crucially, the pathograph represents what is **not** known as a first-class
object — mechanistic hypotheses with status (canonical, alternative,
emerging), competing hypothesis groups, and explicit knowledge gaps attached
to specific nodes — and is designed to interoperate with autonomous
deep-research agents such as OpenScientist that interrogate, refute, and
extend those hypotheses. We describe the design of the pathograph, illustrate
its use across Mendelian disease, complex disease, oncology, and infectious
disease, and argue that an integrative causal representation of disease
mechanism is the missing substrate for explainable clinical AI, NAM-based
regulatory science, and mechanism-aware drug repurposing.

## 1. Why an integrative mechanistic resource is needed now

Three trends are converging on the same gap. First, AI systems trained on
clinical text now exceed clinicians on certain benchmark tasks but cannot
account for *why* an answer is correct in mechanistic terms; failures are
unpredictable because the substrate is statistical rather than causal.
Second, the FDA Modernization Act 2.0 and analogous policies elsewhere have
opened the door to NAMs — organoids, microphysiological systems, iPSC-derived
multicellular models, in silico simulations — as primary evidence for human
disease, but the interpretive layer that maps a NAM readout back to a human
phenotype, a target tissue, and a therapeutic decision is still largely
ad hoc. Third, the genetic and pharmacological data layers themselves are
maturing: GWAS, rare-variant burden tests, Perturb-seq atlases, and clinical
trial registries each individually describe a slice of disease, but the joins
between them are weak.

The common shortfall is the absence of an explicit, machine-readable causal
model of the disease itself. Existing resources address adjacent problems
well — OMIM and HPO describe phenotype associations, KEGG and Reactome
describe canonical pathways, ClinVar and ClinGen describe variant
pathogenicity, DrugBank and OpenTargets describe drug-target relationships —
but none of them encode the directed chain *variant → molecular dysfunction →
cellular phenotype → tissue effect → clinical phenotype → treatment* together
with the evidence supporting each edge and the alternative chains that
competing schools of thought endorse. That chain is what a clinician
implicitly reasons over and what a regulatory reviewer wants to see when a
NAM dossier substitutes for an animal study.

Dismech provides this missing substrate. It is a curated, open knowledge base
covering several hundred disorders, structured around a pathograph data
model. It is built and maintained as a collaboration between human curators
and AI agents under deterministic validation, and is designed to plug into
both upstream evidence generators (NAMs, structured databases, deep-research
agents) and downstream applications (phenotype-driven differential diagnosis,
mechanism-guided drug repurposing, GWAS interpretation).

## 2. The pathograph as an integrative causal representation

A **pathograph** is a typed, directed graph whose nodes are biological
entities along the disease causation chain and whose edges are causal
relations supported by evidence. Six node types are first-class:

| Node type | Examples | Bound to community standards |
|---|---|---|
| Genetic factor | *FBN1* loss of function; gain-of-function variants in *FGFR3* | HGNC, gene-disease validity assertions |
| Environmental factor | UV exposure, gluten ingestion, SARS-CoV-2 infection | ECTO, MeSH |
| Pathophysiology mechanism | "Type 2 immune response", "Replication fork collapse" | GO biological process, CL cell type, UBERON |
| Biochemical state | Elevated phenylalanine; cytotoxic glutamine | ChEBI |
| Phenotype | Aortic root aneurysm, pancytopenia, dyspnea | HPO |
| Treatment | Anti-TNF biologic therapy, PARP inhibition | MAXO, NCIT, ChEBI |

Edges are directional and typed (causes, upregulates, ameliorates, is
diagnostic of). Each edge carries an evidence list in which every item must
cite a primary identifier — a PMID, DOI, NCT trial number, Orphanet entry,
ClinGen assertion ID, or NAM dataset accession — together with the verbatim
snippet supporting the claim and a classification of whether the evidence
supports, refutes, partially supports, or contradicts the claim.

This sounds simple but the consequences are non-trivial. Because the same
node type is reused across diseases, an "inflammatory bone marrow
microenvironment" node in Fanconi anemia and a similar node in
myelodysplastic syndrome become directly comparable, and the cell types and
biological processes inside them become joinable across diseases. Because
treatments are first-class nodes with `target_mechanisms` edges back to the
pathophysiology they modify, the pathograph encodes the *rationale* for a
therapy, not just an indication. Because environmental and genetic factors
are sibling node types, complex diseases (asthma, IBD, long COVID) are
modelled in the same idiom as Mendelian diseases.

We have observed that even partial pathographs change the kind of questions
that can be asked. In our Fanconi anemia entry the pathograph encodes 19
mechanism nodes connecting *FANCA/B/C/…* loss of function through replication
fork instability to bone marrow failure, hyperpigmentation, and predisposition
to specific cancers. With this graph it is straightforward to ask "which of
these phenotypes are explained by the bone-marrow-failure subgraph and which
require the genome-instability subgraph?" and to flag patient phenotypes that
are unexplained by *either*. That kind of decomposition is currently performed
implicitly by specialists; the pathograph makes it inspectable.

### 2.1 Reusing mechanism: pathograph modules

Many diseases share conserved mechanistic motifs. The fibrotic response —
tissue injury, mesenchymal cell activation, myofibroblast differentiation,
excessive ECM deposition, organ dysfunction — recurs in liver cirrhosis,
idiopathic pulmonary fibrosis, systemic sclerosis, and chronic kidney
disease. Adaptive immune resistance via checkpoint upregulation recurs across
solid tumors. Synthetic lethality between HRR deficiency and PARP inhibition
recurs across *BRCA1/2*-driven cancers.

Dismech captures these motifs as **mechanism modules**, structurally
identical to disease entries. A disease pathograph node can declare
conformance to a module node via a `conforms_to` reference; this is checked
for consistency (organ-specific specializations of cell types, expected
downstream edges) but not inherited — duplication is intentional, because
disease-specific specializations matter clinically. The current modules
include the fibrotic response, immune checkpoint blockade, HRR/FA-BRCA
synthetic lethality, RTK/GRB2 signaling adaptation, and PARP/PARG/viral
macrodomain antiviral countermeasures. Each module is itself an object of
curation and revision and can carry its own knowledge gaps and competing
hypotheses (see §3).

### 2.2 Integrating NAMs into the pathograph

NAM datasets fit naturally into the pathograph as evidence on existing
edges, as new mechanism nodes when they reveal an unappreciated process, or
as datasets attached to a hypothesis. The MorPhiC consortium produces null
alleles of human genes in iPSC-derived multicellular systems and measures
molecular and cellular phenotypes; dismech ingests these as evidence with
`evidence_source: IN_VITRO` attached to phenotype descriptors flagged as
`category: Cellular`, with a dataset accession (`morphic:GENE`) pointing back
to the primary data. The same mechanism applies to Perturb-seq atlases:
when a T-cell Perturb-seq study reports that a regulator cluster (e.g.,
IRF4/BATF/STAT3-centred Th17 differentiation) is enriched in genes from a
disease GWAS, that finding can be entered as evidence on the relevant
pathophysiology node and the corresponding edges. Organoid drug-response
studies plug into treatment nodes the same way.

The dividend is that NAM data stop being orphan readouts. A cardiomyocyte
differentiation phenotype in an *ISL1*-null iPSC system is no longer
"interesting if you happen to be reading the MorPhiC paper" — it is an
edge in the congenital heart disease pathograph, immediately neighbouring a
human clinical phenotype and a gene-disease validity assertion. Regulatory
uses of NAM data require this kind of mapping; dismech provides the
substrate.

### 2.3 Integrating genetics, drugs, and trials

Genetic basis is encoded with HGNC-bound gene identifiers, allele-level
detail where relevant, inheritance, and links to authoritative gene-disease
validity assertions (ClinGen) and dosage-sensitivity assertions. Drugs and
other medical actions are bound to MAXO and NCIT for the action and to
ChEBI/NCIT for the therapeutic agent, using a pattern that distinguishes the
medical action (e.g., pharmacotherapy) from the agent (e.g., duloxetine).
Clinical trials are first-class objects bound to ClinicalTrials.gov NCT
identifiers, with target phenotypes that connect a trial back to the
phenotype nodes it addresses. Comorbidity edges between diseases are
supported by EHR disease-trajectory data, literature, GO enrichment, and
genetic correlation, with directionality preserved where the underlying
study supports it. Each of these layers is queryable in isolation, but the
power emerges from their integration: a query for "diseases whose treatments
target the same pathophysiology module" returns mechanism-justified drug
repurposing candidates, not surface-level similarity.

## 3. First-class representation of mechanistic uncertainty

The mechanistic literature is messy. Multiple schools of thought may
co-exist for years (the amyloid cascade vs. tau-first vs. neuroinflammation
schools in Alzheimer's; the persistence vs. autoimmune vs. microclot models
in long COVID). Some claims are well established but cannot be verified to a
specific quotable source. Some questions have no answer yet. Treating these
honestly — rather than collapsing the literature into a single confident
narrative — is essential if the resource is to be trustworthy.

Dismech encodes uncertainty in four ways:

1. **Mechanistic hypotheses** are explicit objects on a disease or module,
   each with a stable `hypothesis_group_id`, a `hypothesis_label`, a status
   (CANONICAL, ALTERNATIVE, EMERGING, REFUTED), a description, and an
   evidence list. Causal edges in the pathograph can opt into one or more
   hypothesis groups via `hypothesis_groups`; a disease can therefore carry
   multiple parallel causal subgraphs that share some nodes and diverge on
   others. Alzheimer's disease currently carries amyloid cascade, tau
   neurodegeneration, neuroimmune/glial amplification, synaptic failure,
   autophagy-lysosomal clearance, vascular/BBB clearance, and HSV-1
   reactivation hypothesis groups. Long COVID currently carries persistence,
   autoimmune, microclot, mast-cell neuroimmune, and microbiome dysbiosis
   hypothesis groups. The pathograph is therefore not a single tree but a
   set of overlapping causal narratives, each independently citable.

2. **Knowledge gaps** are first-class records (`kind: KNOWLEDGE_GAP`) with a
   status (OPEN, ADDRESSED), a rationale, and `attaches_to` references that
   anchor the gap to specific pathograph nodes. A gap can also list
   `proposed_experiments`, including NAM-based experiments, that would
   resolve it. This treats "we do not yet know" as a first-class assertion,
   not an absence. It makes the resource a roadmap for *what to investigate
   next*, not just a record of what is currently believed.

3. **Evidence support classification** is required on every evidence item:
   SUPPORT, REFUTE, PARTIAL, NO_EVIDENCE, or WRONG_STATEMENT. A claim with
   only PARTIAL evidence reads differently from a claim with five SUPPORT
   citations, and refuting citations are kept on the record rather than
   silently deleted.

4. **Evidence source classification** (HUMAN_CLINICAL, MODEL_ORGANISM,
   IN_VITRO, COMPUTATIONAL, OTHER) tags what *kind* of study supports each
   claim. This matters when interpreting NAM data: an iPSC-derived
   cardiomyocyte phenotype is IN_VITRO evidence and should not be the sole
   support for a clinical phenotype claim, but it is exactly the right
   evidence type for a cellular phenotype claim.

Together, these features make dismech an honest mechanistic record. A user
can ask "which claims in this disease rest only on model-organism data?",
"which hypothesis groups are competing for which phenotypes?", and "which
open knowledge gaps could be addressed by which NAMs?" — and get answers.

## 4. Closing the loop with OpenScientist and other autonomous research agents

A mechanistic knowledge base is most useful when it is continuously
interrogated and updated against the primary literature. Static curated
reviews go stale within a year or two; the volume of relevant publications
in mechanistic disease biology exceeds what any individual curator can
track.

Dismech is designed to interoperate with autonomous research agents,
foremost among them OpenScientist, which performs multi-hour deep
investigations of a focused biomedical question with iterative search,
hypothesis refinement, and explicit citation tracking. The integration is
direct: every mechanistic hypothesis on a disease can be the subject of an
OpenScientist run, configured with the existing hypothesis YAML as the seed
claim and asked to support, refute, qualify, or compete with it against the
current literature. The output is captured as a structured report
(`openscientist.md`) alongside a per-citation index, with provider, model,
duration, and citation count recorded in the frontmatter for full
reproducibility.

We have run this loop across more than a hundred hypothesis groups spanning
neurodegenerative disease (Alzheimer's, Huntington's, ALS, Parkinson's),
metabolic disease (porphyrias, ketogenesis disorders, transaldolase
deficiency, Tangier, abetalipoproteinemia), oncology (high-grade serous
ovarian cancer POLQ resistance), infectious and post-infectious disease
(COVID-19 macrodomain biology, long COVID variants), and Mendelian
disorders (cystic fibrosis, sickle cell, hemophilia, Friedreich ataxia,
Rett syndrome, Fragile X, adrenoleukodystrophy, Gaucher, Wilson, achondroplasia).
Each run produces a citation-grounded narrative that human curators triage
into the pathograph: confirmed claims become evidence on existing edges, new
mechanism nodes capture previously unrepresented biology, and unresolved
disputes are recorded as competing hypothesis groups or as new knowledge
gaps.

This is a different relationship between an autonomous agent and a knowledge
base than is usually proposed. The agent does not write to the knowledge
base; it writes *evidence for a curator to act on*. The pathograph is the
shared object that determines which questions are worth asking — a
knowledge gap on a specific node generates a focused OpenScientist prompt
— and the place where the agent's findings are made permanent and
inspectable. Hallucinated citations and misquoted snippets, which are a
real failure mode of all current deep-research systems, are caught by
deterministic validators (§5) before reaching the knowledge base.

## 5. A note on construction: agentic curation under deterministic validation

The pathograph would not exist at its present scale (several hundred
disorders, dozens of mechanism modules, tens of thousands of evidence-backed
edges) if it had been written by hand. It is built collaboratively by domain
experts and AI agents (currently Claude and Codex via the Claude Code and
Claude Agent SDK harnesses). Agents propose new entries, enrich existing
ones, and respond to compliance scoring that identifies the lowest-coverage
files in the repository.

The integrity of the resource does not depend on the integrity of the
agents. It depends on three deterministic validation layers — a schema
validator, an ontology term validator that checks every identifier against
the authoritative ontology, and a reference validator that requires every
evidence snippet to be a verbatim substring of a cached primary source —
that block agent errors at the pull-request boundary. The validators are
not AI; they are mechanical and reproducible. Every change passes through
GitHub-based review and CI, and an automated AI reviewer (Claude) performs a
second pass focused on dismech-specific curation guidelines. Reference
caches and ontology snapshots are version-controlled so that any validation
result can be reproduced. Section 5 of the companion methodology paper
describes this stack in detail.

For the purposes of this paper, the relevant points are: (i) the resource
exists at a scale that would not be achievable by manual curation alone;
(ii) the AI-assisted construction does not compromise verifiability,
because every claim is bound to a primary identifier and an exact quotable
snippet, and the cache is checked at every CI run; and (iii) the explicit
representation of competing hypotheses and knowledge gaps means the resource
does not pretend to be more certain than the literature warrants.

The encoding details — that disease entries are YAML, validated against a
LinkML schema, with ontology bindings to HPO, GO, CL, UBERON, MONDO, MAXO,
CHEBI, NCIT, HGNC, and GENO — are deliberately invisible to most users.
What matters at the resource level is conformance to community standards:
dismech reuses identifiers that the rest of biomedicine already uses, and
exports to Biolink Model KGX so that the pathograph can be consumed by
existing knowledge-graph infrastructure (Monarch KG, NCATS Translator).

## 6. Applications

### 6.1 Mechanism-aware differential diagnosis

A phenotype-driven differential is the standard query against HPO-annotated
disease databases. Pathograph-aware matching adds two things. First,
phenotype frequency on a per-genotype basis means that excluded phenotypes
are honored: pancytopenia is very frequent in Fanconi anemia overall but
explicitly excluded in *FANCD1/BRCA2* and FA-S/*BRCA1* subtypes, and a
phenomatcher that respects this returns a different ranked list than one
that does not. Second, when a patient phenotype is not on the candidate
disease's phenotype list, the pathograph permits a *mechanistic* answer to
the question "is this consistent?". Fever in a Fanconi case is not a
primary FA phenotype, but the bone-marrow-failure → neutropenia → infection
susceptibility subgraph is right there to support it. Our phenomatcher
pipeline takes a GA4GH Phenopacket, performs ontology-aware matching,
weights by curated frequency, and uses the pathograph to generate
explanations for non-exact matches. The output is a probability estimate
with a per-phenotype explanation chain, not a black-box score.

### 6.2 Mechanism-guided drug repurposing

Pathograph treatments are bound to the mechanisms they target. Two diseases
whose pathographs share a mechanism module are immediate repurposing
candidates for therapies that target that module — and crucially, the
shared module identifies *which* therapies. The fibrotic response module is
the most developed example: it predicts that anti-fibrotic agents validated
in IPF should be considered in hepatic, renal, and cutaneous fibrosis with
the same mechanistic rationale; the pathograph makes this rationale
explicit and citable rather than analogical. The immune checkpoint blockade
module similarly explains why a checkpoint inhibitor active in one solid
tumor is a candidate in another with the same adaptive-immune-resistance
node, and conversely why diseases lacking that node are not.

### 6.3 GWAS and Perturb-seq interpretation

Pathographs are a natural validation layer for computational pipelines that
propose gene → program → trait relationships. We have used dismech to
validate output from causal-graph methods that combine GWAS with
Perturb-seq, classifying each gene → program → trait triple as CONFIRMED
(all three documented and connected in dismech), PARTIAL (some elements
present but incomplete chain), NOVEL (not in dismech — a curation
candidate), or CONTRADICTED (dismech documents an opposite effect). The
loop is bidirectional: pipeline-flagged novel candidates feed prioritized
curation; the resulting curation supports the next round of pipeline
validation. This is the same loop we use for OpenScientist (§4), with a
different upstream evidence generator.

### 6.4 NAMs and regulatory science

A mechanistic pathograph is the bridge between a NAM readout and a
regulatory or clinical decision. When an iPSC-derived disease model
recapitulates a cellular phenotype, the pathograph says which clinical
phenotype it is upstream of and via what mechanism — and which clinical
phenotypes it does *not* address. When an organoid drug screen identifies a
candidate, the pathograph identifies which mechanism node it targets and
which other diseases share that node. When a NAM dataset diverges from a
human clinical observation, the pathograph localizes the divergence to a
specific edge, generating a hypothesis-shaped follow-up rather than a
diffuse failure. We see this as the most consequential medium-term
application: the bottleneck in NAM adoption is not the assays themselves
but the interpretive infrastructure, and an open, citable, integrative
causal model is that infrastructure.

### 6.5 Clinical AI grounding

LLM-based clinical assistants are increasingly being deployed in diagnostic
and therapeutic decision support, but they fail in modes that are difficult
to predict and difficult to audit. A pathograph provides a substrate for
**explainable, ontology-grounded** answers: every assertion is bound to a
primary identifier and an exact snippet, and the causal chain is traversable
rather than implicit. When a clinical AI proposes that a patient's symptom
is explained by a particular mechanism, the pathograph either supports that
chain end-to-end with citations or does not — and the failure mode is
visible. We do not claim dismech is ready for direct clinical deployment;
we claim it is the kind of substrate that *would* make such deployment
auditable.

## 7. Limitations and an honest roadmap

Dismech is incomplete: its current ~500 disorder entries are a small
fraction of the Mondo disease space, the depth of curation varies widely
across entries, and the mechanism modules are early. Some entries depend
heavily on review-article evidence rather than primary studies because
suitable quotable abstracts could not be located; we mark these honestly
rather than fabricating support. Knowledge gaps are themselves under-curated
— there are many more open gaps than the ones currently recorded. The
balance between hypothesis groupings and a single canonical narrative is an
ongoing editorial decision that varies by disease. Snippets are limited to
publication abstracts and structured-database fields, which restricts
mechanistic detail; full-text-aware evidence is on the roadmap. Coverage of
NAM datasets is currently limited to a handful of consortium outputs
(MorPhiC anchor genes, selected Perturb-seq atlases); systematic ingestion
of NAM dataset catalogs is a priority. Coverage of pediatric and rare
disease is stronger than coverage of common chronic disease, where the
mechanistic literature is broader and the editorial choices harder.

We are publishing dismech now, openly and explicitly as a work in progress,
because the integrative causal layer is needed *now* by the communities
deploying NAMs, by GWAS/Perturb-seq pipelines that need a mechanistic
validation substrate, by mechanism-aware drug repurposing programs, and by
auditable clinical AI. The pathograph data model and the validation stack
are mature; the content is growing.

## 8. Conclusion

The translational pipeline needs an explicit, evidence-backed, integrative
causal representation of disease mechanism — one that brings together
genetics, environmental exposures, pathophysiology, NAM readouts, drugs,
trials, and the assays and datasets that support each claim, and that
encodes mechanistic uncertainty honestly as competing hypotheses and open
knowledge gaps. Dismech is our attempt at that representation. It is
designed to be the substrate that autonomous research agents
investigate, that NAM dossiers map back onto, that mechanism-aware
repurposing draws from, and that clinical AI can be grounded against. The
pathograph is open, citable, and improving; we invite the community to
interrogate, extend, and challenge it.

## Data and code availability

Knowledge base: <https://github.com/monarch-initiative/dismech>.
Browsable resource: <https://monarch-initiative.github.io/dismech/>.
All disorder entries, mechanism modules, schema, validation tooling, and
reference caches are version-controlled and openly licensed.

## Acknowledgements

Monarch Initiative; LBNL Environmental Genomics & Systems Biology; the
broader OBO Foundry, HPO, MONDO, MAXO, CL, GO, and UBERON development teams;
ClinGen; Orphanet/Orphadata; ClinicalTrials.gov; the MorPhiC Consortium; and
the OpenScientist development team. Funded by [TBD].
