# Alternative Model Discovery Template

## Target Disease
- **Disease Name:** {disease_name}
- **MONDO ID:** {mondo_id}

## Scope — Read This First

This is **not** a request for a general account of this disease. Its pathophysiology and clinical
features are already curated. The single question is narrow:

> **Which model systems, beyond the ones already curated, could be used to study the mechanisms
> this disease's pathograph records — and which specific pathograph nodes could each one
> legitimately support?**

What counts as an alternative model for this run:

{model_scope}

A report that returns models already listed below, or that proposes a model without naming the
pathograph node it serves, has failed this brief.

## What Is Already Curated — Do Not Re-Derive Any Of It

{existing_models}

Do not restate, re-justify or re-report these. Do not report that the existing models cluster in
some taxon or system — that is the premise of the question, not a finding.

## The Mechanism Nodes To Map Against

Any model you propose must be mapped to one or more of these nodes **by name**, exactly as
written. The right-hand column says whether any curated model is already linked to that node; a
node marked **no** is where an alternative model has the most to add, and several such nodes are
usually the point of the exercise.

{mechanism_nodes}

Nodes of greatest interest for this run:

{nodes_of_interest}

Where a node's scale is shown as **not stated**, treat the node's own description as the
authority on what level of organisation it sits at, and say in your answer which level you took
it to be.

## The Substitution Problem — Address It Directly, Do Not Evade It

A model is only useful here if it can host the mechanism the node describes. State plainly, for
every candidate, what the model cannot carry.

{substitution_constraint}

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

{systems_to_cover}

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
