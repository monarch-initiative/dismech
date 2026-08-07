---
title: "DisMech manuscript gap review"
date: 2026-07-29
status: working review
audience: internal planning
---

# DisMech manuscript gap review

> **Internal planning document.** This review is not part of either
> manuscript or their submission package.

This review covers the two manuscript drafts recovered from commit
`f858a0c43d`:

- `dismech-pathograph-resource.md` — the content, pathograph, and translational
  use paper.
- `agentic-curation-jbms.md` — the agentic curation and validation-framework
  paper.

The review emphasizes what is missing rather than prose quality. It compares
the drafts with the current repository, the consortium Google Doc titled
*DisMech manuscript — Data Resource*, the TMC AI keynote, and the CERSI/FDA
surrogate-endpoint presentation.

## Overall assessment

Both manuscripts have a strong thesis and a usable conceptual structure. They
are not yet submission-ready because they are argument-led rather than
result-led.

The content paper currently reads as a Perspective that announces several
potential applications. A high-impact biomedical Resource or Analysis paper
needs a quantitative characterization of the resource, an expert quality
assessment, and at least one convincing evaluation showing that explicit
pathophysiological knowledge changes a clinically or translationally relevant
result.

The agentic paper currently reads as an architecture and position paper.
Its main safety claim is not yet supported by a controlled evaluation, and
several descriptions of enforcement are stronger than the implementation.
It needs measured failure rates, ablations, throughput and review-burden
results, and a precise distinction between policy guardrails and technically
enforced boundaries.

## Comparison with the consortium Google Doc

The Google Doc is the stronger structural base for the content paper. It
already supplies the consortium author list and a conventional data-resource
sequence—abstract, introduction, resource description, methods, discussion,
and submission context. Its current submission context identifies arXiv as
the immediate target and leaves the journal undecided.

The recovered pathograph draft is the stronger scientific donor. It has the
clearer thesis about computable causal explanations, mechanistic knowledge
gaps, pathophysiological reasoning, NAMs, and surrogate endpoints. Neither
version yet contains the empirical package required for a high-impact
resource paper. The integrated revision therefore uses the Google Doc's
resource-paper spine while importing the pathograph thesis and the FDA
Fabry-disease case.

Relative to the recovered draft, the Google Doc adds or improves:

- Consortium authorship and a recognizable resource-manuscript structure.
- More concrete descriptions of schema components, interface features, and
  repository context.
- A clearer basis for an arXiv data-resource preprint.

Relative to the Google Doc, the recovered draft adds or improves:

- A distinctive scientific object—the pathograph—rather than a general
  knowledge-base description.
- Explicit mechanistic hypotheses, gaps, human/model mismatches, and proposed
  experiments.
- A falsifiable application claim: pathograph context should improve
  pathophysiological reasoning.
- A translational narrative linking disease mechanism, NAM readouts, and
  surrogate endpoints.

The principal omissions are shared: frozen-release statistics, graph and
evidence characterization, domain-expert content audit, reasoning evaluation,
comparative resource analysis, complete citations, generated figures, and a
fully developed case study. The two texts are therefore complementary, not
competing drafts.

## Preliminary current-resource snapshot

The May drafts use figures such as approximately 500 disorders and ten
mechanism modules. A direct inventory of the current worktree on 2026-07-29
instead found:

| Object | Current count |
|---|---:|
| Disorder files | 1,635 |
| Mechanism modules | 118 |
| Groupings | 48 |
| Comorbidity files | 17 |
| Pathophysiology nodes, disorders and modules | 9,114 |
| Causal edges, disorders and modules | 17,912 |
| Phenotypes, disorders and modules | 17,314 |
| Treatments, disorders and modules | 6,372 |
| Evidence items, disorders and modules | 79,862 |
| Mechanistic hypotheses, disorders and modules | 360 |
| Discussions, disorders and modules | 656 |
| Knowledge-gap discussions | 447 |
| Human/model-mismatch discussions | 112 |
| Proposed experiments | 375 |
| Reference-cache records | 31,623 |
| Append-only history records | 2,435 |

Coverage is broad but uneven in the dimensions most relevant to the proposed
content paper:

- 99.7% of disorder files contain pathophysiology nodes.
- 92.0% contain at least one causal edge.
- 17.7% contain a discussion.
- 10.3% contain a mechanistic hypothesis object.
- 94.7% of pathophysiology nodes have node-level evidence, but only 47.1% of
  causal edges have edge-specific evidence.
- 8,559 of 79,862 evidence items do not set `evidence_source`.

These are preliminary counts, not manuscript results. They need to be
recomputed by a committed, versioned analysis against a frozen release.

## Paper 1: pathographs, content, and translational use

### Highest-priority missing result: characterize the resource

The paper needs a Results section that establishes what DisMech contains and
how consistently it contains it. At minimum:

1. Freeze a release and report counts by disease class, mechanism-node type,
   biological scale, evidence source, hypothesis status, discussion kind, and
   ontology.
2. Quantify graph structure: nodes and edges per disease, connectedness,
   orphan nodes, edge directness, branching, cross-scale transitions, and
   treatment-to-mechanism links.
3. Quantify evidence coverage separately for nodes, causal edges, phenotypes,
   treatments, hypotheses, gaps, and proposed experiments.
4. Show depth variation rather than reporting only totals. Include medians,
   distributions, and representative high- and low-depth entries.
5. Describe coverage against an explicit denominator such as MONDO, Orphanet
   rare diseases, or a clinically defined target set. Avoid implying that raw
   file count alone establishes completeness.

Without this section, readers cannot tell whether DisMech is a mature resource
or a collection of compelling examples.

### Highest-priority missing result: evaluate pathophysiological reasoning

The manuscript claims that pathographs support mechanistic differential
diagnosis, explanations of unexpected phenotypes, drug repurposing, GWAS
interpretation, surrogate-endpoint reasoning, and clinical-AI grounding. Most
are currently examples or prospective claims.

A central evaluation should test whether access to DisMech improves
pathophysiological reasoning. Candidate tasks include:

- Explain why a phenotype follows from a molecular lesion.
- Distinguish diseases with similar HPO profiles but different causal chains.
- Identify a patient feature not explained by the candidate pathograph.
- Predict which phenotypes should respond when a treatment targets a specific
  mechanism node.
- Distinguish canonical, alternative, and emerging hypotheses.
- Identify which edge is unsupported by human evidence.
- Select a NAM or experiment that would address an explicit knowledge gap.
- Judge whether a biomarker is plausibly upstream of, parallel to, or
  disconnected from a clinical outcome.

A credible design would compare the same model or clinician with and without
DisMech context, use blinded expert scoring, and report correctness,
faithfulness to cited paths, unsupported-claim rate, and calibration. The
current phenomatcher example is not a substitute for this evaluation; its
probability output also needs validation before being described as a
diagnostic probability.

### Highest-priority missing result: make knowledge gaps a main contribution

Knowledge gaps are one paragraph in the draft even though they are central to
the intended paper. The current resource supports a much stronger analysis:

- 447 general knowledge gaps.
- 112 explicit human/model mismatches.
- 375 proposed experiments.
- Gap attachment to specific nodes and edges.
- Lifecycle states and resolutions.
- Automated knowledge-gap and literature scanning workflows.

The paper should develop a gap typology, quantify it across disease classes,
and show how a gap becomes a focused research question and proposed
experiment. Human/model mismatch should be treated separately from simple
absence of evidence.

The strongest worked example is likely the FDA deck's Fabry-disease chain:
GLA deficiency to GL-3 accumulation to organ-specific damage, renal GL-3
clearance as a surrogate endpoint, and the unresolved cardiac branch. This
connects a mechanistic graph, a regulatory endpoint, an explicit evidence gap,
and patient-derived iPSC cardiomyocytes as a proposed way to close it.

### Missing quality and validity assessment

The paper needs evidence that the content is correct, not only that it passes
syntactic and provenance checks. Suggested components:

- Blinded domain-expert review of a stratified sample of nodes and edges.
- Separate ratings for claim correctness, edge direction, causal directness,
  evidence relevance, ontology specificity, and completeness.
- Inter-rater agreement and adjudication.
- Comparison with a conventional narrative review or independent clinical
  guideline for selected diseases.
- Error analysis by evidence source and by agent/human provenance.
- Explicit measurement of real-but-irrelevant snippets, which substring
  validation cannot detect.

### Missing comparative positioning

The comparison with OMIM, HPO, KEGG, Reactome, ClinGen, DrugBank, and Open
Targets is rhetorical. Add a feature-level comparison using a defined sample:

- Does the resource represent intermediate causal steps?
- Are competing hypotheses distinguishable?
- Are causal edges evidence-bearing?
- Are knowledge gaps and proposed experiments represented?
- Are therapies linked to the mechanisms they target?
- Are human and model-system evidence distinguished?
- Can the representation support computable queries?

This should be empirical where possible and careful not to claim that other
resources lack features without a documented comparison.

### Missing methods and reproducibility

The content paper has no Methods section. It needs:

- Scope and inclusion criteria for a DisMech entry.
- Disease-versus-subtype, grouping, and mechanism-module policy.
- Curation and review process, including human governance.
- Schema and ontology choices, aligned with the decision register.
- Evidence inclusion, exact-snippet, and support-direction policy.
- Definition and construction of a pathograph.
- Knowledge-gap and hypothesis encoding.
- Analysis code, release identifier, license, and archival DOI.
- Procedures for generating every figure and table.

### Claims that needed correction or qualification at review time

- Replace approximately 500 disorders and ten modules with frozen-release
  results.
- `DiscussionStatusEnum` uses `RESOLVED`, not `ADDRESSED`.
- Mechanistic hypotheses use `DEPRECATED`, not `REFUTED`, as their terminal
  status; `REFUTE` is an evidence-support direction.
- Knowledge gaps are represented as `Discussion` objects with
  `kind: KNOWLEDGE_GAP`, not in a dedicated structural `knowledge_gaps` slot.
- Do not imply every causal edge has evidence; preliminary coverage is 47.1%.
- Do not imply every assertion has all evidence fields. `evidence_source` is
  optional and is currently unset for thousands of items.
- Distinguish OpenScientist, which produces research artifacts for triage,
  from curation agents that do write changes to the knowledge base.
- Reassess statements that a pathograph directly produces drug-repurposing
  candidates or auditable clinical-AI behavior until those applications are
  evaluated.
- Replace the older GitHub Pages URL with the canonical current site where
  appropriate.

### Missing publication package at review time

- The reviewed resource draft had 18 reference placeholders and four figure
  placeholders. The current integrated resource draft has 16 numbered
  references, with the LinkML citation populated, and five figures; the
  remaining placeholders should be tracked against the current manuscript.
- Author list, contribution statement, funding, competing interests, and
  resource governance are unresolved.
- The manuscript needs a target journal and article type. In its current form
  it is a Perspective; a high-impact Resource or Analysis submission needs
  the empirical results above.

## Paper 2: agentic curation framework

### Highest-priority missing result: controlled evaluation

The paper's central contribution is an architecture, but it reports no
controlled experiment showing what each layer contributes. A minimum
evaluation should use a fixed task corpus and compare:

1. Agent output with no validators.
2. Schema validation only.
3. Schema plus ontology-term validation.
4. Full validation including reference-substring checks.
5. Full validation plus semantic human/expert review.

Stratify tasks across new-entry creation, enrichment, evidence repair,
ontology grounding, and schema evolution. Run more than one agent/model if
the paper claims model independence.

Report:

- Error detection rate by error class.
- False-positive and false-negative rate of each validator.
- End-to-end accepted-claim precision.
- Human review minutes per accepted assertion or pull request.
- Agent retries, wall time, token/API cost, and completion rate.
- Time from issue to merged pull request.
- Revert or post-merge correction rate.
- Performance on deliberately injected adversarial errors.

Without these results, “human-regulating-the-loop” remains a persuasive design
proposal rather than a demonstrated framework.

### Highest-priority missing result: historical production analysis

The repository contains rich longitudinal data that the draft does not use:
git history, pull requests, CI results, automated reviews, 2,435 structured
history records, and multiple scheduled workflows.

The paper should reconstruct:

- Volume and rate of agent-authored changes over time.
- Which workflows produced which changes.
- Validation failures and repair cycles.
- Review decisions and number of iterations.
- Human versus agent intervention points.
- Recurring failure modes before and after each guardrail was introduced.
- Changes in throughput and defect rate after schema or policy changes.

The cache-fabrication incident is valuable, but it needs a traceable incident
record, denominator, and before/after measurement rather than an anecdote.

### Highest-priority missing correction: enforcement is overstated

The draft repeatedly calls the cache “non-fabricatable” and says the harness
denies cache writes. The checked-in Claude settings do not establish that
boundary:

- `.claude/settings.json` allows staging `references_cache/`.
- Its edit hook validates proposed `kb/disorders/*.yaml` edits; it does not
  deny writes to `references_cache/`.
- The prohibition against hand-editing cache files is strongly documented,
  but documentation is a policy control rather than a technical denial.
- Codex behavior is governed by a separate instruction layer, not the checked-in
  Claude permission configuration described in the draft.

Until a deny-write control and a test of that control exist, use
“tool-generated reference cache with integrity checks” rather than
“non-fabricatable cache.” More importantly, add an automated negative test
showing that each supported agent harness cannot directly create or edit a
cache file.

The draft also claims checksums in cache frontmatter. Current PMID cache
frontmatter does not include a content checksum. The frontmatter checker
validates structural and identifier/filename consistency, not equivalence to a
fresh upstream fetch. These guarantees must be described precisely.

### Other claims needing correction or evidence

- `EvidenceItem` does not require `evidence_source`; it is optional, and 8,559
  current evidence items leave it unset.
- A real PMID for the wrong claim is not necessarily caught. A real,
  irrelevant quotation from that paper passes substring validation.
- Schema conformance does not make vague or unsupported prose impossible.
- Agents do modify schema and infrastructure in this repository under human
  direction; “agents are not permitted to modify the schema” is not a general
  enforced rule.
- AI-review findings are advisory. The claim that they require explicit
  acknowledgement before merge needs an enforcement mechanism or softer
  wording.
- Not every curation pull request merges automatically when validation passes.
  Describe the actual approval and auto-merge conditions per workflow.
- “Autonomous end-to-end” needs a precise operational definition and measured
  proportion of qualifying pull requests.
- The statement that RLHF, self-verification, and second-model review do not
  catch any listed failure mode is too absolute without a comparative study.
- “The architecture gets safer as agents get better” is a hypothesis, not a
  result.

### Missing semantic safety layer

The draft correctly notes that substring matching cannot determine whether a
quotation supports a claim. This is not a minor limitation; it is the largest
remaining epistemic gap. The paper should formalize at least four layers:

1. Structural validity.
2. Identifier and ontology validity.
3. Source fidelity: the quotation exists.
4. Claim–evidence entailment and scientific relevance.

The first three can be substantially deterministic. The fourth currently
requires expert judgment or a separately evaluated semantic model. Making this
boundary explicit would strengthen the paper and prevent “green CI” from being
misread as scientific correctness.

Named-entity confusion should be included as a distinct production failure
mode. In that case, the PMID, quotation, and ontology term can all be real and
valid while the research report concerns the wrong disease. This is a clean
demonstration of why deterministic provenance checks are necessary but not
sufficient.

### Missing portability result

The paper presents a general architecture but evaluates only DisMech. Either:

- Narrow the claim to a case study of DisMech; or
- Port the pattern to a second LinkML resource and report what transferred,
  what required local policy, and what did not generalize.

### Missing methods and publication package

- Define the unit of analysis: assertion, file, task, pull request, or agent
  run.
- Freeze agent versions, prompts/skills, models, tool permissions, and
  workflow configurations.
- Publish the evaluation corpus and injected-error suite.
- Add a statistical-analysis plan.
- Replace all 17 remaining reference placeholders.
- Produce the three figures and one failure-mode table from measured data.
- Resolve the journal and article type after the evaluation is designed.

## Boundary between the two papers

The papers will be stronger if they divide responsibility cleanly.

The content paper should own:

- The pathograph model.
- Resource scope and quantitative content.
- Mechanistic hypotheses and knowledge gaps.
- Pathophysiological reasoning evaluation.
- NAM and surrogate-endpoint use.
- Clinical and translational case studies.

The agentic paper should own:

- Curation workflow and human governance.
- Agent harnesses and scheduled workflows.
- Validation and provenance architecture.
- Failure-mode taxonomy.
- Controlled ablation and production-history results.
- Costs, throughput, and review burden.

The content paper should summarize validation in one box and cite the agentic
paper. The agentic paper should treat DisMech content only as the production
substrate and cite the content paper. This avoids publishing the same
validation-stack narrative twice.

## Recommended next milestone

Do not begin by polishing prose or filling the bibliography. First define the
shared empirical package:

1. Select and tag a frozen DisMech release.
2. Commit a reproducible resource-inventory analysis.
3. Design the pathophysiological-reasoning evaluation.
4. Design the agent-validator ablation and historical production analysis.
5. Select two or three shared case studies, with Fabry
   disease/surrogate-endpoint/NAM reasoning as the leading translational case.
6. Only then restructure the manuscripts around the resulting figures and
   tables.
