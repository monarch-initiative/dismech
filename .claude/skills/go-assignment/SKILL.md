---
name: go-assignment
description: >-
  Assess whether GO molecular-function, biological-process, and cellular-component
  assignments explain a dismech mechanism and are supported by the relevant
  experiments. Consult ai-gene-review (AIGR) gene reviews when useful, and prepare
  evidence-linked handoffs between the projects. For identifier/label repair
  alone, use dismech-terms.
---

# GO assignment with optional AIGR context

Produce a defensible assignment to a disease mechanism, including an explicit
gap when the molecular explanation is not known. A valid GO identifier is only
one part of that decision. Use the existing `dismech-terms` skill for ontology
lookups, descriptor placement, and validation, and `dismech-references` when
assessing or changing evidence. Follow the repository's ontology and evidence
contracts in `CLAUDE.md` and `docs/explanation/design-decisions.md`.

## Start from the assertion

For each proposed assignment, identify:

- The actor: gene product or complex, species, and relevant isoform or construct.
- The activity, process, or location asserted, and its cell/tissue context.
- What changes in disease, for which variant or perturbation, and how that was
  measured. Normal gene function alone does not establish the disease modifier.
- The experiment supporting the assertion, separated from the inference linking
  it to the disease phenotype.

Keep gene-product annotations and disease-node annotations distinct. AIGR may
support a normal function without establishing its loss in this disease; a
dismech node may describe a downstream process without asserting that the causal
gene product directly performs it. Do not copy every annotation of a causal gene
onto its disease node.

## Check the molecular explanation

For an enzyme, ask what reaction it catalyzes and what substrate is acted on.
For a kinase, distinguish the kinase, binding partner, phosphorylation substrate,
site (if established), and consequence. Record which of these are unknown;
an experimentally supported kinase activity does not require an identified
physiological substrate, but it does not fill that mechanistic gap either.

Binding to a kinase is an activity of the binding partner. It does not establish
kinase activation, inhibition, or phosphorylation. Co-complex recovery and
co-localization do not by themselves demonstrate direct physical binding.
Keep complex assembly, protein abundance/stability, catalytic activity, and
downstream process output separate when experiments distinguish them. Avoid
adding a generic binding term merely to give a molecular node a GO annotation.

For cellular components, inspect what was actually localized: endogenous protein,
tagged overexpression construct, heterologous protein, or artificially tethered
fusion. Use compartment definitions and relevant `is_a`/`part_of` relationships;
nearby compartments are not interchangeable. Localization alone does not prove
activity there or a causal role in degeneration of that structure.

For biological processes, distinguish participation from regulation and a
measured process defect from a phenotypic inference. Knockout/rescue may establish
a process requirement while leaving the intermediate molecular mechanism open.
Choose specificity supported by the experiment, retaining justified clinical
context in prose. Assess the modifier separately from the term.

## Consult AIGR without making it a dependency

Use an available AIGR checkout, GitHub read access, or raw files. The repository
is https://github.com/ai4curation/ai-gene-review. Discover the relevant gene/species
path; the current human pattern is
`genes/human/<SYMBOL>/<SYMBOL>-ai-review.yaml`, with adjacent `<SYMBOL>-notes.md`.
Confirm the record's gene identity, accession, and taxon rather than relying on
the filename. No clone, submodule, package dependency, or bulk mirror is needed.

When the user supplies a PR, read its current head and review discussion as well
as the changed gene records. Otherwise consult the default branch and check
relevant pending work when it could affect the decision. Record the commit SHA
actually inspected and whether it came from a pending PR or merged content.
An AIGR `status: COMPLETE` is not a statement that a PR is approved or merged.

Read `core_functions`, relevant `existing_annotations` with their `review`
decisions, original reference/evidence/qualifier/partner fields, and supporting
notes or reference reviews. Follow the current record/schema rather than
assuming an action vocabulary. Interpret decisions per annotation record:

- Acceptance does not automatically establish disease relevance.
- Removing an unsupported citation-specific annotation does not assert biological
  absence and does not justify a NOT annotation.
- Independent evidence can support a separate annotation without repairing the
  original record's provenance.
- Unresolved or disputed assignments are leads for investigation. Conflicts
  between notes, YAML decisions, and PR reviews need adjudication, not majority vote.

Trace important claims to primary experiments. AIGR and dismech citing the same
experiment are not independent corroboration. Provider reports are leads, not
substitutes for the source. Missing/inaccessible source material means that claim
is not verified; a successful validator run cannot establish semantic support.
Fetch dismech evidence through its own reference workflow rather than copying or
hand-authoring AIGR publication caches into `references_cache/`.

If AIGR has no review or cannot be accessed, continue with GO and primary sources
and state the limitation. Neither project needs to wait for the other to merge.

## Return a decision and a small handoff when useful

For an audit, report each material assignment as retain, refine, remove, or
unresolved, with the actor/context, proposed GO term and modifier, primary
evidence, and inference or remaining gap. These are report dispositions, not new
schema enum values. Separate label/namespace validity from biological adequacy.

When editing is requested, use existing dismech slots and history records;
do not invent AIGR foreign keys or import its review schema. Put AIGR commit/file
permalinks and relevant PR links in the history record's `links`, and explain
which conclusions were adopted or rejected in `details`. Disease evidence still
points to its primary sources.

When the review exposes a useful upstream question, draft a compact handoff:
gene/taxon; dismech file and node; exact GO assertion or annotation record;
primary reference and experiment; proposed change or unresolved question;
AIGR commit/file/PR links. Post or edit in AIGR only when requested or already
authorized; otherwise include the handoff in the response. No automatic issue
creation, cross-repository writes, or synchronization is implied by consultation.

## Motivating example

[AIGR PR 3044](https://github.com/ai4curation/ai-gene-review/pull/3044) reviews
human CFAP410 and NEK1. Consult its current state rather than treating it as a
fixed verdict. The reusable questions are whether a claim describes CFAP410's
association with NEK1, NEK1 catalysis on a demonstrated substrate, or a cellular
process requiring these proteins; and whether localization evidence distinguishes
the connecting cilium from the outer segment. Keep those assertions separate
even when they share a paper. Do not encode this PR's individual decisions as
universal annotation rules.
