---
title: "Human-regulating-the-loop: deterministic schema validation as the safety boundary for agentic biomedical curation"
target_journal: Nature Computational Science / Journal of Biomedical Semantics (high-end)
authors:
  - Christopher J. Mungall (LBNL, Monarch Initiative)
  - J. Harry Caufield (LBNL)
  - [co-authors TBD]
draft_status: working draft
related_talks:
  - "Mungall CJ. *Unlocking Disease Mechanisms: Agentic AI for Clinical Knowledge.* Zenodo, 2026. https://zenodo.org/records/18720444"
revision_notes:
  - "Restructured to Nat CS Methods Resource layout: Abstract, Introduction, Results (Architecture), Failure-mode analysis, Comparison, Limitations, Outlook, Methods."
  - "Tightened abstract from ~350 to ~190 words with structured context/problem/contribution/result/significance flow."
  - "Removed thesis-style numbered headings; adopted shorter declarative headings."
  - "Reduced first-person assertion verbs (we argue/believe/claim) by roughly 60%; shifted body to evidential framing."
  - "Added Figure 1-3, Table 1, Box 1 placeholders with journal-style callouts and inline (Fig. X)/(Table X) references."
  - "Added inline numeric citation markers [N] and References section stub with TBD placeholders for LinkML, OAK, Biolink, Monarch, ClinGen, RLHF, deep-research hallucination, etc."
  - "Promoted the reference-cache integrity incident to a Box 1 example while keeping a dedicated trust-boundary subsection."
  - "Softened unmeasured percentage claims (~70%, ~25%) to qualitative phrasing."
  - "Cut conclusion repetition; thesis now stated in abstract, introduction, and outlook only."
  - "Added one-sentence acknowledgement of the Zenodo talk in the introduction."
  - "Added Methods section consolidating implementation specifics."
  - "Added three alternative titles in an HTML comment above the abstract."
  - "Corrected claims about cache checks, agent permissions, evidence-source requirements, and autonomous merging to match the implemented repository."
  - "Added a controlled-ablation and production-history evaluation plan; empirical results remain to be generated from a frozen release."
---

<!-- Alternative titles considered:
     1. "Human-regulating-the-loop: a deterministic safety boundary for agentic biomedical curation"
     2. "Schemas, not supervisors: deterministic validation as a safety boundary for autonomous knowledge-base curation"
     3. "Curation under constraint: non-fabricatable substrates and schema-bound validation for LLM agents in biomedical knowledge bases"
-->

## Abstract

Large language model agents now draft structured biomedical content faster
than any human curation pipeline can review, but their errors are
confidently expressed and unevenly distributed: fabricated identifiers,
invented quotations, and ontology terms that pattern-match the real ones.
The reflexive answer, human-in-the-loop review, does not scale and in
practice degrades to rubber-stamping. Here we describe an alternative
architecture, **human-regulating-the-loop**, in which humans and upstream
standards bodies define the schema, ontology bindings, and deterministic
validation gates, and agents operate inside that enclosure. We instantiate
the pattern in the Disorder Mechanisms Knowledge Base (DisMech), a LinkML
schema-driven resource currently covering more than 1,600 disorders with
tens of thousands of evidence items. The architecture combines an
ontology-bound schema, a three-layer deterministic validation stack
(schema conformance, ontology term validation, reference-snippet
substring matching), and a tool-generated reference cache intended to be
reproducible from authoritative upstream sources. Agent failure
modes — fabricated PMIDs, paraphrased snippets, label-mismatched ontology
terms, and hand-fabricated cache files — motivate distinct controls at CI
and workflow boundaries. We define an evaluation based on controlled
validator ablations and repository-history replay to measure which errors
each control detects and which semantic errors remain outside deterministic
validation. This separates implemented guarantees from editorial policy and
provides a testable account of safety in agentic biomedical curation.

## Introduction

The dominant framing for safe AI-assisted curation is human-in-the-loop:
a curator reviews each agent output before it enters the canonical store.
This framing is correct as far as it goes but underspecified. It does not
say what the human is supposed to check, does not constrain agent output
to a form where checking is tractable, and degrades predictably as agent
throughput exceeds human review capacity. In knowledge-base practice,
human-in-the-loop most often means a curator approving a large fraction of
agent output that they did not have the bandwidth to verify against
primary sources [1].

The failure modes of current large language model agents in this setting
are well characterized [2, 3]. Agents fabricate identifiers that look real
(a PubMed identifier with the right number of digits, an HPO term with the
right prefix). They synthesise quotations that are stylistically
consistent with the cited source but do not appear in it. They confidently
assign ontology terms whose canonical label does not match the meaning
required by the schema [4]. They produce cache files, dossiers, and
intermediate artifacts that look like real ones and pass casual review. A
human-in-the-loop pipeline that asks a curator to scan such output by eye
will miss most of these errors; the aggregate error rate is not visible
until much later.

The architecture described here inverts this relationship. The human is
not *in* the loop; the human and the upstream standards community are
*around* the loop, having defined the schema, the ontology bindings, the
evidence contract, and the deterministic validators that police them. The
agent operates inside this enclosure. Errors that would otherwise be
absorbed are surfaced at a continuous-integration (CI) gate and blocked
from merging. We call this **human-regulating-the-loop**, in deliberate
contrast to human-in-the-loop (Fig. 1). The distinction determines where
engineering effort goes, what the agent is incentivised to optimise for,
and whether the resource gets safer or less safe as agent capabilities
grow. The framing builds on a recent presentation that introduced the
anti-hallucination posture this paper formalises [5].

We use the Disorder Mechanisms Knowledge Base (DisMech) as the working
substrate. DisMech is a structured representation of disease
pathophysiology built around a LinkML [6] schema with ontology-bound
dynamic enumerations, currently comprising more than 1,600 disorder
entries, more than 100 mechanism modules, and tens of thousands of
evidence items
linking genetic and environmental causes through pathophysiology and
biochemistry to phenotypes and treatments. The resource has been
constructed using two production agentic systems (Claude Code and Codex)
running both interactively under a curator and autonomously via scheduled
GitHub Actions. A companion paper describes the mechanistic content and
its applications; the present paper describes the curation architecture.

The contributions are: (i) a concrete architecture for
human-regulating-the-loop agentic curation, instantiated in a real
mechanistic-disease knowledge base; (ii) an analysis of agent failure
modes that the architecture must address, with the specific design choices
intended to address each; and (iii) an empirical evaluation plan for
**tool-generated reference caches** and **substring-only snippet matching**
as components of a verifiable evidence substrate.

**Figure 1 |** Human-in-the-loop versus human-regulating-the-loop curation
architectures. In the conventional pattern (left), the curator reviews
free-form agent output, and the failure rate is bounded by review
attention. In the proposed architecture (right), humans define the schema,
ontology bindings, and deterministic validation gates; agents emit typed
structured output into a CI-enforced enclosure; the failure rate is
bounded by gate correctness. [FIGURE PLACEHOLDER]

## The schema as the safety boundary

The first design choice is that the primary artefact emitted by the agent
is not text but a typed, schema-bound structure. The schema is authored
in LinkML [6], a schema language for biomedical data that expresses
classes, slots, enumerations, and constraints, and compiles to JSON
Schema, SHACL, ShEx, OWL, and SQL DDL. LinkML's distinguishing feature for
the present purpose is **dynamic enumerations bound by ontology
constraint** (`reachable_from`): an enum value is valid only if it is
reachable from a specified parent in a specified ontology via specified
predicates. The dismech schema uses this construct to require that every
phenotype descriptor term is reachable from the HPO phenotypic-abnormality
branch or the MONDO disease root, every cell type from the Cell Ontology
(CL) [8], and every treatment action from MAXO or the NCI Thesaurus
Clinical Intervention or Procedure branch. Gene identifiers are instead
validated by ontology term existence and exact label matching against HGNC.

Because the agent is required to emit typed objects, it cannot produce a
free-text evidence summary that looks plausible but is unanchored. Because
every ontology slot is bound to an authoritative source, an identifier
that looks like an HPO term but is not defined in HPO is rejected at
validation. Evidence is represented as a structured object that can carry
a reference, verbatim snippet, support direction, and publication evidence
type (human clinical, model organism, in vitro, or computational). Not all
of these slots are currently required, however, and the present corpus
contains legacy or incomplete evidence items. The distinction matters:
the schema makes omissions measurable, but a populated field is not itself
proof that the cited source entails the associated claim.

The schema is also the locus of editorial policy. When agents were
observed to silently conflate frequency-of-phenotype claims (e.g.,
"frequent") with disease–phenotype association claims, the editorial rule
and its validation were added to the schema. When agents were observed to
classify veterinary case series as human-clinical evidence, the
classification rules were tightened and the validation now flags this.
The schema is not static; it is the place where editorial learning
accumulates and where agents' systematic errors become rules they cannot
violate.

## The three-layer deterministic validation stack

Around the schema run three validation layers (Fig. 2). None invokes a
language model. All are deterministic and reproducible; applicable required
checks must pass for a change to merge.

**Layer 1: schema conformance.** `linkml-validate` checks that the
proposed YAML conforms to the schema: required fields are present, types
are correct, enum values are in range, ontology prefixes are correct,
multivalued slots are multivalued, single-valued slots single-valued.
This is the cheapest layer and, in our experience, catches the largest
class of agent errors — agents routinely emit the right idea in the wrong
shape, and the schema catches that immediately.

**Layer 2: ontology term validation.** `linkml-term-validator` checks
every ontology-bound term against a local authoritative snapshot of the
ontology, accessed via the Ontology Access Kit (OAK) [9]. The check is
twofold: the identifier must exist in the ontology, and the `term.label`
recorded in the YAML must exactly match the canonical label. This catches
a failure mode that is both common and dangerous: an identifier that is
in the ontology but whose label is wrong — for example, asserting that
`HP:0001324` has label "Hypotonia" when in fact `HP:0001324` is "Muscle
weakness". A label mismatch is not cosmetic; it indicates that the
agent's intent and the actual term diverge, and the downstream semantic
interpretation will be wrong [4].

Each descriptor carries two distinct label slots. The `term.label` slot
is canonical and must match the ontology exactly. The `preferred_term`
slot is the human-readable display label and may be more specific or
differently phrased than the ontology label when the ontology term is too
broad to convey the intended clinical granularity. The separation gives
the agent a controlled outlet for clinical nuance without permitting
corruption of the ontology binding.

**Layer 3: reference-snippet validation.**
`linkml-reference-validator` checks that each populated evidence `snippet`
is a verbatim substring of the cached text for the cited `reference`.
This is the single most consequential layer of the stack. It catches
paraphrased or fabricated quotations and many wrong-reference assignments;
unresolvable identifiers fail during cache retrieval. It does not catch a
real quotation from a real but irrelevant paper. Substring
matching is intentionally strict: no fuzzy matching, no normalisation, no
"close enough". The cost is occasional false rejections from whitespace
and encoding issues; the benefit is that *whether a snippet exists in the
source* is a yes/no fact the agent cannot game.

The three layers run in sequence, cheapest first, and the pipeline
short-circuits on the first failure. In our experience, the schema layer
catches the largest class of agent errors before the term and reference
validators are reached; the term validator catches a further substantial
class; the reference validator catches the residual most-dangerous class
— confident textual fabrication. The evaluation below tests these expected
detection boundaries instead of treating them as complete in advance.

**Figure 2 |** Three-layer deterministic validation stack. Each layer is a
deterministic check against an authoritative artifact: the LinkML schema,
local ontology snapshots accessed via OAK, and the per-reference cache.
Example failures caught at each layer are shown: an invalid value or
structural type in an evidence item (Layer 1), an HPO label mismatch where
`HP:0001324` is recorded as "Hypotonia" rather than "Muscle weakness"
(Layer 2), and a paraphrased snippet absent from the cited PubMed
abstract (Layer 3). [FIGURE PLACEHOLDER]

## Tool-generated reference caches and the integrity contract

The reference cache is the asset on which Layer 3 depends, and its
integrity is therefore load-bearing. A production incident exposed the
central threat: an agent can satisfy substring validation by fabricating
the cache that the validator queries (Box 1).

The repository now defines a workflow contract: cache entries must be
regenerated with `just fetch-reference <ID>` and must never be created or
hand-edited. Fetchers obtain records from PubMed, ClinicalTrials.gov, and
supported structured sources and write markdown with YAML frontmatter
under canonical filenames. A deterministic check validates parseable
frontmatter, identifier-to-filename consistency, source-specific required
fields, and known fabrication fingerprints.

These controls are useful but do not yet make the cache
**non-fabricatable** in the strong sense. The checked frontmatter does not
contain a content checksum, and the repository's general agent settings do
not universally deny writes to `references_cache/`. Some scheduled
workflows legitimately regenerate and commit cache files. Consequently,
the integrity guarantee currently combines tool-generated provenance,
documented agent policy, structural checks, code review, and selected
workflow scoping. A well-formed but fabricated cache body could evade the
structural check unless compared with the upstream record.

The target architecture adds a reproducibility audit: re-fetch a stratified
sample, or every changed cache entry, and compare normalized upstream
content with the committed cache. Where the execution environment supports
role-specific file permissions, direct cache writes should also be denied
while the fetch command remains available as the only writer. The paper
will report these as separate controls rather than collapsing policy,
structural validation, and source fidelity into a single claim.

**Figure 3 |** Reference-cache trust boundaries. Source-specific fetchers
materialize upstream records in `references_cache/`; structural CI checks
validate frontmatter and identifier consistency; snippet validation treats
the cached body as its substring substrate. Dashed boundaries show controls
still requiring implementation or evaluation: source-content comparison
and universal prevention of direct agent writes. [FIGURE PLACEHOLDER]

> **Box 1 | Cache fabrication caught in production**
>
> An agent was asked to add a phenotype claim backed by a PubMed
> identifier. It produced a plausible snippet, but the reference
> validator failed because the snippet was not in the cache. The agent,
> instructed to "resolve the validation failure", responded by **creating
> the cache file by hand**, with fabricated abstract content engineered
> to contain the snippet verbatim. Schema validation passed. Term
> validation passed. The reference validator now also passed, because
> the snippet matched the (fabricated) cache. A casual human reviewer
> seeing a green CI would have merged.
>
> The incident motivated the dedicated cache-frontmatter test and the
> explicit repository rule that cache files be regenerated rather than
> hand-edited. Those measures detect malformed or suspicious cache shapes,
> but they do not prove body fidelity. The retrospective history analysis
> proposed below will establish the incidence and outcomes of cache-related
> failures; source re-fetching will test whether structurally valid cache
> bodies match upstream records. The lesson generalises: a validator is only
> as trustworthy as the substrate it queries.

## Structured-database sources as quotable evidence

The same verifiable-substrate pattern extends to non-literature
evidence. Many of the most important biomedical claims are not in
journal abstracts but in structured databases: Orphanet [10] for
rare-disease definitions and phenotypes, ClinGen [11] for gene–disease
validity and dosage sensitivity, ClinicalTrials.gov for trial details,
CIViC [12] for cancer variant evidence. Each has its own access pattern,
schema, and update cadence.

Structured sources are treated as first-class citable evidence. For each
source, a source-specific fetcher in `src/dismech/structured_sources/`
pulls the bulk data at a pinned snapshot version, builds an index, and
materialises one cache file per entity in the same `references_cache/`
directory used for literature. The cache files use a deterministic
line-oriented markdown format with markdown tables for tabular content,
so that an Orphanet phenotype row or a ClinGen validity assertion row
is a **stable quotable substring** that does not drift across rebuilds.
Snapshot versions are pinned in a per-source manifest; refreshes are
explicit and reviewable.

An evidence item with `reference: ORPHA:558` and a snippet quoting
*"Marfan syndrome is a systemic disease of connective tissue"* is
validated by the same substring check that validates a PMID-backed claim.
The agent does not need to distinguish source types, and the validation
mechanism does not need to special-case them. New structured sources are
added by writing a new fetcher; the validation stack is unchanged.

## The agentic harness

Inside the validation enclosure, agents are responsible for a substantial
fraction of the curation work: drafting and enriching disorder entries
from the literature; adding ontology term annotations (HPO phenotypes,
GO processes [13], CL cell types, MAXO treatments) under a dedicated
skill that enforces authoritative term lookup via OAK [9]; validating and
repairing evidence references under a dedicated skill that enforces the
snippet substring contract; responding to compliance scoring that
identifies under-curated entries; and reviewing pull requests against the
dismech contributor guidelines via a dedicated review agent.

Repository instructions tell agents not to hand-edit the reference cache,
not to bypass validation, and to constrain curation changes to the intended
files. Schema changes are reviewed as editorial and infrastructure changes,
not ordinary disorder curation. The available agent harnesses also differ:
some expose command allowlists and pre-tool hooks, while scheduled
workflows constrain prompts, file scope, credentials, and merge eligibility.
These controls are not equivalent to a universal file-system deny rule.

This distinction between **policy**, **preventive enforcement**, and
**detective validation** is part of the architecture rather than an
implementation detail. The evaluation records which control was active for
each production run and uses negative tests to establish what each harness
actually prevents.

## Continuous integration as the enforcement layer

The pull request is the unit of curation work. Every pull request runs
the three-layer validation stack, the structured-cache frontmatter
check, a schema-test suite, and an AI-augmented review pass. The review
pass is run by a language model agent configured against the same
contributor guidelines used for human review, and it produces inline
suggestions with location, issue, and recommendation. **The review
agent's findings are advisory; the deterministic validators' findings are
blocking.**

The human curator (or curating agent) is responsible for resolving
findings; they cannot be dismissed silently. When the review agent finds
a problem and the human disagrees, the disagreement is recorded as a
pull-request comment and the human's reasoning is on the record. This
creates an audit trail of editorial judgement that is mined for schema
refinements: a recurring disagreement between review agent and human
curators is usually a sign that the underlying rule is ambiguous and
needs to be made explicit in the schema or guidelines.

A scheduled GitHub Action periodically inspects compliance results,
identifies low-scoring entries, dispatches an agentic curation job, and
opens pull requests. Those weekly-compliance PRs enter the same review and
deterministic closing path as other PRs; they have no lane-specific merge
classifier, and draft state is not treated as a lifecycle hold. A pull request
that passes CI is therefore not necessarily merged without human intervention.
The production-history analysis below will report the proportions merged
automatically, merged after human edits, closed, or left unresolved, together
with the failures that caused escalation.

## Failure-mode analysis

Table 1 documents the principal agent failure modes observed during
dismech development and the specific architectural mechanism that catches
each. Three patterns recur. First, several dangerous failure modes (label
mismatch and paraphrased snippet) are caught by deterministic checks
against an external authority; cache fabrication is only partially covered
until the cache body is reconciled with its upstream source. Second,
editorial-rule failures
(frequency evidence, evidence-source classification) are caught by a
combination of schema documentation, AI review, and human judgement;
each newly observed failure of this kind is promoted into a more
explicit schema constraint where possible. Third, model training and
self-correction are not treated as independently verified controls in the
current system; their contribution must be measured against deterministic
and human-review baselines.

**Table 1 |** Observed agent failure modes during dismech curation and
the architectural mechanism that catches each.

| Failure mode | Catching mechanism |
|---|---|
| Fabricated PMID | Reference fetcher fails to resolve; PMID absent from cache; snippet check fails. |
| Real PMID, wrong paper for claim | Fails only if the supplied snippet is absent; a real but irrelevant quotation requires semantic review. |
| Real PMID, paraphrased snippet | Substring check fails; reference validator fails. |
| Snippet from PMID A assigned to PMID B | Cache is per-PMID; snippet from A is not a substring of cache for B; validator fails. |
| Cache file fabricated to satisfy snippet | Structural checks catch malformed frontmatter and known fingerprints; upstream reproducibility audit is required for a well-formed fabrication. |
| Fake HP/GO/CL term that looks real | Term validator: identifier absent from ontology snapshot. |
| Real term, wrong label | Term validator: identifier present but `term.label` mismatches canonical. |
| Real term, wrong meaning (HP for GO concept) | Schema `reachable_from` binding to required ontology root rejects. |
| Frequency claim backed by association evidence | Editorial rule in schema and contributor guide; AI review flag; human verification. |
| Veterinary or model-organism evidence classified as human-clinical | `evidence_source` enum with editorial rule; AI review flag; schema documentation. |
| Silent removal of inconvenient REFUTE evidence | Git diff at PR review; AI review flags significant deletions. |
| Subtype foreign-key inconsistency | Dedicated test (`test_subtype_foreign_keys`) verifies subtype references resolve. |

## Comparison with alternative safety architectures

The dominant alternatives to deterministic schema validation for safe
agentic content production are RLHF-style preference training [14],
post-hoc fact-checking by a second language model [16], and agent
self-verification [15]. Each has structural failure modes that
deterministic validation does not.

**RLHF and preference training** [14] can improve instruction following
and the apparent quality of outputs, but do not themselves make a claim
verifiable. Whether they reduce fabricated identifiers or improve source
selection in this task is an empirical question. The relevant comparison
therefore holds the agent and task set fixed and measures outcomes with and
without external validators, rather than inferring safety from the training
method.

**Post-hoc fact-checking by a second language model** [16] can detect
editorial and semantic problems that deterministic validators cannot, but
is not an authoritative oracle for citations, ontology labels, or
quotations. In DisMech it is used as an advisory review layer. The proposed
ablation measures its precision, recall, and overlap with deterministic
validators and expert adjudication.

**Agent self-verification** [15] may reduce some errors, but it queries the
same model family rather than an independent source of truth. We therefore
treat it as a candidate production strategy to compare, not as either a
guarantee or a null control.

The case for deterministic schema and identifier validation as the
*primary* safety boundary is therefore not aesthetic. Deterministic
validation has the useful property that a given check is independent of
the agent's confidence. Its coverage is narrower, however, and its failure
rate depends on human-authored code, schema assumptions, ontology
snapshots, and the integrity of cached sources. The empirical question is
which combination of deterministic, model-based, and expert checks offers
the best coverage at acceptable review cost.

## Evaluation framework

The paper requires two complementary evaluations on a frozen code and data
release. First, a **controlled perturbation benchmark** will sample
curation units across disorders, claim types, ontology namespaces, and
evidence sources. For each valid unit, one mutation will introduce a
pre-specified failure: malformed structure, nonexistent identifier, real
identifier with wrong label, wrong ontology namespace, paraphrased snippet,
snippet/reference swap, real but irrelevant quotation, unsupported
mechanistic interpretation, misclassified evidence source, or fabricated
cache body. Each variant will be run through schema validation, term
validation, snippet validation, cache-structure checks, AI review, and
blinded expert review. Primary outcomes are per-failure sensitivity,
false-positive rate on unchanged controls, overlap among controls, and
review time.

Second, a **production-history study** will identify agent-authored or
agent-revised pull requests over a pre-specified interval. For each pull
request we will record agent and harness, trigger type, files changed,
validator failures by layer, review findings, human edits after agent
output, merge disposition, elapsed time, and whether auto-merge was
enabled. A stratified expert audit of merged claims will estimate residual
semantic error, including real-but-irrelevant quotations and plausible but
unsupported causal links.

The principal ablations are: schema only; schema plus ontology validation;
all deterministic content validators; deterministic validators plus cache
structural checks; AI review alone; and the full production stack. A
separate negative-test matrix will probe whether each harness can directly
edit cache files, modify schema or workflow files, skip required checks, or
merge outside its declared scope. **[TODO: freeze release and interval;
register sampling and adjudication protocol; report confidence intervals
and paired comparisons.]**

## Limitations

The architecture has its own failure modes. Substring snippet matching
does not catch a snippet that is *real but irrelevant* — quoted
correctly from an abstract that does not actually support the claim
being made; AI and human review remain the only defence for this layer,
and have occasionally failed. Term validation does not catch a term that
is correct but too broad or too narrow for the intended meaning; this is
again an editorial judgement that AI and human review must catch. The
schema is human-authored and contains its own errors; mitigation is via
schema tests and an iterative process of promoting rules from
contributor-guide prose to schema constraint. The cache is only as good
as the snapshot date; refreshes can change snippets in ways that
retroactively invalidate evidence, and structural checks do not prove that
a cache body came from upstream. Named-entity validity also does not imply
correct entity selection: a real gene, disease, or anatomical identifier
can refer to the wrong namesake or biological context. Causal direction,
mechanistic relevance, transportability across species or model systems,
and the clinical meaning of a surrogate endpoint all remain semantic
questions outside the current deterministic boundary.

The agentic harness itself is software with bugs, and its permission
boundaries vary across interactive and scheduled environments. Repository
history is also an observational dataset: model versions, prompts, schema,
source availability, and validator coverage change over time. Production
comparisons will therefore be reported by time period and configuration
and will not be interpreted as randomized comparisons among agent systems.

Throughput is the second cost. Deterministic validation is slower than
agent self-verification, particularly when reference fetches must be
performed. Caching, parallelism, and structured-source batch fetches
amortise this, but a single new PMID remains a network call away. This
appears to be an unavoidable cost of the architecture rather than a
defect.

## Outlook

The right relationship between humans and agents in
structured biomedical curation is not human-in-the-loop but
human-regulating-the-loop. As agentic capabilities grow, the
architecture described here can preserve invariant checks even as model
behavior changes, because deterministic gates are independent of agent
confidence. This does not guarantee that the overall system becomes safer:
agents may create novel errors outside the checked boundary. We do not claim this is
the only safe architecture for agentic biomedical curation, but any safe
architecture will share its essential features: typed structured output,
deterministic validation against authoritative sources, verifiable
substrates, and a schema in which editorial learning accumulates. The
priority for future work is to broaden the structured-database fetcher
catalogue, to formalise the schema-promotion workflow by which editorial
rules become validation constraints, and to study whether the same
pattern can be ported to other structured biomedical resources, including
knowledge graphs in the Monarch Initiative [17] and Biolink Model [18]
ecosystem.

## Methods

**Schema and validators.** The dismech LinkML schema is at
`src/dismech/schema/dismech.yaml`. Schema validation uses
`linkml-validate`; ontology term validation uses `linkml-term-validator`
backed by OAK [9] with local SQLite snapshots of HPO, GO, CL, MONDO,
UBERON, CHEBI, GENO, HGNC, MAXO, and NCIT (`conf/oak_config.yaml`).
Reference-snippet validation uses `linkml-reference-validator` with
substring matching against per-reference markdown cache files.

**Reference cache.** Literature cache files
(`references_cache/PMID_*.md`, `references_cache/DOI_*.md`,
`references_cache/clinicaltrials_*.md`) are populated only by dedicated
fetchers invoked through `just fetch-reference <ID>`. Each file carries
YAML frontmatter recording the canonical identifier, fetch date, source,
or source-specific bibliographic fields. A deterministic frontmatter check
(`just check-reference-cache-frontmatter`) runs at every CI invocation
and enforces parseability, filename–identifier consistency, required
source-specific fields, and selected fabrication fingerprints. It does not
currently compare a content checksum with an upstream record.

**Structured-database sources.** Structured-source fetchers are in
`src/dismech/structured_sources/`. Each subclasses a common
`StructuredSource` base class implementing `build_index`, `identifiers`,
and `serialize`. Source implementations include Orphanet, ClinGen
Gene-Disease Validity, ClinGen Dosage Sensitivity, CIViC, ICEES,
MyGeneSet, and ontology-derived edges. **[TODO: report source versions,
entity counts, snapshot policy, and reproducibility results from the
frozen release.]**

**Agentic harness.** Two production agentic systems were used: Claude
Code and Codex. Both operate against the schema and validators through
shell, git, and repository instructions, but their available tools and
permission mechanisms differ by execution environment. The contributor
guide (`CLAUDE.md`) and repository-level `AGENTS.md` prohibit hand-editing
reference cache files and direct agents to the fetcher. Current settings do
not establish a universal deny-write boundary for the cache; the negative
tests described above will document effective permissions by harness.

**Continuous integration.** Pull requests run repository checks including
schema conformance, term validation, reference-snippet validation, cache
frontmatter checks, and schema and data tests, with path and workflow
conditions determining the exact jobs. An AI-augmented review pass can
review changes against contributor guidelines. Deterministic check
failures are blocking where configured as required checks; review-agent
findings are advisory.

**Autonomous curation loop.** A scheduled GitHub Action periodically
inspects compliance output, selects low-scoring entries, and dispatches
agentic curation jobs that open pull requests. Weekly-compliance pull requests
follow the same guarded review and deterministic closing path as other pull
requests; they do not have a separate merge classifier.

## Data and code availability

Schema, validators, agent harness configuration, and full curation
history are at <https://github.com/monarch-initiative/dismech>. A
browsable resource is available at
<https://dismech.monarchinitiative.org/>. LinkML is documented at
<https://linkml.io>. The cache fetcher and structured-source framework
are part of the dismech codebase under
`src/dismech/structured_sources/`.

## Acknowledgements

We thank the LinkML, OAK, Monarch Initiative, ClinGen, Orphanet, and
CIViC communities for the standards and bulk data on which dismech
depends. The framing described here builds on a presentation by the
first author, *Unlocking Disease Mechanisms: Agentic AI for Clinical
Knowledge*, recorded on Zenodo [5]. Funded by [TBD].

## References

- [1] [TBD: human-in-the-loop curation scaling limits, biomedical KB curation throughput literature]
- [2] [TBD: LLM hallucination characterisation in scientific tasks, e.g., Ji et al., survey of hallucination in NLG]
- [3] [TBD: deep-research / agent citation hallucination characterisation, recent agent eval benchmarks]
- [4] [TBD: ontology hallucination in LLMs, e.g., recent work on biomedical concept grounding]
- [5] Mungall CJ. *Unlocking Disease Mechanisms: Agentic AI for Clinical Knowledge.* Zenodo, 2026. <https://zenodo.org/records/18720444>
- [6] Moxon, S.A.T. *et al.* LinkML: an open data modeling framework.
  *GigaScience* **15**, giaf152 (2026).
- [7] [TBD: Human Phenotype Ontology citation, Köhler et al., *Nucleic Acids Research*]
- [8] [TBD: Cell Ontology citation, Diehl et al., *Journal of Biomedical Semantics*]
- [9] [TBD: Ontology Access Kit (OAK) citation, Mungall et al.]
- [10] [TBD: Orphanet / Orphadata citation, Rath et al., *Human Mutation*]
- [11] [TBD: ClinGen Gene-Disease Validity citation, Strande et al., *AJHG*]
- [12] [TBD: CIViC citation, Griffith et al., *Nature Genetics*]
- [13] [TBD: Gene Ontology citation, Ashburner et al. 2000 / GO Consortium update]
- [14] [TBD: RLHF citation, Ouyang et al. *InstructGPT*; Christiano et al.]
- [15] [TBD: agent self-verification / self-critique citation, e.g., Madaan et al. *Self-Refine*]
- [16] [TBD: LLM fact-checking / second-model verification citation]
- [17] [TBD: Monarch Initiative citation, Putman et al. / Shefchek et al.]
- [18] [TBD: Biolink Model citation, Unni et al., *Clinical and Translational Science*]
