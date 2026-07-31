---
title: "DisMech: computable pathographs for disease mechanisms, knowledge gaps, and translational reasoning"
target_journal: "TBD"
authors:
  - "J. Harry Caufield"
  - "Kevin Schaper"
  - "Evan Connelly"
  - "Nico Matentzoglu"
  - "Justin Reese"
  - "Corey Cox"
  - "Katie Mullen"
  - "Nomi Harris"
  - "Sierra Moxon"
  - "Sujay Patil"
  - "Vibhor Gupta"
  - "Jim Balhoff"
  - "Mark A. Miller"
  - "Sarah Gehrke"
  - "Aleix Puig"
  - "Kendall Flaharty"
  - "Shawn T. O'Neil"
  - "Aaron Odell"
  - "Shilpa Sundar"
  - "Marcin P. Joachimiak"
  - "Anne Thessen"
  - "Melissa Haendel"
  - "Christopher J. Mungall"
draft_status: "integrated working draft"
source_material:
  - "Google Doc: DisMech manuscript - Data Resource"
  - "Recovered pathograph manuscript from commit f858a0c43d"
  - "TMC AI keynote, Zenodo 18720444"
  - "CERSI/FDA surrogate-endpoint presentation, Zenodo 20682988"
---

<!--
This revision combines the consortium Data Resource manuscript with the
pathograph/translational draft. It deliberately leaves empirical results and
citations marked where a frozen-release analysis or evaluation is still
required. Do not convert provisional working-snapshot counts into publication
claims until the analysis script and release identifier are committed.
-->

# Abstract

Most knowledge of how a molecular lesion or exposure produces a human disease
phenotype remains distributed across narrative reviews, primary studies,
clinical resources, and model-system reports. These sources are individually
valuable but do not provide a shared, computable account of the causal steps
connecting aetiology, pathophysiology, clinical outcomes, and treatment.
DisMech is an open, mechanism-centred knowledge resource that represents these
accounts as **pathographs**: typed, directed graphs whose nodes and edges are
grounded in community ontologies and linked to provenance-bearing evidence.
Pathographs preserve competing mechanistic hypotheses, identify explicit
knowledge gaps and human/model mismatches, and record experiments proposed to
resolve them. DisMech is maintained through a hybrid curation workflow in
which human curators direct language-model agents while schema, ontology, and
reference validators provide reproducible quality-control gates. Here we
describe the resource, quantify its content and evidentiary structure, and
evaluate whether access to pathographs improves pathophysiological reasoning.
We further show how a disease mechanism graph can connect new approach
methodology readouts to candidate surrogate endpoints and unresolved
organ-specific outcomes. DisMech provides an inspectable substrate for
mechanistic diagnosis, evidence-gap discovery, translational model selection,
and auditable biomedical AI.

# Introduction

Most of what is known about human disease mechanism is written as prose.
Textbooks, review articles, and primary studies describe how molecular events
propagate through cells and tissues to produce signs, symptoms, and clinical
course. This literature is authoritative, but it is not directly computable.
A researcher who wants to compare a mechanism across diseases, determine
which phenotype is downstream of a treatment target, or identify where a
model system fails to explain a human outcome must repeatedly reconstruct
causal models that domain experts already hold implicitly.

Existing biomedical resources solve important adjacent problems. OMIM and the
Human Phenotype Ontology capture disease–phenotype associations; ClinVar and
ClinGen represent variant and gene–disease evidence; Reactome and KEGG
represent biological pathways; and drug resources connect compounds to
targets and indications [CITE]. What remains uncommon is a disease-centred
representation of the complete explanatory chain:

> aetiology → molecular dysfunction → cellular process → tissue pathology →
> clinical phenotype → treatment response

The missing intermediates matter. Diseases that resemble one another
phenotypically may arise through different causal processes and require
different interventions. Conversely, diseases assigned to different clinical
categories may share a pathological process that creates a common therapeutic
vulnerability. A mechanistic representation must also preserve uncertainty:
several causal accounts may coexist, evidence may support different branches,
and the most useful statement may be that a particular edge remains unknown.

This need is becoming more acute as new approach methodologies (NAMs),
including patient-derived cells, organoids, organs-on-chips, and
high-throughput perturbation systems, are used to study disease and support
drug development. A NAM readout is not self-interpreting. Its translational
meaning depends on which part of a human disease mechanism it recapitulates,
which clinical outcome lies downstream, and which organ-specific branches it
does not test. The same problem arises for surrogate endpoints: association
between a biomarker and an outcome is not equivalent to a mechanistic account
of why treatment-induced change in the biomarker should predict clinical
benefit.

Large language models and agentic systems make it possible to assemble
structured biomedical content at a scale that was previously impractical, but
they also introduce fabricated citations, invented identifiers, semantic
misgrounding, and confidently stated unsupported claims. The relevant
question is therefore not whether an agent can generate a disease summary,
but whether agent-assisted curation can produce a resource whose claims,
uncertainties, and provenance remain inspectable.

We address these linked problems with DisMech, the Disorder Mechanisms
Knowledge Base. Each DisMech entry is a structured disease model containing a
pathograph, phenotypes, genetic and environmental factors, biochemical
findings, treatments, experimental models, datasets, and evidence. Reusable
mechanism modules capture conserved pathological motifs across diseases.
Mechanistic hypotheses label alternative or superimposed causal subgraphs,
while discussion objects record knowledge gaps, controversies, and
human/model mismatches attached to particular nodes or edges. The resource is
openly versioned and rendered for both human browsing and computational use.

Here we present DisMech primarily as a biomedical data resource. We describe
its data model and curation governance, characterize its current content and
evidence structure, examine its representation of mechanistic uncertainty,
and define an evaluation of pathophysiological reasoning with and without
pathograph context. We use the relationship between Fabry disease mechanisms,
surrogate endpoints, and patient-derived cellular models as a translational
case study. A companion manuscript describes the agentic curation and
validation architecture in depth.

# Results

## Pathographs make disease explanations computable

A pathograph is a typed, directed graph whose nodes represent states or
processes on a disease-causation chain and whose edges represent established
or hypothesized causal relationships. DisMech stores the graph alongside the
other parts of a disease record rather than treating it as an isolated pathway
diagram. This allows a mechanism node to connect directly to a phenotype,
treatment, biomarker, experimental model, or explicit knowledge gap.

**Figure 1 | DisMech and the pathograph data model.** The central Disease
object connects genetic and environmental aetiology to pathophysiology,
biochemical states, phenotypes, treatments, surrogate endpoints, datasets,
and experimental models. Typed causal edges form the pathograph. Evidence
items, mechanistic hypotheses, and discussions attach to the claims they
qualify. *[FIGURE TO GENERATE FROM THE CURRENT SCHEMA]*

**Table 1 | Core pathograph objects and ontology grounding.**

| Object | Example | Principal standards |
|---|---|---|
| Disease | Fabry disease | MONDO, Orphanet |
| Genetic factor | *GLA* loss of function | HGNC, ClinGen, GENO |
| Environmental factor | ultraviolet exposure | ECTO or other mapped vocabularies |
| Pathophysiology | lysosomal glycosphingolipid accumulation | GO, CL, UBERON |
| Biochemical state | elevated phenylalanine | ChEBI, LOINC |
| Phenotype | renal insufficiency | HPO |
| Treatment | enzyme replacement therapy | MAXO, NCIT, ChEBI |
| Experimental model | patient-derived iPSC cardiomyocyte | NAMO and source dataset |
| Surrogate endpoint | renal peritubular-capillary GL-3 clearance | FDA source table and assay metadata |
| Knowledge gap | uncertain cardiac surrogacy | Discussion attached to a graph branch |

Causal edges can carry evidence specific to the source–target relationship,
while nodes carry evidence for the state or process itself. This distinction
is important: evidence that a process occurs in a disease does not
automatically establish that it causes a particular downstream phenotype.
The current resource has substantially higher node-level than edge-specific
evidence coverage, making edge-level provenance a measurable curation target
rather than an assumed property of every pathograph.

## DisMech spans diseases, reusable mechanisms, and evidence types

The publication analysis will be run against a frozen DisMech release. A
preliminary inventory of the working tree on 29 July 2026 found the following
content; these numbers are included here to define the analysis, not as final
publication values.

**Table 2 | Preliminary working-snapshot inventory.**

| Object | Count |
|---|---:|
| Disorder files | 1,635 |
| Mechanism modules | 118 |
| Groupings | 48 |
| Pathophysiology nodes, disorders and modules | 9,114 |
| Causal edges, disorders and modules | 17,912 |
| Phenotypes, disorders and modules | 17,314 |
| Treatments, disorders and modules | 6,372 |
| Evidence items, disorders and modules | 79,862 |
| Mechanistic hypotheses, disorders and modules | 360 |
| Discussions, disorders and modules | 656 |
| Reference-cache records | 31,623 |

Nearly all disorder files contain pathophysiology and phenotype content, but
the resource is intentionally heterogeneous in depth. The frozen-release
analysis will report distributions rather than totals alone: nodes and edges
per disease, connected components, cross-scale transitions, ontology
coverage, evidence-source composition, treatment-to-mechanism links, and
coverage by disease class. It will also report explicit denominators such as
the relevant MONDO or Orphanet disease space.

**Figure 2 | Scope and depth of DisMech.** Proposed panels: disorders by
clinical/mechanistic class; distributions of pathograph nodes and edges per
disease; evidence items by source type; edge-specific evidence coverage; and
mechanism-module conformance. *[ANALYSIS AND FIGURE REQUIRED]*

## Mechanism modules expose shared pathological motifs

Mechanism modules represent conserved motifs such as fibrosis, amyloid
formation, thrombogenesis, lysosomal substrate accumulation, immune
checkpoint blockade, and cardiac-ion-channel dysfunction. A module has the
same structural form as a disease entry. Disease-specific nodes declare
`conforms_to` relationships to module nodes while retaining organ-, cell-,
gene-, and disease-specific detail.

Conformance is not inheritance. A hepatic stellate-cell activation node and a
pulmonary fibroblast activation node may both conform to a generic
mesenchymal-cell-activation step in the fibrotic-response module, but the
disease records duplicate and specialize the relevant content. This design
allows module consistency to be checked without erasing clinically meaningful
context.

The frozen-release analysis will quantify how often modules are reused,
whether conforming disease subgraphs preserve expected processes and edges,
and which high-frequency motifs remain unrepresented. This converts mechanism
modules from illustrative examples into an evaluated cross-disease layer.

## DisMech represents uncertainty rather than collapsing it

Pathophysiological literature rarely supports a single uncontested graph.
DisMech represents four complementary forms of epistemic qualification.

First, mechanistic hypotheses organize edges into canonical, alternative,
emerging, or deprecated explanatory models. Several hypotheses may share
upstream nodes and diverge only at a contested causal step. Second, evidence
items classify whether a source supports, partially supports, refutes, or
fails to provide evidence for a claim. Third, evidence-source typing
distinguishes human clinical, model-organism, in vitro, computational, and
other evidence. Fourth, discussion objects record open questions,
controversies, interpretations, knowledge gaps, and human/model mismatches.

This representation makes uncertainty queryable. A user can ask which edges
rest only on model-system evidence, where two hypotheses diverge, or which
clinical outcome lacks a mechanistic bridge from an experimentally measured
biomarker.

## Knowledge gaps become research objects

A knowledge gap in DisMech is not free-floating prose. It has a stable
identifier, a prompt, a lifecycle status, a rationale, and an `attaches_to`
pointer identifying the disease object, node, or edge to which the gap
applies. It may also include proposed experiments and supporting evidence.
Human/model mismatch is represented separately from general absence of
evidence: some evidence exists, but its fidelity to human biology is the
unresolved question.

The preliminary working snapshot contains 447 `KNOWLEDGE_GAP` discussions,
112 `HUMAN_MODEL_MISMATCH` discussions, and 375 proposed experiments. The
publication analysis will classify these gaps by biological scale, evidence
source, disease class, graph position, and proposed experimental modality.
It will also distinguish unresolved gaps from resolved or archived
discussions and test whether automated literature and knowledge-gap scans
preferentially identify particular gap classes.

**Figure 3 | The anatomy of a mechanistic knowledge gap.** Proposed panels:
gap typology; graph positions at which gaps occur; evidence-source deficits;
human/model mismatches by tissue or cell type; and proposed experiments by
modality. *[ANALYSIS AND FIGURE REQUIRED]*

## Fabry disease connects mechanism, surrogate endpoints, and NAMs

Fabry disease illustrates why surrogate-endpoint reasoning requires an
explicit disease mechanism. Pathogenic *GLA* variants reduce
alpha-galactosidase A activity, producing lysosomal accumulation of
globotriaosylceramide (GL-3) and related glycosphingolipids. That upstream
storage process branches into renal, cardiac, vascular, and neurological
pathology.

The FDA surrogate-endpoint table records clearance of GL-3 from renal
peritubular capillaries as an endpoint used in support of drug approval
[CITE FDA SOURCE]. The pathograph places this measurement on one renal branch
of a multi-organ mechanism. It therefore makes two propositions inspectable:
the endpoint is mechanistically proximal to enzyme replacement and substrate
clearance, but it is not a direct measurement of podocyte, cardiomyocyte, or
dorsal-root-ganglion outcomes. A response in renal capillary endothelium
cannot simply be assumed to establish benefit in each parallel tissue branch.

This localization identifies a concrete knowledge gap: which treatment-
responsive cellular readout best bridges substrate clearance to cardiac
outcomes? Patient-derived iPSCs differentiated into cardiomyocytes and other
relevant lineages could test enzyme uptake, GL-3 clearance,
electrophysiological effects, hypertrophic response, and drug response in
cells carrying the same patient genotype. The experiment would not by itself
validate a clinical surrogate, but it would supply evidence on the presently
weak mechanistic bridge.

**Figure 4 | Fabry disease mechanism-to-endpoint map.** *GLA* deficiency and
GL-3 accumulation branch to renal, cardiac, and neurological outcomes. The
FDA renal peritubular-capillary endpoint and candidate iPSC cardiomyocyte
readouts are localized to the branches they test. Unsupported extrapolations
are shown as explicit gaps. *[FIGURE AND PRIMARY EVIDENCE REQUIRED]*

## Pathographs provide a substrate for pathophysiological reasoning

The central evaluation asks whether explicit pathograph context improves
reasoning rather than merely supplying more text. The evaluation set will
sample diseases and mechanism modules across genetic, complex, infectious,
neoplastic, and environmental categories. Each item will be derived from
curated graph structure but withheld from the model context used for the
test.

Tasks will include:

1. Explain why a phenotype follows from a molecular lesion.
2. Distinguish two diseases with similar phenotype profiles but different
   causal mechanisms.
3. Identify a patient feature not explained by a candidate pathograph.
4. Predict which outcomes should respond to perturbation of a treatment
   target.
5. Distinguish canonical, alternative, and emerging causal accounts.
6. Identify where human evidence ends and model-system extrapolation begins.
7. Select an experiment that addresses an attached knowledge gap.
8. Judge whether a biomarker is upstream of, parallel to, or disconnected
   from a clinical outcome.

The same reasoner will be tested with no resource context, with conventional
disease-summary context, and with a structured DisMech pathograph and its
evidence. Blinded domain experts will score biological correctness,
faithfulness to the supplied path, unsupported-claim rate, recognition of
uncertainty, and usefulness of the explanation. Deterministic graph-traversal
questions will provide a separate machine-scored subset.

**Table 3 | Pathophysiological-reasoning evaluation.** *[REPORT TASK COUNTS,
DISEASE STRATA, HUMAN RATERS, AGREEMENT, MODEL CONDITIONS, EFFECT SIZES, AND
CONFIDENCE INTERVALS]*

**Figure 5 | Effect of pathograph context on mechanistic reasoning.**
*[RESULTS REQUIRED; DO NOT SUBSTITUTE COMPLIANCE SCORES FOR THIS EVALUATION]*

## Additional resource applications

Mechanism-aware phenotype matching can use a pathograph to distinguish
phenotypically similar diseases and to explain secondary manifestations. Any
diagnostic probability emitted by such a system must be independently
calibrated and is not treated here as a validated clinical score.

Treatments linked to the mechanisms they target enable transparent queries
for diseases sharing a therapeutic vulnerability. Such matches are
hypothesis-generating repurposing candidates, not treatment recommendations.
Evaluation should measure whether known cross-indication relationships are
recovered before novel candidates are emphasized.

Pathographs can also evaluate gene→program→trait relationships proposed by
GWAS and perturbation studies. A proposed triple may be confirmed, partially
represented, absent and therefore a curation candidate, or in conflict with
the curated direction of effect. The existing autoimmune/T-cell analysis
will be regenerated against the frozen release before its numerical results
are included [CITE].

# Methods

## Resource scope and governance

DisMech models disorders and pathological processes rather than attempting to
reproduce the MONDO disease hierarchy. Entry scope, disease-versus-subtype
decisions, disease groupings, module conformance, ontology reuse, evidence
policy, and BioLink/KGX export policy follow the project decision register.
The publication will identify the frozen release and the decision-register
version used for analysis.

The source of truth is a collection of YAML records validated against a
LinkML schema. Changes are proposed through version-controlled branches and
pull requests. Human maintainers define schema and editorial policy, review
scientifically consequential changes, and adjudicate disagreements.
Language-model agents may draft or revise records, but agent provenance is
recorded separately from the type of scientific evidence cited.

## Data model

The central `Disease` class contains identifiers, definitions, classifications,
inheritance, pathophysiology, phenotypes, biochemical findings, genetic and
environmental factors, treatments, trials, datasets, models, hypotheses, and
discussions. `Pathophysiology` nodes connect through `CausalEdge` objects.
Treatments connect to pathophysiology or symptomatic phenotype targets through
mechanism-target objects. Experimental models connect to the graph nodes they
recapitulate, perturb, or read out.

Ontology-grounded descriptors preserve both a canonical ontology label and a
curator-facing preferred term. Major sources include HPO, MONDO, GO, CL,
UBERON, MAXO, NCIT, ChEBI, HGNC, GENO, and LOINC. BioLink reuse is primarily
an export-layer concern rather than the internal modelling principle.

## Curation workflow

Candidate content may originate from primary literature, structured
databases, clinical resources, or retained deep-research reports. Deep
research is treated as a source of leads rather than ground truth. Before
research content is curated, the disease identity is checked against
authoritative identifiers and causal genes to reduce named-entity confusion.
References, quotations, and ontology identifiers are independently verified.

Each curation event may record actors, tools, models, affected sections,
links, outcome, and review detail in an append-only history record. The
companion agentic-framework paper describes the interactive and scheduled
agent workflows.

## Evidence and validation

Evidence items may include an authoritative reference, title, support
direction, evidence-source classification, exact source snippet, explanation,
and images. Reference fidelity means that the quoted text exists in the
cited source; it does not establish by itself that the quotation entails the
curated claim. Scientific relevance and causal interpretation therefore
remain separate review dimensions.

Validation includes schema conformance, ontology identifier and canonical-
label validation, reference-snippet validation against tool-generated cache
records, foreign-key and data-integrity tests, and compliance reporting.
Compliance is a coverage measure and is not used as a proxy for biological
correctness.

## Mechanistic hypotheses and discussions

Mechanistic hypotheses carry stable group identifiers and maturity states.
Causal edges opt into one or more hypothesis groups. Discussions record open
questions, knowledge gaps, controversies, emerging hypotheses,
interpretations, and human/model mismatches. Proposed experiments are stored
on the discussion they are intended to resolve.

## Mechanism modules and groupings

Mechanism modules use the same schema as disease entries and define recurring
pathological motifs. Disease nodes may conform to module nodes while retaining
disease-specific content. Groupings are curated unions of distinct entries
with explicit membership rationales and criteria; they are not inferred
ontology classes.

## Frozen-release resource analysis

*[TO IMPLEMENT]* A committed analysis script will compute all resource counts,
coverage estimates, evidence distributions, graph-topology measures, gap
typologies, and module-conformance summaries from a tagged release. The
script will emit machine-readable tables used directly to generate Tables 2
and the corresponding figures. Every reported percentage will include its
numerator, denominator, and treatment of missing values.

## Pathophysiological-reasoning evaluation

*[TO IMPLEMENT]* The evaluation protocol will be preregistered within the
repository before results are inspected. Disease sampling, question
generation, withheld information, comparison conditions, model versions,
human-rater instructions, adjudication, statistical tests, and exclusion
criteria will be fixed in that protocol. Human evaluation will use at least
two independent raters per item and report agreement.

## Interface and exports

The public site provides a faceted disorder browser, individual disease and
module pages, interactive pathographs, evidence displays, embedding
exploration, project views, and quality-control reporting. DisMech exports
tabular data and an export-layer mapping to BioLink/KGX-compatible nodes and
edges. The publication artifact will archive the release, schema, analysis
outputs, and evaluation set under a persistent identifier.

# Discussion

DisMech treats a disease mechanism as an inspectable scientific object rather
than a narrative summary. The contribution is not simply that causal chains
can be drawn. It is that a chain can be queried together with the evidence,
alternative hypotheses, model-system limitations, and explicit points at
which the explanation fails.

Knowledge gaps are therefore outputs of the resource rather than defects to
hide. A missing human bridge, a contested causal direction, or a model that
reproduces only one tissue branch can be attached to the exact place where
additional evidence is needed. This creates a route from knowledge
representation to experiment design, illustrated by the Fabry
mechanism–surrogate–cardiac-model example.

The reasoning evaluation is essential to establish whether this additional
structure changes performance. If pathograph context does not improve
biological correctness, uncertainty recognition, or evidence faithfulness
over a well-chosen narrative baseline, the representation may still be
useful for curation and integration but its stronger clinical-AI claims would
not be supported.

DisMech also provides a production setting for studying agent-assisted
biocuration. That aspect is important but conceptually separable: this paper
evaluates the biomedical representation and its uses, while the companion
paper evaluates the curation and validation architecture.

# Limitations

DisMech is incomplete and uneven in depth. Coverage of pathophysiology does
not imply complete edge-level evidence, and ontology grounding does not imply
that a term is sufficiently specific. Exact-snippet validation establishes
source fidelity but not claim–evidence entailment. Evidence available only in
full text may be absent when the reference cache contains an abstract alone.

Mechanistic graphs simplify continuous, cyclic, temporal, and context-
dependent biology into a tractable representation. Edge direction and
granularity reflect editorial judgement. Mechanism modules can expose
inconsistency but may also impose a shared abstraction on diseases whose
details differ materially.

Knowledge gaps are curated and are consequently subject to ascertainment
bias. Diseases investigated by automated scans or domain projects will appear
to have more explicit gaps than less-curated diseases. Proposed experiments
are hypotheses, not validated study protocols.

The resource is not a clinical decision-support system. Mechanistic matching,
surrogate-endpoint interpretation, and treatment-repurposing queries require
independent validation in their intended contexts of use.

# Data and code availability

DisMech is publicly available at <https://dismech.monarchinitiative.org/>.
Source code and data are available at
<https://github.com/monarch-initiative/dismech>. The final manuscript will
cite a frozen release and persistent archive containing the data, schema,
analysis code, evaluation set, and generated figures.

# Author contributions

*[TO COMPLETE USING CRediT ROLES]*

# Acknowledgements

We thank the LinkML, OAK, Monarch Initiative, OBO Foundry, HPO, MONDO, MAXO,
Cell Ontology, Gene Ontology, UBERON, ClinGen, Orphanet, ClinicalTrials.gov,
MorPhiC, NAMO, and deep-research-provider communities. Funding and contributor
acknowledgements will be reconciled with the consortium author list.

# Competing interests

*[TO COMPLETE]*

# References

1. Moxon, S.A.T. *et al.* LinkML: an open data modeling framework.
   *GigaScience* **15**, giaf152 (2026).
2. [CITE Human Phenotype Ontology]
3. [CITE Mondo Disease Ontology]
4. [CITE Gene Ontology]
5. [CITE Cell Ontology and UBERON]
6. [CITE ClinGen gene–disease validity]
7. [CITE Monarch Initiative]
8. [CITE GA4GH Phenopackets]
9. [CITE FDA surrogate-endpoint table and regulatory framework]
10. [CITE Fabry disease mechanism and organ-specific pathology]
11. [CITE Fabry renal GL-3 surrogate evidence]
12. [CITE Fabry patient-derived iPSC cardiomyocyte studies]
13. [CITE MorPhiC]
14. [CITE NAMO and relevant reporting standards]
15. [CITE SPIRES and related schema-guided extraction work]
16. [CITE pathophysiological-reasoning and clinical-AI evaluation literature]
